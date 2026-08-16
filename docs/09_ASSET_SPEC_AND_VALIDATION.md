# 09_ASSET_SPEC_AND_VALIDATION

## 1. 문서의 역할

이 문서는 Art Studio에서 사용하는 게임 아트 자산의 **측정 가능하고 검증 가능한 기술 규격과 검사 원칙**을 정의한다.

이 문서는 Art Direction을 수치표로 바꾸는 문서가 아니다.

이 문서는 좋은 아트인지 자동 판정하는 문서도 아니다.

이 문서는 특정 엔진의 import 설정 매뉴얼도 아니다.

이 문서는 개별 프로젝트의 모든 기술 값을 고정하는 문서가 아니다.

핵심 질문은 다음과 같다.

> **현재 자산이 프로젝트와 작업 단계에서 요구되는 기술 규격을 충족하는지 어떻게 확인할 것인가?**

이 문서의 목적은 다음 두 가지를 분리하는 것이다.

```text
공통적으로 재사용 가능한 검증 능력
≠
프로젝트마다 달라지는 실제 규격 값
```

예를 들어:

```text
"이미지 width를 검사하는 능력"
```

은 Studio 공통 기술일 수 있다.

반면:

```text
"이 프로젝트의 캐릭터 sprite width = 48px"
```

는 프로젝트별 규칙이다.

---

## 2. 가장 중요한 원칙

Art Studio는 검증 가능한 항목을 가능한 한 명확하게 만든다.

예:

- dimensions
- aspect ratio
- alpha
- padding
- pivot
- frame count
- tile size
- palette count
- texture dimensions
- naming
- format
- export compatibility

하지만 다음을 validator가 최종 판정하려 하지 않는다.

- 매력
- 분위기
- 캐릭터성
- 세계관 적합성
- 최종 화풍 선택
- 좋은 실루엣인지의 최종 판단
- 충분히 예쁜가
- 충분히 좋은가

따라서 다음 구분을 유지한다.

```text
VALIDATION
=
기술 규격 확인

ART REVIEW
=
미적·게임플레이·방향 적합성 판단
```

---

## 3. Style Specification과 Validation의 관계

향후 프로젝트별 `STYLE_SPEC.md`는 다음을 정의할 수 있다.

예:

```text
character sprite height: 64px
outline: 1px
palette target: <= 32 colors
tile size: 32×32
animation idle: 4 frames
filtering: nearest
```

이 문서는 그 값을 대신 결정하지 않는다.

이 문서는 다음을 정의한다.

> **그 값이 존재할 때 어떻게 검사할 것인가?**

관계는 다음과 같다.

```text
ART DIRECTION
↓
STYLE SPEC
↓
ASSET REQUIREMENT
↓
VALIDATION
```

Art Direction이 의도를 설명하고,
Style Spec이 반복 가능한 기술 규칙을 정의하며,
Validation은 실제 자산이 그 규칙을 만족하는지 확인한다.

---

## 4. 프로젝트별 값과 Studio 공통 능력을 분리한다

다음은 Studio 공통 validator 능력이 될 수 있다.

- image dimensions reader
- alpha detector
- color count analyzer
- palette extractor
- frame detector
- tile seam checker
- filename checker
- duplicate detector
- texture channel checker
- file format checker
- asset existence checker
- export presence checker

반면 다음은 프로젝트별 값이다.

- 캐릭터 height = 64px
- tile = 32×32
- palette <= 24 colors
- outline = 1px
- idle animation = 6 frames
- portrait aspect ratio = 3:4
- UI icon padding = 4px

Validator에 특정 게임의 값을 하드코딩하지 않는 것을 기본으로 한다.

---

## 5. 모든 프로젝트가 같은 규격을 가지지 않는다

Art Studio 전체에 다음과 같은 기본값을 만들지 않는다.

```text
모든 sprite = 64px
모든 tile = 32px
모든 palette = 32 colors
모든 outline = 1px
```

게임마다 요구가 다르다.

또한 같은 프로젝트 안에서도 자산 종류별로 다를 수 있다.

예:

```text
character sprite:
64×64

UI icon:
32×32

portrait:
512×768

environment texture:
1024×1024
```

따라서 Validation은 **규칙을 적용하는 능력**을 공통화하고,
규칙의 실제 값은 프로젝트에 남긴다.

---

## 6. 미정 값을 검사 규칙으로 만들지 않는다

프로젝트 초기에는 다음이 정상일 수 있다.

```text
outline: undecided
palette size: exploratory
character height: 48–64px testing
lighting: engine test required
```

이런 값을 억지로 하나의 숫자로 확정하지 않는다.

Validation은 확정된 규칙에 대해서만 강제할 수 있다.

탐색 중인 값은:

- warning
- informational
- comparison

정도로 사용할 수 있다.

---

## 7. 검사 결과의 기본 성격

필요하면 검사 결과를 다음과 같이 구분할 수 있다.

### PASS

현재 정의된 규격을 충족.

### WARNING

확인할 필요는 있지만 반드시 실패는 아님.

### FAIL

명확한 기술 요구를 충족하지 못함.

예:

```text
PASS
dimensions = 64×64

WARNING
palette = 34 colors
target = 32
difference small

FAIL
alpha channel missing
required = true
```

이 상태를 거대한 품질관리 시스템으로 만들 필요는 없다.

---

## 8. Warning과 Fail을 구분한다

모든 차이를 Fail로 만들지 않는다.

예:

```text
target palette <= 32

actual = 33
```

이것이 반드시 실패인지,
허용 가능한 예외인지,
측정 방식의 차이인지
프로젝트에 따라 다를 수 있다.

반면:

```text
required dimensions = 64×64
actual = 512×512
```

처럼 명백한 mismatch는 Fail일 수 있다.

검사 강도는 규칙의 중요도와 확정 정도에 따라 달라진다.

---

## 9. Dimensions

이미지와 sprite의 기본적인 dimensions를 검사할 수 있다.

예:

- width
- height
- exact dimensions
- min / max dimensions
- multiple-of constraint
- power-of-two requirement

예:

```text
required:
64×64

actual:
64×64

result:
PASS
```

또는:

```text
allowed:
48–64px height

actual:
56px

result:
PASS
```

Dimensions는 파일 크기와 혼동하지 않는다.

---

## 10. Aspect Ratio

다음과 같은 자산에서 중요할 수 있다.

- portrait
- card art
- UI panel
- banner
- loading image
- store image

검사 가능한 항목:

```text
width / height
```

예:

```text
required:
3:4

actual:
768×1024

result:
PASS
```

필요하면 허용 tolerance를 둘 수 있다.

---

## 11. Alpha

투명 배경이 필요한 자산에서는 alpha를 검사할 수 있다.

예:

- sprite
- icon
- VFX texture
- decal
- UI element

확인할 수 있는 것:

- alpha channel 존재
- 완전 불투명 여부
- 완전 투명 이미지 여부
- edge transparency
- unexpected semi-transparent pixels

하지만 alpha가 존재한다고 배경 제거가 미적으로 잘 되었다는 뜻은 아니다.

---

## 12. Transparent Edge

배경 제거 후 다음 문제가 생길 수 있다.

- white fringe
- dark halo
- color bleed
- semi-transparent edge artifact

코드로 일부 탐지할 수 있다.

하지만 최종 edge quality는 시각 확인이 필요할 수 있다.

따라서:

```text
technical detection
+
visual review
```

를 함께 사용할 수 있다.

---

## 13. Padding

일부 자산은 일정한 내부 여백이 필요할 수 있다.

예:

- icon
- UI asset
- sprite frame
- atlas item

검사 가능한 것:

- bounding box
- left / right / top / bottom padding
- minimum transparent border

예:

```text
minimum padding:
4px

actual:
left 5
right 4
top 6
bottom 5
```

하지만 모든 이미지에 padding 규칙을 강제하지 않는다.

---

## 14. Bounding Box

실제 불투명 픽셀 영역의 bounding box를 계산할 수 있다.

유용한 경우:

- sprite alignment
- icon consistency
- animation frame consistency
- automatic crop
- pivot inspection

예:

```text
canvas:
64×64

content bbox:
x 8–55
y 4–61
```

이 값 자체가 좋은 배치를 의미하지는 않는다.

---

## 15. Pivot

게임 엔진에서 sprite나 object의 pivot이 중요할 수 있다.

예:

- 발 위치
- 캐릭터 중심
- weapon rotation point
- UI anchor
- tile origin

검증 가능한 경우:

- metadata 존재
- pivot 값 범위
- frame 간 pivot consistency

실제 엔진에서의 적용은 `10_ENGINE_HANDOFF.md`에서 더 상세히 다룬다.

---

## 16. Palette Count

픽셀 아트나 제한 팔레트 프로젝트에서는 color count를 검사할 수 있다.

예:

```text
target:
<= 32 colors

actual:
27

PASS
```

하지만 color count는 주의해서 해석한다.

다음 때문에 실제 색 수가 증가할 수 있다.

- antialiasing
- alpha variation
- compression
- color profile
- unintended interpolation

필요하면 검사 전에 규칙을 정의한다.

예:

- alpha 제외
- 완전 투명 pixel 제외
- near-color quantization 여부
- RGB 기준인지 indexed palette 기준인지

---

## 17. Palette Membership

프로젝트가 실제 고정 palette를 사용한다면
각 pixel이 허용 palette 안에 있는지 검사할 수 있다.

예:

```text
allowed palette:
24 colors

unexpected colors:
3
```

하지만 프로젝트가 “낮은 채도” 같은 방향만 갖고 있다면
정확한 palette membership 검사를 강제하지 않는다.

Art Direction과 Style Spec을 구분한다.

---

## 18. Color Range

일부 프로젝트에서는 다음을 분석할 수 있다.

- saturation range
- value range
- hue distribution
- average luminance
- dominant colors

이 수치는 스타일 분석과 이상치 탐지에 유용할 수 있다.

하지만:

```text
average saturation = X
```

가 곧:

```text
좋은 스타일
```

을 의미하지 않는다.

이런 값은 주로 비교와 warning에 사용한다.

---

## 19. Outline

Outline을 일부 기술적으로 분석할 수 있다.

예:

- outline presence
- approximate thickness
- hard edge
- outline color
- external border pixels

하지만 복잡한 일러스트에서 outline 품질을 완전히 자동 판정하기 어렵다.

다음처럼 구분한다.

```text
기술 측정:
outline width 추정

Art Review:
outline이 형태와 분위기에 적합한가
```

---

## 20. Pixel Grid

픽셀 아트에서는 실제 pixel grid 정합성이 중요할 수 있다.

검사 가능한 문제:

- unintended antialiasing
- subpixel scaling result
- non-integer scaling
- blurred edge
- interpolation artifact

예:

```text
sprite source:
48×48

display scale:
3×

expected:
144×144 nearest

actual:
145×145 bilinear
```

이 경우 기술 문제로 판단할 수 있다.

---

## 21. Filtering

다음과 같은 filtering 설정이 프로젝트 아트에 영향을 줄 수 있다.

- nearest
- bilinear
- trilinear

특히 픽셀 아트에서는 잘못된 filtering이 스타일을 크게 손상시킬 수 있다.

Style Spec 또는 engine rule에 filtering 요구가 있다면 검사한다.

구체적인 엔진 설정은 Engine Handoff 문서로 넘긴다.

---

## 22. Compression

압축은 다음 문제를 만들 수 있다.

- color shift
- blocking
- edge artifact
- alpha degradation
- texture blur

검사 가능한 것:

- source vs export dimensions
- file format
- compression mode metadata
- file size anomaly

최종 시각 영향은 Runtime Review가 필요할 수 있다.

---

## 23. File Format

자산에 따라 요구 format이 다를 수 있다.

예:

- PNG
- WEBP
- TGA
- PSD
- SVG
- EXR
- FBX
- GLB
- WAV-like animation data
- engine-specific format

검증 가능한 것:

- extension
- actual MIME / magic
- color depth
- alpha support
- channel availability

파일 확장자만 보고 실제 format을 가정하지 않을 수 있다.

---

## 24. Color Mode

필요하면 다음을 검사한다.

- RGB
- RGBA
- grayscale
- indexed
- CMYK

게임 자산에 부적절한 color mode가 들어오는 것을 방지할 수 있다.

예:

```text
expected:
RGBA

actual:
CMYK

FAIL
```

---

## 25. Color Profile

일부 프로젝트에서는 color profile 차이 때문에
도구 간 색이 다르게 보일 수 있다.

검사 가능한 것:

- embedded profile
- sRGB 여부
- profile mismatch

모든 프로젝트에 color management 시스템을 강제하지 않는다.

색상 문제가 실제로 발생할 때 사용한다.

---

## 26. Animation Frame Count

Sprite animation에서는 frame count를 검사할 수 있다.

예:

```text
idle:
4 frames

walk:
8 frames

attack:
6 frames
```

실제 값은 Style Spec 또는 Asset Brief에서 가져온다.

Frame count가 맞아도 animation quality가 좋은 것은 아니다.

Timing, pose, anticipation은 Art Review의 영역일 수 있다.

---

## 27. Frame Dimensions

Sprite sheet에서는 frame size가 일정해야 할 수 있다.

예:

```text
sheet:
512×64

frame:
64×64

expected frames:
8
```

자동으로 검사할 수 있다.

---

## 28. Frame Alignment

Animation frame 사이에서 다음을 검사할 수 있다.

- canvas consistency
- baseline
- pivot
- bounding box drift
- unexpected movement

예:

캐릭터가 제자리 idle인데
frame마다 바닥 위치가 크게 흔들리면 warning을 줄 수 있다.

하지만 의도적인 movement인지 자동으로 단정하지 않는다.

---

## 29. Animation Timing

Animation FPS 또는 frame duration이 기술 규격에 포함될 수 있다.

예:

```text
walk:
8 fps

attack:
12 fps
```

Engine과 실제 gameplay에서 적용되는 timing은
runtime validation과 함께 확인할 수 있다.

---

## 30. Sprite Sheet Layout

검사 가능한 것:

- row / column count
- frame size
- spacing
- margin
- expected animation order
- missing frame

정확한 layout schema는 프로젝트 요구에 따라 달라질 수 있다.

---

## 31. Tile Size

Tile 기반 게임에서는 다음을 검사할 수 있다.

- exact tile dimensions
- grid multiple
- atlas alignment
- border pixels

예:

```text
tile:
32×32

actual:
31×32

FAIL
```

---

## 32. Tile Seam

Seamless tile은 자동 검사가 특히 유용하다.

검사 방법 예:

- left/right edge comparison
- top/bottom edge comparison
- repeated preview generation
- difference image

하지만 pixel-level edge match가 완벽해도
반복 패턴이 시각적으로 부자연스러울 수 있다.

따라서:

```text
technical seam check
+
repeated visual review
```

가 유용하다.

---

## 33. Tile Repetition

다음 문제는 seam과 다르다.

- 눈에 띄는 반복 무늬
- 큰 랜드마크 반복
- 방향성 texture 반복
- 동일 stain 반복

이 문제는 일부 통계 분석을 사용할 수 있지만
최종적으로는 Art Review가 필요할 수 있다.

---

## 34. Isometric Alignment

아이소메트릭 자산에서는 프로젝트가 정한 경우 다음을 검사할 수 있다.

- angle
- grid footprint
- tile occupancy
- base alignment
- anchor

하지만 모든 isometric 프로젝트가 동일한 각도를 사용한다고 가정하지 않는다.

---

## 35. Texture Dimensions

3D 또는 engine texture에서는 다음이 중요할 수 있다.

- width / height
- power of two
- maximum size
- channel layout
- compression suitability

예:

```text
max:
2048×2048

actual:
4096×4096

FAIL
```

실제 제한은 플랫폼과 엔진에 따라 달라진다.

---

## 36. Texture Channels

다음과 같은 texture를 검사할 수 있다.

- albedo
- normal
- roughness
- metallic
- AO
- emission
- mask

검사 가능한 것:

- 파일 존재
- dimensions consistency
- channel count
- naming
- expected grayscale / RGB
- paired texture missing

---

## 37. Normal Map

Normal map은 일반 컬러 이미지와 다른 특성을 가진다.

필요하면 다음을 검사할 수 있다.

- expected channel format
- dimensions
- suspicious color distribution
- naming
- paired texture

구체적인 engine import type은 Handoff 문서에서 다룬다.

---

## 38. Mask Texture

Packed mask를 사용하는 프로젝트에서는 channel 의미가 중요하다.

예:

```text
R = metallic
G = roughness
B = AO
A = emission mask
```

이런 규칙은 프로젝트 Style Spec 또는 engine art spec에 있어야 한다.

Validator는 그 규칙을 읽고 검사한다.

---

## 39. 3D Geometry 기본 검증

Art Studio가 3D asset을 다룬다면 다음을 검사할 수 있다.

- object 존재
- mesh count
- triangle count
- scale
- orientation
- transform
- UV presence
- material slot count
- missing texture
- naming

모든 3D 프로젝트에 동일한 poly budget을 강제하지 않는다.

---

## 40. Polygon / Triangle Count

플랫폼 또는 프로젝트에서 budget이 정의되어 있다면 검사할 수 있다.

예:

```text
target:
<= 20k triangles

actual:
18.2k

PASS
```

하지만 polygon 수가 낮다고 좋은 모델은 아니다.

---

## 41. Scale

3D asset의 실제 world scale은 중요할 수 있다.

예:

- character height
- prop dimension
- building footprint

파일 내부 unit과 engine import 결과가 다를 수 있으므로
Runtime / Engine Handoff와 연결해서 본다.

---

## 42. Orientation

다음 문제를 검사할 수 있다.

- forward axis
- up axis
- rotation
- mirrored asset
- wrong coordinate system

특히 Blender와 엔진 사이 전달에서 중요할 수 있다.

---

## 43. UV

필요하면 다음을 검사할 수 있다.

- UV 존재
- UV bounds
- overlap
- out-of-range UV
- expected texel density

하지만 UV의 미적 배치 품질 전체를 자동 판정하려 하지 않는다.

---

## 44. Naming

Naming rule이 정의되어 있다면 자동 검사가 유용하다.

예:

```text
CHR_HERO_IDLE_01.png
```

검사 가능한 것:

- regex
- prefix
- suffix
- forbidden character
- duplicate
- case
- extension

Naming 규칙 자체는 이 문서에서 강제하지 않는다.

프로젝트 또는 공통 규칙에서 정의된 경우 검사한다.

---

## 45. Asset ID

Asset Manifest가 안정적인 ID를 사용한다면
파일 또는 metadata와 연결할 수 있다.

예:

```text
Asset ID:
CHR_001
```

하지만 모든 작은 파일에 복잡한 ID 체계를 강제하지 않는다.

---

## 46. Missing Asset

Manifest 또는 Asset Brief를 기준으로
필요한 파일이 존재하는지 검사할 수 있다.

예:

```text
expected:
idle
walk
attack
hit

found:
idle
walk
attack

missing:
hit
```

대량 production에서 유용하다.

---

## 47. Duplicate Asset

다음 중복을 탐지할 수 있다.

- identical hash
- same filename
- near-identical image
- duplicate export

하지만 비슷한 이미지가 intentional variant일 수 있으므로
near-duplicate는 warning으로 다룰 수 있다.

---

## 48. File Integrity

기본적으로 다음을 확인할 수 있다.

- 파일 열림
- corrupted image
- zero byte
- unsupported format
- missing metadata

대량 batch 이후 유용하다.

---

## 49. Export Presence

Approved source가 있는데 필요한 export가 없는지 확인할 수 있다.

예:

```text
approved:
hero.png

required exports:
unity
web

found:
unity

missing:
web
```

이 정보는 Engine Handoff와 Asset Manifest에 연결할 수 있다.

---

## 50. Source와 Export 비교

Export 과정에서 source가 의도치 않게 변했는지 일부 검사할 수 있다.

예:

- aspect ratio
- dimensions
- alpha
- color profile
- unexpected crop
- file integrity

하지만 compression이나 lighting처럼
실제 화면 영향이 있는 부분은 Runtime Review가 필요할 수 있다.

---

## 51. Validation 단계는 작업 상태에 따라 달라진다

### Reference

대부분 validation 대상이 아니다.

필요하면 파일 integrity 정도만 본다.

### Concept

기술 규격보다 탐색 목적이 중요하다.

### Candidate

비교와 채택에 필요한 규격을 확인한다.

### Approved Source

공식 source로 보존할 수 있는지 확인한다.

### Export

engine/platform 규격을 더 엄격하게 확인한다.

단계가 진행될수록 검증 강도가 높아질 수 있다.

---

## 52. Concept에 최종 규격을 강제하지 않는다

예:

주인공 silhouette Concept이
최종 sprite size와 다르다고 해서 실패가 아니다.

Concept의 목적은:

- 형태
- 방향
- 비율
- 분위기

를 탐색하는 것일 수 있다.

현재 단계에 필요하지 않은 검사를 강제하지 않는다.

---

## 53. Candidate에 필요한 검사는 자산마다 다르다

예:

### Portrait Candidate

중요할 수 있는 것:

- aspect ratio
- crop
- face visibility

### Tile Candidate

중요할 수 있는 것:

- dimensions
- seam
- repeat

### VFX Candidate

중요할 수 있는 것:

- alpha
- frame
- blending test

### Character Sprite

중요할 수 있는 것:

- dimensions
- palette
- baseline
- frame consistency

모든 자산에 같은 validator set을 적용하지 않는다.

---

## 54. Required / Recommended / Informational

프로젝트가 복잡해지면 규칙의 강도를 개념적으로 구분할 수 있다.

### Required

위반 시 실제 사용이 어려움.

예:

- exact dimensions
- alpha required
- missing frame

### Recommended

현재 스타일이나 효율을 위한 목표.

예:

- palette target
- preferred texture size

### Informational

비교용 측정값.

예:

- average luminance
- edge density

이 구분을 모든 프로젝트에 schema로 강제하지 않는다.

---

## 55. Exact Rule과 Range Rule

규격은 exact일 수도 있고 range일 수도 있다.

예:

```text
exact:
tile = 32×32
```

```text
range:
portrait height = 512–1024px
```

```text
maximum:
texture <= 2048
```

```text
minimum:
padding >= 4px
```

Validator는 규칙의 성격을 구분해야 한다.

---

## 56. Tolerance

일부 규격에는 tolerance가 필요할 수 있다.

예:

```text
aspect ratio:
1.5 ± 0.01
```

또는:

```text
edge color difference:
<= threshold
```

Tolerance를 임의로 정하지 않는다.

프로젝트 요구 또는 검사 목적에 따라 정의한다.

---

## 57. 예외

Approved된 예외는 정상이다.

예:

```text
Project rule:
character height = 64px

Exception:
Boss A = 128px
```

Validator가 Boss A를 계속 Fail로 표시하면 시스템이 잘못된 것이다.

예외는:

- asset-specific
- category-specific
- platform-specific

일 수 있다.

---

## 58. 예외를 전체 규칙으로 확대하지 않는다

Boss A가 128px이라고 해서
모든 boss가 128px인 것은 아니다.

예외의 scope를 존중한다.

---

## 59. Validation 결과는 수정 위치를 알려줘야 한다

좋은 validator output은 단순히:

```text
FAIL
```

만 말하지 않는다.

가능하면:

```text
Asset:
hero_idle.png

Rule:
expected 64×64

Actual:
64×66

Issue:
height mismatch
```

처럼 수정 가능한 정보를 제공한다.

---

## 60. Error Message는 사람이 읽을 수 있어야 한다

예:

나쁜 예:

```text
E013
```

좋은 예:

```text
Frame size mismatch:
expected 64×64, found 64×66.
```

코드 내부 error ID를 사용할 수 있지만
사람이 의미를 이해할 수 있어야 한다.

---

## 61. 자동 수정과 자동 검사를 구분한다

Validator가 문제를 찾았다고
항상 자동 수정하는 것은 아니다.

예:

### 자동 수정에 적합할 수 있음

- 파일명 normalize
- format conversion
- resize
- metadata generation

### 자동 수정에 주의

- crop
- palette reduction
- outline change
- aggressive compression

미적 결과에 영향을 줄 수 있는 수정은
원본을 보존하고 결과를 확인한다.

---

## 62. 원본을 파괴하지 않는다

자동 처리 시 가능한 한 source를 보존한다.

예:

```text
approved/source.png
↓
processing
↓
exports/unity/source.png
```

잘못된 validator fix가 source를 영구 변경하지 않도록 한다.

---

## 63. Validation과 Processing을 분리할 수 있다

개념적으로:

```text
VALIDATE
↓
REPORT
↓
FIX
↓
REVALIDATE
```

가 명확할 수 있다.

하지만 단순한 batch에서는 검사와 수정이 한 번에 이루어질 수 있다.

목적에 맞게 사용한다.

---

## 64. Revalidation

기술 문제를 수정했다면 필요하면 다시 검사한다.

예:

```text
FAIL:
alpha missing

↓
fix

↓
PASS:
alpha present
```

단순 작업에서는 자동으로 처리할 수 있다.

---

## 65. Batch Validation

대량 자산에서는 batch validation이 특히 유용하다.

예:

```text
120 sprites
↓
dimensions
alpha
naming
frame
palette
↓
report
```

결과를 다음처럼 요약할 수 있다.

```text
PASS: 108
WARNING: 8
FAIL: 4
```

그리고 Fail만 우선 수정할 수 있다.

---

## 66. Batch 결과에서 이상치를 찾는다

예:

```text
117 assets:
24–32 colors

3 assets:
70+ colors
```

이 경우 세 자산을 warning 대상으로 볼 수 있다.

하지만 이것이 미적 실패라는 뜻은 아니다.

---

## 67. Baseline Asset 비교

성숙한 프로젝트에서는 대표 Approved asset을 기술적 baseline으로 사용할 수 있다.

예:

- dimensions
- color count range
- outline density
- padding
- texture size

하지만 baseline과 다르다는 이유만으로 자동 실패하지 않는다.

명시된 규칙이 우선이다.

---

## 68. Statistical Validation

대규모 프로젝트에서는 일부 통계값을 활용할 수 있다.

예:

- average palette count
- dimensions distribution
- file size distribution
- luminance distribution
- edge density
- triangle count distribution

이런 값은 anomaly detection에 유용하다.

하지만 Art Direction의 최종 의미를 숫자로 환원하지 않는다.

---

## 69. Visual Validation Sheet

일부 기술 문제는 이미지로 보는 것이 더 빠르다.

예:

- tile repeat sheet
- alpha checkerboard
- sprite contact sheet
- animation strip
- bounding box overlay
- pivot overlay

자동으로 이런 review material을 만들 수 있다.

이것은 Technical Review와 Art Review 사이를 연결하는 유용한 보조 수단이다.

---

## 70. Tile Repeat Preview

Tile 검사에서는 예를 들어:

```text
single tile
↓
5×5 repeat preview
```

를 자동 생성할 수 있다.

이렇게 하면 seam뿐 아니라 반복 패턴도 쉽게 볼 수 있다.

---

## 71. Sprite Contact Sheet

여러 방향 또는 animation frame을 한 번에 볼 수 있다.

예:

```text
front
back
left
right
```

또는:

```text
idle
walk
attack
hit
```

기술적 누락과 시각적 일관성을 함께 확인하기 쉽다.

---

## 72. Alpha Preview

투명 자산은 checkerboard 배경에서 자동 preview할 수 있다.

다음 문제를 찾기 쉽다.

- fringe
- halo
- missed background
- semi-transparent artifact

---

## 73. Scale Preview

게임 내 실제 표시 크기와 비슷한 preview를 만들 수 있다.

예:

```text
100%
50%
25%
```

작은 sprite나 icon의 readability를 확인하는 데 도움이 된다.

하지만 최종 판단은 실제 게임 화면이 더 강한 기준일 수 있다.

---

## 74. Engine Validation과의 경계

이 문서에서는 engine-specific 기술 요구를 다룰 수 있지만
실제 엔진 import 과정 전체를 정의하지 않는다.

예:

```text
Unity export:
PNG required
max 2048
alpha required
```

정도는 validation rule로 사용할 수 있다.

하지만:

- Texture Type
- Pixels Per Unit
- Import Preset
- Material setup
- Prefab
- scene placement

등은 `10_ENGINE_HANDOFF.md`에서 상세히 다룬다.

---

## 75. Runtime Validation과의 경계

Validator가 파일을 PASS했다고
실제 게임 화면에서도 성공한다는 뜻은 아니다.

예:

```text
sprite:
64×64 PASS
alpha PASS
palette PASS
```

하지만 runtime에서:

- 너무 작음
- 배경에 묻힘
- lighting으로 색 변화
- VFX에 가려짐

문제가 있을 수 있다.

따라서:

```text
FILE VALIDATION
≠
RUNTIME VALIDATION
```

---

## 76. Platform Constraint

플랫폼마다 규격이 다를 수 있다.

예:

- Roblox texture limit
- mobile memory budget
- Web texture format
- console requirements
- engine atlas rule

이 값은 현재 프로젝트의 실제 platform requirement에서 가져온다.

Studio 공통 기본값으로 만들지 않는다.

---

## 77. Multi-platform Project

하나의 Approved source에서 여러 platform export가 나올 수 있다.

예:

```text
approved/source
├─ pc export
├─ mobile export
└─ web export
```

각 export에 다른 validation rule이 적용될 수 있다.

예:

```text
PC:
2048 texture

Mobile:
1024 texture

Web:
WEBP
```

Source와 platform export 규격을 구분한다.

---

## 78. Tool Version과 Validation

도구 업데이트로 output이 바뀔 수 있다.

예:

- image encoder
- compression tool
- generator
- exporter

중요한 production pipeline이라면
필요에 따라 tool version을 기록할 수 있다.

모든 단순 작업에 version metadata를 강제하지 않는다.

---

## 79. Deterministic Validation

기술 검사는 가능한 한 같은 입력에 같은 결과가 나오는 것이 좋다.

예:

```text
dimensions
alpha
palette count
hash
```

이런 검사는 deterministic하게 만들 수 있다.

반면 비전 모델 기반 분석은
완전히 동일한 의미의 validator로 취급하지 않을 수 있다.

---

## 80. Vision-based Validation

비전 모델은 다음과 같은 문제를 찾는 데 도움을 줄 수 있다.

- 누락된 무기
- 잘못된 방향
- 이상한 손
- reference와 큰 mismatch
- sprite family inconsistency
- tile에 명백한 오브젝트 반복

하지만 이런 결과는 보통:

```text
analysis
warning
review suggestion
```

으로 다루는 편이 적절하다.

객관적 deterministic validator처럼 취급하지 않는다.

---

## 81. Human Review가 필요한 Validation

다음은 기술적 요소가 있어도 사람이 직접 보는 것이 좋을 수 있다.

- alpha edge quality
- tile visual repetition
- sprite baseline perception
- texture compression artifact
- animation smoothness
- visual aliasing
- actual small-screen readability

자동화와 사람 검토를 조합한다.

---

## 82. Validator는 Art Direction을 읽을 수 있지만 대체하지 않는다

일부 validation은 Art Direction과 연결될 수 있다.

예:

```text
Art Direction:
배경은 캐릭터보다 낮은 contrast

Analyzer:
현재 scene에서 background contrast가 unusually high
```

이것은 useful warning일 수 있다.

하지만 analyzer가:

```text
Art Direction FAIL
```

이라고 최종 판정하는 시스템을 기본으로 하지 않는다.

---

## 83. Style Drift 탐지

대규모 반복 제작에서는 일부 기술 지표로 drift를 찾을 수 있다.

예:

- palette count 증가
- outline thickness 변화
- sprite height 변화
- detail density 증가
- texture resolution 증가

이상치를 찾고 Review 대상으로 올릴 수 있다.

최종 drift 판단은 프로젝트 문맥과 Art Review를 포함한다.

---

## 84. Validation Rule의 출처를 알 수 있어야 한다

가능하면 중요한 규칙은 어디에서 왔는지 이해할 수 있어야 한다.

예:

```text
Rule:
character height = 64px

Source:
STYLE_SPEC.md
```

또는:

```text
Rule:
PNG alpha required

Source:
Unity export requirement
```

이렇게 하면 임의 규칙이 시스템 표준처럼 굳는 것을 막을 수 있다.

---

## 85. 임시 Rule과 공식 Rule을 구분한다

실험 중 다음을 사용할 수 있다.

```text
test target:
palette <= 24
```

하지만 디렉터가 확정하지 않았다면
프로젝트 공식 Style Spec으로 자동 승격하지 않는다.

Validator가 실험 값을 영구 규칙으로 만들지 않는다.

---

## 86. Validation Rule 변경

프로젝트가 발전하면 기술 규격도 바뀔 수 있다.

예:

```text
old:
character = 48px

new:
character = 64px
```

이 경우 기존 자산을 모두 자동 Fail로 처리하기 전에
변경 범위와 migration 필요성을 확인한다.

---

## 87. Legacy Asset

기존 게임 버전의 asset은 현재 규격과 다를 수 있다.

예:

```text
legacy sprite:
48px

new production:
64px
```

Legacy를 계속 지원하는지,
변환할지,
교체할지는 프로젝트 판단이다.

Validator는 상황을 알려줄 수 있다.

---

## 88. Validation Report의 크기

작은 작업에서 수십 줄 report를 만들 필요는 없다.

예:

```text
PASS
64×64 / alpha / PNG
```

정도로 충분할 수 있다.

대량 작업에서는 상세 report가 유용할 수 있다.

---

## 89. Validation 실패가 작업을 항상 중단시키는 것은 아니다

Concept 또는 temporary runtime test에서는
일부 Fail을 알고도 진행할 수 있다.

예:

```text
temporary candidate:
dimensions mismatch

purpose:
lighting comparison only
```

현재 목적에 영향을 주지 않는다면
임시로 허용할 수 있다.

반면 final export에서 critical fail은 막아야 할 수 있다.

---

## 90. Critical Rule

필요하면 일부 규칙은 critical로 다룰 수 있다.

예:

- corrupted file
- required alpha missing
- wrong frame dimensions
- engine unsupported format
- missing required texture

이 경우 export 또는 handoff를 중단할 수 있다.

모든 warning을 critical로 만들지 않는다.

---

## 91. Validation이 디자인을 지배하지 않게 한다

다음과 같은 상황을 피한다.

```text
validator가 32 colors만 지원하므로
디자인을 32 colors로 만든다.
```

만약 프로젝트가 48 colors가 더 적합하다면
validator를 수정해야 한다.

> **검사 도구가 아트 방향을 결정하지 않는다.**

---

## 92. 자동화하기 어려운 규칙

일부 규칙은 명확하지만 자동화하기 어려울 수 있다.

예:

- 얼굴이 충분히 읽혀야 함
- 무기가 실루엣에서 구분되어야 함
- 배경 detail이 캐릭터를 방해하면 안 됨

이런 규칙을 억지로 숫자로 만들지 않는다.

Review 항목으로 남길 수 있다.

---

## 93. 자동화 가능한 규칙

반대로 다음은 적극 자동화할 가치가 높다.

- dimensions
- alpha
- naming
- file format
- frame count
- missing file
- texture size
- color count
- tile edge
- duplicate
- manifest completeness

기계가 잘하는 것은 기계에게 맡긴다.

---

## 94. Validator 구현 위치

공통 validator는 필요에 따라 `studio/tools/` 같은 공통 영역에 둘 수 있다.

예:

```text
studio/tools/
├─ image-dimensions
├─ alpha-check
├─ palette-analyzer
└─ tile-seam-check
```

하지만 이 문서는 실제 폴더를 강제하지 않는다.

구체적인 구현은 프로젝트 필요에 따라 추가한다.

---

## 95. Project-specific Configuration

공통 validator가 프로젝트별 값을 읽을 수 있는 구조를 사용할 수 있다.

개념적으로:

```text
common validator
+
project rules
=
project validation
```

예:

```text
palette-analyzer
+
game-a:
max colors = 24
```

다만 모든 것을 복잡한 YAML schema로 만들 필요는 없다.

Markdown, 간단한 config, script argument 등
현재 규모에 맞는 방법을 사용할 수 있다.

---

## 96. Config를 위한 Config를 만들지 않는다

작은 프로젝트에서 규칙 세 개 때문에
거대한 schema system을 만들지 않는다.

예:

```text
STYLE_SPEC.md
- sprite = 64×64
- palette <= 32
- alpha required
```

정도면 충분할 수 있다.

필요가 커지면 자동화용 structured config를 파생할 수 있다.

---

## 97. Markdown과 Machine-readable Data의 관계

사람이 읽는 Style Spec이 원본 기준일 수 있다.

필요하면 기술 자동화를 위해 일부 값을 machine-readable form으로
추출하거나 별도 config에 둘 수 있다.

하지만 machine-readable config가
디렉터의 Art Direction을 대체하지 않는다.

---

## 98. Validator가 모르는 값

검사에 필요한 값이 없으면
임의로 기본값을 넣지 않는다.

예:

```text
tile size:
unknown
```

이면:

```text
cannot validate tile size
```

라고 말하는 편이 낫다.

---

## 99. Validation과 Asset Manifest

향후 `ASSET_MANIFEST.md`는 다음과 연결될 수 있다.

예:

```text
Asset:
CHR_001

Status:
Candidate

Validation:
warning
```

또는:

```text
Export:
Unity ready
```

하지만 Manifest는 validator report 전체를 담는 문서가 아니다.

필요한 상태만 요약한다.

---

## 100. Validation과 Review Log

중요한 기술 문제로 방향이 바뀐 경우
Review Log에 남길 가치가 있을 수 있다.

예:

```text
기존 48px sprite는 모바일에서 지나치게 작게 보임.
64px 방향으로 변경.
```

단순한 alpha fix 같은 문제는
Review Log에 남길 필요가 없다.

---

## 101. Validation과 Generation Workflow

`07_GENERATION_WORKFLOW.md`에서는
작업 단계에 맞는 기술 검사를 수행한다.

이 문서는 그 검사의 원칙과 대상이 무엇인지 정의한다.

개념적으로:

```text
Generate
↓
Validate
↓
Fix
↓
Review
```

또는:

```text
Generate
↓
Review
↓
Validate before Approval
```

작업에 따라 순서는 달라질 수 있다.

---

## 102. Validation과 Review & Approval

`08_REVIEW_AND_APPROVAL.md`에서 Technical Review는
이 문서의 Validation 결과를 사용할 수 있다.

예:

```text
Technical Review:
PASS
- dimensions
- alpha

WARNING
- palette

Art Review:
실루엣은 좋지만
배경과의 대비가 부족함
```

둘을 한 화면에서 보여줄 수 있지만 의미는 분리한다.

---

## 103. Validation과 Engine Handoff

`10_ENGINE_HANDOFF.md`에서는
Approved source를 실제 엔진으로 전달한다.

이 과정에서:

- export format
- dimensions
- texture limit
- channel
- import compatibility

등을 검사할 수 있다.

Engine-specific validation은
Handoff 과정과 밀접하게 연결될 수 있다.

---

## 104. Validation과 Learning & Reuse

여러 프로젝트에서 반복적으로 유용한 validator는
Studio 공통 도구로 승격할 수 있다.

예:

- alpha checker
- tile seam checker
- sprite sheet validator

반면 특정 게임의 규격 값은
프로젝트 내부에 남긴다.

이 구분이 중요하다.

---

## 105. 공통화할 가치가 있는 Validator

다음 조건을 만족하면 공통화할 수 있다.

- 여러 프로젝트에서 반복됨
- 특정 스타일에 종속되지 않음
- 입력/출력이 명확함
- 기술 문제를 안정적으로 탐지함
- 유지 비용보다 반복 절감 효과가 큼

처음 한 번 썼다고 바로 Studio 공통 도구로 만들지 않는다.

---

## 106. 특정 프로젝트에 남겨야 하는 Validator

다음처럼 프로젝트 특화 규칙이 강한 경우
프로젝트 내부에 남을 수 있다.

예:

- 특정 palette membership
- 특수 atlas layout
- 독특한 sprite naming
- 프로젝트 고유 mask packing
- 특정 boss texture constraint

범용성이 확인되면 이후 공통화할 수 있다.

---

## 107. 검증 결과의 재현 가능성

가능하면 다음을 기록할 수 있다.

- validator version
- rule source
- input file
- result
- timestamp

하지만 소규모 프로젝트에서는
이런 metadata가 과도할 수 있다.

필요한 수준만 사용한다.

---

## 108. Validation Cache

대량 작업에서는 변경되지 않은 파일을
매번 다시 검사하지 않도록 hash 또는 timestamp를 사용할 수 있다.

이런 최적화는 필요할 때 구현한다.

초기 시스템의 필수 요소는 아니다.

---

## 109. Continuous Validation

프로젝트가 커지면 다음 시점에 자동 검사를 붙일 수 있다.

예:

- export 전
- commit 전
- batch generation 후
- engine handoff 전

하지만 CI 시스템을 Art Studio의 필수 구조로 만들지 않는다.

---

## 110. Validation Failure 처리

일반적인 흐름:

```text
FAIL
↓
문제 확인
↓
source / processing / export 중 원인 판단
↓
수정
↓
revalidate
```

미적 재작업이 필요한지,
단순 technical fix인지 구분한다.

---

## 111. Source 문제와 Export 문제

예:

```text
alpha missing
```

Source에 alpha가 없는 것인지,
export 과정에서 alpha가 제거된 것인지 구분한다.

수정 위치를 잘못 선택하면
같은 문제가 반복될 수 있다.

---

## 112. Tool-induced Artifact

처리 도구가 문제를 만들 수 있다.

예:

- resize blur
- quantization artifact
- compression halo
- normal map inversion
- alpha premultiply issue

Validator와 Runtime Review에서
processing stage 문제도 고려한다.

---

## 113. 검사 기준이 서로 충돌할 수 있다

예:

```text
palette <= 16
```

와:

```text
soft transparency required
```

가 특정 방식에서 충돌할 수 있다.

이런 경우 기계적으로 둘 다 강제하기보다
프로젝트의 실제 요구를 다시 확인한다.

---

## 114. Style과 Platform Constraint가 충돌할 수 있다

예:

```text
Art Direction:
고해상도 texture detail

Mobile constraint:
texture memory 부족
```

이 문제는 validator가 해결할 수 없다.

Trade-off를 정리하고
디렉터 또는 프로젝트 결정이 필요하다.

---

## 115. Validation은 문제를 드러내는 역할을 한다

Validator가 모든 문제의 해결책까지 자동 결정할 필요는 없다.

예:

```text
Texture exceeds mobile budget.
```

까지 알려주고,
해결 방법은:

- resize
- compression
- split texture
- asset redesign

중 판단할 수 있다.

---

## 116. Validation 결과를 숨기지 않는다

자동화가 파일을 자동 수정했다면
중요한 변화는 알 수 있어야 한다.

예:

```text
hero.png
resized:
1024 → 512
```

미적 영향 가능성이 있다면 Review를 요청할 수 있다.

---

## 117. Silent Fix를 주의한다

다음처럼 시각 결과를 바꿀 수 있는 작업을
아무 기록 없이 적용하지 않는다.

- palette reduction
- aggressive compression
- crop
- outline modification
- automatic cleanup

원본을 보존하고 결과를 확인한다.

---

## 118. Validator의 실패도 고려한다

도구 자체가 잘못된 결과를 낼 수 있다.

예:

- palette analyzer bug
- alpha detection 오류
- false seam detection
- wrong frame parsing

검사 결과가 실제 파일과 모순되면
validator를 절대적인 권위로 취급하지 않는다.

---

## 119. Manual Override

명확한 이유가 있다면
validator warning 또는 fail을 예외로 승인할 수 있다.

예:

```text
Boss texture exceeds normal limit.

Reason:
대표 컷신에서만 사용,
성능 테스트 완료.

Approved exception.
```

이런 예외는 중요한 경우 기록한다.

---

## 120. Validation Debt

프로토타입에서는 일부 기술 규칙이 미완성일 수 있다.

예:

- naming 불통일
- temporary texture size
- placeholder format

이런 문제를 모두 즉시 해결하지 않을 수 있다.

하지만 production으로 넘어갈 때
정리해야 할 technical debt로 인식할 수 있다.

복잡한 issue tracking 시스템을 이 문서에서 만들지는 않는다.

---

## 121. Production Gate

대규모 프로젝트에서는
일부 validation을 production gate로 사용할 수 있다.

예:

```text
Approved Source
↓
Critical Validation Pass
↓
Export
```

하지만 모든 프로젝트에 gate system을 강제하지 않는다.

---

## 122. Validation Checklist를 자산별로 최소화한다

예:

### Pixel Character

- dimensions
- alpha
- palette
- frame
- baseline

### Tile

- dimensions
- seam
- repeat

### Portrait

- dimensions
- aspect
- format

### Texture

- dimensions
- channels
- format

필요한 항목만 사용한다.

---

## 123. 자산 종류보다 실제 요구를 우선한다

같은 “character”라도:

- 2D sprite
- painted portrait
- 3D model
- Roblox texture

는 검사 대상이 완전히 다르다.

자산 category 이름만으로 validator를 고정하지 않는다.

---

## 124. 기술 규격은 게임 화면을 위해 존재한다

예:

```text
sprite = 64×64
```

이라는 규칙이 존재하는 이유는
단순히 숫자를 맞추기 위해서가 아닐 수 있다.

- 화면 표시 크기
- 픽셀 밀도
- animation
- memory
- atlas
- camera

와 연결될 수 있다.

숫자 자체가 목적이 아니다.

---

## 125. 실제 게임 화면에서 규격이 실패할 수 있다

예:

기술적으로:

```text
64×64 PASS
```

하지만 게임에서:

```text
너무 작아서 얼굴이 안 보임
```

이라면 규격 자체를 재검토할 수 있다.

Validation은 규칙을 지키게 하지만,
규칙이 잘못되었다면 규칙을 바꿀 수 있어야 한다.

---

## 126. 검증 자동화의 우선순위

자동화 가치가 높은 순서는 대체로 다음과 같이 생각할 수 있다.

### 높은 가치

- 반복 빈도 높음
- 오류가 명확함
- 사람이 보기 귀찮음
- 결과가 deterministic

예:

- dimensions
- naming
- alpha
- file existence

### 중간 가치

- 일부 heuristic 필요

예:

- seam
- palette anomaly
- edge artifact

### 낮은 자동화 적합성

- 미적 해석이 핵심

예:

- 캐릭터 매력
- world fit
- visual hierarchy

이것을 절대적인 우선순위로 만들지는 않는다.

---

## 127. 검증 시스템을 먼저 만들지 않는다

실제 문제가 존재하기 전에
거대한 validator framework부터 구축하지 않는다.

작업을 하면서 반복되는 기술 오류를 발견하고
그때 필요한 검사를 추가한다.

> **Validation도 실제 반복에서 성장한다.**

---

## 128. 단순 작업은 단순하게 검사한다

작은 UI icon 하나라면:

```text
64×64
PNG
alpha
```

확인만으로 충분할 수 있다.

거대한 report나 config를 만들지 않는다.

---

## 129. 중요한 Batch는 깊게 검사할 수 있다

예:

```text
300 sprite frames
```

에는:

- dimensions
- alpha
- frame completeness
- naming
- baseline
- palette
- duplicate

를 자동 검사하는 것이 가치가 클 수 있다.

---

## 130. 검사 결과를 디렉터에게 모두 보여줄 필요는 없다

Claude가 technical issue를 처리할 수 있다면
디렉터에게는 다음 정도만 전달할 수 있다.

```text
기술 검사 완료.
2개 frame의 alpha 문제를 수정했다.
Art Review에는 영향 없음.
```

하지만 미적 영향이 있는 수정은 보여줘야 할 수 있다.

---

## 131. 디렉터가 알아야 하는 Validation 문제

다음은 디렉터 판단에 영향을 줄 수 있다.

- 규격 때문에 디자인을 바꿔야 함
- platform limit로 품질 감소
- palette target과 현재 방향 충돌
- compression으로 시각 손실
- runtime scale 문제
- 여러 해결 방법이 서로 다른 미적 결과를 만듦

이 경우 기술 문제를 단순히 뒤에서 처리하지 않는다.

---

## 132. Validation의 최종 목적

Validation의 목적은 자산 제작에 장벽을 추가하는 것이 아니다.

다음 문제를 줄이는 것이다.

- 잘못된 크기
- 누락 파일
- 잘못된 포맷
- 반복되는 export 실수
- 잘못된 alpha
- tile seam
- animation 누락
- 엔진 전달 실패
- batch 작업 오류

이런 기계적인 문제를 줄여
사람이 시각적 판단에 더 집중할 수 있게 한다.

---

## 133. 다른 문서와의 관계

### `04_ART_DIRECTION_SYSTEM.md`

스타일의 시각적 축과 Art Direction / Style Spec의 차이를 정의한다.

이 문서는 그중 측정 가능한 기술 규칙을 검사한다.

---

### `06_ASSET_LIFECYCLE.md`

검증 결과가 Candidate, Approved, Export 상태와 어떤 관계를 갖는지 연결된다.

Technical Fail은 곧 미적 Rejected를 의미하지 않는다.

---

### `07_GENERATION_WORKFLOW.md`

제작 과정 중 언제 어느 정도의 검사를 수행할지 결정한다.

---

### `08_REVIEW_AND_APPROVAL.md`

Validation은 Technical Review의 주요 입력이다.

Art Review와 의미를 구분한다.

---

### `10_ENGINE_HANDOFF.md`

Engine-specific export와 runtime 단계에서 추가 검증이 이루어질 수 있다.

---

### `11_LEARNING_AND_REUSE.md`

범용 validator는 Studio 공통 능력으로 축적할 수 있다.

프로젝트별 규격 값은 스타일과 함께 프로젝트에 남긴다.

---

### `STYLE_SPEC.md`

실제 프로젝트의 기술 규격 값을 기록한다.

이 문서는 그 값을 검사하는 원칙을 제공한다.

---

### `ASSET_MANIFEST.md`

Validation 상태나 export readiness를 필요에 따라 요약할 수 있다.

---

## 134. 이 문서에서 다루지 않는 것

다음은 다른 문서의 역할이다.

### 특정 프로젝트의 실제 규격 값

`STYLE_SPEC.md`

### 최종 미적 승인

`08_REVIEW_AND_APPROVAL.md`

### 자산 상태 정의

`06_ASSET_LIFECYCLE.md`

### 실제 생성 루틴

`07_GENERATION_WORKFLOW.md`

### Unity / Godot / Roblox의 상세 import 설정

`10_ENGINE_HANDOFF.md` 또는 engine-specific guide

### Validator script의 실제 코드 구현

`studio/tools/`의 개별 도구

### 프로젝트별 naming convention

필요한 프로젝트 문서 또는 별도 규칙

이 문서는 **기술 규격과 검증의 상위 원칙**에 집중한다.

---

## 135. 핵심 원칙 요약

Art Studio의 Asset Specification & Validation은
아트를 숫자로 평가하는 시스템이 아니다.

핵심 원칙은 다음과 같다.

> **Art Direction과 Style Specification을 구분한다.**

> **Style Spec에서 내려온 측정 가능한 규칙을 Validation에서 확인한다.**

> **공통화하는 것은 검사 능력이고, 프로젝트별 실제 규격 값은 각 프로젝트에 남긴다.**

> **미정 값을 억지로 공식 규칙으로 만들지 않는다.**

> **Technical Pass와 Art Approval을 동일시하지 않는다.**

> **Concept, Candidate, Approved, Export는 필요한 검증 강도가 다를 수 있다.**

> **Dimensions, alpha, format, frame, tile seam, naming처럼 기계가 잘하는 검사는 적극 자동화한다.**

> **매력, 분위기, 세계관 적합성 같은 미적 판단을 validator가 대신하지 않는다.**

> **예외와 프로젝트별 차이를 허용한다.**

> **검사 도구에 맞추기 위해 디자인을 바꾸지 않는다. 규칙이 잘못되었다면 규칙이나 validator를 수정한다.**

> **자동 수정은 원본을 보존하고 미적 영향 가능성을 고려한다.**

> **파일 validation과 runtime validation을 구분한다.**

> **Validation은 작업을 복잡하게 만드는 절차가 아니라 반복적인 기술 실수를 줄여 디렉터가 아트 판단에 집중하도록 돕는 제작 기반이다.**
