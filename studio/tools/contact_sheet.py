#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""후보 대조 시트 — 여러 후보를 한 장에 모아 디렉터가 고르게 한다.

    python3 studio/tools/contact_sheet.py projects/<게임>/candidates/backgrounds
    python3 studio/tools/contact_sheet.py <폴더> --ref projects/<게임>/references/01_explore.png

이 도구는 **판정하지 않는다.** 점수도 순위도 매기지 않는다.
하는 일은 하나 — 나란히 놓아 눈으로 비교할 수 있게 만드는 것.
(`docs/02_DIRECTOR_RELATIONSHIP` · `docs/08_REVIEW_AND_APPROVAL` §8)

`--ref` 로 앵커를 주면 맨 왼쪽에 «기준»으로 붙여 준다. 후보를 기준과 같은 줄에
놓고 보는 것이 따로 보는 것보다 훨씬 정확하다.

의존성: Pillow.
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow 가 필요하다:  python3 -m pip install --user pillow")


# 한글이 두부(□)로 나오지 않게 시스템 폰트를 물린다.
# 게임 저장소의 폰트를 참조하지 않는다 — 스튜디오는 특정 게임에 의존하지 않는다.
_FONT_CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
]


def font(size: int):
    for path in _FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()

BG = (18, 20, 24)
PANEL = (28, 31, 37)
LINE = (58, 63, 72)
TEXT = (222, 226, 232)
DIM = (138, 146, 158)
REF = (232, 176, 84)

CELL_H = 560          # 후보 한 칸의 그림 높이
PAD = 20
LABEL_H = 40


def load(paths: list[pathlib.Path]) -> list[tuple[pathlib.Path, Image.Image]]:
    out = []
    for p in paths:
        try:
            out.append((p, Image.open(p).convert("RGB")))
        except Exception as e:            # noqa: BLE001 — 무엇이 실패했는지만 알리면 된다
            print(f"  ! 건너뜀 {p.name}: {e}")
    return out


def fit(im: Image.Image, h: int) -> Image.Image:
    w = max(1, round(im.width * h / im.height))
    return im.resize((w, h), Image.LANCZOS)


def build(items, ref=None, title="") -> Image.Image:
    tiles = []
    if ref is not None:
        tiles.append((ref[0], fit(ref[1], CELL_H), True))
    for p, im in items:
        tiles.append((p, fit(im, CELL_H), False))

    width = PAD + sum(t[1].width + PAD for t in tiles)
    height = PAD + 46 + CELL_H + LABEL_H + PAD
    sheet = Image.new("RGB", (width, height), BG)
    d = ImageDraw.Draw(sheet)

    f_title, f_name, f_small = font(17), font(14), font(12)
    d.text((PAD, PAD - 4), title, fill=TEXT, font=f_title)
    d.text((PAD, PAD + 19), f"후보 {len(items)}장 · 기준과 나란히 놓고 눈으로 고른다",
           fill=DIM, font=f_small)

    x = PAD
    y = PAD + 46
    for p, im, is_ref in tiles:
        accent = REF if is_ref else LINE
        d.rectangle([x - 3, y - 3, x + im.width + 2, y + CELL_H + 2], fill=PANEL, outline=accent)
        sheet.paste(im, (x, y))
        name = ("[기준] " if is_ref else "") + p.stem
        d.text((x, y + CELL_H + 9), name[:44], fill=REF if is_ref else TEXT, font=f_name)
        ow, oh = Image.open(p).size
        d.text((x, y + CELL_H + 26), f"원본 {ow}×{oh}", fill=DIM, font=f_small)
        x += im.width + PAD
    return sheet


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="후보가 든 폴더")
    ap.add_argument("--ref", default=None, help="기준으로 나란히 붙일 앵커 이미지")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    folder = pathlib.Path(a.folder)
    # `_` 로 시작하는 것은 이 도구가 만든 생성물이다 — 후보로 다시 집지 않는다
    paths = sorted(p for p in folder.glob("*.png")
                   if not p.name.startswith((".", "_")))
    if not paths:
        print(f"후보가 없다: {folder}")
        return 1

    items = load(paths)
    if not items:
        return 1
    ref = None
    if a.ref:
        r = load([pathlib.Path(a.ref)])
        ref = r[0] if r else None

    stamp = datetime.date.today().isoformat()
    sheet = build(items, ref, f"{folder.name}  ·  {stamp}")
    out = pathlib.Path(a.out) if a.out else folder / f"_contact_sheet_{stamp}.png"
    sheet.save(out)
    print(f"후보 {len(items)}장 → {out}")
    print(f"  {sheet.width}×{sheet.height}")
    print("\n이 시트는 판정하지 않는다. 고르는 것은 사람이다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
