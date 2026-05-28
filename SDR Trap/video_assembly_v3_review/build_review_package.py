from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "video_assembly_v3_review"
ASSETS = OUT / "assets"
SLIDES = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "preview"
VIDEO = ROOT / "YT_ SDR Trap.mp4"

LEFT_W, RIGHT_W, H = 1240, 680, 1080
CANVAS = (1920, 1080)

TIMINGS = [
    (1, "founder raises funding", 2.879, 3.18, "Founder raises funding."),
    (2, "hire SDRs", 7.000, 7.30, "First move: hire SDRs."),
    (3, "Three months later", 14.280, 14.55, "3 months later..."),
    (4, "burn rate vertical", 21.359, 21.65, "Burn rate: vertical."),
    (5, "you're gambling", 32.920, 33.20, "You're gambling."),
    (6, "public payroll", 51.578, 51.85, "You copied the payroll."),
    (7, "public version", 56.898, 57.20, "The public version looks easy."),
    (8, "you don't see pain", 65.058, 65.35, "You don't see the pain."),
    (9, "25-year-old SDR", 77.458, 77.75, "No playbook. Just vibes."),
    (10, "email sequence", 82.904, 83.20, "A sequence is not a playbook."),
    (11, "message-market fit", 89.664, 89.95, "Message-market fit."),
    (12, "becomes creepy", 111.824, 112.10, "Don't be creepy."),
    (13, "careful buyers", 119.130, 119.40, "Founders research everything."),
    (14, "one cold email", 136.450, 136.75, "But when selling..."),
    (15, "not the machine", 154.775, 155.05, "SDRs are not the machine."),
    (16, "playbook is machine", 161.135, 161.42, "The playbook is the machine."),
    (17, "more operators", 172.607, 172.90, "Broken process + more people = bigger mess."),
    (18, "more volume", 189.519, 189.80, "Just send 10,000 more emails."),
    (19, "message is dead", 201.120, 201.40, "Dead message. Faster rejection."),
    (20, "2 out of 100", 240.839, 241.12, "2 people out of 100."),
    (21, "why they said yes", 250.119, 250.40, "Find why they said yes."),
    (22, "6 months not wasted", 261.999, 262.28, "The first 6 months are not wasted."),
    (23, "not SDR agency tool", 294.479, 294.76, "Not the SDR. Not the agency. Not the tool."),
    (24, "build playbook first", 300.119, 300.42, "Build the playbook first."),
]

REPRESENTATIVE = [
    ("start", 1, 3.18),
    ("funding", 1, 3.18),
    ("SDR", 2, 7.30),
    ("burn rate", 4, 21.65),
    ("gambling", 5, 33.20),
    ("payroll", 6, 51.85),
    ("public version", 7, 57.20),
    ("pain", 8, 65.35),
]


def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def ts(seconds: float) -> str:
    m = int(seconds // 60)
    s = seconds - m * 60
    return f"{m}:{s:05.2f}"


def slide_path(n: int) -> Path:
    return SLIDES / f"Slide{n}.PNG"


def fit_contain(img: Image.Image, box: tuple[int, int], bg=(5, 5, 5)) -> Image.Image:
    out = Image.new("RGB", box, bg)
    scale = min(box[0] / img.width, box[1] / img.height)
    new = (int(img.width * scale), int(img.height * scale))
    resized = img.resize(new, Image.Resampling.LANCZOS).convert("RGB")
    out.paste(resized, ((box[0] - new[0]) // 2, (box[1] - new[1]) // 2))
    return out


def extract_frame(seconds: float, out_path: Path) -> None:
    if out_path.exists():
        return
    cmd = [
        ffmpeg_exe(),
        "-y",
        "-ss",
        f"{seconds:.3f}",
        "-i",
        str(VIDEO),
        "-frames:v",
        "1",
        "-q:v",
        "2",
        str(out_path),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def crop_face(frame: Image.Image) -> Image.Image:
    # Crop centered on the speaker for a tall right-side panel. This keeps head,
    # shoulders, and some hands while dropping unused side background.
    crop_x, crop_w = 555, 680
    crop = frame.crop((crop_x, 0, crop_x + crop_w, 1080))
    return crop.resize((RIGHT_W, H), Image.Resampling.LANCZOS).convert("RGB")


def split_screen(slide_num: int, seconds: float, label: str) -> Image.Image:
    canvas = Image.new("RGB", CANVAS, (3, 3, 3))
    slide = fit_contain(Image.open(slide_path(slide_num)), (LEFT_W, H), (2, 2, 2))
    frame_path = ASSETS / f"face_{seconds:.2f}.jpg"
    extract_frame(seconds, frame_path)
    face = crop_face(Image.open(frame_path).convert("RGB"))
    canvas.paste(slide, (0, 0))
    canvas.paste(face, (LEFT_W, 0))
    d = ImageDraw.Draw(canvas, "RGBA")
    d.rectangle((0, 0, 1920, 54), fill=(0, 0, 0, 155))
    d.text((28, 12), f"{label}  |  {ts(seconds)}", font=font(28, True), fill=(255, 255, 255))
    d.line((LEFT_W, 0, LEFT_W, H), fill=(35, 35, 35), width=3)
    return canvas


def build_review_sheet() -> None:
    tile_w, tile_h = 480, 270
    label_h = 68
    cols, rows = 4, 6
    sheet = Image.new("RGB", (cols * tile_w, rows * (tile_h + label_h)), (16, 16, 16))
    d = ImageDraw.Draw(sheet)
    for idx, (n, cue, cue_t, start_t, heading) in enumerate(TIMINGS):
        x = (idx % cols) * tile_w
        y = (idx // cols) * (tile_h + label_h)
        img = fit_contain(Image.open(slide_path(n)), (tile_w, tile_h), (4, 4, 4))
        sheet.paste(img, (x, y))
        delay = start_t - cue_t
        d.rectangle((x, y + tile_h, x + tile_w, y + tile_h + label_h), fill=(24, 24, 24))
        d.text((x + 10, y + tile_h + 8), f"Slide {n} | {ts(start_t)} | +{delay:.2f}s", font=font(20, True), fill=(238, 255, 0))
        d.text((x + 10, y + tile_h + 36), cue[:42], font=font(18), fill=(245, 245, 245))
    sheet.save(OUT / "review_contact_sheet.jpg", quality=92)


def build_crop_sheet() -> None:
    tile = (960, 540)
    cols, rows = 2, math.ceil(len(REPRESENTATIVE) / 2)
    sheet = Image.new("RGB", (cols * tile[0], rows * tile[1]), (18, 18, 18))
    for idx, (label, slide_num, seconds) in enumerate(REPRESENTATIVE):
        img = split_screen(slide_num, seconds, label)
        img = img.resize(tile, Image.Resampling.LANCZOS)
        x = (idx % cols) * tile[0]
        y = (idx // cols) * tile[1]
        sheet.paste(img, (x, y))
    sheet.save(OUT / "crop_layout_contact_sheet.jpg", quality=92)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    build_review_sheet()
    build_crop_sheet()


if __name__ == "__main__":
    main()
