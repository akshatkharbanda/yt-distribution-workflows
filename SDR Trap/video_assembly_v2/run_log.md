# Run Log - video_assembly_v2

## 2026-05-17

- Created folder `video_assembly_v2`.
- Created subfolders: `exports`, `contact_sheets`, `temp`.
- Confirmed Python video tooling is available:
  - `imageio_ffmpeg`
  - `moviepy`
  - `PIL`
- Extracted embedded subtitles from `YT_ SDR Trap.mp4` to:
  - `video_assembly_v2\temp\source_subtitles.srt`
- Subtitle extraction command used FFmpeg mov_text to SRT conversion.
- Confirmed the SRT includes actual spoken timestamps, so v2 timing can use the real delivery instead of rough planned timestamps.
- v2 decision: create only the two requested 75-second layout previews first, then stop for review.


- Created timing map in `timing_adjustments.md` for all 24 slides using the embedded subtitle transcript.
- Created preview renderer: `render_preview_layouts.py`.
- Rendered Layout A preview:
  - `exports\preview_75s_slide_first_v2.mp4`
- Rendered Layout B preview:
  - `exports\preview_75s_face_first_v2.mp4`
- Created contact sheets:
  - `contact_sheets\preview_75s_slide_first_v2_sheet.jpg`
  - `contact_sheets\preview_75s_face_first_v2_sheet.jpg`
- First verification after render showed `yuvj420p` because slide timeline states were generated from image inputs.
- Re-exported both previews with explicit compatibility conversion:
  - `scale=in_range=pc:out_range=tv,format=yuv420p`
  - `-pix_fmt yuv420p`
  - `-profile:v high -level 4.0`
  - `-movflags +faststart`
- Verified final preview files:
  - duration: `00:01:15.00`
  - video: `h264 (High)`, `yuv420p`, `1920x1080`, `30 fps`
  - audio: `aac (LC)`, `44100 Hz`, stereo
- Layout B first pass had the slide panel too wide and it clipped into the speaker's face.
- Adjusted Layout B panel from about 860px wide to 780px wide, keeping it just over 40% of screen width and preserving more face visibility.
- Sound design skipped for these previews; timing/layout is the priority.
