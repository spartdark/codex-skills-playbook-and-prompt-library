# OpenAI Codex Official Usage Notes

- source type: web
- captured date: 2026-05-20
- confidence: verified for official product capabilities; practical guidance is inferred from usage patterns
- raw source: `knowledge/raw/web/openai-codex-official-docs-2026-05-20.json`

## Relevant Findings

Codex is useful as both a local pair-programming agent and a delegated background engineering agent. The strongest workflow is not just asking for code, but giving Codex a clear goal, repo context, success criteria, and permission to inspect files, edit, run commands, and verify with tests.

Official sources emphasize these working modes:

- Local pairing through terminal, IDE, or Codex app for targeted implementation, debugging, and explanation.
- Cloud delegation for background tasks in isolated environments.
- Parallel agent workflows across worktrees or tasks.
- Reviewable outputs through diffs, pull requests, tests, and summaries.
- Better results when the repo has clear setup instructions, test commands, and project documentation.

## Project Relevance

For `ia-learning`, Codex should be treated as an engineering control plane: use it to convert research into specs, specs into validated changes, and recurring discoveries into local knowledge artifacts. The repo's `knowledge/` convention is especially valuable because it gives Codex durable context instead of relying only on chat history.
