# Changelog

Todos los cambios relevantes de este repositorio se documentan aquí.

El formato sigue una variante legible de [Keep a Changelog](https://keepachangelog.com/) y el proyecto usa versionado semántico.

## [0.2.0] - 2026-05-18

### Added

- nueva skill `skill-youtube-transcript` para extraer y normalizar transcripciones publicas de YouTube;
- script sin dependencias externas para obtener captions, preservar timestamps, elegir idioma con fallback y devolver JSON estructurado;
- taxonomia de errores para URLs invalidas, videos restringidos, transcripciones no disponibles y fallos temporales.

## [0.1.0] - 2026-03-26

### Added

- estructura pública inicial del repositorio para distribución de skills de Codex;
- catálogo instalable `catalog.json` con metadatos de tres skills públicas;
- documentación de instalación, compatibilidad, versionado, naming y publicación;
- template reutilizable para nuevas skills;
- tres skills iniciales: Git & GitHub Expert, RAG Research y SDD Architect.
