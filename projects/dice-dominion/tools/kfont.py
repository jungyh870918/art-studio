"""검증 시트에 한글을 쓰기 위한 폰트 로더.

PIL 기본 비트맵 폰트에는 한글 글리프가 없어서 설명이 전부 두부(□)로 나온다.
사람이 읽으라고 만드는 시트이므로 이것이 깨지면 시트의 목적이 사라진다.
"""
from PIL import ImageFont

CANDIDATES = [
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
]


def load(size: int):
    for path in CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()
