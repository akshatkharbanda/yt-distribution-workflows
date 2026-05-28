from pathlib import Path
import math
import subprocess
import json

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

ROOT = Path(r"C:\Codex Projects\YT\SDR Trap")
PHASE = ROOT / "video_assembly_v1"
ASSETS = ROOT / "outputs" / "stop_scaling_chaos_full_deck" / "assets"
VIDEO = ROOT / "YT_ SDR Trap.mp4"
TEMP = PHASE / "temp"
EXPORTS = PHASE / "exports"
CONTACT = PHASE / "contact_sheets"

W, H = 1920, 1080
FPS = 30
TOP_BAND = 208
BOTTOM_BAND = 184
IMG_X, IMG_Y, IMG_W, IMG_H = 144, 192, 1632, 774

YELLOW = (231, 255, 0)
RED = (255, 51, 51)
GREEN = (76, 255, 106)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SLIDES = [
    (1, 0, 7, [("Founder raises ", WHITE), ("funding", YELLOW), (".", WHITE)], "", "What could go wrong?"),
    (2, 7, 18, [("First move: ", WHITE), ("hire SDRs", YELLOW), (".", WHITE)], "", "The outbound cinematic universe begins."),
    (3, 18, 27, [("3 months ", WHITE), ("later", YELLOW), ("...", WHITE)], "Calendar: empty.", "Pipeline looking spacious."),
    (4, 27, 36, [("Burn rate: ", WHITE), ("vertical", RED), (".", WHITE)], "", "At least something is growing."),
    (5, 36, 45, [("You aren't ", WHITE), ("scaling", YELLOW), (".", WHITE)], "You're gambling.", "The house always wins."),
    (6, 45, 55, [("You copied the ", WHITE), ("payroll", YELLOW), (".", WHITE)], "Not the process.", "Org chart != go-to-market strategy."),
    (7, 55, 65, [("The public version ", WHITE), ("looks easy", YELLOW), (".", WHITE)], "", "The backstory was not sponsored."),
    (8, 65, 77, [("You don't see the ", WHITE), ("pain", RED), (".", WHITE)], "", "This is where the playbook was born."),
    (9, 77, 90, [("No playbook. ", WHITE), ("Just vibes", YELLOW), (".", WHITE)], "", "Good luck, Chad."),
    (10, 90, 101, [("A sequence is ", WHITE), ("not a playbook", YELLOW), (".", WHITE)], "", "Downloaded. Not validated."),
    (11, 101, 116, [("Message-market ", WHITE), ("fit", YELLOW), (".", WHITE)], "", "Dark science, but with spreadsheets."),
    (12, 116, 135, [("Don't be ", WHITE), ("creepy", RED), (".", WHITE)], "", "Personalization has a limit."),
    (13, 135, 148, [("Founders research ", WHITE), ("everything", YELLOW), (".", WHITE)], "", "Before buying one $49 tool."),
    (14, 148, 180, [("But when ", WHITE), ("selling", YELLOW), ("...", WHITE)], "That is called delulu.", "Bold strategy."),
    (15, 180, 192, [("SDRs are not the ", WHITE), ("machine", YELLOW), (".", WHITE)], "", "Operator != engine."),
    (16, 192, 207, [("The playbook is the ", WHITE), ("machine", GREEN), (".", WHITE)], "", "Build this first."),
    (17, 207, 225, [("Broken process + more people = ", WHITE), ("bigger mess", RED), (".", WHITE)], "", "Congrats, you scaled chaos."),
    (18, 225, 237, [("Just send ", WHITE), ("10,000 more emails", RED), (".", WHITE)], "", "Every weak strategy's favorite button."),
    (19, 237, 253, [("Dead message. ", WHITE), ("Faster rejection", RED), (".", WHITE)], "", "Industrialized rejection."),
    (20, 253, 272, [("2 people ", YELLOW), ("out of 100.", WHITE)], "", "That's the game."),
    (21, 272, 300, [("Find why they said ", WHITE), ("yes", GREEN), (".", WHITE)], "", "Pain? Timing? Competitor annoyed them?"),
    (22, 300, 318, [("The first 6 months are ", WHITE), ("not wasted", YELLOW), (".", WHITE)], "", "Distribution compounds silently."),
    (23, 318, 332, [("Not the SDR. Not the agency. ", WHITE), ("Not the tool", RED), (".", WHITE)], "The machine.", "The real asset."),
    (24, 332, 345.72, [("Build the ", WHITE), ("playbook", GREEN), (" first.", WHITE)], "", "Then scale."),
]


def ffmpeg_path():
    return imageio_ffmpeg.get_ffmpeg_exe()


def run(cmd):
    subprocess.run(cmd, check=True)


def font(size):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\Arialbd.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


F_HEADING = font(70)
F_HEADING_SMALL = font(58)
F_SUPPORT = font(50)
F_CAPTION = font(42)
F_CAPTION_SMALL = font(34)
F_LABEL = font(24)


def text_w(draw, text, f):
    if not text:
        return 0
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0]


def draw_rich_center(draw, parts, y, f, max_w=1780):
    total = sum(text_w(draw, t, f) for t, _ in parts)
    if total > max_w:
        f = F_HEADING_SMALL
        total = sum(text_w(draw, t, f) for t, _ in parts)
    x = 60
    if total < max_w:
        x = (W - total) // 2
    for text, color in parts:
        draw.text((x + 3, y + 3), text, font=f, fill=(0, 0, 0))
        draw.text((x, y), text, font=f, fill=color)
        x += text_w(draw, text, f)


def draw_center(draw, text, y, f, color, max_w=1700):
    if not text:
        return
    tw = text_w(draw, text, f)
    if tw > max_w:
        f = F_CAPTION_SMALL
        tw = text_w(draw, text, f)
    x = (W - tw) // 2
    draw.text((x + 3, y + 3), text, font=f, fill=(0, 0, 0))
    draw.text((x, y), text, font=f, fill=color)


def fit_cover(im, w, h):
    iw, ih = im.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    return im.crop(((nw - w) // 2, (nh - h) // 2, (nw + w) // 2, (nh + h) // 2))


def make_state(slide_no, parts, support, caption, state):
    canvas = Image.new("RGB", (W, H), BLACK)
    img = Image.open(ASSETS / f"slide{slide_no:02d}.png").convert("RGB")
    img = fit_cover(img, IMG_W, IMG_H)
    canvas.paste(img, (IMG_X, IMG_Y))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 0, W, TOP_BAND], fill=(0, 0, 0))
    d.rectangle([0, H - BOTTOM_BAND, W, H], fill=(0, 0, 0))
    if state >= 1:
        draw_rich_center(d, parts, 52, F_HEADING)
    if state >= 2 and support:
        draw_center(d, support, 812, F_SUPPORT, WHITE)
    if state >= 3:
        draw_center(d, caption, 958, F_CAPTION, YELLOW)
    return canvas


def create_slide_video():
    TEMP.mkdir(parents=True, exist_ok=True)
    segments = []
    ff = ffmpeg_path()
    for slide_no, start, end, parts, support, caption in SLIDES:
        dur = end - start
        state_paths = []
        for state in range(4):
            p = TEMP / f"slide{slide_no:02d}_state{state}.png"
            make_state(slide_no, parts, support, caption, state).save(p, quality=95)
            state_paths.append(p)

        has_support = bool(support)
        d0 = 0.35
        d1 = 0.45 if has_support else 0.55
        caption_at = max(1.8, min(dur * 0.68, dur - 1.25))
        seg = TEMP / f"slide{slide_no:02d}.mp4"
        if has_support:
            use_paths = [state_paths[0], state_paths[1], state_paths[2], state_paths[3]]
            use_durs = [d0, d1, max(0.2, caption_at - d0 - d1), max(0.4, dur - caption_at)]
        else:
            use_paths = [state_paths[0], state_paths[1], state_paths[3]]
            use_durs = [d0, max(0.2, caption_at - d0), max(0.4, dur - caption_at)]

        cmd = [ff, "-y", "-hide_banner", "-loglevel", "error"]
        for p, dsec in zip(use_paths, use_durs):
            cmd += ["-loop", "1", "-t", f"{dsec:.3f}", "-i", str(p)]
        filters = []
        labels = []
        for idx in range(len(use_paths)):
            filters.append(f"[{idx}:v]fps={FPS},format=yuv420p[v{idx}]")
            labels.append(f"[v{idx}]")
        filters.append("".join(labels) + f"concat=n={len(use_paths)}:v=1:a=0[outv]")
        cmd += ["-filter_complex", ";".join(filters), "-map", "[outv]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(seg)]
        run(cmd)
        segments.append(seg)

    concat_all = TEMP / "slides_concat.txt"
    with concat_all.open("w", encoding="utf-8") as f:
        for seg in segments:
            f.write(f"file '{seg.as_posix()}'\n")
    out = TEMP / "slides_recreated_animation_v1.mp4"
    run([ff, "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat_all),
         "-c", "copy", str(out)])
    return out


def compose_final(slide_video):
    EXPORTS.mkdir(parents=True, exist_ok=True)
    ff = ffmpeg_path()
    out = EXPORTS / "stop_scaling_chaos_recreated_animation_pip_v1.mp4"
    # PiP width is 400px, about 21% of 1920. Border and shadow keep it readable.
    filter_complex = (
        "[1:v]scale=400:-2,format=rgba[pip];"
        "[pip]pad=iw+12:ih+12:6:6:color=white@0.95[pipb];"
        "[0:v][pipb]overlay=W-w-46:H-h-46:format=auto[v]"
    )
    run([ff, "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(slide_video), "-i", str(VIDEO),
         "-filter_complex", filter_complex,
         "-map", "[v]", "-map", "1:a:0",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
         "-c:a", "aac", "-b:a", "192k",
         "-shortest", "-movflags", "+faststart", str(out)])
    return out


def make_preview(final):
    ff = ffmpeg_path()
    out = EXPORTS / "preview_first_60s_v1.mp4"
    run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(final), "-t", "60",
         "-c", "copy", str(out)])
    return out


def make_contact_sheet(final):
    ff = ffmpeg_path()
    frame_dir = TEMP / "contact_frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    times = []
    for slide_no, start, end, *_ in SLIDES:
        times.append((slide_no, start))
        if start + 1 < end:
            times.append((slide_no, start + 1))
    frames = []
    for idx, (slide_no, t) in enumerate(times):
        p = frame_dir / f"frame_{idx:03d}.jpg"
        run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(final), "-ss", f"{t:.3f}",
             "-frames:v", "1", "-q:v", "3", str(p)])
        im = Image.open(p).resize((320, 180), Image.LANCZOS).convert("RGB")
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 115, 24], fill=(0, 0, 0))
        d.text((4, 3), f"S{slide_no} {t:.0f}s", font=F_LABEL, fill=WHITE)
        frames.append(im)
    cols = 4
    rows = math.ceil(len(frames) / cols)
    sheet = Image.new("RGB", (cols * 320, rows * 180), BLACK)
    for i, im in enumerate(frames):
        sheet.paste(im, ((i % cols) * 320, (i // cols) * 180))
    out = CONTACT / "contact_sheet_v1.jpg"
    sheet.save(out, quality=88)
    return out


def probe_duration(path):
    ff = ffmpeg_path()
    p = subprocess.run([ff, "-hide_banner", "-i", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p.stderr


def main():
    slide_video = create_slide_video()
    final = compose_final(slide_video)
    preview = make_preview(final)
    sheet = make_contact_sheet(final)
    summary = {
        "slide_video": str(slide_video),
        "final": str(final),
        "preview": str(preview),
        "contact_sheet": str(sheet),
    }
    (PHASE / "temp" / "render_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
