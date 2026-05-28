# Approval

Status: pending_html_review

Primary review file:

```text
review_dashboard.html
```

Primary approval/comment file:

```text
review_dashboard.html
```

Supporting HTML review files:

```text
mobile_preview.html
sendfox_final_preview.html
approval_summary.html
```

## Instructions

Akshat should not edit this Markdown file manually.

Use `review_dashboard.html` to:

- mark each asset as approved, needs_edit, or rejected
- add comments
- generate approval text
- copy a Codex feedback prompt

Then paste that output into Codex.

Codex will update this file and revise content files based on the pasted HTML review output.

## Current Asset Status

| Asset | Status | Notes |
|---|---|---|
| SendFox email preview | pending | Improved conference-specific version created. |
| HubSpot email preview | pending | HTML preview only. No HubSpot API draft. |
| LinkedIn angles | pending | Five angles created, each with full and short version under 900 characters. |
| WhatsApp variants | pending | Ten personal-message variants created. Local copy only. No auto-posting. |
| X/Facebook copy | pending | Local copy only. No publishing. |
| Posting plan | pending | Timing is a hypothesis. |

## External Action Status

Content approval does not approve external actions.

| External Action | Status | Notes |
|---|---|---|
| SendFox read-only test: GET /me | pending | No API call made yet. |
| SendFox read-only test: GET /lists | pending | No API call made yet. Akshat must confirm target list later. |
| SendFox campaign draft creation | pending | Requires content approval, list confirmation, and explicit action approval. Never send or schedule. |
| Buffer read-only channel test | pending | No API call made yet. |
| Buffer LinkedIn draft/queued post | pending | Only if Buffer behavior is confirmed safe. Never publish immediately. |

## Email Defaults

- Recommended subject: 🎟️ Your booth is not enough
- Preview text: Most companies treat conferences like expensive networking trips. The real move starts before the event.
- No-emoji fallback: Your booth is not enough
- Alternate subject: Do pre-event outbound for 2x returns
- The 2x line is not the default because it needs proof before being used as the main claim.

## Hard No

- Do not send SendFox campaign.
- Do not publish LinkedIn immediately.
- Do not publish X/Facebook.
- Do not publish Medium.
- Do not create HubSpot email via API yet.
- Do not auto-post WhatsApp.
- Do not auto-post YouTube Community.
- Do not print or log secrets from `keys.env`.
