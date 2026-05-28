from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
PHASE = ROOT / "video_assembly_v2"
ASSETS = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "assets"
VIDEO = ROOT / "YT_ SDR Trap.mp4"
TEMP = PHASE / "temp"
EXPORTS = PHASE / "exports"
SHEETS = PHASE / "contact_sheets"

W, H = 1920, 1080
FPS = 30
PREVIEW_DUR = 75.0
IMG_X, IMG_Y, IMG_W, IMG_H = 144, 192, 1632, 774
TOP_BAND, BOTTOM_BAND = 208, 184

WHITE = (255, 255, 255)
YELLOW = (231, 255, 0)
RED = (255, 51, 51)
GREEN = (76, 255, 106)
BLACK = (0, 0, 0)


SLIDES = [
    dict(n=1, visual=0.560, headline=3.180, support=None, caption=5.100, parts=[("Founder raises ", WHITE), ("funding", YELLOW), (".", WHITE)], support_text="", caption_text="What could go wrong?"),
    dict(n=2, visual=6.850, headline=7.350, support=None, caption=12.900, parts=[("First move: ", WHITE), ("hire SDRs", YELLOW), (".", WHITE)], support_text="", caption_text="The outbound cinematic universe begins."),
    dict(n=3, visual=14.100, headline=14.650, support=16.900, caption=19.600, parts=[("3 months ", WHITE), ("later", YELLOW), ("...", WHITE)], support_text="Calendar: empty.", caption_text="Pipeline looking spacious."),
    dict(n=4, visual=21.200, headline=21.700, support=None, caption=23.900, parts=[("Burn rate: ", WHITE), ("vertical", RED), (".", WHITE)], support_text="", caption_text="At least something is growing."),
    dict(n=5, visual=30.950, headline=31.400, support=32.450, caption=35.100, parts=[("You aren't ", WHITE), ("scaling", YELLOW), (".", WHITE)], support_text="You're gambling.", caption_text="The house always wins."),
    dict(n=6, visual=51.350, headline=51.900, support=54.400, caption=55.900, parts=[("You copied the ", WHITE), ("payroll", YELLOW), (".", WHITE)], support_text="Not the process.", caption_text="Org chart != go-to-market strategy."),
    dict(n=7, visual=56.700, headline=57.250, support=None, caption=62.800, parts=[("The public version ", WHITE), ("looks easy", YELLOW), (".", WHITE)], support_text="", caption_text="The backstory was not sponsored."),
    dict(n=8, visual=64.900, headline=65.400, support=None, caption=70.900, parts=[("You don't see the ", WHITE), ("pain", RED), (".", WHITE)], support_text="", caption_text="This is where the playbook was born."),
    dict(n=9, visual=77.250, headline=77.800, support=None, caption=83.500, parts=[("No playbook. ", WHITE), ("Just vibes", YELLOW), (".", WHITE)], support_text="", caption_text="Good luck, Chad."),
]


def ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()


def run(cmd):
    subprocess.run(cmd, check=True)


def font(size):
    for candidate in [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"]:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


F_HEAD = font(70)
F_HEAD_SMALL = font(58)
F_SUP = font(50)
F_CAP = font(42)
F_CAP_SMALL = font(34)
F_LABEL = font(24)


def text_w(draw, text, f):
    return draw.textbbox((0, 0), text, font=f)[2]


def draw_rich_center(draw, parts, y, f, max_w=1780):
    total = sum(text_w(draw, t, f) for t, _ in parts)
    if total > max_w:
        f = F_HEAD_SMALL
        total = sum(text_w(draw, t, f) for t, _ in parts)
    x = max(40, (W - total) // 2)
    for t, c in parts:
        draw.text((x + 3, y + 3), t, font=f, fill=BLACK)
        draw.text((x, y), t, font=f, fill=c)
        x += text_w(draw, t, f)


def draw_center(draw, text, y, f, color):
    if not text:
        return
    tw = text_w(draw, text, f)
    if tw > 1700:
        f = F_CAP_SMALL
        tw = text_w(draw, text, f)
    x = (W - tw) // 2
    draw.text((x + 3, y + 3), text, font=f, fill=BLACK)
    draw.text((x, y), text, font=f, fill=color)


def fit_cover(im, w, h):
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    return im.crop(((nw - w) // 2, (nh - h) // 2, (nw + w) // 2, (nh + h) // 2))


def make_slide_state(slide, state):
    canvas = Image.new("RGB", (W, H), BLACK)
    im = Image.open(ASSETS / f"slide{slide['n']:02d}.png").convert("RGB")
    im = fit_cover(im, IMG_W, IMG_H)
    canvas.paste(im, (IMG_X, IMG_Y))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, 0, W, TOP_BAND], fill=BLACK)
    draw.rectangle([0, H - BOTTOM_BAND, W, H], fill=BLACK)
    if state >= 1:
        draw_rich_center(draw, slide["parts"], 52, F_HEAD)
    if state >= 2 and slide["support_text"]:
        draw_center(draw, slide["support_text"], 812, F_SUP, WHITE)
    if state >= 3:
        draw_center(draw, slide["caption_text"], 958, F_CAP, YELLOW)
    return canvas


def build_slide_timeline():
    TEMP.mkdir(parents=True, exist_ok=True)
    states = {}
    for s in SLIDES:
        for state in range(4):
            path = TEMP / f"v2_slide{s['n']:02d}_state{state}.png"
            make_slide_state(s, state).save(path)
            states[(s["n"], state)] = path

    events = [(0.0, 0, 0)]
    for s in SLIDES:
        if s["visual"] < PREVIEW_DUR:
            events.append((s["visual"], s["n"], 0))
        if s["headline"] < PREVIEW_DUR:
            events.append((s["headline"], s["n"], 1))
        if s["support"] and s["support"] < PREVIEW_DUR:
            events.append((s["support"], s["n"], 2))
        if s["caption"] < PREVIEW_DUR:
            events.append((s["caption"], s["n"], 3))
    events = sorted(events, key=lambda x: x[0])

    segments = []
    current_slide, current_state = 0, 0
    for idx, (t, slide_no, state) in enumerate(events):
        if idx > 0:
            prev_t = events[idx - 1][0]
            dur = t - prev_t
            if dur > 0.03:
                if current_slide == 0:
                    p = TEMP / "black.jpg"
                    if not p.exists():
                        Image.new("RGB", (W, H), BLACK).save(p)
                else:
                    p = states[(current_slide, current_state)]
                segments.append((p, dur))
        current_slide, current_state = slide_no, state
    last_t = events[-1][0]
    if last_t < PREVIEW_DUR:
        p = states[(current_slide, current_state)] if current_slide else TEMP / "black.jpg"
        segments.append((p, PREVIEW_DUR - last_t))

    ff = ffmpeg()
    cmd = [ff, "-y", "-hide_banner", "-loglevel", "error"]
    for p, dur in segments:
        cmd += ["-loop", "1", "-t", f"{dur:.3f}", "-i", str(p)]
    filters, labels = [], []
    for idx in range(len(segments)):
        filters.append(f"[{idx}:v]fps={FPS},format=yuv420p[v{idx}]")
        labels.append(f"[v{idx}]")
    filters.append("".join(labels) + f"concat=n={len(segments)}:v=1:a=0[outv]")
    slide_video = TEMP / "v2_preview_slide_timeline.mp4"
    cmd += ["-filter_complex", ";".join(filters), "-map", "[outv]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0", "-preset", "veryfast", "-crf", "20", str(slide_video)]
    run(cmd)
    return slide_video


def export_layouts(slide_video):
    EXPORTS.mkdir(parents=True, exist_ok=True)
    ff = ffmpeg()
    out_a = EXPORTS / "preview_75s_slide_first_v2.mp4"
    pip_filter = "[1:v]scale=400:-2,format=rgba[pip];[pip]pad=iw+12:ih+12:6:6:color=white@0.95[pipb];[0:v][pipb]overlay=W-w-46:H-h-46:format=auto[v]"
    run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(slide_video), "-i", str(VIDEO),
         "-filter_complex", pip_filter, "-map", "[v]", "-map", "1:a:0", "-t", str(PREVIEW_DUR),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0", "-preset", "veryfast", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out_a)])

    out_b = EXPORTS / "preview_75s_face_first_v2.mp4"
    # Face-first: source video full-screen, slide panel left with dark backing.
    # Keep the panel just over 40% of screen width so it does not cover the speaker's face.
    panel_filter = (
        "[1:v]scale=740:-2,format=rgba[slide];"
        "[0:v]drawbox=x=34:y=164:w=780:h=455:color=black@0.74:t=fill[base];"
        "[base][slide]overlay=54:186:format=auto[v]"
    )
    run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(VIDEO), "-i", str(slide_video),
         "-filter_complex", panel_filter, "-map", "[v]", "-map", "0:a:0", "-t", str(PREVIEW_DUR),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0", "-preset", "veryfast", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out_b)])
    return out_a, out_b


def make_sheet(video, out):
    ff = ffmpeg()
    times = [0, 1, 7, 8, 14.1, 15.1, 21.2, 22.2, 31, 32, 51.4, 52.4, 56.7, 57.7, 64.9, 65.9, 70.9, 72.0]
    frames = []
    frame_dir = TEMP / out.stem
    frame_dir.mkdir(exist_ok=True)
    for idx, t in enumerate(times):
        p = frame_dir / f"f{idx:03d}.jpg"
        run([ff, "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-q:v", "3", str(p)])
        im = Image.open(p).resize((320, 180), Image.LANCZOS).convert("RGB")
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 95, 24], fill=BLACK)
        d.text((4, 2), f"{t:.1f}s", font=F_LABEL, fill=WHITE)
        frames.append(im)
    cols = 3
    rows = math.ceil(len(frames) / cols)
    sheet = Image.new("RGB", (cols * 320, rows * 180), BLACK)
    for idx, im in enumerate(frames):
        sheet.paste(im, ((idx % cols) * 320, (idx // cols) * 180))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=88)


def main():
    slide_video = build_slide_timeline()
    out_a, out_b = export_layouts(slide_video)
    make_sheet(out_a, SHEETS / "preview_75s_slide_first_v2_sheet.jpg")
    make_sheet(out_b, SHEETS / "preview_75s_face_first_v2_sheet.jpg")
    print(out_a)
    print(out_b)


if __name__ == "__main__":
    main()
