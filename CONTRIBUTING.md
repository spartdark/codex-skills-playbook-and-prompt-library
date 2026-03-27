# Contributing

Gracias por mejorar esta librería de skills.

## Objetivo de contribución

Cada cambio debe ayudar a que una skill sea:

- más clara al activarse;
- más confiable al ejecutarse;
- más fácil de instalar y versionar;
- más segura para usarse en repositorios reales.

## Flujo recomendado

1. Crea una rama descriptiva desde `main`.
2. Haz cambios pequeños y verificables.
3. Actualiza la documentación afectada.
4. Si cambia una skill pública, actualiza su `skill.json` y `CHANGELOG.md`.
5. Si cambia el catálogo público, actualiza `catalog.json`.
6. Si cambia la distribución del repositorio, actualiza `README.md` o `docs/`.
7. Abre un pull request con contexto suficiente para revisión.

## Convenciones de commits

Usa Conventional Commits cuando sea posible:

- `feat(scope): ...`
- `fix(scope): ...`
- `docs(scope): ...`
- `refactor(scope): ...`
- `chore(scope): ...`

Ejemplos:

- `feat(skills): add prompt assets for rag research`
- `docs(install): clarify CODEX_HOME fallback`
- `chore(release): bump catalog to 0.2.0`

## Checklist antes de abrir PR

- El cambio tiene propósito claro.
- La documentación coincide con el contenido real.
- Los slugs, ids y versiones coinciden entre `catalog.json` y `skill.json`.
- No se introducen placeholders vacíos.
- La skill mantiene un `SKILL.md` enfocado y accionable.

## Criterios para aceptar una nueva skill

Una skill nueva debe incluir:

- nombre claro y alcance específico;
- `SKILL.md` con activadores y flujo operativo;
- `prompt.md` con tono y guardrails;
- `skill.json` con campos completos;
- ejemplo de uso real;
- changelog inicial;
- documentación suficiente para compartirla.

## Versionado

Sigue la política de [`docs/versioning.md`](docs/versioning.md).
