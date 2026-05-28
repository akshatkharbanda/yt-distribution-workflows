from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
OUT = ROOT / "slide_assets_for_clipchamp"
TEMP = OUT / "temp_powerpoint_fixed"
ANIM = OUT / "slide_videos_animated_powerpoint"
SLIDE_VIDEOS = OUT / "slide_videos"
SIMPLE_BACKUP = OUT / "slide_videos_simple_fade_backup"


def ffmpeg_exe() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def compat(infile: Path, outfile: Path) -> None:
    run([
        ffmpeg_exe(), "-y", "-i", str(infile),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,fps=30,format=yuv420p,setsar=1",
        "-an",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-profile:v", "high", "-level", "4.0",
        "-preset", "veryfast", "-crf", "18",
        "-movflags", "+faststart",
        str(outfile),
    ])


def inspect(path: Path) -> str:
    proc = subprocess.run([ffmpeg_exe(), "-hide_banner", "-i", str(path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return "\n".join(line.strip() for line in proc.stdout.splitlines() if "Duration:" in line or "Video:" in line or "Audio:" in line)


def main() -> None:
    ANIM.mkdir(parents=True, exist_ok=True)
    compat(TEMP / "slides_full_animated_powerpoint_fixed_raw.mp4", OUT / "slides_full_animated_powerpoint_native.mp4")
    for i in range(1, 25):
        compat(TEMP / f"slide_{i:02d}_powerpoint_fixed_raw.mp4", ANIM / f"slide_{i:02d}.mp4")

    if SIMPLE_BACKUP.exists():
        shutil.rmtree(SIMPLE_BACKUP)
    if SLIDE_VIDEOS.exists():
        shutil.copytree(SLIDE_VIDEOS, SIMPLE_BACKUP)
        shutil.rmtree(SLIDE_VIDEOS)
    shutil.copytree(ANIM, SLIDE_VIDEOS)

    (OUT / "temp_powerpoint_fixed" / "fixed_inspection.txt").write_text(
        inspect(OUT / "slides_full_animated_powerpoint_native.mp4") + "\n\n" + inspect(SLIDE_VIDEOS / "slide_01.mp4"),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
