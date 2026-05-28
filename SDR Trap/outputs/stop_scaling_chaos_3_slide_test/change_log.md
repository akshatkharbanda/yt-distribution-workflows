# Stop Scaling Chaos - 3 Slide Test Change Log

## Initial Plan
- Recreate the first 3 content slides from `Stop_Scaling_Chaos.pptx`.
- Do not copy full-slide screenshots.
- Preserve the dark, bold, funny NotebookLM style.
- Keep the final output as native Google Slides.

## Decisions Made Before Build
- The source deck slides are flattened images, so editable rebuilding is required.
- Slide 3 uses the user's requested empty-calendar concept instead of NotebookLM's "Burn rate: vertical" source slide.
- Build route is local editable PPTX first, then import into Google Slides.
- Visual route is new generated visuals, with editable text placed on top.

## Implementation Logic
- One strong visual metaphor per slide.
- Main headline and caption are separate editable text objects.
- Yellow is used only for the key punchline word or phrase.
- Speaker notes carry timestamp, narration cue, animation cue, and build rationale.

## Known Limitation
- The local PPTX builder supports speaker notes but does not reliably create Google Slides animations. Reveal order is documented in notes for quick manual animation in Google Slides.
