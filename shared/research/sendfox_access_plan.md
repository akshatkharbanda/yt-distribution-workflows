# SendFox Access Plan

## Goal

Make SendFox the first real integration because draft campaign creation is allowed and safer than direct publishing.

## Secrets

Store real values only in `keys.env`.

Expected placeholders:

- `SENDFOX_API_TOKEN`
- `SENDFOX_FROM_NAME`
- `SENDFOX_FROM_EMAIL`

Never print the token. Never log the token.

## Phase 1: Connection Test

Allowed calls:

- `GET https://api.sendfox.com/me`
- `GET https://api.sendfox.com/lists`

Output should be human-readable:

- Account name/email redacted if needed.
- Contact count.
- Available list names and IDs.
- Any access errors.

## Phase 2: Draft Campaign Test

Only after Akshat approves the Conference Demand content and target list.

Allowed call:

- `POST https://api.sendfox.com/campaigns`

Required body fields:

- `title`
- `subject`
- `preview_text`
- `html`
- `from_name`
- `from_email`
- `lists`

Safety rules:

- Omit `scheduled_at`.
- Never call `/send`.
- Never create or edit lists during this workflow.
- Confirm the created campaign remains unsent.

## Fallback

If API access fails, create:

- `sendfox_email.html`
- `sendfox_manual_publish_steps.md`
- Local campaign preview in Markdown/HTML
