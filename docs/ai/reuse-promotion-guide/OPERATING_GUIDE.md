# Reuse Promotion Operating Guide

Guia operativa para convertir ideas, procesos, fuentes, prompts y workflows en assets reutilizables con evidencia, validacion y bajo contexto.

## Proposito

Evitar que una idea se convierta demasiado pronto en plugin, automation o estructura pesada. La ruta recomendada es:

```txt
idea/proceso -> evidencia -> insight -> experimento -> doc/template -> skill -> plugin -> automation
```

La regla base es usar el asset mas pequeno que preserve valor y trazabilidad.

## Fuentes Internas

Esta guia consolida reglas ya presentes en el repo:

- `docs/ai/governance.md`: ciclo `raw signal -> processed knowledge -> project memory -> docs/templates -> skill -> plugin`.
- `knowledge/README.md`: contrato de memoria local y ciclo raw, processed, project links y briefs.
- `knowledge/projects/ia-learning/reuse-backlog.md`: registro de candidatos antes de promover assets.
- `knowledge/projects/ia-learning/research-ops-evidence-guide.md`: evidencia, confidence labels e insights atomicos.
- `knowledge/projects/ia-learning/spec-driven-development-guide.md`: specs verificables antes de construir ideas ambiguas.
- `knowledge/projects/ia-learning/implementation-patterns.md`: patron `manual run -> skill -> automation`.

## Principios

1. No saltar de una idea a un plugin salvo que el usuario pida explicitamente un paquete.
2. El chat coordina; los archivos guardan memoria durable.
3. Un summary no es evidencia primaria.
4. Separar hechos, inferencias, experimentos y preguntas abiertas.
5. Toda promocion debe tener input, output, done condition y validacion.
6. Automatizar solo despues de una corrida manual y una revision de calidad.
7. Preferir ampliar assets existentes antes de crear otros nuevos.

## Niveles De Promocion

| Nivel | Usar Cuando | Artefacto |
|---|---|---|
| Raw signal | la fuente o idea todavia no esta procesada | `knowledge/raw/` o enlace verificable |
| Processed knowledge | la fuente ya fue normalizada o resumida | `knowledge/processed/` |
| Project memory | el aprendizaje afecta este proyecto | `knowledge/projects/<project-id>/` |
| Docs/templates | el proceso sirve para otras sesiones o repos | `docs/`, `templates/` |
| Skill | Codex debe ejecutar el workflow repetidamente | `skills/<skill-name>/` |
| Plugin | la skill necesita scripts, herramientas, APIs o empaque | `plugins/<plugin-name>/` |
| Automation | el workflow ya fue validado y puede repetirse solo | automation configurada |

## Flujo Operativo

### 1. Capturar La Senal

Usa esto para una idea, proceso, video, comentario, issue, error repetido, prompt util o workflow manual.

```md
## Signal Intake

- Name:
- Source:
- Type: idea | process | video | bug | workflow | market signal
- Raw evidence:
- Why it matters:
- Confidence: verified | inferred | experimental | unverified
- Possible reuse:
- Next action:
```

Destino:

- raw source o payload: `knowledge/raw/<source>/`
- resumen o normalizacion: `knowledge/processed/summaries/`
- insight atomico: `knowledge/processed/insights/`
- impacto del proyecto: `knowledge/projects/<project-id>/`

### 2. Extraer Un Insight Atomico

Un insight debe poder entenderse sin releer toda la fuente.

```md
## <Insight Name>

- Source:
- Confidence:
- Claim:
- Evidence pointer:
- Why it matters:
- Applies to:
- Proposed action:
- Validation needed:
```

No promover todavia si el insight:

- es demasiado amplio;
- no tiene evidencia;
- mezcla varios temas;
- no propone patron, decision, experimento o pregunta.

### 3. Decidir Si Requiere Spec

Usa una spec cuando la idea toca producto, datos, UX, APIs, IA, negocio, arquitectura, varios agentes o cambios de alto riesgo.

Version compacta:

```md
Problem:
User:
Goal:
Non-goals:
Assumptions:
Acceptance criteria:
Validation:
Build decision:
```

No avanzar a implementacion si faltan criterios de aceptacion minimos.

### 4. Crear Un Experimento

Antes de crear una skill, plugin o automation, prueba que el workflow funciona.

```md
## <Experiment Name>

- Hypothesis:
- User/problem:
- Smallest test:
- Success signal:
- Failure signal:
- Evidence to capture:
- Status: planned | running | done | dropped
```

Buenos smallest tests:

- ejecutar el workflow manualmente una vez;
- aplicarlo a dos o tres fuentes;
- producir un reporte real;
- validar con un usuario;
- medir si reduce retrabajo;
- comparar contra el proceso manual.

### 5. Registrar En Reuse Backlog

Antes de crear un asset amplio, registra el candidato.

```md
## <Candidate Name>

- Status: idea | validating | ready | promoted | dropped
- Source:
- Current artifact:
- Proposed asset: docs | template | skill | plugin
- Reuse case:
- Expected users:
- Inputs:
- Outputs:
- Validation needed:
- Token budget impact:
- Decision:
```

Decision:

- `idea`: todavia falta evidencia o forma.
- `validating`: existe un experimento en curso.
- `ready`: paso validacion y puede promoverse.
- `promoted`: ya existe el asset.
- `dropped`: no demostro valor o duplica algo existente.

### 6. Promover A Docs O Templates

Promueve a `docs/` o `templates/` si:

- el proceso ya funciono al menos una vez;
- otra sesion o proyecto podria repetirlo;
- no necesita scripts ni integraciones;
- puede explicarse como checklist, runbook, spec o plantilla.

Ejemplos:

```txt
knowledge/processed/insights/source-to-experiment.md
-> docs/research/source-to-experiment-guide.md
```

```txt
knowledge/projects/<project-id>/process-improvements.md
-> templates/project-ai-starter/docs/workflow-checklist.md
```

### 7. Promover A Skill

Crea una skill cuando Codex deba ejecutar el workflow repetidamente.

Criterios:

- inputs claros;
- outputs claros;
- pasos repetibles;
- guardrails;
- validacion;
- bajo costo de contexto;
- al menos una corrida manual validada.

Estructura recomendada:

```md
# SKILL.md

## Mision

## Cuando usarla

## Inputs

## Workflow

## Outputs

## Guardrails

## Validation

## Memory
```

Una skill ensena comportamiento. No debe existir solo porque una idea parece interesante.

### 8. Promover A Plugin

Crea un plugin si la skill necesita empaque adicional:

- scripts;
- varias skills;
- MCP o tools;
- APIs externas;
- assets;
- setup;
- integraciones;
- distribucion formal.

Regla practica:

```txt
Una skill ensena comportamiento.
Un plugin empaqueta capacidades.
```

Antes de crear plugin:

- validar la skill manualmente;
- revisar seguridad y secretos;
- confirmar que no existe plugin oficial suficiente;
- definir instalacion, versionado y QA.

### 9. Automatizar Al Final

No automatizar outputs que no han sido revisados.

Checklist:

```md
- Manual run completed:
- Output reviewed:
- Failure cases known:
- Logs captured:
- Secrets handled:
- Rollback/disable path:
- Human review needed:
- Cadence:
```

## Arbol De Decision

```txt
Es solo una idea o fuente?
-> knowledge/

Ya produjo un aprendizaje reusable?
-> processed/insights + project memory

Se puede probar?
-> experiments.md

Sirve como proceso para otras sesiones?
-> docs/ o templates/

Codex debe ejecutarlo repetidamente?
-> skills/

Necesita scripts, herramientas, APIs o empaque distribuible?
-> plugins/

Ya fue probado manualmente y tiene QA?
-> automation
```

## Criterios De Aceptacion

Una promocion esta lista cuando:

- el destino del asset esta justificado;
- la evidencia o los supuestos estan marcados;
- el reuse backlog tiene el candidato o la promocion registrada;
- hay validacion manual para skill, plugin o automation;
- el asset tiene instrucciones de uso;
- el asset no duplica algo existente;
- el impacto de contexto para Codex es razonable.

## Antipatrones

- Crear un plugin porque el nombre suena reutilizable.
- Guardar solo resumenes sin raw evidence o fuente verificable.
- Mezclar hechos de una fuente con recomendaciones propias.
- Automatizar antes de revisar manualmente el output.
- Crear una skill para una unica tarea puntual.
- Ignorar `reuse-backlog.md`.
- Copiar todo el conocimiento del repo destino al prompt en vez de usar indices.

## Ejemplo Completo

Caso: aparece en varios videos un workflow util para analizar comentarios de YouTube.

1. Guardar metadata, transcript o failure evidence en `knowledge/raw/youtube/`.
2. Crear resumen normalizado en `knowledge/processed/summaries/`.
3. Extraer insight: "comentarios recientes pueden revelar objeciones, preguntas repetidas y oportunidades de producto".
4. Registrar experimento: analizar 100 comentarios y producir cinco acciones trazables.
5. Si funciona, documentar runbook en `docs/research/youtube-comment-intelligence.md`.
6. Si se repite, crear `skills/skill-youtube-comment-intelligence/`.
7. Si necesita API, scripts y empaquetado, crear `plugins/youtube-comment-intelligence/`.
8. Si pasa QA manual, programar automation recurrente.

## Como Pedirle A Codex Que Use Esta Guia

```md
Usa `docs/ai/reuse-promotion-guide/OPERATING_GUIDE.md` para clasificar esta idea:

Idea:
<describe la idea, proceso o fuente>

Quiero que respondas con:
- destino recomendado: knowledge | docs/template | skill | plugin | automation
- evidencia existente y evidencia faltante
- smallest test
- entrada para reuse-backlog.md
- criterios de aceptacion
- riesgos y decisiones abiertas

No crees skill, plugin ni automation todavia.
```
