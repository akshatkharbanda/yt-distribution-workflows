# YouTube Analytics Access Plan

## Goal

Create a clear path for weekly coaching from YouTube performance without implementing OAuth yet.

## API Reality

There is no simple YouTube Studio API key workflow for this use case.

The YouTube Analytics API requires Google OAuth.

Relevant read scope:

- `https://www.googleapis.com/auth/yt-analytics.readonly`

Possible future scope only if needed:

- `https://www.googleapis.com/auth/youtube.readonly`

## Future OAuth Flow

Do not implement yet.

When approved, the flow should be:

1. Create a Google Cloud project.
2. Enable YouTube Analytics API.
3. Configure OAuth consent screen.
4. Create OAuth client credentials for a desktop or local app.
5. Store client secret outside git.
6. Complete local browser authorization.
7. Store refresh token outside git.
8. Query analytics reports for approved date ranges.

## V1 Manual Export Option

Akshat can provide screenshots or CSV exports from YouTube Studio.

Need:

- Video title
- YouTube URL
- Publish date
- Date range
- Impressions
- Click-through rate
- Views
- Average view duration
- Retention screenshot or notes
- Traffic sources
- Likes
- Comments
- Subscribers gained
- External clicks if available

## Weekly Coaching Fields

- What got attention.
- What got clicks.
- What got replies/comments.
- Which hooks held attention.
- Which hooks got ignored.
- Which topics showed demand.
- Which channels were missed.
- What to make next.
