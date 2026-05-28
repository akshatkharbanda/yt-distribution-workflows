# YouTube Distribution Workflow

This folder is for BizAmps YouTube distribution work.

Each video should live in its own folder, for example:

```text
C:\Codex Projects\YT\SDR Trap
```

The V1 workflow creates local review assets only:

- WhatsApp posts
- SendFox email preview
- HubSpot email preview when requested
- LinkedIn personal post
- LinkedIn carousel outline
- Blog post when requested
- Shorts/native clip ideas when requested
- Quuu Promote copy when requested
- Posting plan
- Local `preview.html`
- `approval.json`

V1 does not send, post, publish, schedule, or create external drafts.

## How To Run

Ask Codex to run `youtube-distribution-draft-system` for a selected video folder.

Codex should confirm:

- video folder
- goal
- audience
- requested assets
- platform priority
- urgency
- geography/timezone

If you ask for all assets, Codex should confirm before generating everything.

## Restart Safety

Each run should write outputs under:

```text
[Video Name]\distribution
```

Required review files:

- `distribution_package.md`
- `preview.html`
- `approval.json`

Use `logs\run-log.md` and `logs\error-log.md` to preserve what happened.

## Approval

All channels start as pending in `approval.json`.

Allowed statuses:

- pending
- approved
- needs_edit
- rejected

Later draft creation can only use approved items.
