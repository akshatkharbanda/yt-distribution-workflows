# Draft Automation Log

## 2026-05-26

- Migrated active work to `C:\Codex Projects\YT\Conference Demand`.
- Old misspelled folder `Demand and Confrences` is empty but still locked by Windows, so it could not be removed yet.
- Created source files from Akshat's provided video title, transcript, planned script, YouTube link, and brief.
- Created local Step A review package:
  - `preview.html`
  - `distribution_package.md`
  - `approval.md`
  - split output files
  - `draft_results.md`
  - `publish_results.md`
- Did not read or print secret values from `keys.env`.
- Did not call SendFox, Buffer, HubSpot, LinkedIn, X/Facebook, Medium, WhatsApp, or YouTube APIs.
- No external drafts, sends, posts, publishes, or schedules were created.

## 2026-05-26 HTML Review Update

- Updated the review workflow so Akshat reviews HTML first.
- Added `review.html` for approvals, comments, generated `approval.md` content, and Codex feedback prompt.
- Improved SendFox and HubSpot email previews using Akshat's conference-specific structure.
- Added `sendfox_email_improved.html`, `hubspot_email_improved.html`, and `email_comparison.html`.
- No external API calls, sends, posts, publishes, or schedules were created.

## 2026-05-27 HTML Safety Review Update

- Changed the recommended SendFox/HubSpot subject to `Your booth is not enough`.
- Kept `Do pre-event outbound for 2x returns` only as an alternate subject because the numeric claim needs proof before becoming the default.
- Separated content approval from external action approval in `review.html`.
- Added `sendfox_final_preview.html`, `mobile_preview.html`, and `approval_summary.html`.
- Added a short LinkedIn version under 900 characters alongside the full founder-essay version.
- Updated the reusable distribution skill and shared prompt/template rules to use HTML-first review, separate external action approval, and safer subject-line defaults.
- No external API calls, sends, posts, publishes, or schedules were created.

## 2026-05-27 Review Dashboard Update

- Created `review_dashboard.html` as the main one-file review surface.
- Dashboard combines content preview, mobile preview, approval controls, comments, copy buttons, missed-channel checklist, SendFox safety preview, and Buffer safety preview.
- Added 5 LinkedIn angles with full and short versions.
- Added 10 WhatsApp variants in a more personal message format.
- Added `output\angle_matrix.md`.
- Updated the recommended subject to `🎟️ Your booth is not enough`, with `Your booth is not enough` as no-emoji fallback.
- Updated reusable workflow rules so future videos use `review_dashboard.html` as the main review file.
- No external API calls, sends, posts, publishes, or schedules were created.

## 2026-05-27 SendFox Draft Creation

- Cleaned `review_dashboard.html` into a content-only dashboard with no approval controls or feedback prompt.
- Ran SendFox read-only `GET /me`.
- Ran SendFox read-only `GET /lists`.
- Selected list `BizAmps's U.S Interested leads` with ID `631826`.
- Created SendFox campaign draft `Conference Demand - Your booth is not enough`.
- Campaign ID: `2830202`.
- Omitted `scheduled_at`.
- Confirmed read-back has blank `scheduled_at` and blank `sent_at`.
- Did not call a send endpoint.
- Did not touch Buffer, HubSpot, X/Facebook publishing, Medium, WhatsApp posting, or YouTube Community.
- Did not print or save secrets from `keys.env`.

## 2026-05-27 SendFox Formatting Cleanup

- Cleaned `review_dashboard.html` further: removed short-copy buttons and simplified the posting plan.
- Rebuilt `sendfox_email_improved.html` with simple table-safe/email-safe HTML.
- Rebuilt `sendfox_final_preview.html` with the same spacing rules.
- Added durable SendFox spacing rules: inline paragraph margins, controlled stacked lines, normal-sized CTA button, and better thumbnail spacing.
- Recorded preferred future SendFox From Name: `🧠 Akshat from BizAmps`.
- Added SendFox list selection rules in `shared\integrations\sendfox\list_selection_rules.md`.
- Noted that future campaigns may target multiple lists based on config.
- Existing SendFox draft `2830202` was not edited, sent, or scheduled.
- Did not call Buffer, HubSpot, X/Facebook, Medium, WhatsApp, or YouTube APIs.

## 2026-05-28 Distribution Copy Quality Rule Update

- Updated the distribution workflow to create only the channel assets Akshat specifically asks for.
- Changed WhatsApp default to 2-3 strong personal messages, not 5-10 variants.
- Changed email default to 2-3 subject options and one strong email unless Akshat asks for more.
- Changed LinkedIn default so LinkedIn posts are created only when Akshat asks for LinkedIn.
- Added flagship-message-first process: study transcript, extract strongest idea, write one message, critique internally, improve, then create final options.
- Added Akshat-approved WhatsApp style as the benchmark for future messages.
- Added an 8-point internal quality check requiring final copy to score 8/10 or higher before showing.
- Added Founder Voice Editor guidance for high-quality copy passes.
- No new content assets, external drafts, sends, schedules, or API calls were created.
