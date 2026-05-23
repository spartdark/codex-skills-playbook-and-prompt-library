# AI Governance For Portable Project Starts

This document defines how this repository should be used as a starting point for new or existing projects that will be managed with Codex.

The goal is not to force a process. The goal is to give the AI a small, stable operating surface so it can work with less context, better continuity, and clearer validation.

## Governance Contract

Every adopted project should have:

- `AGENTS.md`: the first file an AI agent reads.
- `PROJECT_AI_PROFILE.md`: project facts, commands, constraints, and definition of done.
- `knowledge/README.md`: memory rules.
- `knowledge/projects/<project-id>/`: project-specific durable memory.
- `docs/`: specs, decisions, runbooks, and product/engineering documents.
- optional `skills/`: installable agent workflows when the project has repeatable expert behavior.
- optional `plugins/`: packaged capabilities when skills need scripts, tools, or integrations.

Keep `AGENTS.md` short. It should route the agent to the right file instead of containing all knowledge.

## Load Order

Use this order to minimize token use:

1. Read `AGENTS.md`.
2. Read `PROJECT_AI_PROFILE.md` when the task touches project behavior, commands, stack, or constraints.
3. Read the nearest relevant spec, decision, or runbook.
4. Read memory indexes before raw evidence.
5. Read raw sources only when exact evidence is needed.

## Project Memory Model

Use the filesystem as durable memory:

```txt
knowledge/
  README.md
  raw/
  processed/
  projects/<project-id>/
    README.md
    source-index.md
    decisions.md
    open-questions.md
    experiments.md
    validation.md
```

The chat can coordinate work, but durable decisions and reusable learnings must be written to files.

## Reusable Asset Lifecycle

Use this promotion path:

```txt
raw signal -> processed knowledge -> project memory -> docs/templates -> skill -> plugin
```

Do not skip directly from a single idea to a plugin unless the user explicitly asks for a packaged capability.

| Stage | Use When | Artifact |
|---|---|---|
| Raw signal | source evidence matters | `knowledge/raw/` |
| Processed knowledge | source has been normalized or summarized | `knowledge/processed/` |
| Project memory | learning affects this project | `knowledge/projects/<project-id>/` |
| Docs/templates | process is reusable across projects | `docs/`, `templates/` |
| Skill | Codex should execute the workflow repeatedly | `skills/<skill-name>/` |
| Plugin | capability needs packaging, scripts, tools, or integrations | `plugins/<plugin-name>/` |

Before promoting an asset, check:

- Is the workflow repeated at least twice or clearly expected to repeat?
- Is there evidence or validation behind it?
- Can Codex use it without loading excessive context?
- Is the expected input, output, and done condition clear?
- Does this belong in an existing skill/plugin instead of a new one?

Track candidates in `knowledge/projects/<project-id>/reuse-backlog.md`.

## When To Create A Spec

Create or update a spec before implementation when:

- the request is ambiguous;
- multiple files or domains are involved;
- product behavior changes;
- external APIs, data models, auth, payments, deployment, or security are involved;
- validation is unclear;
- the work will be reused or automated.

For small changes, use a compact task contract in chat:

```txt
Objective:
Scope:
Validation:
Evidence:
Done when:
```

## Evidence Rules

- Source summaries are not primary evidence.
- Preserve URLs, timestamps, raw exports, command outputs, screenshots, or test logs when they matter.
- Separate `verified`, `inferred`, `experimental`, and `unverified` claims.
- Promote repeated learnings into docs, templates, scripts, skills, or plugins.

## Token Budget Rules

- Prefer indexes, summaries, and project profiles before long documents.
- Do not load entire transcript or raw-source folders unless the task requires quotes or source verification.
- Use targeted search before broad reading.
- Keep memory files concise and append only reusable information.
- Archive or summarize stale material instead of expanding active files indefinitely.

## Adoption Workflow

1. Copy `templates/project-ai-starter/` to the target repo root.
2. Rename `knowledge/projects/_template/` to match the project id.
3. Fill `PROJECT_AI_PROFILE.md`.
4. Add project commands and sensitive areas.
5. Ask Codex to run an initial repo scan and update only the project profile, open questions, and validation commands.
6. Add a `reuse-backlog.md` if the project will grow reusable knowledge, skills, or plugins.
7. Start new features from a task contract or spec.

## Definition Of Done For AI Work

A task is done when:

- the requested output exists;
- scope changes are called out;
- validation has been run or explicitly blocked;
- durable decisions or reusable learnings are saved;
- the final response lists changed files and residual risk.
