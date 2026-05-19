# Changelog

Todos los cambios relevantes de esta skill se documentan aqui.

## [0.1.1] - 2026-05-18

### Added

- fallback `youtubei/get_transcript` antes de declarar fallo definitivo de proveedor;
- fallback opcional con `yt-dlp` para descargar solo subtitulos con `--skip-download`;
- soporte para `--po-token`, `YOUTUBE_PO_TOKEN` y `--cookies-from-browser` cuando YouTube requiere Proof of Origin token;
- error `po_token_required` para distinguir captions automaticos bloqueados de transcripciones inexistentes.

### Changed

- el diagnostico ahora reporta disponibilidad de `yt-dlp`, modulo `yt_dlp` y presencia de `YOUTUBE_PO_TOKEN`.

## [0.1.0] - 2026-05-18

### Added

- primera version de `skill-youtube-transcript`;
- script `youtube_transcript.py` para validar URLs, extraer captions y devolver JSON estructurado;
- fallback de idioma: solicitado, espanol, ingles o primera transcripcion disponible;
- taxonomia inicial de errores, incluyendo respuestas vacias del proveedor, y ejemplo de uso.

### Changed

- el error de captions anunciados pero vacios ahora incluye metadata del video, track intentado y tracks disponibles;
- se agrego modo `--diagnose` para inspeccionar captions sin intentar descargar texto.
