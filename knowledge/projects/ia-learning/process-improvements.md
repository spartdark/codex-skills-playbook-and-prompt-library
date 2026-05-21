# Process Improvements

Ideas for improving how this workspace researches, builds, validates, documents, or ships.

## Template

```md
## Improvement Name

- Source:
- Confidence:
- Current friction:
- Proposed change:
- Expected impact:
- Validation step:
```

## Source-to-Experiment Pipeline

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: verified
- Current friction: research summaries can become passive notes without driving implementation or validation.
- Proposed change: for each high-signal source, save raw evidence, normalized transcript, summary, insights, project links and at least one experiment with evidence pointer.
- Expected impact: makes `knowledge/` useful for future RAG and turns external learning into testable workflow improvements.
- Validation step: after three sources, inspect whether project files contain enough linked experiments to influence roadmap decisions.

## Multi-Agent Control Plane

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: inferred
- Current friction: parallel agent work can lose state, duplicate effort or finish without validation.
- Proposed change: maintain a small checklist with artifact, owner/chat, dependency, status, risk and validation step before launching multiple agent tasks.
- Expected impact: better orchestration for long-running work and clearer stop conditions.
- Validation step: use the checklist on the next multi-file or multi-artifact task and record cycle time plus rework.

## Transcript Failure Evidence Policy

- Source: [Riley Brown latest 10 videos](../../processed/summaries/youtube-riley-brown-channel-report-2026-05-19.md)
- Confidence: verified
- Current friction: channel-level reports can silently degrade when YouTube exposes caption tracks but transcript endpoints return empty responses or rate limits.
- Proposed change: always save per-video transcript error JSON next to successful transcripts and include a report section separating metadata-backed, transcript-backed, inferred, and recommended claims.
- Expected impact: prevents summaries from pretending to have transcript evidence and makes future retries/audits straightforward.
- Validation step: retry the Riley Brown source pack later with a working PO token or authorized cookies and compare the updated transcript-backed report against this metadata-only version.

## Codex PM Control Plane

- Source: [Codex and AI project management search](../../processed/summaries/youtube-codex-ai-project-management-2026-05-19.md)
- Confidence: inferred
- Current friction: AI coding work can move faster than project tracking, validation, and memory updates.
- Proposed change: use a single control-plane template for Codex-driven work with goal, spec, task owner, worktree/branch, files, validation command, status, risk, and memory update.
- Expected impact: makes AI-assisted software project management auditable instead of just conversational.
- Validation step: run one real `ia-learning` feature through the template and compare rework, missing context, and verification quality against an ad hoc Codex session.

## Codex Prompt Briefs

- Source: [OpenAI Codex official usage notes](../../processed/summaries/openai-codex-official-usage-guide-2026-05-20.md)
- Confidence: inferred
- Current friction: vague Codex prompts produce extra clarification rounds, uneven verification, and final answers that are hard to review.
- Proposed change: treat every meaningful Codex request as a small engineering brief with goal, repo area, constraints, acceptance criteria, verification command, and desired final artifact.
- Expected impact: makes local, app, and cloud Codex runs more reproducible and reduces rework.
- Validation step: apply the brief format to the next three implementation tasks and compare cycle time, test quality, and number of follow-up corrections.

## Engineering Manager Pre-Read

- Source: [AI for engineering management and software project administration](../../processed/summaries/youtube-ai-engineering-management-2026-05-20.md)
- Confidence: inferred
- Current friction: project decisions can be made from chat memory instead of a compact view of recent repo state, source evidence, experiments, and open questions.
- Proposed change: before weekly planning or a medium implementation task, generate a short pre-read from git status, recent commits, source-index changes, stale experiments, open questions, and missing validation evidence.
- Expected impact: better prioritization, fewer forgotten follow-ups, and clearer handoff from research into implementation.
- Validation step: run one manual pre-read for `ia-learning`, then record whether it changes the next three task priorities.

## Checked Harness For Source Intelligence

- Source: [BettaTech Harness Engineering](../../processed/summaries/youtube-bettatech-harness-engineering-q9Vaoz0hd0U-summary.md)
- Confidence: inferred from secondary summary; primary transcript unavailable.
- Current friction: source research currently depends on the agent remembering every step in `knowledge/README.md`.
- Proposed change: add a lightweight validator or checklist that checks high-signal sources have raw evidence, processed summary, confidence label, project link and at least one experiment or explicit "no experiment" note.
- Expected impact: fewer passive summaries, less risk of ungrounded claims, and cleaner future RAG indexing.
- Validation step: run the validator/checklist on the next three YouTube or Reddit sources and record missing fields.
