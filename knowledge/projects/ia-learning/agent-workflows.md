# Agent Workflows

Reusable operating patterns for Codex, plugins, skills, and multi-agent work in this repo.

## Workflow Template

```md
## Workflow Name

- Source:
- Confidence:
- Use when:
- Project folder:
- Inputs:
- Agent lanes:
- Artifacts:
- Validation:
- Memory update:
- Risks:
```

## Source Intelligence Workflow

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: verified
- Use when: analyzing YouTube, Reddit, docs, articles, AI tooling updates, or implementation references.
- Project folder: `knowledge/`
- Inputs: source URL, transcript/export, user objective, project relevance.
- Agent lanes: capture raw evidence; normalize source; analyze with the relevant researcher skill; extract insights; link to project memory.
- Artifacts: raw payload, normalized transcript/thread, summary, insight, source-index row, project links.
- Validation: source URL resolves; raw evidence is preserved; summary includes confidence and evidence pointers; project files link back to processed artifacts.
- Memory update: update `source-index.md`, plus relevant project memory files.
- Risks: summaries becoming treated as primary evidence; transcripts missing visual context; auto-captions introducing errors.

## Multi-Agent Launch Workflow

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: inferred
- Use when: turning an idea into multiple coordinated artifacts such as app, landing, deck, video, waitlist, or automation.
- Project folder: one folder per initiative under the relevant app/docs area, with derived memory under `knowledge/`.
- Inputs: idea brief, target user, artifact list, validation criteria.
- Agent lanes: product spec; implementation; landing/waitlist; supporting assets; automation; QA.
- Artifacts: checklist, generated files, deploy/test links, screenshots or validation notes, memory update.
- Validation: run the app, open deploy preview, submit test form, inspect generated document, or run API smoke test.
- Memory update: record reusable implementation/process patterns and open questions.
- Risks: parallel work without state tracking; unvalidated "done" claims; secrets pasted into prompts.

## Codex PM Control Plane

- Source: [Codex and AI project management search](../../processed/summaries/youtube-codex-ai-project-management-2026-05-19.md)
- Confidence: inferred
- Use when: coordinating Codex, subagents, worktrees, GitHub issues, specs, automations, and validation across a software project.
- Project folder: project repo root plus `knowledge/` for research and decisions.
- Inputs: goal, requirements/spec, task list or issue, relevant files, owner/agent lane, validation command, risk level.
- Agent lanes: planner/spec writer; implementation worker; reviewer/tester; project hygiene automation; memory curator.
- Artifacts: spec, task checklist, branch/worktree notes, test output, review notes, source-index or project-memory update.
- Validation: every lane must produce either passing verification evidence or an explicit blocker with next action.
- Memory update: summarize reusable patterns in `knowledge/projects/ia-learning/` and preserve raw source evidence when external content influenced the decision.
- Risks: vague tasks, hidden dependencies, duplicated work across agents, missing acceptance criteria, and treating generated summaries as primary evidence.

## Agent Harness Task Contract

- Source: [BettaTech Harness Engineering](../../processed/summaries/youtube-bettatech-harness-engineering-q9Vaoz0hd0U-summary.md)
- Confidence: inferred from secondary summary; primary transcript unavailable.
- Use when: running a meaningful Codex/subagent task where context, file scope, tool permissions or validation evidence matter.
- Project folder: repo root plus `knowledge/` for source-backed memory.
- Inputs: objective, non-objectives, allowed files, relevant docs, allowed tools, validation command, memory files to update, escalation criteria.
- Agent lanes: orchestrator owns task contract and final evidence; worker implements within scope; reviewer verifies tests/diff/evidence; memory curator updates `knowledge/`.
- Artifacts: task contract, changed files or research artifacts, validation output, final summary, project-memory links.
- Validation: task is not complete until it has an explicit evidence pointer such as test output, raw source, screenshot, diff review or documented blocker.
- Memory update: save reusable lessons as implementation pattern, process improvement or experiment.
- Risks: over-structuring small tasks; using generated summaries as if they were transcripts; adding too many specialized tools before measuring whether primitives work.

## Codex Project Operating Loop

- Source: [Master 97% of Codex in 1 Hour](../../processed/summaries/youtube-nate-herk-master-97-codex-3TdD8Qv5Tk8-summary.md)
- Confidence: inferred from secondary summaries; primary transcript unavailable.
- Use when: turning a repeatable Codex workflow into a durable project, skill, dashboard, deploy or automation.
- Project folder: one folder per workflow, plus `knowledge/` for source evidence and decisions.
- Inputs: objective, source/data API, expected output artifact, skill candidate, deploy target, QA checklist and automation cadence.
- Agent lanes: setup/API lane; analysis lane; artifact/dashboard lane; skill extraction lane; deploy lane; browser QA lane; automation lane.
- Artifacts: local project folder, `.env` excluded from git, data output, workbook or dashboard, skill/instructions file, deploy URL, QA notes, automation config and memory update.
- Validation: first run is manual; automation starts only after the output artifact passes at least one QA cycle.
- Memory update: record the workflow as manual run -> skill -> automation, with raw evidence and failure notes.
- Risks: automating unverified outputs, exposing API keys, dashboard polish hiding weak data quality, and treating secondary summaries as primary transcript evidence.

## Engineering Manager Pre-Read

- Source: [AI for engineering management and software project administration](../../processed/summaries/youtube-ai-engineering-management-2026-05-20.md)
- Confidence: inferred
- Use when: preparing weekly planning, deciding what to build next, or starting a medium/high-risk implementation task.
- Project folder: `knowledge/projects/ia-learning/`
- Inputs: git status, recent commits, source index, experiments, open questions, process improvements, validation outputs, and new raw sources.
- Agent lanes: signal collector; evidence checker; priority synthesizer; task drafter.
- Artifacts: short pre-read with decisions needed, stale items, missing evidence, validation gaps, and recommended next actions.
- Validation: each recommendation links to a file, source URL, command output, or explicit inference label.
- Memory update: append accepted improvements or experiments to project memory and update source-index if new evidence was used.
- Risks: noisy summaries, treating inferred priorities as facts, and over-automating planning before the signal set is stable.
