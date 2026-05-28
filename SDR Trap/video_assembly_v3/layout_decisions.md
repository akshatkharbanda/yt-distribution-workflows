# Layout Decisions - v3

## Approved Direction

- Use split-screen layout.
- Slides and visuals on the left.
- Cropped talking-head video on the right.
- Do not use the v2 floating overlay layout.
- Create preview first, not the full video.

## Decision

The v3 preview uses a fixed split-screen:

- Left visual panel: 1240x1080
- Right face panel: 680x1080

Slides are contained inside the left panel, not cropped. This protects slide margins and avoids hiding text or image edges.

## Internal Reveal Approach

The source slide images are flattened, so true per-object Google Slides animation is not available in this preview. The preview approximates internal reveal timing by:

- Starting the slide visual near the cue
- Fading/dimming before the main headline moment
- Keeping the lower caption area darker until the later caption/punchline window

This is a preview compromise. If approved, a fuller v3 render can rebuild cleaner per-layer reveals from editable slide assets or re-exported slide components.
