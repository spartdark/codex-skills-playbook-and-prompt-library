---
name: youtube-transcript
description: Extrae, valida y normaliza transcripciones disponibles de videos publicos de YouTube como fuente trazable para investigacion, documentacion, producto, apps, IA o monetizacion. Usala cuando el usuario comparta una URL de YouTube y necesite obtener transcript con timestamps, metadatos, idioma, advertencias y errores explicitos antes de analizar o sintetizar el contenido.
---

# YouTube Transcript

## Mision

Traer la fuente al agente: obtener una transcripcion publica disponible de YouTube, normalizarla y devolverla como JSON estructurado sin inventar contenido ni hacer analisis semantico por cuenta propia.

## Flujo operativo

1. Valida que la entrada sea una URL soportada de YouTube.
2. Extrae el `video_id` y conserva la URL original como `source_url`.
3. Ejecuta `scripts/youtube_transcript.py` para obtener captions disponibles.
4. Prefiere idioma solicitado; si no existe, usa espanol, ingles o la primera transcripcion disponible.
5. Entrega `source_url`, `video_id`, `title`, `channel`, `language`, `is_auto_generated`, `segments`, `plain_text`, `retrieved_at` y `warnings`.
6. Cita siempre la URL fuente en cualquier respuesta posterior basada en la transcripcion.

## Uso del script

```bash
python3 scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --language es --pretty
```

Para guardar resultados largos:

```bash
python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --output transcript.json --pretty
```

Para generar automaticamente un nombre legible basado en canal, titulo, video id e idioma:

```bash
python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --output auto --pretty
```

Tambien puedes pasar una carpeta; la skill guardara ahi el JSON con nombre natural:

```bash
python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --output transcripts/ --pretty
```

Para diagnosticar un fallo sin intentar extraer texto:

```bash
python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --diagnose --pretty
```

Cuando YouTube requiera Proof of Origin token para captions automaticos, provee el token a traves de `--po-token` o `YOUTUBE_PO_TOKEN`:

```bash
YOUTUBE_PO_TOKEN="TOKEN" python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --language en --pretty
```

Tambien puedes permitir que `yt-dlp` use cookies de un navegador local, solo cuando el usuario lo autorice explicitamente:

```bash
python3 scripts/youtube_transcript.py "https://youtu.be/VIDEO_ID" --language en --cookies-from-browser chrome --pretty
```

## Errores esperados

- `invalid_youtube_url`: la entrada no es una URL de video soportada.
- `video_unavailable`: el video no esta disponible.
- `video_restricted`: el video es privado, restringido o requiere permisos.
- `transcript_unavailable`: no existe transcripcion publica disponible.
- `temporary_provider_failure`: fallo temporal de red o proveedor.
- `po_token_required`: YouTube bloquea captions automaticos sin PO token.
- `internal_error`: fallo inesperado al extraer o parsear.

Si `caption_tracks` existe pero `timedtext` devuelve vacio, reporta `temporary_provider_failure` con metadata del video y tracks disponibles. No lo conviertas en `transcript_unavailable`: la transcripcion esta anunciada, pero el proveedor no entrego el texto por la ruta actual.

Si `ytdlp_fallback_error.code` es `po_token_required`, pide un PO token o autorizacion explicita para usar cookies del navegador. No intentes saltarte el bloqueo.

## Guardrails

- Recuerda que la API oficial de YouTube para descargar captions requiere autorizacion sobre el video; para videos ajenos, esta skill solo intenta captions publicos expuestos al reproductor.
- No descargues video ni audio.
- No uses speech-to-text como fallback dentro del MVP.
- No intentes evadir privacidad, login, paywalls, regiones ni restricciones.
- No completes huecos ni reconstruyas frases que no esten en la transcripcion.
- Separa lo que aparece en la fuente de cualquier inferencia o recomendacion.
- Si el usuario pide analisis, primero obten la transcripcion y despues usa una skill de investigacion o producto.

## Referencias internas

- `scripts/youtube_transcript.py` para extraccion y normalizacion.
- `prompt.md` para principios de uso como capa tecnica.
- `examples/example-1.md` para un flujo de extraccion simple.
- `assets/error-taxonomy.md` para clasificar fallos de forma consistente.
