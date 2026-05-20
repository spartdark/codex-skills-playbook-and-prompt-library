# Codex Engineering Pre-Read Prompt

## Enfoque

Actua como un engineering manager pragmatico y como un agente tecnico que revisa evidencia local antes de recomendar trabajo.

Tu objetivo es ayudar al usuario a decidir que hacer despues, no producir una narracion larga del proyecto.

## Prompt Base

````md
# Codex Prompt Brief: Engineering Pre-Read

## Objetivo

Crea un pre-read de ingenieria para este proyecto.

No implementes cambios. No modifiques archivos. Esta tarea es solo analisis, planeacion y priorizacion.

## Contexto

Proyecto:
[Describe brevemente el proyecto.]

Ventana de analisis:
[Ultimos 7 dias / desde el ultimo pre-read / desde el ultimo release.]

Memoria o gestion del proyecto:
[Rutas a knowledge/, docs/, issues, backlog, roadmap o decisiones.]

## Fuentes A Revisar

Revisa como minimo:

```bash
git status --short
git log --oneline --decorate --max-count=20
```

Inspecciona tambien:

- [README o docs de setup]
- [package.json / pyproject.toml / go.mod / equivalente]
- [docs/specs o docs/runbooks relevantes]
- [source-index / experiments / open-questions si existen]
- [issues, PRs o notas si estan disponibles localmente]

## Alcance

Incluye:

- cambios recientes;
- tareas abiertas o incompletas;
- bugs, riesgos o bloqueos;
- decisiones pendientes;
- gaps de validacion;
- proximos pasos recomendados;
- 3 tareas propuestas para Codex.

No incluye:

- implementar codigo;
- refactors;
- cambios de documentacion;
- crear automatizaciones;
- recomendaciones sin evidencia.

## Reglas De Calidad

- Marca cada punto como `verified`, `inferred` o `needs validation`.
- Cada recomendacion debe apuntar a evidencia: archivo, comando, commit, issue, PR, fuente o brecha explicita.
- Si falta evidencia, dilo.
- Si hay cambios no relacionados en el working tree, no los reviertas ni los ignores si afectan el analisis.
- Prioriza acciones pequenas, verificables y utiles para la siguiente sesion.

## Entregable

Devuelve un Markdown con:

1. Executive summary.
2. Changes since last review.
3. Decisions needed.
4. Risks and blockers.
5. Bugs or validation gaps.
6. Open questions.
7. Recommended next actions.
8. Proposed Codex tasks.
9. Evidence table.
10. Assumptions and missing information.

Cada tarea propuesta para Codex debe incluir:

- objetivo;
- alcance;
- no-alcance;
- criterios de aceptacion;
- comando o flujo de verificacion.
````

## Criterio De Calidad

Un buen pre-read termina con:

- evidencia concreta;
- pocas recomendaciones;
- decisiones visibles;
- riesgos sin maquillar;
- tareas que se pueden ejecutar en una sesion;
- comandos o flujos de verificacion.

Si la evidencia es insuficiente, convierte la recomendacion en pregunta abierta o experimento.
