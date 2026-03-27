# Git & GitHub Expert

Skill pública para operadores de código que necesitan trabajar con Git y GitHub sin deteriorar el historial ni la coordinación del equipo.

## Qué cubre

- inspección de estado git;
- estrategia de ramas;
- Conventional Commits;
- preparación de pull requests;
- decisiones de merge, squash y rebase;
- preparación de releases y changelogs.

## Casos de uso

- "Haz commit de mis cambios con un mensaje claro".
- "¿Conviene rebase o merge para esta rama?"
- "Déjame listo un PR publicable".
- "Ayúdame a preparar una release sin ensuciar el historial".

## Instalación

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-git-github-expert "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contenido

- `SKILL.md`: flujo operativo de la skill.
- `prompt.md`: guía de tono y expectativas.
- `skill.json`: metadata instalable.
- `examples/`: ejemplo de activación.
- `assets/`: material reutilizable para PRs.
