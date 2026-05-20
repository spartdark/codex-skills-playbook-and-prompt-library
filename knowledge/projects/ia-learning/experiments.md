# Experiments

Validation tasks derived from source research and implementation work.

## Experiment Template

```md
## Experiment Name

- Source:
- Confidence:
- Hypothesis:
- User/problem:
- Smallest test:
- Success signal:
- Failure signal:
- Evidence to capture:
- Status: planned|running|done|dropped
```

## Source-To-Experiment Pipeline

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: inferred
- Hypothesis: research is more useful when every high-signal source creates at least one testable experiment.
- User/problem: `ia-learning` needs external learning to become implementation decisions, not passive summaries.
- Smallest test: process three sources through `raw -> processed -> insights -> project links -> experiment` and review whether they changed backlog priorities.
- Success signal: each source has a clear source-index row, at least one insight, and at least one project decision or rejected hypothesis.
- Failure signal: summaries accumulate without changing docs, backlog, experiments, or implementation.
- Evidence to capture: source-index rows, experiment outcomes, linked PRDs/backlog changes.
- Status: planned

## YouTube Channel Monthly Report

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: experimental
- Hypothesis: a channel-level reporter can identify useful AI/product/workflow patterns faster than manually watching every video.
- User/problem: `ia-learning` needs recurring discovery from AI YouTube channels without losing evidence traceability.
- Smallest test: use `youtube-channel-reporter` on one channel for the last 10 videos, then analyze the source pack with `youtube-ai-researcher`.
- Success signal: report produces at least three actionable insights with source links and one validated workflow improvement.
- Failure signal: transcript failures or weak summaries make the report less useful than manual selection.
- Evidence to capture: source pack JSON/Markdown, normalized transcripts, summary, insights, project links.
- Status: planned

## AI Marketing Team With Codex Skills

- Source: [Riley Brown latest 10 videos](../../processed/summaries/youtube-riley-brown-channel-report-2026-05-19.md)
- Confidence: inferred
- Hypothesis: role-specific agent/skill packs are easier to validate than broad "AI productivity" workflows.
- User/problem: solo founders need concrete launch assets without coordinating many disconnected tools.
- Smallest test: define 5 Codex skills/agents for one product idea: positioning, landing copy, competitive scan, email sequence, and launch checklist.
- Success signal: a usable artifact set exists with fewer than two manual rewrite passes and all claims are traceable.
- Failure signal: outputs remain generic, require heavy editing, or cannot be reused on a second idea.
- Evidence to capture: prompts, generated artifacts, manual edit log, elapsed time, quality notes.
- Status: planned

## Thirty-Minute Operator Quickstart

- Source: [Riley Brown latest 10 videos](../../processed/summaries/youtube-riley-brown-channel-report-2026-05-19.md)
- Confidence: inferred
- Hypothesis: `ia-learning` workflows will be adopted faster if each one has a "learn 95% in 30 minutes" path ending in durable `knowledge/` artifacts.
- User/problem: research workflows are powerful but easy to forget when they require many conventions.
- Smallest test: create a 30-minute quickstart for YouTube research that produces `raw`, `processed`, `projects/ia-learning`, and source-index updates.
- Success signal: a fresh session can complete the workflow without extra explanation.
- Failure signal: the quickstart omits evidence fields, produces passive summaries, or requires manual convention lookup.
- Evidence to capture: quickstart doc, completed sample report, missing-step notes.
- Status: planned

## Codex PM Control Plane Trial

- Source: [Codex and AI project management search](../../processed/summaries/youtube-codex-ai-project-management-2026-05-19.md)
- Confidence: inferred
- Hypothesis: Codex-driven project work improves when every task is tracked through a compact control plane with spec, owner, files, validation, and memory update.
- User/problem: `ia-learning` needs AI agents to support software project management without losing traceability or shipping unvalidated changes.
- Smallest test: choose one small feature or research-to-implementation task, create a control-plane checklist, execute with Codex, and record validation evidence.
- Success signal: task finishes with clear acceptance criteria, passing verification, updated project memory, and fewer unresolved context gaps than a normal chat-only workflow.
- Failure signal: the checklist becomes overhead, misses important dependencies, or fails to prevent rework.
- Evidence to capture: checklist, changed files, command outputs, final validation notes, and a short post-run improvement.
- Status: planned

## Engineering Manager Pre-Read Trial

- Source: [AI for engineering management and software project administration](../../processed/summaries/youtube-ai-engineering-management-2026-05-20.md)
- Confidence: experimental
- Hypothesis: a compact AI-generated pre-read will make `ia-learning` planning more reliable by surfacing stale sources, experiments, open questions, and validation gaps before work starts.
- User/problem: a solo builder or small team needs engineering-management context without manually scanning every project memory file.
- Smallest test: generate one pre-read from git status, recent commits, `knowledge/projects/ia-learning/source-index.md`, `experiments.md`, `open-questions.md`, and recent raw sources.
- Success signal: the pre-read identifies at least three actionable next steps, one stale item, or one missing evidence link that changes the work plan.
- Failure signal: the pre-read repeats obvious information, misses important project state, or creates more review work than it saves.
- Evidence to capture: generated pre-read, changed priorities, manual corrections, elapsed time, and follow-up tasks.
- Status: planned
