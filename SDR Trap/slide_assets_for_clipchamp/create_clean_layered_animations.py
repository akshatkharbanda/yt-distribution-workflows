from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
OUT = ROOT / "slide_assets_for_clipchamp"
ASSETS = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "assets"
VIDEOS = OUT / "slide_videos"
CLEAN = OUT / "slide_videos_clean_layered_animation"
NOISY_BACKUP = OUT / "slide_videos_powerpoint_noisy_backup"
TEMP = OUT / "temp_clean_layered"

W, H, FPS, DUR = 1920, 1080, 30, 3.5
YELLOW = (231, 255, 0)
RED = (255, 51, 51)
GREEN = (76, 255, 106)
WHITE = (255, 255, 255)

SLIDES = [
    ([("Founder raises ", WHITE), ("funding", YELLOW), (".", WHITE)], "", "What could go wrong?"),
    ([("First move: ", WHITE), ("hire SDRs", YELLOW), (".", WHITE)], "", "The outbound cinematic universe begins."),
    ([("3 months ", WHITE), ("later", YELLOW), ("...", WHITE)], "Calendar: empty.", "Pipeline looking spacious."),
    ([("Burn rate: ", WHITE), ("vertical", RED), (".", WHITE)], "", "At least something is growing."),
    ([("You aren't ", WHITE), ("scaling", YELLOW), (".", WHITE)], "You're gambling.", "The house always wins."),
    ([("You copied the ", WHITE), ("payroll", YELLOW), (".", WHITE)], "Not the process.", "Org chart != go-to-market strategy."),
    ([("The public version ", WHITE), ("looks easy", YELLOW), (".", WHITE)], "", "The backstory was not sponsored."),
    ([("You don't see the ", WHITE), ("pain", RED), (".", WHITE)], "", "This is where the playbook was born."),
    ([("No playbook. ", WHITE), ("Just vibes", YELLOW), (".", WHITE)], "", "Good luck, Chad."),
    ([("A sequence is ", WHITE), ("not a playbook", YELLOW), (".", WHITE)], "", "Downloaded. Not validated."),
    ([("Message-market ", WHITE), ("fit", YELLOW), (".", WHITE)], "", "Dark science, but with spreadsheets."),
    ([("Don't be ", WHITE), ("creepy", RED), (".", WHITE)], "", "Personalization has a limit."),
    ([("Founders research ", WHITE), ("everything", YELLOW), (".", WHITE)], "", "Before buying one $49 tool."),
    ([("But when ", WHITE), ("selling", YELLOW), ("...", WHITE)], "That is called delulu.", "Bold strategy."),
    ([("SDRs are not the ", WHITE), ("machine", YELLOW), (".", WHITE)], "", "Operator != engine."),
    ([("The playbook is the ", WHITE), ("machine", GREEN), (".", WHITE)], "", "Build this first."),
    ([("Broken process + more people = ", WHITE), ("bigger mess", RED), (".", WHITE)], "", "Congrats, you scaled chaos."),
    ([("Just send ", WHITE), ("10,000 more emails", RED), (".", WHITE)], "", "Every weak strategy's favorite button."),
    ([("Dead message. ", WHITE), ("Faster rejection", RED), (".", WHITE)], "", "Industrialized rejection."),
    ([("2 people ", YELLOW), ("out of 100.", WHITE)], "", "That's the game."),
    ([("Find why they said ", WHITE), ("yes", GREEN), (".", WHITE)], "", "Pain? Timing? Competitor annoyed them?"),
    ([("The first 6 months are ", WHITE), ("not wasted", YELLOW), (".", WHITE)], "", "Distribution compounds silently."),
    ([("Not the SDR. Not the agency. ", WHITE), ("Not the tool", RED), (".", WHITE)], "The machine.", "The real asset."),
    ([("Build the ", WHITE), ("playbook", GREEN), (" first.", WHITE)], "", "Then scale."),
]


def ffmpeg_exe() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def font(size: int, bold: bool = False):
    p = Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()


def ease(x: float) -> float:
    x = max(0, min(1, x))
    return x * x * (3 - 2 * x)


def alpha_at(t: float, start: float, dur: float = 0.28) -> float:
    return ease((t - start) / dur)


def fit_asset(i: int) -> Image.Image:
    im = Image.open(ASSETS / f"slide{i:02d}.png").convert("RGB")
    scale = min(1632 / im.width, 760 / im.height)
    new = (round(im.width * scale), round(im.height * scale))
    resized = im.resize(new, Image.Resampling.LANCZOS)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer.paste(resized.convert("RGBA"), ((W - new[0]) // 2, 195), resized.convert("RGBA"))
    return layer


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt) -> int:
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]


def heading_layer(parts) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    full = "".join(t for t, _ in parts)
    size = 82
    if len(full) > 36:
        size = 70
    if len(full) > 48:
        size = 60
    f = font(size, True)
    total = sum(text_width(d, t, f) for t, _ in parts)
    x = max(56, (W - total) // 2)
    y = 52
    for text, color in parts:
        d.text((x, y), text, font=f, fill=color + (255,))
        x += text_width(d, text, f)
    return layer


def centered_text_layer(text: str, y: int, size: int, color) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    f = font(size, True)
    w = text_width(d, text, f)
    d.text(((W - w) // 2, y), text, font=f, fill=color + (255,))
    return layer


def bars_layer() -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.rectangle((0, 0, W, 155), fill=(0, 0, 0, 235))
    d.rectangle((0, 900, W, H), fill=(0, 0, 0, 210))
    return layer


def with_alpha(layer: Image.Image, a: float) -> Image.Image:
    out = layer.copy()
    alpha = out.getchannel("A").point(lambda p: int(p * max(0, min(1, a))))
    out.putalpha(alpha)
    return out


def render_slide(i: int, out_path: Path) -> None:
    from moviepy import VideoClip

    parts, support, caption = SLIDES[i - 1]
    image = fit_asset(i)
    bars = bars_layer()
    heading = heading_layer(parts)
    support_layer = centered_text_layer(support, 814, 45, WHITE) if support else None
    caption_layer = centered_text_layer(caption, 950, 38 if len(caption) < 34 else 32, YELLOW)

    def make_frame(t):
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
        canvas.alpha_composite(with_alpha(image, alpha_at(t, 0.10, 0.35)))
        canvas.alpha_composite(with_alpha(bars, alpha_at(t, 0.10, 0.25)))
        canvas.alpha_composite(with_alpha(heading, alpha_at(t, 0.55, 0.25)))
        if support_layer:
            canvas.alpha_composite(with_alpha(support_layer, alpha_at(t, 0.95, 0.25)))
        canvas.alpha_composite(with_alpha(caption_layer, alpha_at(t, 1.25, 0.30)))
        return np.array(canvas.convert("RGB"))

    clip = VideoClip(make_frame, duration=DUR)
    clip.write_videofile(
        str(out_path),
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="veryfast",
        ffmpeg_params=["-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0", "-movflags", "+faststart"],
        logger=None,
    )
    clip.close()


def concat_full() -> None:
    list_file = TEMP / "concat_clean_layered.txt"
    list_file.write_text("\n".join(f"file '{(CLEAN / f'slide_{i:02d}.mp4').as_posix()}'" for i in range(1, 25)), encoding="utf-8")
    raw = TEMP / "slides_full_clean_layered_raw.mp4"
    subprocess.run([ffmpeg_exe(), "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(raw)], check=True)
    subprocess.run([
        ffmpeg_exe(), "-y", "-i", str(raw), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
        "-preset", "veryfast", "-crf", "18", "-an", "-movflags", "+faststart", str(OUT / "slides_full_animated.mp4")
    ], check=True)


def main() -> None:
    CLEAN.mkdir(parents=True, exist_ok=True)
    TEMP.mkdir(parents=True, exist_ok=True)
    for i in range(1, 25):
        render_slide(i, CLEAN / f"slide_{i:02d}.mp4")
    if NOISY_BACKUP.exists():
        shutil.rmtree(NOISY_BACKUP)
    if VIDEOS.exists():
        shutil.copytree(VIDEOS, NOISY_BACKUP)
        shutil.rmtree(VIDEOS)
    shutil.copytree(CLEAN, VIDEOS)
    concat_full()


if __name__ == "__main__":
    main()
