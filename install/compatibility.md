# Compatibilidad

## Objetivo

Estas skills están diseñadas para instalaciones locales de Codex que cargan skills desde `${CODEX_HOME:-$HOME/.codex}/skills`.

## Compatibilidad esperada

- Repositorios locales gestionados con Git.
- Entornos macOS y Linux con estructura de home estándar.
- Flujos donde Codex carga skills basadas en carpetas con `SKILL.md`.

## Dependencias por skill

- `skill-git-github-expert`: recomienda Git y acceso a GitHub cuando el usuario trabaja con remotos o PRs.
- `skill-rag-research`: no exige una herramienta concreta, pero asume acceso a fuentes primarias, documentación o corpus recuperable.
- `skill-sdd-architect`: no depende de tooling específico; funciona sobre prompts, documentos y repositorios existentes.

## Compatibilidad del catálogo

`catalog.json` está pensado como catálogo estático legible por humanos y scripts sencillos. Si en tu entorno necesitas más campos, puedes extenderlo sin romper la distribución base mientras mantengas compatibilidad hacia atrás.

## Notas prácticas

- Si tu instalación usa otro directorio de skills, ajusta `${CODEX_HOME}`.
- Si empaquetas skills para una organización, conserva `skill.json` y `SKILL.md` sin renombrarlos.
- Si automatizas instalación, usa el `slug` como nombre de carpeta canónico.
