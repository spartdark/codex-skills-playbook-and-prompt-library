# Monetization Productization Guide

Guia operativa portable para convertir conocimiento, workflows de Codex, skills, dashboards, reportes y servicios en ofertas validables, empaquetables y listas para ejecucion por IA.

Esta guia es un anexo especializado de [Codex Operating System Guide](codex-operating-system-guide.md), [Agent Control Plane Guide](agent-control-plane-guide.md) y [Research Ops Evidence Guide](research-ops-evidence-guide.md). Usala junto con [Monetization Ideas](monetization-ideas.md) y [Experiments](experiments.md) para evitar que la monetizacion se quede en ideas sueltas sin validacion.

## Proposito

Convertir activos internos en ofertas de mercado sin perder trazabilidad:

```txt
research -> insight -> workflow -> proof -> package -> offer -> validation -> delivery system -> reusable asset
```

El objetivo no es inventar productos por entusiasmo. El objetivo es detectar problemas repetidos, empaquetar soluciones concretas, validar disposicion a pagar y crear un sistema de entrega que una IA pueda operar con controles claros.

## Cuando Usar Esta Guia

Usar cuando:

- una idea de monetizacion aparece en `monetization-ideas.md`;
- un workflow de Codex se repite y podria venderse como kit, skill pack o servicio;
- un patron de research genera reportes, benchmarks o dashboards reutilizables;
- hay demanda probable en comentarios, comunidades, clientes, creadores o equipos;
- se necesita validar precio, posicionamiento, alcance o delivery antes de construir de mas;
- se quiere crear un activo portable para otros proyectos o clientes;
- una IA debe preparar oferta, landing, demo, propuesta, onboarding, QA o reporte final.

No usar completa cuando:

- la idea aun no tiene usuario objetivo;
- no existe evidencia de dolor o frecuencia;
- el output seria solo contenido informativo sin una accion clara;
- el costo de empaquetar supera el aprendizaje esperado;
- el usuario pidio solo una lluvia de ideas rapida.

Para casos pequenos, usar la version compacta:

```md
Offer:
Target user:
Pain:
Evidence:
Smallest paid validation:
Delivery artifact:
QA:
Decision:
```

## Variables Portables

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable>
PROJECT_ROOT=<raiz del repo>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
MONETIZATION_IDEAS=<PROJECT_MEMORY_DIR>/monetization-ideas.md
EXPERIMENTS=<PROJECT_MEMORY_DIR>/experiments.md
OFFER_DIR=<PROJECT_MEMORY_DIR>/offers
PRODUCTIZATION_DIR=<PROJECT_MEMORY_DIR>/productization
CUSTOMER_RESEARCH_DIR=<PROJECT_MEMORY_DIR>/customer-research
BENCHMARK_DIR=<PROJECT_MEMORY_DIR>/benchmarks
DASHBOARD_DIR=<PROJECT_MEMORY_DIR>/dashboards
SKILL_PACK_DIR=<PROJECT_MEMORY_DIR>/skill-packs
CODEX_KIT_DIR=<PROJECT_MEMORY_DIR>/codex-kits
SERVICE_PLAYBOOK_DIR=<PROJECT_MEMORY_DIR>/service-playbooks
PATH_TO_THIS_GUIDE=<ruta a esta guia>
```

## Project Productization Profile

Completar este bloque antes de convertir una idea en oferta.

```md
# Project Productization Profile

- Project name:
- Project id:
- Primary market:
- Buyer:
- End user:
- Current audience or distribution:
- Existing assets:
- Existing proof:
- Allowed claims:
- Sensitive claims:
- Delivery channels:
- Support capacity:
- Automation maturity:
- Pricing constraints:
- Human approval required for:
- Definition of paid validation:
```

Si falta informacion, escribir `Pendiente`, `No validado aun` o `Supuesto`. No rellenar huecos con confianza falsa.

## Principios

1. La oferta parte de un dolor repetido, no de una herramienta interesante.
2. Un resumen de IA no es evidencia de mercado.
3. Todo claim comercial debe tener evidencia, limitacion o etiqueta de supuesto.
4. El primer paquete debe ser pequeno, entregable y revisable.
5. El MVP comercial es un experimento de disposicion a pagar, no un producto completo.
6. Cada entrega vendible debe tener QA, rollback o politica de correccion.
7. Un servicio exitoso puede convertirse en kit; un kit exitoso puede convertirse en skill; una skill estable puede automatizarse.
8. No se automatiza una oferta hasta tener una corrida manual validada.
9. El precio debe probarse con comportamiento real, no solo con opiniones.
10. La memoria del proyecto debe conservar aprendizajes, objeciones, rework y resultados.

## Mapa Del Sistema

```txt
monetization/productization
  evidence base        fuentes, comentarios, entrevistas, benchmarks, demos
  opportunity brief    usuario, dolor, frecuencia, valor, alternativa actual
  offer design         promesa, alcance, no-alcance, formato, precio
  package              kit, skill pack, dashboard, reporte o servicio
  validation           fake door, pre-order, piloto, paid discovery, concierge
  delivery system      runbook, QA, handoff, soporte, metricas
  productization loop  manual -> template -> script/skill -> automation
```

## Roles Para IA

### Opportunity Researcher

Responsable de encontrar senales de dolor y demanda.

Debe:

- leer fuentes locales y externas cuando aplique;
- preservar evidencia usando el flujo de research ops;
- separar hechos, inferencias y recomendaciones;
- detectar frecuencia, urgencia, buyer y alternativa actual.

Output:

- opportunity brief;
- evidencia;
- riesgos;
- preguntas para validar.

### Offer Strategist

Responsable de convertir una oportunidad en una oferta comprensible.

Debe definir:

- comprador;
- usuario final;
- problema;
- resultado prometido;
- formato de entrega;
- alcance y no-alcance;
- precio inicial;
- validacion mas pequena.

### Packaging Agent

Responsable de transformar workflows en artefactos vendibles.

Debe crear:

- kit structure;
- prompts;
- templates;
- sample outputs;
- checklist de QA;
- setup instructions;
- support boundaries.

### Evidence Auditor

Responsable de revisar si la oferta esta sobre-vendida.

Debe buscar:

- claims sin evidencia;
- extrapolaciones debiles;
- metricas vanidosas;
- riesgos de privacidad;
- dependencia de una unica fuente;
- promises que requieren resultados fuera de control.

### Delivery Operator

Responsable de ejecutar el servicio, reporte o kit con un cliente real o piloto.

Debe:

- usar task contracts;
- capturar input, output y QA;
- registrar rework;
- producir handoff;
- proponer mejoras al playbook.

### Productization Owner

Responsable de decidir si algo queda como servicio, kit, skill pack, dashboard, reporte recurrente o automation.

Debe:

- evaluar repeticion;
- medir margen y rework;
- reducir pasos manuales;
- mantener calidad;
- actualizar memoria.

## Productization Lifecycle

### 1. Opportunity Intake

Entrada minima:

- idea original;
- fuente o evidencia;
- target user;
- dolor;
- evento que dispara la necesidad;
- alternativa actual;
- resultado deseado;
- capacidad de entrega;
- riesgo principal.

Plantilla:

```md
## Opportunity Intake

- Name:
- Source:
- Confidence: observed | inferred | experimental | weak
- Target buyer:
- End user:
- Pain:
- Trigger:
- Current alternative:
- Desired outcome:
- Existing asset:
- Smallest useful deliverable:
- Why now:
- Main risk:
- Next validation:
```

Decision:

- `Drop` si no hay dolor claro o comprador plausible.
- `Research` si la evidencia es debil pero el dolor parece importante.
- `Validate` si se puede probar interes con bajo costo.
- `Package` si ya existe prueba interna o demanda directa.

### 2. Evidence Review

Antes de escribir oferta, revisar evidencia.

Evidencia fuerte:

- cliente pidio explicitamente ayuda;
- usuario pago o acepto piloto con compromiso;
- comentario recurrente con contexto claro;
- problema aparece en multiples fuentes independientes;
- benchmark demuestra brecha reproducible;
- servicio manual resolvio el problema con bajo rework.

Evidencia media:

- comentarios o posts repetidos pero sin buyer claro;
- alto engagement alrededor del problema;
- experiencia propia repetida;
- research de fuente secundaria;
- demanda inferida por titulos, videos o comunidades.

Evidencia debil:

- intuicion;
- tendencia general;
- una sola opinion;
- salida generada por IA sin fuente;
- "la gente podria querer esto".

Regla: la evidencia debil solo permite fake door o investigacion, no construccion extensa.

### 3. Offer Design

Una oferta debe responder:

- para quien es;
- que problema resuelve;
- que resultado entrega;
- como se entrega;
- que incluye;
- que no incluye;
- cuanto tarda;
- que necesita del cliente;
- como se valida calidad;
- que pasa si falla.

Plantilla:

```md
## Offer Brief

- Offer name:
- Buyer:
- End user:
- Problem:
- Promise:
- Deliverable:
- Format: kit | skill pack | dashboard | benchmark report | service | hybrid
- Scope:
- Non-goals:
- Inputs required:
- Output artifacts:
- QA process:
- Evidence behind offer:
- Pricing hypothesis:
- Validation method:
- Success signal:
- Failure signal:
- Support boundary:
- Refund/correction policy:
```

### 4. Package Design

Convertir la oferta en un paquete operativo.

El paquete minimo debe incluir:

- README de uso;
- inputs requeridos;
- prompts listos para IA;
- templates;
- sample output;
- QA checklist;
- decision log;
- limitations;
- handoff notes;
- changelog.

Estructura portable recomendada:

```txt
<PRODUCTIZATION_DIR>/<offer-slug>/
  README.md
  offer-brief.md
  evidence.md
  templates/
  prompts/
  examples/
  qa-checklist.md
  delivery-runbook.md
  changelog.md
```

### 5. Validation

Validar antes de escalar.

Opciones:

- fake door: publicar landing o DM con CTA y medir accion real;
- problem interview: validar dolor, frecuencia, presupuesto y alternativa;
- concierge pilot: entregar manualmente a un usuario;
- paid discovery: cobrar por diagnostico antes del producto completo;
- pre-order: cobrar por una version limitada;
- internal benchmark: probar valor con assets propios;
- creator/operator review: pedir evaluacion de utilidad, no solo opinion general.

Metricas utiles:

- tasa de respuesta de buyer;
- porcentaje que acepta una llamada;
- porcentaje que entrega datos reales;
- porcentaje que paga o firma piloto;
- tiempo ahorrado;
- rework manual;
- acciones adoptadas;
- NPS cualitativo con ejemplos;
- margen estimado;
- repetibilidad de delivery.

Metricas debiles:

- likes;
- impresiones;
- comentarios genericos;
- "me interesa" sin siguiente paso;
- outputs bonitos sin adopcion.

### 6. Delivery

Una entrega debe operar como sistema controlado.

Checklist de delivery:

- task contract aprobado;
- inputs recibidos;
- restricciones y datos sensibles identificados;
- ejecucion registrada;
- QA aplicado;
- evidencia y limitaciones incluidas;
- output entregado;
- feedback capturado;
- rework medido;
- aprendizajes persistidos.

### 7. Productization Decision

Despues de 1 a 3 corridas, decidir:

| Decision | Usar Cuando | Siguiente Paso |
|---|---|---|
| Drop | baja demanda, alto rework, bajo valor | registrar aprendizaje |
| Keep as service | valor alto pero requiere juicio humano | mejorar playbook |
| Package as kit | pasos repetibles y cliente puede operar | crear templates y examples |
| Build skill pack | prompts/tools son reutilizables | crear skill specs y smoke tests |
| Build dashboard | datos recurrentes y decision repetida | definir schema, refresh y QA |
| Build benchmark report | comparacion repetible cambia decisiones | fijar metodologia |
| Automate | manual/script estable con QA | crear automation policy |

## Offer Archetypes

### 1. Codex Kits

Un Codex kit es un paquete de operacion para lograr un resultado concreto con Codex.

Ejemplos:

- launch ops kit;
- agent harness kit;
- research ops kit;
- AI marketing team kit;
- engineering manager pre-read kit;
- support triage kit.

Debe incluir:

- objetivo del kit;
- perfil de usuario;
- requisitos;
- setup;
- workflow paso a paso;
- prompts;
- task contracts;
- templates;
- QA;
- sample outputs;
- troubleshooting;
- extension points.

Plantilla:

```md
# Codex Kit: <name>

## Outcome

## Who This Is For

## Not For

## Prerequisites

## Folder Contract

## Setup

## Workflow

## Prompts

## Templates

## QA Checklist

## Sample Outputs

## Failure Modes

## Upgrade Path
```

Packaging rules:

- vender un resultado, no un conjunto de prompts;
- incluir un ejemplo completo;
- declarar supuestos de entorno;
- agregar una prueba de aceptacion;
- separar instrucciones humanas de instrucciones para IA;
- mantener una version lite para adopcion rapida.

QA:

- ejecutar el kit en un caso real o fixture;
- registrar tiempo;
- medir rework;
- verificar que los outputs no dependan de conocimiento oculto;
- confirmar que el usuario puede completar el flujo sin el autor.

### 2. Skill Packs

Un skill pack es un conjunto de skills o instrucciones especializadas para una familia de tareas.

Ejemplos:

- YouTube research skill pack;
- comments intelligence skill pack;
- benchmark reporter skill pack;
- product discovery skill pack;
- launch asset skill pack;
- team operations skill pack.

Debe incluir:

- lista de skills;
- trigger de cada skill;
- inputs y outputs;
- guardrails;
- ejemplos;
- smoke tests;
- versioning;
- compatibility notes.

Plantilla:

```md
# Skill Pack: <name>

## Purpose

## Skills Included

| Skill | Trigger | Inputs | Outputs | Guardrails |
|---|---|---|---|---|

## Setup

## Operating Rules

## Smoke Tests

## QA

## Versioning

## Known Limitations
```

Pricing logic:

- vender como setup + library si el usuario necesita instalacion;
- vender como subscription si requiere updates frecuentes;
- vender como custom pack si depende de stack, herramientas o datos internos;
- no vender como "autopilot" si requiere supervision humana.

Evidence requirements:

- antes/despues de tiempo o calidad;
- tareas completadas con y sin skill;
- errores reducidos;
- adoption notes de usuarios reales;
- lista de casos donde no funciona.

### 3. Comment Dashboards

Un comment dashboard convierte feedback disperso en decisiones.

Usuarios posibles:

- YouTube creators;
- comunidades de cursos;
- equipos devrel;
- startups con feedback social;
- equipos de producto con comentarios publicos.

Outputs esperados:

- temas frecuentes;
- preguntas repetidas;
- objeciones;
- requests;
- menciones de herramientas;
- sentimiento operativo;
- oportunidades de contenido;
- oportunidades de producto;
- acciones recomendadas con evidencia.

Folder contract:

```txt
<DASHBOARD_DIR>/<dashboard-slug>/
  README.md
  data-contract.md
  taxonomy.md
  refresh-runbook.md
  qa-checklist.md
  sample-report.md
  decisions.md
```

Data contract:

```md
## Comment Data Contract

- Source:
- Authorized access:
- Captured date:
- Fields:
- PII policy:
- Sampling method:
- Deduping method:
- Language handling:
- Classification taxonomy:
- Confidence labels:
- Evidence pointers:
```

Core taxonomy:

- question;
- objection;
- pain;
- requested tutorial;
- requested feature;
- tool mention;
- bug/support issue;
- pricing concern;
- success story;
- spam/noise.

QA:

- sample at least 20 classified comments manually;
- verify evidence links;
- check PII handling;
- measure false positives in top categories;
- ensure actions trace to comments;
- include "insufficient evidence" where needed.

Validation:

- ask owner to rank top actions;
- track accepted actions;
- compare against manual reading;
- measure time saved;
- run weekly report for 2 to 4 cycles before automation.

### 4. Benchmark Reports

Un benchmark report compara herramientas, modelos, workflows o agentes con metodologia reproducible.

Usar cuando:

- el mercado cambia rapido;
- las claims publicas son confusas;
- compradores necesitan elegir herramienta;
- el proyecto puede definir tareas reproducibles;
- existe capacidad de ejecutar y auditar pruebas.

No usar cuando:

- no se puede reproducir;
- solo hay una tarea;
- las metricas favorecen una conclusion predefinida;
- no hay disclosure de entorno, prompts o limites.

Benchmark contract:

```md
## Benchmark Contract

- Question:
- Audience:
- Tools compared:
- Versions/dates:
- Tasks:
- Dataset/fixtures:
- Prompt policy:
- Scoring rubric:
- Human review policy:
- Environment:
- Known limitations:
- Reproducibility package:
```

Metricas:

- correctness;
- task completion;
- elapsed time;
- number of intervention points;
- test pass rate;
- rework required;
- evidence quality;
- scope control;
- handoff quality;
- cost;
- failure recovery.

Report structure:

```md
# Benchmark Report: <name>

## Executive Summary

## Recommendation

## Methodology

## Tools And Versions

## Tasks

## Results

## Failure Analysis

## Buyer Guidance

## Reproducibility Notes

## Limitations
```

QA:

- lock versions and dates;
- keep prompts and fixtures;
- separate observed results from interpretation;
- include failure examples;
- avoid universal "best tool" claims;
- state that results can age quickly.

Productization:

- lead magnet: public summary, paid deep report;
- subscription: monthly or quarterly updates;
- advisory: tool selection workshop;
- internal team report: benchmark against actual repo tasks.

### 5. Team Services

Team services use Codex workflows to help teams adopt agentic operations.

Service examples:

- Codex workflow audit;
- agent harness setup;
- research ops setup;
- team skill pack implementation;
- comment intelligence setup;
- benchmark and tool selection;
- AI operating system onboarding;
- monthly AI ops review.

Service design:

```md
## Service Brief

- Service name:
- Buyer:
- Team size:
- Current workflow:
- Pain:
- Desired outcome:
- Inputs required:
- Delivery phases:
- Artifacts delivered:
- Meetings required:
- Async work:
- QA:
- Handoff:
- Support period:
- Out of scope:
- Price:
```

Delivery phases:

1. Diagnose: current workflows, risks, assets, constraints.
2. Design: target operating model and acceptance criteria.
3. Build: templates, skills, scripts, dashboards or docs.
4. Pilot: run on one real task.
5. QA: review outputs, failures, evidence.
6. Handoff: docs, training, ownership, next steps.
7. Review: measure adoption and rework.

Team service QA:

- no client data in examples without approval;
- document credentials and access boundaries;
- create rollback or disable path for automations;
- record who owns each artifact after handoff;
- define what support includes and excludes.

## Pricing And Validation

### Pricing Inputs

```md
## Pricing Inputs

- Buyer urgency:
- Economic value:
- Current alternative cost:
- Time saved:
- Quality improvement:
- Risk reduction:
- Delivery effort:
- Support burden:
- Update frequency:
- Customization level:
- Proof strength:
```

### Pricing Ladders

Use a ladder instead of one fixed guess.

```md
## Pricing Ladder

| Tier | Format | Price Hypothesis | Buyer | Includes | Excludes | Validation |
|---|---|---:|---|---|---|---|
| Lite | template/kit | | | | | |
| Standard | kit + setup | | | | | |
| Pro | custom service | | | | | |
| Team | implementation + support | | | | | |
```

### Validation Methods

| Method | Use When | Strong Signal |
|---|---|---|
| DM interview | buyer unclear | specific pain, workflow, budget |
| Fake door | distribution exists | CTA click plus qualified follow-up |
| Paid discovery | problem complex | payment for diagnosis |
| Pilot | delivery uncertain | real data, real deadline, accepted output |
| Pre-order | scope clear | money before full build |
| Internal case study | no buyer yet | measurable before/after |

### Decision Rules

Advance when:

- buyer can describe problem without prompting;
- user provides real data or context;
- there is willingness to pay or equivalent commitment;
- delivery creates an accepted artifact;
- rework is understandable and reducible;
- evidence supports the main claim.

Iterate when:

- problem is real but offer language is unclear;
- price is resisted but value is acknowledged;
- output is useful but packaging is hard;
- buyer differs from end user;
- QA finds recurring but fixable gaps.

Stop when:

- no buyer appears after targeted outreach;
- users praise but avoid commitment;
- delivery requires custom work every time;
- evidence remains weak after low-cost tests;
- the offer depends on claims that cannot be supported.

## Evidence Requirements

Every monetization artifact must include:

- source URL or local evidence pointer;
- captured date;
- source type;
- confidence;
- claim supported;
- limitation;
- decision influenced.

Evidence table:

```md
| Claim | Evidence | Source Type | Confidence | Limitation | Decision |
|---|---|---|---|---|---|
```

Confidence labels:

- `observed`: based on direct behavior, payment, usage or explicit request;
- `experimental`: based on pilot, test or prototype;
- `inferred`: based on patterns from sources or adjacent behavior;
- `weak`: based on intuition or single low-signal source.

Claim hygiene:

- Do not say "proven" unless there is repeated evidence.
- Do not say "automated" if human review is required.
- Do not promise revenue, growth or ranking outcomes outside control.
- Do not present benchmark results as timeless.
- Do not use private client outputs as proof without approval.

## QA System

### Offer QA

```md
## Offer QA Checklist

- [ ] Buyer is specific.
- [ ] End user is specific.
- [ ] Pain is observable.
- [ ] Alternative is named.
- [ ] Deliverable is concrete.
- [ ] Scope is bounded.
- [ ] Non-goals are explicit.
- [ ] Main claim has evidence.
- [ ] Price hypothesis is stated.
- [ ] Validation method is behavioral.
- [ ] Failure signal is defined.
- [ ] Support boundary is clear.
```

### Package QA

```md
## Package QA Checklist

- [ ] README explains outcome and prerequisites.
- [ ] Inputs are listed.
- [ ] Prompts are copy-ready.
- [ ] Templates are included.
- [ ] Sample output exists.
- [ ] QA checklist exists.
- [ ] Limitations are visible.
- [ ] First-run path is under 30 minutes if possible.
- [ ] No hidden dependency on author knowledge.
- [ ] Evidence and claims are linked.
```

### Delivery QA

```md
## Delivery QA Checklist

- [ ] Task contract is clear.
- [ ] Client/project inputs are complete.
- [ ] Sensitive data is handled according to policy.
- [ ] Output matches scope.
- [ ] Evidence pointers are included.
- [ ] Manual review completed.
- [ ] Rework notes captured.
- [ ] Handoff includes next steps.
- [ ] Memory updated.
```

### Automation QA

Automation is allowed only after:

- manual run completed;
- checklist passed;
- script or skill run completed;
- output reviewed by human or reviewer agent;
- failure modes documented;
- rollback or pause path exists;
- logs are stored;
- owner is assigned.

## Prompts For AI Agents

### Opportunity Research Prompt

```md
You are the Opportunity Researcher for PROJECT_NAME.

Goal: evaluate whether this monetization idea has enough evidence to become an offer.

Read:
- SOURCE_INDEX
- MONETIZATION_IDEAS
- EXPERIMENTS
- any provided raw or processed source

Return:
1. target buyer and end user;
2. pain and trigger;
3. evidence table with confidence labels;
4. current alternative;
5. smallest validation step;
6. risks and missing evidence;
7. recommendation: drop, research, validate or package.

Rules:
- Separate facts from inferences.
- Do not invent demand.
- Do not propose building until validation is defined.
```

### Offer Strategist Prompt

```md
You are the Offer Strategist for PROJECT_NAME.

Goal: turn a validated opportunity into a bounded offer.

Input:
- opportunity brief;
- evidence table;
- constraints;
- delivery capacity.

Create:
- offer name;
- buyer;
- promise;
- deliverables;
- scope;
- non-goals;
- pricing ladder;
- validation plan;
- QA checklist;
- failure signal.

Rules:
- Sell a concrete outcome, not a tool.
- Keep the first offer small enough to deliver manually.
- Mark all unvalidated claims as assumptions.
```

### Packaging Agent Prompt

```md
You are the Packaging Agent.

Goal: convert the offer into a reusable package that another AI or operator can run.

Create:
- README;
- setup steps;
- folder contract;
- prompts;
- templates;
- sample output outline;
- QA checklist;
- troubleshooting;
- changelog entry.

Rules:
- Keep instructions executable.
- Include all required inputs.
- Include acceptance criteria.
- Do not reference hidden chat context.
```

### Evidence Auditor Prompt

```md
You are the Evidence Auditor.

Review the offer/package for overclaiming, weak evidence and operational risk.

Check:
- unsupported claims;
- missing source links;
- weak confidence labels;
- privacy or data risk;
- vague buyer or pain;
- vanity metrics;
- automation without QA;
- pricing unsupported by value or behavior.

Return:
- blockers;
- risks;
- required edits;
- evidence gaps;
- decision: approve, approve with caveats, or block.
```

### Delivery Operator Prompt

```md
You are the Delivery Operator.

Goal: execute this offer for one real or test customer using the approved runbook.

Before execution:
- confirm scope;
- confirm inputs;
- identify sensitive data;
- define output path;
- define QA path.

After execution:
- summarize output;
- list evidence;
- list QA completed;
- list rework;
- list customer feedback;
- recommend productization changes.
```

### Productization Review Prompt

```md
You are the Productization Owner.

Review 1 to 3 completed runs of this offer.

Decide whether to:
- drop;
- keep as service;
- package as kit;
- convert to skill pack;
- build dashboard;
- publish benchmark report;
- automate.

Use:
- demand evidence;
- delivery time;
- rework;
- QA failures;
- customer value;
- repeatability;
- margin;
- risk.

Return a decision with rationale and next actions.
```

## Templates

### Offer One Pager

```md
# Offer One Pager: <offer-name>

## Buyer

## Problem

## Trigger

## Promise

## Deliverable

## Scope

## Non-Goals

## Inputs Required

## Process

## Timeline

## QA

## Price Hypothesis

## Evidence

## Risks

## Validation Plan
```

### Customer Discovery Notes

```md
# Customer Discovery Notes

- Date:
- Person/company:
- Role:
- Segment:
- Source:
- Permission to quote: yes | no | unknown

## Problem

## Current Workflow

## Frequency

## Cost Of Inaction

## Current Alternatives

## Budget Or Buying Process

## Reaction To Offer

## Objections

## Strong Quotes

## Follow-Up

## Evidence Confidence
```

### Pilot Run Log

```md
# Pilot Run Log: <offer-name>

- Date:
- Operator:
- Customer/test case:
- Scope:
- Inputs:
- Output:
- Time spent:
- Tools used:
- QA completed:
- Issues:
- Rework:
- Accepted by customer: yes | no | partial
- Evidence:
- Lessons:
- Productization decision:
```

### Benchmark Task Card

```md
# Benchmark Task Card

- Task:
- Goal:
- Input fixture:
- Expected output:
- Scoring rubric:
- Time limit:
- Tools:
- Versions:
- Allowed interventions:
- Failure criteria:
- Evidence to capture:
```

### Dashboard Weekly Report

```md
# Weekly Comment Intelligence Report

- Source:
- Period:
- Comments analyzed:
- Sampling method:
- Confidence:

## Top Themes

## Repeated Questions

## Objections

## Requested Content Or Features

## Tool Mentions

## Actions Recommended

## Evidence Links

## QA Notes

## Limitations
```

## Failure Modes

### Weak Demand

Symptoms:

- people like the idea but do not commit;
- no one provides data;
- no one accepts a next step;
- buyer is vague.

Response:

- narrow segment;
- run interviews;
- rewrite around pain;
- reduce scope;
- stop if behavior does not change.

### Overpackaging Too Early

Symptoms:

- complex kit before first paid pilot;
- too many templates;
- no real user output;
- guide grows faster than evidence.

Response:

- run concierge version;
- delete unused parts;
- ship one outcome;
- record rework.

### Unsupported Claims

Symptoms:

- "saves 10 hours" without measurement;
- "best" benchmark claim with weak methodology;
- "fully automated" but manual review is required.

Response:

- downgrade claim;
- add evidence;
- add limitation;
- rerun validation.

### Delivery Drift

Symptoms:

- every customer needs a custom build;
- scope expands during delivery;
- no repeatable checklist;
- support consumes margin.

Response:

- add non-goals;
- create change request process;
- split custom service from productized kit;
- price custom work separately.

### Poor QA

Symptoms:

- dashboards classify incorrectly;
- benchmark tasks are not reproducible;
- skill pack breaks on first fresh run;
- outputs look good but do not drive decisions.

Response:

- add fixtures;
- sample outputs manually;
- add acceptance criteria;
- require reviewer approval before release.

### Automation Before Trust

Symptoms:

- scheduled reports run without review;
- bad data gets sent to stakeholders;
- no failure alert;
- no owner.

Response:

- pause automation;
- return to manual run;
- add logs and QA;
- define owner and escalation.

## Adoption Checklist

Use this checklist to adopt the guide in a new project.

```md
## Checklist Items

- [ ] Copy this guide into the project memory or docs.
- [ ] Complete Project Productization Profile.
- [ ] Create or map MONETIZATION_IDEAS.
- [ ] Create or map EXPERIMENTS.
- [ ] Define evidence confidence labels.
- [ ] Pick one opportunity, not five.
- [ ] Write Opportunity Intake.
- [ ] Run Evidence Review.
- [ ] Draft Offer Brief.
- [ ] Define smallest behavioral validation.
- [ ] Run Offer QA.
- [ ] Deliver one manual pilot or fake door.
- [ ] Capture feedback and rework.
- [ ] Decide drop, iterate, service, kit, skill, dashboard, report or automate.
- [ ] Update project memory.
```

## Definition Of Done

A monetization/productization task is done when:

- offer or package artifact exists;
- buyer, pain, deliverable and scope are explicit;
- evidence table exists;
- validation method exists;
- QA checklist exists;
- failure signal exists;
- next decision is clear;
- memory files are updated within allowed scope;
- limitations and assumptions are visible.

If the task is limited to a single file, as in some subagent contracts, do not update other memory files. Instead, include a "Recommended follow-up updates" section in the final response or task handoff.

## Local Adapter For ia-learning

Use this adapter when applying the guide inside this repo.

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_ROOT=/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
MONETIZATION_IDEAS=knowledge/projects/ia-learning/monetization-ideas.md
EXPERIMENTS=knowledge/projects/ia-learning/experiments.md
OFFER_DIR=knowledge/projects/ia-learning/offers
PRODUCTIZATION_DIR=knowledge/projects/ia-learning/productization
CUSTOMER_RESEARCH_DIR=knowledge/projects/ia-learning/customer-research
BENCHMARK_DIR=knowledge/projects/ia-learning/benchmarks
DASHBOARD_DIR=knowledge/projects/ia-learning/dashboards
SKILL_PACK_DIR=knowledge/projects/ia-learning/skill-packs
CODEX_KIT_DIR=knowledge/projects/ia-learning/codex-kits
SERVICE_PLAYBOOK_DIR=knowledge/projects/ia-learning/service-playbooks
```

### Current ia-learning Offer Candidates

Derived from local memory:

- Agent Launch Ops Kit;
- Curated Skills Library for AI Operators;
- Role-Specific Codex Kits;
- Benchmark-Backed AI Tool Reports;
- Agent Harness Kit;
- Comment Intelligence Dashboard Setup.

Recommended first validation order:

1. Agent Harness Kit, because existing guides already support task contracts, scope, validation and evidence.
2. Comment Intelligence Dashboard Setup, because it has a concrete MVP in `experiments.md`.
3. Benchmark-Backed AI Tool Reports, because methodology can be validated with small repo tasks.
4. Role-Specific Codex Kits, because they need clearer buyer segmentation before packaging.

### ia-learning First Pilot: Agent Harness Kit

```md
## Opportunity Intake

- Name: Agent Harness Kit
- Source: monetization-ideas.md and existing control-plane guides
- Confidence: inferred
- Target buyer: small software teams adopting Codex or coding agents
- End user: founders, tech leads, senior engineers, AI operators
- Pain: agents overreach, lose scope, skip validation or fail to preserve evidence
- Trigger: team starts using agents on real repo work
- Current alternative: ad hoc prompts, informal docs, manual review
- Desired outcome: repeatable task contracts, validation gates and memory workflow
- Existing asset: codex-operating-system-guide.md, agent-control-plane-guide.md, research-ops-evidence-guide.md
- Smallest useful deliverable: 90-minute audit plus one tailored task contract and QA checklist
- Why now: teams are moving from agent demos to operational workflows
- Main risk: buyer may see harness work as process overhead
- Next validation: offer one pilot to a builder/team and measure accepted changes
```

### ia-learning Productization Rule

For this repo:

```txt
manual run -> documented guide/template -> internal pilot -> external pilot -> priced offer -> skill/script -> automation
```

Do not skip from idea to automation. A guide becomes a product candidate only after it produces a useful outcome in at least one real or realistic run.
