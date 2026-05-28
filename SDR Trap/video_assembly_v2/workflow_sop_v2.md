# Workflow SOP v2 - Audio-Aligned YouTube Slide Draft

1. Create a separate version folder with logs, exports, contact sheets, and temp files.
2. Extract subtitles/transcript from the original talking-head MP4 if available.
3. If no embedded transcript exists, generate a timestamped transcript.
4. Build a slide cue list using real spoken phrases, not rough script timestamps.
5. For each slide, record:
   - v1 timestamp
   - detected spoken cue
   - v2 visual start
   - v2 headline start
   - reason for the adjustment
6. Create short layout previews before rendering the full video.
7. Preview layouts:
   - slide-first: slides full-screen, face PiP
   - face-first: face full-screen, slide side panel
8. Preserve original audio and voice timing.
9. Export compatibility settings are mandatory:
   - H.264
   - `-pix_fmt yuv420p`
   - AAC audio
   - `-movflags +faststart`
   - 1920x1080
   - 30fps
10. Create contact sheets for preview review.
11. Stop after preview exports and ask for layout/timing feedback before full v2.


## Added From Preview Run
+- If slide frames are image-based, final preview export may still become `yuvj420p`; always verify and, if needed, run a compatibility pass with `scale=in_range=pc:out_range=tv,format=yuv420p`.
+- For face-first layouts with a centered speaker, keep the side slide panel close to 40% width, not 48%, unless the speaker is clearly framed away from that side.
+- Stop after the preview pair and ask for user choice before full v2 export.
