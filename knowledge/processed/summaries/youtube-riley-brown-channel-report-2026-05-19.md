---
source_type: youtube_channel_report
channel: Riley Brown
channel_id: UCMcoud_ZW7cfxeIugBflSBw
source_url: https://www.youtube.com/@rileybrownai
captured_at: 2026-05-19T17:34:38Z
captured_date: 2026-05-19
video_count: 10
confidence: inferred_from_metadata
raw_source_pack: ../../raw/youtube/channel-reports/youtube-channel-source-pack-riley-brown-UCMcoud_ZW7cfxeIugBflSBw.json
raw_source_pack_md: ../../raw/youtube/channel-reports/youtube-channel-source-pack-riley-brown-UCMcoud_ZW7cfxeIugBflSBw.md
transcript_attempts: ../transcripts/youtube-riley-brown/
---

# Riley Brown Channel Report

## Source

- Channel: Riley Brown
- Channel URL: https://www.youtube.com/@rileybrownai
- Channel ID: `UCMcoud_ZW7cfxeIugBflSBw`
- Capture date: 2026-05-19
- Scope: latest 10 videos from the channel RSS/source pack.
- Stats: unavailable; `YOUTUBE_DATA_API_KEY` was not present, so no views, likes, comments, or ranking claims are included.
- Transcript status: public English auto-caption tracks were detected for all 10 videos, but transcript extraction failed for all 10. `timedtext` returned empty responses, `youtubei/get_transcript` returned HTTP 400 `FAILED_PRECONDITION`, and the `yt-dlp` subtitle fallback returned HTTP 429. The per-video error payloads are saved under `knowledge/processed/transcripts/youtube-riley-brown/`.

## Executive Summary

Riley Brown's most recent 10 videos are tightly clustered around Codex, GPT 5.5, Codex Mobile, vibe coding, and using agents/skills to replace or compress specialist workflows. Based on metadata, the channel is currently positioned as a fast-moving operator guide for AI builders: it turns new AI tooling into concrete setup guides, "best tool" comparisons, full courses, and workflow replacement narratives.

The strongest reusable pattern for `ia-learning` is not a single tool recommendation; it is the packaging pattern: translate fast AI releases into applied workflows, show the shortest path to competence, then convert that into templates, skill packs, automations, or launch kits. Because transcripts were unavailable in this capture, hook and content analysis below is limited to title-level evidence plus channel-level metadata patterns.

## Video Table

| Published | Title | URL | Transcript evidence |
|---|---|---|---|
| 2026-05-18 | Codex: Build Your Full AI Marketing Team (Agents + Skills) | https://www.youtube.com/watch?v=sL_KBnYB17I | Caption track detected; extraction failed |
| 2026-05-15 | OpenAI just released Codex Mobile | https://www.youtube.com/shorts/3mm-hxVtjkM | Caption track detected; extraction failed |
| 2026-05-15 | Codex Mobile App Released (Complete Setup Guide) | https://www.youtube.com/watch?v=4OiLljSo-hw | Caption track detected; extraction failed |
| 2026-05-07 | Vibe Coding for Beginners (Full Course 2026) | https://www.youtube.com/watch?v=BpOsHF5Oj_I | Caption track detected; extraction failed |
| 2026-05-02 | Codex is The NEW Best AI Coding Tool (Here's Why) | https://www.youtube.com/watch?v=FU2iB-UfPPA | Caption track detected; extraction failed |
| 2026-04-30 | 7 Tools That Make Codex 10x MORE Powerful | https://www.youtube.com/watch?v=SNAlFLV9MBE | Caption track detected; extraction failed |
| 2026-04-29 | Learn 95% of Codex in 30 minutes | https://www.youtube.com/watch?v=474wZZHoWN4 | Caption track detected; extraction failed |
| 2026-04-25 | With Codex and GPT 5.5 you can just do things. | https://www.youtube.com/shorts/pDsd2FiMUt8 | Caption track detected; extraction failed |
| 2026-04-24 | Codex Just Replaced 1,000 Hours of Video Editing Tutorials | https://www.youtube.com/watch?v=Xdy1vkhSz-M | Caption track detected; extraction failed |
| 2026-04-24 | GPT 5.5 + Codex Just Became the Best Model Ever | https://www.youtube.com/watch?v=5XZxmkjsNos | Caption track detected; extraction failed |

## Topic Clusters

- Codex as operating surface: seven of ten titles explicitly mention Codex, suggesting the current channel thesis is that Codex is not just a coding assistant but a practical control plane for building, learning, marketing, mobile work, and creative workflows.
- New-release capture: "just released", "released", "new", and model/version references frame the channel as rapid response to platform changes.
- Beginner-to-competent education: "Full Course 2026", "Complete Setup Guide", and "Learn 95% in 30 minutes" package adoption into compressed learning paths.
- Workflow replacement: "replaced 1,000 hours", "10x more powerful", "full AI marketing team", and "you can just do things" emphasize outcome compression rather than feature walkthroughs.
- Agent and skills framing: the latest video explicitly pairs agents and skills with marketing work, which maps directly to this repo's skill/plugin memory model.

## Hook Analysis

Transcript-backed intro analysis is unavailable in this capture.

Title-level hook patterns:

- Timeliness: "OpenAI just released..." and "Codex Mobile App Released..." target viewers who need to catch up immediately.
- Dominance claim: "The NEW Best AI Coding Tool" and "Best Model Ever" create a clear debate or curiosity gap.
- Quantified acceleration: "10x", "95%", "30 minutes", and "1,000 hours" turn abstract productivity into concrete promises.
- Workflow substitution: "Build Your Full AI Marketing Team" makes the video feel like a role-replacement playbook, not only a tutorial.
- Beginner accessibility: "for Beginners" lowers perceived entry cost while still attaching to a trend.

Recommended hook adaptation for `ia-learning`: titles and briefs should name the job-to-be-done first, then the AI surface. Example pattern: "Build a [business function] with Codex agents + skills" is more actionable than "Codex tutorial".

## Transcript-Backed Insights

No transcript-backed semantic claims are available from this capture. The local evidence only verifies channel/video metadata, caption-track presence, and transcript extraction failures. Any interpretation of the video body, exact tools shown, prompt wording, intro structure, or sponsor/affiliate mentions requires a successful transcript capture or manual review.

## Content Opportunities

- Create "operator packs" for specific roles: marketing team, video editing assistant, research analyst, launch assistant, support triage, and product validation agent.
- Turn new AI releases into same-day setup guides that include installation, first workflow, failure modes, and reusable artifacts.
- Publish beginner courses that end in a working artifact, not passive knowledge: a deployed app, a saved skill, an automation, or a monetization landing page.
- Build comparison briefs around "why this is now the best tool" but require reproducible benchmark tasks to avoid hype-only conclusions.
- Convert "95% in 30 minutes" into internal `ia-learning` quickstarts for Codex skills, automations, Figma, YouTube research, Reddit research, and RAG workflows.

## Workflow And AI Automation Ideas

- Channel-to-knowledge pipeline: automate latest-video capture, transcript attempts, source-pack storage, summary generation, and project-link updates under `knowledge/`.
- AI marketing team template: define agents/skills for positioning, landing copy, competitive scan, short-form scripts, email sequence, asset checklist, and experiment logging.
- Codex Mobile field workflow: test whether mobile Codex is useful for reviewing source packs, approving experiments, and triaging idea backlog while away from the workstation.
- Skill pack generator: convert repeatable workflows into local Codex skills with setup, guardrails, smoke tests, and evidence requirements.
- Tutorial compression evaluator: for any "learn 95%" style source, extract the actual minimal skill tree and compare it with what this repo already documents.

## Monetization Hypotheses

- Paid role-specific Codex kits: sell or validate templates for AI marketing, video ops, research ops, and launch ops.
- Done-with-you agent setup: package implementation services for founders who want Codex/skills installed, connected, and documented.
- Micro-courses with artifacts: short paid lessons where the deliverable is a reusable skill, automation, or production workflow.
- Benchmark-backed tool reports: subscription or lead magnet comparing AI coding tools against repeatable tasks instead of opinion-only rankings.
- Internal enablement package: B2B training that teaches non-engineering teams how to use Codex Mobile and agent workflows safely.

## Recommended Experiments

1. Build an "AI marketing team" source-to-template experiment.
   - Smallest test: define 5 Codex skills/agents for one product idea, run them on a landing page + launch checklist, and record cycle time and manual edits.
   - Success signal: a usable launch artifact set exists with fewer than two manual rewrite passes.

2. Create a "95% in 30 minutes" quickstart for one internal workflow.
   - Smallest test: pick YouTube research or Reddit research and compress it into a 30-minute operator guide with required outputs.
   - Success signal: another session can follow it and produce `raw`, `processed`, and `project` artifacts without extra explanation.

3. Validate Codex Mobile as review surface.
   - Smallest test: use mobile only for one review/triage loop: approve a report, prioritize experiments, or comment on generated source packs.
   - Success signal: mobile review saves time without losing traceability or introducing unreviewed changes.

4. Prototype a benchmark-backed "best AI coding tool" matrix.
   - Smallest test: run Codex, one competing tool, and a baseline human workflow on the same small repo task.
   - Success signal: measurable differences in completion time, correctness, test quality, and rework.

## Prompts Detected

No prompts were detected because transcripts were unavailable and no manual video review was performed.

## Open Questions

- Are the videos monetized through affiliates, templates, courses, sponsors, or services? Transcript or description capture is needed.
- Which exact tools are included in "7 Tools That Make Codex 10x MORE Powerful"?
- What does the "AI marketing team" workflow assign to agents versus skills?
- Does Codex Mobile change workflows materially, or is it mostly a setup/update story?
- Which topics perform best by views, retention, or comments? YouTube Data API metrics are needed.

## Evidence Pointers

- Raw source pack JSON: `knowledge/raw/youtube/channel-reports/youtube-channel-source-pack-riley-brown-UCMcoud_ZW7cfxeIugBflSBw.json`
- Raw source pack Markdown: `knowledge/raw/youtube/channel-reports/youtube-channel-source-pack-riley-brown-UCMcoud_ZW7cfxeIugBflSBw.md`
- Transcript attempt JSON files: `knowledge/processed/transcripts/youtube-riley-brown/*.json`
- Confidence: metadata verified; transcript content unavailable; recommendations inferred and experimental.
