# YouTube Distribution Draft System — Codex Skill Pack v1

Use this file with Akshat's Codex setup prompt.

The goal is to move from a Custom GPT workflow to a Codex project workflow that creates local review-ready YouTube distribution assets.

---

# 1. System Name

`youtube-distribution-draft-system`

This is a separate lightweight skill/workflow.

Do not replace the existing `youtube-slide-video-assets` skill.

Existing slide/video skill is for:
- support slides
- timing packages
- Google Slides / Google Vids
- Clipchamp assets
- MP4 exports
- visual review packages

This distribution skill is for:
- WhatsApp posts
- SendFox email draft content
- HubSpot email draft content
- LinkedIn personal profile posts
- LinkedIn carousel outline and later PDF/image prompt packs
- blog posts
- Shorts/native clip ideas
- Quuu Promote copy
- distribution plan
- recommended posting date/time
- local HTML preview
- approval workflow
- later API draft creation only after approval

---

# 2. Core Rule For V1

V1 is local review only.

Do not:
- send emails
- create external drafts
- publish posts
- schedule posts
- call SendFox, HubSpot, Buffer, LinkedIn, or any external API
- build a Python script that needs an OpenAI/LLM API key

Akshat does not have an OpenAI API key for this workflow.

Use Codex itself to generate the content inside the project.

Scripts are allowed only for deterministic tasks:
- creating folders
- writing Markdown
- writing JSON
- writing HTML
- copying templates
- formatting static files

---

# 3. Expected Folder Structure

Parent folder:

```text
C:\Codex Projects\YT
```

Target structure:

```text
C:\Codex Projects\YT
  \AGENTS.md
  \skills
    \youtube-slide-video-assets
    \youtube-distribution-draft-system
  \shared
    \brand
    \prompts
    \templates
    \examples
  \[Video Name]
    \transcript.txt
    \video_brief.md
    \thumbnail.png
    \distribution
      \output
      \preview.html
      \approval.json
      \draft_results.json
```

Create missing folders safely. Never delete existing folders.

Recommended files to create from this pack:

```text
skills\youtube-distribution-draft-system\SKILL.md
shared\brand\bizamps_distribution_voice.md
shared\prompts\generate_distribution_package.md
shared\templates\distribution_package_template.md
shared\templates\approval_template.json
shared\templates\preview_html_requirements.md
shared\examples\nurture_and_linkedin_examples.md
```

---

# 4. Intake Workflow

When Akshat asks to run the distribution workflow, first ask:

1. Which video folder should I work on?
2. What is the goal?
   - reach
   - trust
   - leads
   - nurture
   - testing
3. Who is the target audience?
4. Which assets do you want?
   - all assets
   - WhatsApp only
   - email only
   - LinkedIn only
   - Shorts/native video only
   - carousel only
   - blog only
   - custom set
5. Platform priority order?
6. Urgency:
   - post now
   - stagger over days
   - no timing needed
7. Geography/timezone:
   - India
   - US
   - UK/EU
   - global
   - custom

If Akshat already gave enough information, do not ask again.

If Akshat says “generate everything,” confirm because output can become too large:

```text
Do you want the full package, or only the first-priority assets for review?
```

---

# 5. Inputs To Read

From selected video folder, prefer:

```text
transcript.txt
video_brief.md
thumbnail.png
```

Optional:

```text
title.txt
youtube_link.txt
timestamps.md
notes.md
existing_post_examples.md
thumbnail_text.txt
```

If missing:
- If transcript is missing, ask Akshat for transcript/script.
- If video brief is missing, create a lightweight `video_brief.md` from available information and ask Akshat to review later.
- If thumbnail is missing, use `[THUMBNAIL PLACEHOLDER]` in preview.

---

# 6. V1 Output Files

Create inside selected video folder:

```text
distribution\
```

Required:

```text
distribution_package.md
preview.html
approval.json
```

Optional:

```text
distribution_package.json
draft_results.json
output\
  whatsapp_posts.md
  sendfox_email.md
  hubspot_email.md
  linkedin_posts.md
  carousel_outline.md
  posting_plan.md
  shorts_ideas.md
  blog_post.md
```

For v1, `draft_results.json` should either not exist or clearly say no external drafts were created.

---

# 7. Content Generation Principle

When the video is already published, Akshat wants views.

Do not start with long strategy diagnosis.

The output should prioritize:
1. clickable hooks and subject lines
2. thumbnail/link placement
3. short insight-led writing
4. fast delivery of value
5. soft CTA to watch the video
6. channel-native formatting

If useful, include only a short `Content Lens` with max 3 bullets:
- main idea
- best hook
- CTA

Do not produce a 40-page content dump unless Akshat explicitly asks for a full package.

Default winning creative category:

```text
Punchy/Funny
```

---

# 8. BizAmps / Akshat Voice

Akshat writes for B2B founders.

The content should feel like:
- one founder explaining hard-earned GTM lessons to another founder
- sharp but practical
- simple but not dumb
- witty but not childish
- useful even if the reader never clicks the video

## Core beliefs

- Most sales problems are actually marketing, messaging, offer, and system problems.
- Outbound alone is rarely enough.
- SDRs are operators. The playbook is the machine.
- Content + offer drives most B2B sales.
- Message-market fit comes before scaling sales headcount.
- Buyers do not move because you asked for a meeting. They move when they see value.
- Useful products still get ignored if there is no attention.
- Founder-led content can create trust before sales calls.
- Outbound is a distribution tool, not a magic machine.
- Lead generation without nurturing wastes attention.
- The real game is mindspace, not just meetings.

## Use this tone

- blunt
- simple
- founder-friendly
- slightly funny
- clear
- high-signal
- practical

## Avoid

- polished corporate consultant tone
- long abstract setups
- fake urgency
- generic AI hype
- motivational-guru lines
- fluffy thought-leadership language
- “I’m excited to share”
- “game-changing”
- “revolutionary”
- “unlock”
- “ultimate guide”
- “crush your pipeline”
- “10x your growth” unless Akshat intentionally uses it
- “in today’s fast-paced world”
- “transform your sales funnel”

## Phrases that fit

- Nobody cares yet.
- Hope is not a GTM motion.
- Useful is not enough.
- The market did not pay enough attention.
- Outbound is the multiplier.
- Trust transfers.
- Attention before conversion.
- Meetings are not pipeline.
- “Interesting” is not revenue.
- Fix the content. Or fix the offer.
- The playbook is the machine.
- More volume helps more people ignore you faster.
- Don’t ask for a meeting. Offer useful effort first.
- Mindspace over meetings.

## CTA style

Preferred:
- Watch the full video.
- Would love your thoughts.
- Reply if useful.
- If this is relevant, watch this part.
- I broke it down here.

Use “book a call” only when Akshat specifically asks for direct sales conversion.

---

# 9. Email Newsletter Rules

For SendFox and HubSpot:

- Give **25 subject lines total**, not 25 separately for each tool.
- Rank top 5.
- Pick final recommended subject.
- Include preview text.
- Include plain text version.
- Include HTML version.
- Thumbnail or thumbnail placeholder must appear near the top, ideally within first 20–30% of the email.
- The video link should be obvious near the top.
- Keep email between 180–350 words unless Akshat asks for a long nurture essay.
- Use a skimmable newsletter layout inspired by Superpower Daily:
  - headline
  - subheadline / hook
  - clickable thumbnail
  - key takeaway
  - short insight
  - bullets
  - CTA button/link
  - timestamps only if useful

Email is not a blog post.
Email should sell the click without feeling empty.

## Recommended plain-text structure

```text
Subject:
Preview text:

Hi {{contact.first_name}},

[Short sharp hook.]

[CLICKABLE THUMBNAIL PLACEHOLDER]

Watch the full video:
[YouTube link]

Key takeaway:
[One punchy useful idea.]

Why it matters:
- bullet
- bullet
- bullet

Best parts:
- timestamp – reason
- timestamp – reason
- timestamp – reason

Would love your thoughts.

-Akshat
```

## HTML email rules

HTML should be simple and portable:
- no external JS
- avoid heavy CSS
- include a clear CTA button-like link
- make thumbnail clickable if thumbnail exists
- use sections/cards lightly
- keep it readable in Gmail/HubSpot/SendFox

---

# 10. WhatsApp Rules

Create 5 WhatsApp group post angles when requested.

Rules:
- personal tone
- short
- founder-friendly
- not desperate
- mostly mention the topic, not BizAmps
- can say “I made a video” or “I broke this down in a video”
- “Hi everyone” is optional
- timestamps optional
- CTA can be “watch the video” or “would love your thoughts”
- posts should not look copy-pasted because group members may overlap

Prefer:
1. problem-led
2. tactical
3. punchy/funny
4. contrarian
5. founder lesson

---

# 11. LinkedIn Personal Profile Rules

When requested, create 3–5 post options and rank them.

If Akshat asks for only one LinkedIn post, generate the strongest likely winner.

Rules:
- Main point must appear within first 5–6 lines.
- Avoid long setup.
- One post = one clear idea.
- Use short paragraphs.
- Make reader smarter even if they do not click.
- Soft video CTA near the end.
- Default winner is usually punchy/funny or tactical.

## Strong opening examples

```text
Your booth is not enough.
```

```text
Cold outbound is not the engine.
```

```text
Most companies waste conferences before they even arrive.
```

```text
Your buyer does not hate your product.
They just do not care yet.
```

```text
Hope is not a GTM motion.
```

## Bad opening examples

```text
In today’s competitive business environment...
```

```text
I recently came across an interesting insight...
```

```text
There are many ways to generate demand...
```

---

# 12. LinkedIn Carousel Rules

Do not automatically create a full carousel unless requested.

If Akshat asks for LinkedIn posts and carousel together:
1. Create post options.
2. Create a carousel outline for the strongest angle.
3. Say: “If you like this angle, I can create the image prompts/PDF-style slide copy next.”

Carousel rules:
- one idea per slide
- fast to scan
- visual
- sticky
- mobile-first
- one sharp statement
- one visual metaphor
- one short supporting line
- no dense bullets
- no paragraph slides
- no blog-post screenshot style
- 8–10 slides max

Every slide should have:
- headline
- short supporting line
- visual direction
- optional image prompt

## Good slide structure

```text
Slide 1
Headline: Your booth is not enough.
Support: Events do not create pipeline by magic.
Visual: Empty booth, busy crowd walking past.
Image prompt: Minimal B2B conference booth ignored by a passing crowd, clean 16:9 layout, bold text space.
```

```text
Slide 2
Headline: Hope is not a GTM motion.
Support: “Interesting” is not pipeline.
Visual: Buyer with tote bag disappearing into crowd.
```

---

# 13. Shorts / LinkedIn Native Video Rules

When requested:
- suggest multiple clips
- rank top 5
- include timestamp or section
- first 3 seconds hook
- on-screen caption
- short title
- why it may retain attention
- platform fit:
  - Shorts
  - LinkedIn native
  - both

Prefer clips with:
- punchline
- clear business pain
- sharp analogy
- founder lesson
- visual moment
- contrarian line

---

# 14. Blog Rules

When requested:
- SEO-friendly but not keyword-stuffed
- founder-advisor tone
- embed video near top
- clear sections
- practical takeaways
- soft CTA to watch full video
- optional Medium repost version with canonical note

Do not generate blog by default unless requested.

---

# 15. Quuu Promote Rules

When requested, create:
- title
- short description
- category suggestion
- CTA
- 3 alternate titles

---

# 16. Distribution Plan / Posting Date-Time Rules

Before recommending posting dates/times, collect or infer:
- goal: reach, trust, leads, nurture, or testing
- target audience geography/timezone
- platform
- urgency
- whether the post should go immediately or staggered

Do not hard-code “best times” as universal truth.

Treat timing as a hypothesis.

For each posting recommendation include:
- best post date/time
- backup date/time
- reason
- confidence level
- what to test next time

Default assumptions if Akshat does not answer:
- Audience: B2B founders in India + US
- Goal: reach + trust
- Platform priority: LinkedIn, email, WhatsApp
- Urgency: publish soon
- Timezone: IST, with US overlap considered

State assumptions clearly.

---

# 17. Approval Workflow

Create:

```text
approval.json
```

All requested channels start as:

```text
"status": "pending"
```

Allowed statuses:
- pending
- approved
- needs_edit
- rejected

Later external draft creation must only happen for items marked:

```text
"status": "approved"
```

## Approval JSON Template

```json
{
  "workflow": "youtube-distribution-draft-system",
  "version": "v1-local-review",
  "video_folder": "C:\\Codex Projects\\YT\\SDR Trap",
  "created_at": "YYYY-MM-DDTHH:MM:SS",
  "external_draft_creation_enabled": false,
  "allowed_statuses": ["pending", "approved", "needs_edit", "rejected"],
  "items": [
    {
      "id": "whatsapp_posts_v1",
      "channel": "whatsapp",
      "asset_type": "group_posts",
      "status": "pending",
      "source_file": "distribution_package.md",
      "notes": ""
    },
    {
      "id": "sendfox_email_v1",
      "channel": "sendfox",
      "asset_type": "email_preview",
      "status": "pending",
      "source_file": "distribution_package.md",
      "notes": ""
    },
    {
      "id": "linkedin_post_v1",
      "channel": "linkedin",
      "asset_type": "personal_profile_post",
      "status": "pending",
      "source_file": "distribution_package.md",
      "notes": ""
    },
    {
      "id": "linkedin_carousel_outline_v1",
      "channel": "linkedin",
      "asset_type": "carousel_outline",
      "status": "pending",
      "source_file": "distribution_package.md",
      "notes": ""
    },
    {
      "id": "posting_plan_v1",
      "channel": "distribution",
      "asset_type": "posting_plan",
      "status": "pending",
      "source_file": "distribution_package.md",
      "notes": ""
    }
  ],
  "draft_results": {
    "external_drafts_created": false,
    "results_file": "draft_results.json",
    "notes": "V1 local review only. Do not create external drafts."
  }
}
```

---

# 18. preview.html Rules

`preview.html` is the main review surface.

It should:
- be readable in browser
- be self-contained
- use clean CSS
- show only assets requested for that run
- have a simple table of contents
- show channel sections as cards
- make the email preview look like a newsletter
- put thumbnail near the top for email
- show LinkedIn posts in card format
- show carousel slides as visual cards
- show approval status as pending
- not require external libraries
- not require internet
- not include external trackers

Recommended styling:
- max width around 900px
- system font stack
- cards
- spacing
- light borders
- subtle background
- copy-friendly preformatted blocks where needed

The HTML preview should not be an ugly raw Markdown dump.

---

# 19. distribution_package.md Template

```markdown
# Distribution Package

## Metadata
- Workflow: youtube-distribution-draft-system
- Version: v1-local-review
- Video folder:
- Video title:
- YouTube link:
- Assets requested:
- Created at:
- External drafts created: No
- Status: Pending review

## Content Lens
Max 3 bullets.
- Main idea:
- Best hook:
- CTA:

## Subject Lines

### 25 total options
1.
2.
3.

### Top 5 ranked
1.
2.
3.
4.
5.

### Final recommended subject
Subject:
Preview text:

## WhatsApp Posts

### Angle 1: Problem
...

### Angle 2: Tactical
...

### Angle 3: Punchy/Funny
...

### Angle 4: Contrarian
...

### Angle 5: Founder Lesson
...

## SendFox Email Preview

### Plain Text
...

### HTML
```html
...
```

## HubSpot Email Preview
Only include if requested.

## LinkedIn Personal Post

### Recommended post
...

### Why this one
...

## LinkedIn Carousel Outline

### Slide 1
- Headline:
- Support:
- Visual direction:
- Image prompt:

## Shorts / Native Clip Ideas
Only include if requested.

## Blog Post
Only include if requested.

## Quuu Promote
Only include if requested.

## Posting Plan
- Goal:
- Audience:
- Platform:
- Best date/time:
- Backup date/time:
- Reason:
- Confidence:
- What to test next time:

## Approval Reminder
All items are pending in approval.json.
No external drafts created.
```

---

# 20. Codex Chat Summary After Generation

After creating files, show a short summary in Codex chat:

- video folder used
- files created
- assets generated
- top 5 subject lines
- recommended LinkedIn winner
- posting plan summary
- reminder that all approvals are pending
- next suggested action

Do not paste every full asset into chat unless Akshat asks. Show key outputs only.

---

# 21. Examples and Style Patterns

These are inspiration, not rigid templates.

## Example: The $50,000 Challenge

```text
The $50,000 Challenge.

If you are a SaaS tool and a client says:

If I paid you $50,000 right now to use your SaaS tool, what’s the maximum value you could deliver, fast?

No fluff. No feature tour.

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
```

Why this works:
- strong thought experiment
- buyer psychology
- outcome over feature
- clear actionable tip
- easy visual idea for carousel

---

## Example: Content + Offer

```text
All B2B sales happen because of content + offer.

Cold email = content + micro-offer.
Demo video/deck = content + micro-offer.
Follow-up email = content + micro-offer.
Sales call = spoken content + structured offer.

Did they move forward?

Fix the content.
Or fix the offer.
```

Why this works:
- simple framework
- visual logic
- one memorable idea
- direct diagnostic

---

## Example: Outbound Team Math

```text
When is an outbound team worth $70K?

5-person team in India:
researcher + cold-email specialist + LinkedIn outreach + sales rep + lead sales assistant

Approx cost:
$70K/year in salaries.

At $20K ACV:
Need 4 new clients just to cover payroll.

At $80K ACV:
Need 2 new clients and you are profitable.

Bottom line:
If your deal size is under $20K, lighter models may make more sense.

Above $70K ACV?
An outbound pod becomes much easier to justify.
```

Why this works:
- uses math
- founder-relevant
- helps a buying decision
- practical, not abstract

---

## Example: Never ask for a meeting first

```text
Do you reply to cold emails that end with:
“Can we meet for 30 minutes?”

Most founders do not.

Why?

Because the buyer assumes the meeting will waste time.

A better move:
Offer useful effort first.

Service provider?
Send a custom strategy.

SaaS tool?
Use public data and send a useful insight.

Management software?
Show a dummy dashboard with their workflow.

Now you are not begging for time.

You are giving them a reason to care.
```

Why this works:
- starts with reader behavior
- reframes the CTA
- gives examples by category
- teaches before selling

---

## Example: Personalized B2B lead magnet

```text
Instead of asking cold prospects for meetings, ask if they want a personalized work product.

A teardown.
A custom campaign idea.
A useful report.
A short strategy document.

AI can help create the first 60–75% of this cheaply.

The point is not to impress them with automation.

The point is to show effort before asking for time.

In a no-USP world, effort becomes the USP.
```

Why this works:
- strong phrase: effort becomes the USP
- shifts meeting ask to value ask
- practical AI use without hype

---

## Example: Lead nurturing

```text
Your prospect may be ready 7.5 months later.

If you only follow up twice, you disappear before they trust you.

Build a 12–24 month nurture sequence.

Send useful ideas.
Do not pitch immediately.
Do not force clicks.
Give the full idea inside the email.

People remember good teachers.
```

Why this works:
- explains long buying cycle
- practical sequence idea
- strong belief: teach before selling

---

## Example: Tools are basics

```text
Tools are not the competitive advantage.

They are the basics.

CRM.
Sales Navigator.
Email nurture.
AI research.
Outreach automation.
Integrations.

The advantage is not owning the tools.

The advantage is knowing what system to build with them.
```

Why this works:
- avoids tool worship
- positions systems thinking
- useful for founders overwhelmed by software

---

## Example: Ruthless experimentation

```text
You ignore 99.99% of pitches in your inbox.

So does your prospect.

The way out is not one perfect offer.

It is ruthless experimentation.

Test:
- pricing page
- demo
- education
- done-for-you layer
- lead magnet
- pilot offer
- homepage headline

No offer is born irresistible.

You experiment your way into market truth.
```

Why this works:
- starts with uncomfortable truth
- gives concrete experiments
- founder-friendly and practical

---

## Example: CAC reality

```text
For B2B SaaS/services with $20K lifetime value:

A qualified meeting may cost around $400.
If 1 client closes every 10 meetings, that is $4,000 before sales salary.
Add sales cost and the real CAC may reach $6,000+.

This is why early-stage teams need:
- retention
- better offers
- focused ICP
- strong nurture
- reality-based CAC math
```

Why this works:
- uses numbers
- gives reality check
- avoids fake cheap lead-gen promises

---

# 22. Good Subject Line Style

Good:
- Your booth is not enough
- Pre-event outbound changes everything
- Nobody cares yet. Now what?
- Cold outbound is not the engine
- Good product. Weak attention. No pipeline.
- Hope is not a GTM motion
- Stop asking for meetings first
- Useful is not enough
- The buyer did not care yet
- Meetings are not the strategy
- The market is not looking for you
- Outbound needs a reason to exist

Bad:
- Unlock your B2B growth potential
- The ultimate guide to outbound success
- 10x your demand generation with AI
- We are excited to share our latest video
- Transform your sales funnel today

---

# 23. SDR Trap Test Run

When testing on:

```text
C:\Codex Projects\YT\SDR Trap
```

First generate only:
1. 5 WhatsApp post angles
2. SendFox email preview with 25 subject lines
3. LinkedIn post
4. LinkedIn carousel outline
5. Recommended posting plan

Create:

```text
C:\Codex Projects\YT\SDR Trap\distribution\distribution_package.md
C:\Codex Projects\YT\SDR Trap\distribution\preview.html
C:\Codex Projects\YT\SDR Trap\distribution\approval.json
```

Do not generate:
- HubSpot
- blog
- Quuu
- Shorts
- external drafts

Unless Akshat asks.

All items must start pending approval.

---

# 24. Final Reminder To Codex

The goal is not to build a giant automation too early.

The goal is to make the first local workflow usable:

1. Read transcript and brief.
2. Generate requested assets.
3. Create clean `preview.html`.
4. Create `approval.json`.
5. Show key outputs in Codex chat.
6. Stop.

No external drafts in v1.
No sending.
No posting.
No scheduling.
No API calls.
