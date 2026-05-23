# Agent Control Plane Guide

Guia operativa portable para coordinar agentes de IA con task contracts, scope claro, validacion, evidencia, subagentes y memoria durable.

Esta guia es un anexo especializado de [Codex Operating System Guide](codex-operating-system-guide.md). Usala cuando una tarea sea demasiado grande, ambigua, riesgosa o repetible para resolverse con un prompt suelto.

## Proposito

Un control plane de agentes convierte trabajo asistido por IA en un sistema auditable:

```txt
intencion -> contrato -> lanes -> ejecucion -> evidencia -> review -> memoria
```

El objetivo es reducir scope drift, duplicacion, contexto oculto, validacion debil y entregas que dependen de "confia en mi". El agente puede avanzar con autonomia, pero dentro de limites explicitos.

## Cuando Usar Esta Guia

Usar cuando:

- hay multiples archivos, dominios o artefactos;
- hace falta coordinar subagentes, reviewers o herramientas distintas;
- la tarea requiere investigacion antes de implementar;
- hay riesgo de romper comportamiento existente;
- el usuario pide un workflow, spec, automatizacion, reporte o sistema reusable;
- la salida debe ser trazable con evidencia;
- el trabajo puede repetirse y conviene convertirlo en plantilla, skill o proceso.

No usar completa cuando:

- la tarea es una pregunta simple;
- el cambio es pequeno, reversible y local;
- el usuario pidio solo una explicacion rapida;
- el costo de estructurar supera el riesgo.

Para tareas pequenas, usa la version compacta:

```md
Objective:
Scope:
Validation:
Evidence:
Done when:
```

## Variables Portables

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable>
PROJECT_ROOT=<raiz del repo>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
CONTROL_PLANE_DIR=<PROJECT_MEMORY_DIR>/control-plane
TASK_CONTRACT_DIR=<CONTROL_PLANE_DIR>/tasks
RUN_LOG_DIR=<CONTROL_PLANE_DIR>/runs
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
VALIDATION_COMMANDS=<comandos del repo>
PATH_TO_THIS_GUIDE=<ruta a esta guia>
```

## Componentes Del Control Plane

```txt
control plane
  project profile       reglas permanentes del proyecto
  task contract         scope, contexto, roles, validacion
  lane plan             subagentes y ownership
  state board           estado actual de trabajo
  evidence log          pruebas, links, outputs, screenshots
  decision log          decisiones y tradeoffs
  escalation log        bloqueos y aprobaciones humanas
  memory update         aprendizajes persistidos
```

El control plane puede vivir en el chat para tareas pequenas. Para tareas medianas o de equipo debe quedar versionado en archivos.

## Principios

1. Ningun agente trabaja sin objetivo y scope.
2. Ningun subagente recibe contexto infinito; recibe el contexto minimo suficiente.
3. Ninguna tarea se cierra sin evidencia o bloqueo documentado.
4. Ningun output de IA es evidencia primaria sin verificacion.
5. Ningun agente modifica areas fuera de su contrato sin registrar el cambio de scope.
6. Ninguna automatizacion nace sin una corrida manual validada.
7. Ninguna decision importante queda solo en el chat.

## Niveles De Control

| Nivel | Uso | Overhead | Artefactos |
|---|---|---:|---|
| Lite | tarea local y clara | bajo | mini contrato |
| Standard | cambio multi-archivo o doc reusable | medio | task contract + validation log |
| Coordinated | varios lanes/subagentes | medio-alto | lane plan + state board + evidence log |
| Regulated | datos sensibles, pagos, produccion, seguridad | alto | approvals + rollback + audit log |
| Automated | workflow recurrente | alto | runbook + QA + automation policy |

Empieza con el nivel mas pequeno que preserve trazabilidad suficiente.

## Roles

### Orchestrator

Responsable de convertir la intencion en contrato, dividir lanes, asignar contexto, revisar evidencias y cerrar memoria.

Debe:

- leer contexto local antes de planear;
- definir objetivo, non-goals y validation;
- impedir scope drift;
- coordinar subagentes;
- consolidar resultados;
- reportar riesgos residuales.

No debe:

- delegar sin acceptance criteria;
- aceptar "done" sin evidencia;
- ocultar bloqueos;
- mezclar cambios no relacionados.

### Planner

Responsable de specs, task breakdown, dependencies y acceptance criteria.

Usar cuando:

- la idea es ambigua;
- hay varias opciones tecnicas;
- hace falta separar milestones.

Output:

- spec o task plan;
- assumptions;
- open questions;
- validation plan.

### Researcher

Responsable de fuentes externas, docs, transcripts, benchmarks o evidence gathering.

Debe:

- preservar raw source o link;
- separar hechos, inferencias y opiniones;
- marcar confidence;
- crear source-index entry si el hallazgo sera reusable.

### Implementer

Responsable de editar codigo, docs, scripts o configuracion dentro del scope.

Debe:

- respetar patrones existentes;
- mantener diff acotado;
- ejecutar validacion asignada;
- reportar cambios y riesgos.

### Reviewer

Responsable de buscar bugs, regresiones, gaps de validacion y contratos incumplidos.

Debe:

- revisar contra acceptance criteria;
- priorizar hallazgos por severidad;
- exigir evidencia reproducible;
- distinguir blocker, risk y nit.

### QA / Validator

Responsable de ejecutar comandos, inspecciones visuales, smoke tests, fixtures o checks manuales.

Debe:

- registrar comando y resultado;
- guardar evidencia relevante;
- declarar que no se pudo validar cuando aplique.

### Memory Curator

Responsable de persistir aprendizajes.

Debe actualizar:

- source index;
- implementation patterns;
- process improvements;
- experiments;
- open questions;
- run logs.

### Automation Owner

Responsable de convertir un workflow validado en automation.

Debe:

- requerir corrida manual exitosa;
- definir frecuencia, permisos, logs, rollback;
- documentar fallos esperados;
- evitar automatizar outputs no revisados.

## Task Contract

Un task contract es la unidad minima de delegacion. Debe decir que se hara, que no se hara, con que contexto y como se sabra que termino.

### Plantilla Completa

```md
# Task Contract: <short-name>

## Metadata

- Project:
- Created:
- Owner:
- Risk: low | medium | high | regulated
- Status: proposed | active | blocked | review | done | dropped
- Related issue/spec/source:

## Objective

<resultado concreto>

## User Value

<por que importa>

## Non-Objectives

- 

## Scope

### In

- 

### Out

- 

## Context

### Required Reading

- 

### Relevant Files

- 

### Prior Decisions

- 

## Assumptions

- 

## Open Questions

- 

## Agent Lanes

| Lane | Role | Objective | Inputs | Outputs | Validation | Status |
|---|---|---|---|---|---|---|

## Tool Permissions

- Allowed:
- Ask first:
- Forbidden:

## Data And Safety

- Secrets:
- PII:
- External writes:
- Production risk:

## Acceptance Criteria

- 

## Validation Plan

- Command/check:
- Expected result:
- Evidence artifact:

## Evidence Log

| Time | Lane | Evidence | Result | Link/path |
|---|---|---|---|---|

## Decision Log

| Decision | Reason | Owner | Date |
|---|---|---|---|

## Escalation Rules

- Stop if:
- Ask user if:
- Can proceed if:

## Memory Update

- Required: yes | no
- Target files:
- Summary to persist:

## Done Definition

- 
```

### Plantilla Compacta

```md
# Task Contract

- Objective:
- Scope in:
- Scope out:
- Context files:
- Agent lanes:
- Validation:
- Evidence:
- Memory update:
- Done when:
```

## Scope Management

Scope es el principal mecanismo de seguridad del control plane.

### Scope In

Define lo que el agente puede cambiar o producir.

Ejemplos:

- `knowledge/projects/<project-id>/agent-control-plane-guide.md`
- tests de una funcion especifica
- un script nuevo sin tocar runtime de produccion
- docs y memoria local solamente

### Scope Out

Define lo que el agente no debe tocar.

Ejemplos:

- no cambiar APIs publicas;
- no tocar pagos, auth o permisos;
- no refactorizar archivos no relacionados;
- no crear automation todavia;
- no modificar secretos ni `.env`;
- no asumir datos externos sin fuente.

### Cambios De Scope

Si aparece trabajo fuera del contrato:

```txt
1. Pausar esa parte.
2. Registrar scope change.
3. Explicar razon y riesgo.
4. Pedir aprobacion si el cambio afecta behavior, datos, seguridad o timeline.
5. Actualizar contrato antes de ejecutar.
```

Plantilla:

```md
## Scope Change Request

- Original scope:
- Proposed change:
- Reason:
- Risk:
- Files affected:
- Validation added:
- Approval needed: yes | no
```

## Lane Planning

Un lane es una linea de trabajo con output y validacion propios. Los lanes evitan que "un agente haga todo" sin control.

### Lanes Frecuentes

| Lane | Uso | Output |
|---|---|---|
| Context | leer repo, fuentes, restricciones | context brief |
| Spec | convertir idea en plan implementable | spec |
| Implementation | editar codigo/docs | diff |
| Validation | ejecutar checks | validation log |
| Review | buscar bugs/riesgos | review findings |
| Memory | actualizar conocimiento | memory diff |
| Automation | preparar workflow recurrente | runbook/proposal |

### Regla De Ownership

Cada lane debe tener:

- owner;
- inputs;
- outputs;
- validation;
- status;
- handoff target.

Si no puedes decir quien consume el output, el lane probablemente esta mal definido.

## Subagentes

Los subagentes son utiles cuando hay paralelismo real o especializacion clara. No los uses solo para parecer organizado.

### Cuando Delegar

Delegar si:

- los lanes son independientes;
- el output puede verificarse;
- el contexto cabe en un brief pequeno;
- hay riesgo de sesgo si una sola instancia revisa su propio trabajo;
- hay busqueda o lectura extensa que puede separarse.

No delegar si:

- la tarea requiere una decision unica y sensible;
- el contexto compartido es demasiado grande;
- la coordinacion cuesta mas que ejecutar;
- los outputs no tienen criterios de aceptacion.

### Subagent Brief

```md
# Subagent Brief: <lane-name>

## Role

<planner | researcher | implementer | reviewer | validator | memory curator>

## Objective

## Context You Must Read

- 

## Context You May Ignore

- 

## Scope

### Allowed

- 

### Forbidden

- 

## Expected Output

## Validation Or Evidence Required

## Handoff

- Return to:
- Format:
- Deadline/stop condition:
```

### Handoff Contract

Todo subagente debe devolver:

```md
## Handoff

- Lane:
- Status: done | blocked | partial
- Files read:
- Files changed:
- Output:
- Validation:
- Evidence:
- Assumptions:
- Risks:
- Recommended next action:
```

## State Board

Para trabajo coordinado, mantener una tabla visible.

```md
# Agent State Board

| Lane | Owner | Status | Current Task | Blocking On | Evidence | Next |
|---|---|---|---|---|---|---|
| Context | orchestrator | done | repo scan | n/a | links | spec |
| Spec | planner | active | acceptance criteria | user answer | draft path | review |
| Implementation | implementer | pending | n/a | spec | n/a | start |
| Validation | validator | pending | n/a | diff | n/a | run checks |
| Memory | curator | pending | n/a | final outcome | n/a | update docs |
```

Status permitidos:

- `proposed`
- `active`
- `blocked`
- `review`
- `done`
- `dropped`

## Evidence System

La evidencia es el mecanismo para distinguir trabajo real de afirmaciones.

### Tipos De Evidencia

| Tipo | Ejemplo | Fuerza |
|---|---|---|
| Command output | test/build/lint passing | alta |
| Raw source | API response, transcript, docs URL | alta |
| Diff | archivos modificados | alta |
| Screenshot/render | UI o doc visual | alta si aplica |
| Review finding | archivo/linea/riesgo | media-alta |
| Manual QA note | pasos + resultado | media |
| IA summary | resumen sin fuente | baja |

### Evidence Log

```md
# Evidence Log

| Time | Check | Command/Source | Expected | Actual | Result | Artifact |
|---|---|---|---|---|---|---|
```

### Reglas De Evidencia

- Si algo se valido, di como.
- Si no se valido, di por que.
- Si una fuente fallo, guarda el fallo si importa.
- Si un resultado depende de inferencia, marcalo.
- Si hay riesgo residual, no lo escondas en el resumen.

## Validation

La validacion debe corresponder al tipo de tarea.

### Docs

- revisar links internos;
- revisar headings;
- confirmar que no contradice docs existentes;
- buscar referencias duras que rompan portabilidad;
- verificar que plantillas sean copiables.

### Codigo

- tests unitarios;
- typecheck;
- lint;
- build;
- smoke test;
- review de diff.

### Frontend

- build;
- screenshot en desktop/mobile;
- revisar overlap, estados vacios, loading, error;
- interacciones principales;
- accesibilidad basica.

### Investigacion

- raw source o URL preservada;
- confidence label;
- evidence pointers;
- source index actualizado;
- hechos separados de inferencias.

### Automatizacion

- corrida manual previa;
- output revisado;
- logs definidos;
- permisos claros;
- rollback o pausa;
- costo/rate limits considerados.

## Review Gate

Antes de cerrar un trabajo coordinado, ejecutar un gate de review.

```md
# Review Gate

## Contract Check

- Objective met: yes/no
- Scope respected: yes/no
- Non-objectives respected: yes/no
- Acceptance criteria met: yes/no

## Evidence Check

- Validation run:
- Evidence linked:
- Missing evidence:

## Risk Check

- Behavior risk:
- Data/security risk:
- Maintenance risk:
- Follow-up needed:

## Decision

- approve | request changes | block | drop
```

## Coordination Patterns

### Sequential

Usar cuando un lane depende claramente del anterior.

```txt
context -> spec -> implementation -> validation -> review -> memory
```

Ventaja: bajo riesgo de divergencia.

Riesgo: mas lento.

### Parallel

Usar cuando lanes pueden avanzar sin pisarse.

```txt
research --------\
spec -------------> consolidation -> implementation -> validation
technical scan ---/
```

Ventaja: acelera lectura y exploracion.

Riesgo: outputs inconsistentes si no hay contrato comun.

### Reviewer Sandwich

Usar en cambios con riesgo.

```txt
plan -> review plan -> implement -> review diff -> validate -> close
```

Ventaja: detecta errores antes y despues.

Riesgo: mayor overhead.

### Red Team

Usar en seguridad, datos, pagos, prompts sensibles o arquitectura.

```txt
proposal -> adversarial review -> mitigation -> approval
```

Ventaja: reduce puntos ciegos.

Riesgo: puede frenar tareas simples si se aplica demasiado.

## Escalation

Un agente debe parar o pedir decision humana cuando:

- necesita credenciales o secretos;
- tocaria produccion;
- cambiaria scope o comportamiento publico;
- encuentra datos sensibles;
- hay conflicto entre instrucciones;
- no puede validar;
- el riesgo supera el contrato;
- la accion podria ser destructiva;
- una fuente importante no se puede verificar.

Plantilla:

```md
## Escalation

- Blocker:
- Why it matters:
- Options:
- Recommended option:
- Risk if proceeding:
- User decision needed:
```

## Failure Modes

| Falla | Sintoma | Mitigacion |
|---|---|---|
| Scope drift | se editan archivos no relacionados | non-objectives + scope change request |
| Context flooding | subagente recibe demasiados docs | required reading minimo |
| Fake done | "listo" sin tests/evidencia | evidence log obligatorio |
| Parallel conflict | lanes pisan archivos | state board con ownership |
| Weak review | reviewer resume en vez de buscar bugs | review gate con severidad |
| Lost learning | aprendizaje queda en chat | memory curator lane |
| Premature automation | job recurrente produce basura | manual run + QA antes |
| Hidden assumptions | decisiones no justificadas | assumptions + decision log |

## Ready Checklist

Antes de iniciar:

- [ ] Objective claro.
- [ ] Scope in/out definido.
- [ ] Context files listados.
- [ ] Roles o lanes definidos.
- [ ] Validacion posible.
- [ ] Riesgos identificados.
- [ ] Permisos de herramientas claros.
- [ ] Criterios de done escritos.

## Done Checklist

Antes de cerrar:

- [ ] Acceptance criteria cumplidos.
- [ ] Scope respetado.
- [ ] Validacion ejecutada o limitacion explicada.
- [ ] Evidence log actualizado.
- [ ] Riesgos residuales documentados.
- [ ] Decision log actualizado si hubo tradeoffs.
- [ ] Memoria actualizada si aplica.
- [ ] Follow-ups separados del scope actual.

## Prompt Maestro

```md
Usa `<PATH_TO_THIS_GUIDE>` como control plane de agentes.

Objetivo:
<resultado esperado>

Contexto:
<archivos, fuentes, issue, spec, restricciones>

Nivel de control:
Lite | Standard | Coordinated | Regulated | Automated

Antes de actuar:
1. Crea o resume el task contract.
2. Define scope in/out.
3. Identifica lanes y si hacen falta subagentes.
4. Define validacion y evidencia esperada.
5. Marca riesgos y reglas de escalacion.

Durante la ejecucion:
1. Mantén cada lane dentro de su scope.
2. Registra decisiones y evidencia.
3. Pausa si aparece scope change o riesgo no autorizado.
4. Consolida handoffs antes de cerrar.

Al final:
1. Reporta status por lane.
2. Incluye evidencia de validacion.
3. Lista archivos cambiados.
4. Declara riesgos residuales.
5. Actualiza memoria si aplica.
```

## Prompt Para Orquestador

```md
Actua como orchestrator.

Tarea:
<tarea>

Lee contexto relevante y produce un task contract con:
- objective
- non-objectives
- scope in/out
- required reading
- agent lanes
- validation plan
- evidence requirements
- escalation rules
- done definition

No implementes todavia salvo que el usuario lo haya pedido explicitamente.
```

## Prompt Para Subagente Implementador

```md
Actua como implementer dentro de este lane.

Task contract:
<pegar contrato o ruta>

Tu scope:
<scope especifico>

Reglas:
- No modifiques archivos fuera de scope.
- No hagas refactors no solicitados.
- Usa patrones existentes.
- Ejecuta la validacion asignada si puedes.
- Si necesitas cambiar scope, devuelve Scope Change Request.

Devuelve handoff con:
- files read
- files changed
- summary
- validation
- evidence
- risks
```

## Prompt Para Subagente Reviewer

```md
Actua como reviewer.

Revisa este output contra el task contract:
<contrato + diff/output>

Prioriza:
- incumplimiento de scope
- bugs/regresiones
- gaps de validacion
- evidencia insuficiente
- riesgos de datos/seguridad
- memoria faltante

Formato:
1. Findings por severidad con archivo/linea si aplica.
2. Contract check.
3. Evidence gaps.
4. Required changes.
5. Approval decision.
```

## Prompt Para Validator

```md
Actua como validator.

Task contract:
<contrato>

Ejecuta o revisa el validation plan.

Devuelve:
- checks run
- command/source
- expected result
- actual result
- pass/fail/not run
- evidence artifact
- residual risk
```

## Prompt Para Memory Curator

```md
Actua como memory curator.

Input:
<task outcome, evidence, decisions>

Determina si hay aprendizaje reusable.

Si aplica, actualiza:
- source index
- implementation patterns
- process improvements
- experiments
- open questions
- agent workflows

Reglas:
- No trates summaries como evidencia primaria.
- Marca confidence.
- Linkea evidencia.
- Separa hechos, inferencias y experimentos.
```

## Control Plane File Set

Para proyectos que quieran versionar el control plane, usar esta estructura:

```txt
<PROJECT_MEMORY_DIR>/control-plane/
  README.md
  tasks/
    YYYY-MM-DD-<task-slug>.md
  runs/
    YYYY-MM-DD-<run-slug>.md
  templates/
    task-contract.md
    subagent-brief.md
    evidence-log.md
    review-gate.md
```

No todos los proyectos necesitan esta carpeta desde el dia uno. Crear cuando haya dos o mas tareas coordinadas o cuando el equipo necesite auditoria.

## Ejemplo Completo

### Solicitud

```txt
Crea una guia operativa para coordinar subagentes en este repo.
```

### Task Contract Compacto

```md
- Objective: crear guia reusable para control plane de agentes.
- Scope in: docs/memoria del proyecto.
- Scope out: codigo, automation, cambios de infraestructura.
- Context files: operating guide, agent workflows, harness insight.
- Agent lanes: context, writing, validation, memory.
- Validation: revisar referencias duras, headings, diff.
- Evidence: archivo creado, rg de secciones clave, git diff.
- Memory update: enlazar desde agent-workflows si aplica.
- Done when: guia existe, es portable y lista para IA.
```

### Lane Plan

| Lane | Owner | Output | Validation |
|---|---|---|---|
| Context | orchestrator | patrones existentes | archivos leidos |
| Writing | implementer | guia markdown | headings y plantillas |
| Validation | validator | evidence log | diff + rg |
| Memory | curator | enlace o registro | archivo actualizado |

### Done

La guia queda terminada si:

- explica task contracts, scope, validacion, evidencia y subagentes;
- incluye plantillas copiables;
- es portable por variables;
- no depende de contexto oculto del chat;
- queda enlazada desde la memoria operativa del proyecto.

## Adaptador Actual Para `ia-learning`

Valores locales:

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
CONTROL_PLANE_DIR=knowledge/projects/ia-learning/control-plane
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
PATH_TO_THIS_GUIDE=knowledge/projects/ia-learning/agent-control-plane-guide.md
```

Uso recomendado inmediato:

1. Usar esta guia como anexo de [Codex Operating System Guide](codex-operating-system-guide.md).
2. Enlazarla desde [agent-workflows.md](agent-workflows.md).
3. Probarla con una tarea real de `ia-learning`.
4. Medir si el contrato completo es demasiado pesado.
5. Crear una version Lite si el overhead aparece en tareas pequenas.

## Siguiente Experimento

Ejecutar una tarea mediana usando esta guia y registrar:

- si el scope se mantuvo estable;
- si la validacion fue mas clara;
- si los handoffs de subagentes fueron utiles;
- si el evidence log evito ambiguedades;
- que campos del contrato sobraron o faltaron.
