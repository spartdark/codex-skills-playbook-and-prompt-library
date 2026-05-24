# AI Brand Identity Operating Guide

Guia operativa portable para gestionar proyectos de identidad visual con IA y dejar memoria reutilizable para futuros assets, implementaciones y produccion fisica.

Usala cuando quieras crear o mantener una identidad corporativa con ayuda de IA sin perder consistencia entre logos, tipografia, colores, prompts, mockups, web, social, Cricut, vinilos, packaging o futuras apps.

## Para Que Sirve

- Convierte una identidad visual en contexto legible por IA.
- Evita depender de un unico prompt o una imagen generada.
- Separa estrategia, exploracion visual, decisiones, assets finales y reglas de produccion.
- Permite copiar una base minima a otro proyecto y seguir trabajando con Codex u otros agentes.
- Mantiene trazabilidad entre fuentes, decisiones, prompts y archivos finales.

## Archivos

- [OPERATING_GUIDE.md](OPERATING_GUIDE.md): flujo operativo completo.
- [../../../templates/brand-ai-memory/](../../../templates/brand-ai-memory/): plantilla copiable para otro repo o proyecto.
- [../../../knowledge/processed/summaries/youtube-ai-brand-identity-2026-05-24.md](../../../knowledge/processed/summaries/youtube-ai-brand-identity-2026-05-24.md): investigacion base.
- [../../../knowledge/processed/insights/youtube-ai-brand-identity-memory-workflow.md](../../../knowledge/processed/insights/youtube-ai-brand-identity-memory-workflow.md): insight que origina esta guia.

## Uso Rapido En Otro Proyecto

1. Copia `templates/brand-ai-memory/brand/` al repo destino.
2. Llena `brand/brand-brief.md`.
3. Llena `brand/brand-memory.json` con los tokens y reglas aprobadas.
4. Guarda prompts reutilizables en `brand/prompts/`.
5. Guarda decisiones en `brand/decisions/`.
6. Guarda assets maestros en `brand/assets/logo/`.
7. Guarda exports de corte en `brand/assets/cricut/`.
8. Pide a Codex que lea `brand/README.md` antes de generar piezas nuevas.

## Prompt De Adopcion

```md
Quiero adoptar una guia AI ready para identidad corporativa en este proyecto.

Objetivo:
Crear o mantener una identidad visual con memoria reutilizable para IA: logo, tipografia, colores, prompts, reglas de uso, assets y exports para produccion.

Lee primero:
- AGENTS.md
- PROJECT_AI_PROFILE.md si existe
- brand/README.md si existe
- brand/brand-brief.md
- brand/brand-memory.json
- docs/ai/ai-brand-identity-operating-guide/OPERATING_GUIDE.md desde el repo de referencia

Trabaja en fases:
1. Diagnostica si ya existe identidad, assets, prompts, colores, fuentes y reglas.
2. Separa hechos verificados, supuestos, decisiones pendientes y riesgos.
3. Propone el minimo set de archivos `brand/` para este proyecto.
4. No cambies logo ni decisiones visuales principales sin aprobacion humana.
5. Si generas piezas nuevas, usa `brand-memory.json` como fuente de verdad.
6. Reporta validacion: visual, tecnica y produccion cuando aplique.

Entrega esperada:
- diagnostico breve;
- archivos creados o actualizados;
- decisiones que requieren aprobacion;
- checklist de validacion;
- riesgos restantes.
```

## Criterio Rapido

| Necesidad | Archivo |
|---|---|
| Entender la marca | `brand/brand-brief.md` |
| Dar contexto a IA | `brand/brand-memory.json` |
| Reusar prompts | `brand/prompts/*.md` |
| Registrar por que se eligio algo | `brand/decisions/*.md` |
| Guardar logos finales | `brand/assets/logo/` |
| Preparar Cricut/vinilo | `brand/assets/cricut/` |
| Validar produccion | `brand/production-checklist.md` |
