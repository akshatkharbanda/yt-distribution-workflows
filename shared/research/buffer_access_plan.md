# Buffer Access Plan

## Goal

Use Buffer as the second integration for LinkedIn distribution after SendFox is proven safe.

## Secrets

Store real values only in `keys.env`.

Expected placeholder:

- `BUFFER_ACCESS_TOKEN`

Never print or log the token.

## First Test

Verify connection and available profiles/channels.

Need to identify:

- Whether the LinkedIn profile/page is connected.
- Whether the API/account supports drafts, ideas, or safe queued posts.
- Whether queued posts can be created without immediate publishing.

## Draft / Queue Rule

Allowed only after Akshat approves the Conference Demand LinkedIn copy.

Preferred:

- Create a Buffer draft for LinkedIn.

Acceptable only if Akshat approves:

- Create a queued LinkedIn post that does not publish immediately.

Forbidden:

- Immediate publish.
- Auto-scheduling without review.
- Posting to the wrong profile/page.

## Fallback

If Buffer does not expose a safe draft state, stop and create:

- `buffer_linkedin_post.md`
- `buffer_manual_publish_steps.md`
- Local preview HTML if useful
