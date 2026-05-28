# video_assembly_v1

Goal: create a rough MP4 draft that combines the talking-head video with the recreated slide deck for the YouTube video "Stop Scaling Chaos" / "Outbound Reality Check."

## Inputs
- Talking-head video: `C:\Codex Projects\YT\SDR Trap\YT_ SDR Trap.mp4`
- Local rebuilt deck: `C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck\Stop_Scaling_Chaos_Codex_Full_Deck.pptx`
- Slide visual assets and rendered previews: `C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck\`
- Google Slides deck: `https://docs.google.com/presentation/d/1Sgy-UF7DgaNn-zy5HL1p4JSQbsBZX_iru2u6CFIO8DU`
- Timing plan: `video_assembly_v1\timestamp_plan.md`

## Outputs
- Main draft: `video_assembly_v1\exports\stop_scaling_chaos_recreated_animation_pip_v1.mp4`
- First-minute preview: `video_assembly_v1\exports\preview_first_60s_v1.mp4`
- Contact sheet: `video_assembly_v1\contact_sheets\contact_sheet_v1.jpg`
- Practical sync contact sheet: `video_assembly_v1\contact_sheets\contact_sheet_plus1_v1.jpg`

## Animation Method
This v1 workflow uses recreated basic animations with Python + FFmpeg:
- slide image appears first
- heading appears shortly after
- support text appears if present
- caption appears later

It does not use true Google Slides animation playback because direct Google Slides animated video export is not available through the connected Drive tool, and the PowerPoint animation path is not reliable for voice-synced timing in this draft workflow.


## Compatible Exports
+- Final compatible MP4: `video_assembly_v1\exports\stop_scaling_chaos_recreated_animation_pip_v1_COMPATIBLE.mp4`
+- Preview compatible MP4: `video_assembly_v1\exports\preview_first_60s_v1_COMPATIBLE.mp4`
+- These are the preferred files for Windows playback, browser preview, Google Drive preview, phones, and sharing.
