# Run Log - video_assembly_v3

## Goal

Create 75-second split-screen previews only. Do not render the full 5:45 video.

## 2026-05-17

- Created `video_assembly_v3/` with `exports/`, `contact_sheets/`, and `temp/`.
- Added `render_v3_previews.py` to generate preview renders and contact sheets.
- Rendered crop A preview:
  - `exports/preview_75s_split_screen_cropA_v3.mp4`
- Rendered crop B looser preview:
  - `exports/preview_75s_split_screen_cropB_looser_v3.mp4`
- Created contact sheets:
  - `contact_sheets/preview_75s_split_screen_cropA_v3_sheet.jpg`
  - `contact_sheets/preview_75s_split_screen_cropB_looser_v3_sheet.jpg`
- Created two SFX preview variants using crop B:
  - `exports/preview_75s_split_screen_sfx_normal_v3.mp4`
  - `exports/preview_75s_split_screen_sfx_quiet_v3.mp4`
- Verified exports with the bundled FFmpeg reader output:
  - H.264 High
  - `yuv420p`
  - 1920x1080
  - 30 fps
  - AAC audio
  - 75.00 seconds

## Notes

- The local package did not include `ffprobe.exe`, so verification used FFmpeg input inspection.
- MoviePy warned that the embedded subtitle stream is ignored. This is fine because subtitles were already used earlier for timing decisions and are not needed in the preview render.
- Full video was not rendered.
