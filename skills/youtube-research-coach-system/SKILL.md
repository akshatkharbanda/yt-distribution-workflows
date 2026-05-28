---
name: youtube-research-coach-system
description: Learn from campaign performance, YouTube analytics, Octolens signals, and external workflow research to prepare local weekly coaching reports and next-video recommendations for BizAmps. This skill never publishes, sends, schedules, auto-replies, or creates external drafts unless a later production workflow explicitly approves a safe draft-only step.
---

# YouTube Research Coach System

Use this skill for the Research / Learning / Coaching thread.

## Purpose

Help Akshat improve YouTube distribution by learning from:

- HubSpot and SendFox campaign history
- YouTube analytics and manual exports
- Octolens keyword and reply opportunities
- GitHub, n8n, Buffer, HubSpot, SendFox, and YouTube workflow research
- Weekly distribution performance
- New video topic demand signals

## Hard Rules

- Do not publish, send, schedule, auto-reply, or create external drafts in this thread.
- Never make Akshat review raw JSON; turn findings into Markdown or HTML.
- Never print secrets or write secrets to logs.
- Do not modify current video production files unless Akshat asks.
- Keep work small, useful, and tied to the business output.
- Verify API assumptions before recommending automation.

## Integration Order

1. Learning-layer files and secrets safety.
2. SendFox connection test: `GET /me`, then `GET /lists`.
3. SendFox draft campaign only after approval, using the Conference Demand video in the Production thread.
4. Buffer connection test and safe LinkedIn draft or queued post only after approval.
5. HubSpot access research and fallback HTML workflow.
6. YouTube Analytics manual export and OAuth plan.

## SendFox Rules

- Allowed first tests: `GET /me` and `GET /lists`.
- Allowed later action: create a draft campaign only.
- Forbidden: send endpoint, `scheduled_at`, automatic sending, or list mutation unless Akshat separately approves.
- Draft creation must omit `scheduled_at`.

## Buffer Rules

- Goal: LinkedIn draft or safe queued post after approval.
- First verify whether Buffer supports a safe draft state through the available account/API.
- If no safe draft state exists, stop and create local Markdown/HTML fallback files.

## HubSpot Rules

- Do not assume marketing email scope is available.
- First research/test whether this account can retrieve old marketing emails, access marketing content, and create marketing email drafts.
- If not available, use:
  - `hubspot_email.html`
  - `hubspot_manual_publish_steps.md`
  - manual exports for campaign learning

## YouTube Analytics Rules

- Do not implement OAuth in this skill until separately approved.
- For v1, accept YouTube Studio screenshots or CSV exports.
- Required coaching fields: video, publish date, impressions, click-through rate, views, average view duration, retention notes, traffic sources, likes, comments, subscribers gained, and external clicks where available.

## Report Output

Weekly coaching reports must include:

- What got posted
- What got views, clicks, and replies
- Top hooks
- Weak hooks
- Missed channels
- Demand signals
- Five next video ideas
- One uncomfortable truth for Akshat
- Risks, missing channels, and recommended next action
