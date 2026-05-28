---
name: youtube-distribution-draft-system
description: Create local review-ready YouTube distribution assets from a transcript or video brief, including WhatsApp posts, email previews, LinkedIn posts, carousel outlines, posting plans, review_dashboard.html, and approval.md. V1 is local review only and must not send, publish, schedule, or create external drafts.
---

# YouTube Distribution Draft System

Use this skill when Akshat wants to turn a YouTube video transcript or brief into distribution assets.

This skill is separate from `youtube-slide-video-assets`.

## V1 Rule

V1 is local review only.

Do not:

- send emails
- post to LinkedIn
- publish anything
- schedule anything
- create external drafts
- call SendFox, HubSpot, Buffer, LinkedIn, or any external API
- build a Python script that needs an LLM API key

Use Codex itself to write the content.

## Intake

Before a normal run, confirm:

- video folder
- goal: reach, trust, leads, nurture, or testing
- target audience
- requested assets
- platform priority
- urgency
- geography/timezone

If Akshat asks for all assets, confirm before generating everything.

If Akshat asks for only specific assets, generate only those assets.

## Channel Scope Rule

Do not generate many channels by default.

Create only the channel assets Akshat specifically asks for.

Examples:

- If Akshat asks for WhatsApp, create WhatsApp only.
- If Akshat asks for LinkedIn, create LinkedIn only.
- If Akshat asks for SendFox email, create SendFox email only.
- Do not automatically create email, LinkedIn, WhatsApp, X, Facebook, blog, carousel, and posting plan unless Akshat explicitly asks for a full distribution package.

The best message matters more than many options.

Before creating multiple options for any channel:

1. Study the video script/transcript.
2. Extract the strongest idea.
3. Create one flagship message first.
4. Critique it internally.
5. Improve it.
6. Then create 2-5 final options depending on the channel.

Do not show weak drafts unless Akshat asks to see the thinking.

## Inputs

Prefer these files inside the video folder:

- `transcript.txt`
- `video_brief.md`
- `thumbnail.png`

Optional:

- `title.txt`
- `youtube_link.txt`
- `timestamps.md`
- `notes.md`
- `existing_post_examples.md`

If transcript and brief are missing, ask Akshat before falling back to subtitles, timing files, or notes.

Record any fallback assumption in the package.

## Outputs

Create files inside:

```text
[Video Name]\distribution
```

Required:

- `review_dashboard.html`
- `preview.html`
- `review.html`
- `mobile_preview.html` when email/social formatting needs mobile review
- `sendfox_final_preview.html` before any SendFox draft creation
- `approval_summary.html` for readable post-review summaries
- `distribution_package.md`
- `approval.md`

Optional:

- `output\whatsapp_posts.md`
- `output\sendfox_email.md`
- `output\linkedin_post.md`
- `output\carousel_outline.md`
- `output\posting_plan.md`

## Review Workflow

Akshat reviews HTML first.

- `review_dashboard.html` is the main one-file review surface.
- Keep `preview.html`, `review.html`, `mobile_preview.html`, and `sendfox_final_preview.html` as backup/specialized views when useful.
- `review_dashboard.html` should be a clean content dashboard, not an approval app.
- Keep approval controls, comments, feedback prompts, and external action controls out of the main dashboard unless Akshat asks for them.
- Do not imply browser-to-file approval unless a local review server is explicitly requested.
- Create `local_review_server.py` only if Akshat asks for direct browser-to-file approval.
- `preview.html` is a backup read-only review surface for all content.
- `review.html` is a backup approval and comments surface.
- `review.html` should let Akshat mark each asset as approved, needs_edit, or rejected.
- `review.html` should include comment boxes for each asset.
- `review.html` should generate easy-to-copy `approval.md` content.
- `review.html` should generate an easy-to-copy Codex feedback prompt.
- Codex then updates `approval.md` and content files based on the pasted review output.
- Content approval and external action approval must be separate sections.
- Content approval does not approve API calls, draft creation, sending, publishing, or scheduling.
- External action approval must list specific actions separately:
  - SendFox read-only test: GET /me
  - SendFox read-only test: GET /lists
  - SendFox campaign draft creation
  - Buffer read-only channel test
  - Buffer LinkedIn draft/queued post
- External drafts are created only after the specific external action is approved.
- Add missed-channel reminders in `review.html` when useful:
  - Medium article
  - Website blog
  - YouTube Community post
  - LinkedIn carousel
  - Shorts test
  - HubSpot email later
  - Octolens conversation search
  - Newsletter swap angle

Do not make Akshat review raw JSON.

## Source Material Rule

Before writing any asset, extract 10-20 "killer lines" from the transcript.

Killer lines include:
- sharp claims
- funny lines
- founder pain
- memorable metaphors
- cost/risk/consequence
- lines that could become hooks, subject lines, or carousel slides

Use transcript-native lines before inventing new analogies.

Do not use generic analogies unless they are clearly stronger than the transcript's own language.

## Voice

Default creative category:
Punchy/Funny.

Write for B2B founders:

- blunt
- simple
- founder-friendly
- slightly witty
- high-signal
- practical

Punchy/Funny means:
- founder pain
- real cost
- empty calendar
- payroll burn
- awkward sales reality
- business consequence

Punchy/Funny does not mean:
- random jokes
- cute analogies
- generic metaphors
- LinkedIn intern humor

Avoid:

- generic AI marketing
- corporate fluff
- corporate jargon
- clever words that slow the reader down
- phrases that sound written for marketers instead of founders
- fake urgency
- motivational-guru lines
- "excited to share"
- "game-changing"
- "revolutionary"
- "unlock"
- "ultimate guide"
- "skyrocket"
- "in today's fast-paced world"
- "calendar invite with invoices"
- "lanyards"

Default CTA:

```text
Watch the full video.
```

## Approved Reference Style

Use Akshat's manually approved WhatsApp message style as the benchmark for tone, structure, and sharpness.

The reference style:

- starts with a personal observation
- talks directly to a specific group
- names real founder or business pain
- uses a concrete failure pattern
- uses simple visual rhythm:
  - Buy booth.
  - Print banners.
  - Fly the team out.
  - Hope pipeline appears.
- keeps sharp principle lines:
  - The event creates intent.
  - Outbound creates the meeting.
- gives a simple tactical play
- ends with a clear, natural video CTA

Do not depend on Akshat giving a rough message every time. Infer the best message from the script or transcript, but use Akshat's approved past messages as the style benchmark.

## Internal Quality Check

Before showing final copy, score each message out of 10 on:

1. Sounds like Akshat personally wrote it
2. Clear founder pain
3. Simple words
4. Strong opening
5. Concrete example
6. Clear tactical takeaway
7. Fits the channel
8. CTA feels natural

Only show messages that score 8/10 or above. If a message scores below 8/10, rewrite it before showing it.

Optional quality pass: use a focused Founder Voice Editor pass when quality matters.

Founder Voice Editor job:

- study Akshat's approved past messages
- study the current script/transcript
- extract the strongest idea
- preserve strong founder-level lines
- cut generic phrasing
- make the message sharper, shorter, and more personal
- make sure it sounds like Akshat, not a generic content repurposing tool
- return final copy only after it clears the quality check

## Asset Rules

WhatsApp:

- Create only 2-3 strong WhatsApp messages by default.
- Do not create 5-10 WhatsApp variants unless Akshat asks.
- Keep posts short and personal.
- Avoid making every post look copied.
- Tactical posts must have maximum 3 bullets/questions.
- Punchy/Funny posts should use business pain from the transcript, not random jokes.
- Prefer compressed founder stories.
- WhatsApp should feel like a personal message, not a generic broadcast.
- Most WhatsApp messages should start with "I" or "My observation".
- Prefer "My observation..." or "I've seen..." openings.
- Keep simple words.
- Keep it founder-friendly and direct.
- Avoid over-polishing.
- Avoid cute phrases that sound clever but weak.
- Avoid uncommon words.
- Avoid corporate phrases.
- Do not use "calendar invite with invoices".
- Do not use "lanyards"; prefer "event badges" or avoid the phrase completely.

Email:

- If Akshat asks for SendFox or HubSpot email, create 2-3 subject options and 1 strong email by default.
- Do not create many email variants or 25 subject lines unless asked.
- Pick one final recommended subject.
- A relevant emoji may be used in subject lines.
- Avoid common hype emojis such as rocket, money bag, and fire.
- Prefer relevant emojis such as 🎟️, ☕, 🧭, 🎪, and 🧲.
- Do not use numeric claims such as 2x, 3x, or 10x as the default subject unless the source material or prior data proves the claim.
- Preferred SendFox From Name: `🧠 Akshat from BizAmps`, unless `keys.env` or SendFox account settings block it.
- SendFox draft list selection must follow `shared\integrations\sendfox\list_selection_rules.md`.
- Include preview text.
- Include plain text preview.
- Include HTML preview.
- Thumbnail/link must appear near the top.
- Keep it skimmable and click-focused.
- Use this structure unless Akshat gives a better reference:
  - Opening pain
  - Thumbnail/video CTA
  - Core lesson
  - Best parts
  - Final CTA
- Do not repeat "Watch the full video" so often that the email feels cluttered.
- SendFox HTML must use simple email-safe/table-safe HTML.
- Use inline paragraph spacing such as `<p style="margin: 0 0 14px 0;">`.
- Use separate paragraphs or controlled block rows for stacked punch lines.
- Add enough spacing before and after thumbnails and buttons.
- Use normal-sized buttons:
  `display:inline-block; background:#111111; color:#ffffff; padding:10px 16px; border-radius:6px; font-weight:bold; text-decoration:none; font-size:14px; line-height:1.2;`
- Do not create oversized CTA buttons.

LinkedIn personal post:

- Do not create LinkedIn posts unless Akshat asks for LinkedIn.
- If Akshat asks for LinkedIn posts, create 3-5 options.
- Recommended angle set:
  - Punchy/Funny
  - Tactical
  - Practical
  - Contrarian
  - Founder Lesson
- Main point should appear in the first 5 to 6 lines.
- One post should have one clear idea.
- CTA should be soft and near the end.
- Avoid slow setup and blog-intro style.
- Use simple words. Avoid uncommon terms if a simpler one exists.
- Avoid "lanyards" unless the context really needs it; prefer "badges", "name tags", or "event badges".
- Do not add "recommended winner" or "why it may work" in review HTML unless Akshat asks.

Carousel:

- Do not create unless requested.
- 8 to 10 slides max.
- One idea per slide.
- One sharp statement.
- One visual metaphor.
- One short supporting line.
- No dense bullets.
- No paragraph slides.
- Mobile-first.
- Prefer visual metaphors that can become images later.

Posting plan:

- Treat timing as a hypothesis.
- Ask or infer goal, geography/timezone, platform, urgency, and stagger/immediate preference.
- Include best time, backup time, reason, confidence, and what to test next.

## Creative QA

Before saving final output, score every asset using:

```text
shared\brand\creative_qa_rubric.md
```

If any asset scores below 8/10, rewrite it.

Automatic rewrite triggers:

- weak random joke
- more than 3 tactical bullets/questions in WhatsApp
- subject line sounds generic
- LinkedIn main point appears after line 6
- asset does not use transcript-specific language
- output sounds corporate
- output feels like a summary instead of a promotion asset
- output uses clever or uncommon words where a simpler word would be faster

## Approval

Create `approval.md` for the HTML review workflow.

If `approval.json` is also needed for automation later, keep it internal and do not make Akshat review raw JSON.

All requested items start as pending.

Allowed statuses:

- pending
- approved
- needs_edit
- rejected

External draft creation, if added later, must only use approved items.
