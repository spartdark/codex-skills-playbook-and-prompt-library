# RAG Research

Skill pública para equipos que necesitan diseñar, evaluar o refinar flujos de Retrieval-Augmented Generation con evidencia verificable.

## Qué cubre

- análisis del caso de uso;
- selección de fuentes;
- chunking y retrieval;
- grounding y citas;
- plan de evaluación;
- reducción de alucinación y huecos de cobertura.

## Casos de uso

- "Diseña un RAG para documentos privados y notas de producto".
- "¿Cómo cito mejor mis respuestas y detecto huecos del corpus?"
- "Compara BM25, embeddings y reranking para este caso".

## Instalación

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-rag-research "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Contenido

- `SKILL.md`: flujo y guardrails.
- `prompt.md`: enfoque de diseño.
- `skill.json`: metadata instalable.
- `examples/`: ejemplo práctico.
- `assets/`: checklist de calidad de fuentes.
