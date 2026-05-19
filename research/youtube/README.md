# YouTube Research Sources

Use this folder for reusable YouTube research inputs and derived analysis.

Recommended layout per video:

```text
research/youtube/<slug>-<video_id>/
  source/
    transcript.<language>.<kind>.json
  analysis/
    findings.md
    prompts.md
    product-ideas.md
  README.md
```

Conventions:

- Keep `source/` immutable: raw transcripts, metadata, diagnostics, and checksums.
- Put interpreted material in `analysis/`: summaries, extracted prompts, product ideas, workflows, monetization hypotheses, and follow-up questions.
- Cite timestamps or segment starts when making claims from a transcript.
- Mark auto-generated captions clearly; they can include repeated or malformed text.
- Do not paste API keys, browser cookies, or private credentials into source files.
