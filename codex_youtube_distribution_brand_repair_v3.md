# Codex Update Pack: YouTube Distribution Brand Repair V3

Use this file as the source of truth for improving the `youtube-distribution-draft-system`.

This is not a new workflow. It is a repair patch for the current workflow.

The current HTML preview and approval workflow are good.
The weak part is the brand/creative layer.

## Goal

Improve the creative quality of the YouTube distribution workflow so Codex produces sharper WhatsApp posts, stronger subject lines, better LinkedIn posts, and cleaner carousel outlines.

The output should feel closer to Akshat's best Custom GPT outputs, not generic marketing copy.

---

# Paste This Prompt Into Codex

```text
Update the current YouTube distribution workflow using the attached "Codex Update Pack: YouTube Distribution Brand Repair V3" as the source of truth.

First inspect:
- C:\Codex Projects\YT\skills\youtube-distribution-draft-system\SKILL.md
- C:\Codex Projects\YT\shared\brand
- C:\Codex Projects\YT\shared\examples
- C:\Codex Projects\YT\shared\prompts
- C:\Codex Projects\YT\shared\templates
- C:\Codex Projects\YT\SDR Trap\distribution\distribution_package.md
- C:\Codex Projects\YT\SDR Trap\distribution\preview.html

Do not replace the existing slide/video asset skill.

Keep:
- local review workflow
- preview.html format
- approval.json
- no external drafts
- no external API calls
- no send/post/publish/schedule behavior

Fix:
1. The brand folder is too thin and generic.
2. The examples folder does not include enough good full examples.
3. The prompt does not force extraction of transcript-native killer lines.
4. Punchy/Funny is not defined tightly, so Codex invents weak jokes.
5. Subject lines are too safe and not pattern-driven.
6. Tactical WhatsApp posts can become too heavy.
7. Contrarian posts can become too obvious.
8. LinkedIn posts need faster value in the first 5 lines.
9. Carousel outlines need to be more visual, less essay-like.
10. Add a creative QA gate before saving final outputs.

Create or replace the files listed in this update pack.

Then regenerate the SDR Trap distribution package using the same requested assets:
- 5 WhatsApp post angles
- SendFox email preview with 25 subject lines
- LinkedIn personal profile post
- LinkedIn carousel outline
- Recommended posting plan

Important:
Use top-level transcript.txt and video_brief.md if available.
If they are missing, ask me before falling back to subtitles/timing files.

Do not create external drafts.
Do not send, post, publish, schedule, or call any external API.
```

---

# Diagnosis: What Went Wrong

## 1. The workflow skeleton is fine

The current `SKILL.md` correctly says this is a local review workflow and must not send, publish, schedule, create external drafts, or call external APIs.

Keep that.

The current skill also correctly creates:
- `distribution_package.md`
- `preview.html`
- `approval.json`
- optional split output files

Keep that too.

## 2. The brand folder is too generic

Current brand guidance is directionally right but too thin.

It says:
- blunt
- simple
- founder-friendly
- slightly funny
- high-signal
- practical

That is not enough.

Every B2B content prompt says this now. It does not teach taste.

The result: Codex created a weak joke like:

> Hiring SDRs without a playbook is like buying gym shoes and expecting abs by Friday.

This is not Akshat's voice.

Akshat's better version is closer to:

> A founder hires 2 SDRs and a “VP of Sales.”
>
> 3 months later:
> Calendar empty.
> Burn rate vertical.
> Team confused.
> Market still does not care.
>
> That is not scaling.
>
> That is gambling with payroll.

This works because it uses founder pain, cost, embarrassment, and the video's own thesis.

## 3. The workflow ignored the transcript's strongest lines

For the SDR Trap video, the script already has strong lines:

- You aren’t scaling. You’re gambling.
- The house always wins.
- You copied their public payroll, not their private process.
- SDRs are not the machine. SDRs are operators.
- The playbook is the machine.
- If the message is dead, volume just helps more people ignore you faster.
- That’s industrialized rejection.
- Scaling a system also scales its problems.
- Build the playbook first.

Codex should first mine these lines before writing.

Do not invent analogies until transcript-native lines have been extracted and tested.

## 4. The examples folder needs full examples, not just hooks

A hook list is not enough.

Codex needs:
- good WhatsApp post examples
- bad WhatsApp post examples
- good subject line examples
- bad subject line examples
- good LinkedIn post examples
- carousel slide style examples
- QA scoring rubric

## 5. Punchy/Funny must be defined

Punchy/Funny does NOT mean random jokes.

It means:
- sharp founder pain
- mild absurdity
- real business consequence
- compressed story
- no sitcom analogies
- no cute metaphors unless they come from the transcript
- no jokes that could be posted by a LinkedIn intern

Good humor:
> Your ideal buyer walked past your booth.
> Grabbed a tote bag.
> Said “interesting.”
> Then disappeared forever.

Bad humor:
> Hiring SDRs without a playbook is like buying gym shoes and expecting abs by Friday.

---

# Files To Create Or Replace

Create or replace the following files:

```text
C:\Codex Projects\YT\shared\brand\bizamps_distribution_voice.md
C:\Codex Projects\YT\shared\brand\creative_qa_rubric.md
C:\Codex Projects\YT\shared\examples\akshat_style_examples.md
C:\Codex Projects\YT\shared\examples\subject_line_examples.md
C:\Codex Projects\YT\shared\examples\whatsapp_examples.md
C:\Codex Projects\YT\shared\examples\linkedin_examples.md
C:\Codex Projects\YT\shared\prompts\generate_distribution_package.md
C:\Codex Projects\YT\shared\prompts\creative_generation_process.md
C:\Codex Projects\YT\skills\youtube-distribution-draft-system\SKILL.md
```

---

# Replacement File: shared/brand/bizamps_distribution_voice.md

```markdown
# BizAmps Distribution Voice

Audience:
B2B founders and revenue leaders, especially SaaS, IT services, AI services, and founder-led sales teams.

Core job:
Turn one YouTube video into distribution assets that get views, build trust, and create mindspace.

The output should feel like one founder warning another founder about an expensive GTM mistake.

## Voice

Write like Akshat:
- blunt
- simple
- founder-to-founder
- practical
- slightly witty
- high-signal
- no corporate fog
- no guru motivation
- no generic AI hype

## Core Beliefs

- Most sales problems are actually messaging, offer, market, and system problems.
- SDRs are operators. The playbook is the machine.
- More volume makes a weak message fail faster.
- Message-market fit comes before scaling headcount.
- Buyers move when they see value, not because someone asked for a meeting.
- Founder-led content can build trust before sales calls.
- Mindspace matters before meetings.
- Content + offer drives sales.
- Features do not sell. Outcomes do.
- Useful is not enough. Distribution matters.
- Outbound should often attach itself to trust, events, partnerships, content, or proof assets.
- Hope is not a GTM motion.

## What Punchy/Funny Means

Punchy/Funny does NOT mean random jokes.

It means using:
- founder pain
- payroll burn
- empty calendar
- market indifference
- awkward sales reality
- costly mistakes
- slightly dark business humor

Good:
A founder hires 2 SDRs and a “VP of Sales.”

3 months later:
Calendar empty.
Burn rate vertical.
Team confused.
Market still does not care.

That is not scaling.

That is gambling with payroll.

Bad:
Hiring SDRs without a playbook is like buying gym shoes and expecting abs by Friday.

Why bad:
It is generic. It could be about anything. It does not use the video's actual language or founder pain.

## Preferred Line Patterns

Use patterns like:

- You are not scaling. You are gambling.
- The SDR is not the machine. The playbook is the machine.
- You copied the public payroll. Not the private process.
- More volume just helps more people ignore you faster.
- A dead message at 10x speed is still dead.
- Meetings are not pipeline.
- Hope is not a GTM motion.
- Useful is not enough.
- Nobody cares yet.
- Good product. Weak attention. No pipeline.
- Your booth is not enough.
- Outbound is not the engine. It is the multiplier.
- Build the playbook before the team.
- Payroll is not pipeline.
- More reps can create a bigger mess.

## Avoid

Never use:
- excited to share
- game-changing
- revolutionary
- unlock
- ultimate guide
- crush your pipeline
- in today's fast-paced world
- transform your business
- skyrocket
- unleash
- growth hack, unless used critically
- generic AI-powered magic
- polished corporate consultant tone
- motivational LinkedIn guru tone

## Default CTA

Use one of:
- Watch the full video.
- I broke this down in the full video.
- Would love your thoughts.
- If this is relevant, watch the full video.

Avoid hard CTAs unless Akshat asks:
- Book a call
- Schedule a demo
- Talk to us today
```

---

# New File: shared/brand/creative_qa_rubric.md

```markdown
# Creative QA Rubric

Before saving any final asset, score it out of 10.

If any asset scores below 8, rewrite it.

## Scoring

### 1. Transcript specificity: 0-2 points

2 = Uses the video's actual sharp lines, examples, or metaphors.
1 = Uses the general idea but not the strongest wording.
0 = Generic and could apply to any video.

### 2. Founder relevance: 0-2 points

2 = Speaks to founder pain: payroll, burn, weak pipeline, risk, wasted hiring, market ignoring them.
1 = Mildly relevant.
0 = Sounds like generic marketing advice.

### 3. Hook strength: 0-2 points

2 = First 1-3 lines create curiosity or recognition.
1 = Okay but slow.
0 = Weak setup, generic intro, or obvious point.

### 4. Clarity: 0-2 points

2 = Simple, direct, no dense paragraphs.
1 = Understandable but slightly heavy.
0 = Too wordy, abstract, or consultant-like.

### 5. Akshat voice: 0-2 points

2 = Blunt, practical, slightly witty, founder-to-founder.
1 = Close but too safe.
0 = Corporate, generic, or cute.

## Automatic Fail Rules

Rewrite immediately if the asset:
- starts with "I am excited to share"
- uses "game-changing", "unlock", "revolutionary", "ultimate guide", or "skyrocket"
- uses a generic analogy not present in the transcript
- has more than 3 questions in a WhatsApp post
- has a LinkedIn post where the main point appears after line 6
- sounds like a newsletter intern wrote it
- uses random humor instead of business pain
- summarizes the whole video instead of teasing one sharp idea

## Good Enough Standard

The asset should pass this test:

"Would Akshat plausibly post this without rewriting 70% of it?"

If no, rewrite.
```

---

# New File: shared/examples/whatsapp_examples.md

```markdown
# WhatsApp Examples

WhatsApp should sound personal, useful, and low-pressure.

It can say:
- I made a video
- I broke this down in a video
- Watch the full video
- Would love your thoughts

It should not sound like a newsletter blast.

## Good Punchy/Funny Example: SDR Trap

A founder hires 2 SDRs and a “VP of Sales.”

3 months later:
Calendar empty.
Burn rate vertical.
Team confused.
Market still does not care.

That is not scaling.

That is gambling with payroll.

Broke this down in a video:
[VIDEO LINK]

## Good Contrarian Example: SDR Trap

SDRs are not the machine.

They are operators.

The machine is the outbound playbook:

- which pain creates curiosity
- which proof asset moves buyers
- which message does not get ignored

If the playbook is broken, hiring more reps just creates a bigger mess.

I made a video on this:
[VIDEO LINK]

## Good Problem-Led Example: SDR Trap

I made a video on a common founder trap:

Raise money.
Hire SDRs.
Buy tools.
Increase volume.

Then wonder why pipeline is still empty.

The problem is usually not the SDR.

It is the missing playbook.

Watch the full video:
[VIDEO LINK]

## Good Tactical Example: SDR Trap

Before hiring SDRs, answer 3 questions:

1. Which buyer actually replies?
2. Which pain creates curiosity?
3. Which proof asset moves them from “interesting” to “let’s talk”?

That is the playbook.

The SDR only operates it.

Watch the full video:
[VIDEO LINK]

## Good Founder Lesson Example: SDR Trap

The first 6 months of outbound are not wasted if you use them properly.

Even 1-2 good replies out of 100 can teach you:

- which pain matters
- which buyer is active
- which message earns attention

That is how the playbook gets built.

Watch the full video:
[VIDEO LINK]

## Bad Example

Hiring SDRs without a playbook is like buying gym shoes and expecting abs by Friday.

Nice shoes.

Still no system.

Why this is bad:
- too generic
- too cute
- not tied to the transcript
- does not feel like Akshat
- business pain is weaker than the original script
```

---

# New File: shared/examples/subject_line_examples.md

```markdown
# Subject Line Examples

Generate 25 total subject lines for SendFox + HubSpot combined.

Do not generate 25 for each tool.

Subject lines should be short, sharp, and linked to the video thesis.

## Subject Line Categories

For every video, generate a mix:

1. Blunt thesis
2. Founder pain
3. Tactical curiosity
4. Punchy/funny
5. Cost/risk/consequence
6. Transcript-native killer line

## SDR Trap Example Subject Lines

1. You’re not scaling. You’re gambling.
2. The SDR trap
3. Your first SDR is not strategy
4. Public payroll. Private process.
5. SDRs are not the machine
6. Don’t hire the operator first
7. Build the playbook first
8. Calendar empty. Burn vertical.
9. More reps, bigger mess
10. Stop copying SaaS headcount
11. Outbound before playbook hurts
12. The house always wins
13. You copied the wrong thing
14. Message-market fit before SDRs
15. More volume won’t save you
16. Your VP of Sales can’t fix this
17. The hidden outbound playbook
18. Hiring SDRs too early?
19. Payroll is not pipeline
20. Your outbound machine is missing
21. The 1% reply reality
22. Industrialized rejection
23. Founders: feel the market punch
24. The valley of unknown
25. Build the machine first

## Conference Demand Example Subject Lines

1. Your booth is not enough
2. Pre-event outbound changes everything
3. Nobody cares yet. Now what?
4. Cold outbound is not the engine
5. Hope is not a GTM motion
6. Your buyers walked past you
7. Stop hoping buyers find you
8. Useful is not enough
9. Good product. Weak attention.
10. Events are not pipeline
11. Outbound needs trust
12. Attach outbound to attention
13. The tote bag problem
14. Conferences need pre-selling
15. The market does not care yet
16. Attention before meetings
17. Your event ROI is leaking
18. The booth is a trap
19. Distribution beats waiting
20. Buyers need repeated signals
21. Warm the room first
22. Pre-book the event
23. Outbound is the multiplier
24. Nobody cares. Build demand.
25. Don’t waste the conference

## Bad Subject Lines

Bad:
- Unlock your outbound potential
- The ultimate SDR guide
- Game-changing sales strategy
- Transform your pipeline today
- How to revolutionize outbound

Why bad:
- generic
- fake hype
- not Akshat's voice
- no founder pain
- no specific video insight

## Ranking Rule

The top 5 should prioritize:
1. Curiosity
2. Specificity
3. Founder pain
4. Video-native language
5. Clickability without cheap hype

Do not always pick the safest subject line.
```

---

# New File: shared/examples/linkedin_examples.md

```markdown
# LinkedIn Examples

LinkedIn posts must get to the point fast.

The main idea should appear by line 5 or 6.

Do not slowly build up.

## Good LinkedIn Pattern: Founder Math

When is an outbound team worth $70K?

5-person outbound pod in India:
Researcher.
Cold email specialist.
LinkedIn outreach.
Sales rep.
Lead assistant.

Approx cost:
$70K/year in salaries.

Now the math:

At $20K ACV:
You need 4 new clients just to cover payroll.

At $80K ACV:
You need 2 clients and you are already in profit.

This is why deal size matters.

If your deal size is under $20K, a lighter model may make more sense:

- outsourcing
- interns + AI
- founder-led sales
- automation

Above $70K?

A proper outbound pod becomes much easier to justify.

Founder lesson:

Do not copy someone else's sales team.

First check if your unit economics can carry it.

## Good LinkedIn Pattern: Content + Offer

I think all sales happen because of CONTENT + OFFER.

Cold email?
Content + micro-offer.

Demo video?
Content + micro-offer.

Follow-up email?
Content + micro-offer.

Sales call?
Spoken content + structured offer.

Simple test:

Did they move forward?

If no, fix the content or fix the offer.

Most teams keep changing the channel.

Wrong diagnosis.

The channel is usually just the delivery truck.

The thing inside the truck is the content + offer.

## Good LinkedIn Pattern: SDR Trap

Your first SDR is not a strategy.

It is a payroll line.

A founder raises money.

Then the first move feels obvious:

Hire SDRs.
Add a VP of Sales.
Buy tools.
Increase volume.

Three months later:

Calendar empty.
Burn rate vertical.
Team confused.
Market still does not care.

That is not scaling.

That is gambling with payroll.

The SDR is not the machine.

The SDR is the operator.

The machine is the outbound playbook:

- which pain creates curiosity
- which proof asset moves buyers
- which message does not get ignored

If the playbook is broken, hiring more reps just creates a bigger mess.

I broke this down in the full video.

## Bad LinkedIn Pattern

A lot of founders today are trying to grow their businesses and generate more pipeline through outbound sales. However, many of them do not realize that there are multiple steps involved in building a successful outbound engine...

Why bad:
- slow
- generic
- no strong first line
- main point comes too late
- sounds like a blog intro
```

---

# New File: shared/examples/akshat_style_examples.md

```markdown
# Akshat Style Examples

Use these examples to understand the writing style.

## Example: $50,000 Challenge

The $50,000 Challenge.

If you are a SaaS tool and a client says:

If I paid you $50,000 right now to use your SaaS tool, what’s the maximum value you could deliver, fast?

No fluff.
No feature tour.

Just:

“Here’s what we’d do, here’s what you’d get.”

This is the test most SaaS companies fail.

They’re stuck in the “we have lots of features” trap.

Endless updates.
Beautiful UI.
But no clear path to impact.

Here’s the truth:

Features don’t sell.
Outcomes do.

Every buyer is secretly thinking:

“If I buy this today, what real results will I get?”

If your demo can’t answer that in 90 seconds, you’re not ready to scale.

Tip:

Build a $50,000 Use Case Video.

Pick your best integration.
Solve one high-impact pain.
Show the before/after.
Record it once.
Let it sell while you sleep.

It’s not about features.

It’s about focus.

## Style Notes

This works because:
- Strong named concept
- Thought experiment
- Clear buyer psychology
- Simple short paragraphs
- Practical takeaway
- No fluff
- No fake hype
```

---

# New File: shared/prompts/creative_generation_process.md

```markdown
# Creative Generation Process

Use this process before writing final assets.

## Step 1: Extract Killer Lines

Read the transcript/script and extract 10-20 lines that could become:
- hooks
- subject lines
- WhatsApp punchlines
- LinkedIn opening lines
- carousel slide headlines

Look for:
- sharp claims
- founder pain
- jokes
- metaphors
- cost/risk/consequence
- memorable wording
- counterintuitive lines

For SDR Trap, examples include:
- You aren’t scaling. You’re gambling.
- The house always wins.
- You copied their public payroll, not their private process.
- The hidden playbook.
- SDRs are not the machine.
- SDRs are operators.
- The playbook is the machine.
- If the message is dead, volume just helps more people ignore you faster.
- Industrialized rejection.
- Build the playbook first.

## Step 2: Choose One Primary Distribution Hook

Do not summarize the whole video.

Choose one hook for the current asset batch.

Examples:
- SDR Trap: "The SDR is not the machine. The playbook is the machine."
- Conference Demand: "Cold outbound is not the engine. It is the multiplier."
- Offer/Content: "Fix the content. Or fix the offer."

## Step 3: Generate Candidates

For each requested asset, generate multiple candidates internally:
- WhatsApp: 2 candidates per angle
- Subject lines: 40 raw lines, then shortlist 25
- LinkedIn: 3 post structures, then choose 1
- Carousel: 2 possible narratives, then choose 1

Only save the strongest final outputs.

## Step 4: Apply Channel Rules

WhatsApp:
- short
- personal
- no more than 3 bullets/questions
- no heavy setup
- must feel forwardable

Email:
- 25 total subject lines
- top 5 ranked
- thumbnail near top
- skimmable
- short hook before thumbnail
- key takeaway box
- CTA to watch

LinkedIn:
- main point by line 5
- short paragraphs
- one strong idea
- should be useful even if they do not watch

Carousel:
- one idea per slide
- one sharp statement
- one short support line
- one visual metaphor
- no dense bullets
- mobile-first

## Step 5: Creative QA

Use `shared/brand/creative_qa_rubric.md`.

If score is below 8/10, rewrite before saving.
```

---

# Replacement File: shared/prompts/generate_distribution_package.md

```markdown
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
9. Create `preview.html`.
10. Create `approval.json`.
11. Show a short summary in chat.

## Hard Rules

- Do not send, post, publish, schedule, or create external drafts.
- Do not call external APIs.
- Do not build an LLM API script.
- All approvals start as pending.
- `preview.html` is the main review surface.
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
3. Draft multiple candidates.
4. Run QA rubric.
5. Rewrite weak assets.
6. Save only final version.

## Output Rules

Subject lines:
- 25 total only.
- Rank top 5.
- Pick final recommended subject.
- Use the subject-line examples file as reference.

WhatsApp:
- 5 different angles.
- Use the WhatsApp examples file.
- Tactical posts max 3 bullets/questions.
- Punchy/Funny must use founder pain, not generic jokes.

Email:
- Thumbnail/link near top.
- Skimmable newsletter preview.
- 180-350 words unless Akshat asks for longer.
- Include plain text and HTML preview.

LinkedIn:
- Main point in first 5-6 lines.
- One idea only.
- No slow blog intro.

Carousel:
- 8-10 slides.
- One sharp statement per slide.
- One short support line.
- One visual metaphor.
- No paragraph slides.

Posting plan:
- Timing is a hypothesis.
- Include best time, backup, reason, confidence, and what to test.
```

---

# Replacement File: skills/youtube-distribution-draft-system/SKILL.md

```markdown
---
name: youtube-distribution-draft-system
description: Create local review-ready YouTube distribution assets from a transcript or video brief, including WhatsApp posts, email previews, LinkedIn posts, carousel outlines, posting plans, preview.html, and approval.json. V1 is local review only and must not send, publish, schedule, or create external drafts.
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

- `distribution_package.md`
- `preview.html`
- `approval.json`

Optional:

- `output\whatsapp_posts.md`
- `output\sendfox_email.md`
- `output\linkedin_post.md`
- `output\carousel_outline.md`
- `output\posting_plan.md`

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
- fake urgency
- motivational-guru lines
- "excited to share"
- "game-changing"
- "revolutionary"
- "unlock"
- "ultimate guide"
- "skyrocket"
- "in today's fast-paced world"

Default CTA:

```text
Watch the full video.
```

## Asset Rules

WhatsApp:

- Create 5 different angles.
- Keep posts short and personal.
- Avoid making every post look copied.
- Tactical posts must have maximum 3 bullets/questions.
- Punchy/Funny posts should use business pain from the transcript, not random jokes.
- Prefer compressed founder stories.

Email:

- Give 25 subject lines total.
- Rank the top 5.
- Pick one final recommended subject.
- Include preview text.
- Include plain text preview.
- Include HTML preview.
- Thumbnail/link must appear near the top.
- Keep it skimmable and click-focused.

LinkedIn personal post:

- Main point should appear in the first 5 to 6 lines.
- One post should have one clear idea.
- CTA should be soft and near the end.
- Avoid slow setup and blog-intro style.

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

## Approval

Create `approval.json`.

All requested items start as pending.

Allowed statuses:

- pending
- approved
- needs_edit
- rejected

External draft creation, if added later, must only use approved items.
```

---

# SDR Trap Regeneration Guidance

When regenerating SDR Trap, use these source-native lines as the creative raw material:

```text
A founder raises another round of funding.

Their first move?

Hire two SDRs and a “VP of Sales.”

Three months later, their calendar is empty.

Their burn rate is vertical.

You aren’t scaling.

You’re gambling.

The house always wins.

You copied their public payroll.

Not their private process.

SDRs are not the machine.

SDRs are operators.

The playbook is the machine.

If the process is broken, adding more operators doesn’t give you more output.

It just creates a big mess with a bigger payroll.

If the message is dead, volume just helps more people ignore you faster.

That’s industrialized rejection.

The first six months are not wasted.

Build the playbook first.

Scaling a system also scales its problems.
```

## Required Better WhatsApp Outputs For SDR Trap

Use these as the baseline quality bar.

### Punchy/Funny

```text
A founder hires 2 SDRs and a “VP of Sales.”

3 months later:
Calendar empty.
Burn rate vertical.
Team confused.
Market still does not care.

That is not scaling.

That is gambling with payroll.

Broke this down in a video:
[VIDEO LINK]
```

### Contrarian

```text
SDRs are not the machine.

They are operators.

The machine is the outbound playbook:

- which pain creates curiosity
- which proof asset moves buyers
- which message does not get ignored

If the playbook is broken, hiring more reps just creates a bigger mess.

I made a video on this:
[VIDEO LINK]
```

### Tactical

```text
Before hiring SDRs, answer 3 questions:

1. Which buyer actually replies?
2. Which pain creates curiosity?
3. Which proof asset moves them from “interesting” to “let’s talk”?

That is the playbook.

The SDR only operates it.

Watch the full video:
[VIDEO LINK]
```

## Required Better Subject Line Direction For SDR Trap

Generate 25, but make sure these are included in the candidate pool:

```text
You’re not scaling. You’re gambling.
The SDR trap
Public payroll. Private process.
SDRs are not the machine
Payroll is not pipeline
Build the playbook first
More reps, bigger mess
The house always wins
You copied the wrong thing
Industrialized rejection
Calendar empty. Burn vertical.
The hidden outbound playbook
Your VP of Sales can’t fix this
Don’t hire the operator first
Message-market fit before SDRs
```

---

# Success Criteria

After update, Codex output should:

1. Keep the same useful HTML review format.
2. Produce WhatsApp posts close to Custom GPT quality.
3. Use transcript-native punchlines.
4. Avoid generic invented jokes.
5. Give stronger subject lines.
6. Keep tactical WhatsApp posts to 3 bullets/questions.
7. Make LinkedIn posts land the main point by line 5.
8. Keep carousel slides visual and mobile-first.
9. Save all outputs locally only.
10. Keep all approval statuses pending.

```
Do not move to external draft creation yet.
V3 is still local review only.
```
