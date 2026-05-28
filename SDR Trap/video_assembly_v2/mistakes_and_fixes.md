# Mistakes And Fixes - video_assembly_v2

## v1 used rough timestamps too literally
- What went wrong: slides appeared several seconds late, for example "Burn rate: vertical" appeared while the narration had already moved to gambling.
- Why it happened: v1 followed the rough planned timestamp list, but the actual spoken delivery was faster/different.
- Fix: v2 extracts the embedded subtitle transcript and aligns each slide to real spoken cue phrases.
- Check next time: never use script/planned timestamps as final edit timing without checking transcript or audio.

## Do not globally shift the timeline
- What went wrong risk: a simple global shift would fix one slide but break others.
- Why it happens: spoken sections drift differently across the video.
- Fix: v2 records slide-by-slide cue timings in `timing_adjustments.md`.
- Check next time: align each slide to a cue phrase.

## Compatibility is mandatory
- What went wrong in v1: initial exports used `yuv444p` / High 4:4:4 Predictive.
- Fix: all v2 exports must force `-pix_fmt yuv420p` and `-movflags +faststart`.


## v2 previews initially exported as yuvj420p
- What went wrong: first v2 preview render reported `yuvj420p`, not plain `yuv420p`.
- Why it happened: the slide timeline was built from image inputs and FFmpeg treated them as full-range JPEG/video.
- Fix: re-exported with `scale=in_range=pc:out_range=tv,format=yuv420p` plus `-pix_fmt yuv420p`.
- Check next time: verify the final preview files, not just the renderer command.

## Face-first panel covered the speaker too much
- What went wrong: the initial Layout B slide panel was too wide and overlapped the face.
- Why it happened: a 40-48% slide panel is large for a centered talking-head crop.
- Fix: reduced the panel to about 780px wide and kept it on the left.
- Check next time: face-first layouts need a contact sheet before full export.
