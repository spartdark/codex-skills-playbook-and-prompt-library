# Research Ops Evidence Guide

Guia operativa portable para investigacion con evidencia: raw sources, transcripts, summaries, insights, source index y enlaces hacia decisiones del proyecto.

Esta guia es un anexo especializado de [Codex Operating System Guide](codex-operating-system-guide.md) y se puede ejecutar con el control de agentes descrito en [Agent Control Plane Guide](agent-control-plane-guide.md). Usala cuando una IA analice YouTube, Reddit, articulos, docs, papers, changelogs, benchmarks, comentarios, issues publicos o cualquier fuente externa que pueda influir en decisiones del proyecto.

## Proposito

Research ops convierte fuentes ruidosas en conocimiento reusable y auditable:

```txt
source -> raw evidence -> normalized artifact -> summary -> insight -> project decision -> experiment/backlog
```

El objetivo no es acumular resúmenes. El objetivo es conservar evidencia primaria, separar hechos de inferencias y conectar hallazgos con decisiones, experimentos o preguntas abiertas.

## Resultado Esperado

Cada fuente util debe terminar con:

- raw source preservado o enlace verificable;
- transcript, thread, scrape, export o metadata normalizada;
- summary que separe hechos, inferencias, recomendaciones y limitaciones;
- insights atomicos con evidence pointers;
- row en source index;
- links hacia decisiones del proyecto;
- confidence label;
- next action o razon para no actuar.

## Variables Portables

```txt
PROJECT_NAME=<nombre humano del proyecto>
PROJECT_ID=<slug estable>
PROJECT_MEMORY_DIR=knowledge/projects/<project-id>
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
TRANSCRIPTS_DIR=<PROCESSED_DIR>/transcripts
THREADS_DIR=<PROCESSED_DIR>/threads
SUMMARIES_DIR=<PROCESSED_DIR>/summaries
INSIGHTS_DIR=<PROCESSED_DIR>/insights
SOURCE_INDEX=<PROJECT_MEMORY_DIR>/source-index.md
PROJECT_DECISIONS_DIR=<PROJECT_MEMORY_DIR>
BRIEFS_DIR=knowledge/briefs
SCHEMA_DIR=knowledge/schema
PATH_TO_THIS_GUIDE=<ruta a esta guia>
```

## Folder Contract

Estructura recomendada:

```txt
knowledge/
  raw/
    youtube/
    reddit/
    web/
    docs/
    papers/
    other/
  processed/
    transcripts/
    threads/
    summaries/
    insights/
  projects/
    <project-id>/
      source-index.md
      experiments.md
      implementation-patterns.md
      process-improvements.md
      monetization-ideas.md
      ai-news.md
      open-questions.md
      decisions.md
  briefs/
    weekly/
    topic/
  schema/
    source-metadata.template.json
    source-package.template.md
    summary.template.md
    insight.template.md
```

No todos los proyectos necesitan todos los archivos desde el inicio. El minimo viable es:

```txt
knowledge/raw/
knowledge/processed/summaries/
knowledge/processed/insights/
<PROJECT_MEMORY_DIR>/source-index.md
<PROJECT_MEMORY_DIR>/experiments.md
<PROJECT_MEMORY_DIR>/open-questions.md
```

## Principios

1. Raw primero, resumen despues.
2. Una fuente sin URL, payload o failure evidence no puede sostener una decision fuerte.
3. Un summary no es evidencia primaria.
4. Todo insight reusable debe apuntar a evidencia.
5. Toda recomendacion debe marcar confidence.
6. Toda limitacion de captura debe quedar visible.
7. Toda fuente de alto valor debe conectar con una decision, experimento, patron o pregunta abierta.
8. Toda investigacion repetible debe convertirse en checklist, script, skill o automation despues de QA.

## Source Lifecycle

```txt
intake -> capture -> normalize -> summarize -> extract insights -> index -> link decisions -> validate -> brief/automation
```

### 1. Intake

Decidir si la fuente merece entrar al sistema.

Capturar:

- source type;
- source URL/permalink;
- title;
- author/channel/community;
- published date si existe;
- captured date;
- user question;
- project relevance;
- expected decision.

No procesar a fondo fuentes que no tienen una pregunta clara o valor probable.

### 2. Capture Raw

Guardar evidencia primaria antes de analizar.

Ejemplos:

- YouTube: oEmbed, metadata, transcript JSON, captions, screenshot si hay elementos visuales relevantes.
- Reddit: post JSON, comentarios, permalinks, timestamps, subreddit.
- Web/docs: URL, captured metadata, relevante excerpt corto, fecha de acceso.
- Papers: DOI/arXiv URL, metadata, PDF link o local copy si permitido.
- APIs: response JSON, request parameters sin secretos.
- Failures: error JSON/log, status code, extractor warning, rate-limit note.

Regla: si la captura falla pero la fuente es importante, guardar el fallo.

### 3. Normalize

Convertir raw en artefacto legible y estable.

Tipos:

- transcript Markdown con timestamps;
- thread Markdown con comentarios y permalinks;
- source pack Markdown/JSON;
- notes normalizadas;
- failure note con causa probable.

Debe incluir:

- URL original;
- captured date;
- source type;
- confidence inicial;
- limitaciones;
- links al raw.

### 4. Summarize

Crear summary con estructura consistente.

Debe separar:

- fuente;
- resumen ejecutivo;
- ideas clave;
- hechos respaldados;
- inferencias;
- casos practicos;
- oportunidades;
- prompts detectados si aplica;
- experimentos recomendados;
- preguntas abiertas;
- evidencia y limitaciones.

No mezclar "lo que dijo la fuente" con "lo que recomendamos hacer" sin marcarlo.

### 5. Extract Insights

Un insight debe ser atomico: una idea reusable con evidencia.

Buen insight:

- se entiende sin releer toda la fuente;
- apunta a evidencia;
- tiene confidence;
- dice por que importa;
- propone patron, experimento, decision o pregunta.

Mal insight:

- es un resumen amplio;
- no tiene evidencia;
- mezcla cinco temas;
- recomienda sin explicar por que.

### 6. Source Index

Registrar la fuente en `<SOURCE_INDEX>`.

El source index es el punto de entrada para no depender de memoria del chat.

Columnas recomendadas:

```md
| Captured | Source | Title | Raw | Processed | Insights | Confidence | Project relevance |
|---|---|---|---|---|---|---|---|
```

Reglas:

- agregar solo fuentes que generen conocimiento reusable;
- preferir links locales a raw/processed;
- marcar limitaciones de transcript o metadata;
- mantener project relevance accionable;
- no indexar consultas descartables.

### 7. Link To Project Decisions

Conectar hallazgos con archivos de decision:

- `experiments.md`: hipotesis verificables.
- `implementation-patterns.md`: patrones tecnicos reutilizables.
- `process-improvements.md`: mejoras de forma de trabajo.
- `monetization-ideas.md`: ofertas, productos, servicios o cursos.
- `ai-news.md`: cambios temporales de herramientas/modelos.
- `open-questions.md`: dudas que requieren evidencia.
- `decisions.md` o ADRs: decisiones aceptadas.
- backlog/issues/specs: trabajo implementable.

Si una fuente no cambia nada, registrar "no action" con razon breve.

### 8. Validate Evidence

Antes de cerrar:

- comprobar que raw existe o URL resuelve;
- comprobar que processed apunta al raw;
- comprobar que summary marca confidence;
- comprobar que insights tienen evidence pointers;
- comprobar que source index enlaza artefactos estables;
- comprobar que project links existen;
- declarar limitaciones.

### 9. Promote Or Archive

Promover si:

- aparece en varias fuentes;
- cambia una decision;
- genera experimento;
- revela riesgo;
- se convierte en workflow reusable.

Archivar o dejar bajo si:

- fuente incompleta;
- evidencia debil;
- idea no relevante;
- duplicado sin señal nueva.

## Confidence Labels

Usar consistentemente:

- `verified`: soportado directamente por raw source, transcript, docs oficiales, comando o evidencia primaria.
- `inferred`: interpretacion razonable desde evidencia parcial.
- `experimental`: hipotesis lista para validar con prueba.
- `unverified`: guardado para futura investigacion; no usar como base de decision.

## Evidence Classes

| Clase | Descripcion | Decision Weight |
|---|---|---|
| Primary raw | transcript, API response, docs oficiales, paper, permalink | alto |
| Primary failure | error de extractor, HTTP status, unavailable captions | alto para limitaciones |
| Normalized artifact | transcript/thread Markdown derivado de raw | medio-alto |
| Summary | sintesis derivada | medio |
| Secondary summary | resumen de terceros o IA sin raw | bajo-medio |
| Inference | conclusion del agente | bajo hasta validarse |
| Anecdote | comentario aislado o opinion | bajo |

Regla: decisiones fuertes requieren primary raw o multiples fuentes independientes.

## Metadata Standard

Cada fuente debe tener:

```yaml
source_type:
source_id:
source_url:
canonical_url:
source_title:
author:
community_or_channel:
published_at:
captured_at:
language:
topics:
projects:
raw_evidence:
processed_artifacts:
confidence:
evidence_pointer:
limitations:
```

Para JSON:

```json
{
  "source_type": "youtube|reddit|web|docs|paper|api|other",
  "source_id": "",
  "url": "",
  "canonical_url": "",
  "title": "",
  "author": "",
  "community_or_channel": "",
  "published_at": "",
  "captured_at": "",
  "language": "",
  "topics": [],
  "projects": [],
  "raw_evidence": [],
  "processed_artifacts": [],
  "confidence": "verified|inferred|experimental|unverified",
  "evidence_pointer": "",
  "limitations": ""
}
```

## Naming Convention

```txt
<source>-<short-title>-<source-id>.<ext>
```

Ejemplos:

```txt
youtube-codex-full-course-KXIdYEdOPys-en-auto.json
youtube-codex-full-course-KXIdYEdOPys-transcript.md
youtube-codex-full-course-KXIdYEdOPys-summary.md
youtube-codex-full-course-agent-workflows.md
reddit-local-llm-costs-thread-abc123.json
web-openai-codex-docs-2026-05-20.json
```

Reglas:

- nombres estables;
- source id si existe;
- fecha si el contenido cambia con frecuencia;
- idioma si hay transcript;
- evitar espacios y caracteres especiales.

## Source Package

Para fuentes importantes, crear un paquete de fuente.

```md
# Source Package: <title>

## Metadata

- Source type:
- Source id:
- URL:
- Title:
- Author:
- Published:
- Captured:
- Language:
- Confidence:
- Project relevance:

## Raw Evidence

- 

## Normalized Artifacts

- 

## Summaries

- 

## Insights

- 

## Project Links

- 

## Limitations

- 

## Next Actions

- 
```

## Transcript Policy

Transcripts son evidencia derivada, no siempre perfectos.

### Transcript Debe Incluir

- source URL;
- video/audio id;
- language;
- captured date;
- extraction method;
- whether auto-caption or human;
- timestamps;
- known gaps;
- raw transcript path.

### Transcript Failure Debe Incluir

- source URL;
- attempted method;
- error message/status;
- captured date;
- fallback attempts;
- recommended retry;
- whether analysis used metadata or secondary summary instead.

### Transcript Confidence

| Caso | Confidence |
|---|---|
| official transcript/manual captions captured | verified source capture |
| auto-caption captured | verified capture; content accuracy unverified |
| transcript unavailable, metadata only | metadata verified; content inferred |
| secondary summary only | inferred from secondary source |
| extractor failed and no fallback | unverified for content |

## Summary Template

```md
---
source_type:
source_url:
canonical_url:
source_title:
author:
published_at:
captured_at:
language:
raw_evidence: []
normalized_artifacts: []
confidence:
projects: []
limitations:
---

# Fuente

# Resumen Ejecutivo

# Hechos Respaldados

# Inferencias

# Ideas Clave

# Casos Practicos

# Oportunidades Para El Proyecto

# Patrones Reusables

# Riesgos O Limitaciones

# Experimentos Recomendados

# Prompts Detectados

# Preguntas Abiertas

# Evidence Pointers
```

## Insight Template

```md
---
source_type:
source_url:
source_title:
author:
published_at:
captured_at:
confidence:
topics: []
projects: []
evidence_pointer:
---

# <Insight Title>

## Claim

## Evidence

## Why It Matters

## Applicable Project Areas

## Decision Link

## Experiment Or Action

## Risks And Limits

## Open Questions
```

## Project Link Types

| Link Type | Uso | Archivo |
|---|---|---|
| experiment | probar hipotesis | `experiments.md` |
| implementation pattern | reutilizar tecnica | `implementation-patterns.md` |
| process improvement | mejorar workflow | `process-improvements.md` |
| monetization | validar oferta | `monetization-ideas.md` |
| AI/tooling news | cambio temporal | `ai-news.md` |
| open question | falta evidencia | `open-questions.md` |
| decision | decision aceptada | `decisions.md` o ADR |
| backlog/spec | trabajo implementable | issue/spec |

Cada link debe incluir evidencia o apuntar al insight que la contiene.

## Decision Link Template

```md
## <Decision Or Experiment Name>

- Source:
- Insight:
- Evidence:
- Confidence:
- Decision status: proposed | accepted | rejected | superseded
- Reason:
- Action:
- Validation:
- Owner:
- Review date:
```

## Research Intake Contract

Usar antes de iniciar una investigacion.

```md
# Research Intake

## Question

<que queremos saber o decidir>

## Source

- URL:
- Type:
- Expected relevance:

## Scope

### In

- 

### Out

- 

## Evidence Required

- raw:
- transcript/thread:
- summary:
- insight:
- source index:
- project links:

## Confidence Target

verified | inferred | experimental | unverified acceptable

## Decision Target

- experiment:
- implementation:
- process:
- monetization:
- open question:

## Stop Conditions

- 
```

## Research Execution Checklist

- [ ] Read project research rules.
- [ ] Define research question.
- [ ] Capture source metadata.
- [ ] Save raw evidence.
- [ ] Save failure evidence if capture fails.
- [ ] Normalize transcript/thread/source pack.
- [ ] Create summary with confidence and limitations.
- [ ] Extract atomic insights.
- [ ] Update source index.
- [ ] Link to project decisions.
- [ ] Add experiment or open question if needed.
- [ ] Validate links and evidence pointers.
- [ ] Report residual uncertainty.

## Evidence QA Checklist

- [ ] Raw path or URL exists.
- [ ] Captured date present.
- [ ] Source type present.
- [ ] Author/channel/community present if available.
- [ ] Processed artifact links raw.
- [ ] Summary separates facts and inferences.
- [ ] Confidence label present.
- [ ] Evidence pointer present.
- [ ] Transcript limitations visible.
- [ ] Source index row added.
- [ ] Project link added or no-action reason documented.
- [ ] Claims do not exceed evidence.

## Source Index QA

```md
| Captured | Source | Title | Raw | Processed | Insights | Confidence | Project relevance |
```

Checks:

- `Captured`: ISO date.
- `Source`: platform/type, not vague.
- `Title`: human-readable.
- `Raw`: local raw evidence or failure evidence.
- `Processed`: transcript/thread/summary links.
- `Insights`: insight links or `n/a`.
- `Confidence`: includes limitations.
- `Project relevance`: decision-oriented.

## Claim Hygiene

Use these prefixes when writing research outputs:

- `Fact:` supported directly by source.
- `Observed:` visible in metadata, transcript, comments, or docs.
- `Inference:` reasoned interpretation.
- `Hypothesis:` testable claim.
- `Recommendation:` proposed action.
- `Limitation:` evidence gap or caveat.

Avoid:

- "proves" unless evidence is strong;
- "users want" from one comment;
- "best" without benchmark criteria;
- "latest" without current date and source;
- quoting long copyrighted material.

## Research Roles

### Capture Agent

Owns raw source preservation.

Output:

- metadata;
- raw payload;
- failure logs;
- capture notes.

### Normalization Agent

Owns transcripts, threads or source packs.

Output:

- readable Markdown;
- structured JSON if useful;
- limitations.

### Analysis Agent

Owns summary and insights.

Output:

- summary;
- insights;
- confidence;
- evidence pointers.

### Decision Linker

Owns project memory updates.

Output:

- source-index row;
- experiment/pattern/process update;
- open questions;
- no-action note if relevant.

### Evidence Reviewer

Owns QA.

Output:

- missing evidence;
- overclaim risks;
- broken links;
- confidence corrections.

## Prompts

### Prompt Maestro

```md
Usa `<PATH_TO_THIS_GUIDE>` para ejecutar research ops con evidencia.

Research question:
<pregunta o decision>

Source:
<URL, payload, transcript, thread, docs, etc.>

Project context:
<proyecto, area, decision esperada>

Entregables:
1. Raw source o failure evidence.
2. Normalized transcript/thread/source pack.
3. Summary con hechos, inferencias, limitaciones y confidence.
4. Insights atomicos con evidence pointers.
5. Source index row.
6. Links hacia decisiones, experimentos, patrones, mejoras o preguntas abiertas.

Reglas:
- Raw primero.
- No trates summaries como evidencia primaria.
- Marca confidence.
- Separa hechos de inferencias.
- Declara limitaciones.
- No cierres sin evidence QA.
```

### Prompt Para Capture Agent

```md
Actua como Capture Agent.

Fuente:
<url o payload>

Tarea:
1. Captura metadata.
2. Guarda raw evidence o failure evidence.
3. No analices aun.
4. Reporta paths, metodos, errores y limitaciones.

Output:
- source metadata
- raw paths
- failure paths
- capture confidence
- recommended next step
```

### Prompt Para Analysis Agent

```md
Actua como Analysis Agent.

Input:
<raw paths + normalized artifact>

Produce:
- summary estructurado
- facts
- inferences
- recommendations
- limitations
- insights atomicos
- confidence labels
- evidence pointers

No uses claims que no puedan rastrearse a evidencia.
```

### Prompt Para Decision Linker

```md
Actua como Decision Linker.

Input:
<summary + insights + source metadata>

Actualiza o propone actualizaciones para:
- source index
- experiments
- implementation patterns
- process improvements
- monetization ideas
- ai news
- open questions
- decisions/backlog/specs

Para cada link incluye:
- source
- insight
- confidence
- action
- validation
```

### Prompt Para Evidence Reviewer

```md
Actua como Evidence Reviewer.

Revisa estos artefactos:
<raw, processed, summary, insights, source-index row, project links>

Busca:
- raw faltante
- links rotos
- claims sin evidencia
- facts mezclados con inferencias
- confidence exagerado
- limitaciones ocultas
- falta de project decision link

Devuelve:
1. Findings por severidad.
2. Correcciones requeridas.
3. Confidence adjustments.
4. Approval: pass | pass with caveats | fail.
```

## Failure Handling

| Falla | Que Guardar | Como Reportar |
|---|---|---|
| transcript unavailable | error JSON/log + metadata | content unverified |
| HTTP 429/rate limit | status, retry time, tool | retry later |
| deleted source | URL, timestamp, unavailable note | source inaccessible |
| paywall/login | metadata + access limitation | partial evidence |
| language mismatch | detected language + attempted language | translation risk |
| malformed export | raw payload + parser error | normalization failed |
| conflicting sources | both sources + comparison | decision pending |

Nunca borres fallos utiles: son evidencia de limitaciones.

## Automation Policy

Research automation solo despues de:

- una corrida manual exitosa;
- output revisado;
- schema estable;
- rate limits entendidos;
- failure handling definido;
- source index update probado;
- QA checklist aplicada.

Automatizaciones candidatas:

- reporte semanal de fuentes nuevas;
- retry de transcript failures;
- source-index consistency check;
- stale experiment detection;
- brief mensual por tema;
- RAG indexing local.

## RAG Readiness

Una fuente esta lista para RAG si:

- tiene metadata completa;
- raw o URL preservado;
- normalized artifact limpio;
- chunks pueden apuntar a source id;
- confidence y limitations estan disponibles;
- project links estan separados de content;
- no contiene secretos ni PII indebida;
- derechos de uso permiten indexacion local.

Campos utiles para futura base:

```txt
sources
source_items
chunks
embeddings
projects
insights
project_links
briefs
validation_logs
```

## Portable Adoption Checklist

Para usar esta guia en otro proyecto:

- [ ] Crear `knowledge/` o mapear memoria equivalente.
- [ ] Definir `<PROJECT_MEMORY_DIR>`.
- [ ] Crear `<SOURCE_INDEX>`.
- [ ] Copiar templates de source package, summary e insight.
- [ ] Definir confidence labels.
- [ ] Definir que fuentes se aceptan.
- [ ] Definir reglas de derechos, PII y secretos.
- [ ] Ejecutar una fuente piloto.
- [ ] Hacer evidence QA.
- [ ] Revisar si el output cambio una decision.

## Adaptador Actual Para `ia-learning`

Valores locales:

```txt
PROJECT_NAME=ia-learning
PROJECT_ID=ia-learning
PROJECT_MEMORY_DIR=knowledge/projects/ia-learning
RAW_DIR=knowledge/raw
PROCESSED_DIR=knowledge/processed
SOURCE_INDEX=knowledge/projects/ia-learning/source-index.md
PATH_TO_THIS_GUIDE=knowledge/projects/ia-learning/research-ops-evidence-guide.md
```

Archivos locales relacionados:

- [source-index.md](source-index.md)
- [experiments.md](experiments.md)
- [implementation-patterns.md](implementation-patterns.md)
- [process-improvements.md](process-improvements.md)
- [monetization-ideas.md](monetization-ideas.md)
- [open-questions.md](open-questions.md)

Uso recomendado inmediato:

1. Enlazar esta guia desde [agent-workflows.md](agent-workflows.md).
2. Usarla en la proxima fuente YouTube/Reddit/docs.
3. Registrar si faltan campos en los templates existentes.
4. Crear un validator ligero para source packages si se repite el proceso.

## Siguiente Experimento

Procesar una fuente nueva de alto valor usando esta guia y medir:

- tiempo de captura;
- porcentaje de claims con evidence pointer;
- numero de decisiones o experimentos derivados;
- fallos de transcript/source capture;
- campos faltantes para RAG;
- si el source index permite reubicar todo sin chat history.
