#!/usr/bin/env python3
"""콘셉트 아트에서 의미 토큰 단위의 색값을 뽑고, 검증용 시트를 함께 만든다.

색을 눈으로 짐작하지 않기 위한 도구다. 뽑은 값이 의도한 자리에서 나왔는지
사람이 바로 확인할 수 있도록, 표본 위치를 표시한 지도와 색 견본을 같이 낸다.

    python3 extract_palette.py battle <이미지> <출력폴더>
    python3 extract_palette.py board  <이미지> <출력폴더>

영역 안에서 무엇을 고르는지가 중요하다. 표 영역의 중앙값은 바탕색이고
그 안의 글자색은 어두운 쪽 극단에 있다. 그래서 선택자를 나눈다.

    flat   중앙값. 넓고 균일한 면.
    dark   어두운 쪽 8%의 중앙값. 글자·먹선.
    light  밝은 쪽 92%의 중앙값. 상아색 면.
    vivid  채도 상위 12%의 중앙값. 가문색처럼 좁고 선명한 것.
    vivid:lo-hi  위와 같되 색상환 lo~hi도(度) 안의 화소만. 금장을 로브와 구별할 때.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).parent))
import kfont

# (이름, 선택자, 설명, x0, y0, x1, y1) — 좌표는 0~1 정규화.
BATTLE = [
    ("bg.far",       "flat",  "원경 안개",             0.700, 0.030, 0.780, 0.090),
    ("bg.mid",       "flat",  "성 실루엣 중경",        0.300, 0.170, 0.345, 0.220),
    ("bg.ground",    "flat",  "판 바닥 · 다리 상판",   0.620, 0.600, 0.660, 0.640),
    ("panel.bg",     "flat",  "카드 바탕 아이보리",    0.028, 0.455, 0.048, 0.530),
    ("panel.bg2",    "flat",  "하단 버튼 바탕",        0.800, 0.850, 0.825, 0.890),
    ("panel.header", "flat",  "표 머리띠",             0.445, 0.447, 0.465, 0.468),
    ("panel.row",    "flat",  "표 행 바탕",            0.465, 0.500, 0.485, 0.520),
    ("text.ink",     "ink",   "표 글자 · 먹",          0.440, 0.460, 0.600, 0.740),
    ("gold.trim",    "vivid:25-55", "카드 금장 · 왕관",0.020, 0.360, 0.200, 0.580),
    ("gold.deep",    "vivid:20-45", "대포 · 갑옷 금속",  0.100, 0.630, 0.260, 0.780),
    ("dice.face",    "light", "주사위 면 상아색",      0.418, 0.800, 0.448, 0.845),
    ("accent.blue",  "vivid", "결과 보기 버튼",        0.845, 0.830, 0.935, 0.950),
    ("house.purple", "vivid", "세리스 가문 (전투화면)", 0.020, 0.360, 0.200, 0.450),
    ("house.blue",   "vivid", "리안 가문 (전투화면)",   0.860, 0.360, 0.990, 0.450),
]

# 판 시안은 어두운 톤이다. 여기서는 가문 4색의 색상만 가져오고 명도는 신뢰하지 않는다.
BOARD = [
    ("house.purple", "vivid", "말 받침대 · 좌상",   0.255, 0.178, 0.285, 0.208),
    ("house.blue",   "vivid", "말 받침대 · 우상",   0.715, 0.172, 0.752, 0.202),
    ("house.red",    "vivid", "말 받침대 · 우하",   0.697, 0.714, 0.734, 0.750),
    ("house.green",  "vivid", "말 받침대 · 좌하",   0.278, 0.723, 0.315, 0.756),
    ("tile.face",    "light", "판 칸 윗면",         0.315, 0.190, 0.360, 0.215),
    ("tile.edge",    "dark",  "판 칸 옆면 · 두께",   0.315, 0.215, 0.360, 0.232),
]

SETS = {"battle": BATTLE, "board": BOARD}
SWATCH_W, ROW_H, PAD = 150, 46, 12


LUMA = np.array([0.2126, 0.7152, 0.0722])


def _hue(px):
    mx, mn = px.max(axis=1), px.min(axis=1)
    c = np.maximum(mx - mn, 1e-6)
    r, g, b = px[:, 0], px[:, 1], px[:, 2]
    h = np.where(mx == r, ((g - b) / c) % 6, np.where(mx == g, (b - r) / c + 2, (r - g) / c + 4))
    return h * 60


def pick(patch, how):
    px = patch.reshape(-1, 3).astype(np.float64)
    if how == "flat":
        sel = px
    elif how in ("dark", "ink"):
        lum = px @ LUMA
        sel = px[lum <= np.percentile(lum, 8 if how == "dark" else 2)]
    elif how == "light":
        lum = px @ LUMA
        sel = px[lum >= np.percentile(lum, 92)]
    elif how.startswith("vivid"):
        mx, mn = px.max(axis=1), px.min(axis=1)
        sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
        keep = np.ones(len(px), bool)
        if ":" in how:
            lo, hi = (float(v) for v in how.split(":")[1].split("-"))
            h = _hue(px)
            keep = (h >= lo) & (h <= hi)
            if keep.sum() < 50:  # 그 색상이 거의 없으면 창을 풀고 알린다
                keep = np.ones(len(px), bool)
        cand = px[keep]
        s2 = sat[keep]
        sel = cand[s2 >= np.percentile(s2, 88)]
    else:
        raise ValueError(how)
    med = np.median(sel, axis=0).astype(int)
    return "#%02x%02x%02x" % tuple(med), tuple(int(v) for v in med), int(np.median(np.std(sel, axis=0)))


def main(which: str, src: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    W, H = im.size
    a = np.asarray(im)

    rows = []
    for name, how, desc, x0, y0, x1, y1 in SETS[which]:
        box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
        hexv, rgb, spread = pick(a[box[1]:box[3], box[0]:box[2]], how)
        rows.append(dict(name=name, how=how, desc=desc, hex=hexv, rgb=rgb, spread=spread, box=box))

    map_w = 900
    map_im = im.resize((map_w, int(H * map_w / W)))
    d = ImageDraw.Draw(map_im)
    sx, sy = map_w / W, map_im.height / H
    for i, r in enumerate(rows, 1):
        b = r["box"]
        d.rectangle([b[0] * sx, b[1] * sy, b[2] * sx, b[3] * sy], outline=(255, 0, 0), width=2)
        d.text((b[0] * sx + 3, b[1] * sy - 12), str(i), fill=(255, 0, 0))

    sheet_h = max(map_im.height, len(rows) * ROW_H) + PAD * 2
    sheet = Image.new("RGB", (map_w + SWATCH_W + 430 + PAD * 3, sheet_h), (30, 30, 34))
    sheet.paste(map_im, (PAD, PAD))
    ds = ImageDraw.Draw(sheet)
    f_name, f_desc = kfont.load(13), kfont.load(12)
    x = map_w + PAD * 2
    for i, r in enumerate(rows):
        y = PAD + i * ROW_H
        ds.rectangle([x, y, x + SWATCH_W, y + ROW_H - 6], fill=r["rgb"])
        sheet.paste(im.crop(r["box"]).resize((60, ROW_H - 6)), (x + SWATCH_W + 8, y))
        ds.text((x + SWATCH_W + 76, y + 6), f'{i+1}. {r["name"]}  {r["hex"]}  [{r["how"]}]', fill=(235, 235, 235), font=f_name)
        ds.text((x + SWATCH_W + 76, y + 22), r["desc"], fill=(150, 150, 156), font=f_desc)
    sheet.save(out / f"palette_check_{which}.png")

    (out / f"palette_{which}.json").write_text(
        json.dumps({r["name"]: r["hex"] for r in rows}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    for r in rows:
        print(f'{r["name"]:<14} {r["hex"]}  [{r["how"]:<5}] {r["desc"]}')
    print(f'→ {out}/palette_check_{which}.png')


if __name__ == "__main__":
    main(sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3]))
