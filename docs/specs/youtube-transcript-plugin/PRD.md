---
title: "PRD: Transcripcion de YouTube"
status: "draft"
owner: "VSM / Codex"
created: "2026-05-18"
---

# PRD: Transcripcion de YouTube

## 1. Resumen

Crear un plugin para Codex que permita extraer transcripciones de videos de YouTube de forma automatica y entregarlas como fuente confiable para una skill de investigacion, ideacion y aplicacion practica en proyectos de IA, desarrollo de apps y monetizacion.

El plugin no reemplaza a la skill `youtube-ai-researcher`; la habilita. El plugin se encarga de obtener y normalizar la fuente. La skill se encarga de analizar, sintetizar, aplicar y convertir esa fuente en decisiones utiles.

## 2. Problema

Actualmente, para analizar videos de YouTube con profundidad, el usuario necesita copiar transcripciones manualmente o depender de resumenes incompletos. Esto limita la capacidad de:

- estudiar contenido tecnico o estrategico de forma verificable;
- extraer ideas aplicables a proyectos como Altar MX y futuras apps;
- identificar patrones de explicacion, estructuras conceptuales y modelos mentales;
- detectar oportunidades de automatizacion, producto y monetizacion;
- construir una biblioteca reutilizable de conocimiento basado en fuentes.

Sin una transcripcion completa y trazable, los analisis corren el riesgo de inventar detalles, perder matices importantes o no poder citar correctamente el material fuente.

## 3. Objetivo

Construir un plugin que, dado uno o varios enlaces de YouTube, obtenga la transcripcion disponible, la normalice y la entregue a Codex en un formato estructurado que pueda ser usado por skills de investigacion, documentacion, producto o desarrollo.

## 4. Usuarios

### Usuario principal

Fundador, builder o creador que usa IA para desarrollar productos, apps, automatizaciones y estrategias de monetizacion.

### Usuarios secundarios

- Agentes de Codex que necesitan fuentes verificables antes de generar analisis.
- Skills de investigacion que requieren transcripciones limpias.
- Flujos de especificacion de producto que convierten videos en PRDs, planes tecnicos o tareas.

## 5. Casos de uso iniciales

### UC1: Analizar un video para aprendizaje

El usuario proporciona una URL de YouTube y pide entender el contenido. El plugin obtiene la transcripcion y la skill genera resumen, conceptos clave, first principles y explicacion pedagogica.

### UC2: Convertir un video en ideas para apps

El usuario proporciona una URL sobre IA, producto o desarrollo. El plugin extrae la transcripcion y la skill produce ideas accionables para Altar MX u otras apps.

### UC3: Detectar oportunidades de monetizacion

El usuario proporciona videos de creadores, builders o expertos. El plugin obtiene la fuente y la skill identifica ofertas posibles, audiencias, canales de distribucion y experimentos de validacion.

### UC4: Estudiar estructura explicativa

El usuario proporciona videos de referencia. El plugin extrae transcripciones y la skill analiza estructura conceptual, ritmo, tono, analogias y progresion de ideas sin generar contenido nuevo ni copiar la voz exacta del creador.

### UC5: Procesar varios videos

El usuario proporciona una lista de URLs. El plugin extrae transcripciones y devuelve un paquete estructurado para comparacion entre videos.

## 6. Alcance MVP

El MVP debe permitir:

- recibir una URL individual de YouTube;
- validar que la URL corresponde a un video soportado;
- obtener la transcripcion disponible del video;
- preservar metadatos basicos: URL, video id, titulo si esta disponible, canal si esta disponible, idioma de transcripcion si esta disponible;
- devolver la transcripcion con timestamps cuando existan;
- guardar resultados con nombres de archivo legibles cuando el usuario pida persistir el JSON;
- devolver errores claros cuando no exista transcripcion, el video sea privado, el video no este disponible o la extraccion falle;
- entregar un formato de salida estable para que otras skills lo consuman;
- citar siempre la URL fuente en la respuesta final.

## 7. Fuera de alcance para MVP

- Descargar video o audio.
- Transcribir audio con modelos speech-to-text cuando no exista transcripcion disponible.
- Analisis semantico profundo dentro del plugin.
- Generacion de guiones, PRDs o planes tecnicos dentro del plugin.
- Monitoreo automatico de canales.
- Persistencia en base de datos.
- Dashboard visual.
- Login con cuenta de YouTube.
- Evadir restricciones, paywalls, privacidad o terminos de acceso.

## 8. Requisitos funcionales

### RF1: Entrada de video

El plugin debe aceptar URLs de YouTube en formatos comunes:

- `https://www.youtube.com/watch?v=...`
- `https://youtu.be/...`
- URLs con parametros adicionales.

### RF2: Normalizacion de video id

El plugin debe extraer un `video_id` estable a partir de la URL y usarlo como identificador primario.

### RF3: Extraccion de transcripcion

El plugin debe intentar obtener la transcripcion disponible para el video.

Si existen varias transcripciones, debe preferir este orden inicial:

1. idioma solicitado por el usuario, si existe;
2. espanol, si existe;
3. ingles, si existe;
4. primera transcripcion disponible.

### RF4: Salida estructurada

El plugin debe devolver un objeto estructurado con:

- `source_url`
- `video_id`
- `title`
- `channel`
- `language`
- `is_auto_generated`, si se puede determinar
- `segments`
- `plain_text`
- `retrieved_at`
- `warnings`
- `output_filename`, si el resultado se guarda en disco

Cada segmento debe incluir, cuando este disponible:

- `start`
- `duration`
- `text`

### RF5: Manejo de errores

El plugin debe distinguir entre:

- URL invalida;
- video no disponible;
- video privado o restringido;
- transcripcion no disponible;
- idioma solicitado no disponible;
- fallo temporal de red o proveedor;
- fallo interno inesperado.

### RF6: Consumo por skills

La salida debe ser suficientemente limpia para que una skill como `youtube-ai-researcher` pueda:

- citar la fuente;
- analizar contenido;
- mapear ideas;
- separar lo que esta en la transcripcion de inferencias del agente.

### RF7: Trazabilidad

Toda respuesta generada a partir de una transcripcion debe conservar referencia a la URL fuente y, cuando sea posible, timestamps relevantes.

### RF8: Nombres legibles para archivos JSON

Cuando el plugin guarde una transcripcion en disco, debe poder generar un nombre natural basado en metadatos disponibles:

- canal;
- titulo del video;
- idioma;
- `video_id`;
- fecha de extraccion, si ayuda a evitar colisiones.

El nombre debe ser seguro para filesystem, corto, identificable y mas facil de reconocer que un archivo basado solo en `video_id`.

Ejemplo preferido:

`riley-brown_codex-build-your-full-ai-marketing-team_en_sL-KBnYB17I.json`

### RF9: Soporte para deteccion posterior de prompts

El plugin no debe hacer analisis semantico profundo, pero debe preservar suficiente estructura para que una skill posterior pueda detectar prompts o instrucciones dictadas en el video:

- segmentos con timestamps;
- texto sin normalizaciones agresivas;
- metadatos de idioma;
- advertencias sobre transcripcion auto-generada;
- advertencias cuando el texto venga de fallback o pueda estar incompleto.

Si el prompt solo aparece visualmente en pantalla y no esta en la transcripcion, el plugin no debe inventarlo. Esa capacidad requeriria una fase futura con captura visual u OCR.

## 9. Requisitos no funcionales

### Confiabilidad

El plugin debe fallar de forma explicita y recuperable. No debe inventar transcripciones ni completar huecos.

### Legalidad y terminos

El plugin debe respetar disponibilidad publica, restricciones de privacidad y terminos de acceso aplicables. No debe descargar contenido audiovisual ni intentar saltarse restricciones.

### Seguridad

El plugin no debe ejecutar contenido remoto como codigo. Las URLs deben validarse y tratarse como entrada no confiable.

### Rendimiento

Para un video individual, el resultado deberia estar disponible en menos de 15 segundos en condiciones normales de red y proveedor.

### Observabilidad

Los errores deben incluir mensajes accionables para el agente y para el usuario.

## 10. Criterios de aceptacion

### CA1: URL valida con transcripcion disponible

GIVEN una URL publica de YouTube con transcripcion disponible  
WHEN el usuario solicita extraer la transcripcion  
THEN el plugin devuelve `video_id`, metadatos disponibles, segmentos con texto y `plain_text`.

### CA2: URL con parametros extra

GIVEN una URL de YouTube con parametros adicionales  
WHEN el plugin procesa la URL  
THEN extrae correctamente el `video_id` y conserva la URL fuente original.

### CA3: Transcripcion no disponible

GIVEN un video sin transcripcion disponible  
WHEN el plugin intenta extraerla  
THEN devuelve un error `transcript_unavailable` y no inventa contenido.

### CA4: Idioma preferido

GIVEN un video con transcripciones en varios idiomas  
WHEN el usuario solicita un idioma especifico disponible  
THEN el plugin devuelve esa transcripcion e identifica el idioma.

### CA5: Idioma no disponible

GIVEN un usuario solicita un idioma que no existe para el video  
WHEN existen otras transcripciones disponibles  
THEN el plugin devuelve una advertencia y usa el fallback configurado.

### CA6: Fuente trazable

GIVEN una transcripcion extraida correctamente  
WHEN una skill genera analisis a partir de ella  
THEN la salida incluye la URL fuente y distingue datos del video vs inferencias del agente.

### CA7: Error de URL invalida

GIVEN una entrada que no es una URL de video de YouTube soportada  
WHEN el plugin la procesa  
THEN devuelve un error `invalid_youtube_url` con mensaje claro.

### CA8: Nombre legible de salida

GIVEN una URL de YouTube con titulo y canal disponibles  
WHEN el usuario pide guardar la transcripcion con nombre automatico  
THEN el plugin genera un archivo JSON identificable por canal, titulo, idioma y `video_id`, no solo por ID.

### CA9: Base para prompts detectables

GIVEN una transcripcion donde el creador dicta instrucciones para un agente  
WHEN el plugin devuelve los segmentos  
THEN conserva timestamps y texto suficiente para que una skill posterior pueda extraer esos prompts sin reconstruir contenido inventado.

## 11. Relacion plugin + skill

El sistema debe separarse en dos capas:

### Plugin: `youtube-transcript`

Responsabilidad:

- acceso tecnico;
- extraccion;
- normalizacion;
- errores;
- formato estructurado.

No debe:

- decidir estrategia de producto;
- escribir guiones;
- proponer monetizacion;
- imitar estilos;
- resumir sin que una skill lo pida.

### Skill: `youtube-ai-researcher`

Responsabilidad:

- analisis de contenido;
- first principles;
- patrones de explicacion;
- oportunidades para apps;
- ideas de IA;
- monetizacion;
- prompts detectados y explicaciones basadas en la fuente.

No debe:

- fingir que tiene transcripcion si no existe;
- copiar voz exacta de una persona real;
- generar guiones, posts, newsletters, anuncios o piezas de contenido;
- inventar detalles no presentes en la fuente.

## 12. Formato de salida propuesto

```json
{
  "source_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "video_id": "VIDEO_ID",
  "title": "Video title if available",
  "channel": "Channel name if available",
  "language": "es",
  "is_auto_generated": true,
  "retrieved_at": "2026-05-18T00:00:00Z",
  "output_filename": "riley-brown_codex-build-your-full-ai-marketing-team_en_sL-KBnYB17I.json",
  "segments": [
    {
      "start": 0.0,
      "duration": 4.2,
      "text": "Transcript text segment."
    }
  ],
  "plain_text": "Full normalized transcript text.",
  "warnings": []
}
```

## 13. Riesgos

- YouTube puede cambiar disponibilidad, formato o acceso a transcripciones.
- Algunos videos no tienen transcripcion.
- Las transcripciones automaticas pueden contener errores.
- Videos largos pueden producir textos muy extensos para el contexto del agente.
- Dependencias no oficiales pueden romperse o tener restricciones.
- El usuario puede esperar analisis cuando el plugin solo debe extraer fuente.

## 14. Mitigaciones

- Separar extraccion tecnica de analisis.
- Devolver errores explicitos y advertencias.
- Mantener timestamps para auditoria.
- Permitir salida segmentada para resumir por partes.
- Documentar claramente que speech-to-text es fase posterior.
- Validar opciones tecnicas contra documentacion oficial antes de implementar.

## 15. Metricas de exito

- Porcentaje de videos publicos con transcripcion disponible extraidos correctamente.
- Tiempo medio de extraccion por video.
- Porcentaje de errores clasificados correctamente.
- Numero de analisis reutilizables generados por la skill a partir de transcripciones.
- Numero de ideas de app, automatizacion o monetizacion derivadas de videos.

## 16. Fases futuras

### Fase 2: Procesamiento por lotes

- aceptar multiples URLs;
- devolver resultados parciales;
- comparar videos;
- detectar temas recurrentes.

### Fase 3: Cache y biblioteca local

- guardar transcripciones;
- evitar extracciones duplicadas;
- etiquetar por proyecto, canal, tema o oportunidad.

### Fase 4: Monitoreo de canales

- revisar canales o playlists;
- detectar videos nuevos;
- disparar analisis automaticos.

### Fase 5: Transcripcion por audio

- usar speech-to-text cuando no exista transcripcion disponible;
- marcar claramente que la fuente proviene de audio transcrito, no de subtitulos de YouTube.

### Fase 6: Integracion con flujos de producto

- generar PRDs;
- generar planes tecnicos;
- generar tareas para agentes;
- conectar insights con proyectos como Altar MX.

## 17. Decisiones abiertas

- Si el plugin sera repo-local o home-local.
- Que proveedor o mecanismo se usara para obtener transcripciones.
- Si se permitira cache desde el MVP.
- Si el plugin debe incluir una tool MCP propia desde la primera version.
- Si se requiere autenticacion para ciertos casos.
- Donde se guardaran transcripciones largas si exceden el contexto.
- Que idiomas seran prioritarios para el usuario.

## 18. Supuestos

- El usuario quiere usar videos como fuente de aprendizaje, estrategia y ejecucion, no solo como resumenes genericos.
- El primer producto valioso es extraer transcripciones confiables; el analisis puede vivir en una skill separada.
- Altar MX y futuros proyectos de apps seran los principales destinos de aplicacion.
- La monetizacion se explorara a partir de insights, no como promesa automatica del plugin.

## 19. Principio rector

El plugin debe traer la fuente al agente. La skill debe convertir la fuente en criterio.
