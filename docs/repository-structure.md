# Repository Structure

## Principios

La estructura del repositorio prioriza:

- descubribilidad;
- instalación simple;
- versionado explícito;
- documentación legible;
- independencia de cada skill.

## Directorios

- `skills/`: skills públicas listas para instalar.
- `templates/`: bases reutilizables para crear nuevas skills o iniciar proyectos AI-first.
- `templates/project-ai-starter/`: plantilla portable con `AGENTS.md`, perfil de proyecto y memoria minima para repos nuevos o existentes.
- `install/`: documentación para instalación, quickstart y compatibilidad.
- `docs/`: políticas del repositorio.
- `docs/ai/`: gobernanza de agentes, memoria, evidencia y adopción token-light.
- `knowledge/`: memoria local, evidencia y aprendizajes derivados.

## Archivos raíz

- `AGENTS.md`: punto de entrada operativo para Codex y otros agentes.
- `README.md`: entrada principal del proyecto.
- `LICENSE`: licencia MIT.
- `VERSION`: versión global del repo.
- `catalog.json`: catálogo instalable de skills.
- `CHANGELOG.md`: historial global.
- `CONTRIBUTING.md`: guía para contribuciones.

## Decisión de diseño

Cada skill mantiene su propia documentación y changelog para permitir releases ordenadas, revisiones claras y distribución individual sin depender del contexto completo del repositorio.
