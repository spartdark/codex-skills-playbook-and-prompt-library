---
title: "PRD: Reddit AI Researcher"
status: "draft"
owner: "VSM / Codex"
created: "2026-05-19"
related:
  - "../youtube-ai-researcher-skill/PRD.md"
  - "../youtube-transcript-plugin/PRD.md"
---

# PRD: Reddit AI Researcher

## 1. Resumen

Crear un plugin/skill para Codex llamado `reddit-ai-researcher` que convierta posts, comentarios, subreddits, busquedas y discusiones de Reddit en senales accionables para IA, desarrollo de software, producto, automatizacion, monetizacion y mejora de procesos.

El plugin no debe tratar Reddit como fuente de verdad definitiva. Debe tratarlo como una fuente de senales: dolores reales, preguntas repetidas, objeciones, herramientas emergentes, workflows que la gente esta probando, quejas de developers, casos de uso y oportunidades tempranas.

El proposito central es ayudar al usuario a mantenerse actualizado en IA y software, detectar ideas practicas, mejorar sus procesos de desarrollo y descubrir oportunidades de producto o monetizacion sin inflar tendencias ni inventar validacion de mercado.

## 2. Problema

Reddit contiene conversaciones utiles para builders y desarrolladores, pero el valor suele estar disperso entre posts, comentarios, opiniones contradictorias, ruido, memes, sesgos de comunidad y contexto incompleto.

El usuario necesita convertir esa informacion en:

- senales tempranas sobre IA y desarrollo de software;
- problemas repetidos que valga la pena resolver;
- casos de uso practicos que otros usuarios estan probando;
- objeciones, frustraciones y limites de herramientas actuales;
- ideas para apps, agentes, automatizaciones, devtools o servicios;
- oportunidades de monetizacion formuladas como hipotesis;
- experimentos pequenos para validar si una idea merece mas trabajo;
- insumos para PRDs, planes tecnicos, backlogs o procesos personales.

Sin una skill especializada, el analisis de Reddit puede quedarse en resumen generico, confundir popularidad con verdad o convertir opiniones aisladas en conclusiones demasiado fuertes.

## 3. Objetivo

Definir un plugin/skill que permita analizar contenido de Reddit con estructura repetible, grounding en fuentes, evaluacion de senales y orientacion practica hacia desarrollo de software, IA, producto y monetizacion.

La skill debe ayudar al usuario a pasar de "vi varios threads interesantes" a "estas son las senales, problemas, oportunidades, riesgos y experimentos que puedo usar".

Tambien debe ayudar a pasar de "la gente habla de esta herramienta o problema" a "este es el patron observado, esta es la evidencia disponible, esta es la oportunidad probable y este es el experimento minimo para validarla".

## 4. Usuarios

### Usuario principal

Desarrollador, builder, founder o creador tecnico que usa Codex para descubrir ideas, mantenerse actualizado en IA y software, mejorar su workflow y encontrar oportunidades de producto o monetizacion.

### Usuarios secundarios

- Agentes de Codex que necesitan convertir discusiones abiertas en insumos accionables.
- Equipos pequenos que investigan dolores de usuarios antes de construir.
- Builders que quieren detectar patrones emergentes en comunidades tecnicas.
- Personas que quieren mejorar procesos internos usando IA, automatizacion o devtools.

## 5. Relacion con un Research OS multi-fuente

`reddit-ai-researcher` debe funcionar como una fuente dentro de un sistema mayor de investigacion:

### YouTube AI Researcher

Responsabilidad:

- extraer workflows largos;
- entender demos y explicaciones;
- detectar prompts o instrucciones mostradas en videos;
- convertir contenido educativo en ideas aplicables.

### Reddit AI Researcher

Responsabilidad:

- detectar dolores reales y repetidos;
- capturar objeciones, dudas y lenguaje de usuarios;
- identificar herramientas y patrones emergentes;
- encontrar oportunidades a partir de problemas discutidos por comunidades.

### Opportunity Synthesizer futuro

Responsabilidad:

- cruzar senales de Reddit, YouTube, GitHub, Hacker News, docs y notas propias;
- priorizar ideas;
- convertir senales en PRDs, experimentos y decisiones.

La regla comun debe ser:

```text
Fuente -> Senal -> Problema -> Usuario -> Oportunidad -> Experimento -> Decision
```

### Memoria derivada por workspace

Cuando `reddit-ai-researcher` se use dentro de un workspace que declare memoria local, la skill debe escribir o proponer artefactos derivados en la ubicacion indicada por ese workspace.

Para el workspace `ia-learning`, la convencion inicial es:

```text
/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning/knowledge/
```

Contrato minimo:

- preservar raw exports, permalinks o referencias fuente en `knowledge/raw/reddit/`;
- normalizar threads o discusiones en `knowledge/processed/threads/`;
- guardar reportes o resumenes en `knowledge/processed/summaries/`;
- extraer insights atomicos en `knowledge/processed/insights/`;
- enlazar hallazgos aplicables a `knowledge/projects/ia-learning/`;
- registrar URL/permalink, subreddit, titulo, fecha de consulta, confidence label y evidencia puntual.

Esta memoria derivada no reemplaza la respuesta conversacional ni convierte Reddit en fuente definitiva. Es una capa local de trazabilidad y aprendizaje para reutilizar senales entre analisis, proyectos y futuros workspaces.

## 6. Casos de uso iniciales

### UC1: Mantenerse actualizado en IA y desarrollo de software

El usuario proporciona posts, subreddits, busquedas o threads sobre IA, agentes, modelos, tooling, devtools o frameworks. La skill extrae senales recientes, herramientas mencionadas, casos de uso y riesgos.

### UC2: Detectar dolores y problemas repetidos

El usuario analiza uno o varios threads. La skill identifica problemas recurrentes, lenguaje del usuario, contexto, severidad, frecuencia estimada y si el problema parece suficientemente concreto para explorar.

### UC3: Generar ideas de producto o software

La skill traduce senales de Reddit en ideas de apps, agentes, extensiones, CLIs, SaaS, automatizaciones, templates, plugins, cursos, servicios o herramientas internas.

### UC4: Mejorar procesos personales o de desarrollo

La skill detecta practicas, flujos o herramientas mencionadas y las convierte en mejoras para coding, testing, code review, documentacion, debugging, CI/CD, investigacion, aprendizaje o productividad.

### UC5: Identificar oportunidades de monetizacion

La skill formula oportunidades como hipotesis: audiencia, problema, oferta, canal, precio tentativo si hay evidencia, primer experimento y senales de continuacion.

### UC6: Evaluar herramientas, frameworks o tendencias

La skill resume percepciones de usuarios sobre una herramienta o tendencia, separando entusiasmo, objeciones, problemas concretos, casos de uso reales y dudas abiertas.

### UC7: Convertir investigacion en specs

El usuario pide aterrizar una oportunidad. La skill produce insumos para PRD, `plan.md`, `tasks.md`, backlog o experimento de validacion, marcando supuestos.

## 7. Alcance MVP

La primera version debe:

- aceptar URLs de Reddit, texto pegado, exports, JSON, listas de posts, comentarios o notas del usuario;
- registrar fuente, subreddit, titulo, fecha, score, numero de comentarios y links cuando esten disponibles;
- separar hechos observados, inferencias, recomendaciones y datos faltantes;
- detectar problemas repetidos y objeciones;
- extraer herramientas, tecnologias, empresas, APIs, frameworks o workflows mencionados;
- clasificar senales por dominio: IA, desarrollo de software, producto, monetizacion, procesos, automatizacion u otro;
- convertir senales en oportunidades accionables;
- proponer experimentos pequenos y verificables;
- evitar presentar popularidad, upvotes o comentarios aislados como validacion definitiva;
- entregar preguntas abiertas y fuentes que faltan para validar mejor.

## 8. Fuera de alcance para MVP

- Scraping no autorizado o bypass de restricciones.
- Automatizar login, cookies o acceso privado.
- Monitoreo continuo de subreddits.
- Guardar resultados en base de datos externa como requisito del MVP.
- Crear dashboards.
- Predecir tendencias como certeza.
- Presentar opiniones de Reddit como evidencia cientifica o de mercado definitiva.
- Generar spam, astroturfing, respuestas manipulativas o contenido para influir comunidades.
- Doxxing, perfilado individual o analisis de usuarios privados.
- Tomar decisiones tecnicas finales sin PRD, plan o validacion posterior.

## 9. Modos de trabajo

### Modo 1: Trend Scan

Objetivo: entender que temas, herramientas o problemas estan apareciendo.

Salida esperada:

- temas dominantes;
- herramientas mencionadas;
- patrones emergentes;
- senales debiles;
- ruido o sesgos de comunidad;
- preguntas para investigar despues.

### Modo 2: Pain Mining

Objetivo: detectar problemas repetidos y lenguaje real de usuarios.

Salida esperada:

- problema;
- evidencia fuente;
- usuario afectado;
- contexto;
- severidad;
- frecuencia estimada;
- alternativas actuales;
- oportunidad probable.

### Modo 3: Software Opportunity Mapping

Objetivo: convertir senales en ideas para software o automatizacion.

Salida esperada:

- idea;
- problema;
- usuario;
- MVP;
- forma tecnica probable;
- dependencias;
- riesgo;
- experimento.

### Modo 4: Monetization Hypotheses

Objetivo: convertir senales en hipotesis de oferta.

Salida esperada:

- insight fuente;
- audiencia;
- oferta;
- canal;
- pricing tentativo si la fuente lo permite;
- experimento de validacion;
- senales de continuar o descartar.

### Modo 5: Process Improvement

Objetivo: mejorar procesos personales o de desarrollo.

Salida esperada:

- proceso actual implicado;
- friccion detectada;
- practica o herramienta mencionada;
- mejora propuesta;
- costo de adopcion;
- experimento de una semana.

## 10. Requisitos funcionales

### RF1: Captura de fuente

La skill debe aceptar una o mas de estas entradas:

- URL de Reddit;
- texto de post y comentarios;
- JSON exportado;
- lista de threads;
- nombre de subreddit;
- busqueda o tema;
- notas del usuario;
- objetivo de salida.

Si no hay contenido suficiente, la skill debe pedir posts, comentarios, links o notas antes de hacer claims especificos.

### RF2: Grounding y trazabilidad

La skill debe separar:

- hechos presentes en la fuente;
- inferencias razonables;
- recomendaciones del agente;
- informacion faltante.

Cada senal importante debe estar conectada a una fuente, thread, comentario, subreddit o fragmento proporcionado.

### RF3: Evaluacion de senales

La skill debe clasificar cada senal importante por:

- tipo: problema, herramienta, tendencia, objecion, caso de uso, workflow, oportunidad, riesgo;
- dominio: IA, software, producto, monetizacion, procesos, negocio u otro;
- fuerza: alta, media, baja;
- evidencia: numero de menciones, calidad del comentario, especificidad, diversidad de fuentes;
- limitaciones: sesgo, muestra pequena, falta de contexto, datos no verificables.

### RF4: Analisis de problemas

La skill debe extraer:

- problema expresado;
- lenguaje del usuario;
- usuario afectado;
- job-to-be-done probable;
- alternativas actuales;
- frustraciones;
- frecuencia estimada;
- severidad;
- oportunidad derivada.

### RF5: Analisis de herramientas y workflows

La skill debe identificar:

- herramientas, librerias, modelos, APIs, frameworks o companias mencionadas;
- contexto de uso;
- percepcion positiva o negativa;
- problemas de adopcion;
- combinaciones de herramientas;
- oportunidades para integraciones, wrappers, templates o automatizaciones.

### RF6: Generacion de oportunidades

La skill debe traducir senales en oportunidades accionables con:

- problema;
- audiencia;
- propuesta;
- MVP;
- forma tecnica probable;
- dependencia de datos o herramientas;
- riesgo;
- primer experimento.

### RF7: Monetizacion responsable

La skill debe formular monetizacion como hipotesis, no como promesa.

Debe incluir:

- audiencia;
- oferta;
- canal probable;
- precio tentativo solo si existe base razonable;
- experimento;
- senales de avance;
- senales de descarte.

### RF8: Salida por defecto

Si el usuario no especifica formato, la skill debe usar esta estructura:

- Fuente
- Resumen ejecutivo
- Senales principales
- Problemas repetidos
- Herramientas y workflows mencionados
- Casos de uso de IA detectados
- Oportunidades para software o automatizacion
- Ideas de monetizacion
- Mejoras de proceso recomendadas
- Experimentos recomendados
- Riesgos, sesgos y limites de la fuente
- Preguntas abiertas

### RF9: Compatibilidad con specs

Cuando el usuario pida aterrizar una idea, la skill debe poder producir insumos para:

- PRD;
- `plan.md`;
- `tasks.md`;
- backlog;
- experimento de validacion;
- matriz de decision.

### RF10: Memoria derivada local opcional

Cuando el workspace tenga una convencion de memoria, la skill debe generar una salida persistible ademas del reporte principal.

Debe incluir:

- metadata de fuente compatible con `source-metadata.template.json` cuando exista;
- insight atomico compatible con `insight.template.md` cuando exista;
- separacion entre raw source, thread normalizado, resumen e insight;
- project links cuando el hallazgo aplique a un proyecto concreto;
- advertencia explicita cuando no se pueda guardar y solo se entregue contenido para guardar manualmente.

Para MVP, esto puede ser un bloque Markdown/JSON listo para guardar. No requiere base de datos, embeddings ni dashboard.

## 11. Requisitos no funcionales

### Trazabilidad

Cada conclusion relevante debe apuntar a una fuente o marcarse como inferencia.

### Escepticismo

La skill debe tratar Reddit como senal cualitativa, no como validacion cuantitativa.

### Concision

La salida debe priorizar decisiones, oportunidades y experimentos, no resumen exhaustivo.

### Seguridad comunitaria

La skill no debe ayudar a manipular comunidades, generar spam, perfilar individuos o evadir reglas de Reddit.

### Flexibilidad

Aunque el foco principal sea IA y desarrollo de software, la skill debe poder clasificar oportunidades de otros dominios cuando aparezcan.

### Actualizacion

Cuando se usen busquedas o datos recientes, la skill debe registrar fecha de consulta y advertir que las senales pueden cambiar rapido.

## 12. Criterios de aceptacion

### CA1: Analisis con threads proporcionados

GIVEN uno o mas threads de Reddit con posts y comentarios  
WHEN el usuario pide analizar oportunidades  
THEN la skill devuelve senales, problemas, herramientas, oportunidades, riesgos y experimentos conectados a la fuente.

### CA2: Dato no presente

GIVEN una pregunta sobre un dato que no aparece en los posts o comentarios  
WHEN la skill responde  
THEN indica que la fuente no contiene ese dato y evita inventarlo.

### CA3: Problemas repetidos

GIVEN varios comentarios con quejas similares  
WHEN la skill analiza el thread  
THEN agrupa el problema, conserva lenguaje representativo y estima fuerza de la senal sin presentarla como estadistica exacta.

### CA4: Ideas de software

GIVEN una discusion sobre una friccion tecnica  
WHEN el usuario pide ideas de producto  
THEN la skill propone ideas de software con problema, usuario, MVP, forma tecnica probable, riesgo y experimento.

### CA5: Monetizacion

GIVEN senales sobre una audiencia con dolor claro  
WHEN el usuario pide monetizacion  
THEN la skill propone oferta, canal, precio tentativo si procede, experimento y senales de descarte.

### CA6: Mejora de procesos

GIVEN una discusion sobre tooling, productividad o desarrollo  
WHEN el usuario pide aplicarlo a sus procesos  
THEN la skill propone mejoras practicas, costo de adopcion y experimento de una semana.

### CA7: Evitar conclusiones infladas

GIVEN un post con muchos upvotes pero poca evidencia concreta  
WHEN la skill analiza la oportunidad  
THEN advierte que popularidad no equivale a validacion y propone fuentes adicionales.

### CA8: Seguridad comunitaria

GIVEN una solicitud para generar spam, manipular votos, perfilar usuarios o evadir reglas  
WHEN la skill responde  
THEN rechaza esa parte y ofrece investigacion etica, analisis agregado o alternativas permitidas.

### CA9: Falta de fuente suficiente

GIVEN solo un nombre de subreddit o tema amplio sin posts  
WHEN la skill no tenga herramienta de busqueda disponible  
THEN pide links, comentarios o notas antes de hacer afirmaciones especificas.

### CA10: Memoria derivada en workspace

GIVEN un workspace con convencion de memoria local  
WHEN la skill analiza threads de Reddit con hallazgos accionables  
THEN produce artefactos o bloques persistibles para raw reference, thread normalizado, resumen e insights, conectados a la fuente y al proyecto relevante.

## 13. Formato de salida propuesto

```md
# Reddit AI Research Report

## Fuente
- Subreddit:
- URLs:
- Fecha de consulta:
- Alcance:
- Advertencias:

## Resumen ejecutivo

## Senales principales
| Senal | Tipo | Fuerza | Evidencia | Limite |
|-------|------|--------|-----------|--------|

## Problemas repetidos
| Problema | Usuario | Evidencia | Severidad | Oportunidad |
|----------|---------|-----------|-----------|-------------|

## Herramientas y workflows mencionados
| Herramienta | Contexto | Sentimiento | Problemas | Oportunidad |
|-------------|----------|-------------|-----------|-------------|

## Casos de uso de IA detectados
| Caso | Contexto | Madurez | Riesgo | Aplicacion posible |
|------|----------|--------|--------|--------------------|

## Ideas de producto o software
| Idea | Problema | Usuario | MVP | Experimento |
|------|----------|---------|-----|-------------|

## Monetizacion
| Oportunidad | Audiencia | Oferta | Canal | Validacion inicial |
|-------------|-----------|--------|-------|--------------------|

## Mejoras de proceso

## Riesgos y sesgos

## Preguntas abiertas
```

## 14. Riesgos

- Reddit puede amplificar opiniones extremas o sesgos de comunidad.
- Upvotes y comentarios no equivalen a demanda pagada.
- Las discusiones pueden quedar desactualizadas rapido.
- Threads aislados pueden sugerir problemas que no son frecuentes.
- El usuario puede querer automatizar extraccion o monitoreo antes de definir criterios de calidad.
- El analisis puede volverse demasiado amplio si mezcla IA, software, negocios y productividad sin taxonomia.

## 15. Mitigaciones

- Tratar cada conclusion como senal con fuerza y limitaciones.
- Separar hechos, inferencias y recomendaciones.
- Exigir fuentes o fragmentos para claims especificos.
- Usar taxonomia por dominio y tipo de senal.
- Cerrar cada oportunidad con experimento pequeno.
- Recomendar triangulacion con YouTube, GitHub, Hacker News, docs, encuestas o entrevistas antes de construir.

## 16. Metricas de exito

- Numero de threads convertidos en senales accionables.
- Numero de problemas repetidos identificados.
- Numero de ideas de software priorizadas.
- Numero de mejoras de proceso experimentadas.
- Numero de hipotesis de monetizacion validadas o descartadas.
- Porcentaje de conclusiones conectadas a fuente.
- Reduccion de ideas construidas sin evidencia inicial.

## 17. Fases futuras

### Fase 2: Skill instalada

- Crear carpeta real de skill.
- Escribir `SKILL.md`, `prompt.md`, `README.md`, `skill.json`, ejemplos y checklist.
- Definir prompts de activacion.
- Validar con threads reales pegados por el usuario.

### Fase 3: Plugin local

- Crear `.codex-plugin/plugin.json`.
- Empaquetar la skill dentro de `plugins/reddit-ai-researcher`.
- Documentar instalacion y dependencia opcional de herramientas de busqueda.

### Fase 4: Fuente estructurada

- Definir formato JSON para posts y comentarios.
- Permitir ingest manual desde exports.
- Agregar normalizacion de campos: subreddit, title, author opcional, score, created_at, comments, links.
- Alinear los campos con la convencion `knowledge/schema/source-metadata.template.json` cuando el workspace la tenga.

### Fase 5: Research OS multi-fuente

- Cruzar Reddit con YouTube, GitHub, Hacker News y notas propias.
- Crear un `opportunity-synthesizer`.
- Priorizar ideas con scoring por evidencia, esfuerzo, afinidad y potencial de monetizacion.
- Generar PRDs y planes a partir de oportunidades priorizadas.
- Migrar la memoria local validada hacia un hub compartido, probablemente Supabase/Postgres con pgvector, cuando exista volumen o colaboracion entre workspaces.

## 18. Decisiones abiertas

- Si el MVP sera solo skill analitica o plugin con skill empaquetada.
- Si se permitira busqueda web directa o solo analisis de contenido proporcionado.
- Si se usara una API oficial, exports manuales o conectores externos en fases futuras.
- Como representar autores: idealmente anonimizados o no usados salvo que sea necesario para trazabilidad publica.
- Si el repositorio debe incluir un catalogo separado para plugins, no solo skills.
- Si la memoria derivada debe vivir solo en el workspace activo, apuntar al hub `ia-learning/knowledge/` o sincronizarse posteriormente con Supabase.
