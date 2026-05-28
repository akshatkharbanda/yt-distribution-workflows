# HubSpot Access Plan

## Goal

Use HubSpot for campaign learning first. Draft creation is optional and unproven for this account.

## Secrets

Store real values only in `keys.env`.

Expected placeholder:

- `HUBSPOT_PRIVATE_APP_TOKEN`

Never print or log the token.

## Questions To Verify

- Can the HubSpot MCP access marketing emails or marketing content in this account?
- Can the HubSpot API retrieve old marketing emails?
- Can the HubSpot API retrieve post-send email statistics?
- Can the HubSpot API create marketing email drafts?
- Does this account expose the needed marketing email scope for private apps?

## Safe Test Order

1. Confirm token/account access without printing secrets.
2. Try read-only marketing email retrieval.
3. Try read-only campaign/stat retrieval if available.
4. Only if read access works, evaluate draft creation capability.
5. Do not publish or send from HubSpot.

## Fallback Workflow

If marketing email API/MCP access is blocked:

- Use manual exports/screenshots for campaign learning.
- Create local `hubspot_email.html`.
- Create local `hubspot_manual_publish_steps.md`.
- Keep HubSpot draft creation out of scope until account access is proven.

## Learning Fields Needed

- Subject
- Preview text
- Send date
- Audience/list
- Opens
- Clicks
- Replies if available
- Linked video/topic
- Unsubscribes or spam complaints if available
