# Implementation Patterns

Reusable technical patterns discovered from YouTube, Reddit, docs, experiments, or project work.

## Template

```md
## Pattern Name

- Source:
- Confidence:
- Applies to:
- Problem:
- Pattern:
- Tradeoffs:
- Next experiment:
```

## Project Folder as Agent Artifact Boundary

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: verified
- Applies to: `knowledge/`, local experiments, generated docs/apps, RAG source capture
- Problem: agent work gets fragmented across chats unless generated artifacts live in a durable project location.
- Pattern: create or select a folder before delegating work; keep outputs, source evidence, normalized transcripts and derived notes under that boundary; mention prior files when asking follow-up agents to update or audit them.
- Tradeoffs: folder discipline adds overhead, but improves traceability and future indexing.
- Next experiment: add a lightweight `agent-workflows.md` control plane for one `ia-learning` experiment and compare it against ad hoc chat-only work.

## Skill Factory for Missing Integrations

- Source: [Codex Full Course 2026](../../processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md)
- Confidence: inferred
- Applies to: API integrations, Codex skills, local automations
- Problem: many useful tools will not have official plugins at the moment they are needed.
- Pattern: first check for an official plugin/skill; if absent, ask the agent to inspect current API docs, create a narrow local skill, keep secrets out of source, and run a smoke test before using it in automations.
- Tradeoffs: faster capability creation, but higher safety burden around API keys, permissions and unintended external actions.
- Next experiment: create a non-sensitive sample skill with mock credentials and document a review checklist before touching real external APIs.

## Official API Boundary for MCP Wrappers

- Source: [NotebookLM Enterprise MCP API scope](../../processed/summaries/notebooklm-enterprise-mcp-api-scope-2026-05-20.md)
- Confidence: verified
- Applies to: `services/notebooklm-mcp`, future Google Cloud service wrappers
- Problem: web apps often have unofficial internal APIs, but MCP tools become operational dependencies and should not rely on brittle reverse engineered calls when an official enterprise API exists.
- Pattern: map MCP tools only to documented API methods, expose unsupported gaps explicitly, and keep authentication delegated to the provider's supported OAuth/ADC flow.
- Tradeoffs: the first version may omit desirable UI features such as NotebookLM personal chat, but it is easier to maintain and safer to automate.
- Next experiment: validate `services/notebooklm-mcp` against a real NotebookLM Enterprise project and capture the minimum IAM roles needed for each tool.

## Harness Task Contract

- Source: [BettaTech Harness Engineering](../../processed/summaries/youtube-bettatech-harness-engineering-q9Vaoz0hd0U-summary.md)
- Confidence: inferred from secondary summary; transcript extraction failed.
- Applies to: Codex runs, subagent orchestration, research pipelines, RAG memory updates.
- Problem: agents degrade when context is long-lived, tools are ambiguous, memory is implicit and success is asserted without evidence.
- Pattern: wrap each meaningful task in a small versioned contract: objective, non-objectives, allowed scope, context sources, tools, checks, memory update and escalation conditions.
- Tradeoffs: adds upfront ceremony, but reduces hidden state and makes failures attributable.
- Next experiment: use this contract on one `ia-learning` implementation or research-to-action task and compare rework against a normal chat-only run.
