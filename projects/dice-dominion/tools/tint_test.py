#!/usr/bin/env python3
"""가문 색 변형을 코드 틴트로 만들 수 있는지 시험한다 (B3).

판 시안에는 네 가문의 미니어처가 이미 그려져 있다. 그래서 물어볼 수 있다.
  보라 미니어처의 색상을 회전시키면 실제로 그려진 청·적·녹과 같아지는가?
  그 과정에서 피부와 금속은 어떻게 되는가?

윗줄이 실제로 그려진 것, 아랫줄이 보라에서 코드로 돌린 것이다. 판단은 사람이 한다.
"""
import colorsys
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).parent))
import kfont

# 판 시안(1672×941)에서 네 미니어처의 위치. 정규화 좌표.
MINI = {
    "purple": (0.248, 0.062, 0.290, 0.215),
    "blue":   (0.708, 0.055, 0.760, 0.208),
    "red":    (0.690, 0.550, 0.742, 0.755),
    "green":  (0.272, 0.550, 0.322, 0.755),
}
# 받침대에서 측정된 색상(도). extract_palette.py board 결과.
HUE = {"purple": 275.8, "blue": 209.7, "red": 7.3, "green": 94.6}


def rotate_hue(im: Image.Image, delta: float, only_hue=None, window=45.0, min_sat=0.25) -> Image.Image:
    """only_hue를 주면 그 색상 ±window 안, 채도 min_sat 이상인 화소만 돌린다.
    피부와 금속을 건드리지 않기 위한 것이다."""
    a = np.asarray(im.convert("RGB")).astype(np.float64) / 255
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    l = (mx + mn) / 2
    c = mx - mn
    s = np.where(c == 0, 0, c / np.maximum(1 - np.abs(2 * l - 1), 1e-6))
    cc = np.maximum(c, 1e-6)
    h = np.where(mx == r, ((g - b) / cc) % 6, np.where(mx == g, (b - r) / cc + 2, (r - g) / cc + 4)) * 60
    if only_hue is None:
        mask = np.ones(h.shape, bool)
    else:
        d = np.abs((h - only_hue + 180) % 360 - 180)
        mask = (d <= window) & (s >= min_sat)
    h = np.where(mask, (h + delta) % 360, h)
    out = np.zeros_like(a)
    it = np.nditer(h, flags=["multi_index"])
    for _ in it:
        i = it.multi_index
        out[i] = colorsys.hls_to_rgb(h[i] / 360, l[i], min(s[i], 1))
    return Image.fromarray((out * 255).astype(np.uint8))


def main(src: Path, out: Path):
    im = Image.open(src).convert("RGB")
    W, H = im.size
    crops = {k: im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).resize((150, 300))
             for k, (x0, y0, x1, y1) in MINI.items()}

    order = ["purple", "blue", "red", "green"]
    pad, top = 16, 34
    sheet = Image.new("RGB", (pad + 4 * (150 + pad), top * 2 + 300 * 2 + pad * 3), (36, 34, 38))
    d = ImageDraw.Draw(sheet)
    f = kfont.load(13)
    d.text((pad, 8), "윗줄 — 판 시안에 실제로 그려진 네 가문", fill=(230, 230, 230), font=f)
    for i, k in enumerate(order):
        sheet.paste(crops[k], (pad + i * (150 + pad), top))
        d.text((pad + i * (150 + pad), top + 302), k, fill=(180, 180, 186), font=f)

    y2 = top + 300 + pad + top
    d.text((pad, y2 - 26), "아랫줄 — 보라 한 장을 코드로 색상 회전한 결과", fill=(230, 230, 230), font=f)
    for i, k in enumerate(order):
        delta = HUE[k] - HUE["purple"]
        tinted = crops["purple"] if k == "purple" else rotate_hue(crops["purple"], delta)
        sheet.paste(tinted, (pad + i * (150 + pad), y2))
        label = "원본" if k == "purple" else f"{k}  ({delta:+.0f}°)"
        d.text((pad + i * (150 + pad), y2 + 302), label, fill=(180, 180, 186), font=f)

    y3 = y2 + 300 + pad + top
    sheet2 = Image.new("RGB", (sheet.width, y3 + 300 + pad + 26), (36, 34, 38))
    sheet2.paste(sheet, (0, 0))
    d = ImageDraw.Draw(sheet2)
    d.text((pad, y3 - 26), "셋째 줄 — 의상·받침대 색상대만 골라 회전 (피부·금속 보존)",
           fill=(230, 230, 230), font=f)
    for i, k in enumerate(order):
        delta = HUE[k] - HUE["purple"]
        t = crops["purple"] if k == "purple" else rotate_hue(crops["purple"], delta, only_hue=HUE["purple"])
        sheet2.paste(t, (pad + i * (150 + pad), y3))
        d.text((pad + i * (150 + pad), y3 + 302), "원본" if k == "purple" else k,
               fill=(180, 180, 186), font=f)
    sheet = sheet2

    out.mkdir(parents=True, exist_ok=True)
    sheet.save(out / "tint_test.png")
    print(f'→ {out}/tint_test.png')


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
