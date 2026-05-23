# Knowledge

Durable local memory for this project.

Use this folder to preserve evidence, decisions, experiments, and reusable learnings. Do not use it as a dump for every chat response.

## Structure

```txt
knowledge/
  raw/                       original source evidence
  processed/                 normalized summaries, transcripts, insights
  projects/<project-id>/     project-specific memory
```

## Rules

- Preserve raw evidence when a claim affects product, architecture, process, or research decisions.
- Read indexes and project memory before raw sources.
- Separate facts, assumptions, inferences, experiments, and open questions.
- Keep active memory concise.
- Promote reusable patterns into docs, scripts, templates, or skills.

## Confidence Labels

- `verified`: directly supported by evidence.
- `inferred`: reasonable interpretation from evidence.
- `experimental`: needs validation in this project.
- `unverified`: saved for later review, not decision-ready.
