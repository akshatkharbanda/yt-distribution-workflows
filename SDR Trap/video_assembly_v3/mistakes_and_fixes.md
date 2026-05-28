# Mistakes And Fixes - v3

## Carryover Mistake From v1

Initial video export used `yuv444p` / High 4:4:4 Predictive, which caused compatibility problems. Future exports must force:

- `-pix_fmt yuv420p`
- `-movflags +faststart`

## v2 Issue

Some visuals still felt late by 1-2 seconds, and the face-first layout felt like a floating slide overlay.

Fix in v3 preview:

- Use split-screen layout instead of overlay.
- Use actual spoken cue timings.
- Start visuals near the phrase, then delay punchline/caption windows.

## v3 Preview Limitation

The slide assets are flattened, so the preview cannot truly reveal every text object independently.

Fix used:

- Approximate internal reveal timing with fade/dim/caption-area masking.

Next improvement:

- Rebuild key slide text as separate layers for full v3 if exact punchline reveal timing matters.
