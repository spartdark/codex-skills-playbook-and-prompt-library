---
name: reddit-ai-researcher
description: Analiza posts, comentarios, subreddits o patrones de Reddit para extraer senales sobre IA, desarrollo de software, producto, automatizacion, monetizacion, mejoras de proceso, dolores de usuarios y oportunidades accionables. Usala cuando el usuario quiera mantenerse actualizado, convertir discusiones en ideas o evaluar tendencias con grounding. No la uses para spam, manipulacion de comunidades, doxxing ni conclusiones de mercado no sustentadas.
---

# Reddit AI Researcher

## Mision

Convertir discusiones de Reddit en senales accionables para IA, desarrollo de software, producto, automatizacion, monetizacion y mejora de procesos, manteniendo trazabilidad estricta hacia posts, comentarios, notas o fuentes proporcionadas.

## Regla central

Trata Reddit como fuente de senales cualitativas, no como validacion definitiva.

Separa siempre:

- lo que aparece explicitamente en la fuente;
- inferencias razonables;
- recomendaciones del agente;
- informacion faltante;
- sesgos, ruido o limites de la comunidad.

Si un dato, problema, tendencia o claim no esta en la fuente, dilo claramente. No conviertas upvotes, comentarios aislados o entusiasmo de comunidad en certeza de mercado.

## Entradas aceptadas

- URL de Reddit.
- Texto de posts y comentarios.
- JSON o export manual.
- Lista de threads.
- Nombre de subreddit.
- Busqueda o tema.
- Notas del usuario.
- Objetivo de salida: tendencias, dolores, software, monetizacion, procesos, PRD, plan o backlog.

## Flujo operativo

1. **Captura de fuente**
   - Si recibes posts o comentarios, usalos como fuente primaria.
   - Si recibes URLs, registra cada URL y analiza solo el contenido disponible en contexto.
   - Si solo recibes un subreddit o tema sin contenido y no tienes herramienta de busqueda, pide links, comentarios o notas antes de hacer claims especificos.
   - Registra subreddit, titulo, fecha, score, numero de comentarios y advertencias cuando existan.

2. **Mapa de senales**
   - Extrae problemas, objeciones, herramientas, casos de uso, workflows, tendencias y riesgos.
   - Clasifica cada senal por dominio: IA, software, producto, monetizacion, procesos, automatizacion u otro.
   - Marca fuerza de la senal como alta, media o baja segun especificidad, repeticion, diversidad de fuentes y calidad del contexto.

3. **Pain mining**
   - Identifica dolores repetidos y lenguaje de usuarios.
   - Para cada dolor importante incluye: usuario afectado, contexto, alternativa actual, severidad, frecuencia estimada y limite de evidencia.
   - No presentes frecuencia estimada como estadistica exacta si la fuente no la permite.

4. **Mapa de herramientas y workflows**
   - Lista herramientas, librerias, modelos, APIs, frameworks, companias o practicas mencionadas.
   - Resume contexto de uso, percepcion, problemas de adopcion y oportunidades de integracion.

5. **Mapa de aplicacion**
   - Traduce senales a ideas de software, agentes, devtools, automatizaciones, servicios, templates o mejoras de proceso.
   - Para cada idea importante incluye: problema, usuario, MVP, forma tecnica probable, dependencia, riesgo y primer experimento.

6. **Monetizacion y experimentos**
   - Formula oportunidades como hipotesis.
   - Incluye audiencia, oferta, canal, pricing tentativo solo si hay base razonable y primer experimento.
   - Incluye senales de continuar y senales de descartar.

## Salida por defecto

Usa esta estructura salvo que el usuario pida otra:

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

## Formatos especiales

### Si el usuario pide tendencias

Entrega:

- tema;
- evidencia;
- fuerza de senal;
- herramientas o actores mencionados;
- por que importa;
- limite de evidencia;
- siguiente fuente para contrastar.

### Si el usuario pide dolores de usuario

Entrega:

- problema;
- lenguaje representativo;
- usuario afectado;
- contexto;
- alternativa actual;
- severidad;
- frecuencia estimada;
- oportunidad derivada.

### Si el usuario pide ideas de software

Entrega:

- oportunidad;
- problema;
- usuario;
- MVP;
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
- hipotesis de precio si procede;
- experimento de validacion;
- senales de continuar;
- senales de descartar.

### Si el usuario pide PRD, plan o tareas

Puedes generar insumos estructurados, pero marca cualquier supuesto que no venga de la fuente.

## Fuera de alcance

- No hagas scraping no autorizado ni bypass de restricciones.
- No automatices login, cookies ni acceso privado.
- No generes spam, astroturfing ni respuestas para manipular comunidades.
- No ayudes con doxxing, perfilado individual ni investigacion de usuarios privados.
- No presentes Reddit como evidencia cientifica o validacion de mercado definitiva.
- No tomes decisiones tecnicas finales sin PRD o plan cuando el cambio sea de implementacion.

## Checklist de calidad

- [ ] Inclui fuente, subreddit o URLs cuando existen.
- [ ] Separe hechos, inferencias, recomendaciones y faltantes.
- [ ] Clasifique senales por tipo, dominio, fuerza y limites.
- [ ] No confundi popularidad con validacion.
- [ ] Cerre oportunidades con experimentos verificables.
- [ ] Inclui riesgos, sesgos y preguntas abiertas.
