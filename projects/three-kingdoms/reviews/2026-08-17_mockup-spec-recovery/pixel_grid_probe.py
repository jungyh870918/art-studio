"""픽셀 격자 검출기 — 「이 그림이 진짜 도트인가」를 판정한다.

원리
  픽셀 아트를 N배로 확대하면 인접 화소 차분 프로파일이 주기 N으로 반복되고,
  그 주기성은 자기상관 ac[N] 이 «이웃 lag 보다 솟아오르는 것»으로 나타난다.
  매끄러운 그림(회화·AI 생성물)은 ac 가 단조 감소할 뿐 솟아오르지 않는다.

  지표 = ac[N] − (ac[N−1] + ac[N+1]) / 2

판정 기준 (아래 대조군에서 얻은 값)
  진짜 격자  +1.2 이상
  회화        +0.05 이하

사용
  python3 pixel_grid_probe.py
  webp → png 변환이 필요하면 ImageMagick 을 쓴다 (자동으로 시도한다).

주의
  이 도구는 화풍을 판정하지 않는다. 격자의 유무만 본다.
  「좋은가」는 검사하지 않는다 — CAPABILITY_2D_ASSET_FACTORY.md §11.
"""
import numpy as np
from PIL import Image
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.abspath(os.path.join(HERE, "..", "..", "references"))
MK   = os.path.join(HERE, "_mk")          # 변환 캐시 (git 에 넣지 않는다)

THRESH_GRID = 0.5        # 이 위면 격자가 있다고 본다 (대조군 +1.2 / 회화 +0.04 사이)


# ── 준비 ────────────────────────────────────────────────────────────────
def ensure_pngs():
    os.makedirs(MK, exist_ok=True)
    for name in ("m1-map", "m2-city", "m3-officer", "m4-battle"):
        dst = os.path.join(MK, name + ".png")
        if os.path.exists(dst):
            continue
        src = os.path.join(REFS, "mockups", name + "-full.webp")
        if not os.path.exists(src):
            sys.exit(f"레퍼런스가 없다: {src}")
        subprocess.run(["magick", src, dst], check=True)


def load(path):
    return np.asarray(Image.open(path).convert("RGB")).astype(np.float64)


# ── 검출 ────────────────────────────────────────────────────────────────
def autocorr(crop, axis):
    g = np.abs(np.diff(crop, axis=axis)).mean(axis=2)
    prof = g.mean(axis=1 - axis)
    prof = prof - prof.mean()
    n = len(prof)
    ac = np.correlate(prof, prof, mode="full")[n - 1:]
    return ac / ac[0]


def excess(crop, axis, maxlag=13):
    """lag 별 «이웃 대비 솟아오른 정도»."""
    ac = autocorr(crop, axis)
    out = {}
    for N in range(2, min(maxlag, len(ac) - 1)):
        out[N] = round(float(ac[N] - (ac[N - 1] + ac[N + 1]) / 2), 3)
    return out


def probe(crop, label, verbose=False):
    h, v = excess(crop, 1), excess(crop, 0)
    bh = max(h.items(), key=lambda kv: kv[1])
    bv = max(v.items(), key=lambda kv: kv[1])
    hit = bh[1] > THRESH_GRID or bv[1] > THRESH_GRID
    # 두 축의 주기가 같아야 진짜 격자다
    agree = "" if not hit else ("  축 일치" if bh[0] == bv[0] else "  ※ 두 축의 주기가 다르다")
    print(f"  {label:<34} {'격자 있음' if hit else '격자 없음':<9} "
          f"가로 lag{bh[0]} {bh[1]:+.3f} · 세로 lag{bv[0]} {bv[1]:+.3f}{agree}")
    if verbose:
        print(f"      가로 {h}")
    return hit


# ── 실행 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    ensure_pngs()

    print("=== 대조군 1: 합성 도트 (정답을 아는 경우) ===")
    rng = np.random.default_rng(0)
    small = rng.integers(0, 255, (64, 64, 3)).astype(np.float64)
    for k in (3, 4, 5):
        probe(np.kron(small, np.ones((k, k, 1))), f"최근접 확대 ×{k}  (정답 {k})")

    print("\n=== 대조군 2: 현재 게임 화면 (내부 640×400 을 2배) ===")
    shots = os.path.join(REFS, "current-build")
    for f, box in (("03-main.png", (200, 900, 200, 700)),
                   ("09-battle-a.png", (200, 900, 200, 700))):
        p = os.path.join(shots, f)
        if os.path.exists(p):
            x0, x1, y0, y1 = box
            probe(load(p)[y0:y1, x0:x1], f)

    print("\n=== 대조군 3: 회화 (격자 없음이 정답) ===")
    m3 = load(os.path.join(MK, "m3-officer.png"))
    probe(m3[250:600, 150:500], "m3 관우 초상 — 회화")

    print("\n=== 검사 대상: 목업의 «도트처럼 보이는» 영역 ===")
    m1 = load(os.path.join(MK, "m1-map.png"))
    m2 = load(os.path.join(MK, "m2-city.png"))
    m4 = load(os.path.join(MK, "m4-battle.png"))
    probe(m1[900:1150, 120:420], "m1 산악 지형")
    probe(m1[250:500,  500:800], "m1 평야·삼림")
    probe(m1[400:480,  330:550], "m1 허창 성채")
    probe(m1[810:950,  300:540], "m1 성도 성채")
    probe(m4[150:380,  250:600], "m4 전투 지형")
    probe(m4[500:600,   60:160], "m4 부대 스프라이트")
    probe(m2[840:1040,  60:330], "m2 도시 전경")

    print(f"\n판정 기준: 지표 > {THRESH_GRID} 이면 격자 있음.")
    print("대조군에서 진짜 격자는 +1.2~+1.6, 회화는 +0.04 가 나온다.")
