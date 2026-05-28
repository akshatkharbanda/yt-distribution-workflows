# Logic History

## 2026-05-25

Decision: Keep distribution separate from slide/video production.

Reason: The existing slide/video skill handles support slides, timing packages, Google Slides/Google Vids, Clipchamp assets, MP4 exports, and visual review packages. Distribution needs a different workflow focused on written assets, local preview, approvals, and later draft creation.

Decision: V1 uses Codex-generated content only.

Reason: Akshat does not want a Python script that requires an LLM API key for this workflow.

Decision: SDR Trap test uses existing subtitles and timing notes.

Reason: Top-level `transcript.txt` and `video_brief.md` were not present, but the folder already had extracted subtitles and timing notes from the video workflow.

Decision: Add a creative QA gate before saving distribution outputs.

Reason: The first SDR Trap output had weak random humor, generic subject lines, and a tactical WhatsApp post with too many questions. Brand Repair V3 now requires transcript-native killer lines, Punchy/Funny defined as founder pain, max 3 tactical questions, and rewrite rules for generic assets.

## 2026-05-26

Decision: Build the learning layer as Markdown-first research and coaching files before any live integration.

Reason: Akshat needs readable learning, weekly coaching, and safe build order before any campaign draft creation.

Decision: Make SendFox the first integration, but only test `GET /me` and `GET /lists` before any draft campaign.

Reason: SendFox supports draft campaign creation when `scheduled_at` is omitted, but sending must remain forbidden.

Decision: Treat HubSpot marketing email drafts as unproven for this account.

Reason: HubSpot marketing email API access depends on account scope and private app permissions, so the fallback is local HTML plus manual publish steps.

Decision: Keep YouTube Analytics as manual export/OAuth planning only for now.

Reason: YouTube Analytics requires Google OAuth and should not be implemented before the simpler learning/report workflow is useful.
