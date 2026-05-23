# Prudent Automation Guide

Guia operativa portable para convertir un workflow manual en una skill, script o automatizacion recurrente con QA, evidencia, permisos claros y capacidad de pausa o rollback.

Esta guia es un anexo especializado de [Codex Operating System Guide](codex-operating-system-guide.md), [Agent Control Plane Guide](agent-control-plane-guide.md) y [Research Ops Evidence Guide](research-ops-evidence-guide.md). Usala cuando un equipo o agente quiera automatizar trabajo repetible sin perder trazabilidad ni calidad.

## Proposito

La automatizacion prudente evita convertir un proceso inmaduro en un error recurrente.

El flujo base es:

```txt
manual run -> reviewed output -> repeatable checklist -> skill/script -> QA gates -> scheduled automation -> monitoring -> improvement loop
```

El objetivo no es automatizar pronto. El objetivo es automatizar solo cuando el workflow ya demostro:

- valor real;
- output estable;
- criterios de calidad verificables;
- evidencia suficiente;
- permisos y secretos bajo control;
- manejo claro de fallos;
- capacidad de pausar, revertir o degradar manualmente.

## Cuando Usar Esta Guia

Usar esta guia cuando:

- un workflow se repite semanal, diario, mensual o por evento;
- el equipo quiere transformar un prompt recurrente en skill, script o automation;
- la salida influye en decisiones de producto, research, backlog, ventas, contenido o operaciones;
- se procesan fuentes externas como YouTube, Reddit, docs, issues, comentarios o benchmarks;
- se generan reportes, dashboards, briefs, summaries, insights o recomendaciones;
- el agente necesita correr sin supervision directa;
- hay riesgo de costos, rate limits, datos sensibles o outputs incorrectos;
- se quiere decidir si automatizar o mantener una corrida manual.

No usar completa cuando:

- la tarea ocurre una sola vez;
- la salida no se va a reutilizar;
- no existe un criterio de calidad claro;
- el costo de operar manualmente es menor que el costo de mantener la automatizacion;
- el workflow requiere juicio humano profundo en cada paso y no tiene patrones estables.

Para tareas pequenas, usa la version compacta:

```md
Workflow:
Manual run evidence:
QA criteria:
Extraction target: checklist | skill | script | automation
Schedule:
Pause trigger:
Owner:
```

## Resultado Esperado

Al terminar este proceso debe existir uno de estos resultados:

1. Decision de no automatizar todavia, con razones y condiciones para reintentar.
2. Checklist manual mejorado, si el workflow aun necesita madurar.
3. Skill o script reusable con validacion manual.
4. Automation recurrente con QA, logs, permisos, owner y pausa definida.

Una automatizacion lista debe tener:

- contrato del workflow;
- evidencia de corrida manual;
- salida esperada y formato estable;
- QA gates;
- logs de ejecucion;
- politica de permisos y secretos;
- politica de scheduling;
- manejo de fallos;
- plan de rollback o pause;
- owner humano;
- criterios para modificarla o retirarla.

## Variables Portables

Copiar y adaptar estas variables por proyecto:

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable>
PROJECT_ROOT=<raiz del repo>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
AUTOMATION_DIR=<PROJECT_MEMORY_DIR>/automation
RUNBOOK_DIR=<AUTOMATION_DIR>/runbooks
RUN_LOG_DIR=<AUTOMATION_DIR>/runs
QA_LOG_DIR=<AUTOMATION_DIR>/qa
SCRIPT_DIR=scripts
SKILL_DIR=<ruta de skills del entorno>
SECRETS_POLICY=<ruta o descripcion>
SCHEDULE_POLICY=<ruta o descripcion>
VALIDATION_COMMANDS=<comandos del repo>
PATH_TO_THIS_GUIDE=<ruta a esta guia>
```

Si el proyecto no usa `knowledge/`, reemplaza `PROJECT_MEMORY_DIR`, `RAW_DIR` y `PROCESSED_DIR` por las carpetas equivalentes. La funcion debe mantenerse aunque cambien los nombres.

## Principios

1. Primero manual, despues reusable, despues recurrente.
2. Ningun output de IA se automatiza sin QA definido.
3. Ninguna automatizacion se agenda sin un owner humano.
4. Ninguna credencial vive en prompts, markdown o logs.
5. Ningun fallo debe quedar silencioso.
6. Ninguna automatizacion debe modificar areas fuera de su contrato.
7. Toda corrida debe dejar evidencia suficiente para auditarla.
8. Toda automatizacion debe poder pausarse rapido.
9. Toda mejora debe provenir de fallos, QA o necesidades reales, no de complejidad anticipada.
10. Toda automatizacion debe justificar su costo operativo.

## Modelo De Madurez

Usa este modelo para decidir el siguiente paso. No saltar niveles sin evidencia.

| Nivel | Nombre | Estado | Requisito Para Avanzar |
|---|---|---|---|
| 0 | Idea recurrente | Hay una tarea que parece repetible | Describir problema, usuario, frecuencia y valor |
| 1 | Manual run | Un humano o agente ejecuta la tarea paso a paso | Guardar output, tiempo, fricciones y QA notes |
| 2 | Manual run validado | La salida fue revisada y sirvio | Definir criterios de calidad y fallos esperados |
| 3 | Checklist estable | El workflow se puede repetir desde instrucciones | Ejecutar otra corrida con menos ambiguedad |
| 4 | Skill o script | Parte del trabajo ya es reusable | Validar input/output, errores y permisos |
| 5 | Automation asistida | Se ejecuta bajo supervision o disparador manual | Dos corridas exitosas con logs y QA |
| 6 | Automation recurrente | Se agenda con owner, logs y pausa | Monitoreo, alertas y revision periodica |
| 7 | Automation mantenida | Tiene historial, mejoras y retiros controlados | Revisar costo, calidad y drift cada periodo |

### Regla De Avance

Avanza solo si todas las condiciones son verdaderas:

- el problema sigue siendo importante;
- el workflow se repitio al menos una vez sin redisenarlo por completo;
- el output tiene una forma esperada;
- hay una forma clara de detectar salida mala;
- el costo de automatizar es menor que repetir manualmente;
- los riesgos son aceptables o mitigables;
- existe owner para revisar fallos.

Si cualquiera falla, mantener el workflow en el nivel actual y documentar el bloqueo.

## Tipos De Automatizacion

### Checklist Manual

Usar cuando el workflow aun requiere criterio humano, fuentes variables o decisiones abiertas.

Ejemplos:

- revisar si una fuente vale la pena;
- clasificar insights nuevos;
- preparar un brief experimental;
- auditar una spec antes de implementar.

Output esperado:

- checklist;
- criterios de calidad;
- ejemplos buenos y malos;
- evidencia de una corrida.

### Skill

Usar cuando el workflow es principalmente razonamiento, analisis, transformacion de fuentes o generacion de documentos.

Una skill debe incluir:

- mision;
- cuando usarla;
- flujo de trabajo;
- guardrails;
- salida esperada;
- plantillas;
- ejemplos;
- criterios de revision.

Automatizar como skill cuando:

- la entrada puede variar;
- el agente necesita juicio;
- la salida es narrativa, analitica o de planificacion;
- se requiere trazabilidad de razonamiento y fuentes.

### Script

Usar cuando el workflow tiene pasos mecanicos, reproducibles y testeables.

Un script debe incluir:

- argumentos claros;
- validacion de inputs;
- output deterministico cuando sea posible;
- errores estructurados;
- logs sin secretos;
- modo dry-run si hay efectos laterales;
- tests o fixtures.

Automatizar como script cuando:

- se procesan archivos;
- se normalizan datos;
- se validan campos;
- se generan reportes desde entradas conocidas;
- el fallo puede expresarse con exit codes o excepciones.

### Scheduled Automation

Usar cuando la ejecucion recurrente ya esta justificada.

Una scheduled automation debe incluir:

- frecuencia;
- timezone;
- owner;
- prompt o comando autosuficiente;
- cwd o contexto;
- permisos;
- secrets requeridos;
- QA gate;
- output esperado;
- pause trigger;
- failure route;
- revision periodica.

No agendar si el output todavia necesita redaccion completa en cada corrida.

## Workflow De Automatizacion Prudente

### Fase 0. Intake

Objetivo: decidir si el workflow merece evaluarse.

Preguntas:

- Que problema resuelve?
- Para quien?
- Con que frecuencia ocurre?
- Que decision o accion mejora?
- Cual es el costo manual actual?
- Que pasaria si falla?
- Que datos o fuentes usa?
- Que permisos necesita?
- Que partes son juicio humano y que partes son mecanicas?

Salida:

```md
## Automation Candidate

- Workflow:
- User/problem:
- Trigger:
- Frequency:
- Current manual cost:
- Expected value:
- Inputs:
- Outputs:
- Decisions affected:
- Risk level: low | medium | high | regulated
- Candidate type: checklist | skill | script | scheduled automation
- Owner:
- Decision: test manually | reject | defer
```

### Fase 1. Manual Run

Objetivo: ejecutar el workflow una vez sin ocultar pasos ni fricciones.

Reglas:

- no optimizar antes de observar;
- registrar cada input relevante;
- conservar raw source cuando aplique;
- guardar output final;
- anotar tiempo, bloqueos y correcciones;
- separar hechos, inferencias y decisiones;
- pedir revision humana si el output influye en decisiones importantes.

Checklist:

```md
## Manual Run Checklist

- [ ] Workflow name:
- [ ] Date:
- [ ] Runner:
- [ ] Objective:
- [ ] Inputs listed:
- [ ] Raw evidence saved or linked:
- [ ] Commands/prompts used:
- [ ] Output saved:
- [ ] QA criteria applied:
- [ ] Manual corrections logged:
- [ ] Decision made:
- [ ] Next action:
```

Evidencia minima:

- input o link al input;
- output generado;
- notas de QA;
- decision de utilidad;
- fallos o ambiguedades.

### Fase 2. QA De La Corrida Manual

Objetivo: decidir si la salida es suficientemente buena para extraer un proceso.

Evaluar:

- completitud;
- exactitud;
- trazabilidad;
- utilidad;
- formato;
- costo;
- riesgo;
- repetibilidad.

Score sugerido:

| Dimension | Pregunta | Score 0-5 |
|---|---|---:|
| Valor | La salida ayudo a una decision real? | |
| Repetibilidad | Otro agente podria repetirla? | |
| Evidencia | Los claims importantes estan trazados? | |
| Calidad | El output requiere poca correccion? | |
| Riesgo | Los fallos son detectables? | |
| Costo | El costo de automatizar se justifica? | |

Regla:

- si cualquier score es menor a `3`, no crear automatizacion recurrente;
- si valor es menor a `3`, abandonar o redefinir problema;
- si evidencia es menor a `3`, mejorar capture y source indexing;
- si repetibilidad es menor a `3`, crear checklist antes de script o skill;
- si riesgo es menor a `3`, definir pause, approvals y QA mas fuertes.

### Fase 3. Extraccion A Checklist

Objetivo: convertir la corrida manual en pasos repetibles.

La checklist debe incluir:

- precondiciones;
- inputs;
- pasos;
- decisiones;
- outputs;
- QA;
- errores comunes;
- criterio de done.

Template:

```md
# Checklist: <workflow>

## Preconditions
- 

## Inputs
- 

## Steps
1. 
2. 
3. 

## Output
- 

## QA
- 

## Failure Handling
- 

## Done When
- 
```

Avanzar a skill o script cuando:

- la checklist se entiende sin contexto del chat;
- los pasos no dependen de memoria implicita;
- hay ejemplos de output bueno y malo;
- los fallos frecuentes estan escritos;
- el owner acepta el formato.

### Fase 4. Extraccion A Skill O Script

Objetivo: encapsular el workflow en una herramienta reusable.

Elegir skill si:

- la tarea requiere razonamiento;
- la entrada es semi-estructurada;
- se sintetizan fuentes;
- se generan guias, specs, briefs o insights;
- se necesita aplicar guardrails de contenido.

Elegir script si:

- la tarea procesa archivos o APIs;
- hay reglas de transformacion;
- hay validacion estructurada;
- se puede probar con fixtures;
- se necesitan exit codes.

Elegir ambos si:

- el script captura o valida datos;
- la skill interpreta, resume, prioriza o decide;
- la salida final combina estructura y criterio.

Contrato minimo de skill:

```md
# <Skill Name>

## Mission

## When To Use

## Inputs

## Workflow

## Guardrails

## Output Contract

## QA Checklist

## Failure Modes

## Examples
```

Contrato minimo de script:

```md
# Script Contract: <script>

- Purpose:
- Inputs:
- Outputs:
- Side effects:
- Secrets:
- Dry run:
- Validation:
- Error format:
- Owner:
```

### Fase 5. QA Gates Antes De Agendar

Objetivo: impedir que errores se repitan automaticamente.

Gates obligatorios:

1. Input gate: entradas existen, formato valido, permisos correctos.
2. Evidence gate: raw source o link trazable existe cuando aplica.
3. Output gate: formato esperado y secciones obligatorias presentes.
4. Quality gate: criterios especificos superan umbral.
5. Safety gate: secretos no aparecen en output ni logs.
6. Scope gate: la automation solo escribe en rutas permitidas.
7. Human gate: revision humana si el riesgo lo requiere.
8. Failure gate: errores generan log visible y estado no ambiguo.

Template:

```md
## QA Gates

| Gate | Check | Pass Criteria | Evidence | Status |
|---|---|---|---|---|
| Input | | | | pending |
| Evidence | | | | pending |
| Output | | | | pending |
| Quality | | | | pending |
| Safety | | | | pending |
| Scope | | | | pending |
| Human | | | | pending |
| Failure | | | | pending |
```

### Fase 6. Automation Readiness Review

Objetivo: decidir si se puede agendar.

Checklist:

```md
## Automation Readiness Review

- [ ] Manual run completed.
- [ ] Manual run QA completed.
- [ ] Checklist exists.
- [ ] Skill or script exists if needed.
- [ ] Output contract is stable.
- [ ] Owner assigned.
- [ ] Schedule defined.
- [ ] Permissions defined.
- [ ] Secrets policy defined.
- [ ] Logs defined.
- [ ] Allowed write paths defined.
- [ ] Failure handling defined.
- [ ] Pause trigger defined.
- [ ] Rollback or manual fallback defined.
- [ ] Review cadence defined.
- [ ] Decision recorded.
```

Decision:

- `schedule`: listo para automation recurrente;
- `manual-assisted`: ejecutar bajo supervision;
- `extract-more`: falta skill, script o checklist;
- `defer`: falta valor, estabilidad o owner;
- `reject`: no conviene automatizar.

### Fase 7. Scheduling

Objetivo: agendar con minimo riesgo.

Politica:

- empezar con baja frecuencia;
- preferir horarios donde un humano pueda revisar fallos;
- evitar escribir sobre archivos criticos sin aprobacion;
- no agendar tareas que requieran credenciales no definidas;
- usar timezone explicita;
- documentar el motivo de la frecuencia;
- revisar costo y utilidad despues de las primeras corridas.

Campos:

```md
## Schedule Policy

- Workflow:
- Frequency:
- Timezone:
- Reason for frequency:
- Owner:
- Reviewer:
- Output destination:
- Allowed write paths:
- Read dependencies:
- Secrets required:
- Cost/rate-limit risk:
- First review after:
- Pause trigger:
```

### Fase 8. Operacion Y Mantenimiento

Objetivo: que la automation mejore o se retire con evidencia.

Cada corrida debe registrar:

- fecha;
- version de workflow;
- inputs;
- output;
- QA status;
- errores;
- cambios realizados;
- decision;
- follow-up.

Cada periodo revisar:

- sigue resolviendo el problema?
- el output se usa?
- hay drift de fuentes, APIs o formatos?
- hay fallos repetidos?
- el costo sigue justificado?
- se debe pausar, reducir frecuencia o retirar?

## Evidence Logs

Toda automatizacion debe dejar evidencia suficiente para reconstruir que paso.

### Run Log

```md
# Automation Run Log: <workflow>

## Metadata
- Run id:
- Workflow:
- Date:
- Runner:
- Version:
- Trigger: manual | scheduled | event
- Status: success | partial | failed | paused

## Inputs
- 

## Outputs
- 

## Evidence
- Raw:
- Processed:
- Source index:
- QA:

## Checks
| Check | Result | Evidence |
|---|---|---|
| Input | | |
| Output | | |
| Evidence | | |
| Safety | | |
| Scope | | |

## Errors
- 

## Manual Corrections
- 

## Decision
- keep | revise | pause | rollback | retire

## Follow-Up
- 
```

### QA Log

```md
# QA Log: <workflow>

- Date:
- Reviewer:
- Output reviewed:
- Criteria:
- Pass/fail:
- Issues:
- Corrections:
- Evidence gaps:
- Decision:
```

### Decision Log

```md
# Automation Decision

- Date:
- Workflow:
- Decision: schedule | defer | pause | rollback | retire
- Reason:
- Evidence:
- Risks accepted:
- Owner:
- Next review:
```

## Permisos Y Secretos

La automation debe operar con el menor permiso posible.

### Clasificacion De Permisos

| Nivel | Permisos | Ejemplos | Requiere Aprobacion |
|---|---|---|---|
| Read-only | leer archivos o fuentes publicas | summaries, reports | baja |
| Local write | escribir en rutas permitidas | `knowledge/`, `docs/` | media |
| External read | leer APIs privadas | analytics, comments | media-alta |
| External write | publicar, comentar, enviar emails | CRM, YouTube, Slack | alta |
| Destructive | borrar, sobrescribir, migrar | DB, deploys | regulada |

### Reglas De Secretos

- Nunca escribir secretos en markdown, prompts, logs o outputs.
- Usar variables de entorno, secret managers o conectores aprobados.
- Redactar tokens en errores.
- Registrar solo el nombre logico del secreto, no su valor.
- Separar permisos de lectura y escritura.
- Rotar credenciales si aparecen en logs.
- No pasar secretos a subagentes que no los necesitan.

Template:

```md
## Secrets And Permissions

- Required secrets:
- Secret source:
- Read permissions:
- Write permissions:
- Disallowed actions:
- Redaction rules:
- Rotation owner:
- Approval required:
```

## Politica De Scope Y Escritura

Antes de agendar, definir:

- rutas que puede leer;
- rutas que puede escribir;
- archivos que no puede tocar;
- formatos permitidos;
- si puede crear commits;
- si puede abrir PRs;
- si puede enviar mensajes externos;
- si requiere aprobacion humana.

Template:

```md
## Write Scope

Allowed:
- 

Disallowed:
- 

Requires approval:
- 

On conflict:
- pause and report | write conflict note | skip file
```

## Manejo De Fallos

Una automation falla bien cuando:

- no oculta el error;
- no produce una salida que parece valida si no lo es;
- conserva evidencia del fallo;
- no corrompe estado;
- avisa al owner o deja un estado visible;
- propone una accion concreta.

### Taxonomia De Fallos

| Tipo | Ejemplo | Accion |
|---|---|---|
| Input missing | archivo o URL no existe | fallar con mensaje claro |
| Source unavailable | API, captions o web caidos | guardar failure evidence |
| Permission denied | token vencido | pausar y pedir owner |
| Output invalid | schema incompleto | bloquear publicacion |
| Quality low | summary generico | marcar partial y revisar |
| Scope conflict | archivo con cambios ajenos | pausar ese archivo |
| Rate limit | muchas requests | backoff y reintento controlado |
| Cost spike | consumo inesperado | detener y notificar |
| Drift | fuente cambio formato | crear issue o improvement |
| Safety risk | secretos o datos sensibles | redactar, pausar, escalar |

### Failure Report

```md
# Failure Report

- Workflow:
- Run id:
- Date:
- Severity: low | medium | high | critical
- What failed:
- Where it failed:
- User impact:
- Data impact:
- Evidence:
- Immediate action:
- Recommended fix:
- Retry allowed: yes | no | after fix
- Owner:
```

## Rollback, Pause Y Manual Fallback

Toda automation recurrente necesita una forma de detenerse y una forma manual de reemplazarla.

### Pause Triggers

Pausar si:

- falla dos veces seguidas;
- escribe fuera de scope;
- aparece un secreto en output o logs;
- la fuente primaria cambia de formato;
- el output baja de umbral de calidad;
- el owner no revisa fallos;
- el costo supera el limite definido;
- se detecta drift en claims o evidencia;
- el workflow deja de influir en decisiones reales.

### Rollback

Definir rollback cuando la automation modifica archivos, dashboards, tickets, emails, PRs o sistemas externos.

Template:

```md
## Rollback Plan

- Last known good state:
- Files or systems affected:
- How to revert:
- Who can approve:
- Evidence to preserve:
- User notification:
- Follow-up fix:
```

### Manual Fallback

Template:

```md
## Manual Fallback

- When to use:
- Manual owner:
- Checklist:
- Expected time:
- Output destination:
- QA:
- How to resume automation:
```

## Patrones Por Caso De Uso

### Research Report Automation

Usar para reportes de YouTube, Reddit, docs, papers o benchmarks.

Requisitos:

- raw source o failure evidence;
- processed artifact;
- summary con hechos e inferencias separados;
- source index actualizado;
- insights atomicos;
- confidence labels;
- QA de claims importantes;
- link a decision, experimento o open question.

No automatizar si:

- la fuente no se puede capturar;
- no hay decision afectada;
- la salida solo resume sin accion;
- el agente no puede distinguir evidencia primaria de inferencia.

### Dashboard Automation

Usar para dashboards de comentarios, feedback, metricas o tendencias.

Requisitos:

- schema de datos;
- definicion de metricas;
- freshness esperada;
- control de duplicados;
- datos raw preservados;
- filtros y segmentos;
- QA de conteos;
- decision log sobre cambios de metrica.

No automatizar si:

- las metricas no tienen uso claro;
- hay datos sensibles sin politica;
- el dashboard induce vanity metrics;
- no hay owner que revise anomalias.

### Benchmark Report Automation

Usar para comparar modelos, herramientas, costos, tiempos o calidad.

Requisitos:

- version de herramientas;
- fecha de captura;
- dataset o prompts;
- ambiente de prueba;
- criterios de evaluacion;
- resultados raw;
- limites y sesgos;
- conclusion con confidence.

No automatizar si:

- el benchmark no es reproducible;
- cambia el dataset sin registro;
- no se separan resultados de interpretacion;
- la conclusion se usa fuera de contexto.

### Comment Intelligence Automation

Usar para comentarios de YouTube, issues, feedback o comunidades.

Requisitos:

- permisos de API;
- rate limit;
- deduplicacion;
- clasificacion con ejemplos;
- muestra revisada manualmente;
- links a comentarios o IDs;
- proteccion de datos personales;
- acciones recomendadas con evidencia.

No automatizar si:

- la clasificacion es generica;
- no hay acciones tomadas;
- se pierde permalink o contexto;
- se mezclan comunidades sin segmentacion.

### Release Or QA Automation

Usar para checks recurrentes de repos, builds, tests o documentacion.

Requisitos:

- comandos definidos;
- entorno definido;
- exit codes;
- logs;
- owner de fallos;
- retries limitados;
- rutas afectadas;
- politica para cambios de lockfile o snapshots.

No automatizar si:

- el comando es flaky sin diagnostico;
- no hay criterio de pass/fail;
- el fallo no llega a quien puede actuar;
- la automation cambia codigo sin review.

## Prompts Para Agentes IA

### Prompt 1. Evaluar Candidato

```md
Actua como Automation Evaluator.

Objetivo: decidir si este workflow debe quedarse manual, convertirse en checklist, extraerse como skill/script o agendarse.

Contexto:
- Proyecto: <PROJECT_NAME>
- Workflow:
- Frecuencia esperada:
- Output esperado:
- Riesgo:
- Owner:

Instrucciones:
1. Identifica problema, usuario, valor y frecuencia.
2. Distingue pasos de juicio humano vs pasos mecanicos.
3. Evalua madurez usando el modelo 0-7.
4. Lista evidencia faltante.
5. Recomienda siguiente paso.

Salida:
- Decision:
- Nivel actual:
- Proximo nivel:
- Bloqueos:
- QA requerido:
- Riesgos:
- Siguiente accion:
```

### Prompt 2. Ejecutar Corrida Manual

```md
Actua como Manual Run Agent.

Objetivo: ejecutar una primera corrida manual del workflow y dejar evidencia para decidir si se puede automatizar.

Debes:
1. Registrar inputs y objetivo.
2. Ejecutar los pasos de forma transparente.
3. Guardar o enlazar raw evidence cuando aplique.
4. Producir output en formato revisable.
5. Registrar fricciones, fallos y correcciones.
6. Completar QA notes.

No debes:
- agendar automation;
- ocultar fallos;
- tratar summaries como evidencia primaria;
- escribir fuera del scope permitido.

Salida:
- Run log:
- Output:
- QA notes:
- Recomendacion:
```

### Prompt 3. Extraer Checklist

```md
Actua como Workflow Extractor.

Objetivo: convertir una corrida manual validada en una checklist portable.

Contexto:
- Manual run log:
- Output:
- QA notes:
- Fallos observados:

Instrucciones:
1. Identifica precondiciones.
2. Lista inputs y outputs.
3. Escribe pasos repetibles.
4. Marca decisiones humanas.
5. Agrega QA gates.
6. Agrega failure handling.
7. Define done.

Salida:
- Checklist:
- Ambiguedades:
- Recomendacion: mantener checklist | crear skill | crear script | ambos
```

### Prompt 4. Crear Skill

```md
Actua como Skill Designer.

Objetivo: convertir un workflow validado en una skill reusable para agentes IA.

Contexto:
- Checklist:
- Ejemplos de output bueno:
- Ejemplos de output malo:
- QA criteria:
- Failure modes:

Instrucciones:
1. Define mision.
2. Define cuando usar y cuando no usar.
3. Define inputs.
4. Define workflow.
5. Define guardrails.
6. Define output contract.
7. Define QA checklist.
8. Define failure modes.

Salida:
- Skill draft:
- Riesgos:
- Pruebas sugeridas:
```

### Prompt 5. Crear Script Contract

```md
Actua como Script Architect.

Objetivo: definir un script reproducible para la parte mecanica del workflow.

Contexto:
- Checklist:
- Inputs:
- Outputs:
- Side effects:
- Validation needs:

Instrucciones:
1. Define CLI o funcion.
2. Define argumentos.
3. Define schema de input y output.
4. Define errores estructurados.
5. Define logs sin secretos.
6. Define dry-run si hay efectos laterales.
7. Define tests o fixtures.

Salida:
- Script contract:
- Test plan:
- Failure handling:
- Security notes:
```

### Prompt 6. Readiness Review

```md
Actua como Automation Readiness Reviewer.

Objetivo: decidir si el workflow puede agendarse.

Revisa:
- manual run evidence;
- QA log;
- checklist;
- skill/script;
- permisos;
- secretos;
- schedule;
- failure handling;
- pause/rollback;
- owner.

Decision permitida:
- schedule;
- manual-assisted;
- extract-more;
- defer;
- reject.

Salida:
- Decision:
- Evidencia revisada:
- Bloqueos:
- Riesgos aceptados:
- Condiciones antes de agendar:
- Primer review:
```

### Prompt 7. Post-Run Auditor

```md
Actua como Post-Run Auditor.

Objetivo: auditar una corrida de automation y decidir si continua, se ajusta, se pausa o se retira.

Contexto:
- Run log:
- Output:
- QA results:
- Errors:
- User decisions affected:

Instrucciones:
1. Evalua calidad del output.
2. Verifica evidencia.
3. Identifica drift o fallos repetidos.
4. Revisa si el output fue usado.
5. Recomienda accion.

Salida:
- Status:
- Findings:
- Decision: keep | revise | pause | rollback | retire
- Required fixes:
- Next review:
```

## Templates

### Automation Spec

```md
# Automation Spec: <workflow>

## Metadata
- Project:
- Workflow:
- Owner:
- Reviewer:
- Status: candidate | manual | checklist | skill | script | scheduled | paused | retired
- Risk: low | medium | high | regulated
- Version:

## Problem
- User/problem:
- Why it repeats:
- Current manual cost:
- Expected value:

## Scope
- In scope:
- Out of scope:
- Allowed write paths:
- Disallowed actions:

## Inputs
- 

## Outputs
- 

## Evidence
- Manual run:
- QA log:
- Source index:
- Related decisions:

## QA Gates
- 

## Permissions
- Read:
- Write:
- Secrets:
- Approvals:

## Schedule
- Trigger:
- Frequency:
- Timezone:
- First review:

## Failure Handling
- Expected failures:
- Retry policy:
- Pause triggers:
- Owner notification:

## Rollback
- 

## Decision
- 
```

### Output Contract

```md
# Output Contract

- Format:
- Required sections:
- Required metadata:
- Evidence pointers:
- Confidence labels:
- Prohibited content:
- Validation checks:
- Destination:
```

### QA Checklist

```md
# QA Checklist

- [ ] Output matches format.
- [ ] Required metadata exists.
- [ ] Evidence pointers exist.
- [ ] Claims separate facts from inference.
- [ ] Confidence labels exist.
- [ ] No secrets in output.
- [ ] Write scope respected.
- [ ] Failure notes are visible.
- [ ] Next action is explicit.
```

### Retirement Note

```md
# Automation Retirement Note

- Workflow:
- Retired on:
- Reason:
- Last successful run:
- Last failure:
- Data/artifacts to keep:
- Files/scripts/skills affected:
- Manual fallback:
- Lessons:
```

## Failure Modes Comunes

### Automatizar Sin Valor Probado

Sintoma:

- hay automation, pero nadie usa el output.

Prevencion:

- exigir decision o accion afectada;
- registrar uso real del output;
- retirar automation si no cambia decisiones.

### Automatizar Summaries Sin Evidencia

Sintoma:

- reportes convincentes sin raw source, transcript, permalink o source index.

Prevencion:

- aplicar [Research Ops Evidence Guide](research-ops-evidence-guide.md);
- bloquear claims fuertes sin evidencia primaria;
- guardar failure evidence cuando capture falla.

### Scope Drift Recurrente

Sintoma:

- cada corrida edita archivos nuevos o mezcla temas.

Prevencion:

- write scope explicito;
- task contract;
- pausas ante conflictos;
- output destination estable.

### Fallos Silenciosos

Sintoma:

- la automation termina "bien" pero faltan datos o secciones.

Prevencion:

- output gate;
- schema o checklist;
- status `partial` cuando falte evidencia;
- failure report obligatorio.

### Prompt Drift

Sintoma:

- cambios menores al prompt alteran la salida sin darse cuenta.

Prevencion:

- versionar prompt;
- conservar ejemplos buenos;
- usar output contract;
- revisar despues de cambios.

### Secret Leakage

Sintoma:

- tokens, emails privados o payloads sensibles aparecen en logs.

Prevencion:

- redaction rules;
- no escribir env vars;
- logs minimos;
- revisar safety gate.

### Over-Automation

Sintoma:

- hay scripts, skills y schedules para un proceso que aun cambia cada vez.

Prevencion:

- mantener checklist hasta estabilizar;
- medir costo de mantenimiento;
- retirar automation que no ahorra tiempo real.

### No Owner

Sintoma:

- fallos se acumulan sin respuesta.

Prevencion:

- owner obligatorio;
- pause trigger si no hay revision;
- review cadence.

## Adoption Checklist

Para adoptar esta guia en un proyecto:

- [ ] Copiar o enlazar esta guia.
- [ ] Completar variables portables.
- [ ] Definir carpeta de run logs.
- [ ] Definir politica de secretos.
- [ ] Definir rutas permitidas de escritura.
- [ ] Elegir un primer workflow pequeno.
- [ ] Ejecutar una corrida manual.
- [ ] Guardar evidencia y QA.
- [ ] Extraer checklist.
- [ ] Decidir skill, script o mantener manual.
- [ ] Ejecutar una segunda corrida validada.
- [ ] Hacer readiness review antes de agendar.
- [ ] Agendar con baja frecuencia si procede.
- [ ] Revisar despues de las primeras corridas.
- [ ] Pausar o retirar si el output no se usa.

## Definition Of Done

Una automatizacion prudente esta done cuando:

- tiene owner;
- tiene scope;
- tiene evidencia de al menos una corrida manual;
- tiene QA gates;
- tiene output contract;
- tiene logs;
- respeta permisos y secretos;
- tiene schedule justificado;
- tiene pause triggers;
- tiene rollback o fallback manual;
- tiene review cadence;
- su salida influye en una decision o accion real.

Si no cumple esto, puede estar en progreso, pero no debe considerarse lista para correr sin supervision.

## Local Adapter Para ia-learning

Este repo usa `knowledge/` como memoria local para research, patrones, ideas, experimentos y mejoras de proceso. Para `ia-learning`, aplicar esta guia asi:

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_ROOT=/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
AUTOMATION_DIR=knowledge/projects/ia-learning/automation
RUNBOOK_DIR=knowledge/projects/ia-learning/automation/runbooks
RUN_LOG_DIR=knowledge/projects/ia-learning/automation/runs
QA_LOG_DIR=knowledge/projects/ia-learning/automation/qa
```

Guias relacionadas:

- [Codex Operating System Guide](codex-operating-system-guide.md)
- [Agent Control Plane Guide](agent-control-plane-guide.md)
- [Research Ops Evidence Guide](research-ops-evidence-guide.md)
- [Spec Driven Development Guide](spec-driven-development-guide.md)
- [process-improvements.md](process-improvements.md)
- [experiments.md](experiments.md)

Workflows candidatos para automatizacion prudente en `ia-learning`:

- reportes recurrentes de canales de YouTube;
- captura y analisis de comentarios;
- pre-read semanal de engineering management;
- validacion de `knowledge/` contra source index;
- reporte de experimentos stale;
- resumen de open questions y decisiones pendientes;
- QA de guias operativas antes de commit.

Politica local:

1. Toda fuente externa debe seguir `knowledge/README.md`.
2. Toda research automation debe preservar raw source o failure evidence.
3. Todo summary debe apuntar a source index.
4. Toda automation que actualice `knowledge/projects/ia-learning/` debe declarar archivos permitidos.
5. No agendar reportes recurrentes hasta tener una corrida manual con QA.
6. Mantener `node_modules/` y outputs pesados fuera de cambios documentales salvo que una tarea lo pida explicitamente.

Primer workflow recomendado:

```md
# Candidate: Knowledge QA Pre-Read

- Problem: detectar fuentes, insights, experimentos y preguntas que quedaron sin conectar.
- Frequency: semanal o antes de planificacion.
- Manual run: revisar source-index, experiments, process-improvements y open-questions.
- Output: brief con stale items, missing evidence, next actions y suggested experiments.
- QA: cada recomendacion debe apuntar a archivo o fuente.
- Automation path: manual run -> checklist -> skill -> scheduled heartbeat/cron si el output cambia prioridades.
```

## Cierre Operativo

La automatizacion prudente es una politica de calidad, no una preferencia de estilo. Un agente puede ejecutar trabajo recurrente, pero solo debe hacerlo cuando el proyecto pueda responder estas preguntas:

- Que problema recurrente resuelve?
- Como sabemos que funciono?
- Donde esta la evidencia?
- Que pasa si falla?
- Quien la mantiene?
- Como se pausa?
- Cuando se retira?

Si esas respuestas no existen, la siguiente accion correcta es una corrida manual mejor instrumentada, no una automation.
