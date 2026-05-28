# Stop Scaling Chaos - Full Deck Change Log

## Initial Direction
- Expand the approved 3-slide test into a full 24-slide YouTube support deck.
- Use `Stop_Scaling_Chaos.pptx` as the style and concept reference, not as screenshots.
- Keep dark background, bold white headlines, yellow emphasis, and one visual joke per slide.

## User Feedback Applied
- The 3-slide test had text overlays that hid part of the image margin.
- Full-deck layout now gives the headline its own top space and centers the image lower, so the main visual is less covered.
- Visible timestamps were removed from slides; timestamps live only in speaker notes.

## Build Logic
- Slides 1-3 reuse the approved test visuals.
- Slides 4-24 use new generated visuals matched to the requested metaphors.
- Headlines, support text, captions, and speaker notes are editable PowerPoint/Google Slides objects.
- Images are used as scene layers only; punchline copy stays editable.

## Simplifications From NotebookLM
- Removed tiny labels inside images.
- Reduced busy scenes to one clear visual metaphor.
- Replaced source Slide 3 burn-rate joke with the user-requested empty-calendar joke.
- Kept burn-rate as Slide 4.

## Known Limitation
- Generated scenes are not individually editable objects, but all text, captions, notes, and animation order are editable.
- Google Slides may simplify imported PowerPoint animation details, so each slide includes animation instructions in speaker notes.
