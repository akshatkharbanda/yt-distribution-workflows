# Workflow SOP - v3 Preview

## Purpose

Create a short preview before rendering the full YouTube edit.

## Steps

1. Use original talking-head video as audio truth.
2. Use subtitle/audio cue timings, not rough slide plan timings.
3. Create review timing table before rendering.
4. Use split-screen layout:
   - left: slide/visual
   - right: cropped talking-head video
5. Render a 75-second preview first.
6. Test at least two face crops:
   - tighter crop
   - looser crop
7. Generate contact sheets for quick visual inspection.
8. Add SFX only after layout/timing preview exists.
9. Export all MP4s with:
   - H.264
   - `yuv420p`
   - AAC
   - 1920x1080
   - 30fps
   - `+faststart`
10. Stop before full render and get approval.

## Restart Point

If the PC sleeps, resume from:

`C:\Codex Projects\YT\SDR Trap\video_assembly_v3`

Run:

`render_v3_previews.py`

Then review:

1. `exports/preview_75s_split_screen_cropB_looser_v3.mp4`
2. `exports/preview_75s_split_screen_sfx_quiet_v3.mp4`
3. contact sheets in `contact_sheets/`
