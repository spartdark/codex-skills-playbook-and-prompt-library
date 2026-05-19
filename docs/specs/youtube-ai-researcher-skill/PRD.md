---
title: "PRD: YouTube AI Researcher"
status: "draft"
owner: "VSM / Codex"
created: "2026-05-18"
related:
  - "../youtube-transcript-plugin/PRD.md"
---

# PRD: YouTube AI Researcher

## 1. Resumen

Crear una skill para Codex llamada `youtube-ai-researcher` que convierta videos, transcripciones, canales o patrones de creadores de YouTube en conocimiento accionable para procesos de IA, desarrollo de apps, estrategia de producto y monetizacion. La skill tambien debe detectar prompts, instrucciones o comandos que el creador dicte o escriba cuando esten presentes en la transcripcion o fuente disponible.

La skill no extrae transcripciones por si misma como responsabilidad principal. Su trabajo es usar fuentes disponibles, idealmente provistas por el plugin `Transcripcion de YouTube`, para analizar, sintetizar y aplicar ideas con trazabilidad. Su proposito central es ayudar al usuario a mantenerse al dia con casos practicos, detectar oportunidades, monetizar aprendizajes y generar nuevas ideas de proyectos.

## 2. Problema

Los videos de YouTube contienen ideas valiosas sobre IA, programacion, producto, negocios y monetizacion, pero suelen quedar como consumo pasivo. El usuario necesita convertir ese material en:

- aprendizajes claros;
- principios fundamentales;
- ideas para cualquier tipo de proyecto;
- mejoras para procesos de IA;
- casos practicos recientes y aplicables;
- prompts, instrucciones o comandos reutilizables que aparezcan en la fuente;
- oportunidades de monetizacion;
- planes o specs que puedan alimentar trabajo posterior de Codex.

Sin una skill especializada, el analisis puede volverse generico, perder grounding en la fuente o no traducir los aprendizajes a acciones concretas.

## 3. Objetivo

Definir una skill que permita analizar contenido de YouTube con estructura repetible, citas de fuente y orientacion practica hacia cualquier tipo de proyecto: apps, automatizaciones, productos digitales, servicios, negocios, herramientas internas o experimentos de IA.

La skill debe ayudar al usuario a pasar de "vi este video interesante" a "estas son las ideas, principios, casos practicos, riesgos, oportunidades de monetizacion y proximos experimentos que puedo usar".

Tambien debe ayudar a pasar de "el creador escribio o dicto un prompt util" a "este es el prompt detectado, este es el contexto en que lo uso y esta es la forma responsable de reutilizarlo o adaptarlo".

## 4. Usuarios

### Usuario principal

Fundador, builder, creador o desarrollador que usa Codex para construir productos y quiere convertir videos de YouTube en ventaja practica.

### Usuarios secundarios

- Agentes de Codex que necesitan un flujo claro para analizar transcripciones.
- Equipos pequenos que convierten investigacion en PRDs, planes tecnicos, backlogs o experimentos.
- Builders que estudian patrones de explicacion para entender mejor una fuente, no para generar contenido.

## 5. Relacion con el plugin Transcripcion de YouTube

El sistema ideal tiene dos capas:

### Plugin: Transcripcion de YouTube

Responsabilidad:

- obtener transcripciones;
- normalizar segmentos y timestamps;
- entregar metadatos;
- reportar errores de fuente.

### Skill: YouTube AI Researcher

Responsabilidad:

- analizar contenido;
- extraer first principles;
- identificar patrones de explicacion y estructura;
- traducir ideas a productos, apps, agentes, automatizaciones o monetizacion;
- generar salidas utiles basadas en la fuente.

La skill debe poder funcionar tambien con transcripciones pegadas manualmente por el usuario, pero debe preferir una fuente estructurada cuando exista.

## 6. Casos de uso iniciales

### UC1: Aprender de un video

El usuario proporciona una URL o transcripcion y pide entender el contenido. La skill entrega resumen, ideas clave, principios, ejemplos y una explicacion clara.

### UC2: Aplicar un video a cualquier proyecto

El usuario proporciona contenido relacionado con IA, producto, desarrollo, negocio o automatizacion. La skill traduce el material en oportunidades para proyectos existentes o nuevos: features, arquitectura, UX, prompts, agentes, automatizaciones, flujos de usuario, servicios, productos digitales o experimentos.

### UC3: Generar ideas de monetizacion

El usuario analiza contenido de builders, creadores o expertos. La skill identifica posibles ofertas, productos digitales, servicios, audiencias, canales de distribucion y experimentos de validacion.

### UC3b: Mantenerse al dia con casos practicos

El usuario analiza videos recientes o canales relevantes. La skill extrae que esta funcionando, que patrones emergen, que herramientas nuevas aparecen y como podria aplicarse a proyectos actuales o futuros.

### UC3c: Detectar prompts e instrucciones utiles

El usuario analiza un video donde el creador dicta, pega o escribe instrucciones para un agente de IA. La skill identifica esos prompts o comandos, los agrupa al final del analisis y explica para que sirven, con timestamps cuando existan.

### UC4: Analizar estructura explicativa

El usuario quiere entender como un video presenta ideas complejas. La skill identifica estructura, tono, nivel tecnico, ritmo, analogias, ejemplos y progresion conceptual para mejorar la comprension del material.

### UC6: Convertir investigacion en specs

El usuario quiere transformar aprendizajes de videos en PRDs, planes tecnicos, tareas o experimentos de producto.

## 7. Alcance MVP

La primera version de la skill debe:

- aceptar URL, transcripcion, notas o salida estructurada del plugin de transcripcion;
- distinguir hechos presentes en la fuente de inferencias del agente;
- citar siempre la fuente cuando haya URL;
- extraer tesis central, ideas clave, first principles y modelos mentales;
- identificar patrones de explicacion y estructura conceptual;
- detectar prompts, instrucciones o comandos presentes en la fuente;
- generar aplicaciones concretas para IA, apps y producto;
- generar ideas de monetizacion y experimentos simples;
- indicar claramente cuando falta informacion o la fuente no contiene un dato.

## 8. Fuera de alcance para MVP

- Extraer transcripciones automaticamente como responsabilidad interna.
- Descargar audio o video.
- Monitorear canales.
- Guardar resultados en base de datos.
- Crear dashboards.
- Imitar de forma exacta la voz de una persona real.
- Producir deepfakes textuales o contenido que haga creer que fue escrito por el creador original.
- Generar guiones, posts, newsletters, anuncios o piezas de contenido.
- Tomar decisiones de implementacion tecnica sin PRD o plan posterior.

## 9. Modos de trabajo

### Modo 1: Aprendizaje

Objetivo: convertir un video en entendimiento claro.

Salida esperada:

- resumen ejecutivo;
- conceptos clave;
- first principles;
- ejemplos;
- analogias;
- puntos confusos o no cubiertos;
- preguntas para estudiar despues.

### Modo 2: Aplicacion a proyectos

Objetivo: convertir el video en oportunidades concretas para cualquier proyecto actual o futuro.

Salida esperada:

- ideas de proyectos, features o servicios;
- mejoras de UX;
- oportunidades de automatizacion;
- agentes o workflows de IA;
- prompts o sistemas RAG potenciales;
- prompts detectados en la fuente y posibles adaptaciones;
- casos practicos replicables;
- riesgos y dependencias;
- siguiente experimento recomendado.

### Modo 3: Casos practicos y monetizacion

Objetivo: convertir el video en casos practicos, ofertas, oportunidades de negocio y experimentos de monetizacion.

Salida esperada:

- casos practicos detectados;
- oferta potencial;
- audiencia;
- hipotesis de precio;
- canal de adquisicion;
- experimento de validacion.

## 10. Requisitos funcionales

### RF1: Captura de fuente

La skill debe aceptar una o mas de estas entradas:

- URL de YouTube;
- transcripcion completa;
- segmentos con timestamps;
- notas del usuario;
- canal, playlist o tema;
- objetivo de salida.

Si la transcripcion no esta disponible, la skill debe usar herramientas existentes si estan disponibles o pedir la fuente al usuario.

### RF2: Grounding

La skill debe separar:

- datos presentes en la fuente;
- inferencias razonables;
- recomendaciones del agente;
- informacion faltante.

### RF3: Mapa de contenido

La skill debe extraer:

- tesis central;
- claims principales;
- first principles;
- modelos mentales;
- ejemplos;
- herramientas, APIs, librerias o companias mencionadas;
- supuestos;
- limitaciones.

### RF4: Mapa de estilo

La skill debe identificar:

- tono;
- estructura de explicacion;
- ritmo general;
- uso de analogias;
- nivel tecnico;
- audiencia implicita.

### RF5: Mapa de aplicacion

La skill debe traducir los aprendizajes a:

- mejoras de procesos de IA;
- ideas de app;
- oportunidades de producto;
- automatizaciones;
- agentes;
- casos practicos recientes;
- nuevas ideas de proyecto;
- ideas de monetizacion;
- experimentos de validacion.

### RF6: Deteccion de prompts e instrucciones

La skill debe buscar prompts, comandos, instrucciones para agentes o texto operativo que el creador dicte, pegue o escriba durante el video, siempre que aparezcan en la transcripcion o fuente disponible.

Debe detectar senales como:

- "I ask the agent...";
- "I'm going to say...";
- "please...";
- "can you...";
- "copy this...";
- "paste this...";
- "prompt";
- nombres de archivos como `prompt.md`, `SKILL.md` o configuraciones similares;
- instrucciones imperativas dirigidas a un agente o herramienta.

Cuando detecte prompts, la skill debe devolverlos en una seccion final llamada `Prompts detectados` con:

- texto del prompt o reconstruccion minima basada solo en la transcripcion;
- timestamp o segmento de origen, si existe;
- contexto de uso;
- objetivo del prompt;
- posible adaptacion para proyectos del usuario;
- advertencia si la transcripcion es auto-generada o incompleta.

La skill no debe inventar prompts que no aparezcan en la fuente. Si un prompt parece estar escrito visualmente en pantalla pero la transcripcion no lo contiene, debe indicarlo como limitacion y sugerir una fase futura con OCR o captura visual.

### RF7: No generacion de contenido

Cuando el usuario pida guiones, posts, newsletters, anuncios u otras piezas de contenido, la skill debe aclarar que ese trabajo esta fuera de alcance. Puede ofrecer, en cambio, analisis de la fuente, ideas de producto, oportunidades de monetizacion o experimentos de validacion.

### RF8: Salida por defecto

Si el usuario no especifica formato, la skill debe usar esta estructura:

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

### RF9: Compatibilidad con specs

Cuando el usuario pida aterrizar una idea, la skill debe poder producir insumos para:

- PRD;
- `plan.md`;
- `tasks.md`;
- backlog;
- experimento de validacion.

## 11. Requisitos no funcionales

### Trazabilidad

Cada analisis debe incluir la fuente y, cuando existan, timestamps o segmentos relevantes.

### Concision

La skill debe evitar resumenes inflados. Debe priorizar ideas accionables y evidencia.

### Seguridad de estilo

La skill no debe imitar exactamente a creadores vivos ni presentar contenido como si fuera escrito por ellos.

### Veracidad

La skill debe decir "la fuente no lo especifica" cuando el dato no aparezca.

### Flexibilidad

La skill debe servir tanto para videos tecnicos como estrategicos, de producto, negocio o IA.

## 12. Criterios de aceptacion

### CA1: Analisis con transcripcion

GIVEN una transcripcion de YouTube y una URL fuente  
WHEN el usuario pide analizar el video  
THEN la skill devuelve resumen, ideas clave, first principles, estructura explicativa y oportunidades accionables citando la fuente.

### CA2: Dato no presente

GIVEN una pregunta sobre un dato que no aparece en la transcripcion  
WHEN la skill responde  
THEN indica que la fuente no contiene ese dato y evita inventarlo.

### CA3: Aplicacion a proyecto

GIVEN un video sobre IA, producto o desarrollo  
WHEN el usuario pide aplicarlo a un proyecto actual o a nuevas ideas de proyecto  
THEN la skill produce oportunidades concretas, razonamiento, riesgo y experimento de validacion.

### CA4: Monetizacion

GIVEN un video con ideas de negocio, producto o IA  
WHEN el usuario pide monetizacion  
THEN la skill propone ofertas, audiencia, canal, hipotesis de precio y primer experimento.

### CA5: Prompts detectados

GIVEN una transcripcion donde el creador dicta o escribe instrucciones para un agente  
WHEN el usuario pide analizar el video  
THEN la skill incluye al final una seccion `Prompts detectados` con texto, timestamp, contexto, objetivo y posible adaptacion.

### CA6: Prompt ausente o incompleto

GIVEN un video donde parece haber un prompt visual pero la transcripcion no contiene el texto completo  
WHEN la skill analiza la fuente  
THEN indica que el prompt no esta disponible en la transcripcion y evita reconstruirlo sin evidencia.

### CA7: Solicitud de contenido fuera de alcance

GIVEN una fuente de YouTube  
WHEN el usuario pide generar guiones, posts, newsletters, anuncios u otras piezas de contenido  
THEN la skill aclara que la generacion de contenido esta fuera de alcance y ofrece analisis, oportunidades, monetizacion o experimentos como alternativa.

### CA8: Estructura explicativa

GIVEN una fuente con explicaciones utiles  
WHEN el usuario pide entender como esta organizado el video  
THEN la skill describe la estructura conceptual, ejemplos, analogias y progresion de ideas sin producir contenido nuevo.

### CA9: Falta de transcripcion

GIVEN solo una URL y sin plugin de transcripcion disponible  
WHEN la skill no pueda obtener la fuente  
THEN pide la transcripcion o notas al usuario antes de hacer afirmaciones especificas.

## 13. Borrador de skill propuesto

```markdown
---
name: youtube-ai-researcher
description: Use when analyzing YouTube videos, transcripts, channels, or creator patterns to extract practical AI cases, detected prompts, agent instructions, project ideas, product insights, monetization opportunities, experiments, and source-grounded summaries for current or future projects. Do not use for generating scripts, posts, newsletters, ads, or other content pieces.
---

# YouTube AI Researcher

## Purpose

Turn YouTube videos into source-grounded insight for AI workflows, app development, product strategy, project ideas, practical cases, detected prompts, agent instructions, and monetization.

## Core Rule

Always ground claims in the provided video, transcript, notes, or linked source. If a detail is not present, say so clearly.

Do not copy long transcript passages. Use paraphrase, concise quotes only when useful, and always cite the video URL.

Do not generate scripts, posts, newsletters, ads, or other content pieces. Do not imitate a living creator's exact voice. When useful, describe general explanation patterns such as teaching style, example order, or level of technical depth.

When a transcript contains prompts or agent instructions, extract them into a final `Detected Prompts` section with timestamp, context, purpose, and possible adaptation. Do not invent prompt text that is not present in the source.

## Workflow

1. Source Capture
2. Content Map
3. Style Map
4. Application Map
5. Output Mode
```

## 14. Riesgos

- La skill puede generar recomendaciones demasiado genericas si la fuente no es buena.
- El usuario puede esperar extraccion automatica de YouTube aunque eso pertenezca al plugin.
- La solicitud de guiones o contenido puede desviar la skill de su objetivo de investigacion.
- Videos largos pueden exceder contexto y requerir chunking.
- El analisis de monetizacion puede sonar concluyente sin validacion real de mercado.

## 15. Mitigaciones

- Separar claramente plugin y skill.
- Requerir fuente o transcripcion antes de claims especificos.
- Etiquetar inferencias y recomendaciones.
- Usar chunks o secciones cuando el contenido sea largo.
- En monetizacion, formular hipotesis y experimentos, no promesas.
- Mantener reglas explicitas contra generacion de contenido y contra imitacion exacta de personas reales.

## 16. Metricas de exito

- Numero de videos convertidos en aprendizajes accionables.
- Numero de ideas de proyecto generadas y evaluadas.
- Numero de casos practicos recientes detectados.
- Numero de experimentos de monetizacion propuestos.
- Porcentaje de analisis con fuente citada.
- Porcentaje de recomendaciones conectadas a proyectos actuales o futuros.
- Reduccion de analisis genericos o no trazables.

## 17. Fases futuras

### Fase 2: Skill instalada

- Crear carpeta real de skill.
- Escribir `SKILL.md` final.
- Agregar metadata para UI si aplica.
- Validar con ejemplos reales.

### Fase 3: Integracion con plugin de transcripcion

- Usar salida estructurada del plugin `Transcripcion de YouTube`.
- Citar timestamps en respuestas.
- Manejar videos largos por segmentos.

### Fase 4: Biblioteca de insights

- Guardar analisis por proyecto, canal, tema y oportunidad.
- Reusar aprendizajes en PRDs y planes tecnicos.

### Fase 5: Research OS para IA y producto

- Comparar videos entre creadores.
- Detectar tendencias.
- Generar mapas de oportunidad.
- Convertir investigacion en backlog priorizado.

## 18. Decisiones abiertas

- Nombre final visible de la skill.
- Si la skill vivira en `$CODEX_HOME/skills` o dentro de este repo.
- Nivel de detalle del `SKILL.md` final.
- Si se incluiran referencias adicionales con plantillas de salida.
- Si se creara una skill separada para monetizacion o se mantendra como modo interno.
- Como se conectara con specs de proyectos actuales o futuros.

## 19. Principio rector

La skill no debe resumir videos por resumir. Debe convertir fuentes de YouTube en criterio, experimentos y decisiones utiles para construir.
