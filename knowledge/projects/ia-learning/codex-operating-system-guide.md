# Codex Operating System Guide

Guia operativa portable para usar Codex como sistema de trabajo, no solo como chat. Esta guia esta escrita para que una IA pueda leerla, adaptarla a un repo nuevo y producir artefactos verificables con memoria local.

Esta version funciona como punto de partida. Cada proyecto debe completar el perfil de proyecto, elegir sus carpetas de memoria, definir sus comandos de validacion y agregar anexos especificos cuando necesite profundizar en investigacion, producto, arquitectura, QA, seguridad o automatizaciones.

## Proposito

Convertir ideas, fuentes, bugs, experimentos y tareas de producto en un flujo repetible:

```txt
intencion -> contexto -> spec -> ejecucion -> validacion -> memoria -> automatizacion opcional
```

El objetivo no es que Codex responda rapido. El objetivo es que trabaje dentro de una frontera durable, con evidencia, criterios de aceptacion y aprendizajes reutilizables.

## Portabilidad

Esta guia debe poder copiarse a cualquier repo y empezar a funcionar con cambios minimos. Para portarla:

1. Copia este archivo a una ubicacion estable del proyecto, por ejemplo `docs/ai/codex-operating-system-guide.md` o `knowledge/projects/<project-id>/codex-operating-system-guide.md`.
2. Completa el `Project Profile`.
3. Ajusta `PROJECT_MEMORY_DIR`, `SOURCE_INDEX`, `VALIDATION_COMMANDS` y `AUTOMATION_POLICY`.
4. Conserva el core operativo sin cambios hasta que el equipo detecte fricciones reales.
5. Agrega anexos por dominio solo cuando hagan falta.

Variables usadas en esta guia:

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable del proyecto>
PROJECT_ROOT=<ruta o raiz del repo>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
BRIEFS_DIR=knowledge/briefs
VALIDATION_COMMANDS=<comandos del repo>
```

## Project Profile

Cada proyecto que use esta guia debe mantener este bloque actualizado, dentro de este archivo o en un `PROJECT_AI_PROFILE.md`.

```md
# Project AI Profile

- Project name:
- Project id:
- Primary user/customer:
- Product/domain:
- Repo type: app | library | docs | research | automation | mixed
- Main stack:
- Runtime/package manager:
- Test commands:
- Build commands:
- Lint/typecheck commands:
- Dev server command:
- Deployment target:
- Source memory dir:
- Sensitive areas:
- External APIs:
- Required docs before work:
- Definition of done:
- Human approval required for:
```

Si un campo no aplica, marcarlo como `n/a`. No dejar campos importantes en blanco.

## Niveles De Uso

Usa el nivel mas pequeno que resuelva el trabajo.

| Nivel | Usar Cuando | Artefacto |
|---|---|---|
| Lite | tarea pequena, reversible y clara | respuesta + validacion breve |
| Standard | cambio de repo, investigacion o doc reusable | task brief + artefacto + evidencia |
| Deep | trabajo multi-area, alto riesgo, producto o automatizacion | spec/control plane + validacion + memoria |
| System | workflow repetible o reusable por otros equipos | skill/script/template + QA + politica de mantenimiento |

La guia es portable porque el core no asume stack, producto ni proveedor. El adaptador de proyecto define esos detalles.

## Principios Operativos

1. Todo trabajo importante debe tener una frontera de proyecto.
2. Toda fuente externa util debe preservar evidencia raw o un enlace verificable.
3. Toda tarea de implementacion debe tener criterios de aceptacion.
4. Toda entrega debe incluir evidencia de validacion o un bloqueo explicito.
5. Toda repeticion exitosa debe convertirse en plantilla, skill, script o automatizacion.
6. Toda automatizacion debe pasar primero por una corrida manual y una revision de calidad.
7. Toda memoria generada debe separar hechos, inferencias, experimentos y dudas abiertas.

## Mapa Del Sistema

```txt
repo/
  AGENTS.md                    instrucciones estables para agentes
  knowledge/                   memoria local y evidencia
    README.md                  contrato de memoria
    raw/                       fuentes originales, exports, APIs, fallos
    processed/                 transcripts, summaries, insights normalizados
    projects/<project-id>/     decisiones, patrones, experimentos, preguntas
    briefs/                    sintesis recurrentes
  docs/                        specs, backlog o documentacion de producto
  scripts/                     automatizaciones y utilidades reproducibles
  services/                    integraciones o MCP wrappers
```

Codex debe tratar el repo como el sistema de registro. El chat coordina; los archivos conservan estado.

## Archivos Base Del Sistema

Cada proyecto debe crear o mapear estos archivos base. Los nombres pueden cambiar, pero la funcion debe mantenerse clara:

```txt
<PROJECT_MEMORY_DIR>/agent-workflows.md             workflows operativos
<PROJECT_MEMORY_DIR>/implementation-patterns.md     patrones tecnicos reutilizables
<PROJECT_MEMORY_DIR>/process-improvements.md        mejoras del sistema de trabajo
<PROJECT_MEMORY_DIR>/experiments.md                 hipotesis y validaciones
<PROJECT_MEMORY_DIR>/open-questions.md              decisiones pendientes
<SOURCE_INDEX>                                      fuentes y evidencia
<SPEC_CONTEXT_PATH>                                 reglas para specs implementables
```

Si un proyecto no necesita todos los archivos, puede empezar solo con esta guia, `<SOURCE_INDEX>`, `experiments.md` y `open-questions.md`. Las fuentes originales y su confianza deben registrarse en `<SOURCE_INDEX>`. No trates esta guia como evidencia primaria de videos, documentos externos o decisiones historicas.

## Roles Del Sistema

### Usuario

Define intencion, prioridad y restricciones. Aprueba decisiones de producto, scope amplio, credenciales, integraciones externas, automatizaciones y cambios de alto riesgo.

### Orquestador

Convierte la intencion en un contrato operativo. Decide si hace falta spec, investiga contexto local, divide trabajo, define validacion y mantiene memoria.

### Implementador

Edita codigo, documentos, scripts o artefactos siguiendo el contrato. Debe respetar scope, patrones del repo y restricciones de seguridad.

### Revisor

Busca bugs, riesgos, regresiones, huecos de validacion y evidencia debil. Debe reportar hallazgos con archivo, linea, severidad y accion recomendada.

### Curador De Memoria

Actualiza `knowledge/` con fuentes, insights, experimentos, patrones y preguntas abiertas. Debe preservar trazabilidad.

### Automatizador

Convierte un flujo validado en script, skill o automation. No debe automatizar outputs no revisados.

## Tipos De Trabajo

### 1. Investigacion De Fuentes

Usar cuando el input es YouTube, Reddit, articulos, docs, papers, changelogs o benchmarks.

Artefactos minimos:

- raw source en `knowledge/raw/<source>/`
- transcript, thread o resumen normalizado en `knowledge/processed/`
- insight atomico en `knowledge/processed/insights/` si hay aprendizaje reusable
- enlace en `<SOURCE_INDEX>`
- actualizacion de los archivos equivalentes a `experiments.md`, `implementation-patterns.md`, `process-improvements.md`, `monetization-ideas.md` u `open-questions.md`

Criterio de completitud:

- La fuente puede rastrearse.
- La confianza esta marcada.
- Las inferencias estan separadas de hechos.
- Hay una accion, experimento o razon explicita para no actuar.

### 2. Spec Antes De Implementar

Usar cuando la idea es ambigua, afecta varias areas, requiere UI/API/datos o tiene riesgo de regresion.

Entrada minima:

- idea original
- problema
- usuario afectado
- resultado esperado
- restricciones conocidas

Salida esperada:

- spec con goals, non-goals, comportamiento actual, comportamiento deseado, edge cases, archivos probables, acceptance criteria y plan de verificacion.

Archivo de apoyo:

- [spec-driven-development-context.md](spec-driven-development-context.md)

### 3. Implementacion

Usar cuando hay una tarea concreta o una spec aceptada.

Contrato minimo:

- objetivo
- no-objetivos
- archivos o areas permitidas
- contexto relevante
- comandos de verificacion
- riesgo
- memoria que debe actualizarse

Criterio de completitud:

- diff acotado
- pruebas o verificacion ejecutadas
- limitaciones declaradas
- memoria actualizada si el cambio genero aprendizaje reusable

### 4. Workflow Repetible

Usar cuando una secuencia se repite: capturar fuentes, analizar comentarios, preparar pre-read, generar reportes, validar releases, revisar backlog.

Evolucion esperada:

```txt
manual run -> checklist -> script/skill -> QA -> automation
```

No saltar directo a automatizacion salvo que el usuario lo pida explicitamente y acepte el riesgo.

### 5. Producto O Monetizacion

Usar cuando una idea pueda convertirse en kit, servicio, curso, dashboard, benchmark, skill pack o template.

Salida esperada:

- target user
- dolor
- oferta
- evidencia
- smallest test
- success signal
- failure signal
- assets necesarios
- riesgos de demanda no verificada

Memoria relacionada:

- archivo de monetizacion u oportunidades del proyecto
- archivo de experimentos o backlog de validacion del proyecto

## Bucle Operativo Principal

### Paso 0: Clasificar La Solicitud

Antes de actuar, Codex debe clasificar el trabajo:

```txt
tipo: investigacion | spec | implementacion | review | automatizacion | memoria | producto
riesgo: bajo | medio | alto
requiere web: si | no
requiere archivos: si | no
requiere aprobacion: si | no
artefacto esperado: respuesta | archivo | codigo | reporte | automatizacion
```

Reglas:

- Si el usuario pide informacion actual, docs cambiantes, precios, lanzamientos o noticias, verificar fuentes actuales.
- Si el usuario pide codigo o documentos del repo, leer el contexto local primero.
- Si la tarea toca credenciales, produccion, pagos o datos sensibles, pedir confirmacion o usar datos mock.
- Si la tarea es pequena y reversible, ejecutar sin sobredisenar.

### Paso 1: Crear O Seleccionar Frontera

Elegir donde vive el trabajo:

- investigacion: `knowledge/raw`, `knowledge/processed`, `<PROJECT_MEMORY_DIR>`
- specs: `docs/`, `specs/` o `<PROJECT_MEMORY_DIR>` segun permanencia
- codigo: area existente del repo
- scripts: `scripts/`
- integraciones: `services/`
- briefs recurrentes: `knowledge/briefs/`

La frontera evita que el resultado quede atrapado en el chat.

### Paso 2: Recolectar Contexto

Leer solo lo necesario:

- `AGENTS.md` o instrucciones locales
- `knowledge/README.md` si hay fuentes externas
- archivos de proyecto relevantes
- specs o docs existentes
- `<SOURCE_INDEX>` si la tarea deriva de investigacion
- tests o scripts cercanos

Salida mental esperada:

```txt
hechos conocidos:
supuestos:
archivos relevantes:
riesgos:
validacion posible:
```

### Paso 3: Definir Contrato De Tarea

Para tareas medianas o grandes, crear un contrato antes de editar.

Plantilla:

```md
## Task Contract

- Objective:
- Non-objectives:
- User value:
- Source/context:
- Allowed files:
- Out of scope:
- Dependencies:
- Validation:
- Memory update:
- Risks:
- Escalation:
```

El contrato puede vivir en el chat para tareas pequenas. Para tareas largas debe quedar en un archivo de spec, checklist o issue.

### Paso 4: Ejecutar En Lotes Pequenos

Reglas para implementacion:

- Preferir patrones existentes del repo.
- Evitar refactors no solicitados.
- Mantener cambios cerca del objetivo.
- Hacer commits solo si el usuario lo pide.
- No revertir cambios ajenos.
- Usar parsers o APIs estructuradas cuando existan.
- Para UI, verificar visualmente si hay servidor/app.

Reglas para investigacion:

- Capturar raw antes de resumir.
- Guardar fallos de captura como evidencia.
- No tratar summaries como evidencia primaria.
- Separar metadata-backed, transcript-backed, inferred y experimental.

### Paso 5: Validar

La validacion debe corresponder al riesgo:

- docs: revisar links, formato, consistencia y trazabilidad.
- scripts: ejecutar help, dry-run o prueba con fixture.
- backend: tests unitarios/integracion o smoke test.
- frontend: build, lint y browser/screenshot si aplica.
- investigacion: comprobar `<SOURCE_INDEX>`, raw payload, processed artifact y confidence.
- automatizacion: corrida manual, QA output y logs.

Formato de evidencia:

```txt
validated:
- command: <comando>
- result: passed | failed | not run
- evidence: <archivo, salida clave, screenshot, raw source>
- residual risk: <riesgo restante>
```

### Paso 6: Actualizar Memoria

Actualizar memoria si hubo:

- nueva fuente externa
- patron reusable
- decision de producto
- experimento propuesto o ejecutado
- fallo repetible
- mejora de proceso
- pregunta abierta

Destino:

- `<SOURCE_INDEX>`: fuentes analizadas
- `<PROJECT_MEMORY_DIR>/implementation-patterns.md`: patrones tecnicos
- `<PROJECT_MEMORY_DIR>/process-improvements.md`: mejoras de workflow
- `<PROJECT_MEMORY_DIR>/experiments.md`: hipotesis verificables
- `<PROJECT_MEMORY_DIR>/monetization-ideas.md`: ofertas/productos, si aplica
- `<PROJECT_MEMORY_DIR>/open-questions.md`: dudas no resueltas
- `<PROJECT_MEMORY_DIR>/agent-workflows.md`: workflows operativos

### Paso 7: Convertir En Sistema Reutilizable

Si una tarea se repite y funciono:

1. Extraer checklist.
2. Crear script o skill minimo.
3. Agregar guardrails.
4. Probar con fixture o caso pequeno.
5. Documentar input/output.
6. Solo despues crear automation.

## Control Plane Diario

Usar este bloque para iniciar una sesion de trabajo.

```md
# Daily Control Plane

## Objective

## Current State

- Branch:
- Dirty files:
- Recent relevant sources:
- Active experiments:
- Open questions:

## Work Queue

| Task | Type | Owner | Files | Status | Validation | Risk |
|---|---|---|---|---|---|---|

## Decisions Needed

## Validation Evidence

## Memory Updates
```

## Control Plane Para Tareas De Codex

Usar este formato cuando una IA vaya a ejecutar una tarea concreta.

```md
# Codex Task Brief

## Goal

## Why It Matters

## Context Files

- 

## Source Evidence

- 

## Constraints

- 

## Scope

### In

- 

### Out

- 

## Expected Artifact

## Acceptance Criteria

- 

## Verification Plan

- 

## Memory Update Required

- yes/no:
- target file:

## Final Response Must Include

- changed files
- validation run
- evidence
- assumptions
- residual risks
```

## Prompt Maestro Para Una IA

Copiar este prompt cuando quieras que otra IA use este sistema.

```md
Usa `<PATH_TO_THIS_GUIDE>` como guia operativa.

Objetivo:
<describe el resultado esperado>

Contexto:
<pega enlaces a archivos, fuentes, issues, specs o notas>

Restricciones:
<scope, no-objetivos, seguridad, fechas, formato, herramientas>

Entrega esperada:
<archivo, codigo, reporte, spec, checklist, automation, etc.>

Antes de actuar:
1. Clasifica el tipo de trabajo y riesgo.
2. Lee los archivos relevantes del repo.
3. Define criterios de aceptacion.
4. Si hay fuente externa, sigue `knowledge/README.md`.

Durante la ejecucion:
1. Mantén cambios acotados.
2. Preserva evidencia.
3. Separa hechos, inferencias y supuestos.
4. Valida con comandos, screenshots, raw sources o revision documental.

Al final:
1. Resume el diff o artefacto creado.
2. Reporta validacion ejecutada.
3. Indica riesgos residuales.
4. Actualiza memoria si el trabajo genero aprendizaje reusable.
```

## Prompt Para Investigacion De Fuentes

```md
Analiza esta fuente para `<PROJECT_NAME>` siguiendo `knowledge/README.md` y `<PATH_TO_THIS_GUIDE>`.

Fuente:
<url o payload>

Objetivo de analisis:
<que queremos aprender o decidir>

Entregables:
1. Raw source en `knowledge/raw/<source>/`.
2. Processed transcript/thread/summary en `knowledge/processed/`.
3. Insight reusable si aplica.
4. Row en `<SOURCE_INDEX>`.
5. Links hacia los archivos de experimentos, patrones, mejoras de proceso, monetizacion u open questions del proyecto.

Reglas:
- No trates el resumen como evidencia primaria.
- Marca confidence.
- Separa hechos de inferencias.
- Incluye evidence pointers.
- Si falla la captura, guarda evidencia del fallo.
```

## Prompt Para Crear Una Spec

```md
Usa `<SPEC_CONTEXT_PATH>` y `<PATH_TO_THIS_GUIDE>`.

Convierte esta idea en una spec implementable:

<idea>

Requisitos:
- Lee el repo antes de proponer archivos.
- Separa hechos, supuestos y preguntas abiertas.
- Incluye goals, non-goals, user flows, comportamiento actual/deseado, edge cases, acceptance criteria y verification plan.
- No implementes codigo todavia.
```

## Prompt Para Implementar Desde Spec

```md
Implementa siguiendo esta spec:

<ruta o contenido de spec>

Reglas:
- Respeta scope y non-goals.
- Usa patrones existentes del repo.
- No cambies areas no relacionadas.
- Ejecuta el plan de verificacion.
- Si el scope real cambia, actualiza la spec o reporta el bloqueo antes de continuar.

Entrega:
- archivos modificados
- resumen del diff
- comandos ejecutados
- evidencia
- riesgos residuales
- memoria actualizada si aplica
```

## Prompt Para Review

```md
Haz review de este cambio con postura de revisor senior.

Contexto:
<PR, diff, branch, archivos o descripcion>

Prioriza:
- bugs
- regresiones
- riesgos de seguridad/datos
- gaps de validacion
- inconsistencias con la spec
- memoria faltante si el cambio deriva de investigacion

Formato:
1. Hallazgos ordenados por severidad con archivo/linea.
2. Preguntas abiertas.
3. Gaps de prueba.
4. Resumen breve.
```

## Prompt Para Automatizar Un Workflow

```md
Quiero convertir este workflow en automatizacion:

<workflow>

Antes de crear la automatizacion:
1. Verifica que exista al menos una corrida manual exitosa.
2. Revisa el output y registra QA.
3. Define input, output, frecuencia, permisos, logs y rollback.
4. Identifica fuentes de fallo.

Entrega:
- checklist del workflow
- propuesta de script/skill/automation
- validacion manual requerida
- riesgos
- memoria a actualizar

No programes la automatizacion si falta evidencia de una corrida manual valida, salvo que yo lo apruebe explicitamente.
```

## Matriz De Decision

| Situacion | Accion Correcta | No Hacer |
|---|---|---|
| Idea vaga de producto | Crear spec | Implementar directamente |
| Fuente externa nueva | Capturar raw y registrar `<SOURCE_INDEX>` | Resumir solo en chat |
| Tarea chica y clara | Ejecutar y validar rapido | Crear proceso pesado |
| Cambio multi-archivo | Task brief y plan de verificacion | Editar sin scope |
| Workflow repetido | Manual -> checklist -> skill/script | Automatizar sin QA |
| Error de transcript | Guardar failure evidence | Ocultar limitacion |
| Integracion sin plugin | Revisar docs oficiales y crear skill estrecha | Usar APIs no documentadas sin advertir |
| Hallazgo monetizable | Convertir a experimento con success/failure signal | Guardar como idea suelta |
| Output no verificable | Reportar bloqueo y proponer evidencia | Declarar done |

## Checklist De Calidad Para Entregas

Antes de cerrar una tarea, Codex debe poder responder:

- Que se pidio exactamente?
- Que archivos o fuentes se leyeron?
- Que se creo o cambio?
- Que no se cambio?
- Como se valido?
- Que evidencia existe?
- Que supuestos quedan?
- Que riesgo residual existe?
- Que memoria se actualizo o por que no aplica?
- Cual es el siguiente paso mas util?

## Checklist Para Memoria `knowledge/`

Cuando el trabajo toque conocimiento externo:

- [ ] `knowledge/README.md` leido.
- [ ] Raw source guardado o link preservado.
- [ ] Processed artifact creado.
- [ ] Confidence label incluido.
- [ ] Evidence pointers incluidos.
- [ ] Source-index actualizado.
- [ ] Insights conectados a proyecto.
- [ ] Experimentos o preguntas abiertas actualizados.
- [ ] Fallos de captura preservados si existieron.

## Checklist Para Skills

Crear una skill cuando:

- el flujo se repite al menos dos veces o sera delegado a otra IA
- el input/output es estable
- hay reglas de seguridad o validacion especificas
- una checklist en Markdown ya no es suficiente

Contenido minimo de una skill:

- trigger
- objetivo
- inputs
- pasos
- guardrails
- archivos de memoria a leer/escribir
- validacion
- ejemplos de uso
- errores conocidos

No crear una skill si el workflow todavia es exploratorio.

## Checklist Para Automatizaciones

Antes de activar una automation:

- [ ] Corrida manual exitosa.
- [ ] Output revisado por humano o QA definido.
- [ ] Permisos claros.
- [ ] Frecuencia justificada.
- [ ] Logs o evidencia de ejecucion.
- [ ] Accion en caso de fallo.
- [ ] Costo/rate limits revisados si usa APIs.
- [ ] Secretos fuera del repo.
- [ ] Memoria de proceso actualizada.

## Niveles De Confianza

Usar estos labels de forma consistente:

- `verified`: soportado por fuente primaria, comando, test o evidencia directa.
- `inferred`: interpretacion razonable desde evidencia parcial.
- `experimental`: hipotesis lista para probar.
- `unverified`: guardado para investigar; no usar para decisiones.

## Politica De Evidencia

Evidencia aceptable:

- raw API response
- transcript con URL y fecha
- permalink
- screenshot o render
- salida de test o build
- diff revisado
- documento oficial
- failure JSON/log

Evidencia debil:

- recuerdo del chat
- resumen sin fuente
- afirmacion de un video sin timestamp ni transcript
- benchmark sin metodo
- output de IA sin verificacion

## Riesgos Comunes

### Chat Como Memoria

Riesgo: la siguiente sesion pierde estado.

Mitigacion: guardar decisiones en `<PROJECT_MEMORY_DIR>` o docs del repo.

### Automatizacion Prematura

Riesgo: se repiten errores a escala.

Mitigacion: una corrida manual, QA y logs antes de agendar.

### Summaries Como Evidencia

Riesgo: se toman inferencias como hechos.

Mitigacion: `<SOURCE_INDEX>`, raw payload y confidence labels.

### Scope Drift

Riesgo: una tarea pequena se vuelve refactor amplio.

Mitigacion: task contract con non-objectives.

### Agentes Paralelos Sin Estado

Riesgo: duplican trabajo o generan conflictos.

Mitigacion: control plane con owner, files, status y validation.

### Integraciones Fragiles

Riesgo: scripts dependen de APIs no oficiales o sesiones manuales.

Mitigacion: preferir APIs oficiales; documentar gaps y permisos.

## Ejemplo De Flujo Completo

### Entrada Del Usuario

```txt
Quiero analizar comentarios recientes de un canal de YouTube y convertirlos en ideas de producto.
```

### Clasificacion

```txt
tipo: investigacion + producto + workflow repetible
riesgo: medio
requiere web/API: si
artefacto esperado: raw comments, analysis report, experiment ideas, dashboard opcional
```

### Ejecucion

1. Leer `knowledge/README.md`.
2. Confirmar fuente/canal y permisos/API.
3. Capturar comentarios raw en `knowledge/raw/youtube/`.
4. Normalizar datos en `knowledge/processed/`.
5. Clasificar preguntas, objeciones, tool mentions y requests.
6. Crear summary con confidence y evidence pointers.
7. Extraer insights y oportunidades.
8. Actualizar `<SOURCE_INDEX>`.
9. Crear experimentos en el archivo de experimentos del proyecto.
10. Si se repite, crear skill o script.
11. Solo despues proponer automation semanal.

### Validacion

```txt
- raw comments existen
- conteos reproducibles
- muestra manual revisada
- acciones trazan a comentarios
- limitaciones declaradas
```

## Ejemplo De Flujo De Implementacion

### Entrada Del Usuario

```txt
Agrega un reporte semanal que lea la memoria del proyecto y detecte fuentes nuevas, experimentos estancados y proximos pasos.
```

### Clasificacion

```txt
tipo: spec + implementacion + automation opcional
riesgo: medio
artefacto esperado: script o doc generator + brief markdown
```

### Ejecucion Recomendada

1. Crear spec con acceptance criteria.
2. Leer `<SOURCE_INDEX>`, el archivo de experimentos, open questions y process improvements.
3. Implementar generador manual.
4. Ejecutar sobre datos actuales.
5. Revisar output.
6. Guardar brief en `knowledge/briefs/weekly/`.
7. Documentar limitaciones.
8. Despues de QA, proponer automation.

## Definicion De Done

Una tarea esta terminada cuando:

- el artefacto solicitado existe
- el scope esta respetado
- la validacion correspondiente fue ejecutada o se explica por que no
- la evidencia es visible
- los riesgos residuales estan claros
- la memoria fue actualizada si aplica
- el usuario puede continuar sin depender de contexto oculto del chat

## Como Profundizar

Esta guia debe crecer por anexos, no por mezclar todo en el core. Cuando un proyecto necesite mas profundidad, agrega uno de estos anexos:

| Anexo | Usar Cuando | Archivo Sugerido |
|---|---|---|
| Research Ops | muchas fuentes externas, RAG, transcripts, benchmarks | `docs/ai/research-ops.md` |
| Product Discovery | ideas, monetizacion, entrevistas, experimentos | `docs/ai/product-discovery.md` |
| Engineering Delivery | specs, PRs, QA, releases | `docs/ai/engineering-delivery.md` |
| Agent Harness | subagentes, permisos, contexto, task contracts | `docs/ai/agent-harness.md` |
| Automation Policy | jobs recurrentes, alertas, reportes | `docs/ai/automation-policy.md` |
| Security And Data | secretos, PII, permisos, proveedores | `docs/ai/security-and-data.md` |
| UI QA | frontend, screenshots, accesibilidad, visual regression | `docs/ai/ui-qa.md` |

Regla: si una seccion solo aplica a un proyecto, ponerla en un adaptador. Si aplica a tres o mas proyectos, promoverla al core.

## Portable Adoption Checklist

Para reutilizar esta guia en un proyecto nuevo:

- [ ] Copiar el archivo a una ruta estable.
- [ ] Completar `Project Profile`.
- [ ] Definir `<PROJECT_MEMORY_DIR>`.
- [ ] Crear o mapear `<SOURCE_INDEX>`.
- [ ] Definir comandos de validacion.
- [ ] Agregar reglas de seguridad y datos sensibles.
- [ ] Crear una primera tarea con `Codex Task Brief`.
- [ ] Ejecutar una validacion real.
- [ ] Registrar el primer aprendizaje reusable.
- [ ] Decidir si hace falta un anexo especifico.

## Adaptador Actual Para `ia-learning`

Para este repo, el foco inmediato debe ser:

1. Consolidar Codex como sistema operativo de trabajo mediante esta guia.
2. Ejecutar un primer workflow real usando el control plane.
3. Convertir el workflow exitoso en una skill o checklist.
4. Registrar el resultado en `experiments.md`.
5. Evaluar si merece automatizacion.

Valores locales:

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
PATH_TO_THIS_GUIDE=knowledge/projects/ia-learning/codex-operating-system-guide.md
SPEC_CONTEXT_PATH=knowledge/projects/ia-learning/spec-driven-development-context.md
```

## Siguiente Experimento Sugerido

Crear un `Daily Control Plane` real para una tarea pequena del proyecto y medir:

- cuantas aclaraciones evita
- si mejora la evidencia final
- si reduce rework
- si deja memoria reusable
- si el formato es demasiado pesado para tareas pequenas

Resultado esperado:

- Si funciona, promover el formato a `agent-workflows.md`.
- Si pesa demasiado, crear una version compacta de 5 campos.
