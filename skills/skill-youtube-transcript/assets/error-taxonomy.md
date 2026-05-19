# Error Taxonomy

Usa estos codigos de error al comunicar fallos de extraccion:

- `invalid_youtube_url`: la URL no corresponde a un video de YouTube soportado o no contiene un `video_id` valido.
- `video_unavailable`: YouTube indica que el video no existe o no puede reproducirse.
- `video_restricted`: el video es privado, restringido, requiere login o no esta disponible publicamente.
- `transcript_unavailable`: el video no expone captions publicos o los captions no contienen texto util.
- `temporary_provider_failure`: fallo de red, timeout o respuesta vacia del proveedor aunque existan captions anunciados.
- `po_token_required`: YouTube requiere Proof of Origin token o cookies autorizadas para entregar captions automaticos.
- `internal_error`: bug o caso no esperado dentro del extractor.

No conviertas un error en resumen. Explica el fallo y pide una URL alternativa o una transcripcion proporcionada por el usuario.

Cuando `temporary_provider_failure` incluya `available_tracks`, tratala como fallo de acceso al proveedor, no como ausencia de captions. El siguiente paso practico es diagnosticar, probar otra ruta autorizada o pedir la transcripcion al usuario.

Cuando aparezca `po_token_required`, el siguiente paso practico es pedir al usuario un PO token, usar `YOUTUBE_PO_TOKEN`, o solicitar autorizacion explicita para `--cookies-from-browser`.
