# YouTube Transcript Plugin Improvements

Objetivo: convertir los fallos observados al extraer captions en trabajo ejecutable para mejorar la skill/plugin `youtube-transcript`.

## Fuente del problema

- Video: [Master 97% of Codex in 1 Hour](https://www.youtube.com/watch?v=3TdD8Qv5Tk8)
- Evidencia local: [transcript failure JSON](../../knowledge/raw/youtube/youtube-transcript-nate-herk-ai-automation-master-97-of-codex-in-1-hour-full-course-3TdD8Qv5Tk8-en.json)
- Nota procesada: [transcript unavailable](../../knowledge/processed/transcripts/youtube-nate-herk-master-97-codex-3TdD8Qv5Tk8-transcript-unavailable.md)
- Fecha de captura: 2026-05-21

## Issues detectados

### YT-TX-001: Caption track anunciado, pero `timedtext` devuelve vacio

- Severidad: alta
- Observado: YouTube expuso un track `English (auto-generated)`, pero el endpoint `timedtext` devolvio una respuesta vacia.
- Impacto: el flujo actual no puede producir transcripcion primaria aunque el video anuncie captions.
- Hipotesis: YouTube requiere Proof of Origin token, cambio de acceso a captions o parametros adicionales de player/client.
- Evidencia: `error.code = temporary_provider_failure`, `message = YouTube anuncio captions, pero el endpoint timedtext devolvio una respuesta vacia`.
- Criterio de aceptacion: el plugin debe clasificar este caso como recuperable, preservar metadata/tracks y sugerir retry con PO token o cookies autorizadas sin degradarlo a `transcript_unavailable`.

### YT-TX-002: YouTubei fallback falla con `FAILED_PRECONDITION`

- Severidad: alta
- Observado: fallback YouTubei devolvio HTTP 400 con status `FAILED_PRECONDITION`.
- Impacto: no hay segunda ruta efectiva cuando `timedtext` falla.
- Hipotesis: falta PO token o faltan parametros actualizados de cliente/contexto.
- Evidencia: `youtubei_fallback_error.details.youtube_error.status = FAILED_PRECONDITION`.
- Criterio de aceptacion: el plugin debe mapear explicitamente `FAILED_PRECONDITION` a una accion sugerida: PO token, cookies autorizadas o retry diferido, segun corresponda.

### YT-TX-003: `yt-dlp` fallback recibe HTTP 429

- Severidad: media
- Observado: `yt-dlp` no pudo obtener captions por HTTP 429 `Too Many Requests`.
- Impacto: el fallback puede fallar por rate limit aunque existan captions.
- Hipotesis: YouTube limita solicitudes anonimas; se requiere backoff, cache, PO token o cookies con autorizacion explicita.
- Evidencia: `ytdlp_fallback_error.details.stderr_preview` incluye `HTTP Error 429: Too Many Requests`.
- Criterio de aceptacion: el plugin debe distinguir rate limit de ausencia real de transcript, registrar retry-after si existe y evitar reintentos agresivos inmediatos.

### YT-TX-004: Posible inconsistencia de idioma en fallback

- Severidad: media
- Observado: la metadata indica `language: en`, pero el stderr de `yt-dlp` dice que no pudo obtener subtitulos para `es`.
- Impacto: puede ocultar captions disponibles si el fallback intenta un idioma diferente al track seleccionado.
- Hipotesis: el orden de preferencia `es -> en -> first available` o traduccion automatica esta afectando el comando de fallback.
- Evidencia: JSON de fallo muestra `language = en` y `attempted_track.language = en`, pero `stderr_preview` menciona `subtitles for 'es'`.
- Criterio de aceptacion: agregar logging del comando efectivo de fallback y tests que aseguren que el idioma intentado coincide con el track seleccionado, salvo que se haya pedido traduccion explicitamente.

### YT-TX-005: Warnings de entorno mezclados con causa raiz

- Severidad: baja
- Observado: stderr incluye warnings de EJS, ffmpeg e impersonation junto al error real.
- Impacto: complica diagnostico automatico y puede distraer del bloqueo principal.
- Hipotesis: el plugin guarda un preview crudo de stderr sin extraer causa raiz.
- Evidencia: `stderr_preview` contiene warnings antes de `ERROR: Unable to download video subtitles`.
- Criterio de aceptacion: guardar stderr completo en raw evidence si es necesario, pero extraer campos estructurados: `root_error`, `http_status`, `environment_warnings`.

## Propuesta de mejora

1. Agregar una taxonomia de fallo mas fina:
   - `caption_track_empty`
   - `po_token_or_precondition_required`
   - `rate_limited`
   - `language_fallback_mismatch`
   - `environment_warning`
2. Guardar `available_tracks`, `attempted_track`, estrategia usada, idioma efectivo y accion recomendada en todos los fallos.
3. Agregar fixture de este fallo como test de regresion.
4. Documentar retry seguro:
   - retry diferido para 429;
   - PO token cuando el usuario lo provea;
   - cookies de navegador solo con autorizacion explicita;
   - no descargar audio/video ni usar speech-to-text como fallback.

## Done when

- Existe al menos un test de regresion basado en este JSON de fallo.
- La salida del plugin separa causa raiz, warnings de entorno y accion recomendada.
- El fallback de idioma queda auditado con logs o campos estructurados.
- `temporary_provider_failure` conserva evidencia suficiente para reintentar sin perder metadata.
- La documentacion de `youtube-transcript` explica que un track anunciado no equivale a transcript recuperado.
