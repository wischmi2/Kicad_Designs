"""Draw labels and insertion arrows on Fusion base views.

Usage: python draw_callouts.py <json> [<json> ...] --out <folder>

JSON format (same as mechanical/crown/assembly_guide_2026-11-12/callouts/):
  image, width, height, note, crop [x0,y0,x1,y1] (optional),
  labels: [{text, x, y, side: left|right|top|bottom,
            arrow_dir: [dx,dy] (optional, short direction arrow),
            arrow_to: [x,y] (optional, thick arrow from the piece to its hole)}]
A label with empty text only draws its arrow.
"""
import argparse
import json
import math
import os

from PIL import Image, ImageDraw, ImageFont

RED = (200, 30, 30)
BLUE = (20, 90, 200)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)


def font(size):
    for name in ("arialbd.ttf", "DejaVuSans-Bold.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def arrow(draw, p0, p1, color, width, head):
    draw.line([p0, p1], fill=color, width=width)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        draw.line([p1, (p1[0] + head * math.cos(a), p1[1] + head * math.sin(a))],
                  fill=color, width=width)


def place_box(lab, tw, th, offset, W, H):
    x, y = lab["x"], lab["y"]
    side = lab.get("side", "right")
    if side == "left":
        bx, by = x - offset - tw, y - th / 2
    elif side == "top":
        bx, by = x - tw / 2, y - offset - th
    elif side == "bottom":
        bx, by = x - tw / 2, y + offset
    else:
        bx, by = x + offset, y - th / 2
    bx = min(max(bx, 4), W - tw - 4)
    by = min(max(by, 4), H - th - 4)
    return bx, by


def overlaps(a, b, pad=6):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0] or a[3] + pad < b[1] or b[3] + pad < a[1])


def render(json_path, out_dir):
    with open(json_path, encoding="utf-8") as f:
        spec = json.load(f)
    img = Image.open(os.path.join(os.path.dirname(json_path), spec["image"])).convert("RGB")
    crop = spec.get("crop")
    ox, oy = 0, 0
    if crop:
        img = img.crop(tuple(crop))
        ox, oy = crop[0], crop[1]
    W, H = img.size
    scale = max(W, H) / 1400.0
    fnt = font(int(30 * scale))
    lw = max(3, int(3 * scale))
    d = ImageDraw.Draw(img)
    labels = []
    for lab in spec["labels"]:
        lab = dict(lab)
        lab["x"] -= ox
        lab["y"] -= oy
        if "arrow_to" in lab:
            lab["arrow_to"] = [lab["arrow_to"][0] - ox, lab["arrow_to"][1] - oy]
        labels.append(lab)

    # Insertion arrows first (under the boxes).
    for lab in labels:
        if "arrow_to" in lab:
            p0 = (lab["x"], lab["y"])
            p1 = tuple(lab["arrow_to"])
            dx, dy = p1[0] - p0[0], p1[1] - p0[1]
            L = math.hypot(dx, dy) or 1
            gap = 8 * scale
            q0 = (p0[0] + dx / L * gap, p0[1] + dy / L * gap)
            arrow(d, q0, p1, BLUE, lw + 2, 22 * scale)
            r = 7 * scale
            d.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], outline=BLUE, width=lw)
        if "arrow_dir" in lab:
            dx, dy = lab["arrow_dir"]
            L = math.hypot(dx, dy) or 1
            n = 120 * scale
            p0 = (lab["x"], lab["y"])
            arrow(d, p0, (p0[0] + dx / L * n, p0[1] + dy / L * n), RED, lw, 22 * scale)

    placed = []
    for lab in labels:
        if not lab.get("text"):
            continue
        tb = d.textbbox((0, 0), lab["text"], font=fnt)
        tw, th = tb[2] - tb[0] + 16 * scale, tb[3] - tb[1] + 14 * scale
        offset = 160 * scale
        bx, by = place_box(lab, tw, th, offset, W, H)
        box = (bx, by, bx + tw, by + th)
        # Try pushing the box further out, then sliding it across the leader axis.
        tries = [(offset + k * 45 * scale, 0) for k in range(5)]
        tries += [(offset, s * k * (th + 8 * scale)) for k in range(1, 6) for s in (1, -1)]
        for off, shift in tries:
            bx, by = place_box(lab, tw, th, off, W, H)
            if lab.get("side", "right") in ("left", "right"):
                by = min(max(by + shift, 4), H - th - 4)
            else:
                bx = min(max(bx + shift, 4), W - tw - 4)
            cand = (bx, by, bx + tw, by + th)
            if not any(overlaps(cand, p) for p in placed):
                box = cand
                break
        placed.append(box)
        cx = min(max(lab["x"], box[0]), box[2])
        cy = min(max(lab["y"], box[1]), box[3])
        arrow(d, (cx, cy), (lab["x"], lab["y"]), RED, lw, 14 * scale)
        r = 5 * scale
        d.ellipse([lab["x"] - r, lab["y"] - r, lab["x"] + r, lab["y"] + r], fill=RED)
        d.rectangle(box, fill=WHITE, outline=RED, width=lw)
        d.text((box[0] + 8 * scale, box[1] + 5 * scale - tb[1]), lab["text"], font=fnt, fill=BLACK)

    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, os.path.splitext(spec["image"])[0] + "_labelled.png")
    img.save(out)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("json", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    for j in a.json:
        print(render(j, a.out))
