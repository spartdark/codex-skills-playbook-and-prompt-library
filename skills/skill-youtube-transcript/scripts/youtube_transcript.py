#!/usr/bin/env python3
"""Extract available YouTube captions into a stable JSON transcript object."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import shutil
import re
import sys
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


class TranscriptError(Exception):
    def __init__(self, code: str, message: str, details: dict[str, Any] | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_video_id(source: str) -> str:
    try:
        parsed = urllib.parse.urlparse(source)
    except ValueError as exc:
        raise TranscriptError("invalid_youtube_url", "URL invalida o mal formada.") from exc

    host = (parsed.netloc or "").lower()
    host = host[4:] if host.startswith("www.") else host

    video_id = ""
    if host in {"youtube.com", "m.youtube.com", "music.youtube.com"}:
        if parsed.path == "/watch":
            video_id = urllib.parse.parse_qs(parsed.query).get("v", [""])[0]
        elif parsed.path.startswith(("/embed/", "/shorts/", "/live/")):
            video_id = parsed.path.split("/")[2] if len(parsed.path.split("/")) > 2 else ""
    elif host == "youtu.be":
        video_id = parsed.path.strip("/").split("/")[0]

    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id or ""):
        raise TranscriptError(
            "invalid_youtube_url",
            "La entrada no parece ser una URL de video de YouTube soportada.",
            {"source_url": source},
        )
    return video_id


def fetch_text(url: str, headers: dict[str, str] | None = None) -> str:
    request_headers = {"User-Agent": USER_AGENT}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 410, 451}:
            raise TranscriptError("video_restricted", "El video parece privado, restringido o no disponible.") from exc
        if exc.code == 404:
            raise TranscriptError("video_unavailable", "El video no esta disponible.") from exc
        raise TranscriptError("temporary_provider_failure", f"YouTube devolvio HTTP {exc.code}.") from exc
    except urllib.error.URLError as exc:
        raise TranscriptError("temporary_provider_failure", "Fallo temporal de red o proveedor.") from exc


def post_json(url: str, payload: dict[str, Any], headers: dict[str, str] | None = None) -> dict[str, Any]:
    request_headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    request_headers.update(headers or {})
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return json.loads(response.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        details: dict[str, Any] = {"http_status": exc.code}
        try:
            details["youtube_error"] = json.loads(body).get("error")
        except json.JSONDecodeError:
            details["body_preview"] = body[:300]
        raise TranscriptError("temporary_provider_failure", f"YouTube devolvio HTTP {exc.code}.", details) from exc
    except urllib.error.URLError as exc:
        raise TranscriptError("temporary_provider_failure", "Fallo temporal de red o proveedor.") from exc


def extract_balanced_json(text: str, marker: str) -> dict[str, Any]:
    start = text.find(marker)
    if start == -1:
        raise TranscriptError("video_unavailable", "No se encontro metadata reproducible del video.")

    brace_start = text.find("{", start)
    if brace_start == -1:
        raise TranscriptError("internal_error", "No se encontro el inicio del JSON de metadata.")

    depth = 0
    in_string = False
    escaped = False
    for index in range(brace_start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[brace_start : index + 1])

    raise TranscriptError("internal_error", "No se pudo leer el JSON de metadata del video.")


def get_watch_page(video_id: str) -> str:
    watch_url = f"https://www.youtube.com/watch?v={video_id}&hl=en"
    page = fetch_text(watch_url)
    if "This video is private" in page:
        raise TranscriptError("video_restricted", "El video es privado o requiere permisos.")
    return page


def get_player_response(video_id: str) -> dict[str, Any]:
    page = get_watch_page(video_id)
    return extract_balanced_json(page, "ytInitialPlayerResponse")


def caption_tracks(player_response: dict[str, Any]) -> list[dict[str, Any]]:
    captions = player_response.get("captions", {})
    renderer = captions.get("playerCaptionsTracklistRenderer", {})
    tracks = renderer.get("captionTracks", []) or []
    if not tracks:
        raise TranscriptError("transcript_unavailable", "No hay transcripcion disponible para este video.")
    return tracks


def track_label(track: dict[str, Any]) -> str:
    name = track.get("name", {})
    if isinstance(name, dict):
        runs = name.get("runs")
        if runs:
            return "".join(run.get("text", "") for run in runs)
        return name.get("simpleText", "")
    return ""


def summarize_track(track: dict[str, Any]) -> dict[str, Any]:
    return {
        "language": track.get("languageCode"),
        "label": track_label(track),
        "is_auto_generated": track.get("kind") == "asr",
        "is_translatable": bool(track.get("isTranslatable")),
    }


def ordered_tracks(
    tracks: list[dict[str, Any]], requested_language: str | None
) -> tuple[list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    priority = [requested_language, "es", "en"] if requested_language else ["es", "en"]
    priority = [item for item in priority if item]
    ordered: list[dict[str, Any]] = []

    for language in priority:
        for track in tracks:
            if track.get("languageCode", "").lower() == language.lower() and track not in ordered:
                ordered.append(track)

    for track in tracks:
        if track not in ordered:
            ordered.append(track)

    if requested_language and not any(
        track.get("languageCode", "").lower() == requested_language.lower() for track in tracks
    ):
        available = sorted({track.get("languageCode", "unknown") for track in tracks})
        warnings.append(
            "requested_language_unavailable: "
            f"'{requested_language}' no existe; se usara el primer fallback disponible. "
            f"Disponibles: {', '.join(available)}."
        )

    return ordered, warnings


def with_query_param(url: str, key: str, value: str) -> str:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    query[key] = [value]
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query, doseq=True)))


def parse_json3_caption(raw: str) -> list[dict[str, Any]]:
    data = json.loads(raw)
    segments: list[dict[str, Any]] = []
    for event in data.get("events", []):
        parts = event.get("segs") or []
        text = normalize_text("".join(part.get("utf8", "") for part in parts))
        if not text:
            continue
        segments.append(
            {
                "start": round((event.get("tStartMs") or 0) / 1000, 3),
                "duration": round((event.get("dDurationMs") or 0) / 1000, 3),
                "text": text,
            }
        )
    return segments


def parse_xml_caption(raw: str) -> list[dict[str, Any]]:
    root = ET.fromstring(raw)
    segments: list[dict[str, Any]] = []
    for item in root.findall(".//text"):
        text = normalize_text("".join(item.itertext()))
        if not text:
            continue
        segments.append(
            {
                "start": round(float(item.attrib.get("start", "0")), 3),
                "duration": round(float(item.attrib.get("dur", "0")), 3),
                "text": text,
            }
        )
    return segments


def parse_timestamp(value: str) -> float:
    match = re.match(r"(?:(\d+):)?(\d{2}):(\d{2})[.,](\d{3})", value.strip())
    if not match:
        return 0
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    millis = int(match.group(4))
    return hours * 3600 + minutes * 60 + seconds + millis / 1000


def parse_vtt_caption(raw: str) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    blocks = re.split(r"\n\s*\n", raw.replace("\r\n", "\n"))
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        timing_index = next((i for i, line in enumerate(lines) if "-->" in line), -1)
        if timing_index == -1:
            continue
        start_raw, end_raw = lines[timing_index].split("-->", 1)
        start = parse_timestamp(start_raw)
        end = parse_timestamp(end_raw.split()[0])
        text = normalize_text(" ".join(re.sub(r"<[^>]+>", "", line) for line in lines[timing_index + 1 :]))
        if not text:
            continue
        segments.append({"start": round(start, 3), "duration": round(max(0, end - start), 3), "text": text})
    return segments


def language_candidates(requested_language: str | None) -> list[str]:
    values = [requested_language, "es", "en"] if requested_language else ["es", "en"]
    return [item for item in values if item]


def fetch_ytdlp_segments(
    source_url: str,
    requested_language: str | None,
    po_token: str | None = None,
    cookies_from_browser: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    executable = shutil.which("yt-dlp")
    command_prefix = [executable] if executable else [sys.executable, "-m", "yt_dlp"]

    with tempfile.TemporaryDirectory(prefix="youtube-transcript-") as tmp:
        output_template = str(Path(tmp) / "%(id)s.%(ext)s")
        command = [
            *command_prefix,
            "--skip-download",
            "--write-sub",
            "--write-auto-sub",
            "--sub-format",
            "vtt",
            "--sub-langs",
            ",".join(language_candidates(requested_language)),
            "--output",
            output_template,
            source_url,
        ]
        if po_token:
            command.extend(["--extractor-args", f"youtube:po_token=web.subs+{po_token}"])
        if cookies_from_browser:
            command.extend(["--cookies-from-browser", cookies_from_browser])

        completed = subprocess.run(command, text=True, capture_output=True, timeout=60, check=False)
        if completed.returncode != 0 and "No module named yt_dlp" in completed.stderr:
            raise TranscriptError(
                "optional_dependency_unavailable",
                "yt-dlp no esta instalado; se omitio este fallback.",
                {"strategy": "yt-dlp"},
            )
        if completed.returncode != 0:
            code = "po_token_required" if "PO token" in completed.stderr else "temporary_provider_failure"
            raise TranscriptError(
                code,
                "yt-dlp no pudo obtener captions.",
                {
                    "strategy": "yt-dlp",
                    "returncode": completed.returncode,
                    "stderr_preview": completed.stderr[-600:],
                    "po_token_used": bool(po_token),
                    "cookies_from_browser_used": bool(cookies_from_browser),
                },
            )

        files = sorted(Path(tmp).glob("*.vtt"))
        for file_path in files:
            raw = file_path.read_text(encoding="utf-8", errors="replace")
            segments = parse_vtt_caption(raw)
            if segments:
                return segments, {
                    "strategy": "yt-dlp",
                    "file": file_path.name,
                    "language": detect_language_from_subtitle_filename(file_path.name),
                }

    raise TranscriptError(
        "po_token_required",
        "yt-dlp no produjo subtitulos utiles; YouTube puede requerir PO token para captions automaticos.",
        {
            "strategy": "yt-dlp",
            "po_token_used": bool(po_token),
            "cookies_from_browser_used": bool(cookies_from_browser),
        },
    )


def detect_language_from_subtitle_filename(name: str) -> str | None:
    parts = name.split(".")
    if len(parts) >= 3:
        return parts[-2]
    return None


def extract_page_config(page: str) -> dict[str, str]:
    config: dict[str, str] = {}
    for key in ("INNERTUBE_API_KEY", "INNERTUBE_CLIENT_VERSION", "VISITOR_DATA"):
        match = re.search(rf'"{key}":"([^"]+)"', page)
        if match:
            config[key] = match.group(1)
    return config


def transcript_params(page: str) -> list[str]:
    return re.findall(r'"getTranscriptEndpoint":\{"params":"([^"]+)"\}', page)


def text_from_runs(value: dict[str, Any]) -> str:
    if not isinstance(value, dict):
        return ""
    if "simpleText" in value:
        return normalize_text(value.get("simpleText", ""))
    runs = value.get("runs") or []
    return normalize_text("".join(run.get("text", "") for run in runs))


def walk_json(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)


def parse_youtubei_transcript(data: dict[str, Any]) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    for node in walk_json(data):
        renderer = node.get("transcriptSegmentRenderer")
        if not isinstance(renderer, dict):
            continue
        text = text_from_runs(renderer.get("snippet", {}))
        if not text:
            continue
        start_ms = renderer.get("startMs")
        end_ms = renderer.get("endMs")
        try:
            start = int(start_ms) / 1000 if start_ms is not None else 0
            duration = max(0, (int(end_ms) - int(start_ms)) / 1000) if end_ms and start_ms else 0
        except (TypeError, ValueError):
            start = 0
            duration = 0
        segments.append({"start": round(start, 3), "duration": round(duration, 3), "text": text})
    return segments


def fetch_youtubei_segments(page: str, video_id: str) -> list[dict[str, Any]]:
    config = extract_page_config(page)
    params = transcript_params(page)
    missing = [key for key in ("INNERTUBE_API_KEY", "INNERTUBE_CLIENT_VERSION") if key not in config]
    if missing or not params:
        raise TranscriptError(
            "temporary_provider_failure",
            "No se encontro configuracion completa para youtubei/get_transcript.",
            {"missing": missing, "has_transcript_params": bool(params)},
        )

    endpoint = f"https://www.youtube.com/youtubei/v1/get_transcript?key={config['INNERTUBE_API_KEY']}"
    headers = {
        "Origin": "https://www.youtube.com",
        "Referer": f"https://www.youtube.com/watch?v={video_id}",
        "X-YouTube-Client-Name": "1",
        "X-YouTube-Client-Version": config["INNERTUBE_CLIENT_VERSION"],
    }
    last_error: TranscriptError | None = None
    for item in params:
        payload = {
            "context": {
                "client": {
                    "clientName": "WEB",
                    "clientVersion": config["INNERTUBE_CLIENT_VERSION"],
                    **({"visitorData": config["VISITOR_DATA"]} if "VISITOR_DATA" in config else {}),
                }
            },
            "params": item,
        }
        try:
            data = post_json(endpoint, payload, headers)
            segments = parse_youtubei_transcript(data)
            if segments:
                return segments
            last_error = TranscriptError(
                "transcript_unavailable",
                "youtubei/get_transcript respondio sin segmentos utiles.",
                {"strategy": "youtubei"},
            )
        except TranscriptError as exc:
            exc.details = {**exc.details, "strategy": "youtubei"}
            last_error = exc

    raise last_error or TranscriptError("temporary_provider_failure", "youtubei/get_transcript no devolvio texto.")


def fetch_segments(track: dict[str, Any]) -> list[dict[str, Any]]:
    base_url = track.get("baseUrl")
    if not base_url:
        raise TranscriptError("transcript_unavailable", "La transcripcion no incluye una URL de captions.")

    raw = fetch_text(with_query_param(base_url, "fmt", "json3"))
    if not raw.strip():
        raw = fetch_text(base_url)
        if not raw.strip():
            raise TranscriptError(
                "temporary_provider_failure",
                "YouTube anuncio captions, pero el endpoint timedtext devolvio una respuesta vacia.",
                {
                    "language": track.get("languageCode"),
                    "is_auto_generated": track.get("kind") == "asr",
                    "hint": "YouTube puede requerir Proof of Origin token o haber cambiado el acceso a captions.",
                },
            )

    try:
        segments = parse_json3_caption(raw)
    except (json.JSONDecodeError, TypeError, ValueError):
        raw = fetch_text(base_url)
        try:
            segments = parse_xml_caption(raw)
        except (ET.ParseError, TypeError, ValueError) as exc:
            raise TranscriptError("internal_error", "No se pudo parsear el formato de transcripcion.") from exc

    if not segments:
        raise TranscriptError("transcript_unavailable", "La transcripcion existe pero no contiene texto util.")
    return segments


def build_transcript(
    source_url: str,
    requested_language: str | None,
    po_token: str | None = None,
    cookies_from_browser: str | None = None,
) -> dict[str, Any]:
    video_id = extract_video_id(source_url)
    page = get_watch_page(video_id)
    player = extract_balanced_json(page, "ytInitialPlayerResponse")
    details = player.get("videoDetails", {})
    status = player.get("playabilityStatus", {})
    if status.get("status") not in {None, "OK"}:
        reason = status.get("reason") or "El video no esta disponible para reproduccion."
        code = "video_restricted" if "private" in reason.lower() or "sign in" in reason.lower() else "video_unavailable"
        raise TranscriptError(code, reason, {"video_id": video_id})

    tracks, warnings = ordered_tracks(caption_tracks(player), requested_language)
    last_error: TranscriptError | None = None
    selected_track: dict[str, Any] | None = None
    selected_strategy = "timedtext"
    selected_language: str | None = None
    segments: list[dict[str, Any]] = []
    for candidate in tracks:
        try:
            segments = fetch_segments(candidate)
            selected_track = candidate
            selected_language = candidate.get("languageCode")
            break
        except TranscriptError as exc:
            last_error = exc
            exc.details = {
                **exc.details,
                "source_url": source_url,
                "video_id": video_id,
                "title": details.get("title"),
                "channel": details.get("author"),
                "attempted_track": summarize_track(candidate),
                "available_tracks": [summarize_track(track) for track in tracks],
            }
            if exc.code == "transcript_unavailable":
                continue
            if exc.code == "temporary_provider_failure":
                try:
                    segments = fetch_youtubei_segments(page, video_id)
                    selected_track = candidate
                    selected_strategy = "youtubei"
                    selected_language = candidate.get("languageCode")
                    warnings.append("timedtext_empty_used_youtubei_fallback")
                    break
                except TranscriptError as youtubei_error:
                    exc.details["youtubei_fallback_error"] = {
                        "code": youtubei_error.code,
                        "message": youtubei_error.message,
                        "details": youtubei_error.details,
                    }
                try:
                    segments, ytdlp_details = fetch_ytdlp_segments(
                        source_url,
                        requested_language,
                        po_token=po_token,
                        cookies_from_browser=cookies_from_browser,
                    )
                    selected_track = candidate
                    selected_strategy = "yt-dlp"
                    selected_language = ytdlp_details.get("language") or candidate.get("languageCode")
                    warnings.append("timedtext_empty_used_ytdlp_fallback")
                    break
                except TranscriptError as ytdlp_error:
                    exc.details["ytdlp_fallback_error"] = {
                        "code": ytdlp_error.code,
                        "message": ytdlp_error.message,
                        "details": ytdlp_error.details,
                    }
                raise
            else:
                raise

    if selected_track is None:
        raise last_error or TranscriptError("transcript_unavailable", "No hay transcripcion disponible.")

    track = selected_track
    plain_text = "\n".join(segment["text"] for segment in segments)

    return {
        "source_url": source_url,
        "video_id": video_id,
        "title": details.get("title"),
        "channel": details.get("author"),
        "language": selected_language,
        "is_auto_generated": track.get("kind") == "asr",
        "retrieved_at": utc_now(),
        "segments": segments,
        "plain_text": plain_text,
        "warnings": warnings,
        "caption_track": {
            "label": track_label(track),
            "is_translatable": bool(track.get("isTranslatable")),
        },
        "extraction_strategy": selected_strategy,
    }


def diagnose_video(source_url: str) -> dict[str, Any]:
    video_id = extract_video_id(source_url)
    player = get_player_response(video_id)
    details = player.get("videoDetails", {})
    status = player.get("playabilityStatus", {})
    tracks = caption_tracks(player)
    return {
        "source_url": source_url,
        "video_id": video_id,
        "title": details.get("title"),
        "channel": details.get("author"),
        "playability_status": status.get("status"),
        "playability_reason": status.get("reason"),
        "caption_tracks": [summarize_track(track) for track in tracks],
        "optional_fallbacks": {
            "yt_dlp_available": bool(shutil.which("yt-dlp")),
            "yt_dlp_module_available": is_ytdlp_module_available(),
            "po_token_env_present": bool(os.environ.get("YOUTUBE_PO_TOKEN")),
        },
        "retrieved_at": utc_now(),
        "warnings": [
            "Diagnostico solamente: no se descargo video ni audio.",
            "La presencia de caption_tracks no garantiza que timedtext entregue texto.",
            "Si yt-dlp esta instalado, la extraccion normal puede intentar ese fallback sin descargar video/audio.",
        ],
    }


def is_ytdlp_module_available() -> bool:
    try:
        __import__("yt_dlp")
        return True
    except ImportError:
        return False


def error_payload(error: TranscriptError) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "error": {
            "code": error.code,
            "message": error.message,
            "details": error.details,
            "retrieved_at": utc_now(),
        }
    }
    for key in ("source_url", "video_id", "title", "channel"):
        if key in error.details:
            payload[key] = error.details[key]
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract a public YouTube transcript as structured JSON.")
    parser.add_argument("url", help="YouTube video URL.")
    parser.add_argument("--language", "-l", help="Preferred transcript language code, for example es or en.")
    parser.add_argument("--output", "-o", help="Optional file path for the JSON result.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    parser.add_argument("--diagnose", action="store_true", help="Return video/caption metadata without fetching text.")
    parser.add_argument("--po-token", help="Optional YouTube PO token for yt-dlp subtitle fallback.")
    parser.add_argument("--cookies-from-browser", help="Optional browser name/profile for yt-dlp cookies, for example chrome.")
    args = parser.parse_args()

    try:
        po_token = args.po_token or os.environ.get("YOUTUBE_PO_TOKEN")
        payload = (
            diagnose_video(args.url)
            if args.diagnose
            else build_transcript(
                args.url,
                args.language,
                po_token=po_token,
                cookies_from_browser=args.cookies_from_browser,
            )
        )
        exit_code = 0
    except TranscriptError as exc:
        payload = error_payload(exc)
        exit_code = 1
    except Exception as exc:  # pragma: no cover - defensive CLI boundary.
        payload = error_payload(TranscriptError("internal_error", str(exc)))
        exit_code = 1

    rendered = json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered + "\n")
    print(rendered)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
