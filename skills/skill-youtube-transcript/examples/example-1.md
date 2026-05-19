# Example 1

## Solicitud

"Extrae la transcripcion de `https://www.youtube.com/watch?v=VIDEO_ID` en espanol si esta disponible."

## Ejecucion sugerida

```bash
python3 scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --language es --pretty
```

Para guardar el resultado con nombre amigable:

```bash
python3 scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --language es --output auto --pretty
```

## Resultado

La skill devuelve un objeto JSON con:

- URL fuente;
- `video_id`;
- titulo y canal si estan disponibles;
- idioma elegido;
- segmentos con timestamps;
- `plain_text`;
- advertencias de fallback si el idioma solicitado no existe.
- `saved_to` cuando se uso `--output`.

Si no hay captions disponibles, devuelve `transcript_unavailable` sin inventar contenido.

Si YouTube anuncia captions pero devuelve texto vacio, ejecuta:

```bash
python3 scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --diagnose --pretty
```

Usa el diagnostico para decidir si pedir otra URL, una transcripcion pegada por el usuario o una fase posterior con speech-to-text.

Si el fallo indica `po_token_required`, reintenta con un token:

```bash
YOUTUBE_PO_TOKEN="TOKEN" python3 scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID" --language en --pretty
```
