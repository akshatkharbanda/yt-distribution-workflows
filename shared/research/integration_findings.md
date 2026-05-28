# Integration Findings

Updated: 2026-05-26

## Current Build Order

### Phase 1

- Learning-layer files.
- Secrets safety.

### Phase 2

- SendFox connection test.
- SendFox real draft campaign from Conference Demand after approval.

### Phase 3

- Buffer connection test.
- Buffer LinkedIn draft or queued post from Conference Demand after approval.

### Phase 4

- HubSpot access research.
- HubSpot fallback HTML workflow.

### Phase 5

- YouTube Analytics manual export and OAuth plan.

## SendFox

Findings from SendFox docs:

- Personal access tokens use bearer auth.
- `GET /me` can verify the current user.
- `GET /lists` can retrieve lists.
- `POST /campaigns` creates a campaign as a draft.
- `scheduled_at` schedules sending and must be omitted for draft-only work.
- `POST /campaigns/{id}/send` sends immediately and is forbidden here.
- Campaign stats can include sent count, opens, clicks, bounces, unsubscribes, spam, and rates.

Decision:

- First live test should only call `GET /me` and `GET /lists`.
- Draft creation is allowed later only after Akshat approves content and list selection.

Source:

- SendFox API docs: https://sendfox.com/developer/docs/

## Buffer

Findings from Buffer docs:

- Buffer has API support for posts, ideas, profiles, scheduled posts, and sent posts.
- Buffer Help Center describes draft posts in the product.
- Need to verify whether the connected API/account exposes a safe draft state for LinkedIn.

Decision:

- Test connection first.
- If safe draft creation is available, use it only after approval.
- If only immediate publishing is available, stop and create local fallback files.

Sources:

- Buffer developer docs: https://developers.buffer.com
- Buffer API help: https://support.buffer.com/article/859-does-buffer-have-an-api
- Buffer draft help: https://support.buffer.com/article/656-saving-and-scheduling-draft-posts

## HubSpot

Findings from HubSpot docs:

- Marketing Emails v3 API can create, update, retrieve marketing emails, and query post-send statistics.
- It does not cover one-to-one sales emails from contact records.
- Publishing/unpublishing has account-level restrictions.
- This account may not expose marketing email scope through a private app.

Decision:

- Do not assume HubSpot draft creation works.
- First test access/read capability.
- If blocked, use manual exports for learning and local HTML/manual publishing steps.

Source:

- HubSpot Marketing Email API docs: https://developers.hubspot.com/docs/api-reference/legacy/marketing/marketing-emails/guide

## YouTube Analytics

Findings from Google docs:

- YouTube Analytics API requests require OAuth authorization.
- Relevant read scope: `https://www.googleapis.com/auth/yt-analytics.readonly`.
- Reports are queried through `GET https://youtubeanalytics.googleapis.com/v2/reports`.

Decision:

- Do not implement OAuth yet.
- For v1, use manual YouTube Studio exports/screenshots.

Source:

- YouTube Analytics Reports Query docs: https://developers.google.com/youtube/analytics/reference/reports/query
