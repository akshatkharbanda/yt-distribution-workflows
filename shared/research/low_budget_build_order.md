# Low Budget Build Order

## Phase 1: Learning Layer And Secrets Safety

- Create the research/coaching skill.
- Create human-readable learning templates.
- Update `.gitignore` for `keys.env`, `.env`, token files, and credential files.
- Keep `.env.example` placeholder-only.
- Do not call APIs yet unless separately asked.

## Phase 2: SendFox

- Test SendFox with `GET /me`.
- Test SendFox with `GET /lists`.
- After approval in the Production thread, create a real SendFox draft campaign from Conference Demand.
- Omit `scheduled_at`.
- Never call the send endpoint.

## Phase 3: Buffer

- Test Buffer connection and LinkedIn profile/page access.
- Verify safe draft or queue behavior.
- After approval in the Production thread, create a LinkedIn draft or queued post from Conference Demand.
- If no safe draft/queue state exists, create local fallback files only.

## Phase 4: HubSpot

- Research/test HubSpot MCP and API access.
- Check if old marketing emails and stats can be retrieved.
- Check if draft creation is available in this account.
- If blocked, use local `hubspot_email.html`, manual publish steps, and manual exports for learning.

## Phase 5: YouTube Analytics

- Use manual YouTube Studio exports/screenshots for v1 weekly coaching.
- Write OAuth requirements clearly.
- Implement OAuth only after separate approval.

## Why This Order

SendFox is the lowest-risk first integration because draft campaign creation is documented and sending can be avoided by omitting `scheduled_at` and never calling `/send`.

Buffer is second because LinkedIn draft/queue safety must be verified.

HubSpot is later because account scopes may block marketing email workflows.

YouTube Analytics is last because OAuth setup is heavier than manual exports for v1.
