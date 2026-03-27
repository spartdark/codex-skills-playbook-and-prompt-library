---
name: rag-research
description: Skill para diseñar y ejecutar investigación RAG con grounding, evaluación de fuentes, citas verificables y menor riesgo de alucinación.
---

# RAG Research

## Misión

Convertir necesidades de investigación o diseño RAG en un plan operativo con fuentes confiables, estrategia de recuperación y respuesta anclada a evidencia.

## Cuándo usarla

Usa esta skill cuando el usuario necesite:

- diseñar un pipeline RAG;
- elegir chunking, retrieval o reranking;
- reducir alucinación con grounding;
- comparar fuentes públicas y privadas;
- definir evaluación y citas verificables.

## Flujo de trabajo

1. Aclara el caso de uso y el tipo de fuente.
2. Distingue conocimiento estable de información cambiante.
3. Selecciona corpus, estrategia de chunking y recuperación.
4. Define cómo se citarán y validarán las respuestas.
5. Propón métricas y pruebas de calidad.

## Guardrails

- Prioriza fuentes primarias y trazables.
- Separa inferencias de hechos confirmados.
- No presentes una arquitectura RAG sin plan de evaluación.
- Evita depender de un único mecanismo de recuperación si el caso requiere robustez.

## Referencias internas

- `prompt.md` para principios de grounding.
- `examples/example-1.md` para un caso de diseño.
- `assets/source-evaluation-checklist.md` para revisión rápida de fuentes.
