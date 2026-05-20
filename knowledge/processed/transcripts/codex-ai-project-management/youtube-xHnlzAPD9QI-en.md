---
source_type: youtube_transcript
source_url: https://www.youtube.com/watch?v=xHnlzAPD9QI
video_id: xHnlzAPD9QI
source_title: "Automate tasks with the Codex app"
channel: "OpenAI"
language: en
is_auto_generated: false
extraction_strategy: yt-dlp
retrieved_at: 2026-05-19T19:50:39Z
raw_evidence: knowledge/raw/youtube/codex-ai-project-management/transcript-xHnlzAPD9QI.json
confidence: verified source capture; caption accuracy not independently verified
---

# Automate tasks with the Codex app

## Transcript

- [00:00] So there is a lot about the job
- [00:02] isn't actually that fun that I have
- [00:05] now automated away almost entirely.
- [00:09] And so I'll show you a few of those
- [00:10] here in our automations tab. And we've
- [00:13] got a bunch running now, but we can
- [00:15] run down a few of these because I kind
- [00:16] of have set up a few different types
- [00:18] of automation. And the first type is
- [00:19] just sort of information. I'm asking
- [00:21] Codex to look at the last day of
- [00:23] commits into this section of our
- [00:26] monorepo. And basically group them,
- [00:28] tell me who worked on what, what got
- [00:31] done, what do I need to know about.
- [00:32] And so I wake up in the morning with
- [00:34] almost like a, if you've used JotGPT
- [00:36] Pulse, it's like a personalized pulse
- [00:38] that I walk, I open the app in the
- [00:40] morning and sitting there is like,
- [00:41] here's what happened yesterday in the
- [00:43] code base, which is super,
- [00:46] super useful. So I have one called
- [00:47] Upskill. And what Upskill does is
- [00:50] it looks at the last day of skill
- [00:52] usage. So it says, hey, skills are
- [00:55] really useful, but sometimes they take
- [00:57] a little bit of tinkering to get
- [00:58] right. And so it looks at Codex usage
- [01:00] throughout the past day and detects if
- [01:03] any skills, like if Codex had any
- [01:05] trouble with skills or if any of the
- [01:07] scripts didn't work correctly or if
- [01:10] like something could be sped up. And
- [01:11] it makes improvements to the skills.
- [01:13] So it's upskilling like overnight.
- [01:15] Like I'm going to sleep, I wake up,
- [01:16] Codex is smarter in the morning based
- [01:18] on what we're trying to do here.
- [01:20] Similarly, update AgentsMD, like
- [01:22] this I just have run every, I don't
- [01:25] know, six hours. And it just looks at
- [01:27] what we've been doing. And if there's
- [01:28] any like disagreements or
- [01:30] misunderstandings that I've had with
- [01:32] Codex or things where things took
- [01:33] longer to communicate than, or I used
- [01:36] some shorthands that Codex wasn't
- [01:37] familiar with, it will just add that
- [01:39] to the personalization. So that next
- [01:41] time things can just be quicker.
- [01:44] I've got a few others that are
- [01:45] integrated deeply into our other
- [01:47] tools. And so one of them is Sentry.
- [01:50] This is kind of a different type of
- [01:52] automation where it's going to go
- [01:54] through on whatever schedule, whatever
- [01:56] cadence, and it picks off one of the
- [01:58] top Sentry issues. So that could be
- [02:00] like a performance regression or
- [02:01] a crash or an error that's being
- [02:04] thrown in the app. And it like goes
- [02:07] through all of the information that we
- [02:09] have about it, the logs, the maps,
- [02:12] everything that Sentry has, it looks
- [02:13] at the code base and it picks
- [02:16] something to fix basically. And
- [02:18] automations have memory. So it
- [02:20] remembers what it tried to solve last
- [02:22] time. And so you're not going to get a
- [02:23] PR like solving the number one issue
- [02:25] every hour, right? But it's really
- [02:28] good because what this, you know, what
- [02:30] this type of automation does is it
- [02:32] allows us to focus on what is going to
- [02:35] make the Codex app great to use and
- [02:37] useful and joyful and all of the
- [02:40] things that like, you know,
- [02:43] bugs and things that fall through
- [02:45] cracks that like aren't quite as
- [02:46] fun to figure out, at least for me.
- [02:48] I know some people love it.
- [02:51] That stuff can happen kind of behind
- [02:52] the scenes, right? And so it's really
- [02:54] common that you run into merge
- [02:57] conflicts when you try to merge your
- [02:58] thing. And like you find, you know,
- [02:59] you iterate on your approach and
- [03:01] you've got like different types of
- [03:03] people giving reviews and then you're
- [03:05] finally ready to merge something and
- [03:06] there's a conflict. Your CI is failing
- [03:08] for, you know, some small reason.
- [03:10] You got to kind of dive into that. And
- [03:12] so I don't like dealing with any of
- [03:14] that. Maybe, you know. Most people
- [03:17] probably don't. Some people love doing
- [03:19] that and they work on CI tools.
- [03:22] But I have a green PRs automation here
- [03:24] that uses some of our skills. So
- [03:26] we use BuildKai, we use GitHub. And so
- [03:28] what this does is it checks if I have
- [03:31] any open PRs and I usually have like
- [03:34] at any given time between 10 and
- [03:35] 20 PRs these days open at a time
- [03:38] because of the Codex app. Separate
- [03:41] problem. And this is going to go
- [03:43] through and it's going to say like, do
- [03:45] any have CI failures because of like,
- [03:48] you know, something that like linted
- [03:50] wrong or like didn't get caught in the
- [03:53] pre -push? Or maybe it's going to
- [03:55] merge conflict because someone is like
- [03:57] also changing it because we're rushing
- [03:59] to, you know, finish up a project or
- [04:01] something like that. And this is going
- [04:03] to go through and it's going to make
- [04:04] sure that all my PRs are green. It's
- [04:06] going to update the base branch.
- [04:07] It's going to intelligently resolve
- [04:09] merge conflicts by looking at like
- [04:10] what have people been trying to do. So
- [04:12] it's not just a factual like, you
- [04:15] know, I'm going to clean up the like
- [04:17] conflict markers. It can look at,
- [04:20] oh, like Joey was putting in this
- [04:21] feature. So we changed this block for
- [04:23] this reason. I'm trying to do this.
- [04:25] I'm changing it and there's a conflict
- [04:26] and like kind of knows how to do that.
- [04:28] And so that's a very long way of
- [04:30] saying my PRs are always green.
