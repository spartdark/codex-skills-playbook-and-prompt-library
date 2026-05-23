# AGENTS.md

Token-light instructions for AI agents in this project.

## First Read

1. `AGENTS.md`
2. `PROJECT_AI_PROFILE.md`
3. `knowledge/README.md`
4. `knowledge/projects/<project-id>/README.md`
5. Relevant specs, decisions, or runbooks only when needed

Avoid bulk-reading raw sources, generated files, build outputs, or dependency folders.

## Working Rules

- Start from a clear objective, scope, validation path, and done condition.
- Read local context before changing code or docs.
- Keep changes small and aligned with existing patterns.
- Ask before broad architecture, security, credential, billing, production, or automation decisions.
- Treat chat as coordination and files as durable memory.
- Update memory only for decisions, reusable learnings, experiments, or open questions.
- Always report validation performed, or explain why it was not possible.

## Memory Routing

- Project profile: `PROJECT_AI_PROFILE.md`
- Memory contract: `knowledge/README.md`
- Project memory: `knowledge/projects/<project-id>/`
- Specs and runbooks: `docs/`
- Source evidence: `knowledge/raw/`
- Processed research: `knowledge/processed/`
- Reuse candidates: `knowledge/projects/<project-id>/reuse-backlog.md`

## Reuse Promotion

- Keep evidence and early ideas in `knowledge/`.
- Move repeated processes to `docs/` or `templates/`.
- Create a `skills/` asset only for repeatable agent behavior.
- Create a `plugins/` asset only when packaging, scripts, tools, or integrations are needed.

## Compact Task Contract

Use this for non-trivial work:

```txt
Objective:
Scope:
Validation:
Evidence:
Done when:
```
