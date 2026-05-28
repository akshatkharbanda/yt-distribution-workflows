# Review Build Log

## Initial plan

Create v3 as a review package only, not a rendered MP4.

## Change from v2

V2 used cue timing but still allowed some pre-roll and slide-first layout. For v3 review, timing is stricter: visuals start after the cue phrase, usually by 0.27-0.30 seconds.

## Files generated

- `review_contact_sheet.jpg`
- `crop_layout_contact_sheet.jpg`
- `timing_decision_table.md`
- `crop_layout_review.md`
- `face_only_moments.md`
- `sound_design_plan.md`
- `README.md`

## Tooling note

The first local Python run could not find the image library in the default Python environment. The bundled Codex workspace Python was used instead, which had the needed image tools.

## Next restart point

If the computer sleeps, resume from this folder:

`C:\Codex Projects\YT\SDR Trap\video_assembly_v3_review`

Review the two JPG sheets first, then approve timing/layout before any MP4 render.
