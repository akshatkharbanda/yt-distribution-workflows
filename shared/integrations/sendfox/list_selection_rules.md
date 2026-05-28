# SendFox List Selection Rules

Use these rules before creating any SendFox campaign draft.

## Default Behavior

1. If `SENDFOX_LIST_ID` is explicitly set in `keys.env`, use that list.
2. If `SENDFOX_LIST_ID` is set to `ALL_VALID_LISTS` or an equivalent config value, include all eligible lists.
3. If no clear list setting exists, show available list names and IDs to Akshat and ask which list or lists to use.
4. Do not assume only one list.
5. Do not include test lists unless Akshat explicitly allows them.
6. Do not include old, event-specific, or irrelevant lists unless the config says to include all eligible lists.

## Multi-List Note

Akshat may want SendFox drafts to target multiple existing lists, not only one list, depending on the campaign.

## Safety

- Never print or log API tokens.
- Never call a send endpoint.
- Never include `scheduled_at` unless Akshat explicitly approves scheduling.
- Existing drafts should not be edited, sent, or scheduled without Akshat approval.
