# Reuse Promotion Guide

Guia portable para convertir ideas, procesos, fuentes y aprendizajes en assets reutilizables para Codex:

```txt
raw signal -> processed knowledge -> project memory -> docs/templates -> skill -> plugin -> automation
```

Usala cuando quieras decidir si algo debe quedarse como memoria en `knowledge/`, promoverse a documentacion, convertirse en una skill, empaquetarse como plugin o automatizarse.

## Para Que Sirve

- Evita crear plugins a partir de ideas todavia no validadas.
- Mantiene evidencia, supuestos, experimentos y decisiones separados.
- Da a Codex una ruta clara para convertir aprendizaje en assets instalables.
- Permite adoptar el flujo desde GitHub en otros repos sin cargar todo este proyecto.

## Archivos

- [OPERATING_GUIDE.md](OPERATING_GUIDE.md): guia operativa completa.
- [../governance.md](../governance.md): reglas generales de adopcion AI-first.
- [../../README.md](../../README.md): indice de documentacion del repo.

## Uso Desde Otro Proyecto En GitHub

1. Abre el repo destino en Codex.
2. Agrega o copia el starter AI si el proyecto aun no lo tiene:
   - `AGENTS.md`
   - `PROJECT_AI_PROFILE.md`
   - `knowledge/README.md`
   - `knowledge/projects/<project-id>/reuse-backlog.md`
3. Pega el prompt de abajo en Codex.
4. Pide primero un diagnostico y despues una propuesta de archivos. No empieces creando plugins.

## Prompt De Ejemplo

```md
Quiero adoptar la Reuse Promotion Guide desde este repositorio:

https://github.com/spartdark/codex-skills-playbook-and-prompt-library

Objetivo:
Convertir ideas, procesos y aprendizajes de este proyecto en assets reutilizables sin saltar directo a skills o plugins.

Lee primero:
- AGENTS.md
- PROJECT_AI_PROFILE.md si existe
- docs/ai/governance.md desde el repo de referencia
- docs/ai/reuse-promotion-guide/README.md desde el repo de referencia
- docs/ai/reuse-promotion-guide/OPERATING_GUIDE.md desde el repo de referencia

Trabaja en dos fases:

Fase 1 - Diagnostico:
- identifica si este repo ya tiene `knowledge/`, `docs/`, `skills/`, `plugins/` o equivalentes;
- detecta donde deberia vivir la memoria del proyecto;
- lista procesos, prompts, scripts o aprendizajes que podrian ser candidatos;
- marca cada candidato como knowledge, docs/template, skill, plugin o automation;
- separa hechos verificados, inferencias y preguntas abiertas.

Fase 2 - Propuesta:
- propone la estructura minima de archivos para adoptar la guia;
- crea o actualiza `knowledge/projects/<project-id>/reuse-backlog.md`;
- no crees skills, plugins ni automations sin validar primero un workflow manual;
- define criterios de aceptacion y comandos de validacion;
- reporta los archivos que cambiarias antes de editar.

Entrega esperada:
- diagnostico breve;
- backlog inicial de candidatos;
- plan de promocion por fases;
- riesgos y decisiones que requieren aprobacion humana.
```

## Criterio Rapido

| Pregunta | Destino |
|---|---|
| Es solo una idea, fuente o aprendizaje? | `knowledge/` |
| Ya tiene evidencia y afecta decisiones? | `knowledge/projects/<project-id>/` |
| Es un proceso repetible para personas o agentes? | `docs/` o `templates/` |
| Codex debe ejecutarlo muchas veces? | `skills/` |
| Necesita scripts, tools, APIs o empaque? | `plugins/` |
| Ya paso corrida manual y QA? | automation |

## Validacion Antes De Promover

- Existe evidencia o una razon explicita para tratarlo como supuesto.
- El input, output y done condition son claros.
- Se probo manualmente al menos una vez si va a skill, plugin o automation.
- El asset no duplica una skill, plugin o doc existente.
- El impacto de contexto para Codex es bajo.
