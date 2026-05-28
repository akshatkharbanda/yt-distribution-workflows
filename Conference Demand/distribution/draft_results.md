# Draft Results

Status: SendFox draft created

## SendFox

- Connection test `GET /me`: completed
- Connection test `GET /lists`: completed
- Target list: BizAmps's U.S Interested leads
- Target list ID: 631826
- Campaign draft: created
- Campaign ID: 2830202
- Campaign title: Conference Demand - Your booth is not enough
- Subject: 🎟️ Your booth is not enough
- Preview text: Most companies treat conferences like expensive networking trips. The real move starts before the event.
- `scheduled_at`: omitted
- `sent_at`: blank on read-back
- Send endpoint called: no
- Campaign link: not returned by API
- Formatting issue found in SendFox UI: body spacing needs stronger email-safe paragraph and button spacing.
- Existing draft should not be edited, sent, or scheduled without Akshat approval.
- Preferred future sender name: 🧠 Akshat from BizAmps
- Future list selection may include multiple lists based on config.

## Where To Verify

Open SendFox and check Campaigns/Drafts for:

```text
Conference Demand - Your booth is not enough
```

or campaign ID:

```text
2830202
```

## Buffer

- Connection test: not run
- Channel check: not run
- Target channel: not selected
- LinkedIn draft/queued post: not created

## Notes

- No Buffer, HubSpot, X/Facebook, Medium, WhatsApp, or YouTube publishing action was taken.
- Secrets from `keys.env` were not printed or saved.
- Next fix: use improved email-safe spacing and normal-sized CTA buttons before any future draft update.
