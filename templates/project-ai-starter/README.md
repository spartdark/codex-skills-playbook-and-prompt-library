# Project AI Starter

Portable starter files for a repo that should work well with Codex.

## Install Into Another Repo

Copy this folder's contents to the target repo root.

Then:

1. Fill `PROJECT_AI_PROFILE.md`.
2. Rename `knowledge/projects/_template/` to `knowledge/projects/<project-id>/`.
3. Update `AGENTS.md` if the project has special rules.
4. Add project-specific specs, decisions, and runbooks under `docs/`.

## Design

- `AGENTS.md` stays short and routes the agent.
- `PROJECT_AI_PROFILE.md` stores facts and commands.
- `knowledge/` stores durable memory and evidence.
- `docs/` stores specs, decisions, and runbooks.

Agents should read indexes first and raw evidence only when needed.
