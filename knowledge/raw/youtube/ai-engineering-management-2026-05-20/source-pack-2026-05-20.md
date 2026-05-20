---
source_type: youtube_search_pack
source_url: https://www.youtube.com/results?search_query=AI+engineering+management+software+teams+project+management
captured_at: 2026-05-20
captured_via: web search, YouTube oEmbed, youtube-transcript script
topic: AI for engineering management and software project administration
confidence: mixed; one new transcript-backed source plus prior local transcript-backed Codex/spec-driven sources and secondary metadata for broader leadership talks
---

# AI Engineering Management Source Pack

## Search Intent

Find YouTube content relevant to using AI to manage software development teams, engineering project administration, agent workflows, standups, specs, CI, PR review, and engineering leadership.

## Highest-Signal Sources

| Priority | Source | Evidence status | Use for |
|---|---|---|---|
| 1 | [Spec-driven development: the AI engineering workflow at Notion](https://www.youtube.com/watch?v=pUHA_jNwuYE) - How I AI / Ryan Nystrom | transcript recovered; English auto captions; oEmbed saved | Engineering manager workflow: standup pre-read, Slack/GitHub/Honeycomb context, background agents, specs, CI speed. |
| 2 | [Automate tasks with the Codex app](https://www.youtube.com/watch?v=xHnlzAPD9QI) - OpenAI | existing local transcript; manual English captions | Recurring engineering hygiene: commit pulse, Sentry triage, AGENTS.md updates, CI and PR health. |
| 3 | [Spec-Driven Development: AI Assisted Coding Explained](https://www.youtube.com/watch?v=mViFYTwWvcM) - IBM Technology | existing local transcript; manual English captions | Requirements, PRD, design, implementation, staging, production, and maintenance discipline for AI-assisted work. |
| 4 | [Full Walkthrough: Workflow for AI Coding](https://www.youtube.com/watch?v=-QFHIoCo-Ko) - AI Engineer / Matt Pocock | existing local transcript; English auto captions | Task sizing, context management, planning from ambiguous requirements. |
| 5 | [How AI is Impacting Engineering Leadership](https://www.classcentral.com/course/youtube-how-ai-is-impacting-engineering-leadership-494687) - JavaScript Conferences by GitNation via YouTube | secondary metadata; transcript not captured in this run | Leadership framing: expectation management, AI strategy, role convergence, team pressure. |
| 6 | [The AI-Native Software Engineer](https://devopsflow.net/ai-native-engineer-addy-osmani/) - Addy Osmani / JSNation US 2025 | secondary summary of YouTube talk; transcript not captured in this run | Why raw code generation does not automatically improve shipping; review, quality, deployment, reliability bottlenecks. |
| 7 | [Coding with AI: The End of Software Development as We Know It](https://www.oreilly.com/CodingwithAI/) - O'Reilly | event page with YouTube highlights/channel link; no transcript captured | Broader team composition and skill-shift context: senior leverage, junior development, task breakdown, feedback loops. |
| 8 | [Will AI Replace Software Engineers? Here's What an Engineering Leader Says](https://www.listennotes.com/podcasts/digital-disruption/will-ai-replace-software-G3sYTela2qM/) - Digital Disruption / Bala Muthiah | secondary podcast metadata; no transcript captured | Grounded leadership counterweight: value creation over lines of code, governance, culture, trust, remote teams. |

## New Raw Evidence

- `knowledge/raw/youtube/ai-engineering-management-2026-05-20/oembed-pUHA_jNwuYE.json`
- `knowledge/raw/youtube/ai-engineering-management-2026-05-20/youtube-transcript-how-i-ai-spec-driven-development-the-ai-engineering-workflow-at-notion-ryan-nystr-pUHA_jNwuYE-en.json`

## Related Existing Evidence

- `knowledge/raw/youtube/codex-ai-project-management/source-pack-2026-05-19.md`
- `knowledge/processed/summaries/youtube-codex-ai-project-management-2026-05-19.md`
- `knowledge/processed/transcripts/codex-ai-project-management/youtube-xHnlzAPD9QI-en.md`
- `knowledge/processed/transcripts/codex-ai-project-management/youtube-mViFYTwWvcM-en.md`
- `knowledge/processed/transcripts/codex-ai-project-management/youtube--QFHIoCo-Ko-en.md`

## Selection Rationale

The Notion source is the clearest match for "AI for managing software teams" because it is explicitly from an engineering manager perspective and covers recurring management work, implementation delegation, specs, PRs, and CI. The existing Codex/spec-driven pack remains relevant because it explains how to turn software project work into bounded agent tasks with validation.

The broader leadership sources were kept as secondary inputs because they appear relevant from metadata, but they were not treated as transcript-backed evidence in this run.

## Limitations

- No YouTube Data API key was used.
- Only the Notion video received a new transcript capture in this run.
- The Notion transcript is auto-generated and contains repeated caption fragments; extracted claims should be checked against timestamps before becoming final process rules.
- Secondary pages may summarize YouTube content accurately, but they are not primary transcript evidence.
