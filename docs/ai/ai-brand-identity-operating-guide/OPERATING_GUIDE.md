# AI Brand Identity Operating Guide

Guia operativa para crear, evolucionar y reutilizar una identidad corporativa con IA, manteniendo contexto persistente para agentes y archivos listos para produccion.

## Proposito

El objetivo no es que la IA "haga un logo" y termine el proyecto. El objetivo es construir un sistema de identidad que la IA pueda leer, respetar y reutilizar.

La ruta recomendada es:

```txt
brief -> exploracion -> direccion aprobada -> refinamiento -> brand memory -> assets -> validacion -> reutilizacion
```

## Principios

1. La estrategia va antes que la imagen.
2. Un logo no es una identidad corporativa.
3. La IA explora rapido, pero una persona aprueba direccion, legibilidad, derechos y produccion.
4. El archivo de memoria es la fuente de verdad para futuros prompts.
5. Los assets finales deben existir como archivos, no solo como capturas o links.
6. Cricut, vinilo, impresion y web tienen constraints diferentes.
7. Cada decision importante debe quedar escrita para que otro agente no reinvente la marca.

## Estructura Recomendada

```txt
brand/
  README.md
  brand-brief.md
  brand-memory.json
  production-checklist.md
  prompts/
    logo-exploration.md
    typography.md
    mockups.md
  decisions/
    0001-direction-selection.md
  assets/
    logo/
      .gitkeep
    cricut/
      .gitkeep
    references/
      .gitkeep
```

## Load Order Para Agentes

Cuando Codex u otro agente trabaje en piezas de marca, debe leer solo lo necesario:

1. `brand/README.md`
2. `brand/brand-memory.json`
3. `brand/brand-brief.md` si el trabajo toca estrategia, audiencia o tono.
4. `brand/production-checklist.md` si el trabajo toca Cricut, vinilo, impresion o packaging.
5. La decision especifica en `brand/decisions/` si esta modificando una direccion ya aprobada.
6. Assets especificos en `brand/assets/` solo cuando necesita inspeccionar o editar archivos.

## Fase 1 - Brief

Llena `brand/brand-brief.md` antes de generar imagenes.

Minimo requerido:

- nombre de marca;
- descripcion del negocio;
- audiencia;
- objetivo de la identidad;
- personalidad;
- tono verbal;
- usos esperados;
- restricciones;
- competidores o referencias;
- decisiones que requieren aprobacion humana.

No avanzar a produccion si no esta claro:

- donde se usara la marca;
- si necesita funcionar en una tinta;
- si necesita corte en vinilo;
- si necesita registrar marca;
- si el nombre y simbolo pueden tener conflictos legales.

## Fase 2 - Exploracion Con IA

Usa IA para generar direcciones, no para decidir el resultado final.

Prompt base:

```md
Actua como director de identidad visual.

Contexto de marca:
- Nombre:
- Audiencia:
- Personalidad:
- Valores:
- Usos principales:
- Restricciones:

Genera 5 territorios visuales distintos.
Para cada territorio incluye:
- concepto;
- tipo de logo recomendado: wordmark, lettermark, symbol, combination, badge;
- paleta tentativa;
- tipografia sugerida;
- estilo de imagen;
- riesgos;
- prompt para generar moodboard o logo mark.

Separa claramente recomendaciones de supuestos.
```

Reglas:

- Para Midjourney o generadores similares, pedir `icon`, `mark`, `badge` o `symbol` cuando no se quiera texto roto.
- Para wordmarks y tipografia final, preferir Figma, Illustrator, Affinity, Kittl, Recraft u otra herramienta vectorial.
- Guardar prompts buenos en `brand/prompts/`.
- Guardar exploraciones aprobadas y rechazadas en `brand/decisions/`.

## Fase 3 - Seleccion De Direccion

Antes de refinar, crear una decision:

```md
# 0001 Direction Selection

- Date:
- Status: proposed | approved | rejected | superseded
- Selected direction:
- Why selected:
- Rejected directions:
- Risks:
- Required changes:
- Approved by:
- Evidence/assets:
```

Una direccion aprobada debe responder:

- que concepto representa;
- que debe evitarse;
- que elementos son obligatorios;
- que elementos son opcionales;
- como se vera en una tinta;
- como se vera en tamano pequeno.

## Fase 4 - Refinamiento

Convertir la direccion en assets reales.

Checklist:

- logo principal vectorial;
- version horizontal;
- version vertical o apilada si aplica;
- icono/simbolo aislado;
- una tinta;
- reversed/light-on-dark;
- PNG transparente para usos rapidos;
- SVG limpio para web;
- SVG plano para Cricut/vinilo si aplica.

Reglas de refinamiento:

- No usar texto generado por IA como tipografia final sin recrearlo.
- Convertir texto a contornos antes de exportar archivos de corte.
- Simplificar detalles pequenos para vinilo.
- Evitar sombras, texturas, gradientes y detalles fotograficos en archivos de corte.
- Revisar legibilidad a tamanos pequenos.
- Validar contraste si se usara en web o UI.

## Fase 5 - Brand Memory

Actualizar `brand/brand-memory.json` cuando una decision este aprobada.

La memoria debe contener:

- datos de marca;
- personalidad y tono;
- rutas de assets aprobados;
- colores con nombres, HEX y uso;
- tipografia y fallbacks;
- prompts aprobados;
- prompts negativos;
- estilos prohibidos;
- reglas de produccion;
- decisiones pendientes.

No guardar exploraciones dudosas como si fueran verdad. Usa:

- `approved` para decisiones validadas;
- `candidate` para ideas prometedoras;
- `rejected` para direcciones descartadas;
- `unknown` para informacion faltante.

## Fase 6 - Produccion Cricut, Vinilo E Impresion

Para Cricut/vinilo, el asset ideal suele ser un SVG con paths limpios y colores planos.

Reglas:

- Usar SVG para corte vectorial.
- Usar PNG/JPG para Print Then Cut si hay textura, foto, gradiente o efectos raster.
- Convertir texto a contornos.
- Expandir strokes.
- Unir o separar paths segun las capas de vinilo.
- Eliminar clipping masks complejas.
- Evitar pattern fills.
- Probar upload en Cricut Design Space antes de entregar.

Export recomendado:

```txt
brand/assets/cricut/
  logo-cut-one-color.svg
  logo-cut-layered.svg
  logo-print-then-cut.png
```

## Fase 7 - Reutilizacion

Cuando se pidan futuras piezas:

1. Leer `brand-memory.json`.
2. Confirmar el canal: web, app, social, print, vinyl, packaging, signage.
3. Usar los assets aprobados.
4. Usar prompts aprobados como base.
5. Registrar cualquier decision nueva.
6. Actualizar memoria solo si el aprendizaje sera reutilizable.

Prompt para generar una pieza nueva:

```md
Usa la identidad en `brand/brand-memory.json` como fuente de verdad.

Objetivo:
Crear una pieza de marca para:

Canal:
Formato:
Dimensiones:
Uso:
Restricciones de produccion:

Antes de generar, lista:
- assets que vas a usar;
- tokens de color y tipografia;
- riesgos;
- validacion necesaria.

No inventes nuevos colores, tipografias o estilos salvo que lo marques como propuesta.
```

## Validacion

### Visual

- El logo se reconoce en pequeno.
- La version de una tinta funciona.
- Hay contraste suficiente.
- La tipografia es legible.
- No parece una marca generica de IA.

### Tecnica

- SVG abre en navegador o herramienta vectorial.
- PNG tiene fondo transparente cuando aplica.
- Colores coinciden con `brand-memory.json`.
- Nombres de archivos son estables.
- Assets finales estan referenciados desde `brand-memory.json`.

### Produccion

- SVG de corte no contiene texto editable.
- SVG de corte no contiene pattern fills, gradientes o raster embebido.
- Strokes estan expandidos si el grosor importa.
- Capas estan separadas por color si habra vinilo por capas.
- Se probo import en Cricut Design Space cuando sea posible.

## Done Condition

Un proyecto de identidad esta listo para reutilizacion IA cuando:

- `brand/brand-brief.md` esta completo;
- `brand/brand-memory.json` tiene tokens y assets aprobados;
- hay al menos un logo maestro y una version de una tinta;
- las decisiones principales estan en `brand/decisions/`;
- los prompts reutilizables estan en `brand/prompts/`;
- la validacion realizada esta registrada;
- riesgos y pendientes estan explicitamente marcados.
