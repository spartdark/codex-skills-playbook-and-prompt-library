# Manual Pre-Read Prompt

Source: [Spec-driven development: the AI engineering workflow at Notion](https://www.youtube.com/watch?v=pUHA_jNwuYE)

Confidence: inferred from transcript-backed workflow. The video describes the agent instructions at a high level, but the exact full prompt is not visible in the transcript. This file adapts the pattern to `ia-learning`.

## What The Video Shows

The Notion workflow uses a custom agent that:

- runs before a recurring meeting;
- looks back over recent activity;
- checks Slack, closed tasks, merged PRs, metrics and the previous meeting transcript;
- generates a pre-read;
- focuses the meeting on decisions, progress, bugs, feedback, open questions and risks;
- keeps permissions narrow;
- posts the result where the team works.

For this repo, run the same idea manually before automating it.

## Manual Weekly Pre-Read Prompt

Use this from the root of `/Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning`.

```md
Quiero un pre-read semanal manual para este proyecto antes de decidir qué hacer después.

Lee el repo y genera un brief en Markdown. No modifiques archivos todavía.

Periodo:
- Últimos 7 días desde la fecha actual.

Fuentes a revisar:
- `git status --short`
- `git log --since="7 days ago" --oneline --decorate`
- cambios recientes en `knowledge/projects/ia-learning/`
- `knowledge/projects/ia-learning/source-index.md`
- `knowledge/projects/ia-learning/experiments.md`
- `knowledge/projects/ia-learning/open-questions.md`
- `knowledge/projects/ia-learning/process-improvements.md`
- `knowledge/projects/ia-learning/implementation-patterns.md`
- archivos nuevos o modificados bajo `knowledge/raw/` y `knowledge/processed/`
- `package.json`, workspaces o servicios si cambiaron
- TODOs o FIXME si aparecen en el repo

Quiero que el pre-read tenga estas secciones:

1. Resumen ejecutivo
2. Cambios recientes
3. Fuentes nuevas o conocimiento agregado
4. Tareas abiertas o experimentos pendientes
5. Bugs, riesgos o inconsistencias detectadas
6. Decisiones pendientes
7. Próximos pasos recomendados
8. Validación sugerida
9. Preguntas abiertas

Reglas:
- Separa hechos, inferencias y recomendaciones.
- Cada claim importante debe apuntar a un archivo, comando, fuente o evidencia.
- Si algo no se puede verificar, márcalo como supuesto.
- No inventes métricas, bugs ni tareas.
- No implementes cambios.
- No edites `knowledge/` en esta pasada.
- Si encuentras cambios no relacionados o worktree sucio, repórtalo sin revertir nada.

Formato de salida:
- Markdown conciso.
- Máximo 1 pantalla larga.
- Prioriza acciones concretas.
- Incluye una lista final de 3 acciones recomendadas para la próxima sesión.
```

## Version That Writes The Brief

Use this only after you like the manual output above.

```md
Genera un pre-read semanal para `ia-learning` usando el prompt de
`knowledge/projects/ia-learning/manual-pre-read-prompt.md`.

Esta vez sí escribe el resultado en:

`knowledge/briefs/weekly/pre-read-YYYY-MM-DD.md`

Reemplaza `YYYY-MM-DD` por la fecha actual.

Después de escribirlo, devuelve:
- ruta del archivo creado;
- resumen de 5 bullets;
- 3 acciones recomendadas;
- cualquier evidencia faltante.

No modifiques otros archivos.
```

## Step-By-Step Execution

1. Abre Codex en este repo:

   ```txt
   /Users/vladimir.saldivar/Documents/IntelliJProyects/ia-learning
   ```

2. Pega el `Manual Weekly Pre-Read Prompt`.

3. Revisa el resultado en chat.

4. Si el resultado es útil, corre la `Version That Writes The Brief`.

5. Lee el archivo generado en `knowledge/briefs/weekly/`.

6. Escoge una de las 3 acciones recomendadas.

7. Si la acción implica implementación, crea primero una spec usando:

   ```txt
   knowledge/projects/ia-learning/spec-driven-development-context.md
   ```

8. Solo después de tener spec, pide implementación.

## Optional Future Automation

Once the manual brief is consistently useful, convert it into a weekly automation that writes to `knowledge/briefs/weekly/` and does not modify product code.
