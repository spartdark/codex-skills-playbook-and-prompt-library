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
- `templates/`: base reutilizable para crear nuevas skills.
- `install/`: documentación para instalación, quickstart y compatibilidad.
- `docs/`: políticas del repositorio.

## Archivos raíz

- `README.md`: entrada principal del proyecto.
- `LICENSE`: licencia MIT.
- `VERSION`: versión global del repo.
- `catalog.json`: catálogo instalable de skills.
- `CHANGELOG.md`: historial global.
- `CONTRIBUTING.md`: guía para contribuciones.

## Decisión de diseño

Cada skill mantiene su propia documentación y changelog para permitir releases ordenadas, revisiones claras y distribución individual sin depender del contexto completo del repositorio.
