# YouTube Transcript Plugin

Plugin local para Codex que empaqueta la skill `youtube-transcript` y su script de extraccion de captions publicos de YouTube.

## Capacidades

- Extraer transcripciones publicas disponibles desde URLs de YouTube.
- Normalizar salida como JSON con `source_url`, `video_id`, metadatos, segmentos, timestamps, `plain_text` y advertencias.
- Preferir idioma solicitado y usar fallbacks a espanol, ingles o primera transcripcion disponible.
- Guardar resultados con nombre natural usando canal, titulo, idioma y `video_id`.
- Diagnosticar captions disponibles sin descargar audio o video.
- Reportar errores explicitos como URL invalida, video restringido, transcripcion ausente, fallo temporal o PO token requerido.

## Uso desde la skill

```bash
python3 skills/skill-youtube-transcript/scripts/youtube_transcript.py \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  --language es \
  --output auto \
  --pretty
```

## Guardrails

- No descarga audio ni video.
- No usa speech-to-text como fallback.
- No evade privacidad, login, paywalls, regiones ni restricciones.
- No inventa texto ausente de la transcripcion.
- Conserva timestamps para que otras skills puedan citar fuente o detectar prompts mencionados en el video.

