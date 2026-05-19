# Reddit AI Researcher Plugin

Plugin publico para Codex que empaqueta la skill `reddit-ai-researcher`.

## Que hace

- Analiza posts, comentarios, subreddits, notas o exports de Reddit como fuentes trazables.
- Detecta dolores reales, preguntas repetidas, objeciones y lenguaje de usuarios.
- Extrae herramientas, frameworks, modelos, APIs y workflows mencionados.
- Traduce senales en ideas de software, automatizaciones, agentes, devtools, servicios o productos.
- Identifica oportunidades de monetizacion como hipotesis y experimentos, no promesas.
- Propone mejoras practicas para procesos de desarrollo, investigacion y productividad.
- Puede producir insumos para PRDs, planes tecnicos, backlogs y experimentos.

## Principio central

Reddit es una fuente de senales, no una fuente de verdad definitiva.

El plugin debe separar:

- hechos presentes en los posts o comentarios;
- inferencias razonables;
- recomendaciones del agente;
- informacion faltante;
- sesgos o limites de la comunidad analizada.

## Entradas esperadas

- URLs de Reddit.
- Texto pegado de posts y comentarios.
- JSON o exports manuales.
- Listas de threads.
- Nombre de subreddit o tema.
- Notas del usuario y objetivo de salida.

Si solo existe un tema amplio y no hay herramienta de busqueda disponible, la skill debe pedir links, comentarios o notas antes de hacer afirmaciones especificas.

## Fuera de alcance

- No hace scraping no autorizado ni bypass de restricciones.
- No automatiza login, cookies ni acceso privado.
- No genera spam, astroturfing ni respuestas para manipular comunidades.
- No perfila usuarios individuales ni ayuda con doxxing.
- No presenta upvotes o comentarios aislados como validacion de mercado.
- No toma decisiones tecnicas finales sin PRD, plan o validacion posterior.
