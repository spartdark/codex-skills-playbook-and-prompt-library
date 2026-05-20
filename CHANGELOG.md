# Changelog

Todos los cambios relevantes de este repositorio se documentan aquí.

El formato sigue una variante legible de [Keep a Changelog](https://keepachangelog.com/) y el proyecto usa versionado semántico.

## [0.5.0] - 2026-05-20

### Added

- nueva skill `skill-codex-engineering-pre-read` para preparar pre-reads tecnicos con Codex antes de planear, implementar o automatizar;
- assets portables con guia de pre-read, guia practica de Codex y templates de prompt briefs;
- ejemplo de pre-read semanal y prompts para forzar evidencia y convertir recomendaciones en tareas.

### Changed

- version del repositorio actualizada a `0.5.0`.

## [0.4.0] - 2026-05-19

### Added

- nuevo PRD `reddit-ai-researcher-plugin` para convertir Reddit en senales accionables de IA, software, producto, monetizacion y mejora de procesos;
- nuevo plugin publico experimental `reddit-ai-researcher` con skill empaquetada, prompt guide, checklist y ejemplo;
- documentacion base para tratar Reddit como fuente cualitativa de senales, no como validacion definitiva.

### Changed

- version del repositorio actualizada a `0.4.0`.

## [0.3.0] - 2026-05-19

### Added

- nueva skill `skill-intent-spec-context-generation-validation` para transformar ideas AI-first en PRDs validables con gates obligatorios;
- nueva skill `skill-intent-spec-context-generation-validation-en` en ingles para producto AI-first y validacion por gates;
- metadatos, ejemplo y checklist publico para la version inglesa de ISCGV.

### Changed

- version del repositorio actualizada a `0.3.0`;
- posicionamiento visible de la skill refinado a `ISCGV++ Product Operating System`;
- metadata publica alineada con el framework ISCGV++ y su sistema de auditoria y scoring.

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
