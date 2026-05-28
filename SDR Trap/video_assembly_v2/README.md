# video_assembly_v2

Goal: create better-synced preview drafts for the "Stop Scaling Chaos" YouTube video by aligning slide moments to the actual spoken delivery in `YT_ SDR Trap.mp4`.

## Inputs
- Talking-head source: `C:\Codex Projects\YT\SDR Trap\YT_ SDR Trap.mp4`
- Slide assets: `C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck\assets`
- v1 timing/log reference: `C:\Codex Projects\YT\SDR Trap\video_assembly_v1`
- Extracted subtitle transcript: `video_assembly_v2\temp\source_subtitles.srt`

## Outputs In This Phase
- Slide-first 75s preview: `video_assembly_v2\exports\preview_75s_slide_first_v2.mp4`
- Face-first 75s preview: `video_assembly_v2\exports\preview_75s_face_first_v2.mp4`
- Contact sheets:
  - `video_assembly_v2\contact_sheets\preview_75s_slide_first_v2_sheet.jpg`
  - `video_assembly_v2\contact_sheets\preview_75s_face_first_v2_sheet.jpg`

## Current Method
- Uses the original video/audio as the master timeline.
- Uses the embedded MP4 subtitle stream to find actual spoken cue timings.
- Recreates simple slide reveals in code instead of relying on Google Slides animation export.
- Exports broad-compatible MP4s with H.264, `yuv420p`, AAC, and `+faststart`.
