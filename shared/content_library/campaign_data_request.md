# Campaign Data Request

This file lists exactly what is needed to pull old campaign learnings for the YouTube distribution system.

## HubSpot

Preferred:

- HubSpot MCP access, if it can read marketing email or marketing content.
- Or a HubSpot private app token with the available marketing email/content scopes.

Need to verify:

- Can the account retrieve old marketing emails?
- Can the account retrieve marketing email performance stats?
- Can the account create marketing email drafts?
- Does the private app actually expose marketing email scope in this portal?

If API/MCP access is not available:

- Export campaign/email performance from HubSpot manually.
- Provide screenshots or CSVs with subject, preview text, send date, audience/list, opens, clicks, replies if available, and linked topic/video.
- Use local fallback files: `hubspot_email.html` and `hubspot_manual_publish_steps.md`.

## SendFox

Preferred:

- SendFox API token in `keys.env`.
- Sender name and sender email.

First safe tests:

- `GET /me`
- `GET /lists`

Need for draft campaign creation later:

- Approved subject line
- Preview text
- HTML body
- From name
- From email
- Target list ID, only after Akshat confirms the list

Forbidden:

- Send endpoint
- `scheduled_at`
- Automatic sending

If API access is not available:

- Export campaign data from SendFox manually.
- Provide CSV/screenshots with subject, preview text, open rate, click rate, send date, audience/list, and linked video/topic.

## YouTube Analytics

There is no simple YouTube Studio API key path for this workflow.

For API access later, use Google OAuth for the YouTube Analytics API.

For v1 manual learning, provide:

- Video title
- YouTube URL
- Publish date
- Date range
- Impressions
- Click-through rate
- Views
- Average view duration
- Retention highlights or screenshot
- Traffic sources
- Likes
- Comments
- Subscribers gained
- External clicks if available

## Campaign Fields Needed

For each campaign or post, collect:

- Channel
- Video/topic
- Subject or hook
- Preview text or opening line
- Body/link used
- Send/post date
- Audience/list
- Opens
- Clicks
- Replies/comments
- Views if applicable
- Notes on what looked strong or weak

## Fallback Rule

If API access is blocked, use manual exports, screenshots, or copied tables. The learning layer should still produce a weekly Markdown/HTML coaching report.
