from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
OUT = ROOT / "slide_assets_for_clipchamp"
VIDEOS = OUT / "slide_videos"
IMAGES = OUT / "slide_images"
TEMP = OUT / "temp"
SOURCE_PREVIEW = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "preview"


def ffmpeg_exe() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def font(size: int, bold: bool = False):
    p = Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf")
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()


def normalize_images() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    for i in range(1, 25):
        src = SOURCE_PREVIEW / f"Slide{i}.PNG"
        dst = IMAGES / f"slide_{i:02d}.png"
        im = Image.open(src).convert("RGB")
        canvas = Image.new("RGB", (1920, 1080), (0, 0, 0))
        scale = min(1920 / im.width, 1080 / im.height)
        resized = im.resize((round(im.width * scale), round(im.height * scale)), Image.Resampling.LANCZOS)
        canvas.paste(resized, ((1920 - resized.width) // 2, (1080 - resized.height) // 2))
        canvas.save(dst)


def create_slide_video(i: int) -> None:
    src = IMAGES / f"slide_{i:02d}.png"
    out = VIDEOS / f"slide_{i:02d}.mp4"
    vf = (
        "scale=1920:1080:force_original_aspect_ratio=decrease,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,"
        "fps=30,fade=t=in:st=0.50:d=0.35,fade=t=out:st=2.75:d=0.25,"
        "format=yuv420p,setsar=1"
    )
    run([
        ffmpeg_exe(), "-y",
        "-loop", "1", "-t", "3.0", "-i", str(src),
        "-vf", vf,
        "-an",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-profile:v", "high", "-level", "4.0",
        "-r", "30", "-preset", "veryfast", "-crf", "18",
        "-movflags", "+faststart",
        str(out),
    ])


def concat_full() -> None:
    list_file = TEMP / "concat_slide_videos.txt"
    list_file.write_text(
        "\n".join(f"file '{(VIDEOS / f'slide_{i:02d}.mp4').as_posix()}'" for i in range(1, 25)),
        encoding="utf-8",
    )
    raw = TEMP / "slides_full_recreated_raw.mp4"
    run([
        ffmpeg_exe(), "-y",
        "-f", "concat", "-safe", "0", "-i", str(list_file),
        "-c", "copy", str(raw),
    ])
    run([
        ffmpeg_exe(), "-y", "-i", str(raw),
        "-vf", "scale=1920:1080,fps=30,format=yuv420p,setsar=1",
        "-an",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-profile:v", "high", "-level", "4.0",
        "-preset", "veryfast", "-crf", "18",
        "-movflags", "+faststart",
        str(OUT / "slides_full_animated.mp4"),
    ])


def make_contact_sheet() -> None:
    thumbs = []
    for i in range(1, 25):
        im = Image.open(IMAGES / f"slide_{i:02d}.png").convert("RGB").resize((480, 270), Image.Resampling.LANCZOS)
        d = ImageDraw.Draw(im, "RGBA")
        d.rectangle((0, 0, 140, 38), fill=(0, 0, 0, 170))
        d.text((12, 8), f"Slide {i:02d}", font=font(22, True), fill=(238, 255, 0))
        thumbs.append(im)
    sheet = Image.new("RGB", (1920, 1620), (18, 18, 18))
    for idx, im in enumerate(thumbs):
        sheet.paste(im, ((idx % 4) * 480, (idx // 4) * 270))
    sheet.save(OUT / "contact_sheet_slide_assets.jpg", quality=92)


def inspect(path: Path) -> str:
    proc = subprocess.run([ffmpeg_exe(), "-hide_banner", "-i", str(path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return "\n".join(line.strip() for line in proc.stdout.splitlines() if "Duration:" in line or "Video:" in line or "Audio:" in line)


def main() -> None:
    VIDEOS.mkdir(parents=True, exist_ok=True)
    TEMP.mkdir(parents=True, exist_ok=True)
    normalize_images()
    for i in range(1, 25):
        create_slide_video(i)
    concat_full()
    make_contact_sheet()
    (TEMP / "final_inspection.txt").write_text(inspect(OUT / "slides_full_animated.mp4"), encoding="utf-8")


if __name__ == "__main__":
    main()
