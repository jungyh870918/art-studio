#!/usr/bin/env python3
"""받은 부품에서 크로마 배경을 지우고 조립기가 쓸 수 있는 형태로 만든다.

    python3 prep_parts.py <받은그림폴더> <출력폴더>

생성 AI는 부품을 캔버스 한가운데에 띄워 놓고 나머지를 초록으로 채운다.
그 여백을 그대로 두면 조립기가 여백까지 포함해 규격에 맞추므로, 장식이 제 크기의
몇 분의 일로 쪼그라든다. 그래서 배경을 지운 다음 내용물 경계로 잘라낸다.

가운데 바탕(center)은 배경도 지우지 않고 잘라내지도 않는다 — 그것은 면 전체가 내용이다.

그리고 잘라낸 다음 **목표 칸의 비율로 여백을 채운다.** 조립기는 부품을 칸 크기로 늘려 맞추므로,
부품의 비율이 칸과 다르면 장식이 그만큼 찌그러진다. 늘리는 대신 투명 여백을 붙여 비율을 맞춘다.

    corner   96×96      → 1:1    바깥 모서리에 붙이므로 좌상단 기준
    edge-h   마디 하나   → 1:1    띠는 테두리 한가운데에 놓이므로 상하 균등

띠를 테두리 전체 길이(320:96)에 맞추면 안 된다. 조립기는 부품의 «비율»로 마디 수를 정하므로
(`markCount`), 10:3으로 맞추면 마디가 하나로 떨어져 띠 하나가 변 전체로 늘어난다.
정사각으로 두어야 두께에 맞는 정사각 마디가 3개 들어간다.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def detect_key(a: np.ndarray) -> np.ndarray:
    """테두리 화소의 중앙값을 배경색으로 본다."""
    edges = np.concatenate([
        a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3),
        a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3),
    ])
    return np.median(edges, axis=0)


def cutout(im: Image.Image, inner: float = 55.0, outer: float = 135.0) -> Image.Image:
    a = np.asarray(im.convert("RGB")).astype(np.float64)
    key = detect_key(a)
    dist = np.sqrt(((a - key) ** 2).sum(-1))
    t = np.clip((dist - inner) / max(outer - inner, 1e-6), 0, 1)
    alpha = t * t * (3 - 2 * t)  # smoothstep

    # 반투명 가장자리에서 배경색을 빼낸다 (언프리멀티플라이).
    safe = np.maximum(alpha, 1e-3)[..., None]
    rgb = np.clip((a - (1 - safe) * key) / safe, 0, 255)

    # despill — 남은 초록 기운을 이웃 채널 수준으로 눌러 준다.
    dom = int(np.argmax(key))
    others = [c for c in range(3) if c != dom]
    cap = rgb[..., others].max(-1)
    over = rgb[..., dom] > cap
    rgb[..., dom] = np.where(over, cap, rgb[..., dom])

    out = np.dstack([rgb, alpha * 255]).astype(np.uint8)
    return Image.fromarray(out)


def trim(im: Image.Image, threshold: int = 12) -> Image.Image:
    a = np.asarray(im)[..., 3]
    ys, xs = np.where(a > threshold)
    if len(xs) == 0:
        return im
    return im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def pad_to_ratio(im: Image.Image, ratio: float, anchor: str) -> Image.Image:
    """투명 여백을 붙여 가로/세로 비를 ratio로 맞춘다. 늘리지 않는다."""
    w, h = im.size
    tw, th = (w, round(w / ratio)) if w / h > ratio else (round(h * ratio), h)
    canvas = Image.new("RGBA", (max(tw, w), max(th, h)), (0, 0, 0, 0))
    x = 0 if anchor == "topleft" else (canvas.width - w) // 2
    y = 0 if anchor == "topleft" else (canvas.height - h) // 2
    canvas.paste(im, (x, y))
    return canvas


# 부품별 목표 비율과 기준점. panel 규격(512×512 · 여백 96)에서 나온 값이다.
CELL = {
    "corner": (96 / 96, "topleft"),
    "edge-h": (1.0, "center"),
}


def main(src: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    for role in ("corner", "edge-h", "center"):
        p = src / f"{role}.png"
        if not p.exists():
            print(f"  {role}: 없음")
            continue
        im = Image.open(p)
        before = im.size
        if role == "center":
            result = im.convert("RGBA")  # 초록 배경이 없다. 건드리지 않는다
        else:
            ratio, anchor = CELL[role]
            result = pad_to_ratio(trim(cutout(im)), ratio, anchor)
        result.save(out / f"panel.{role}.png")
        opaque = (np.asarray(result)[..., 3] > 200).mean()
        print(f"  {role:<7} {before[0]}×{before[1]} → {result.width}×{result.height}  "
              f"불투명 {opaque:.0%}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
