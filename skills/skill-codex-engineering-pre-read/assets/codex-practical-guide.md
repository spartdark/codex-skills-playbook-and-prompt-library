# Guia Practica de Codex

## Proposito

Guia operativa para usar Codex como agente de ingenieria, no solo como generador de codigo. Resume la investigacion realizada sobre Codex y la convierte en reglas practicas para trabajar mejor en este repo y en futuros proyectos.

## Tesis principal

Codex rinde mejor cuando se usa como un colaborador tecnico con contexto, limites, criterios de aceptacion y verificacion. La unidad de trabajo no deberia ser "dame codigo", sino una tarea revisable:

```txt
intencion -> contexto -> alcance -> implementacion -> verificacion -> memoria
```

## Fuentes y trazabilidad

- Investigacion oficial: `knowledge/processed/summaries/openai-codex-official-usage-guide-2026-05-20.md`
- Metadata de fuentes oficiales: `knowledge/raw/web/openai-codex-official-docs-2026-05-20.json`
- Workflows derivados: `knowledge/projects/ia-learning/agent-workflows.md`
- Mejora de proceso: `knowledge/projects/ia-learning/process-improvements.md`
- Template complementario: `docs/skills/codex-prompt-briefs.md`
- Carpeta de control SDD: `docs/skills/codex-control-folder-sdd.md`

## Modelo mental

Codex puede operar en varios niveles:

- pair programmer local: leer archivos, editar codigo, correr comandos y explicar decisiones;
- investigador tecnico: analizar docs, fuentes, errores, logs o repos y convertirlos en criterio;
- ejecutor de tareas: implementar features, bugs, tests, refactors y documentacion;
- reviewer: revisar diffs, riesgos, regresiones y cobertura de pruebas;
- coordinador: dividir trabajo en fases, agentes, worktrees, backlog y validaciones;
- curador de memoria: guardar fuentes, summaries, insights y decisiones en `knowledge/`.

El mayor valor aparece cuando estos niveles se conectan. Por ejemplo: una fuente externa produce un insight, el insight produce un experimento, el experimento produce un cambio validado, y el resultado vuelve a la memoria del proyecto.

## Flujo recomendado

### 1. Preparar la tarea

Antes de pedir implementacion, define:

- objetivo concreto;
- usuario o flujo afectado;
- archivos, modulos o areas probables;
- restricciones;
- criterios de aceptacion;
- comando de verificacion.

Usa `docs/skills/codex-prompt-briefs.md` para tareas medianas o grandes.

### 2. Pedir exploracion

Cuando el area no es obvia, pide primero contexto:

```md
Revisa el repo y dime donde vive este flujo, que archivos tocarias, que riesgos ves y como lo verificarias. No implementes todavia.
```

Esto evita cambios prematuros y ayuda a detectar dependencias ocultas.

### 3. Convertir a plan tecnico

Para cambios relevantes, pide un plan corto:

```md
Propone un plan por fases pequenas. Cada fase debe tener archivos probables, criterio de aceptacion y comando de verificacion.
```

### 4. Ejecutar cambios acotados

Cuando el plan sea claro:

```md
Implementa la fase 1. Mantente dentro del alcance definido. Si encuentras una decision abierta, explicala antes de ampliar el cambio.
```

### 5. Verificar

Codex debe correr pruebas, builds, linters o validaciones manuales cuando sea posible. Si no puede ejecutar algo, debe decirlo explicitamente y dejar el riesgo visible.

### 6. Cerrar con resumen revisable

El cierre esperado debe incluir:

- archivos modificados;
- que cambio;
- como se verifico;
- riesgos restantes;
- siguiente accion recomendada, si aplica.

### 7. Actualizar memoria

Si la tarea uso fuentes externas o produjo un aprendizaje reutilizable, actualizar `knowledge/`:

- `knowledge/raw/`: evidencia o metadata original;
- `knowledge/processed/`: resumen, transcript, thread o insight;
- `knowledge/projects/ia-learning/`: decision, experimento, patron o mejora de proceso.

## Casos de uso poco aprovechados

### 1. Memoria local del proyecto

Usa Codex para preservar contexto que normalmente se pierde en el chat:

- fuentes consultadas;
- decisiones tecnicas;
- errores recurrentes;
- prompts que funcionaron;
- criterios de aceptacion;
- experimentos y resultados.

Regla: no guardar solo resumenes. Guardar evidencia, confianza y enlace al proyecto.

Cuando el proyecto requiera continuidad entre sesiones, usa una carpeta de control SDD. El patron recomendado esta en `docs/skills/codex-control-folder-sdd.md` y define donde guardar specs, decisiones, preguntas abiertas, experimentos, validacion y fuentes.

### 2. Investigacion a backlog

Codex puede transformar videos, Reddit, articulos o docs en tareas reales:

```txt
fuente -> claims -> insights -> experimentos -> backlog -> implementacion
```

Esto evita que la investigacion termine como notas pasivas.

### 3. Reviewer tecnico antes del PR

Pide a Codex que revise sus propios cambios:

```md
Haz code review de este diff. Prioriza bugs, regresiones, edge cases, seguridad, performance y tests faltantes.
```

Debe responder con hallazgos accionables, no con una aprobacion generica.

### 4. Generacion de tests desde comportamiento

En vez de pedir "agrega tests", pide:

```md
Identifica el comportamiento critico de este modulo, encuentra casos borde no cubiertos y agrega pruebas que protejan ese comportamiento.
```

### 5. Migraciones por fases

Para cambios grandes, Codex puede disenar una migracion incremental:

- fase 1: compatibilidad;
- fase 2: nuevo comportamiento detras de feature flag o adaptador;
- fase 3: migracion de consumidores;
- fase 4: limpieza;
- fase 5: validacion final.

### 6. Control plane de agentes

Cuando hay varias piezas de trabajo, Codex puede coordinar:

- spec;
- implementacion;
- QA;
- docs;
- memoria;
- release notes.

Cada lane debe tener entregable y verificacion.

### 7. Auditoria de deuda tecnica

Pide una auditoria enfocada:

```md
Encuentra deuda tecnica de alto riesgo en esta area. Ordena por impacto, evidencia, costo probable y primer paso de mitigacion.
```

### 8. Documentacion viva

Despues de implementar, Codex puede actualizar README, runbooks, docs de skills o decisiones tecnicas. Esto mantiene el conocimiento cerca del codigo.

## Buenas practicas

- Dar contexto antes de pedir codigo.
- Definir no-alcance para evitar cambios laterales.
- Pedir criterios de aceptacion observables.
- Pedir verificacion real, no solo explicacion.
- Mantener cambios pequenos cuando el riesgo sea alto.
- Pedir a Codex que lea patrones existentes antes de crear abstracciones.
- Usar `knowledge/` para fuentes externas y aprendizajes reutilizables.
- Separar evidencia verificada de inferencias.
- Pedir resumen final orientado a review.
- Reutilizar templates y checklists del repo.

## Antipatrones

- "Hazme una app completa" sin usuario, alcance ni validacion.
- "Arregla esto" sin sintoma, error o reproduccion.
- "Mejora el codigo" sin definir el criterio de mejora.
- "Investiga" sin pedir decision, evidencia o siguiente accion.
- Aceptar una respuesta sin pruebas cuando habia forma razonable de verificar.
- Guardar resumenes sin fuente primaria o metadata.
- Hacer cambios grandes sin fases ni rollback.
- Pedir paralelismo sin ownership claro de archivos o entregables.

## Checklist para una buena sesion de Codex

- El objetivo esta escrito como resultado.
- El contexto minimo esta disponible.
- El alcance y no-alcance estan delimitados.
- Hay restricciones tecnicas claras.
- Los criterios de aceptacion son observables.
- Existe comando o flujo de verificacion.
- Se pidio resumen final con archivos y riesgos.
- Si hubo fuentes externas, quedaron registradas en `knowledge/`.
- Si hubo aprendizaje reutilizable, quedo vinculado a `knowledge/projects/ia-learning/`.

## Mini templates

### Bug

```md
Hay un bug: [sintoma].
Pasos o evidencia: [error, log, screenshot, input/output].
Encuentra causa raiz, corrige, agrega prueba y ejecuta verificacion.
```

### Feature

```md
Agrega [feature] para [usuario/flujo].
Revisa patrones existentes antes de implementar.
Incluye [alcance].
No incluyas [no-alcance].
Verifica con [comando/flujo].
```

### Investigacion

```md
Investiga [tema] para decidir [decision].
Guarda fuentes en `knowledge/` si son externas.
Entrega: fuentes, hallazgos, confianza, opciones, recomendacion y siguiente accion.
```

### Review

```md
Revisa este cambio como maintainer.
Prioriza bugs, regresiones, seguridad, performance, mantenibilidad y tests faltantes.
Incluye archivo/linea cuando aplique.
```

## Criterio de exito

Una buena sesion de Codex termina con una de estas salidas:

- cambio implementado y verificado;
- plan tecnico listo para ejecutar;
- decision documentada con evidencia;
- blocker claro con siguiente accion;
- memoria actualizada para futuras sesiones.

Si no deja ninguna de esas salidas, probablemente fue una conversacion util pero no una unidad de trabajo reutilizable.
