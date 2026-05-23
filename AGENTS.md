# AGENTS.md

Token-light operating instructions for AI agents working in this repository.

## Mission

This repo is a portable AI operating playbook. Its purpose is to help Codex and other agents start new or existing projects with clear memory, specs, validation, source evidence, and low-context workflows.

This repo has three reusable asset types:

- `knowledge/`: growing evidence, insights, experiments, and project memory.
- `skills/`: installable agent behaviors for repeatable expert workflows.
- `plugins/`: packaged capabilities that may include skills, tools, scripts, or external integrations.

## Read Order

Read only what is needed for the task.

1. `AGENTS.md` - stable agent rules and routing.
2. `README.md` - public repo purpose and installable assets.
3. `docs/ai/governance.md` - how to adopt this repo in another project.
4. `knowledge/README.md` - memory contract and evidence lifecycle.
5. `knowledge/projects/ia-learning/source-index.md` - source registry when research evidence matters.
6. `knowledge/projects/ia-learning/reuse-backlog.md` - reusable candidates for future docs, templates, skills, or plugins.
7. Specific skill or plugin `SKILL.md` files only when the task clearly matches that asset.

Do not bulk-read `knowledge/raw/`, `knowledge/processed/`, transcripts, or plugin folders unless the task requires source-level evidence.

## Operating Rules

- Prefer small, explicit task contracts: objective, scope, validation, evidence, done condition.
- Keep context narrow. Read indexes and summaries before raw sources.
- Treat chat as coordination and files as durable memory.
- Preserve evidence for research, product, architecture, and process claims.
- Mark assumptions, inferred claims, experimental ideas, and verified facts separately.
- Update memory only when the learning is reusable.
- Promote reusable work deliberately: knowledge -> docs/templates -> skill -> plugin.
- For implementation work, follow existing repo patterns and keep diffs scoped.
- Always report validation performed, or state why validation was not possible.

## Memory Routing

- Durable project memory: `knowledge/projects/ia-learning/`
- Source evidence: `knowledge/raw/`
- Normalized source outputs: `knowledge/processed/`
- Reusable project docs: `docs/`
- Installable agent capabilities: `skills/`
- Packaged integrations/capabilities: `plugins/`
- Portable starter files for new repos: `templates/project-ai-starter/`

## Reuse Promotion

Use the smallest durable asset that fits:

- Save as `knowledge/` when it is evidence, an insight, an experiment, or an open question.
- Promote to `docs/` or `templates/` when it becomes a reusable process or project starter.
- Promote to `skills/` when Codex should repeatedly follow the same expert workflow.
- Promote to `plugins/` when a workflow needs packaging, bundled skills, scripts, tools, or integrations.

Record candidates in `knowledge/projects/ia-learning/reuse-backlog.md` before creating broad new assets.

## Adoption In Another Repo

When this repository is used as a starting point for another project:

1. Copy `templates/project-ai-starter/` into the target repo.
2. Rename `knowledge/projects/_template/` to `knowledge/projects/<project-id>/`.
3. Fill `PROJECT_AI_PROFILE.md`.
4. Add the target repo's build, test, lint, and dev-server commands.
5. Keep `AGENTS.md` short. Put detail in linked docs.

## Escalation

Ask the user before making broad product, architecture, security, credential, billing, deployment, or automation decisions. For small reversible edits, proceed with clear validation.
