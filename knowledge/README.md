# Knowledge

Local derived memory for `ia-learning`.

This folder stores research outputs from YouTube, Reddit, AI tooling updates, implementation experiments, and monetization/process insights. It is intentionally local-first so we can validate the schema and workflow before moving the durable shared memory to Supabase.

## Goals

- Preserve raw source evidence.
- Convert noisy source material into reusable technical and product knowledge.
- Connect findings to concrete project areas.
- Support future RAG indexing with SQLite, embeddings, and later Supabase.
- Give Codex/plugins a stable place to read and write derived memory.
- Provide a portable memory pattern for new projects through `templates/project-ai-starter/`.

## Folder Contract

```txt
knowledge/
  raw/
    youtube/
    reddit/
    web/
  processed/
    transcripts/
    threads/
    summaries/
    insights/
  projects/
    ia-learning/
      implementation-patterns.md
      monetization-ideas.md
      process-improvements.md
      ai-news.md
      open-questions.md
      reuse-backlog.md
  briefs/
    weekly/
    topic/
  index/
    local generated SQLite/vector indexes, ignored by git
  schema/
    source-metadata.template.json
    insight.template.md
    summary.template.md
    source-package.template.md
```

## Operating Model

Use the chat as the coordinator and the filesystem as the durable record.

For project adoption, start with `AGENTS.md`, `docs/ai/governance.md`, and `templates/project-ai-starter/`. This keeps the active context small while preserving a clear path to deeper evidence.

For every useful source or initiative, create the same four layers:

1. `raw/`: original payloads, exports, API responses, metadata, or failure evidence.
2. `processed/`: normalized transcripts, threads, summaries, and atomic insights.
3. `projects/ia-learning/`: curated links from insights to project decisions, experiments, and open questions.
4. `briefs/`: recurring synthesis by week or topic when multiple sources accumulate.

The recommended naming pattern is:

```txt
<source>-<short-title>-<source-id>.<ext>
```

Examples:

```txt
knowledge/raw/youtube/ytscribe-codex-full-course-2026-KXIdYEdOPys-en-auto.json
knowledge/processed/transcripts/youtube-codex-full-course-2026-KXIdYEdOPys-en-auto.md
knowledge/processed/summaries/youtube-codex-full-course-2026-KXIdYEdOPys-summary.md
knowledge/processed/insights/youtube-codex-full-course-2026-agent-workflows.md
```

To scaffold a new source package:

```bash
python3 scripts/knowledge_new_source.py youtube "Source Title" --source-id VIDEO_ID --url "https://..."
```

This creates placeholders in the correct folders; replace placeholders with real source data and analysis.

## Source Lifecycle

1. Capture raw source output in `knowledge/raw/<source>/`.
2. Normalize content into Markdown in `knowledge/processed/`.
3. Extract insights with source references and confidence labels.
4. Link relevant insights into `knowledge/projects/ia-learning/`.
5. Promote repeated or validated insights into docs, backlog, PRDs, or implementation tasks.

## Project Control Files

`knowledge/projects/ia-learning/` is the curated decision surface for this repo:

- `source-index.md`: registry of analyzed sources and where their artifacts live.
- `agent-workflows.md`: reusable multi-agent/project-folder workflows.
- `experiments.md`: validation tasks derived from research.
- `implementation-patterns.md`: technical patterns worth reusing.
- `monetization-ideas.md`: product/business hypotheses.
- `process-improvements.md`: improvements to how this repo researches, builds, validates, and ships.
- `ai-news.md`: time-sensitive AI/tooling updates.
- `open-questions.md`: decisions that still need evidence.
- `reuse-backlog.md`: candidates to promote into docs, templates, skills, or plugins.

## Confidence Labels

- `verified`: supported directly by the source material.
- `inferred`: reasonable interpretation from source material.
- `experimental`: needs implementation/testing in this repo.
- `unverified`: saved for later validation, not ready for decisions.

## Plugin / Agent Rule

Any YouTube, Reddit, research, or RAG plugin used in this workspace should write a derived memory artifact here instead of only returning a chat summary.

Minimum required fields:

- source type
- source URL or permalink
- source title
- author/channel/community if available
- published date if available
- captured date
- confidence label
- project relevance
- extracted insight
- evidence pointer, such as timestamp, quote excerpt, comment permalink, or section heading

## Future Supabase Migration

When this structure is stable, migrate durable shared memory to Supabase:

- `sources`
- `source_items`
- `chunks`
- `embeddings`
- `projects`
- `insights`
- `project_links`
- `briefs`

Until then, this folder is the source of truth for local knowledge.
