# Versioning

## Política general

Este repositorio usa Semantic Versioning.

Formato: `MAJOR.MINOR.PATCH`

## Repositorio

La versión del repositorio vive en [`VERSION`](../VERSION).

- `MAJOR`: cambios incompatibles en estructura pública, catálogo o convención de instalación.
- `MINOR`: nuevas skills, capacidades nuevas o ampliaciones compatibles.
- `PATCH`: correcciones editoriales, ajustes de metadata o mejoras no rompientes.

## Skills

Cada skill versiona de forma independiente en `skill.json`.

- sube `MAJOR` si rompes compatibilidad de uso o renombrado público;
- sube `MINOR` si agregas flujos, ejemplos o capacidades compatibles;
- sube `PATCH` si corriges redacción, assets o metadata sin cambiar el uso esperado.

## Changelogs

- El repo mantiene `CHANGELOG.md`.
- Cada skill mantiene su propio `CHANGELOG.md`.
- Si una release toca varias skills, documenta el impacto en ambos niveles.

## Recomendación operativa

Cuando publiques:

1. actualiza `VERSION`;
2. actualiza `catalog.json`;
3. actualiza changelogs relevantes;
4. crea tag `vX.Y.Z`.
