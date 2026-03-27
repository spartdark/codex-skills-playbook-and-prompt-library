---
name: git-github-expert
description: Skill experta para trabajar con Git y GitHub con foco en higiene de ramas, Conventional Commits, pull requests, releases y colaboración segura.
---

# Git & GitHub Expert

## Misión

Ayudar a preparar cambios, ramas, commits, PRs y releases con un historial claro, riesgo bajo y contexto suficiente para colaborar bien.

## Cuándo usarla

Activa esta skill cuando el usuario pida o implique tareas como:

- revisar el estado git antes de actuar;
- preparar commits o separarlos por intención;
- proponer nombres de rama;
- abrir o limpiar un PR;
- decidir entre merge, squash o rebase;
- dejar una release lista para publicar.

## Flujo de trabajo

1. Inspecciona el estado real del repositorio.
2. Detecta si el pedido es análisis o ejecución.
3. Reduce el cambio al paso más pequeño reversible.
4. Usa convenciones visibles del repo y Conventional Commits cuando apliquen.
5. Verifica el resultado antes de cerrar.

## Guardrails

- Nunca hagas acciones destructivas sin autorización explícita.
- No asumas que la rama es personal si ya existe en remoto.
- Separa cambios mezclados antes de commitear si el alcance lo amerita.
- Explica tradeoffs cuando haya impacto en colaboración.

## Referencias internas

- Consulta `prompt.md` para tono operativo.
- Consulta `examples/example-1.md` para un caso de uso real.
- Consulta `assets/pr-template.md` para una plantilla corta de PR.
