# Workflow SOP Draft - YouTube Slide + Talking Head Assembly

1. Create a separate phase folder with `exports`, `contact_sheets`, `temp`, and logs.
2. Inspect the talking-head video:
   - duration
   - resolution
   - frame rate
   - audio stream
3. Inspect the deck:
   - slide count
   - speaker notes
   - whether animations exist
   - whether export path can preserve animations
4. Choose animation path:
   - Try native animated export only if available.
   - Try PowerPoint video export if animations have usable automatic timings.
   - Try browser screen recording if true slide playback is critical.
   - Otherwise recreate simple animations with code.
5. Use the voice as the master timeline.
6. Build a slide timeline from timestamps.
7. For each slide:
   - image appears first
   - headline appears 0.2-0.8s later
   - support appears after headline
   - caption appears later to avoid spoiling the joke
8. Compose output:
   - 1920x1080
   - slide-first full-screen
   - talking-head picture-in-picture around 20% screen width
   - original audio copied from talking-head video
9. Verify:
   - duration matches source
   - audio is present
   - slides appear near planned timestamps
   - face box does not cover key text
   - contact sheet includes every slide start and +1s checks
10. Log every command, file, error, and fix.

## v1 Rendering Pattern
- Build slide animation as a separate silent video.
- Use one FFmpeg command per slide:
  - input visual-only frame
  - input headline frame
  - input support frame if needed
  - input caption frame
  - concatenate those states with explicit durations
- Concatenate all slide clips.
- Overlay the original talking-head video as PiP.
- Map the original audio from the talking-head video.

## QA Rule Added
- Always check the contact sheet before reporting completion.
- If exact timestamp frames are confusing at cuts, create a second contact sheet at `slide_start + 1s`.


## Mandatory Compatibility Export Rule
+- Every final or preview MP4 must be encoded for broad compatibility:
+  - H.264 video: `-c:v libx264`
+  - Pixel format: `-pix_fmt yuv420p`
+  - Profile/level: `-profile:v high -level 4.0`
+  - AAC audio: `-c:a aac -b:a 192k`
+  - MP4 faststart: `-movflags +faststart`
+  - 1920x1080, 30fps unless the user requests otherwise
+- Do not deliver `yuv444p` / `High 4:4:4 Predictive` exports for YouTube draft review, browser preview, phones, WhatsApp, or Google Drive preview.
+- Verification command when `ffprobe` is available:
+  `ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,pix_fmt,width,height,r_frame_rate,duration -of default=nw=1 <file>`
+- If `ffprobe` is unavailable, use `ffmpeg -hide_banner -i <file>` and confirm the video stream says `h264 (High)`, `yuv420p`, `1920x1080`, and `30 fps`.
