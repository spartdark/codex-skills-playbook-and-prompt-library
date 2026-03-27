---
name: template-skill
description: Plantilla para crear una skill de Codex con activadores claros, flujo operativo, guardrails y referencias reutilizables.
---

# Template Skill

## Cuándo usarla

Usa esta plantilla cuando vayas a crear una skill nueva para Codex y necesites un punto de partida consistente con esta librería pública.

## Resultado esperado

La skill final debe dejar claro:

- qué problema resuelve;
- cuándo debe activarse;
- qué flujo sigue;
- qué riesgos evita;
- qué archivos adicionales conviene leer.

## Estructura recomendada

1. Define la misión en una frase.
2. Enumera activadores concretos.
3. Describe el flujo principal en pocos pasos.
4. Añade guardrails operativos.
5. Enlaza referencias, ejemplos y assets cuando hagan falta.

## Guardrails mínimos

- No repitas conocimiento obvio del modelo.
- Mantén `SKILL.md` corto y accionable.
- Mueve detalles extensos a `README.md`, `examples/` o `assets/`.
- Usa nombres y slugs coherentes con `skill.json`.
