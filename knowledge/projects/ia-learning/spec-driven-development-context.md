# Spec-Driven Development Context

Use this document as context when asking Codex or another coding agent to turn a rough idea into an implementable spec.

Advanced operating guide: [Spec-Driven Development Guide](spec-driven-development-guide.md).

## Purpose

Convert vague product or engineering intent into a durable spec before implementation. The spec becomes the source of truth for the agent, reviewer and future changes.

## What Counts As A Rough Idea

A rough idea can be any unstructured input, for example:

- a short feature request
- a bug description
- a screenshot with notes
- a voice transcript
- a chat message
- a customer pain point
- a task title plus a few bullets
- an improvement observed from a YouTube/source analysis

The rough idea does not need to mention files, architecture or exact implementation details. The agent should infer likely technical areas only after reading the repo.

## Required Agent Behavior

When given a rough idea, the agent must:

1. Read the relevant repo context before writing the spec.
2. Separate facts from assumptions.
3. Ask questions only if implementation would be risky without the answer.
4. Produce a spec, not code.
5. Include verification steps that can realistically be executed.
6. Mark unknowns and unresolved decisions clearly.
7. Keep the spec scoped enough that another agent can implement it.

## Spec Output Format

```md
# Feature Spec: <name>

## Source Idea

## Problem

## Goals

## Non-Goals

## Current Behavior

## Desired Behavior

## User Flows

## Technical Approach

## Files Or Areas Likely Involved

## Data, API Or Integration Changes

## UI States

## Edge Cases

## Acceptance Criteria

## Verification Plan

## Risks

## Open Questions
```

## Prompt To Generate A Spec

```md
Use `knowledge/projects/ia-learning/spec-driven-development-context.md` as context.

Toma esta idea en bruto y conviértela en una spec implementable:

<pega aquí la idea, notas, transcript, screenshot description o bug report>

Incluye goals, non-goals, comportamiento esperado, edge cases,
archivos probables, criterios de aceptación y plan de verificación.

Lee el repo antes de proponer archivos o enfoque técnico.
Separa hechos de supuestos.
No implementes todavía.
```

## Prompt To Implement From The Spec

```md
Implementa la feature siguiendo esta spec:

<pega o referencia la ruta de la spec>

No cambies el scope sin actualizar primero la spec.
Devuelve resumen del diff, comandos de verificación ejecutados,
evidencia, riesgos y supuestos no verificados.
```

## Example Rough Ideas

```md
Quiero que el proyecto tenga un reporte semanal que lea `knowledge/`,
detecte fuentes nuevas, experimentos estancados y próximos pasos.
Debe dejar un brief en Markdown y no modificar código de producto.
```

```md
Al analizar videos de YouTube, quiero que además del resumen se genere
una lista de experimentos accionables para `ia-learning`, con evidencia
y confidence label.
```

```md
La app tarda mucho en validar cambios. Quiero identificar qué comandos
son lentos y proponer un plan para mejorar el feedback loop de agentes.
```
