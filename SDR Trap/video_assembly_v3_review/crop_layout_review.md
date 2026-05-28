# Crop Layout Review - v3

Preferred review layout:

- Canvas: 1920x1080
- Left slide panel: x=0, y=0, width=1240, height=1080
- Right face panel: x=1240, y=0, width=680, height=1080

What was tested:

- A proper split-screen mockup, not a floating slide overlay.
- The talking-head video is cropped for the right panel, not simply shrunk.
- Crop target keeps face, shoulders, and some hand movement while removing side background.
- Slide visuals are contained inside the left panel so text/image margins do not get hidden.

Representative frames in `crop_layout_contact_sheet.jpg`:

| Moment | Slide | Timestamp | Review note |
|---|---:|---:|---|
| start | 1 | 0:03.18 | Confirms face crop at first spoken funding cue. |
| funding | 1 | 0:03.18 | Slide text is readable; left panel has safe margins. |
| SDR | 2 | 0:07.30 | Team visual remains readable; face crop keeps shoulders. |
| burn rate | 4 | 0:21.65 | Fixes the late burn-rate issue; visual lands on the phrase. |
| gambling | 5 | 0:33.20 | Face panel does not cover casino text because it is separate. |
| payroll | 6 | 0:51.85 | Org-chart joke remains on left; speaker is cleanly framed. |
| public version | 7 | 0:57.20 | Left slide is readable but visually dense; acceptable for review. |
| pain | 8 | 1:05.35 | Dark visual remains understandable in split layout. |

## Current Crop Judgment

The right-side crop is usable for review. It keeps the head visible and removes much of the empty side background. In a final render, I would still inspect a few high-hand-motion moments to make sure hand gestures are not cut off too aggressively.

## Layout Risk

The left panel is narrower than a full 16:9 slide, so the slide image is shown with vertical breathing room rather than cropped. This is intentional because you warned that image margins can get hidden when text overlays are involved.
