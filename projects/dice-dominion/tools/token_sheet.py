#!/usr/bin/env python3
"""측정·제안된 색을 의미 토큰 목록으로 묶어 디렉터가 볼 견본 시트를 만든다.

값이 바뀌면 TOKENS만 고쳐 다시 돌린다. 판단은 사람이 보고 한다.
"""
import colorsys
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).parent))
import kfont


def hex2rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def rgb2hex(r):
    return "#%02x%02x%02x" % tuple(int(round(v)) for v in r)


def to_tone(src_hex, L, S):
    """색상만 가져오고 명도·채도는 기준 톤에 맞춘다."""
    r, g, b = (v / 255 for v in hex2rgb(src_hex))
    h = colorsys.rgb_to_hls(r, g, b)[0]
    return rgb2hex([c * 255 for c in colorsys.hls_to_rgb(h, L, S)])


# 전투 화면에서 측정된 두 가문색이 아이보리 톤의 기준이 된다.
REF = ['#695794', '#416491']
_l = [colorsys.rgb_to_hls(*[v / 255 for v in hex2rgb(h)]) for h in REF]
TONE_L = sum(x[1] for x in _l) / 2
TONE_S = sum(x[2] for x in _l) / 2

TOKENS = [
    ('— 바탕과 원경 —', None, None),
    ('bg.far', '#b3becd', '원경 안개 · 가장 먼 층'),
    ('bg.mid', '#8b9eba', '중경 실루엣'),
    ('bg.ground', '#bbc1cd', '판 바닥 · 석재'),
    ('— 패널 —', None, None),
    ('panel.bg', '#e4ddd8', '카드 · 패널 바탕 (기본 아이보리)'),
    ('panel.bg2', '#e1dad2', '버튼 바탕 (반 톤 낮음)'),
    ('panel.row', '#dfd3c4', '표 행 바탕 (따뜻한 쪽)'),
    ('panel.header', '#675955', '표 머리띠 · 어두운 고동'),
    ('— 선과 글자 —', None, None),
    ('gold.line', '#d1c6b7', '가는 금선 (밝은 쪽 · 테두리)'),
    ('gold.metal', '#54402e', '금속 금장 (깊은 쪽 · 대포 · 갑옷)'),
    ('text.ink', '#44423d', '본문 먹'),
    ('surface.ivory', '#f0ece8', '가장 밝은 면 (주사위 · 하이라이트)'),
    ('— 강조 —', None, None),
    ('accent.blue', '#334981', '주 행동 버튼'),
    ('— 어두운 바탕 위의 글자 —', None, None),
    ('on.panel.header', '#ece3da', 'panel.header 위 · 실측'),
    ('on.accent.blue', '#edeae6', 'accent.blue 위 · 실측'),
    ('— 가문 4색 (2026-08-17 확정) —', None, None),
    ('house.purple', '#695794', '측정 · 전투 화면'),
    ('house.blue', '#416491', '측정 · 전투 화면'),
    ('house.red', to_tone('#370c06', TONE_L, TONE_S), '확정 · 판 시안 색상 + 전투 화면 톤'),
    ('house.green', to_tone('#16250b', TONE_L, TONE_S), '확정 · 판 시안 색상 + 전투 화면 톤'),
]

RH, W = 42, 780


def main(out: Path):
    img = Image.new('RGB', (W, RH * len(TOKENS) + 24), (244, 241, 237))
    d = ImageDraw.Draw(img)
    f_head, f_name, f_desc = kfont.load(13), kfont.load(14), kfont.load(12)
    y = 12
    for name, hx, desc in TOKENS:
        if hx is None:
            d.text((16, y + 14), name, fill=(120, 112, 104), font=f_head)
            y += RH
            continue
        d.rectangle([16, y, 116, y + RH - 8], fill=hex2rgb(hx), outline=(190, 183, 175))
        d.text((130, y + 5), name, fill=(40, 38, 34), font=f_name)
        d.text((250, y + 5), hx, fill=(40, 38, 34), font=f_name)
        d.text((130, y + 22), desc, fill=(130, 124, 116), font=f_desc)
        y += RH
    img.save(out / 'ivory_tokens.png')
    (out / 'tokens.json').write_text(
        json.dumps({n: h for n, h, _ in TOKENS if h}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'기준 톤 L={TONE_L:.3f} S={TONE_S:.3f}')
    for n, h, dsc in TOKENS:
        if h:
            print(f'{n:<14} {h}  {dsc}')
    print(f'→ {out}/ivory_tokens.png · tokens.json')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
