# Codex Prompt Briefs

## Proposito

Convencion para trabajar con Codex como un agente de ingenieria: cada tarea importante debe tener contexto, limites, criterios de aceptacion y una forma clara de verificacion.

El objetivo no es escribir prompts largos por costumbre. El objetivo es reducir ambiguedad, evitar retrabajo y hacer que cada sesion de Codex produzca cambios revisables.

## Cuando usarla

Usar este brief cuando pidas a Codex:

- implementar una feature;
- corregir un bug;
- refactorizar codigo;
- escribir o actualizar tests;
- documentar un flujo;
- revisar un PR o cambios locales;
- investigar una decision tecnica;
- convertir investigacion en tareas ejecutables.

Para preguntas simples o comandos puntuales, no hace falta usar el formato completo.

## Principio guia

No pidas "hazme X" como si Codex fuera magia. Dale una tarea como se la darias a un ingeniero:

- que resultado esperas;
- donde debe mirar;
- que no debe tocar;
- como sabra que termino;
- como debe verificarlo;
- que debe reportar al final.

## Template completo

````md
# Codex Prompt Brief

## Objetivo

Quiero que [implementes / arregles / investigues / refactorices / documentes] lo siguiente:

[Describe el resultado esperado en 2-5 lineas.]

## Contexto

Proyecto:
[Que hace el proyecto.]

Area relevante:
[Archivos, modulos, carpetas o flujo afectado.]

Situacion actual:
[Que existe hoy, que problema hay o que quieres mejorar.]

Ejemplo si aplica:
[URL, captura, error, input/output esperado, ticket, stack trace, diseno, etc.]

## Alcance

Incluye:
- [Cambio 1]
- [Cambio 2]
- [Cambio 3]

No incluye:
- [Cosa que no debe tocar]
- [Refactor que debe evitar]
- [Dependencia o tecnologia que no quieres agregar]

## Restricciones

- Sigue los patrones existentes del repo.
- Manten los cambios lo mas acotados posible.
- No cambies APIs publicas salvo que sea necesario.
- No agregues dependencias sin justificarlo.
- No borres cambios existentes que no sean tuyos.
- Si encuentras ambiguedad importante, explicala antes de avanzar.

## Criterios de aceptacion

La tarea esta terminada cuando:

- [Criterio observable 1]
- [Criterio observable 2]
- [Criterio observable 3]
- No se rompe el flujo existente de [X].
- El codigo queda cubierto por pruebas o verificacion manual clara.

## Verificacion

Antes de terminar, ejecuta:

```bash
[comando de test/build/lint]
```

Tambien verifica manualmente:

```txt
[flujo manual esperado]
```

Si no puedes ejecutar algo, explica por que.

## Entregable esperado

Al final responde con:

- Archivos modificados.
- Que cambio.
- Como lo verificaste.
- Riesgos o casos pendientes.
- Siguiente paso recomendado, si aplica.
````

## Version corta

```md
Quiero que [objetivo].

Contexto:
[Que hace el proyecto y donde mirar.]

Alcance:
- Incluye [X]
- No incluye [Y]

Restricciones:
[Sigue patrones existentes, no agregues dependencias, cambio acotado.]

Criterios de aceptacion:
- [Resultado verificable 1]
- [Resultado verificable 2]

Verificacion:
Ejecuta [comando].

Entrega:
Resume cambios, archivos modificados, pruebas y riesgos.
```

## Ejemplo

````md
# Codex Prompt Brief

## Objetivo

Corrige el bug donde el usuario puede guardar un curso sin titulo en el modulo de creacion de cursos.

## Contexto

Proyecto:
Plataforma de aprendizaje con cursos, lecciones y progreso de usuarios.

Area relevante:
Revisa `src/courses/`, `src/components/course-form/` y tests relacionados.

Situacion actual:
El formulario permite enviar un curso con titulo vacio si el usuario escribe solo espacios.

Ejemplo:
Input: `"   "`
Resultado actual: se guarda.
Resultado esperado: se muestra error de validacion y no se envia.

## Alcance

Incluye:
- Validar titulo vacio o solo espacios.
- Mostrar mensaje de error en UI.
- Evitar envio al backend si el titulo no es valido.
- Agregar o actualizar tests.

No incluye:
- Redisenar el formulario.
- Cambiar el modelo de datos.
- Agregar nueva libreria de validacion.

## Restricciones

- Sigue los patrones existentes del repo.
- Manten el cambio acotado al formulario y validacion relacionada.
- No cambies APIs publicas salvo que sea necesario.
- No borres cambios existentes que no sean tuyos.

## Criterios de aceptacion

La tarea esta terminada cuando:

- El formulario rechaza titulos vacios.
- El formulario rechaza titulos con solo espacios.
- El usuario ve un error claro.
- No se llama al backend con datos invalidos.
- Los tests relevantes pasan.

## Verificacion

Ejecuta:

```bash
npm test
npm run lint
```

Si hay tests especificos para cursos, ejecutalos tambien.

## Entregable esperado

Al final responde con:

- Archivos modificados.
- Que cambio.
- Tests ejecutados.
- Riesgos pendientes.
````

## Checklist de calidad

Antes de enviar una tarea a Codex, valida:

- El objetivo describe un resultado, no solo una actividad.
- El contexto dice donde mirar o que flujo entender.
- El alcance separa lo incluido de lo excluido.
- Las restricciones protegen decisiones importantes del repo.
- Los criterios de aceptacion son observables.
- Hay al menos una forma de verificacion.
- El entregable final esperado esta definido.

## Antipatrones

- "Hazme una app completa" sin usuario, alcance ni criterios.
- "Arregla los bugs" sin sintomas, errores o pasos de reproduccion.
- "Mejora el codigo" sin definir que significa mejorar.
- "Agrega tests" sin especificar comportamiento critico.
- "Investiga esto" sin pedir una decision, resumen trazable o siguiente accion.

## Relacion con memoria local

Cuando el brief use fuentes externas, videos, Reddit, documentacion o articulos, aplica la convencion de `knowledge/`:

- guardar evidencia en `knowledge/raw/`;
- normalizar resumen o transcript en `knowledge/processed/`;
- enlazar insights utiles en `knowledge/projects/ia-learning/`;
- marcar confianza y fecha de captura.

Esto permite que futuras sesiones de Codex recuperen contexto sin depender solo del historial del chat.
