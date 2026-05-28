# Generate Distribution Package Prompt

Use this prompt as the operating brief for Codex.

## Task

Create a local review-only YouTube distribution package for the selected video folder.

## Required Checks

1. Confirm selected video folder.
2. Confirm requested assets.
3. Read `transcript.txt`, `video_brief.md`, `thumbnail.png`, `youtube_link.txt`, and `timestamps.md` when available.
4. If transcript and brief are missing, ask Akshat before falling back to subtitles/timing files.
5. Extract killer lines from the transcript before writing assets.
6. Generate only the requested assets.
7. Apply the creative QA rubric.
8. Create `distribution_package.md`.
9. Create `review_dashboard.html` as the main one-file review surface.
10. Keep `preview.html` and `review.html` as backup/specialized views when useful.
11. Create `approval.md`.
12. Create `sendfox_final_preview.html` before any SendFox draft creation.
13. Create `mobile_preview.html` when email or social layout needs phone review.
14. Create `approval_summary.html` for readable approval summaries.
15. Show a short summary in chat.

## Scope Rule

Do not create many channels by default.

Create only the channel assets Akshat specifically asks for.

- WhatsApp request = WhatsApp only.
- LinkedIn request = LinkedIn only.
- SendFox email request = SendFox email only.
- Full distribution package = only when Akshat explicitly asks for a full distribution package.

Do not add email, LinkedIn, WhatsApp, X/Facebook, blog, carousel, or posting plan automatically.

## Hard Rules

- Do not send, post, publish, schedule, or create external drafts.
- Do not call external APIs.
- Do not build an LLM API script.
- All approvals start as pending.
- `review_dashboard.html` is the main review surface.
- `review.html` is the approval/comment surface.
- Keep the main dashboard clean: no approval controls, comment boxes, feedback prompt buttons, or external action controls unless Akshat asks.
- Use `review.html` only as a backup approval/comment page when a formal approval workflow is requested.
- Content approval and external action approval must be separate.
- Do not make Akshat review raw JSON.
- Keep the existing clean HTML preview style unless Akshat asks for a redesign.

## Default Creative Direction

Default winning category:
Punchy/Funny.

But Punchy/Funny means:
- founder pain
- real business consequence
- transcript-native humor
- sharp lines
- not random analogies

CTA:
Watch the full video.

## Required Creative Process

Before final output:
1. Extract killer lines.
2. Pick primary hook.
3. Create one flagship message first.
4. Critique it internally.
5. Improve it.
6. Create only the final options needed for the requested channel.
7. Run QA rubric.
8. Rewrite weak assets.
9. Save only final version.

Do not show weak drafts unless Akshat asks to see the thinking.

## Output Rules

Subject lines:
- If email is requested, create 2-3 subject options and 1 strong email by default.
- Create 25 subject lines only if Akshat asks.
- Pick final recommended subject.
- Use one relevant emoji when helpful. Avoid hype emojis like rocket, money bag, and fire.
- Do not use numeric claims like 2x, 3x, or 10x as the final recommended subject unless proof exists.
- Use the subject-line examples file as reference.

WhatsApp:
- Create 2-3 strong messages by default.
- Do not create 5-10 variants unless Akshat asks.
- Use the WhatsApp examples file.
- Tactical posts max 3 bullets/questions.
- Punchy/Funny must use founder pain, not generic jokes.
- Use Akshat's approved personal observation style as the benchmark.
- Must feel like a personal message, not a newsletter.
- Prefer "My observation..." or "I've seen..." openings.

Email:
- Thumbnail/link near top.
- Skimmable newsletter preview.
- 180-350 words unless Akshat asks for longer.
- Include plain text and HTML preview.
- Recommended structure: opening pain, thumbnail/video CTA, core lesson, best parts, final CTA.
- Do not repeat the CTA enough times to create clutter.

LinkedIn:
- Do not create LinkedIn posts unless Akshat asks for LinkedIn.
- If LinkedIn is requested, create 3-5 options:
  - Punchy/Funny
  - Tactical
  - Practical
  - Contrarian
  - Founder Lesson
- Main point in first 5-6 lines.
- One idea only.
- No slow blog intro.
- Do not include recommended winner or why it may work unless Akshat asks.

Carousel:
- 8-10 slides.
- One sharp statement per slide.
- One short support line.
- One visual metaphor.
- No paragraph slides.

Posting plan:
- Timing is a hypothesis.
- Include best time, backup, reason, confidence, and what to test.
