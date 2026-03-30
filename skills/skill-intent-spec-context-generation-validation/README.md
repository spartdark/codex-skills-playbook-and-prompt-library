# ISCGV++ Product Operating System

Skill publica para transformar ideas ambiguas en especificaciones AI-first auditables y validables antes de invertir en construccion.

## Que cubre

- arquitectura multi-agente por fases;
- intent engineering y JTBD;
- PRD estructurado con trazabilidad;
- contexto, memoria y estrategia RAG;
- guardrails y control de generacion;
- validacion de producto con experimentos y metricas;
- arquitectura AI-first con riesgos tecnicos y de seguridad;
- auditoria obligatoria por fase;
- scoring para bloquear o permitir avance.

## Casos de uso

- "Convierte esta idea de AI product en un PRD serio".
- "Quiero validar si esta solucion con LLM vale la pena antes de construir".
- "Necesito definir contexto, RAG y evals para este sistema".
- "Quiero un proceso duro que bloquee fases flojas y me fuerce a iterar".

## Instalacion

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-intent-spec-context-generation-validation "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contenido

- `SKILL.md`: agentes, gates, scoring y guardrails.
- `prompt.md`: tono y disciplina operativa.
- `skill.json`: metadata instalable.
- `examples/`: ejemplo de solicitud compatible.
- `assets/`: checklist de revision.
