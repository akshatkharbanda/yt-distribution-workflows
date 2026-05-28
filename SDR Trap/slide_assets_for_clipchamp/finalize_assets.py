from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
OUT = ROOT / "slide_assets_for_clipchamp"
TEMP = OUT / "temp"
VIDEOS = OUT / "slide_videos"
IMAGES = OUT / "slide_images"


def ffmpeg_exe() -> str:
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def compat(infile: Path, outfile: Path) -> None:
    run([
        ffmpeg_exe(), "-y", "-i", str(infile),
        "-vf", "scale=1920:1080,fps=30,format=yuv420p",
        "-an",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-profile:v", "high",
        "-level", "4.0",
        "-preset", "veryfast",
        "-crf", "20",
        "-movflags", "+faststart",
        str(outfile),
    ])


def font(size: int, bold: bool = False):
    p = Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()


def make_contact_sheet() -> None:
    imgs = []
    for i in range(1, 25):
        p = IMAGES / f"slide_{i:02d}.png"
        im = Image.open(p).convert("RGB").resize((480, 270), Image.Resampling.LANCZOS)
        d = ImageDraw.Draw(im, "RGBA")
        d.rectangle((0, 0, 140, 38), fill=(0, 0, 0, 170))
        d.text((12, 8), f"Slide {i:02d}", font=font(22, True), fill=(238, 255, 0))
        imgs.append(im)
    sheet = Image.new("RGB", (1920, 1620), (18, 18, 18))
    for idx, im in enumerate(imgs):
        sheet.paste(im, ((idx % 4) * 480, (idx // 4) * 270))
    sheet.save(OUT / "contact_sheet_slide_assets.jpg", quality=92)


def inspect_mp4(p: Path) -> str:
    proc = subprocess.run(
        [ffmpeg_exe(), "-hide_banner", "-i", str(p)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    lines = []
    for line in proc.stdout.splitlines():
        if "Duration:" in line or "Video:" in line or "Audio:" in line:
            lines.append(line.strip())
    return "\n".join(lines)


def main() -> None:
    VIDEOS.mkdir(parents=True, exist_ok=True)
    full_raw = TEMP / "slides_full_animated_powerpoint_raw.mp4"
    compat(full_raw, OUT / "slides_full_animated.mp4")
    for i in range(1, 25):
        compat(TEMP / f"slide_{i:02d}_powerpoint_raw.mp4", VIDEOS / f"slide_{i:02d}.mp4")
    make_contact_sheet()
    checked = inspect_mp4(OUT / "slides_full_animated.mp4")
    (TEMP / "ffmpeg_inspection.txt").write_text(checked, encoding="utf-8")


if __name__ == "__main__":
    main()
