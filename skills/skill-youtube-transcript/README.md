# YouTube Transcript

Skill publica para obtener transcripciones disponibles de videos de YouTube como fuente estructurada y trazable.

## Que cubre

- validacion de URLs de YouTube;
- extraccion de `video_id`;
- seleccion de idioma con fallback;
- metadatos basicos del video;
- segmentos con timestamps;
- texto plano normalizado;
- errores explicitos cuando no hay transcripcion o acceso.

Nota: la API oficial de YouTube para descargar captions requiere autorizacion sobre el video. Esta skill usa captions publicos expuestos al reproductor cuando estan disponibles y falla de forma explicita si YouTube devuelve respuestas vacias o restringidas.

## Casos de uso

- "Extrae la transcripcion de este video y citame la fuente".
- "Dame el transcript en espanol si existe; si no, usa ingles".
- "Prepara la fuente para que otra skill analice ideas de apps o monetizacion".

## Instalacion

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-youtube-transcript "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Uso directo del script

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language es \
  --pretty
```

Guardar con nombre natural:

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language es \
  --output auto \
  --pretty
```

O guardar dentro de una carpeta con nombre generado automaticamente:

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language es \
  --output transcripts/ \
  --pretty
```

Diagnosticar captions sin extraer texto:

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --diagnose \
  --pretty
```

Fallbacks avanzados para captions automaticos protegidos por YouTube:

```bash
YOUTUBE_PO_TOKEN="TOKEN" python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language en \
  --pretty
```

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language en \
  --cookies-from-browser chrome \
  --pretty
```

Estos fallbacks usan `yt-dlp` solo para subtitulos y mantienen `--skip-download`; no descargan video ni audio.

## Contenido

- `SKILL.md`: flujo operativo y guardrails.
- `prompt.md`: rol tecnico y limites.
- `scripts/youtube_transcript.py`: extractor sin dependencias externas.
- `examples/`: ejemplo de uso.
- `assets/`: taxonomia de errores.
