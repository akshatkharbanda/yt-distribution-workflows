from __future__ import annotations

import math
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "video_assembly_v3"
EXPORTS = OUT / "exports"
SHEETS = OUT / "contact_sheets"
TEMP = OUT / "temp"
SLIDES = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "preview"
VIDEO = ROOT / "YT_ SDR Trap.mp4"

W, H, FPS = 1920, 1080, 30
LEFT_W, RIGHT_W = 1240, 680
PREVIEW_DUR = 75.0

TIMINGS = [
    (1, 2.879, 3.18, "founder raises funding"),
    (2, 7.000, 7.30, "hire SDRs"),
    (3, 14.280, 14.55, "Three months later"),
    (4, 21.359, 21.65, "burn rate vertical"),
    (5, 31.080, 31.35, "not scaling setup"),
    (6, 51.578, 51.85, "public payroll"),
    (7, 56.898, 57.20, "public version"),
    (8, 65.058, 65.35, "hidden pain"),
]

# More precise reveal cues for the first 75 seconds.
# visual_start: base image appears; headline_start: text/slide fully appears;
# caption_start: punchline/caption reveal. The source slide is flattened, so this
# preview approximates reveals with a dark hold and fade rather than editing each text layer.
REVEALS = {
    1: (3.00, 3.18, 3.90),
    2: (7.10, 7.35, 8.15),
    3: (14.35, 14.65, 15.35),
    4: (21.45, 21.75, 22.35),
    5: (31.25, 31.55, 33.35),
    6: (51.65, 51.95, 52.65),
    7: (57.00, 57.30, 58.15),
    8: (65.15, 65.45, 66.10),
}

SFX = [
    (7.30, "whoosh", 0.22),
    (14.55, "click", 0.12),
    (21.35, "riser", 0.45),
    (21.65, "impact", 0.18),
    (33.20, "impact", 0.16),
    (51.85, "stamp", 0.13),
    (65.35, "whoosh2", 0.22),
]


def ffmpeg_exe() -> str:
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def font(size: int, bold: bool = False):
    p = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    return ImageFont.truetype(p, size) if Path(p).exists() else ImageFont.load_default()


def ts(seconds: float) -> str:
    m = int(seconds // 60)
    s = seconds - m * 60
    return f"{m}:{s:05.2f}"


def fit_contain(img: Image.Image, box: tuple[int, int], bg=(3, 3, 3)) -> Image.Image:
    out = Image.new("RGB", box, bg)
    scale = min(box[0] / img.width, box[1] / img.height)
    new = (int(img.width * scale), int(img.height * scale))
    resized = img.resize(new, Image.Resampling.LANCZOS).convert("RGB")
    out.paste(resized, ((box[0] - new[0]) // 2, (box[1] - new[1]) // 2))
    return out


def load_slides() -> dict[int, Image.Image]:
    slides = {}
    for n in range(1, 9):
        slides[n] = fit_contain(Image.open(SLIDES / f"Slide{n}.PNG"), (LEFT_W, H), (2, 2, 2))
    return slides


def slide_for_time(t: float) -> int:
    current = 1
    for n, _, start, _ in TIMINGS:
        if t >= REVEALS[n][0]:
            current = n
    return current


def left_panel(slides: dict[int, Image.Image], t: float) -> Image.Image:
    n = slide_for_time(t)
    visual_start, headline_start, caption_start = REVEALS[n]
    img = slides[n].copy()
    # Approximate internal reveal with fade up. Keep the visual from feeling like
    # it reads before the line, while still using the flattened slide assets.
    if t < visual_start:
        img = Image.new("RGB", (LEFT_W, H), (2, 2, 2))
    elif t < headline_start:
        alpha = max(0.18, min(1.0, (t - visual_start) / max(0.01, headline_start - visual_start)))
        dark = Image.new("RGB", (LEFT_W, H), (2, 2, 2))
        img = Image.blend(dark, img, alpha * 0.55)
    elif t < caption_start:
        # Darken lower caption area until the punchline/caption window.
        overlay = Image.new("RGBA", (LEFT_W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)
        d.rectangle((0, int(H * 0.73), LEFT_W, H), fill=(0, 0, 0, 200))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def crop_face_frame(frame: np.ndarray, crop: str) -> Image.Image:
    img = Image.fromarray(frame).convert("RGB")
    if crop == "A":
        x, w = 555, 680
        return img.crop((x, 0, x + w, H)).resize((RIGHT_W, H), Image.Resampling.LANCZOS)
    # Looser by about 10 percent, then fit into the same right panel.
    x, w = 520, 760
    cropped = img.crop((x, 0, x + w, H))
    return cropped.resize((RIGHT_W, H), Image.Resampling.LANCZOS)


def make_frame_factory(crop: str):
    from moviepy import VideoFileClip

    source = VideoFileClip(str(VIDEO))
    slides = load_slides()

    def make_frame(t: float):
        frame = source.get_frame(t)
        canvas = Image.new("RGB", (W, H), (3, 3, 3))
        canvas.paste(left_panel(slides, t), (0, 0))
        canvas.paste(crop_face_frame(frame, crop), (LEFT_W, 0))
        d = ImageDraw.Draw(canvas)
        d.line((LEFT_W, 0, LEFT_W, H), fill=(32, 32, 32), width=3)
        return np.array(canvas)

    return make_frame, source


def render_base(crop: str, out_path: Path) -> None:
    from moviepy import AudioFileClip, VideoClip

    make_frame, source = make_frame_factory(crop)
    audio = AudioFileClip(str(VIDEO)).subclipped(0, PREVIEW_DUR)
    clip = VideoClip(make_frame, duration=PREVIEW_DUR).with_audio(audio)
    tmp = TEMP / f"base_crop{crop}.mp4"
    clip.write_videofile(
        str(tmp),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        audio_bitrate="192k",
        preset="veryfast",
        ffmpeg_params=["-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0", "-movflags", "+faststart"],
        logger=None,
    )
    source.close()
    audio.close()
    compat(tmp, out_path)


def compat(in_path: Path, out_path: Path) -> None:
    cmd = [
        ffmpeg_exe(), "-y", "-i", str(in_path),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
        "-preset", "veryfast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(out_path)
    ]
    subprocess.run(cmd, check=True)


def make_sheet(video_path: Path, out_path: Path) -> None:
    times = [0, 3.18, 7.30, 14.55, 21.65, 33.20, 51.85, 57.20, 65.35, 74.0]
    frames = []
    for t in times:
        p = TEMP / f"{video_path.stem}_{t:.2f}.jpg"
        subprocess.run([
            ffmpeg_exe(), "-y", "-ss", f"{t:.3f}", "-i", str(video_path),
            "-frames:v", "1", "-q:v", "2", str(p)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        im = Image.open(p).convert("RGB").resize((480, 270), Image.Resampling.LANCZOS)
        d = ImageDraw.Draw(im, "RGBA")
        d.rectangle((0, 0, 480, 34), fill=(0, 0, 0, 165))
        d.text((10, 7), ts(t), font=font(20, True), fill=(238, 255, 0))
        frames.append(im)
    sheet = Image.new("RGB", (960, 270 * math.ceil(len(frames) / 2)), (18, 18, 18))
    for i, im in enumerate(frames):
        sheet.paste(im, ((i % 2) * 480, (i // 2) * 270))
    sheet.save(out_path, quality=92)


def tone(kind: str, dur: float, sr=48000, quiet_db=0.0):
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    if kind.startswith("whoosh"):
        noise = np.random.default_rng(42 if kind == "whoosh" else 43).normal(0, 1, len(t))
        env = np.sin(np.linspace(0, math.pi, len(t))) ** 1.6
        sig = noise * env * 0.08
    elif kind == "click":
        sig = np.sin(2 * math.pi * 2400 * t) * np.exp(-t * 55) * 0.10
    elif kind == "stamp":
        sig = np.sin(2 * math.pi * 180 * t) * np.exp(-t * 22) * 0.13
    elif kind == "riser":
        freq = 220 + 520 * (t / max(dur, 0.001))
        sig = np.sin(2 * math.pi * freq * t) * np.linspace(0, 1, len(t)) * 0.05
    else:  # impact
        sig = np.sin(2 * math.pi * 95 * t) * np.exp(-t * 18) * 0.15
    sig *= 10 ** (quiet_db / 20)
    return sig


def write_sfx_wav(out_wav: Path, quiet_db: float = 0.0) -> None:
    import wave

    sr = 48000
    audio = np.zeros(int((PREVIEW_DUR + 1) * sr), dtype=np.float32)
    for start, kind, dur in SFX:
        s = int(start * sr)
        sig = tone(kind, dur, sr, quiet_db)
        audio[s:s + len(sig)] += sig.astype(np.float32)
    audio = np.clip(audio, -0.35, 0.35)
    pcm = (audio * 32767).astype(np.int16)
    with wave.open(str(out_wav), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes(pcm.tobytes())


def add_sfx(base_video: Path, out_path: Path, quiet: bool) -> None:
    wav = TEMP / ("sfx_quiet.wav" if quiet else "sfx_normal.wav")
    write_sfx_wav(wav, quiet_db=-5.0 if quiet else 0.0)
    cmd = [
        ffmpeg_exe(), "-y", "-i", str(base_video), "-i", str(wav),
        "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=0[a]",
        "-map", "0:v", "-map", "[a]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(out_path)
    ]
    subprocess.run(cmd, check=True)
    compat(out_path, out_path.with_name(out_path.stem + "_compat_tmp.mp4"))
    tmp = out_path.with_name(out_path.stem + "_compat_tmp.mp4")
    tmp.replace(out_path)


def main() -> None:
    EXPORTS.mkdir(parents=True, exist_ok=True)
    SHEETS.mkdir(parents=True, exist_ok=True)
    TEMP.mkdir(parents=True, exist_ok=True)

    crop_a = EXPORTS / "preview_75s_split_screen_cropA_v3.mp4"
    crop_b = EXPORTS / "preview_75s_split_screen_cropB_looser_v3.mp4"
    render_base("A", crop_a)
    render_base("B", crop_b)
    make_sheet(crop_a, SHEETS / "preview_75s_split_screen_cropA_v3_sheet.jpg")
    make_sheet(crop_b, SHEETS / "preview_75s_split_screen_cropB_looser_v3_sheet.jpg")
    add_sfx(crop_b, EXPORTS / "preview_75s_split_screen_sfx_normal_v3.mp4", quiet=False)
    add_sfx(crop_b, EXPORTS / "preview_75s_split_screen_sfx_quiet_v3.mp4", quiet=True)


if __name__ == "__main__":
    main()
