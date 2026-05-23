# Spec-Driven Development Guide

Guia operativa portable para convertir ideas vagas en specs verificables antes de implementar.

Esta guia combina tres enfoques:

- ISCGV++: intent, spec, context, generation, validation y architecture gates con auditoria y scoring.
- SDD: requisitos claros, alcance/no alcance, trazabilidad y criterios de aceptacion verificables.
- RAG Research: contexto anclado a evidencia, fuentes trazables, chunking/retrieval cuando el sistema usa conocimiento externo.

Usala como anexo de [Codex Operating System Guide](codex-operating-system-guide.md), [Agent Control Plane Guide](agent-control-plane-guide.md) y [Research Ops Evidence Guide](research-ops-evidence-guide.md).

## Proposito

Convertir una idea ambigua en una especificacion lista para decision:

```txt
idea vaga -> intent map -> PRD -> context plan -> generation contract -> validation plan -> architecture notes -> build/no-build decision
```

El objetivo no es escribir un documento largo. El objetivo es impedir que el equipo construya antes de entender problema, usuario, alcance, evidencia, riesgos y criterios de falsificacion.

## Principio Central

No se implementa hasta que la spec sea verificable.

Una spec verificable tiene:

- usuario objetivo claro;
- problema y consecuencia de no resolverlo;
- alcance y no alcance;
- requisitos funcionales y no funcionales;
- criterios GIVEN / WHEN / THEN;
- trazabilidad problema -> feature -> metrica;
- contexto/RAG definido si aplica;
- output contracts y guardrails si hay generacion con IA;
- plan de validacion con hipotesis y falsificacion;
- riesgos tecnicos y de seguridad;
- decision explicita: construir, iterar, investigar o detener.

## Variables Portables

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable>
PROJECT_ROOT=<raiz del repo>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
SPEC_DIR=docs/specs
SPEC_SLUG=<slug-del-problema>
PRD_PATH=<SPEC_DIR>/<SPEC_SLUG>/PRD.md
SPEC_REVIEW_PATH=<SPEC_DIR>/<SPEC_SLUG>/SPEC_REVIEW.md
VALIDATION_PLAN_PATH=<SPEC_DIR>/<SPEC_SLUG>/VALIDATION.md
CONTEXT_PLAN_PATH=<SPEC_DIR>/<SPEC_SLUG>/CONTEXT.md
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
PATH_TO_THIS_GUIDE=<ruta a esta guia>
```

## Cuando Usar

Usar esta guia cuando:

- la idea es vaga o contiene varias interpretaciones;
- el usuario pide convertir una idea en PRD/spec;
- el cambio toca producto, datos, API, IA, RAG, UX, negocio o arquitectura;
- hay riesgo de construir una solucion sin validar problema;
- la implementacion requerira varias tareas o agentes;
- hace falta separar hechos, supuestos y decisiones;
- se necesita una decision antes de invertir en codigo.

No usar completa cuando:

- el usuario pide una correccion trivial;
- ya existe una spec suficiente y solo falta implementar;
- la respuesta esperada es conceptual y no generara trabajo;
- el costo de gates supera el riesgo.

Para tareas pequenas usa la version compacta:

```md
Problem:
User:
Goal:
Non-goals:
Acceptance criteria:
Validation:
Open questions:
Build decision:
```

## Reglas Criticas

1. No escribir codigo durante esta fase.
2. No inventar features para llenar el PRD.
3. No avanzar con ambiguedad material sin marcarla como supuesto o bloqueo.
4. No confundir deseo del usuario con requisito confirmado.
5. No proponer RAG sin plan de evaluacion.
6. No proponer generacion con IA sin output contract y guardrails.
7. No aprobar MVP si no valida una hipotesis.
8. No cerrar sin decision final: avanzar, iterar, investigar o no construir.

## Sistema De Gates

Cada gate produce entregable, auditoria, scoring y decision.

Score por dimension: `0-5`.

Dimensiones:

- Claridad: el problema y decisiones se entienden.
- Completitud: contiene lo minimo para decidir.
- Riesgo: riesgos identificados y mitigados.
- Validabilidad: se puede probar o falsificar.

Regla de avance:

- si cualquier dimension es menor a `3`, no avanzar;
- iterar, pedir informacion o declarar bloqueo estructural;
- si el usuario ordena avanzar igual, registrar decision y riesgo.

Formato de scoring:

```md
| Dimension | Score | Rationale | Required Fix |
|---|---:|---|---|
| Claridad |  |  |  |
| Completitud |  |  |  |
| Riesgo |  |  |  |
| Validabilidad |  |  |  |
```

## Gate 0 - Intake

Antes de ejecutar agentes, crear un intake breve.

```md
# Spec Intake

## Raw Idea

## Requested Outcome

## Known Context

## Unknowns

## Existing Evidence

## Likely Project Areas

## Risk Level

## Required Sources

## Initial Decision Needed
```

Decision de Gate 0:

- `proceed`: hay suficiente para Gate 1.
- `ask`: falta informacion critica.
- `research`: hace falta evidencia externa o interna.
- `drop`: no hay objetivo accionable.

## Gate 1 - Intent Engineering

Responsable: Intent Agent.

Objetivo: definir problema real, usuario especifico, contexto, urgencia y consecuencias.

### Entregables

```md
## Intent Map

- Problem statement:
- Target user:
- User segment:
- Current workaround:
- Trigger/context:
- Urgency:
- Cost of inaction:
- Desired outcome:
- Functional JTBD:
- Emotional JTBD:
- Social JTBD:
- Second-order effects:

## Critical Assumptions

| Assumption | Type | Evidence | Risk | Validation |
|---|---|---|---|---|
```

### Auditoria

El Audit Agent debe revisar:

- si el problema es especifico o generico;
- si el usuario es real o abstracto;
- si hay urgencia demostrable;
- si la solucion aparece demasiado pronto;
- si las consecuencias estan inventadas;
- si los supuestos son falsificables.

### Gate Decision

Avanzar solo si:

- usuario y problema son claros;
- el problema puede observarse;
- los supuestos criticos estan listados;
- hay una razon para seguir investigando o especificando.

## Gate 2 - Spec Engineering

Responsable: Spec Agent.

Objetivo: convertir intent en PRD estructurado con requisitos verificables.

### Entregables

```md
## Goals

- 

## Non-Goals

- 

## User Stories

| User Story | Reasoning | Source Problem | Priority |
|---|---|---|---|

## Functional Requirements

| ID | Requirement | Rationale | Priority | Acceptance |
|---|---|---|---|---|

## Non-Functional Requirements

| ID | Requirement | Rationale | Validation |
|---|---|---|---|

## Acceptance Criteria

### AC-001

GIVEN <context>
WHEN <action>
THEN <observable result>

## Traceability

| Problem | Requirement | Feature/Behavior | Metric | Validation |
|---|---|---|---|---|

## MVP As Experiment

- Hypothesis:
- Smallest artifact:
- What it validates:
- What it does not validate:
- Stop/iterate/advance thresholds:
```

### Auditoria

El Audit Agent debe revisar:

- features sin problema claro;
- criterios no observables;
- requisitos sin prioridad;
- MVP como backlog recortado en vez de experimento;
- ausencia de metricas;
- dependencias ocultas.

### Gate Decision

Avanzar solo si:

- cada feature importante traza a problema;
- acceptance criteria son verificables;
- no-goals reducen scope;
- MVP prueba una hipotesis.

## Gate 3 - Context Engineering

Responsable: Context Agent con disciplina RAG Research.

Objetivo: definir que conocimiento necesita el sistema y como se recupera/valida.

Usar este gate cuando:

- el producto usa LLMs;
- depende de documentos, fuentes, memoria o knowledge base;
- necesita grounding o citas;
- hay riesgo de alucinacion;
- necesita distinguir informacion estable y cambiante.

### Entregables

```md
## Context Inventory

| Context Type | Examples | Owner | Freshness | Source Of Truth |
|---|---|---|---|---|
| Stable knowledge |  |  |  |  |
| Dynamic data |  |  |  |  |
| User memory |  |  |  |  |
| Session state |  |  |  |  |
| Tool output |  |  |  |  |

## Source Evaluation

| Source | Type | Authority | Freshness | Coverage | Risk | Use |
|---|---|---|---|---|---|---|

## RAG Strategy

- Corpus:
- Chunking approach:
- Metadata:
- Retrieval strategy:
- Reranking:
- Citation format:
- Grounding rules:
- Fallback when no evidence:
- Evaluation set:

## Hallucination And Context Risks

| Risk | Scenario | Mitigation | Eval |
|---|---|---|---|
```

### RAG Rules

- Priorizar fuentes primarias y trazables.
- Separar conocimiento estable de datos dinamicos.
- No usar una sola estrategia de retrieval si el caso requiere robustez.
- Definir como se citan fuentes.
- Definir que hace el sistema cuando no recupera evidencia.
- Probar retrieval con preguntas reales y adversariales.

### Auditoria

El Audit Agent debe revisar:

- fuentes no trazables;
- chunking sin justificacion;
- ausencia de citation policy;
- dependencia de memoria no versionada;
- riesgo de context window;
- datos cambiantes tratados como estables;
- falta de evals de retrieval.

### Gate Decision

Avanzar solo si:

- source of truth esta claro;
- la estrategia RAG incluye evaluacion;
- se sabe que no debe responder el sistema;
- las fuentes importantes son trazables.

## Gate 4 - Generation Control

Responsable: Generation Agent.

Objetivo: definir contratos de salida, reglas de generacion, guardrails y validacion de outputs.

Usar este gate cuando:

- el sistema genera texto, JSON, acciones, codigo, reportes o recomendaciones;
- el output puede afectar usuarios, datos o decisiones;
- se requieren formatos estructurados;
- hay riesgo de prompt injection o acciones no autorizadas.

### Entregables

```md
## Output Contracts

| Output | Consumer | Format | Required Fields | Validation |
|---|---|---|---|---|

## JSON Schema

{
  "type": "object",
  "required": [],
  "properties": {}
}

## Generation Rules

- Must:
- Must not:
- Ask user when:
- Refuse when:
- Fallback:

## Guardrails

| Risk | Guardrail | Enforcement | Test |
|---|---|---|---|

## Output Evals

| Eval | Input | Expected | Failure Mode |
|---|---|---|---|
```

### Auditoria

El Audit Agent debe revisar:

- outputs ambiguos;
- schemas incompletos;
- acciones prohibidas ausentes;
- guardrails no verificables;
- no hay evals;
- falta de politica para evidencia insuficiente.

### Gate Decision

Avanzar solo si:

- outputs son validables;
- guardrails tienen pruebas;
- hay comportamiento definido para incertidumbre;
- la generacion no puede ejecutar acciones peligrosas sin aprobacion.

## Gate 5 - Validation Engineering

Responsable: Validation Agent.

Objetivo: disenar experimentos para validar problema, solucion y riesgo antes de construir de mas.

### Entregables

```md
## Key Hypotheses

| Hypothesis | Type | Evidence Needed | Falsification |
|---|---|---|---|

## Experiments

| Experiment | Type | Cost | Measures | Success | Failure |
|---|---|---:|---|---|---|

## Leading Metrics

- 

## Lagging Metrics

- 

## Falsification Criteria

- 

## Decision Thresholds

- Stop if:
- Iterate if:
- Advance if:
```

Experimentos recomendados:

- fake door;
- wizard of oz;
- prototype;
- concierge test;
- manual workflow;
- landing/waitlist;
- internal dogfood;
- benchmark/eval set;
- usability test;
- support/comment analysis.

### Auditoria

El Audit Agent debe revisar:

- vanity metrics;
- experimentos que no falsifican nada;
- success thresholds vagos;
- costo desproporcionado;
- ausencia de leading indicators;
- sesgo de confirmacion.

### Gate Decision

Avanzar solo si:

- las hipotesis clave son falsificables;
- el MVP es el experimento mas pequeno razonable;
- hay umbrales de stop/iterate/advance;
- se sabe que aprenderemos aunque falle.

## Gate 6 - Architecture AI-First

Responsable: Architecture Agent.

Objetivo: definir arquitectura suficiente para implementar sin acoplar, filtrar secretos ni bloquear portabilidad.

### Entregables

```md
## State Separation

| State | Owner | Lifetime | Storage | Risk |
|---|---|---|---|---|

## Modules

| Module | Responsibility | Inputs | Outputs | Dependencies |
|---|---|---|---|---|

## Integration Boundaries

- APIs:
- Tools:
- Background jobs:
- Human approvals:

## Security Defaults

- Secrets:
- PII:
- Auth:
- Permissions:
- Logging:

## Portability

- Provider dependencies:
- Lock-in risks:
- Exit strategy:

## OWASP LLM Risks

| Risk | Applies? | Mitigation | Test |
|---|---|---|---|
```

### Auditoria

El Audit Agent debe revisar:

- arquitectura demasiado detallada para fase actual;
- estados mezclados;
- datos sensibles sin politica;
- lock-in no reconocido;
- tool permissions demasiado amplios;
- ausencia de rollback o observabilidad.

### Gate Decision

Avanzar solo si:

- arquitectura cubre riesgos principales;
- no sobredisena;
- permisos y datos sensibles estan claros;
- el plan tecnico puede implementarse por fases verificables.

## Gate 7 - Build Readiness

Responsable: Orchestrator + Audit Agent.

Objetivo: decidir si la spec esta lista para implementacion.

```md
# Build Readiness Review

## Required Artifacts

- PRD:
- Context/RAG plan:
- Generation contracts:
- Validation plan:
- Architecture notes:
- Traceability matrix:

## Readiness Checks

- Problem clear:
- User clear:
- Scope bounded:
- Acceptance criteria testable:
- Evidence sufficient:
- Risks documented:
- Validation realistic:
- Open questions non-blocking:

## Decision

- build:
- iterate spec:
- run research:
- run experiment:
- do not build:

## Reason
```

## PRD File Set

Para specs importantes, crear:

```txt
docs/specs/<slug>/
  PRD.md
  CONTEXT.md
  VALIDATION.md
  ARCHITECTURE.md
  REVIEW.md
  CHANGELOG.md
```

Para specs pequenas, un solo `PRD.md` puede bastar.

## PRD Template

```md
# PRD

## 0. Metadata

- Problem name:
- Slug:
- Date:
- Author:
- Status: draft | blocked | ready-for-build | rejected | superseded
- Recommended decision:
- Source idea:

## 1. Executive Summary

- Problem:
- Target user:
- Opportunity:
- Why now:
- Primary risk:
- Build recommendation:

## 2. Global Scoreboard

| Gate | Clarity | Completeness | Risk | Validability | Decision |
|---|---:|---:|---:|---:|---|
| Gate 1 - Intent |  |  |  |  |  |
| Gate 2 - Spec |  |  |  |  |  |
| Gate 3 - Context |  |  |  |  |  |
| Gate 4 - Generation |  |  |  |  |  |
| Gate 5 - Validation |  |  |  |  |  |
| Gate 6 - Architecture |  |  |  |  |  |

## 3. Gate 1 - Intent Engineering

### 3.1 Intent Agent Output
### 3.2 JTBD
### 3.3 Critical Assumptions
### 3.4 Audit
### 3.5 Scores
### 3.6 Decision

## 4. Gate 2 - Spec Engineering

### 4.1 Spec Agent Output
### 4.2 Goals
### 4.3 Non-Goals
### 4.4 User Stories
### 4.5 Functional Requirements
### 4.6 Non-Functional Requirements
### 4.7 Acceptance Criteria GIVEN / WHEN / THEN
### 4.8 Traceability Problem -> Feature -> Metric
### 4.9 MVP As Experiment
### 4.10 Audit
### 4.11 Scores
### 4.12 Decision

## 5. Gate 3 - Context Engineering

### 5.1 Context Agent Output
### 5.2 Stable Knowledge
### 5.3 Dynamic Data
### 5.4 User Memory
### 5.5 RAG Strategy
### 5.6 Citation And Grounding Policy
### 5.7 Hallucination And Context Window Risks
### 5.8 Retrieval Evals
### 5.9 Audit
### 5.10 Scores
### 5.11 Decision

## 6. Gate 4 - Generation Control

### 6.1 Generation Agent Output
### 6.2 Output Contracts
### 6.3 JSON Schemas
### 6.4 Guardrails
### 6.5 Output Validation
### 6.6 Evals
### 6.7 Audit
### 6.8 Scores
### 6.9 Decision

## 7. Gate 5 - Validation Engineering

### 7.1 Validation Agent Output
### 7.2 Key Hypotheses
### 7.3 Experiments
### 7.4 Leading Metrics
### 7.5 Lagging Metrics
### 7.6 Falsification Criteria
### 7.7 Stop / Iterate / Advance Thresholds
### 7.8 Audit
### 7.9 Scores
### 7.10 Decision

## 8. Gate 6 - Architecture AI-First

### 8.1 Architecture Agent Output
### 8.2 State Separation
### 8.3 Modularity And Boundaries
### 8.4 Security Defaults
### 8.5 Portability
### 8.6 Technical Risks
### 8.7 OWASP LLM Risks
### 8.8 Audit
### 8.9 Scores
### 8.10 Decision

## 9. Consolidated Risks

## 10. Open Assumptions

## 11. Pending Questions

## 12. Build Readiness

## 13. Final Recommendation
```

## Acceptance Criteria Rules

Good acceptance criteria are:

- observable;
- testable;
- specific;
- tied to a user or system behavior;
- independent of implementation details when possible.

Pattern:

```md
GIVEN <state/context>
WHEN <actor/action/event>
THEN <observable outcome>
AND <constraint if needed>
```

Bad:

```md
The feature should be easy to use.
```

Better:

```md
GIVEN a first-time user with no saved sources
WHEN they open the source intake screen
THEN they see an empty state with one primary action to add a source
AND no disabled controls are shown without explanation.
```

## Traceability Matrix

```md
| Problem | User Need | Requirement | Acceptance Criteria | Metric | Experiment | Evidence |
|---|---|---|---|---|---|---|
```

Rules:

- every major requirement maps to a problem;
- every experiment maps to a hypothesis;
- every build decision references evidence or an explicit assumption;
- features without traceability are removed or parked.

## Audit Agent Checklist

Use after every gate.

- [ ] Is the user specific?
- [ ] Is the problem observable?
- [ ] Is the solution separated from the problem?
- [ ] Are assumptions explicit?
- [ ] Are requirements testable?
- [ ] Are non-goals strong enough to bound scope?
- [ ] Does every feature map to a problem?
- [ ] Does the MVP validate a hypothesis?
- [ ] Are metrics behavioral, not vanity?
- [ ] Is RAG grounded in source evaluation if applicable?
- [ ] Are generated outputs constrained and validatable?
- [ ] Are security and data risks visible?
- [ ] Is the decision to build justified?

## Spec Review Decision

```md
# Spec Review Decision

- Decision: approve | request changes | block | reject
- Reason:
- Blocking issues:
- Non-blocking risks:
- Required changes:
- Suggested follow-ups:
- Reviewer:
- Date:
```

## Prompts

### Prompt Maestro

```md
Usa `<PATH_TO_THIS_GUIDE>` para convertir esta idea vaga en una spec verificable antes de implementar.

Idea:
<idea, nota, screenshot, bug, oportunidad o transcript>

Contexto:
<repo, usuario, fuente, restricciones, evidencia disponible>

Reglas:
1. No escribas codigo.
2. Ejecuta gates: Intent, Spec, Context, Generation, Validation, Architecture.
3. Despues de cada gate, ejecuta auditoria, scoring y decision.
4. Si cualquier score es menor a 3, itera o declara bloqueo.
5. Separa hechos, supuestos, inferencias, decisiones y riesgos.
6. Incluye criterios GIVEN / WHEN / THEN.
7. Si hay IA/RAG, define fuentes, chunking, retrieval, grounding, citas y evals.
8. Trata el MVP como experimento.

Entrega:
- PRD completo en formato Markdown.
- Scoreboard global.
- Riesgos consolidados.
- Supuestos abiertos.
- Preguntas pendientes.
- Decision final: avanzar, iterar, investigar o no construir.
```

### Prompt Intent Agent

```md
Actua como Intent Agent.

Input:
<idea bruta>

Produce:
- problem statement
- target user
- JTBD funcional, emocional y social
- contexto y urgencia
- consecuencias de no resolver
- supuestos criticos
- evidencia disponible
- dudas bloqueantes

No propongas features todavia salvo como hipotesis.
```

### Prompt Spec Agent

```md
Actua como Spec Agent.

Input:
<Intent Map aprobado>

Produce:
- goals
- non-goals
- user stories con razonamiento
- requisitos funcionales
- requisitos no funcionales
- acceptance criteria GIVEN / WHEN / THEN
- trazabilidad problema -> feature -> metrica
- MVP como experimento

No incluyas requisitos que no tengan problema o metrica.
```

### Prompt Context/RAG Agent

```md
Actua como Context Agent con disciplina RAG Research.

Input:
<PRD draft + fuentes disponibles>

Define:
- conocimiento estable
- datos dinamicos
- memoria de usuario
- corpus
- chunking
- retrieval/reranking
- citation policy
- grounding rules
- fallback cuando no haya evidencia
- eval set de retrieval
- riesgos de alucinacion y context window

No propongas RAG sin evaluacion.
```

### Prompt Generation Agent

```md
Actua como Generation Agent.

Input:
<Spec + Context Plan>

Define:
- output contracts
- JSON schemas si aplica
- reglas must/must not
- acciones prohibidas
- guardrails contra prompt injection y overreach
- validacion automatica de outputs
- evals de calidad y cumplimiento

El output debe ser validable por maquina o por checklist clara.
```

### Prompt Validation Agent

```md
Actua como Validation Agent.

Input:
<Spec + Context + Generation Plan>

Define:
- hipotesis clave
- experimentos de problema
- experimentos de solucion
- fake door / wizard of oz / prototype si aplica
- metricas leading
- metricas lagging
- falsification criteria
- stop/iterate/advance thresholds

Evita vanity metrics.
```

### Prompt Architecture Agent

```md
Actua como Architecture Agent.

Input:
<PRD + Validation Plan>

Define:
- separacion de estados
- modulos
- boundaries
- integraciones
- seguridad por defecto
- permisos
- logging/observabilidad
- portabilidad y lock-in
- riesgos OWASP LLM si aplica

No sobredisene; produce arquitectura suficiente para el MVP experimental.
```

### Prompt Audit Agent

```md
Actua como Audit Agent.

Gate:
<gate name>

Artifact:
<artifact>

Evalua:
- inconsistencias
- supuestos debiles
- falta de evidencia
- features sin valor claro
- metricas ausentes o vanity
- criterios no verificables
- riesgos no tratados

Devuelve:
- findings
- required fixes
- scores 0-5 para claridad, completitud, riesgo y validabilidad
- decision: advance | iterate | block
```

## Build Handoff

Cuando la spec este aprobada, crear handoff para implementacion:

```md
# Build Handoff

## Spec

- PRD:
- Status:
- Decision:

## Scope

### Build Now

- 

### Do Not Build

- 

## Acceptance Criteria

- 

## Implementation Notes

- likely files:
- dependencies:
- migration/data:
- UI/API states:

## Validation Commands

- 

## Evidence Required

- 

## Risks

- 
```

## Change Control

Una spec cambia cuando:

- aparece evidencia nueva;
- cambia el usuario objetivo;
- se agrega requisito;
- cambia una metrica;
- se altera alcance;
- un experimento invalida hipotesis.

Plantilla:

```md
## Spec Change

- Date:
- Change:
- Reason:
- Evidence:
- Impacted gates:
- Acceptance criteria changed:
- Validation changed:
- Decision:
```

## Failure Modes

| Falla | Sintoma | Mitigacion |
|---|---|---|
| Solution-first | se habla de features antes del problema | Gate 1 bloquea |
| Fake MVP | backlog recortado sin hipotesis | Gate 5 exige experimento |
| Weak acceptance | criterios subjetivos | GIVEN / WHEN / THEN |
| RAG handwave | "usar embeddings" sin eval | Gate 3 exige corpus/evals |
| Unbounded scope | todo entra en v1 | non-goals + traceability |
| Vanity metrics | clicks sin relacion con valor | falsification criteria |
| Hidden risk | seguridad/datos al final | Gate 6 obligatorio |
| Build pressure | se implementa con scores bajos | build readiness gate |

## Portable Adoption Checklist

Para usar esta guia en otro proyecto:

- [ ] Copiar guia o enlazarla desde docs/AI.
- [ ] Definir `SPEC_DIR`.
- [ ] Definir PRD template local.
- [ ] Crear decision rules para build/no-build.
- [ ] Definir validation commands del repo.
- [ ] Definir fuente de verdad para research/evidence.
- [ ] Ejecutar una spec piloto.
- [ ] Auditar todos los gates.
- [ ] Ajustar scoring si es demasiado pesado.
- [ ] Crear version Lite para tareas pequenas.

## Adaptador Actual Para `ia-learning`

Valores locales:

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
SPEC_DIR=docs/specs
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
PATH_TO_THIS_GUIDE=knowledge/projects/ia-learning/spec-driven-development-guide.md
SPEC_CONTEXT_PATH=knowledge/projects/ia-learning/spec-driven-development-context.md
```

Archivos relacionados:

- [spec-driven-development-context.md](spec-driven-development-context.md)
- [codex-operating-system-guide.md](codex-operating-system-guide.md)
- [agent-control-plane-guide.md](agent-control-plane-guide.md)
- [research-ops-evidence-guide.md](research-ops-evidence-guide.md)
- [experiments.md](experiments.md)
- [open-questions.md](open-questions.md)

Uso recomendado inmediato:

1. Enlazar esta guia desde [agent-workflows.md](agent-workflows.md).
2. Usarla como version avanzada de [spec-driven-development-context.md](spec-driven-development-context.md).
3. Aplicarla a una idea vaga real antes de implementar.
4. Guardar el PRD en `docs/specs/<slug>/PRD.md`.
5. Registrar experimentos derivados en [experiments.md](experiments.md).

## Siguiente Experimento

Tomar una idea vaga de `ia-learning` y generar un PRD con esta guia. Medir:

- cuantas preguntas abiertas aparecen antes de implementar;
- cuantas features se eliminan por falta de trazabilidad;
- si los criterios GIVEN / WHEN / THEN son suficientes para otro agente;
- si Gate 3 detecta necesidades reales de RAG/contexto;
- si Gate 5 produce un experimento mas pequeno que construir la feature;
- si el Build Handoff permite implementar sin volver al chat.
