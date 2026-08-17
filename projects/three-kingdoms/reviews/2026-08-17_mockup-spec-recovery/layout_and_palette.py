"""목업에서 «회수 가능한» 값만 측정한다 — 레이아웃 · 전투 격자 · 색.

픽셀 격자는 여기서 다루지 않는다. pixel_grid_probe.py 가 그것이 없음을 보였다.
비율과 색은 픽셀 정렬과 무관하므로 그대로 회수된다.

사용
  python3 layout_and_palette.py     (pixel_grid_probe.py 를 먼저 한 번 돌려 _mk 를 만든다)
"""
import numpy as np
from PIL import Image
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MK = os.path.join(HERE, "_mk")
if not os.path.isdir(MK):
    sys.exit("_mk 가 없다. pixel_grid_probe.py 를 먼저 실행한다.")

def load(n): return np.asarray(Image.open(os.path.join(MK, n + ".png")).convert("RGB")).astype(np.int16)
m1, m2, m3, m4 = load("m1-map"), load("m2-city"), load("m3-officer"), load("m4-battle")
H, W = m1.shape[:2]

print("=== 캔버스 ===")
print(f"  {W}×{H}   비율 {W/H:.4f}   9:16 = {9/16:.4f}   차이 {W - H*9/16:+.1f}px")

# ── UI 3단 구조 ─────────────────────────────────────────────────────────
print("\n=== 화면 3단 구조 (균일하고 어두운 가로 띠) ===")
def bands(img, name):
    rows = img.mean(axis=2)
    ui = (rows.std(axis=1) < 28) & (rows.mean(axis=1) < 60)
    runs, s = [], None
    for y, v in enumerate(ui):
        if v and s is None: s = y
        elif not v and s is not None:
            if y - s >= 6: runs.append((s, y))
            s = None
    if s is not None: runs.append((s, len(ui)))
    top = [r for r in runs if r[0] < 200]
    bot = [r for r in runs if r[1] > H - 200]
    print(f"  {name}  상단 {top[:2]}   하단 {bot[-2:] if bot else []}")
for img, n in ((m1, "m1"), (m2, "m2"), (m3, "m3"), (m4, "m4")): bands(img, n)
print(f"  → m1 기준: HUD 0–106 ({106/H:.1%}) · 콘텐츠 106–1527 ({1421/H:.1%}) · 탭바 1527–{H} ({145/H:.1%})")

# ── 전투 격자 ───────────────────────────────────────────────────────────
print("\n=== m4 전투 격자 ===")
sub = m4[380:1120, 30:700].mean(axis=2)
def lines(prof, off, label):
    th = prof.mean() * 1.6
    idx, merged = [i for i in range(1, len(prof)-1)
                   if prof[i] > th and prof[i] >= prof[i-1] and prof[i] > prof[i+1]], []
    for i in idx:
        if merged and i - merged[-1] < 8: continue
        merged.append(i)
    d = np.diff(merged)
    print(f"  {label} @ {[i+off for i in merged]}")
    print(f"    간격 {list(d)}")
lines(np.abs(np.diff(sub, axis=1)).mean(axis=0), 30,  "세로선")
lines(np.abs(np.diff(sub, axis=0)).mean(axis=1), 380, "가로선")
print("  → 세로 간격 107±2 로 안정. 아래로 갈수록 넓어지는 추세 없음 = 등각이 아니다.")
print("  → 셀 비율 107 : 102 ≈ 1.05 : 1  → 정사각에 가까운 top-down")

# ── 색 ─────────────────────────────────────────────────────────────────
print("\n=== 팔레트 ===")
def dom(img, box, label, n=4, satmin=0):
    x0, y0, x1, y1 = box
    c = img[y0:y1, x0:x1].reshape(-1, 3)
    if satmin:
        c = c[(c.max(1) - c.min(1)) > satmin]
    if not len(c): return print(f"  {label}: 없음")
    q = c // 24 * 24
    u, k = np.unique(q, axis=0, return_counts=True)
    o = np.argsort(-k)[:n]
    print(f"  {label:<24} {[('#%02x%02x%02x' % tuple(u[i]), f'{100*k[i]/len(c):.0f}%') for i in o]}")

print(" UI 바탕:")
dom(m1, (0, 0, W, 106),        "헤더")
dom(m1, (0, 1527, W, H),       "탭바")
dom(m2, (30, 720, 910, 1500),  "도시 패널")
dom(m3, (620, 420, 910, 720),  "능력치 패널")
def red_only(img, box, label, n=3):
    """붉은 배너가 바다·해안에 둘러싸인 경우 색상으로 걸러 낸다."""
    x0, y0, x1, y1 = box
    reg = img[y0:y1, x0:x1]
    r, g, b = reg[:, :, 0], reg[:, :, 1], reg[:, :, 2]
    c = reg[(r > g + 40) & (r > b + 40) & (r > 80)]
    if not len(c): return print(f"  {label}: 없음")
    q = c // 16 * 16
    u, k = np.unique(q, axis=0, return_counts=True)
    o = np.argsort(-k)[:n]
    print(f"  {label:<24} {[('#%02x%02x%02x' % tuple(u[i]), f'{100*k[i]/len(c):.0f}%') for i in o]}  (붉은 화소만)")

print(" 세력 배너 (채도 있는 화소만):")
dom(m1, (408, 332, 466, 404),  "조 曹", 3, 40)
red_only(m1, (700, 500, 795, 620), "손 孫")      # 해안이라 색상으로 걸러야 한다
dom(m1, (372, 748, 428, 822),  "유 劉", 3, 40)
dom(m1, (160, 660, 216, 732),  "마 馬", 3, 40)
dom(m1, (596, 966, 652, 1038), "원 袁", 3, 40)
print(" 금 강조:")
dom(m3, (30, 190, 120, 740),   "m3 족자", 6, 50)

# ── 요소 크기 비율 (논리 해상도 환산의 근거) ────────────────────────────
print("\n=== 요소 크기 — 화면 폭 대비 비율 ===")
for label, px in (("인물 마커", 78), ("전투 격자 셀", 107),
                  ("성채(중)", 240), ("무장 상세 초상", 610)):
    print(f"  {label:<16} {px}px = 폭의 {px/W:.1%}")
print("\n  논리 폭별 마커 크기 (8.3%):")
for lw in (270, 360, 470, 640, 720, 941):
    print(f"    {lw:>4} → {round(lw*78/W):>3}px")
