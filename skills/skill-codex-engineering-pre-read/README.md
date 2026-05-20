# Codex Engineering Pre-Read

Skill portable para usar Codex como asistente de preparacion tecnica antes de planear, priorizar, implementar o automatizar trabajo de ingenieria.

## Que Cubre

- pre-reads semanales o por ventana de trabajo;
- revision de estado git, docs, memoria local y validacion;
- separacion entre evidencia, inferencia y falta de datos;
- conversion de contexto acumulado en tareas Codex verificables;
- prompts reutilizables para pedir evidencia, corregir el pre-read y convertirlo en backlog.

## Casos De Uso

- "Haz un pre-read semanal de este repo antes de decidir que sigue".
- "Retomo este proyecto, dime que cambio y que deberia priorizar".
- "Convierte estos docs y knowledge files en 3 tareas para Codex".
- "Antes de automatizar esto, ayudame a correrlo manualmente".

## Instalacion

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-codex-engineering-pre-read "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contenido

- `SKILL.md`: flujo base, activadores y guardrails.
- `prompt.md`: prompt operativo listo para adaptar.
- `skill.json`: metadata instalable.
- `assets/codex-engineering-pre-read.md`: guia portable completa.
- `assets/codex-practical-guide.md`: guia general para usar Codex como agente de ingenieria.
- `assets/codex-prompt-briefs.md`: templates para tareas con contexto, alcance y verificacion.
- `examples/example-1.md`: ejemplo de aplicacion.

## Recomendacion De Uso

Corre 2 o 3 pre-reads manuales antes de automatizar. La primera automatizacion deberia escribir un draft Markdown, no modificar backlog, specs o archivos de decision automaticamente.
