"""Video and image helpers: durations, frame grabs, contact sheets."""
import json
import subprocess
from pathlib import Path

from PIL import Image


def run(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], check=True)


def durations(path) -> dict:
    """{'video': s, 'audio': s} from ffprobe."""
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,duration",
                        "-of", "json", str(path)], capture_output=True, text=True, check=True)
    return {s["codec_type"]: float(s.get("duration", 0)) for s in json.loads(p.stdout)["streams"]}


def grab(video, at: float, out):
    run("-ss", f"{max(at, 0):.3f}", "-i", video, "-frames:v", "1", out)
    return Path(out)


def contact(images, out, cols=4, width=320, label=True) -> Path:
    """Tile images into one sheet, each scaled to `width`, labelled with its file stem."""
    from PIL import ImageDraw
    ims = [Image.open(p).convert("RGB") for p in images]
    if not ims:
        raise ValueError("no images for a contact sheet")
    th = [int(i.height * width / i.width) for i in ims]
    cell_h = max(th) + (18 if label else 0)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * width, rows * cell_h), "white")
    d = ImageDraw.Draw(sheet)
    for k, (im, p) in enumerate(zip(ims, images)):
        x, y = (k % cols) * width, (k // cols) * cell_h
        sheet.paste(im.resize((width, th[k])), (x, y))
        if label:
            d.text((x + 4, y + th[k] + 3), Path(p).stem, fill="black")
    sheet.save(out)
    return Path(out)
