# YouTube AI Researcher Plugin

Plugin publico para Codex que empaqueta la skill `youtube-ai-researcher`.

## Que hace

- Analiza videos, transcripciones, notas o canales de YouTube como fuentes trazables.
- Extrae tesis central, ideas clave, first principles, modelos mentales y casos practicos.
- Traduce aprendizajes en ideas de producto, apps, automatizaciones, agentes y workflows de IA.
- Identifica oportunidades de monetizacion como hipotesis y experimentos, no promesas.
- Detecta prompts, comandos o instrucciones que aparezcan en la transcripcion.
- Puede producir insumos para PRDs, planes tecnicos, backlogs y experimentos.

## Dependencia tecnica

Cuando el usuario comparta una URL sin transcripcion, usa la skill `youtube-transcript` si esta instalada en el entorno de Codex del usuario, normalmente bajo `${CODEX_HOME:-$HOME/.codex}/skills/skill-youtube-transcript`, para obtener la fuente.

No empaquetes ni dupliques esa skill dentro de este plugin. `youtube-ai-researcher` solo analiza; `youtube-transcript` extrae y normaliza la transcripcion.

## Distribucion publica

Este plugin esta preparado para publicarse o compartirse desde este repositorio. No depende de rutas privadas de una maquina especifica; si `youtube-transcript` no esta instalada, la skill debe pedir al usuario una transcripcion, notas o JSON estructurado antes de hacer claims especificos sobre el video.

## Memoria derivada por workspace

Si el workspace declara una memoria local, la skill debe guardar o proponer artefactos persistibles ahi ademas de responder en chat.

Para `ia-learning`, la convencion vive en:

```text
/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning/knowledge/
```

Destinos esperados:

- `knowledge/raw/youtube/` para JSON/transcripts originales o referencias fuente;
- `knowledge/processed/transcripts/` para transcripciones limpias;
- `knowledge/processed/summaries/` para reportes;
- `knowledge/processed/insights/` para hallazgos atomicos;
- `knowledge/projects/ia-learning/` para patrones, monetizacion, mejoras de proceso y novedades de IA aplicables.

No requiere base de datos para el MVP. Si no puede escribir archivos, debe entregar bloques Markdown/JSON listos para guardar.

## Fuera de alcance

- No genera guiones, posts, newsletters, anuncios ni piezas de contenido.
- No imita la voz exacta de creadores reales.
- No inventa prompts que no aparezcan en la fuente.
- No extrae transcripciones por cuenta propia; delega esa capa a `youtube-transcript` cuando sea necesario.
