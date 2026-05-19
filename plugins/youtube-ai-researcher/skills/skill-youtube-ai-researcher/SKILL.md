---
name: youtube-ai-researcher
description: Analiza videos, transcripciones, canales o patrones de YouTube para extraer aprendizajes, casos practicos, first principles, ideas de producto, workflows de IA, oportunidades de monetizacion, experimentos y prompts detectados con grounding en la fuente. Usala cuando el usuario quiera convertir contenido de YouTube en criterio, specs, ideas de apps o decisiones accionables. No la uses para generar guiones, posts, newsletters, anuncios ni piezas de contenido.
---

# YouTube AI Researcher

## Mision

Convertir fuentes de YouTube en criterio accionable para IA, apps, producto, automatizacion y monetizacion, manteniendo trazabilidad estricta hacia la transcripcion, notas o fuente proporcionada.

Esta skill analiza. No extrae captions por si misma como responsabilidad principal. Si el usuario da una URL y no hay transcripcion disponible en contexto, primero usa la skill `youtube-transcript` cuando este instalada en el entorno de Codex del usuario, normalmente bajo `${CODEX_HOME:-$HOME/.codex}/skills/skill-youtube-transcript`, para obtener la fuente estructurada, sin modificarla ni duplicarla dentro de este plugin.

## Regla central

Separa siempre:

- lo que aparece explicitamente en la fuente;
- inferencias razonables;
- recomendaciones del agente;
- informacion faltante.

Si un dato, prompt o claim no esta en la fuente, dilo claramente. No reconstruyas texto ausente.

## Entradas aceptadas

- URL de YouTube.
- JSON generado por `youtube-transcript`.
- Transcripcion completa.
- Segmentos con timestamps.
- Notas del usuario.
- Canal, playlist o tema.
- Objetivo de salida: aprendizaje, proyecto, monetizacion, prompts, PRD, plan o backlog.

## Flujo operativo

1. **Captura de fuente**
   - Si recibes JSON de transcript, usalo como fuente primaria.
   - Si recibes URL sin transcript, usa `youtube-transcript` cuando este disponible.
   - Si no puedes obtener transcripcion, pide transcript o notas antes de hacer claims especificos.
   - Registra URL, titulo, canal, idioma, fecha de extraccion y advertencias si existen.

2. **Mapa de contenido**
   - Extrae tesis central.
   - Lista claims principales.
   - Identifica first principles y modelos mentales.
   - Resume ejemplos, herramientas, APIs, librerias, companias o workflows mencionados.
   - Marca supuestos, limitaciones y puntos no cubiertos.

3. **Mapa de estructura explicativa**
   - Describe tono, ritmo, nivel tecnico, analogias y progresion conceptual.
   - Usa este mapa para entender la fuente, no para generar contenido nuevo.

4. **Mapa de aplicacion**
   - Traduce aprendizajes a ideas de producto, apps, automatizaciones, agentes, prompts, sistemas RAG o workflows de IA.
   - Para cada idea importante incluye: problema, oportunidad, forma tecnica probable, riesgo y experimento de validacion.

5. **Deteccion de prompts**
   - Busca comandos, prompts o instrucciones dictadas, pegadas o escritas que aparezcan en la transcripcion.
   - Senales utiles: "I ask the agent", "I'm going to say", "please", "can you", "copy this", "paste this", "prompt", `prompt.md`, `SKILL.md`.
   - Al final, incluye `Prompts detectados` con texto, timestamp, contexto, objetivo, adaptacion posible y advertencia si la transcripcion es auto-generada.
   - Si el prompt parece visual pero no esta en la transcripcion, indica que falta OCR/captura visual y no lo inventes.

6. **Monetizacion y experimentos**
   - Formula oportunidades como hipotesis.
   - Incluye audiencia, oferta, canal, pricing tentativo si la fuente lo permite y primer experimento.
   - No prometas ingresos ni validacion de mercado sin evidencia.

7. **Memoria derivada del workspace**
   - Si el workspace declara una memoria local, guarda o propone artefactos persistibles ahi ademas del reporte conversacional.
   - Para `ia-learning`, usa `/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning/knowledge/`.
   - Preserva raw transcript o JSON en `knowledge/raw/youtube/` cuando exista.
   - Guarda transcripciones limpias en `knowledge/processed/transcripts/`.
   - Guarda reportes en `knowledge/processed/summaries/`.
   - Guarda insights atomicos en `knowledge/processed/insights/`.
   - Enlaza patrones, monetizacion, mejoras de proceso y novedades relevantes en `knowledge/projects/ia-learning/`.
   - Incluye URL, video id, titulo, canal, idioma, fecha de consulta, confidence label y timestamps relevantes.
   - Si no puedes escribir archivos, entrega bloques Markdown/JSON listos para guardar.

## Salida por defecto

Usa esta estructura salvo que el usuario pida otra:

- Fuente
- Resumen ejecutivo
- Ideas clave
- First principles
- Estructura explicativa
- Casos practicos detectados
- Oportunidades para proyectos actuales o nuevos
- Ideas de workflow de IA
- Ideas de monetizacion
- Experimentos recomendados
- Prompts detectados
- Preguntas abiertas

## Formatos especiales

### Si el usuario pide aplicar a un proyecto

Entrega:

- oportunidad;
- usuario o problema;
- feature/app/workflow propuesto;
- forma tecnica probable;
- dependencia de datos o herramientas;
- riesgo;
- primer experimento.

### Si el usuario pide monetizacion

Entrega:

- insight fuente;
- audiencia;
- oferta;
- canal de adquisicion;
- hipotesis de precio;
- experimento de validacion;
- senales de que valdria la pena continuar.

### Si el usuario pide PRD, plan o tareas

Puedes generar insumos estructurados, pero marca cualquier supuesto que no venga de la fuente.

## Fuera de alcance

- No generes guiones, posts, newsletters, anuncios ni piezas de contenido.
- No imites la voz exacta de creadores reales.
- No presentes contenido como si hubiera sido escrito por otra persona.
- No descargues audio o video.
- No uses speech-to-text como fallback dentro de esta skill.
- No requieras base de datos, embeddings ni dashboard para guardar memoria derivada en el MVP.
- No tomes decisiones tecnicas finales sin PRD o plan cuando el cambio sea de implementacion.

## Checklist de calidad

- [ ] Inclui fuente y URL cuando existe.
- [ ] Separe hechos, inferencias y recomendaciones.
- [ ] No invente prompts ausentes.
- [ ] Inclui `Prompts detectados`, aunque sea para decir "no detectados".
- [ ] Escribi o propuse memoria derivada si el workspace la declara.
- [ ] No genere contenido fuera de alcance.
- [ ] Cerre con experimentos o preguntas utiles.
