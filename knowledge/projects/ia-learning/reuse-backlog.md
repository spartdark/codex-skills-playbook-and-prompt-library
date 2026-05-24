# Reuse Backlog

Candidates for promoting knowledge, docs, templates, skills, or plugins into reusable assets.

Use this file before creating broad new assets. The goal is to keep the repo useful and composable without turning every idea into a skill or plugin.

## Promotion Path

```txt
knowledge -> docs/templates -> skill -> plugin
```

## Candidate Template

```md
## <Candidate Name>

- Status: idea | validating | ready | promoted | dropped
- Source:
- Current artifact:
- Proposed asset: docs | template | skill | plugin
- Reuse case:
- Expected users:
- Inputs:
- Outputs:
- Validation needed:
- Token budget impact:
- Decision:
```

## Active Candidates

## AI Brand Memory Template

- Status: promoted
- Source: `knowledge/raw/youtube/ai-brand-identity-2026-05-24/source-pack-2026-05-24.md`
- Current artifact: `knowledge/processed/summaries/youtube-ai-brand-identity-2026-05-24.md`
- Proposed asset: docs | template
- Reuse case: Start a brand identity project with AI-readable memory, logo assets, color/type tokens, prompt recipes, and Cricut/vinyl export constraints.
- Expected users: Designers, solopreneurs, Codex users building brand systems, and agents generating future brand-consistent assets.
- Inputs: Brand brief, audience, logo directions, colors, type, usage constraints, production targets.
- Outputs: `brand-memory.json`, brand brief, prompt library, logo variants, Cricut-ready SVG export checklist.
- Validation needed: Apply to one real identity project and test a generated SVG upload in Cricut Design Space.
- Token budget impact: Low if stored as indexed Markdown/JSON and read selectively.
- Decision: Promoted to `docs/ai/ai-brand-identity-operating-guide/` and `templates/brand-ai-memory/`; keep validation caveat until applied to a real brand project.

## Promoted Assets

| Date | Candidate | Promoted To | Evidence |
|---|---|---|---|
| 2026-05-23 | Reuse Promotion Guide | `docs/ai/reuse-promotion-guide/` | Derived from `docs/ai/governance.md`, `knowledge/README.md`, `research-ops-evidence-guide.md`, `spec-driven-development-guide.md`, and `implementation-patterns.md` |
| 2026-05-24 | AI Brand Memory Template | `docs/ai/ai-brand-identity-operating-guide/`, `templates/brand-ai-memory/` | Derived from `knowledge/processed/summaries/youtube-ai-brand-identity-2026-05-24.md` and `knowledge/processed/insights/youtube-ai-brand-identity-memory-workflow.md` |
