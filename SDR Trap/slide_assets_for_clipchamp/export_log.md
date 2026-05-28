# Export Log - Slide Assets For Clipchamp

## Goal

Create a clean slide asset package for a human editor to import into Clipchamp. No final edited talking-head video was created.

## Input

- Source PPTX: `C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck\Stop_Scaling_Chaos_Codex_Full_Deck.pptx`
- Backup visual source used for clean renders: `C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck\preview\Slide1.PNG` through `Slide24.PNG`

## Output Folder

`C:\Codex Projects\YT\SDR Trap\slide_assets_for_clipchamp`

## Files Created

- Full slide asset reel:
  - `slides_full_animated.mp4`
- Individual slide videos:
  - `slide_videos\slide_01.mp4` through `slide_videos\slide_24.mp4`
- Static fallback images:
  - `slide_images\slide_01.png` through `slide_images\slide_24.png`
- Review contact sheet:
  - `contact_sheet_slide_assets.jpg`
- Export scripts:
  - `export_slide_assets.ps1`
  - `finalize_assets.py`
  - `recreate_clean_assets.py`

## Method Tried A - PowerPoint Native Animation Export

Result: failed quality check.

What worked:

- PowerPoint was installed and usable.
- PowerPoint detected/exported video files from the PPTX.
- The source PPTX contained animation/timing tags.

What failed:

- PowerPoint exported the deck videos as square `1080x1080`, not true 16:9.
- The exported slide PNGs from PowerPoint also rendered the slide content tiny in the middle of a 1920x1080 canvas.
- This made the output unsuitable for Clipchamp and YouTube.

Decision:

- Do not use the native PowerPoint export files as final assets.
- Keep raw failed exports in `temp/` only for audit/debug.

## Method B - Browser Screen Recording

Not used.

Reason:

- Native PowerPoint export already proved the deck's current animation path is unreliable.
- Screen recording would be slower and more fragile.

## Method C - Programmatic Recreated Animation

Used for final asset package.

How:

- Used the clean full-deck preview images from the existing deck build.
- Normalized each slide image to 1920x1080 PNG.
- Created one 3-second MP4 per slide:
  - 0.5 second clean hold
  - simple fade in
  - clean hold
  - short fade out
- Concatenated the 24 slide videos into `slides_full_animated.mp4`.

Animation fidelity:

- Actual PowerPoint/Google Slides object animations were not preserved.
- Final MP4s use simple recreated fade animation only.
- This is intentional because the real animation export produced bad 16:9 quality.

## Compatibility Settings

Every final MP4 was created with:

- H.264
- `yuv420p`
- 1920x1080
- 30fps
- no audio
- `+faststart`
- square pixels / 16:9 display aspect ratio

Final inspection for `slides_full_animated.mp4`:

```text
Duration: 00:01:11.17
Video: h264 (High), yuv420p(progressive), 1920x1080 [SAR 1:1 DAR 16:9], 30 fps
Audio: none
```

## Quality Notes

- The static slide visuals look clean and readable.
- The slide videos are intentionally short and simple so the intern can drag each one into Clipchamp and manually sync to the talking-head video.
- If exact headline/caption object animation is required later, the better route is to rebuild per-slide animation layers programmatically or fix the deck page-size/export issue before using PowerPoint video export.

## Failed Methods / Issues

- Failed: PowerPoint native video export as final output because it produced square/tiny renders.
- Not attempted: browser screen recording because it is more fragile and not needed for the current Clipchamp asset handoff.

## 2026-05-23 Update - Animation Priority Fix

User reported that `slide_videos` did not show the PowerPoint animations and said animation is more important than strict 16:9.

Root cause:

- The first PowerPoint animation export used the wrong PowerPoint COM slide-size units.
- PowerPoint expects points, but the earlier script used inch values (`13.333` x `7.5`), which made animated exports render tiny.

Fix attempted:

- Added `export_powerpoint_animated_fixed.ps1`.
- Re-exported the PPTX using correct widescreen dimensions:
  - width `960` points
  - height `540` points
- Added `finalize_powerpoint_animated_fixed.py`.
- Created native PowerPoint animated files in:
  - `slide_videos_animated_powerpoint\slide_01.mp4` through `slide_24.mp4`
- Replaced the main `slide_videos\` folder with those native animated versions.
- Backed up the previous simple-fade files in:
  - `slide_videos_simple_fade_backup\`

Current status:

- `slide_videos\` now contains PowerPoint-native animated clips.
- `slide_videos_simple_fade_backup\` contains the clean simple-fade version.
- `slides_full_animated_powerpoint_native.mp4` contains the native PowerPoint full-deck export.

Quality warning:

- Native PowerPoint export now renders at correct 1920x1080 size.
- However, sampled frames show PowerPoint's animation/export may produce a noisy dissolve-looking pattern during animation frames.
- This may be the actual PowerPoint animation effect, or a PowerPoint video-export rendering artifact.
- Human review is required before using these in Clipchamp.

Recommended next step if this still looks bad:

- Use screen recording of slideshow playback instead of PowerPoint `CreateVideo`.
- That should capture what PowerPoint shows visually, but it is a more fragile workflow and may need manual checking.

## 2026-05-23 Update 2 - PowerPoint Export Confirmed Unusable

User shared a screenshot showing the PowerPoint-native animated export was extremely noisy and unusable.

Decision:

- Stop using PowerPoint native video export for final slide assets.
- Do not use `slide_videos_powerpoint_noisy_backup` unless specifically debugging.

Fix implemented:

- Added `create_clean_layered_animations.py`.
- Recreated the intended slide animation cleanly from layers:
  - visual image fades in first
  - top/bottom dark bands fade in
  - headline fades in
  - support line fades in when present
  - caption fades in last
- Replaced the main `slide_videos\` folder with these clean layered animated clips.
- Saved the noisy PowerPoint-native version in:
  - `slide_videos_powerpoint_noisy_backup\`
- Saved the clean layered version in:
  - `slide_videos_clean_layered_animation\`

Current recommended folder for Clipchamp:

- `slide_videos\`

Current output settings:

- H.264
- `yuv420p`
- 1920x1080
- 30fps
- no audio
- `+faststart`
- each slide video is about 3.5 seconds

Tradeoff:

- These are not PowerPoint's exact animation engine output.
- They preserve the useful animation structure without the ugly noisy render artifact.

## Restart Notes

To regenerate the final clean asset package:

1. Use `recreate_clean_assets.py`.
2. It rebuilds `slide_images`, `slide_videos`, `slides_full_animated.mp4`, and `contact_sheet_slide_assets.jpg`.
3. Keep `-pix_fmt yuv420p` and `-movflags +faststart` mandatory for every MP4.
