---
source_type: youtube_search_pack
source_url: https://www.youtube.com/results?search_query=OpenAI+Codex+AI+software+project+management
captured_at: 2026-05-19
captured_via: Codex Browser plugin, YouTube oEmbed, youtube-transcript script
topic: Codex and AI-based software project management
confidence: metadata verified; transcripts recovered after extractor SSL and language fallback fixes
---

# Codex and AI Project Management Source Pack

## Capture Notes

- Search intent: find content related to OpenAI Codex and AI-based management of software projects.
- Browser search surfaced official OpenAI Codex videos, a recent long-form Codex course, and spec-driven/AI coding workflow videos that connect AI coding with project planning.
- YouTube oEmbed metadata was saved for each selected video under `knowledge/raw/youtube/codex-ai-project-management/`.
- Initial transcript extraction returned `temporary_provider_failure` on 2026-05-19 because Python `urllib` could not validate local CA certificates and the fallback requested multiple subtitle languages.
- The extractor was fixed to use `certifi` for HTTPS verification and to request only the explicit language in the `yt-dlp` fallback. All selected new videos now have transcript JSON under `knowledge/raw/youtube/codex-ai-project-management/` and normalized Markdown under `knowledge/processed/transcripts/codex-ai-project-management/`.
- Existing prior evidence in this repo includes a transcript-backed summary for Riley Brown's `Codex Full Course 2026`.

## Selected Videos

| Video ID | Title | Channel | URL | Local raw evidence | Transcript status | Why it matters |
|---|---|---|---|---|---|---|
| HFM3se4lNiw | Introducing the Codex app | OpenAI | https://www.youtube.com/watch?v=HFM3se4lNiw | `oembed-HFM3se4lNiw.json`, `transcript-HFM3se4lNiw.json` | recovered: English manual captions via `yt-dlp` fallback | Official framing of Codex as a command center for agent-based development. |
| sd21Igx4HtA | OpenAI Codex in your code editor | OpenAI | https://www.youtube.com/watch?v=sd21Igx4HtA | `oembed-sd21Igx4HtA.json`, `transcript-sd21Igx4HtA.json` | recovered: English auto captions via `yt-dlp` fallback | Shows IDE workflow, codebase exploration, task handoff to cloud agents, and review loops. |
| xHnlzAPD9QI | Automate tasks with the Codex app | OpenAI | https://www.youtube.com/watch?v=xHnlzAPD9QI | `oembed-xHnlzAPD9QI.json`, `transcript-xHnlzAPD9QI.json` | recovered: English manual captions via `yt-dlp` fallback | Directly relevant to recurring software project operations: commit pulse, Sentry triage, CI, merge conflicts, and keeping PRs green. |
| j7d5rs0iMlE | OpenAI Codex Full Course 4 Hours: Build & Ship | Aniket Panjwani | https://www.youtube.com/watch?v=j7d5rs0iMlE | `oembed-j7d5rs0iMlE.json`, `transcript-j7d5rs0iMlE.json` | recovered: English auto captions via `yt-dlp` fallback | Long-form course with chapters on AGENTS.md, plugins, skills, subagents, GitHub issues, automations, worktrees, and parallel repo work. |
| KXIdYEdOPys | Codex Full Course 2026: The NEW Best AI Coding Tool | Riley Brown | https://www.youtube.com/watch?v=KXIdYEdOPys | existing raw transcript and oEmbed in `knowledge/raw/youtube/` | available via prior ytscribe capture | Existing transcript-backed source for Codex project folders, skills, plugins, automations, launch workflows, and multi-agent orchestration. |
| mViFYTwWvcM | Spec-Driven Development: AI Assisted Coding Explained | IBM Technology | https://www.youtube.com/watch?v=mViFYTwWvcM | `oembed-mViFYTwWvcM.json`, `transcript-mViFYTwWvcM.json` | recovered: English manual captions via `yt-dlp` fallback | Strong bridge from AI coding to requirements, behavioral specs, and software lifecycle discipline. |
| -QFHIoCo-Ko | Full Walkthrough: Workflow for AI Coding - Matt Pocock | AI Engineer | https://www.youtube.com/watch?v=-QFHIoCo-Ko | `oembed--QFHIoCo-Ko.json`, `transcript--QFHIoCo-Ko.json` | recovered: English auto captions via `yt-dlp` fallback | Lifecycle-oriented workshop: ambiguous requirements, task sizing, context control, and systematic planning with AI agents. |
| 2mq8-y-GV28 | Build Better Apps With AI Using This NEW Method (Spec-Driven Development) | Jordan Urbs | https://www.youtube.com/watch?v=2mq8-y-GV28 | `oembed-2mq8-y-GV28.json`, `transcript-2mq8-y-GV28.json` | recovered: English manual captions via `yt-dlp` fallback | Practitioner framing around why simple vibe-coding breaks on complex projects and why structured specs matter. |

## Browser-Visible Signals

- Official Codex app search result described Codex as a command center for developers to manage projects, supervise agents, and automate tasks.
- Official Codex editor result exposed chapters on exploring a codebase, implementing changes, moving tasks to Codex cloud, brainstorming designs, workflow changes, and reviewing Codex work.
- Official automation result exposed chapters on unfun work, morning commit pulse, skill improvement, AGENTS.md updates, Sentry triage, merge conflicts, CI pain, keeping PRs green, and auto-fixing CI/conflicts.
- Aniket Panjwani's course exposed chapters on AGENTS.md instructions, practical primitives, plugins, skills, MCPs, subagents, Git/GitHub basics, GitHub issues, Codex automations, worktrees, and worktree bootstrap scripts.
- IBM's result positioned spec-driven development as a bridge between AI assisted coding and traditional software engineering lifecycles.
- Matt Pocock's AI Engineer result emphasized lifecycle workflow from ambiguous requirements to systematic planning, context control, and task sizing.

## Remaining Limitations

- No YouTube Data API key was used, so view/like/comment metrics are limited to visible search snippets and should not be treated as durable metrics.
- YouTube Data API is available in the environment now and can enrich video metadata/statistics, but captions for third-party videos still come from public subtitle endpoints/fallbacks rather than the API key alone.
- Auto-generated captions are imperfect and should be labeled as such in downstream analysis.
