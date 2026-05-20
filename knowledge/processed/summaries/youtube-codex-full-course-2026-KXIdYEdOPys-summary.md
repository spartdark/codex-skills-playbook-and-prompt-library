---
source_type: youtube
source_url: https://www.youtube.com/watch?v=KXIdYEdOPys&t=3040s
canonical_url: https://www.youtube.com/watch?v=KXIdYEdOPys
source_title: "Codex Full Course 2026: The NEW Best AI Coding Tool"
author: Riley Brown
author_url: https://www.youtube.com/@rileybrownai
captured_at: 2026-05-19
language: en
transcript_source: "YouTube auto-captions via ytscribe; local youtube-transcript script returned temporary_provider_failure"
raw_evidence:
  - knowledge/raw/youtube/ytscribe-codex-full-course-2026-KXIdYEdOPys-en-auto.json
  - knowledge/raw/youtube/youtube-oembed-codex-full-course-2026-KXIdYEdOPys.json
normalized_transcript: knowledge/processed/transcripts/youtube-codex-full-course-2026-KXIdYEdOPys-en-auto.md
confidence: verified
projects: [ia-learning]
---

# Fuente

- URL: https://www.youtube.com/watch?v=KXIdYEdOPys&t=3040s
- Titulo: "Codex Full Course 2026: The NEW Best AI Coding Tool"
- Canal/autor: Riley Brown, verificado por YouTube oEmbed.
- Captura: 2026-05-19.
- Fuente primaria intentada: `youtube-transcript`; fallo `temporary_provider_failure`.
- Fuente usada para analisis: transcript auto-generado de YouTube obtenido via ytscribe. La precision literal puede tener errores de auto-caption.

# Resumen ejecutivo

El video presenta Codex Desktop como una interfaz de agente generalista para trabajo de software y operaciones: investigacion web, creacion y edicion de archivos, documentos, hojas de calculo, presentaciones, plugins, skills, automations, browser/computer use y flujos de desarrollo de apps. La tesis explicita es que Codex funciona como una "super app" de agentes porque une coding, co-work, browser y computer use en un solo lugar (0:00:24-0:00:38).

La parte practica importante para `ia-learning` no es solo la lista de funciones, sino el modelo operativo: organizar trabajo por carpetas/proyectos, usar chats paralelos o bifurcados, tratar cada prompt como una unidad de trabajo delegable, crear skills cuando falta integracion, y conectar outputs a validacion real como Vercel, TestFlight, Tally, Canva y Typefully.

# Ideas clave

- Codex se muestra como agente con contexto de filesystem: crea, edita y organiza archivos dentro de una carpeta de proyecto (0:04:33-0:05:33, 0:07:41-0:08:19).
- El flujo recomienda usar proyectos como boundary de memoria y artefactos; los chats viven en la UI, pero los outputs quedan en el folder del proyecto (0:08:00-0:08:18).
- Skills y plugins se explican como extensiones de capacidad: skill como "reusable workflow package" y plugin como unidad instalable (0:14:31-0:15:08).
- Automations convierten una tarea conversacional en ejecución recurrente, por ejemplo un resumen semanal del calendario (0:18:06-0:18:34).
- El valor de agentes largos se captura con "serial tasking": poner esfuerzo en un prompt, enviarlo y pasar a otro chat mientras corre (0:35:58-0:36:37).
- El caso de negocio completo combina producto, marketing y distribucion: app iOS, web app/landing, investor deck, launch video, waitlist y automatizacion de posts (0:36:45-0:37:45).
- Cuando no existe plugin oficial, el video propone pedir al agente que busque APIs y cree una skill local, como con Supabase o Typefully (0:55:33-0:56:18, 1:36:14-1:36:48).
- El cierre recomienda auditar las tareas del trabajo o negocio y probar que partes se pueden automatizar con apps, imagenes, videos, graficos y publicaciones (1:41:43-1:42:39).

# First principles

- El folder del proyecto es el contrato de estado: si un agente crea o edita artefactos, deben quedar en una ubicacion compartida, reabrible y mencionable.
- El prompt es una unidad de delegacion, no solo una pregunta. Debe contener objetivo, contexto, restricciones y criterio de avance suficiente para que el agente trabaje sin supervision inmediata.
- La productividad con agentes largos viene de pipeline, no de esperar sincronicamente. El usuario orquesta multiples tareas y vuelve a revisar cuando hay resultados.
- Las integraciones deben aproximarse por niveles: plugin oficial si existe; skill local si no existe; API key y prueba controlada si se necesita capacidad nueva.
- La validacion debe tocar el mundo real: desplegar, probar formularios, correr app en dispositivo, exportar a Canva, ver drafts creados en Typefully.

# Estructura explicativa

El video avanza en dos mitades. Primero usa un tutorial lineal para explicar UI, proyectos, permisos, modelos, esfuerzo, preview, documentos, plugins, skills y automations. Despues cambia a una demostracion de multitarea con un producto ficticio/real llamado Chorus, donde se crean artefactos de producto y go-to-market en paralelo.

El tono es demostrativo y pragmatico, con mucho "hacer en pantalla". El nivel tecnico mezcla principiante e intermedio: explica conceptos basicos como carpetas y chats, pero tambien usa Xcode, Supabase, Remotion, Vercel, TestFlight, Typefully, APIs y skills. La progresion conceptual es: entender interfaz -> extender capacidades -> orquestar agentes -> validar outputs.

# Casos practicos detectados

- Research sobre features de Codex y creacion de spreadsheet editable (0:03:59-0:09:33).
- Mencion de archivos creados con `@` para enriquecer otra investigacion (0:10:09-0:10:31).
- Conectar Google Calendar y Gmail para listar eventos y enviar resumen semanal (0:16:33-0:17:48).
- Convertir ese resumen en automation recurrente cada viernes (0:18:06-0:18:34).
- Usar computer/browser use para revisar una web y screenshots (0:20:47-0:22:05).
- Planear un set de seis artefactos alrededor de Chorus: diseno mobile, app iOS, web app, investor deck, launch video y automatizacion X (0:38:39-0:41:27).
- Crear landing/waitlist con Tally y desplegarla con Vercel (0:46:13-0:46:50, 1:33:16-1:37:31).
- Crear app iOS con autenticacion Supabase/email, probarla en Xcode y preparar TestFlight (1:29:05-1:31:40, 1:38:00-1:38:24).
- Exportar investor deck a Canva para el ultimo 5-10% manual (1:20:20-1:20:40, 1:32:01-1:32:49).
- Crear skill Typefully para drafts y automation diaria de posts (1:36:14-1:39:46).

# Oportunidades para proyectos actuales o nuevos

## Orquestador de experimentos de agente para `ia-learning`

- Problema: los aprendizajes de videos y pruebas quedan dispersos en chats.
- Oportunidad: convertir cada fuente en backlog de experimentos con evidencia y criterios.
- Forma tecnica probable: Markdown estructurado en `knowledge/`, SQLite local para indexar fuentes, y futuro Supabase.
- Riesgo: guardar demasiada informacion no accionable.
- Experimento: crear un comando local que lea `knowledge/processed/summaries` y genere `experiments.md` priorizado por impacto/esfuerzo.

## Skill factory controlada

- Problema: se necesitan skills para APIs que no tienen plugin oficial.
- Oportunidad: generar skills con plantilla, pruebas y secreto fuera de repo.
- Forma tecnica probable: usar `skill-creator`, `.env.example`, test de smoke con API mock o sandbox.
- Riesgo: fuga de claves o skills que ejecutan acciones externas sin guardrails.
- Experimento: crear una skill interna no sensible para una API de ejemplo y documentar checklist de seguridad.

## Agent launch kit

- Problema: pasar de idea a demo publica exige demasiados artefactos separados.
- Oportunidad: pipeline de "idea -> landing -> waitlist -> demo -> assets -> update social" con agentes.
- Forma tecnica probable: plan Markdown, tareas por worktree/chat, Vercel/Tally o alternativa propia, y verificacion con browser.
- Riesgo: parecer completo sin validar demanda real.
- Experimento: para una idea pequena de `ia-learning`, lanzar waitlist y medir conversion de visitas a registros.

# Ideas de workflow de IA

- Antes de construir, pedir una lista chequeable de artefactos y estados: pending, working, blocked, done.
- Usar un proyecto/folder por iniciativa y guardar outputs generados dentro del mismo folder.
- Para cada integracion externa, pedir al agente: docs actuales, alcance minimo, secretos necesarios, prueba de humo y riesgos.
- Separar generacion y refinamiento: usar agentes para primer borrador de deck/video/app y herramienta humana como Canva/Xcode/browser para validacion final.
- En multitarea, mantener un "control plane" con el estado de cada agente y el proximo checkpoint.

# Ideas de monetizacion

- Servicio/producto de "AI launch ops": paquete que construye landing, waitlist, deck, demo y automation de distribucion para founders tecnicos. Hipotesis, no validada por la fuente.
- Libreria curada de skills y agentes por caso de uso: Typefully, Supabase, Remotion, Tally, Vercel, TestFlight. La fuente muestra demanda implicita del creador por skills reutilizables, pero no valida mercado.
- Plantillas de workspace para equipos: estructura de carpetas, prompts, automations y criterios QA para usar Codex en producto/marketing.
- Auditoria de tareas automatizables: consultoria o app que toma procesos diarios de un negocio y los convierte en candidates de skills/plugins/automations.

# Experimentos recomendados

1. Crear `knowledge/projects/ia-learning/agent-workflows.md` con un template de control plane para trabajos multiagente.
2. Probar un experimento "idea a landing" con una microfeature de `ia-learning`: plan, landing, formulario, deploy, verificacion y memoria derivada.
3. Definir checklist para crear skills con APIs externas: permisos minimos, almacenamiento de secrets, prueba sandbox, rollback y evidencia.
4. Medir si un flujo multiagente realmente ahorra tiempo: una tarea hecha secuencialmente vs. con chats paralelos, registrando duracion, retrabajo y calidad.
5. Indexar transcripts y summaries en SQLite local para busqueda por timestamps y patrones de workflow.

# Prompts detectados

> Advertencia: transcript auto-generado. Los prompts pueden estar truncados o reconstruidos por captions; no se deben tratar como texto literal perfecto.

- 0:03:59: "Hello, please search and tell me the latest news on Open AI's new desktop app. List all the different features."
  - Contexto: research inicial con web search.
  - Objetivo: obtener features recientes.
  - Adaptacion: usar para fuentes actuales, pero exigir fecha y citas.

- 0:07:41: "please create a spreadsheet of the new features that you just told me."
  - Contexto: convertir research en archivo `.xlsx`.
  - Objetivo: estructurar hallazgos en tabla.
  - Adaptacion: pedir columnas explicitas y fuente por fila.

- 0:09:00: "please remove the source page column."
  - Contexto: edicion directa del spreadsheet.
  - Objetivo: modificar artefacto generado.
  - Adaptacion: pedir mantener una version con fuentes si se usa para investigacion.

- 0:10:09: "Please add anything that I missed to @Codex desktop features. Do research. Let me know if I missed anything for new features for Codex."
  - Contexto: menciona archivo existente como contexto.
  - Objetivo: enriquecer documento.
  - Adaptacion: agregar "no borres fuentes existentes; marca diferencias".

- 0:16:33: "Please list out the events for this week for me."
  - Contexto: plugin Google Calendar.
  - Objetivo: listar agenda.
  - Adaptacion: pedir conflictos, preparacion necesaria y links.

- 0:17:10: "Please, can you send me a weekly recap in email? Just email it to myself."
  - Contexto: Calendar + Gmail.
  - Objetivo: enviar resumen por email.
  - Adaptacion: pedir preview antes de enviar si hay datos sensibles.

- 0:18:06: "Please, can you make this task an automation for every Friday at 4:00 p.m. for the previous week?"
  - Contexto: convertir tarea en automation.
  - Objetivo: ejecucion recurrente.
  - Adaptacion: incluir zona horaria y criterio de contenido.

- 0:38:39: "please just make a simple bulleted list that I can check off as I go along..."
  - Contexto: control plane para crear app/producto.
  - Objetivo: checklist de seis artefactos.
  - Adaptacion: usar estados, owners, risks y validation step.

- 0:46:13: "I want to create a very basic web app landing page that can collect data from interested users for our app..."
  - Contexto: landing/waitlist.
  - Objetivo: shell con captura de emails.
  - Adaptacion: pedir privacy copy, spam protection y almacenamiento.

- 0:54:44: "please just come up with a list of considerations... Don't make the video yet."
  - Contexto: planning con Remotion skill.
  - Objetivo: pensar antes de generar.
  - Adaptacion: separar brief, storyboard, assets y QA.

- 0:55:33: "is there a Supabase skill I could download... If so, download that skill. Let's use it. Let me know where I need to sign in."
  - Contexto: falta plugin oficial.
  - Objetivo: descubrir/instalar skill.
  - Adaptacion: exigir origen, permisos, mantenimiento y smoke test.

- 1:31:36: "Please do everything to prep for this."
  - Contexto: TestFlight/App Store.
  - Objetivo: preparar release.
  - Adaptacion: demasiado abierto; convertir en checklist de App Store Connect, signing, build, screenshots y privacy.

- 1:33:16: "deploy this to @vercel and give me the public link."
  - Contexto: deploy de web app.
  - Objetivo: publicar landing.
  - Adaptacion: agregar verificacion post-deploy y env vars.

- 1:33:47: "please add this song at 50% volume in the launch video. Keep everything else the same."
  - Contexto: edicion de video.
  - Objetivo: modificar audio sin alterar resto.
  - Adaptacion: pedir licencia/uso permitido antes de usar audio.

- 1:36:14: "please, can you search Typefully and I want you to create a skill that allows me to fully control it with their new API..."
  - Contexto: crear skill con API externa.
  - Objetivo: automatizar drafts de X.
  - Adaptacion: no pegar API key en chat persistente; usar env vars/secrets.

- 1:39:22: "Please create that automation now..."
  - Contexto: daily X drafts.
  - Objetivo: automation recurrente con Typefully.
  - Adaptacion: incluir aprobacion humana antes de publicar.

# Preguntas abiertas

- Que partes del transcript son errores de auto-caption y requieren verificacion visual u OCR?
- Que features descritas como "released today" siguen vigentes al 2026-05-19? Requiere verificacion en docs oficiales de OpenAI antes de tomar decisiones.
- Que modelo de permisos es apropiado para `ia-learning` si se automatizan herramientas externas?
- Conviene crear skills locales por API o esperar plugins oficiales para herramientas sensibles?
- Que metricas debe usar `ia-learning` para saber si un workflow multiagente mejora resultados y no solo produce mas artefactos?
