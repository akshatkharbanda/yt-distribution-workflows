# Distribution System Plan

## Current Safe Flow

Step A is complete:

1. Source files exist.
2. Local distribution assets are generated.
3. `review_dashboard.html` is ready as the main one-file review surface.
4. `preview.html` and `review.html` remain as backup/specialized review files.

## Next Steps After Approval

1. Akshat reviews `review_dashboard.html`.
2. Akshat records approvals/comments in `review_dashboard.html`.
3. Akshat clicks "Copy Codex feedback prompt" and pastes it into Codex.
4. Codex updates `approval.md` and content files.
5. Check `approval.md`.
6. If SendFox read-only tests are approved:
   - run `GET /me`
   - run `GET /lists`
7. Ask Akshat to confirm the target SendFox list.
8. Create SendFox campaign draft only.
9. Save campaign ID/link if available in `draft_results.md`.
10. Only after SendFox works, test Buffer connection/channel.
11. If Buffer supports a safe draft or queue state, create LinkedIn draft/queued post.
12. If Buffer behavior is unclear, create local fallback file and stop.

## Keys

Use only:

```text
C:\Codex Projects\YT\keys.env
```

Never print, log, or copy secret values.

## OAuth Guidance

SendFox should work with the API token already represented in `keys.env`; Google OAuth is not needed.

Buffer usually uses OAuth to issue access tokens. Since `keys.env` has a Buffer token variable, first test read-only channel access after approval. If the token is expired or lacks scopes, then a Buffer OAuth refresh/setup is needed.

Google OAuth is only needed later for Gmail, Google Drive/Sheets, or YouTube API workflows.

HubSpot draft creation is intentionally excluded from this test.

## Safety Rules

- Never call a SendFox send endpoint.
- Never include `scheduled_at` in SendFox draft creation.
- Never publish LinkedIn immediately.
- Never publish X/Facebook.
- Never publish Medium.
- Never create HubSpot email via API in this test.
- Never auto-post WhatsApp or YouTube Community.
