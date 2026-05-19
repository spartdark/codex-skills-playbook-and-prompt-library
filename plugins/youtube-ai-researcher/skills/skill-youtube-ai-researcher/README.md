# YouTube AI Researcher

Skill para convertir videos, transcripciones o notas de YouTube en aprendizajes, ideas de producto, workflows de IA, oportunidades de monetizacion, experimentos y prompts detectados.

Usa la skill `youtube-transcript` si esta instalada en el entorno de Codex del usuario, normalmente bajo `${CODEX_HOME:-$HOME/.codex}/skills/skill-youtube-transcript`, como fuente tecnica cuando solo exista una URL y se necesite obtener la transcripcion. No dupliques esa skill dentro de este plugin.

## Ejemplo de activacion

```text
Usa youtube-ai-researcher para analizar esta transcripcion.
Detecta prompts, ideas de producto, oportunidades de monetizacion y experimentos.
```

## Guardrail principal

No genera guiones ni piezas de contenido. Analiza fuentes y produce criterio accionable.

## Memoria derivada

Cuando el workspace declare una memoria local, la skill debe guardar o proponer artefactos persistibles ademas del reporte conversacional.

Para `ia-learning`, usa:

```text
/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning/knowledge/
```

Usa esa memoria para conservar raw transcripts, resumenes, prompts detectados, insights, ideas de monetizacion, patrones de implementacion y mejoras de proceso con trazabilidad a la fuente.
