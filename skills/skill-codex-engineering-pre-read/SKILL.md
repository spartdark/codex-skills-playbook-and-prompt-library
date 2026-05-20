---
name: codex-engineering-pre-read
description: Guia portable para usar Codex como asistente de pre-read tecnico antes de planear, priorizar, implementar o automatizar trabajo de ingenieria, con evidencia local, tareas verificables y prompts reutilizables.
---

# Codex Engineering Pre-Read

## Mision

Preparar un pre-read tecnico accionable antes de una sesion de planeacion, implementacion o automatizacion con Codex.

La salida esperada no es un resumen decorativo. Debe convertir estado del repo, memoria del proyecto, decisiones abiertas, riesgos y gaps de validacion en tareas concretas y verificables.

## Cuando Usarla

Activa esta skill cuando el usuario quiera:

- preparar una semana o sesion de trabajo tecnico;
- retomar un proyecto con contexto acumulado;
- revisar cambios recientes antes de implementar;
- convertir investigacion, notas o knowledge base en backlog accionable;
- detectar riesgos, bugs o preguntas abiertas antes de dar tareas a Codex;
- disenar una automatizacion futura de pre-read semanal o diario.

No la uses para tareas pequenas que solo requieren una respuesta directa o un comando puntual.

## Flujo De Trabajo

1. Define la ventana de analisis: ultimos 7 dias, desde el ultimo pre-read, desde el ultimo release o la ventana indicada por el usuario.
2. Inspecciona actividad local: `git status --short`, commits recientes, archivos cambiados, dependencias y configuracion.
3. Revisa memoria del proyecto: docs, specs, backlog, experiments, open questions, process improvements o el sistema equivalente del repo.
4. Revisa validacion: scripts de test/build/lint, CI disponible, gaps de pruebas, fallos visibles o ausencia de comandos claros.
5. Sintetiza solo lo que cambia decisiones: progreso, riesgos, bloqueos, bugs, preguntas abiertas y proximas acciones.
6. Marca confianza: `verified`, `inferred` o `needs validation`.
7. Cierra con tareas Codex pequenas, cada una con objetivo, alcance, no-alcance, criterios de aceptacion y verificacion.

## Formato De Salida

Usa esta estructura por defecto:

```md
# Engineering Pre-Read

## Metadata

- Project:
- Window:
- Generated:
- Sources inspected:
- Confidence:

## Executive Summary

## Changes Since Last Review

## Decisions Needed

## Risks And Blockers

## Bugs Or Validation Gaps

## Open Questions

## Recommended Next Actions

## Proposed Codex Tasks

## Evidence Table

## Assumptions And Missing Information
```

## Guardrails

- No implementes cambios durante el pre-read salvo que el usuario lo pida explicitamente.
- No modifiques archivos si el usuario pidio solo analisis.
- No presentes inferencias como hechos.
- No recomiendes acciones sin evidencia o sin decir que falta evidencia.
- No automatices el workflow hasta que existan 2 o 3 pre-reads manuales utiles.
- Si el working tree contiene cambios de usuario, analizalos sin revertirlos.
- Si el repo no tiene `knowledge/`, adapta la revision a issues, PRs, docs, roadmap, changelog o notas disponibles.

## Prompts Reutilizables

Pre-read inicial:

```md
Review the last 7 days of project activity. Produce a pre-read focused on decisions, risks, progress, bugs, open questions and next actions. Link every claim to local evidence.
```

Correccion del pre-read:

```md
Update the pre-read with these corrections. Preserve only recommendations with evidence. Move speculative items to assumptions or open questions.
```

Forzar evidencia:

```md
Defend your recommendations with specific evidence. If evidence is weak, mark the item as an inference and propose the smallest validation step.
```

Convertir en tareas:

```md
Convert this pre-read into a small Codex backlog. Each task must fit in one session and include acceptance criteria plus verification.
```

## Referencias Internas

- `prompt.md`: prompt operativo completo para correr el pre-read.
- `assets/codex-engineering-pre-read.md`: guia portable completa.
- `assets/codex-practical-guide.md`: guia general para usar Codex como agente de ingenieria.
- `assets/codex-prompt-briefs.md`: plantilla para convertir recomendaciones en tareas ejecutables.
- `examples/example-1.md`: ejemplo de uso en un repo con memoria local.
