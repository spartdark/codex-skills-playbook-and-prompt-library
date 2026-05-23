# Codex Engineering Pre-Read

## Proposito

Guia portable para usar Codex como asistente de preparacion tecnica antes de planear, priorizar o iniciar trabajo de ingenieria.

El objetivo es producir un pre-read accionable: un resumen corto, basado en evidencia local, que ayude a decidir que hacer despues. No es un reporte decorativo ni una minuta automatica.

Este documento esta disenado para copiarse a otros proyectos. Ajusta solo las rutas de memoria, comandos de verificacion y fuentes del proyecto.

## Decision De Formato

Este archivo sigue siendo una guia portable, no una skill formal de Codex.

Razones:

- debe poder copiarse a cualquier repo sin depender de instalacion en `$CODEX_HOME/skills`;
- contiene prompts, criterios y convenciones editables por proyecto;
- su uso principal es preparar sesiones manuales antes de automatizar.

Si mas adelante se convierte en skill formal, crea un `SKILL.md` separado con:

- descripcion y triggers de uso;
- pasos obligatorios;
- formato de salida;
- guardrails;
- referencias a esta guia como documentacion extendida.

## Origen Del Patron

El patron viene del workflow mostrado en el video "Spec-driven development: the AI engineering workflow at Notion | Ryan Nystrom".

En el video, Notion usa un agente diario para preparar el standup:

- corre antes de la reunion;
- mira una ventana fija de actividad;
- revisa Slack, tareas, PRs, metricas y notas previas;
- llena una pagina de reunion con secciones utiles;
- publica el link para que el equipo llegue con contexto;
- permite que la reunion se enfoque en decisiones, riesgos, progreso y siguientes acciones.

La adaptacion para proyectos propios es empezar manualmente con Codex antes de automatizar.

## Cuando Usarlo

Usa este pre-read cuando:

- vas a empezar una semana de trabajo;
- retomas un proyecto despues de varios dias;
- hay muchas notas, commits, fuentes o experimentos acumulados;
- necesitas decidir que tarea dar a Codex despues;
- quieres detectar riesgos antes de implementar;
- quieres convertir investigacion en backlog o specs.

No hace falta usarlo para tareas pequenas o preguntas puntuales.

## Principios

- Evidencia antes que narrativa: cada recomendacion debe apuntar a un archivo, commit, comando, issue, PR, fuente o brecha explicita.
- Manual antes que automatico: corre 2 o 3 pre-reads manuales antes de crear una automatizacion.
- Accion antes que resumen: el resultado debe cambiar prioridades o producir tareas claras.
- Ventana fija: define "ultimos 7 dias", "desde el ultimo pre-read" o "desde el ultimo release".
- Separar confianza: marca hechos verificados, inferencias y puntos que necesitan validacion.
- Sin cambios de codigo: el pre-read es analisis y planeacion, no implementacion.

## Politica De Fechas Y Zona Horaria

Usa fechas absolutas en todos los pre-reads.

Reglas:

- No dejes la ventana como "ultimos 7 dias" en el entregable final.
- Convierte la ventana a rango explicito: `YYYY-MM-DD to YYYY-MM-DD`.
- Incluye zona horaria: `America/Mexico_City` salvo que el proyecto indique otra.
- Incluye fecha y hora de generacion en formato ISO local: `YYYY-MM-DD HH:mm TZ`.
- Si el usuario pide "hoy", "ayer", "esta semana" o "desde la ultima vez", traduce esa frase a fechas concretas antes de analizar.
- Si no existe un pre-read anterior, marca la ventana como `initial review` y declara el supuesto.

## Estructura Recomendada Del Proyecto

Para que Codex pueda generar buenos pre-reads, cada proyecto deberia tener al menos:

```txt
docs/
  skills/
    codex-engineering-pre-read.md
  specs/
  runbooks/
knowledge/                  # opcional, si usas memoria local
  raw/
  processed/
  briefs/
    weekly/
  projects/<project>/
    source-index.md
    experiments.md
    open-questions.md
    process-improvements.md
    implementation-patterns.md
```

Si tu proyecto no usa `knowledge/`, reemplaza esas rutas por:

- issues de GitHub;
- Linear/Jira;
- `docs/decisions.md`;
- `docs/roadmap.md`;
- `docs/experiments.md`;
- changelog o release notes.

## Output Storage

Por defecto, el pre-read se responde en chat y no modifica archivos.

Guarda un draft solo si el usuario lo pide explicitamente o si existe una automatizacion aprobada.

Rutas recomendadas:

- manual en docs: `docs/pre-reads/YYYY-MM-DD-engineering-pre-read.md`;
- manual en memoria local: `knowledge/briefs/weekly/YYYY-MM-DD-engineering-pre-read.md`;
- automatizado semanal: `knowledge/briefs/weekly/YYYY-Www-engineering-pre-read.md`.

Naming:

- usa fecha de inicio o fecha de generacion, segun la convencion del proyecto;
- evita nombres relativos como `latest.md`;
- si hay varios pre-reads el mismo dia, agrega sufijo corto: `-v2`, `-frontend`, `-release`.

Politica de escritura:

- Chat-only: Codex devuelve el Markdown y no escribe archivos.
- Draft: Codex crea o actualiza solo el archivo del pre-read.
- Automation draft: Codex escribe solo en la ruta aprobada y no toca backlog, specs ni decisiones.

## Fuentes A Revisar

### Minimas En Cualquier Repo

- `git status --short`
- `git log --oneline --decorate --max-count=20`
- archivos modificados o no trackeados relevantes
- `README.md`
- `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml` o equivalente
- comandos de test/build/lint disponibles
- docs de arquitectura o setup

### Si Usas Memoria Local

- `knowledge/projects/<project>/source-index.md`
- `knowledge/projects/<project>/experiments.md`
- `knowledge/projects/<project>/open-questions.md`
- `knowledge/projects/<project>/process-improvements.md`
- `knowledge/projects/<project>/implementation-patterns.md`
- `knowledge/projects/<project>/agent-workflows.md`

### Si Usas Gestion Externa

- issues abiertos y cerrados recientemente;
- PRs mergeados o bloqueados;
- incidentes;
- bugs reportados;
- metricas o dashboards;
- notas de reuniones;
- feedback de usuarios.

## Proceso Manual

1. Define la ventana de analisis.
   Ejemplo: `2026-05-13 to 2026-05-20, America/Mexico_City`.

2. Pide a Codex que inspeccione solo contexto.
   No debe implementar ni modificar archivos.

3. Revisa actividad del repo.
   Git status, commits recientes, archivos cambiados, dependencias y configuracion.

4. Revisa memoria o gestion de proyecto.
   Experimentos, preguntas abiertas, decisiones, fuentes, backlog y mejoras de proceso.

5. Revisa validacion.
   Scripts disponibles, tests faltantes, CI lento, builds rotos o ausencia de comandos claros.

6. Sintetiza decisiones.
   El pre-read debe responder: que cambio, que importa, que esta bloqueado, que riesgo existe y que conviene hacer ahora.

7. Cierra con tareas para Codex.
   Cada tarea debe tener objetivo, alcance, criterios de aceptacion y verificacion.

8. Decide destino del resultado.
   Si no hay instruccion explicita para guardar, responde en chat.

## Formato Del Pre-Read

```md
# Engineering Pre-Read

## Metadata

- Project:
- Window:
- Generated:
- Sources inspected:
- Confidence:
- Output destination:

## Executive Summary

## Changes Since Last Review

## Decisions Needed

## Risks And Blockers

## Bugs Or Validation Gaps

## Open Questions

## Recommended Next Actions

## Proposed Codex Tasks

## Evidence Table

| Claim | Status | Evidence | Source | Inference | Next validation |
|-------|--------|----------|--------|-----------|-----------------|
|  | verified / inferred / needs validation |  | file path, command, commit, issue, PR or source |  |  |

## Failure Modes Encountered

## Assumptions And Missing Information
```

## Prompt Principal

Copia este prompt en Codex y ajusta las rutas entre corchetes.

````md
# Codex Prompt Brief: Engineering Pre-Read

Crea un pre-read de ingenieria para `[project]`.

No implementes cambios, no modifiques archivos y no crees automatizaciones. Esta tarea es solo analisis, planeacion y priorizacion.

Window:
- Requested window: `[relative or absolute window]`
- Convert it to absolute dates before analyzing.
- Timezone: `[timezone, default America/Mexico_City]`

Output:
- Destination: chat-only unless I explicitly ask you to save a draft.
- If saving is requested, use `[docs/pre-reads/YYYY-MM-DD-engineering-pre-read.md or knowledge/briefs/weekly/YYYY-MM-DD-engineering-pre-read.md]`.

Inspect at minimum:

```bash
git status --short
git log --oneline --decorate --max-count=20
```

Also inspect:

- `[README or setup docs]`
- `[package.json / pyproject.toml / go.mod / Cargo.toml / equivalent]`
- `[docs/specs or docs/runbooks]`
- `[knowledge/projects/<project>/source-index.md if present]`
- `[knowledge/projects/<project>/experiments.md if present]`
- `[knowledge/projects/<project>/open-questions.md if present]`
- `[issues, PRs or local meeting notes if available]`

Return Markdown with these sections:

1. Metadata
2. Executive Summary
3. Changes Since Last Review
4. Decisions Needed
5. Risks And Blockers
6. Bugs Or Validation Gaps
7. Open Questions
8. Recommended Next Actions
9. Proposed Codex Tasks
10. Evidence Table
11. Assumptions And Missing Information
12. Failure Modes Encountered

Quality rules:

- Mark each material point as `verified`, `inferred` or `needs validation`.
- Every recommendation must cite evidence: file, command, commit, issue, PR, source or explicit gap.
- Use absolute dates and include timezone.
- If evidence is missing, say so and move the point to open questions or assumptions.
- Do not revert or hide unrelated working tree changes; mention them if they affect the analysis.
- Keep proposed tasks small enough for one Codex session.

Evidence table schema:

| Claim | Status | Evidence | Source | Inference | Next validation |
|-------|--------|----------|--------|-----------|-----------------|

Each proposed Codex task must include:

- Objective
- Scope
- Non-scope
- Acceptance criteria
- Verification command or manual flow
````

## Failure Modes

Incluye una seccion `Failure Modes Encountered` cuando ocurra cualquiera de estos casos.

| Failure mode | Como reportarlo | Accion recomendada |
|--------------|-----------------|--------------------|
| Fuentes ausentes | Lista la ruta, issue, PR, dashboard o nota que no estuvo disponible. | Marca las conclusiones relacionadas como `needs validation`. |
| Working tree sucio | Resume archivos modificados/no trackeados relevantes sin revertir nada. | Distingue cambios relacionados vs no relacionados. |
| Tests no disponibles | Indica que no hay script claro de test/build/lint o que no se encontro manifest. | Propone una tarea pequena para documentar verificacion minima. |
| Repo sin commits recientes | Reporta el ultimo commit disponible y la fecha si se puede obtener. | Cambia el foco a docs, backlog, memoria local o preguntas abiertas. |
| CI o gestion externa inaccesible | Reporta herramienta y razon de inaccesibilidad si se conoce. | No inventes estado; pide validar o usa evidencia local. |
| Ventana ambigua | Muestra el supuesto de fechas absolutas usado. | Pide confirmacion solo si el supuesto cambia decisiones importantes. |

## Prompt De Correccion Del Pre-Read

Usalo despues de revisar manualmente el primer resultado.

```md
Actualiza el pre-read con estas correcciones:

[Pega tus correcciones.]

Preserva solo recomendaciones con evidencia.
Mueve lo especulativo a "Assumptions And Missing Information".
Haz que las tareas propuestas sean mas pequenas y verificables.
No agregues nuevas conclusiones sin revisar fuentes locales.
```

## Prompt Para Forzar Evidencia

Usalo cuando Codex este siendo demasiado complaciente o generico.

```md
Defiende tus recomendaciones con evidencia especifica.

Para cada recomendacion, dime:

- que evidencia la soporta;
- que parte es inferencia;
- que riesgo hay si no se hace;
- cual es el experimento o verificacion mas pequeno para confirmarla.

Si no hay evidencia suficiente, degrada la recomendacion a pregunta abierta.
```

## Prompt Para Convertir Pre-Read En Tareas

```md
Convierte este pre-read en un backlog pequeno para Codex.

Reglas:

- maximo 5 tareas;
- cada tarea debe poder completarse en una sesion;
- cada tarea debe tener criterios de aceptacion observables;
- cada tarea debe tener comando o flujo de verificacion;
- separa investigacion, documentacion e implementacion;
- no combines tareas con archivos o riesgos no relacionados.
```

## Ejemplo De Tarea Propuesta

```md
## Task 1: Crear spec para el workflow de pre-read

- Objective: documentar el workflow esperado antes de automatizarlo.
- Scope: crear o actualizar `docs/specs/engineering-pre-read.md`.
- Non-scope: no crear cron, heartbeat ni integraciones externas.
- Acceptance criteria:
  - la spec define inputs, outputs, permisos y formato;
  - incluye criterios de exito y fallo;
  - lista fuentes requeridas por proyecto.
- Verification:
  - revisar que la spec pueda ejecutarse manualmente con un prompt de Codex;
  - confirmar que no depende de herramientas externas no configuradas.
```

## Cuando Automatizar

Automatiza solo cuando:

- ya corriste 2 o 3 pre-reads manuales;
- el formato produjo decisiones utiles;
- las fuentes son estables;
- sabes donde guardar el resultado;
- el agente no necesita permisos amplios de escritura.

Primera automatizacion recomendada:

- frecuencia: semanal;
- salida: draft Markdown;
- destino: `knowledge/briefs/weekly/` o `docs/pre-reads/`;
- permisos: lectura del repo y escritura solo del draft;
- no debe modificar backlog, specs ni archivos de decision automaticamente.

## Checklist Portable

Antes de llevar esta guia a otro proyecto:

- Cambia el nombre del proyecto.
- Ajusta rutas de memoria y docs.
- Ajusta comandos de test/build/lint.
- Define donde guardar pre-reads.
- Define la ventana de analisis.
- Define que fuentes son evidencia primaria.
- Decide si Codex puede escribir drafts o solo responder en chat.
- Corre una version manual antes de automatizar.

## Relacion Con Otros Documentos

Combina bien con:

- `codex-practical-guide.md`: reglas generales para usar Codex como agente de ingenieria.
- `codex-prompt-briefs.md`: plantilla para convertir una recomendacion del pre-read en una tarea implementable.
- specs del proyecto: cuando el pre-read detecta una iniciativa que necesita diseno antes de codigo.
- memoria local o backlog: donde se guardan decisiones, experimentos y preguntas abiertas.
