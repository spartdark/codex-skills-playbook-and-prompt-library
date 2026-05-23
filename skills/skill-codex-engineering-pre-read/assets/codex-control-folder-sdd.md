# Codex Control Folder SDD

## Proposito

Definir como crear y usar una carpeta de control para trabajar con Codex bajo desarrollo guiado por especificaciones.

La carpeta de control es el lugar donde Codex encuentra el estado operativo del proyecto: specs, decisiones, preguntas abiertas, experimentos, validaciones y fuentes. Su funcion es convertir conversaciones sueltas en unidades de trabajo trazables.

Este documento aplica el enfoque de `sdd-architect`: requisitos claros, alcance delimitado, criterios de aceptacion observables, plan tecnico y trazabilidad entre intencion, implementacion y validacion.

## Contexto Codex

Usa este patron junto con:

- `docs/skills/codex-practical-guide.md`
- `docs/skills/codex-prompt-briefs.md`
- `docs/skills/codex-engineering-pre-read.md`
- `knowledge/projects/ia-learning/spec-driven-development-context.md`

La guia practica de Codex define la unidad de trabajo como:

```txt
intencion -> contexto -> alcance -> implementacion -> verificacion -> memoria
```

La carpeta de control materializa esa cadena en archivos que Codex puede leer y actualizar.

## Problema

Cuando Codex trabaja solo desde chat, el proyecto pierde continuidad:

- las decisiones quedan enterradas en conversaciones;
- los criterios de aceptacion cambian sin registro;
- las fuentes externas se resumen sin evidencia primaria;
- los experimentos no se conectan con implementacion;
- la verificacion queda implicita o incompleta;
- futuras sesiones no saben que ya se decidio.

## Usuario Objetivo

- Desarrollador usando Codex en un repo local.
- Equipo pequeno que quiere usar Codex para specs, implementacion, review y memoria.
- Proyecto que combina investigacion externa, ideas de producto, tareas tecnicas y validacion.

## Objetivo

Crear una estructura minima para que Codex pueda:

1. leer contexto actualizado antes de actuar;
2. convertir ideas en specs implementables;
3. separar alcance y no alcance;
4. registrar decisiones y preguntas abiertas;
5. ejecutar o documentar verificacion;
6. guardar aprendizajes reutilizables;
7. cerrar cada tarea con evidencia revisable.

## No Objetivos

- No reemplaza Git, issues, Linear, Jira o PRs.
- No obliga a documentar tareas pequenas o comandos puntuales.
- No convierte todo el repo en burocracia de specs.
- No autoriza a Codex a modificar archivos sin criterios de aceptacion.
- No trata summaries generados como evidencia primaria.

## Estructura Recomendada

Para proyectos con memoria local:

```txt
knowledge/projects/<project>/
  README.md
  specs/
    001-feature-or-workflow.md
  decisions.md
  open-questions.md
  experiments.md
  validation.md
  source-links.md
  changelog.md
```

Para proyectos sin `knowledge/`:

```txt
docs/control/
  README.md
  specs/
    001-feature-or-workflow.md
  decisions.md
  open-questions.md
  experiments.md
  validation.md
  source-links.md
  changelog.md
```

En `ia-learning`, la ruta preferida es:

```txt
knowledge/projects/ia-learning/
```

## Responsabilidad De Cada Archivo

### `README.md`

Estado ejecutivo del proyecto para Codex.

Debe responder:

- que intenta lograr el proyecto;
- que esta activo ahora;
- que fuentes o docs son canonicos;
- cuales son las prioridades actuales;
- como debe comportarse Codex en este proyecto.

Template:

```md
# <project>

## Objetivo

## Estado Actual

## Prioridades

## Rutas Canonicas

## Como Debe Trabajar Codex

## Ultima Revision
```

### `specs/`

Specs implementables. Una spec debe existir antes de pedir a Codex una feature mediana o riesgosa.

Template:

```md
# Spec: <nombre>

## Source Idea

## Problem

## Goals

## Non-Goals

## Current Behavior

## Desired Behavior

## Scope

## Out Of Scope

## User Flows

## Technical Approach

## Files Or Areas Likely Involved

## Data, API Or Integration Changes

## Edge Cases

## Acceptance Criteria

## Verification Plan

## Risks

## Open Questions
```

Regla para Codex:

- si la tarea no tiene criterios de aceptacion, primero crear o completar la spec;
- si el scope cambia durante implementacion, actualizar la spec antes de ampliar el cambio;
- si la verificacion es ambigua, proponer primero una forma de verificar.

### `decisions.md`

Registro de decisiones que deben sobrevivir al chat.

Template:

```md
# Decisions

## YYYY-MM-DD - <decision>

- Status: proposed / accepted / superseded
- Context:
- Decision:
- Rationale:
- Alternatives considered:
- Evidence:
- Consequences:
```

Usalo cuando:

- se elige una arquitectura;
- se descarta una alternativa;
- se decide una convencion de carpetas;
- se acepta un tradeoff;
- se fija una regla para Codex.

### `open-questions.md`

Preguntas que afectan scope, implementacion o validacion.

Template:

```md
# Open Questions

## <question>

- Status: open / answered / parked
- Why it matters:
- Options:
- Current assumption:
- Needed evidence:
- Owner:
```

Regla para Codex:

- si una pregunta bloquea implementacion segura, detenerse y pedir decision;
- si no bloquea, documentar el supuesto y seguir dentro del scope.

### `experiments.md`

Hipotesis pequenas y verificables.

Template:

```md
# Experiments

## <experiment>

- Hypothesis:
- Method:
- Success criteria:
- Evidence to collect:
- Status: pending / running / done / dropped
- Result:
- Follow-up:
```

Usalo para validar:

- si una automatizacion de Codex ahorra tiempo;
- si un workflow reduce retrabajo;
- si una fuente externa produce tareas utiles;
- si un comando de validacion es suficiente.

### `validation.md`

Mapa de comandos, checks y flujos manuales que Codex debe usar.

Template:

````md
# Validation

## Default Commands

```bash
<test command>
<lint command>
<typecheck command>
```

## Manual Checks

- <flujo o inspeccion manual>

## Evidence Expected From Codex

- command output summary
- screenshots when UI changes
- logs or traces for runtime behavior
- explicit unverified assumptions

## Known Gaps

- <validacion faltante o lenta>
````

Regla para Codex:

- ejecutar comandos cuando sea posible;
- si no puede ejecutar algo, explicar por que y marcar riesgo;
- no cerrar tareas relevantes sin evidencia de verificacion o brecha explicita.

### `source-links.md`

Indice de fuentes que influyen en decisiones del proyecto.

Template:

```md
# Source Links

| Date | Source | Claim Or Use | Evidence | Confidence |
|---|---|---|---|---|
| YYYY-MM-DD |  |  |  | verified / inferred / unverified |
```

En proyectos con `knowledge/`, este archivo puede apuntar a `knowledge/raw/`, `knowledge/processed/` y `knowledge/projects/<project>/source-index.md`.

### `changelog.md`

Registro humano de cambios significativos en specs, decisiones o workflows.

Template:

```md
# Changelog

## YYYY-MM-DD

- Changed:
- Why:
- Evidence:
- Follow-up:
```

No reemplaza Git. Resume cambios de direccion que Codex debe entender rapido.

## Requisitos Funcionales

| ID | Requisito | Archivo | Criterio de aceptacion |
|---|---|---|---|
| FR-1 | Codex debe encontrar el objetivo y estado del proyecto | `README.md` | Un agente nuevo puede explicar que se esta construyendo y que rutas son canonicas |
| FR-2 | Codex debe implementar features medianas desde specs | `specs/` | Cada spec tiene goals, non-goals, acceptance criteria y verification plan |
| FR-3 | Codex debe preservar decisiones importantes | `decisions.md` | Cada decision tiene contexto, decision, rationale y evidencia |
| FR-4 | Codex debe mantener incertidumbre visible | `open-questions.md` | Preguntas abiertas incluyen impacto, supuesto actual y evidencia necesaria |
| FR-5 | Codex debe validar hipotesis antes de promover procesos | `experiments.md` | Cada experimento tiene hipotesis, metodo y criterio de exito |
| FR-6 | Codex debe saber como verificar cambios | `validation.md` | Existen comandos o checks manuales por defecto |
| FR-7 | Codex debe conectar fuentes con decisiones | `source-links.md` | Claims importantes tienen evidencia y confidence |

## Requisitos No Funcionales

- Bajo overhead: no usar este flujo completo para tareas triviales.
- Trazabilidad: toda recomendacion importante debe apuntar a archivo, comando, fuente o supuesto.
- Reusabilidad: una nueva sesion de Codex debe poder retomar contexto leyendo la carpeta.
- Seguridad: permisos y acciones externas deben documentarse antes de automatizar.
- Mantenibilidad: templates pequenos, Markdown simple y enlaces locales estables.

## Plan Tecnico Por Fases

### Fase 1 - Crear estructura minima

Entregables:

- carpeta de control;
- `README.md`;
- `specs/`;
- `open-questions.md`;
- `validation.md`.

Criterio de aceptacion:

- Codex puede leer la carpeta y producir un resumen del proyecto;
- hay al menos un comando o flujo de verificacion documentado;
- hay una primera pregunta abierta o decision registrada.

### Fase 2 - Introducir specs para tareas medianas

Entregables:

- primera spec en `specs/`;
- criterios de aceptacion observables;
- plan de verificacion;
- prompt de implementacion desde spec.

Criterio de aceptacion:

- Codex puede implementar o planear desde la spec sin pedir contexto basico;
- la tarea final reporta cambios, verificacion, riesgos y supuestos.

### Fase 3 - Conectar decisiones, fuentes y experimentos

Entregables:

- `decisions.md`;
- `source-links.md`;
- `experiments.md`;
- links a `knowledge/` cuando aplique.

Criterio de aceptacion:

- cada decision importante tiene evidencia;
- cada experimento tiene hipotesis y exito medible;
- fuentes externas no quedan solo en chat.

### Fase 4 - Automatizar pre-reads

Entregables:

- prompt o runbook de pre-read;
- output destino aprobado;
- ventana de analisis explicita;
- reglas de no modificacion de codigo.

Criterio de aceptacion:

- el pre-read produce decisiones, riesgos y tareas Codex accionables;
- no modifica backlog, specs ni codigo sin instruccion explicita.

## Prompts Para Codex

### Crear Carpeta De Control

```md
Usa `docs/skills/codex-control-folder-sdd.md` como guia.

Crea una carpeta de control para este proyecto en `[ruta]`.

No implementes features. Solo crea documentacion operativa.

Incluye:
- README.md
- specs/
- decisions.md
- open-questions.md
- experiments.md
- validation.md
- source-links.md
- changelog.md

Adapta los templates al repo actual.
No inventes comandos de validacion: inspecciona el repo y documenta solo los que existan o marca gaps.

Entrega:
- archivos creados;
- supuestos;
- preguntas abiertas;
- siguiente accion recomendada.
```

### Generar Spec Desde Idea

```md
Usa la carpeta de control de `[project]` y `knowledge/projects/ia-learning/spec-driven-development-context.md`.

Convierte esta idea en una spec en `[ruta]/specs/<id>-<name>.md`.

Idea:
<pegar idea>

No implementes codigo.
Lee el repo antes de proponer archivos.
Separa hechos de supuestos.
Incluye acceptance criteria y verification plan.
```

### Implementar Desde Spec

```md
Implementa siguiendo esta spec:
`[ruta]/specs/<id>-<name>.md`

Reglas:
- no cambies el scope sin actualizar primero la spec;
- sigue patrones existentes del repo;
- ejecuta la verificacion indicada en la spec o explica por que no puedes;
- actualiza decisions/open-questions/validation solo si aparece aprendizaje reusable.

Entrega:
- archivos modificados;
- resumen del cambio;
- verificacion ejecutada;
- evidencia;
- riesgos restantes;
- memoria actualizada.
```

### Hacer Review SDD

```md
Revisa esta spec o cambio con criterio SDD.

Valida:
- problema claro;
- usuario explicito;
- scope y no-scope;
- criterios de aceptacion observables;
- plan tecnico conectado a requisitos;
- riesgos y decisiones abiertas;
- verificacion realista.

Devuelve hallazgos ordenados por severidad y acciones concretas.
```

## Trazabilidad

| Intencion | Archivo | Uso Por Codex | Validacion |
|---|---|---|---|
| Entender el proyecto | `README.md` | Contexto inicial | Codex puede resumir objetivo y prioridades |
| Definir trabajo | `specs/*.md` | Implementacion y review | Acceptance criteria completos |
| Preservar decisiones | `decisions.md` | Evitar repetir debates | Decision tiene rationale y evidencia |
| Manejar incertidumbre | `open-questions.md` | Bloquear o documentar supuestos | Pregunta tiene impacto y siguiente evidencia |
| Validar hipotesis | `experiments.md` | Convertir research en aprendizaje | Resultado y follow-up registrados |
| Verificar entregas | `validation.md` | Ejecutar checks | Comandos o gaps documentados |
| Conectar fuentes | `source-links.md` | Grounding de recomendaciones | Confidence y evidencia visibles |

## Definition Of Done

La carpeta de control esta lista cuando:

- existe una ruta canonica documentada;
- Codex puede explicar el estado del proyecto leyendo solo esa carpeta y docs enlazados;
- hay al menos una spec o template de spec;
- hay criterios de aceptacion y verificacion documentados;
- las decisiones y preguntas abiertas tienen lugar propio;
- las fuentes externas se enlazan con evidencia;
- el flujo indica cuando Codex debe detenerse, preguntar o seguir con supuestos.

## Checklist SDD

- El problema esta descrito con claridad.
- El usuario objetivo es explicito.
- El alcance y no alcance estan delimitados.
- Los criterios de aceptacion son observables.
- El plan tecnico esta conectado con los requisitos.
- Hay decisiones abiertas y riesgos identificados.
- La verificacion produce evidencia revisable.
- La memoria del proyecto se actualiza solo cuando hay aprendizaje reusable.

## Antipatrones

- Crear la carpeta y no usarla en prompts futuros.
- Guardar todo en `README.md` sin separar specs, decisiones y validacion.
- Pedir a Codex que implemente desde una idea vaga cuando el riesgo es medio o alto.
- Actualizar codigo pero no actualizar la spec cuando cambia el comportamiento.
- Documentar comandos de validacion que no existen.
- Mezclar evidencia verificada con inferencias sin confidence.
- Convertir cada microtarea en una spec pesada.
