# Mistakes And Fixes - video_assembly_v1

## Missing ffmpeg on PATH
- What went wrong: `ffmpeg` and `ffprobe` were not available from the normal Windows PATH.
- Why it happened: the project folder did not include a video toolchain.
- Fix: installed `imageio-ffmpeg` and `moviepy` into the user Python environment and used the bundled ffmpeg binary.
- Check next time: run a tool availability check before planning the render path.

## Google Slides animation export uncertainty
- What went wrong: native Google Slides import worked, but export-back from Google Drive hit a 403 on the full deck.
- Why it happened: Drive export permissions/tool limitation, not a deck-design failure.
- Fix: use the locally rendered PPTX/PNG layers and recreate simple animation timing in code.
- Check next time: if true Google Slides animations are required, use a browser recording workflow early before building the full video.

## Text margin issue from slide phase
- What went wrong: the approved 3-slide test had text overlay covering part of the image area.
- Why it happened: headline band sat on top of the image.
- Fix: full deck and video renderer reserve separate top/bottom bands so slide image margins are less hidden.
- Check next time: contact-sheet review should include image margin safety, not just text readability.

## Slide timing drift in first render
- What went wrong: the first contact sheet showed slides appearing late and out of order.
- Why it happened: the first FFmpeg still-image concat method did not respect the intended per-state durations.
- Fix: rebuilt the renderer to create each slide from timed still inputs in one FFmpeg concat-filter command.
- Check next time: verify segment durations before rendering the full final video.

## Slow per-state render fallback
- What went wrong: rendering every reveal state as its own video was too slow and timed out.
- Why it happened: it required roughly 96 mini-video encodes before the final compose.
- Fix: replaced it with one encode per slide.
- Check next time: avoid render plans that multiply video encodes per animation state.

## Contact-sheet boundary ambiguity
- What went wrong: frames grabbed at exact slide start sometimes showed the previous slide.
- Why it happened: fast seeking can land on a nearby keyframe around a cut.
- Fix: also created a `+1s` contact sheet, which is better for checking the intended slide after the cut.
- Check next time: include both exact-start and post-start frames, and use the post-start sheet for practical sync QA.


## Initial export used yuv444p / High 4:4:4 Predictive
+- What went wrong: the first MP4 was valid, but common players/previews may not open it properly because it used `yuv444p` / `High 4:4:4 Predictive`.
+- Why it happened: FFmpeg/libx264 kept the RGB-style slide composition in a less compatible pixel format when `-pix_fmt yuv420p` was not forced.
+- Fix: re-exported both final and preview MP4s with `-pix_fmt yuv420p`, `-profile:v high`, `-level 4.0`, AAC audio, MP4 container, and `-movflags +faststart`.
+- Check next time: every future video export must force `-pix_fmt yuv420p` and `+faststart` before delivery.
