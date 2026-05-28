# YT Project Instructions

This project stores repeatable YouTube workflows for BizAmps.

## How To Work Here

- Use plan mode first for non-trivial tasks.
- Verify assumptions before code or API calls.
- Keep it simple.
- Make surgical edits only.
- Work backward from the business goal.
- Use subagents only for focused research or analysis.
- Never overbuild.
- Never make Akshat review raw JSON.
- Use human-readable Markdown or HTML first.
- End with risks, missing channels, and the recommended next action.

## What This Project Does

- Keeps each YouTube video in its own folder.
- Creates local review packages for YouTube distribution.
- Keeps slide/video production separate from distribution writing.
- Builds a local learning layer from campaign results, YouTube analytics, research, and coaching notes.

## Key Business Rules

- V1 distribution work is local review only.
- Do not send, publish, schedule, or create external drafts unless Akshat explicitly approves a later workflow.
- Use Codex itself for content generation. Do not build an LLM API script for V1.
- Keep writing founder-friendly, sharp, simple, and slightly witty.
- Default CTA: Watch the full video.
- Create only the channels Akshat specifically asks for. Do not create a full distribution package unless Akshat asks for one.
- Optimize for the best message, not many options.
- For WhatsApp, default to 2-3 strong personal messages, not 5-10 variants.
- For LinkedIn, create posts only when Akshat asks for LinkedIn.
- For email, default to 2-3 subject options and 1 strong email unless Akshat asks for more.
- Learning-layer work must not modify current video production files unless Akshat asks.
- SendFox is the first integration to test: start with `GET /me` and `GET /lists`; later create draft campaigns only.
- Never call SendFox send endpoints, never include `scheduled_at`, and never automate sending.
- Preferred SendFox From Name for future drafts: `🧠 Akshat from BizAmps`, unless `keys.env` or SendFox account settings block it.
- SendFox list selection must follow `shared\integrations\sendfox\list_selection_rules.md`; do not assume one list and do not include test or old lists unless configured.
- Buffer is second: create a LinkedIn draft or queued post only after approval; if a safe draft state is not supported, stop and create local fallback files.
- HubSpot marketing email draft creation is unproven for this account; research access first and fall back to local HTML/manual steps if needed.
- YouTube Analytics requires a Google OAuth flow; do not implement OAuth until separately approved.
- Never auto-reply from Octolens or any monitoring tool.

## Input And Output Expectations

- Preferred video inputs: `transcript.txt`, `video_brief.md`, and optional `thumbnail.png`.
- If those are missing, use available transcript, subtitle, timing, or notes files and clearly record the assumption.
- Distribution outputs live in `[Video Name]\distribution`.
- `preview.html` is the main review surface.
- `approval.json` controls later draft creation; every item starts as pending.
- Research and learning outputs live under `shared\content_library`, `shared\research`, and `shared\video_coaching`.
- Do not create external drafts in this Research / Learning / Coaching thread.

## Testing Rules

- Confirm the preview only includes requested assets.
- Confirm `approval.json` is valid JSON.
- Confirm no external drafts were created.
- Confirm all requested channels start as pending.
- Confirm secret files are ignored before any backup.
- Confirm no secrets are printed in chat or written into logs.
- Confirm learning-layer files are readable Markdown or HTML.

## Mistakes To Avoid

- Do not overwrite the existing `youtube-slide-video-assets` workflow.
- Do not create every possible asset unless Akshat asks for everything.
- Do not create extra dashboards, extra channels, or 10 options when 2-3 strong options are enough.
- Do not hard-code posting times as universal truth.
- Do not use generic AI marketing, hype, or corporate fluff.
- Use simple words. Avoid uncommon or clever words when a simpler founder-friendly word works better.
- Do not commit `keys.env`, `.env`, token files, credential files, or OAuth client secret files.
- Do not treat weak campaign signals as proof of demand.
