# Preview HTML Requirements

`review_dashboard.html` is the main review surface.

Akshat should only need to open `review_dashboard.html` for normal review.

Keep `preview.html`, `review.html`, `mobile_preview.html`, and `sendfox_final_preview.html` as backup/specialized views when useful.

`review_dashboard.html` should be a clean content dashboard, not a control panel.

Keep approval controls, comments, feedback prompts, and external action controls out of the main dashboard unless Akshat asks for them.

Use `review.html` only as a backup approval and comments surface when specifically needed.

Use `mobile_preview.html` when email/social content needs phone-width review.

Use `sendfox_final_preview.html` before any SendFox draft creation.

Use `approval_summary.html` to turn pasted review output into a readable summary.

It should:

- be self-contained
- work offline
- use clean CSS
- show only requested assets
- include a simple table of contents
- show approval status as pending
- show email as a newsletter-style preview
- show improved SendFox and HubSpot email formatting when requested
- show LinkedIn posts in card format
- show both full and short LinkedIn versions when production review is requested
- show carousel slides as visual cards
- avoid external scripts, trackers, and libraries

`review_dashboard.html` should:

- use collapsible sections
- put SendFox email first
- put LinkedIn angles second
- put WhatsApp variants third
- include copy buttons only where they reduce friction without clutter
- include mobile previews
- include missed-channel checklist near the bottom
- include SendFox safety preview when a draft exists or is planned

Backup `review.html` can:

- separate content approval from external action approval
- make clear that content approval does not approve API calls, drafts, sending, publishing, or scheduling
- include approved / needs_edit / rejected options
- include comment boxes
- include copy-friendly generated `approval.md` content if Akshat asks for an approval workflow
- include missed-channel reminders where useful

Recommended style:

- max width around 900px
- system font stack
- light background
- white cards
- readable spacing
- copy-friendly text blocks
