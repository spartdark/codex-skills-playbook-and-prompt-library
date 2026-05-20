---
source_type: youtube_transcript_analysis
source_url: https://www.youtube.com/watch?v=pUHA_jNwuYE
video_id: pUHA_jNwuYE
source_title: "Spec-driven development: the AI engineering workflow at Notion | Ryan Nystrom"
channel: "How I AI"
captured_date: 2026-05-20
raw_evidence: ../../raw/youtube/ai-engineering-management-2026-05-20/youtube-transcript-how-i-ai-spec-driven-development-the-ai-engineering-workflow-at-notion-ryan-nystr-pUHA_jNwuYE-en.json
processed_evidence: ../transcripts/youtube-how-i-ai-notion-spec-driven-development-pUHA_jNwuYE-en-excerpts.md
confidence: verified source capture; English auto-captions not independently verified; timestamps should be checked before quoting exact wording
project_relevance: spec-driven development, engineering-management agents, background coding agents, CI and verification loops
---

# Notion Spec-Driven Development - Practical Guide

## Core Thesis

The video presents AI as an engineering operating layer, not just a coding assistant. The workflow moves human effort away from repetitive prep, status formatting and first-pass implementation, and toward architecture, prioritization, review, verification and live evidence.

The three main use cases are:

1. Automated meeting pre-reads from project signals.
2. Background coding agents launched from project tasks.
3. Specs stored in the repo as the source of truth for autonomous implementation.

## Step-by-Step Points From the Video

1. Create a project hub with docs, databases, meetings and measurable wins. Ryan shows a Notion project hub for a CI-speed project and tracks small improvements over time. Evidence: 06:12-06:36.
2. Replace low-value status standups with an AI-generated pre-read. A daily meeting template starts blank, then a custom agent fills it before the meeting. Evidence: 07:07-07:23.
3. Feed the agent real project signals from the last 24 hours: Slack discussion, closed Notion tasks, merged PRs and the previous meeting transcript. Evidence: 07:30-07:49.
4. Include live metrics and decision sections. The pre-read includes CI time, decisions, progress, bugs, feedback, open questions and concerns. Evidence: 08:01-08:18.
5. Use the meeting to discuss problems, decisions, wins, findings and next work, not to recite individual status. Evidence: 08:21-08:57.
6. Give the pre-read agent explicit instructions: purpose, time window, data sources, output format, writing style and Slack posting behavior. Evidence: 17:13-18:46.
7. Use subagents or a map-reduce pattern when the agent must inspect several sources, such as metrics, project channel, task database and prior meeting notes. Evidence: 17:34-18:17.
8. Keep permissions narrow. Ryan gives view access to shared project data and edit access only to the meeting page the agent writes. Evidence: 19:01-19:22.
9. Improve agent instructions by giving it examples, screenshots or queries and asking it to update its own instructions. Evidence: 19:52-20:20.
10. Optimize for reduced context switching, not only massive time savings. The example may save around 20 minutes per day, but the larger win is not reloading scattered project context manually. Evidence: 21:14-22:16.
11. Launch coding agents from project tasks. Ryan writes a short task, adds a screenshot and edge cases, then mentions Codex from the task/comment flow. Evidence: 25:30-28:19.
12. Run implementation in background infrastructure. Their internal tool launches coding agents in VMs and returns a pull request plus preview URL. Evidence: 26:30-28:40.
13. Require the agent to show verification. The PR includes testing notes and UI verification screenshots; follow-up comments handle type issues and CI failures. Evidence: 28:49-29:24.
14. Use blunt review prompts when unclear: say that you do not understand a change and ask the agent to explain or fix it. Evidence: 29:34-30:22.
15. For larger work, do not start with code. Start with a spec folder in the repo and Markdown spec files. Evidence: 32:11-33:08.
16. Dictate or write rough intent, then ask the agent to learn from existing specs and write a first spec draft. Revise the spec before building. Evidence: 33:24-33:59.
17. Point the coding agent at the spec and ask it to build. The spec should include code pointers and verification instructions. Evidence: 34:11-34:33.
18. Give agents runnable verification tools. Their workflow includes CLI tools that let the coding agent run Notion AI, send queries, toggle modes and inspect transcripts. Evidence: 34:36-34:53.
19. Treat the spec as source of truth and changelog. Update the spec first, then ask the agent to update the code from it. Evidence: 35:07-36:25 and 39:37-39:51.
20. Make engineering work more about systems thinking, architecture and verification loops. If verification is hazy, build the verification tool first. Evidence: 37:01-37:39.
21. Improve CI speed because slow CI caps the value of background agents. A one-hour loop makes agents wait; a three-minute loop enables much more throughput. Evidence: 44:10-44:56.
22. Challenge the agent to defend its reasoning with specific evidence, especially when you are outside your expertise. Evidence: 45:59-46:26.

## Implementation Guide For Your Own Projects

### 1. Create a Project Control Surface

Use one place where the project state lives. It can be Notion, GitHub issues, Linear, Markdown files or this repo's `knowledge/` folder.

Minimum structure:

- `docs/specs/` or `knowledge/projects/<project>/specs/`
- decision log
- open questions
- active experiments
- source index or evidence list
- validation commands
- meeting/pre-read notes

### 2. Build a Pre-Read Agent

Start manual before automating. Ask Codex to produce a daily or weekly pre-read from local signals.

Inputs:

- recent git commits and changed files
- open tasks/issues
- PRs or merge history
- test/CI status
- latest project notes
- metrics or logs if available
- prior meeting notes

Output sections:

- decisions needed
- progress since last readout
- risks and blockers
- bugs or failing checks
- open questions
- next recommended actions
- stale items that need closing

Guardrails:

- read-only access by default
- write only to the pre-read file/page
- every claim links to a file, PR, issue, metric or source
- label inferences clearly

### 3. Convert Tasks Into Agent-Ready Briefs

For any implementation task, write a compact brief before asking an agent to code.

Task brief template:

```md
# Task

## Goal

## User/problem

## Current behavior

## Desired behavior

## Scope

## Out of scope

## Files or areas likely involved

## Edge cases

## Acceptance criteria

## Verification commands

## Evidence to return
```

Attach screenshots or examples when UI or behavior matters.

### 4. Use Spec-Driven Development For Medium/Large Work

Create repo-owned specs, not disposable prompts.

Spec template:

```md
# Feature Spec

## Problem

## Goals

## Non-goals

## User flows

## System behavior

## Data/model changes

## API or integration changes

## UI states

## Edge cases

## Code pointers

## Rollout/migration plan

## Verification plan

## Open questions
```

Workflow:

1. Dictate or write rough intent.
2. Ask the agent to study nearby specs and draft the new spec.
3. Review and revise the spec.
4. Commit or save the spec.
5. Ask the agent to implement from the spec.
6. Review the diff, tests, screenshots and logs.
7. When requirements change, update the spec first.
8. Ask the agent to update implementation from the spec change.

### 5. Require Verification Evidence

Do not accept "done" without evidence.

Useful evidence:

- test command output
- typecheck/lint output
- CI result
- UI screenshot
- preview URL
- log excerpt
- observability query result
- explicit list of unverified assumptions

If the agent cannot verify the feature, the next task should often be: build the verification harness.

### 6. Improve Agent Throughput With DevX

The workflow depends on fast feedback.

Prioritize:

- fast local test commands
- isolated worktrees or VMs
- preview environments
- narrow CI jobs per task type
- scripts that reproduce important user flows
- clear failure logs

Slow validation turns background agents into idle workers.

### 7. Use Strong Review Prompts

Prompt patterns detected from the video:

- "I do not know what I am doing here. Explain it simply."
- "Write a spec from this rough description."
- "Build from this spec."
- "Update your instructions from this example/query/screenshot."
- "Defend your argument with specific evidence."
- "I do not understand this change. Explain why it is needed or fix it."

Do not treat these as exact quotes; the source is auto-captioned.

## Practical First Experiment For `ia-learning`

Run one manual version of the workflow:

1. Choose one medium feature or repo improvement.
2. Create a spec under `knowledge/projects/ia-learning/` or `docs/specs/`.
3. Include acceptance criteria and verification commands.
4. Ask Codex to implement only from that spec.
5. Require test or inspection evidence in the final response.
6. Update the spec with anything learned during implementation.
7. Add the result to `knowledge/projects/ia-learning/experiments.md`.

Success signal: the spec reduces clarification, improves review quality and leaves reusable project memory behind.

## Manual Pre-Read Process For Codex

This is the recommended first version before creating an automation. It adapts the video's daily Notion AI "Hot Potato" agent to a local Codex workflow.

### What The Video Suggests

The video's pre-read workflow is not a generic meeting summary. It is a just-in-time engineering-management briefing produced before the meeting so the human discussion can focus on decisions, risks, findings and next work.

The source workflow:

1. A meeting page/template is created on a schedule.
2. A custom agent runs shortly after the template is created.
3. The agent looks back over a fixed time window, usually the last 24 hours.
4. It fans out across project evidence: Slack discussion, closed tasks, merged pull requests, metrics and the prior meeting transcript.
5. It writes a structured pre-read into the meeting page.
6. It posts a short Slack notification linking to the pre-read.
7. The team uses the meeting to discuss problems, decisions, wins, findings and next work.

For `ia-learning`, the equivalent should start weekly rather than daily because the repo is still building its research and workflow foundation.

### How To Run It Manually

1. Define the window: "since the last pre-read" or "last 7 days".
2. Inspect repo activity: `git status`, recent commits, changed files, untracked files and package/config changes.
3. Inspect project memory: source index, experiments, process improvements, implementation patterns, agent workflows and open questions.
4. Inspect validation state: package scripts, available test/build commands, recent failures if present and missing verification hooks.
5. Synthesize only what changes action: do not produce a passive digest.
6. Separate verified evidence, inference and recommendation.
7. End with 3-5 next actions, each small enough for a Codex session.

### Recommended Output Format

```md
# Weekly Engineering Pre-Read

## Executive Summary

## Changes Since Last Review

## Decisions Needed

## Risks And Blockers

## Bugs Or Validation Gaps

## Open Questions

## Recommended Next Actions

## Evidence

## Assumptions And Missing Information
```

### Local Evidence Map

Use these local sources first:

- `git status --short`
- `git log --oneline --decorate --max-count=20`
- `package.json`
- `pnpm-workspace.yaml`
- `knowledge/projects/ia-learning/source-index.md`
- `knowledge/projects/ia-learning/experiments.md`
- `knowledge/projects/ia-learning/open-questions.md`
- `knowledge/projects/ia-learning/process-improvements.md`
- `knowledge/projects/ia-learning/implementation-patterns.md`
- `knowledge/projects/ia-learning/agent-workflows.md`
- `docs/skills/codex-practical-guide.md`
- `docs/skills/codex-prompt-briefs.md`

### Prompt Patterns To Reuse

These are prompt patterns supported by the video context. They are not exact reusable quotes unless verified against the video.

```md
I do not know what I am doing here. Explain it simply and point out the concrete things I need to understand.
```

Use when Codex is reasoning about unfamiliar CI, architecture, integrations or tooling.

```md
Review the last 7 days of project activity. Produce a pre-read focused on decisions, risks, progress, bugs, open questions and next actions. Link every claim to local evidence.
```

Use as the manual pre-read seed prompt.

```md
Update your instructions based on this example. Preserve the useful structure, remove noise and make future outputs easier to verify.
```

Use after a pre-read is manually corrected.

```md
Defend your recommendation with specific evidence. If the evidence is weak, mark it as an inference and propose the smallest validation step.
```

Use to fight shallow reassurance or overconfident planning.

```md
I do not understand this change or recommendation. Explain why it is necessary, what evidence supports it and what would break if we do not do it.
```

Use during review of the pre-read or a follow-up implementation.

## Codex Work Proposal: Weekly Manual Pre-Read

This proposal combines the official Codex guidance and the local Codex practical guide: give Codex a clear goal, repo context, success criteria, permission to inspect files and a reviewable output.

```md
# Codex Prompt Brief

## Objective

Create a manual weekly engineering pre-read for the `ia-learning` repo.

Do not implement code changes. Do not modify files. This is an analysis and planning task only.

## Context

This repo uses `knowledge/` as local project memory. The goal is to convert recent repo activity and research artifacts into a concise planning brief with evidence-backed next actions.

Use these references:

- `knowledge/raw/web/openai-codex-official-docs-2026-05-20.json`
- `docs/skills/codex-practical-guide.md`
- `docs/skills/codex-prompt-briefs.md`
- `knowledge/projects/ia-learning/source-index.md`
- `knowledge/projects/ia-learning/experiments.md`
- `knowledge/projects/ia-learning/open-questions.md`
- `knowledge/projects/ia-learning/process-improvements.md`
- `knowledge/projects/ia-learning/implementation-patterns.md`
- `knowledge/projects/ia-learning/agent-workflows.md`

## Scope

Include:

- recent git status and changed files;
- recent commits if available;
- new or stale knowledge artifacts;
- open experiments and process improvements;
- validation gaps;
- concrete next actions for the next Codex sessions.

Do not include:

- broad strategic brainstorming without evidence;
- implementation changes;
- automation setup yet;
- claims from external sources unless they are already saved under `knowledge/`.

## Verification

Run or inspect:

```bash
git status --short
git log --oneline --decorate --max-count=20
```

Inspect available validation commands in:

```bash
package.json
pnpm-workspace.yaml
```

If tests/build commands are obvious and cheap, report which should be run next. Do not run expensive or destructive commands.

## Output

Return a Markdown pre-read with:

1. Executive summary.
2. Changes since last review.
3. Decisions needed.
4. Risks and blockers.
5. Bugs or validation gaps.
6. Open questions.
7. Recommended next actions.
8. Evidence table.
9. Assumptions and missing information.

Rules:

- Mark each item as `verified`, `inferred` or `needs validation`.
- Every recommendation must point to a file, command, source artifact or explicit missing evidence.
- End with exactly 3 proposed Codex tasks. Each task must include objective, scope, acceptance criteria and verification command.
```

### When To Automate

Only automate this after 2-3 manual pre-reads produce useful decisions. The first automation should write a draft to `knowledge/briefs/weekly/` and avoid changing project decision files automatically.
