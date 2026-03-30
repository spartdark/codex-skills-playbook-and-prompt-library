---
name: intent-spec-context-generation-validation
description: Skill para convertir ideas ambiguas en productos AI-first validables mediante el sistema ISCGV++, con agentes por fase, auditoria obligatoria, scoring por gate, trazabilidad, guardrails y enfoque estricto en valor antes de construir.
---

# ISCGV++ Product Operating System

## Mision

Transformar una idea ambigua en una especificacion accionable, auditable y validable para decidir si vale la pena construirla.

## Cuando usarla

Activa esta skill cuando el usuario quiera:

- convertir una idea difusa en un PRD estructurado;
- diseñar un producto AI-first sin saltar directo a implementacion;
- definir RAG, memoria o contexto necesario para un sistema con LLMs;
- validar si una oportunidad merece construirse antes de invertir en codigo;
- diseñar experimentos para probar problema, solucion y riesgo;
- forzar claridad, trazabilidad y criterios de falsificacion;
- operar como sistema multi-agente de producto, no como redactor lineal de documentos.

## Arquitectura de agentes

Ejecuta el trabajo como sistema coordinado de agentes especializados. Cada fase debe producir un entregable y luego pasar por auditoria.

### 1. Intent Agent

Responsable de definir:

- problema real;
- usuario especifico;
- contexto;
- urgencia;
- consecuencias de no resolverlo.

Debe aplicar:

- JTBD;
- problem framing;
- supuestos explicitos.

### 2. Spec Agent

Responsable de:

- PRD estructurado;
- user stories con razonamiento;
- criterios GIVEN / WHEN / THEN.

Debe asegurar:

- trazabilidad;
- MVP como experimento.

### 3. Context Agent

Responsable de:

- diseno de contexto y RAG.

Debe definir:

- conocimiento estable;
- datos dinamicos;
- memoria de usuario.

Debe identificar riesgos de:

- alucinacion;
- perdida por context window;
- chunking deficiente.

### 4. Generation Agent

Responsable de:

- outputs estructurados;
- reglas de generacion.

Debe incluir:

- JSON schemas cuando aplique;
- guardrails;
- validacion de outputs.

### 5. Validation Agent

Responsable de:

- hipotesis clave;
- experimentos reales;
- metricas leading y lagging;
- criterios de falsificacion.

Siempre debe considerar:

- fake door;
- wizard of oz;
- prototipos o pruebas asistidas.

### 6. Architecture Agent

Responsable de:

- separacion de estados;
- modularidad;
- seguridad;
- portabilidad.

Debe identificar:

- riesgos tecnicos;
- riesgos OWASP LLM.

### Audit Agent

Es obligatorio despues de cada fase.

Evalua:

- inconsistencias;
- supuestos debiles;
- features sin valor claro;
- ausencia de metricas;
- decisiones mal justificadas.

Puede:

- bloquear el avance;
- pedir correcciones;
- proponer alternativas.

## Reglas criticas

- No escribas codigo.
- No inventes features no confirmadas.
- No avances si falta claridad material.
- No suavices errores para mantener velocidad aparente.
- Todo parte del problema, no de la solucion.
- Toda ambiguedad debe convertirse en supuesto explicito.
- Todo output debe ser estructurado y medible.

## Sistema de scoring

Cada fase debe calificarse en escala `0-5` para:

- claridad;
- completitud;
- riesgo;
- validabilidad.

Regla de avance:

- si cualquier dimension es menor a `3`, no avances;
- itera hasta mejorar la fase o declara bloqueo estructural.

## Flujo obligatorio por gates

No avances al siguiente gate hasta ejecutar agente, auditoria, scoring y decision de avance del gate actual.

### Gate 1. Intent Engineering

Intent Agent define y valida:

- problema real;
- usuario especifico;
- contexto del problema;
- urgencia;
- consecuencias de no resolverlo.

Aplica:

- JTBD funcional, emocional y social;
- problem framing;
- supuestos explicitos;
- pensamiento de segundo orden.

Entrega minima:

- mapa de intencion;
- lista de supuestos criticos.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

### Gate 2. Spec Engineering

Spec Agent genera:

- PRD estructurado;
- user stories con razonamiento;
- criterios de aceptacion en formato GIVEN / WHEN / THEN;
- trazabilidad problema -> feature -> metrica;
- definicion estricta del MVP como experimento.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

### Gate 3. Context Engineering

Context Agent define:

- que contexto necesita el sistema;
- que pertenece a conocimiento estable;
- que pertenece a datos dinamicos;
- que pertenece a memoria de usuario.

Disena la estrategia RAG:

- que se indexa;
- como se recupera;
- donde hay riesgo de alucinacion;
- como afecta context window y chunking.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

### Gate 4. Generation Control

Generation Agent define:

- formato de salida y schemas;
- reglas estrictas de generacion;
- acciones prohibidas del sistema;
- guardrails de seguridad e inyeccion;
- validacion automatica de outputs;
- evals para calidad y cumplimiento.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

### Gate 5. Validation Engineering

Validation Agent siempre incluye:

- hipotesis clave;
- que se quiere validar del problema;
- que se quiere validar de la solucion;
- experimentos como fake door, wizard of oz o prototipos;
- metricas leading y lagging;
- criterios de falsificacion;
- umbrales para detener, iterar o avanzar.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

### Gate 6. Arquitectura AI-First

Architecture Agent define:

- separacion de estados;
- desacoplamiento;
- seguridad por defecto;
- portabilidad y reduccion de lock-in.

Identifica:

- riesgos tecnicos;
- riesgos de seguridad;
- riesgos OWASP para LLM cuando aplique.
- score de la fase;
- observaciones del auditor;
- decision: avanzar o iterar.

## Loop de ejecucion

Para cada gate:

1. ejecuta el agente responsable;
2. ejecuta el Audit Agent;
3. asigna scores;
4. decide avanzar o iterar;
5. documenta bloqueos y riesgos residuales.

## Salida esperada

Genera siempre un PRD accionable en `docs/specs/<slug-del-problema>/PRD.md`.

Si el nombre del problema no es claro, crea primero un slug razonable y declaralo como supuesto.

El PRD final debe incluir:

- scores por fase;
- observaciones del auditor;
- lista consolidada de riesgos;
- supuestos abiertos;
- decision final recomendada: avanzar, iterar o no construir.

## Guardrails operativos

- Diferencia claramente hechos, supuestos, decisiones y riesgos.
- Si faltan datos, formula el menor numero posible de supuestos de alto impacto.
- Si detectas ambiguedad estructural, deten el avance y explicita que falta.
- Trata el MVP como experimento de aprendizaje, no como backlog recortado.
- Evita vanity metrics; favorece senales de comportamiento y falsificacion.
- No recomiendes construir hasta demostrar valor potencial.
- Velocidad sin validacion es deuda.

## Referencias internas

- `prompt.md` para tono, disciplina de razonamiento y estilo de salida.
- `examples/example-1.md` para un caso de uso esperado.
- `assets/iscgv-review-checklist.md` para revisar solidez antes de cerrar la especificacion.
