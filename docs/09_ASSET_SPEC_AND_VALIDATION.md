# 09_ASSET_SPEC_AND_VALIDATION

## 1. 문서의 역할

이 문서는 게임 아트 자산의 **측정 가능하고 검증 가능한 기술 규격과 검사 원칙**을 정의한다.

이 문서는 Art Direction을 수치표로 바꾸는 문서가 아니다. 좋은 아트인지 자동 판정하는 문서도 아니다. 특정 엔진의 import 설정 매뉴얼도, 개별 프로젝트의 기술 값을 고정하는 문서도 아니다.

핵심 질문은 하나다.

> **현재 자산이 프로젝트와 작업 단계에서 요구되는 기술 규격을 충족하는지 어떻게 확인할 것인가?**

그리고 이 문서의 목적은 다음 두 가지를 분리하는 것이다.

```text
공통적으로 재사용 가능한 검증 능력
≠
프로젝트마다 달라지는 실제 규격 값
```

"이미지 width를 검사하는 능력"은 Studio 공통 기술일 수 있다.
"이 프로젝트의 캐릭터 sprite width = 48px"는 프로젝트별 규칙이다.

---

## 2. 가장 중요한 원칙

Art Studio는 검증 가능한 항목을 가능한 한 명확하게 만든다.

**Validator가 판정할 수 있는 것 — 기계에게 맡긴다**

> dimensions · aspect ratio · alpha · padding · bounding box · pivot · palette count · palette membership · color mode · color profile · outline 두께 추정 · pixel grid · frame count · frame dimensions · frame alignment · sprite sheet layout · tile size · tile seam · texture dimensions · texture channel · 3D scale/orientation/UV/triangle count · file format · file integrity · naming · 누락 파일 · 중복 · export 존재 여부 · source와 export의 기술적 차이

**Validator가 최종 판정하려 하지 않는 것 — Art Review의 영역이다**

> 매력 · 분위기 · 캐릭터성 · 세계관 적합성 · 최종 화풍 선택 · 좋은 실루엣인지의 판단 · 충분히 예쁜가 · 충분히 좋은가

따라서 다음 구분을 유지한다.

```text
VALIDATION
=
기술 규격 확인

ART REVIEW
=
미적·게임플레이·방향 적합성 판단
```

이 구분에서 파생되는 결론이 두 개 있고, 둘 다 이 문서 전체에 걸쳐 유지된다.

> **Technical Pass는 Director Approval이 아니다.**
> 검사를 통과했다는 사실이 좋은 아트라는 뜻이 아니다.

> **Validation Failure는 Director Rejection이 아니다.**
> 기술 검사에 실패했다는 사실이 그 디자인 방향을 버려야 한다는 뜻이 아니다.
> 대부분의 technical fail은 같은 디자인을 유지한 채 수정할 수 있다.

---

## 3. Art Direction → Style Spec → Validation

```text
ART DIRECTION      의도 · 인상 · 금지사항
↓
STYLE SPEC         반복 가능한 기술 규칙
↓
ASSET REQUIREMENT  이번 자산의 요구
↓
VALIDATION         실제 자산이 그 규칙을 만족하는가
```

프로젝트별 `STYLE_SPEC.md`가 값을 정의한다.

```text
character sprite height: 64px
outline: 1px
palette target: <= 32 colors
tile size: 32×32
animation idle: 4 frames
filtering: nearest
```

이 문서는 그 값을 대신 결정하지 않는다. **그 값이 존재할 때 어떻게 검사할 것인가**를 정의한다.

---

## 4. 공통 검사 능력과 프로젝트별 값을 분리한다

Studio 공통 능력이 될 수 있는 것.

> image dimensions reader · alpha detector · color count analyzer · palette extractor · frame detector · tile seam checker · filename checker · duplicate detector · texture channel checker · file format checker · asset existence checker · export presence checker

프로젝트에 남는 값.

> 캐릭터 height 64px · tile 32×32 · palette <= 24 · outline 1px · idle 6 frames · portrait 3:4 · UI icon padding 4px

**Validator에 특정 게임의 값을 하드코딩하지 않는다.**

그리고 Art Studio 전체의 기본값(모든 sprite = 64px, 모든 tile = 32px 같은 것)을 만들지 않는다. 게임마다 요구가 다르고, 같은 프로젝트 안에서도 자산 종류별로 다르다.

```text
character sprite     64×64
UI icon              32×32
portrait             512×768
environment texture  1024×1024
```

---

## 5. 미정 값을 FAIL 조건으로 만들지 않는다

프로젝트 초기에는 다음이 정상 상태다.

```text
outline: undecided
palette size: exploratory
character height: 48–64px testing
lighting: engine test required
```

이런 값을 억지로 하나의 숫자로 확정하지 않는다.

> **Validation은 확정된 규칙에 대해서만 강제할 수 있다.**

탐색 중인 값은 warning · informational · comparison 정도로만 사용한다.
실험 중의 임시 목표값(`test target: palette <= 24`)도 마찬가지다. 디렉터가 확정하지 않았다면 프로젝트 공식 Style Spec으로 자동 승격하지 않는다. **Validator가 실험 값을 영구 규칙으로 만들지 않는다.**

---

## 6. 검사 결과의 등급

### PASS / WARNING / FAIL

```text
PASS
dimensions = 64×64

WARNING
palette = 34 colors / target = 32 / difference small

FAIL
alpha channel missing / required = true
```

모든 차이를 Fail로 만들지 않는다. `target <= 32`에 `actual 33`이 실패인지, 허용 예외인지, 측정 방식의 차이인지는 프로젝트에 따라 다르다. 반면 `required 64×64`에 `actual 512×512`처럼 명백한 mismatch는 Fail이다.
**검사 강도는 규칙의 중요도와 확정 정도에 따라 달라진다.**

### 규칙의 강도

프로젝트가 복잡해지면 규칙 자체의 성격을 구분할 수 있다.

```text
Required        위반 시 실제 사용이 어려움      exact dimensions · alpha required · missing frame
Recommended     현재 스타일이나 효율의 목표      palette target · preferred texture size
Informational   비교용 측정값                  average luminance · edge density
```

일부는 critical로 다뤄 export나 handoff를 중단시킬 수 있다.

> corrupted file · required alpha missing · wrong frame dimensions · engine unsupported format · missing required texture

다만 이 구분을 모든 프로젝트에 schema로 강제하지 않고, 모든 warning을 critical로 만들지도 않는다.

---

## 7. 규칙의 형태

```text
exact     tile = 32×32
range     portrait height = 512–1024px
maximum   texture <= 2048
minimum   padding >= 4px
```

Validator는 규칙의 성격을 구분해야 한다.

일부 규격에는 tolerance가 필요하다(`aspect ratio 1.5 ± 0.01`, `edge color difference <= threshold`).
**Tolerance를 임의로 정하지 않는다.** 프로젝트 요구 또는 검사 목적에서 가져온다.

---

## 8. 검사 항목 — 이미지 기본

**Dimensions** — width · height · exact · min/max · multiple-of · power-of-two. 파일 크기와 혼동하지 않는다.

**Aspect ratio** — portrait · card art · UI panel · banner · loading image · store image에서 중요할 수 있다. 필요하면 tolerance를 둔다.

**Alpha** — alpha channel 존재 · 완전 불투명 여부 · 완전 투명 이미지 · edge transparency · 예상치 못한 반투명 픽셀.
alpha가 존재한다는 것이 배경 제거가 미적으로 잘 되었다는 뜻은 아니다.

**Transparent edge** — 배경 제거 후의 white fringe · dark halo · color bleed · 반투명 edge artifact. 코드로 일부 탐지할 수 있지만 최종 edge quality는 시각 확인이 필요하다.

**Padding** — bounding box 기준의 상하좌우 여백 · 최소 투명 테두리. icon · UI asset · sprite frame · atlas item에서 쓴다. 모든 이미지에 padding 규칙을 강제하지 않는다.

**Bounding box** — 실제 불투명 픽셀 영역. sprite alignment · icon consistency · frame consistency · 자동 crop · pivot 점검에 쓴다. 이 값 자체가 좋은 배치를 의미하지는 않는다.

**Pivot** — metadata 존재 · 값 범위 · frame 간 consistency. 발 위치 · 캐릭터 중심 · weapon rotation point · UI anchor · tile origin 등이 대상이다. 엔진에서의 실제 적용은 `10_ENGINE_HANDOFF.md`가 다룬다.

---

## 9. 검사 항목 — 색

**Palette count** — 제한 팔레트 프로젝트에서 유효하다. 다만 antialiasing · alpha variation · compression · color profile · 의도치 않은 interpolation 때문에 실제 색 수가 늘어날 수 있으므로, 검사 전에 기준을 정한다.

```text
alpha 제외 여부 · 완전 투명 pixel 제외 여부 ·
near-color quantization 여부 · RGB 기준인지 indexed palette 기준인지
```

**Palette membership** — 프로젝트가 실제 고정 palette를 쓴다면 각 pixel이 허용 palette 안에 있는지 검사한다. 프로젝트가 "낮은 채도" 같은 방향만 가지고 있다면 membership 검사를 강제하지 않는다. Art Direction과 Style Spec을 구분한다.

**Color range** — saturation range · value range · hue distribution · average luminance · dominant colors. 이 수치는 비교와 이상치 탐지용이다. `average saturation = X`가 좋은 스타일을 뜻하지 않는다.

**Color mode** — RGB · RGBA · grayscale · indexed · CMYK. 게임 자산에 부적절한 mode가 들어오는 것을 막는다(`expected RGBA / actual CMYK → FAIL`).

**Color profile** — embedded profile · sRGB 여부 · profile mismatch. 모든 프로젝트에 color management를 강제하지 않고, 도구 간 색 차이가 실제로 발생할 때 사용한다.

---

## 10. 검사 항목 — 픽셀과 엣지

**Outline** — presence · 대략적 두께 · hard edge · outline color · 외곽 border pixel. 복잡한 일러스트에서 outline 품질 전체를 자동 판정하기는 어렵다.

```text
기술 측정:  outline width 추정
Art Review: outline이 형태와 분위기에 적합한가
```

**Pixel grid** — 의도치 않은 antialiasing · subpixel scaling · 비정수 배율 · 흐려진 edge · interpolation artifact.

```text
sprite source 48×48 · display scale 3×
expected  144×144 nearest
actual    145×145 bilinear    → 기술 문제
```

**Filtering** — nearest / bilinear / trilinear. 픽셀 아트에서 잘못된 filtering은 스타일 자체를 손상시킨다. Style Spec이나 engine rule에 요구가 있으면 검사하고, 엔진 설정 자체는 `10_ENGINE_HANDOFF.md`가 다룬다.

**Compression** — color shift · blocking · edge artifact · alpha degradation · texture blur를 만들 수 있다. 검사할 수 있는 것은 source와 export의 dimensions 비교 · file format · compression mode metadata · file size 이상치이며, 최종 시각 영향은 runtime 확인이 필요하다.

---

## 11. 검사 항목 — 애니메이션과 시퀀스

**Frame count** — 실제 값은 Style Spec 또는 Asset Brief에서 가져온다(`idle 4 · walk 8 · attack 6`). frame 수가 맞아도 animation quality가 좋은 것은 아니다. timing · pose · anticipation은 Art Review의 영역이다.

**Frame dimensions** — sprite sheet에서 frame size가 일정한지 자동으로 검사한다.

```text
sheet 512×64 · frame 64×64 → expected frames 8
```

**Frame alignment** — canvas consistency · baseline · pivot · bounding box drift · 예상치 못한 이동. 제자리 idle인데 frame마다 바닥 위치가 흔들리면 warning을 줄 수 있다. 다만 **의도적인 movement인지 자동으로 단정하지 않는다.**

**Animation timing** — FPS 또는 frame duration이 기술 규격에 포함될 수 있다. 엔진과 실제 gameplay에서 적용되는 timing은 runtime 확인과 함께 본다.

**Sprite sheet layout** — row/column count · frame size · spacing · margin · 예상 animation 순서 · 누락 frame. 정확한 layout 규칙은 프로젝트마다 다르다.

---

## 12. 검사 항목 — 타일과 아이소메트릭

**Tile size** — exact dimensions · grid multiple · atlas alignment · border pixel (`tile 32×32 / actual 31×32 → FAIL`).

**Tile seam** — 좌우 edge 비교 · 상하 edge 비교 · 반복 preview 생성 · difference image. 자동 검사의 가치가 특히 높은 영역이다.

**Tile repetition** — seam과 다른 문제다. 눈에 띄는 반복 무늬 · 큰 랜드마크 반복 · 방향성 texture 반복 · 동일 stain 반복. 일부 통계 분석이 가능하지만 최종 판단은 Art Review가 한다.

```text
technical seam check
+
repeated visual review
```

pixel-level edge match가 완벽해도 반복 패턴이 시각적으로 부자연스러울 수 있다.

**Isometric alignment** — 프로젝트가 각도와 grid를 정한 경우 angle · grid footprint · tile occupancy · base alignment · anchor를 검사한다. 모든 isometric 프로젝트가 같은 각도를 쓴다고 가정하지 않는다.

---

## 13. 검사 항목 — 텍스처와 3D

**Texture dimensions** — width/height · power of two · maximum size · channel layout · compression 적합성. 실제 제한은 플랫폼과 엔진에서 온다(`max 2048 / actual 4096 → FAIL`).

**Texture channels** — albedo · normal · roughness · metallic · AO · emission · mask에 대해 파일 존재 · dimensions consistency · channel count · naming · grayscale/RGB 기대값 · 짝 texture 누락을 검사한다.

**Normal map** — expected channel format · dimensions · 이상한 색 분포 · naming · 짝 texture. engine import type은 `10_ENGINE_HANDOFF.md`가 다룬다.

**Mask texture** — packed mask를 쓰는 프로젝트에서는 channel의 의미가 규격이다.

```text
R = metallic · G = roughness · B = AO · A = emission mask
```

이 규칙은 프로젝트 Style Spec 또는 engine art spec에 있어야 하고, validator는 그 규칙을 읽어 검사한다.

**3D geometry** — object 존재 · mesh count · triangle count · scale · orientation · transform · UV presence · material slot count · 누락 texture · naming.

- **Triangle count** — budget이 정의되어 있을 때만 검사한다. polygon 수가 낮다고 좋은 모델은 아니다.
- **Scale** — character height · prop dimension · building footprint. 파일 내부 unit과 engine import 결과가 다를 수 있으므로 Engine Handoff와 연결해서 본다.
- **Orientation** — forward axis · up axis · rotation · mirrored asset · 잘못된 좌표계. Blender와 엔진 사이 전달에서 특히 중요하다.
- **UV** — UV 존재 · bounds · overlap · out-of-range · 기대 texel density. UV 배치의 품질 전체를 자동 판정하려 하지 않는다.

모든 3D 프로젝트에 동일한 poly budget을 강제하지 않는다.

---

## 14. 검사 항목 — 파일과 세트

**File format** — PNG · WEBP · TGA · PSD · SVG · EXR · FBX · GLB · engine-specific format 등 자산에 따라 요구가 다르다. extension · 실제 MIME/magic · color depth · alpha 지원 · channel 가용성을 확인한다. **파일 확장자만 보고 실제 format을 가정하지 않는다.**

**File integrity** — 파일 열림 · corrupted image · zero byte · 미지원 format · metadata 누락. 대량 batch 이후 특히 유용하다.

**Naming** — regex · prefix · suffix · 금지 문자 · 중복 · case · extension.

```text
CHR_HERO_IDLE_01.png
```

naming 규칙 자체는 이 문서가 강제하지 않는다. 프로젝트나 공통 규칙에 정의되어 있을 때 검사한다.

**Asset ID** — Manifest가 안정적인 ID를 쓴다면 파일이나 metadata와 연결할 수 있다. 모든 작은 파일에 복잡한 ID 체계를 강제하지 않는다.

**Missing asset** — Manifest나 Asset Brief를 기준으로 필요한 파일이 존재하는지 검사한다.

```text
expected: idle · walk · attack · hit
found:    idle · walk · attack
missing:  hit
```

**Duplicate** — identical hash · 동일 파일명 · near-identical image · 중복 export. 비슷한 이미지가 의도된 variant일 수 있으므로 near-duplicate는 warning으로 다룬다.

---

## 15. 검사 항목 — Export

**Export presence** — Approved source가 있는데 필요한 export가 없는 상태를 찾는다.

```text
approved: hero.png
required: unity · web
found:    unity
missing:  web
```

**Source와 Export 비교** — export 과정에서 source가 의도치 않게 변했는지 검사한다. aspect ratio · dimensions · alpha · color profile · 예상치 못한 crop · file integrity가 대상이다. compression이나 lighting처럼 실제 화면 영향이 있는 부분은 runtime 확인이 필요하다.

**Platform constraint** — Roblox texture limit · mobile memory budget · Web texture format · console requirement · engine atlas rule. 이 값은 현재 프로젝트의 실제 platform requirement에서 가져오며, **Studio 공통 기본값으로 만들지 않는다.**

**Multi-platform** — 하나의 Approved source에서 여러 platform export가 나오고, 각 export에 다른 규칙이 적용될 수 있다(`PC 2048 · Mobile 1024 · Web WEBP`).

> **Approved source의 규격과 platform export의 규격은 별개다.**

---

## 16. 검증 강도는 단계에 따라 달라진다

```text
REFERENCE        대부분 validation 대상이 아니다. 필요하면 file integrity 정도.
CONCEPT          기술 규격보다 탐색 목적이 우선한다.
CANDIDATE        비교와 채택 판단에 필요한 규격을 확인한다.
APPROVED SOURCE  공식 source로 보존할 수 있는 상태인지 확인한다.
EXPORT           engine/platform 규격을 가장 엄격하게 확인한다.
```

주인공 silhouette Concept이 최종 sprite size와 다르다는 것은 실패가 아니다. Concept의 목적이 형태·방향·비율·분위기 탐색이라면 그 판단에 필요하지 않은 검사를 강제하지 않는다.

> **현재 단계의 목적에 맞는 수준의 검증을 한다.**

Validation 실패가 항상 작업을 중단시키는 것도 아니다. 조명 비교만을 위한 임시 candidate라면 dimensions mismatch를 알고도 진행할 수 있다. 반면 final export의 critical fail은 막아야 한다.

---

## 17. 자산마다 필요한 검사가 다르다

같은 원칙이 자산 종류별로 다르게 적용된다.

```text
pixel character   dimensions · alpha · palette · frame · baseline
tile              dimensions · seam · repeat
portrait          dimensions · aspect · crop · format
VFX               alpha · frame · blending
texture           dimensions · channels · format
```

**모든 자산에 같은 validator set을 적용하지 않는다.**

그리고 자산 category 이름만으로 validator를 고정하지 않는다. 같은 "character"라도 2D sprite · painted portrait · 3D model · Roblox texture는 검사 대상이 완전히 다르다. **category보다 실제 요구를 본다.**

검사의 양도 작업 규모를 따른다. 작은 UI icon 하나는 `64×64 / PNG / alpha` 확인이면 충분하고, 거대한 report나 config를 만들지 않는다. 반대로 300 frame batch에서는 dimensions · alpha · frame completeness · naming · baseline · palette · duplicate를 자동 검사하는 가치가 크다.

---

## 18. 예외

승인된 예외는 정상이다.

```text
Project rule:  character height = 64px
Exception:     Boss A = 128px
```

**Validator가 Boss A를 계속 Fail로 표시하면 시스템 쪽이 잘못된 것이다.**

예외는 asset-specific · category-specific · platform-specific일 수 있고, 각각의 scope를 존중한다. Boss A가 128px이라고 해서 모든 boss가 128px인 것은 아니다.

명확한 이유가 있으면 warning이나 fail을 예외로 승인할 수 있다.

```text
Boss texture exceeds normal limit.
Reason: 대표 컷신에서만 사용 · 성능 테스트 완료.
Approved exception.
```

중요한 예외는 기록한다.

**Legacy asset**도 같은 성격의 문제다. 기존 버전의 48px sprite가 현재 64px 규격과 다르다고 해서 자동으로 실패 처리하지 않는다. 계속 지원할지, 변환할지, 교체할지는 프로젝트의 판단이고 validator는 상황을 알려주는 쪽이다.

**규칙 자체가 바뀔 때**도 마찬가지다. 기존 자산을 모두 자동 Fail로 만들기 전에 변경 범위와 migration 필요성을 먼저 확인한다.

---

## 19. Validation 결과의 형태

좋은 결과는 `FAIL`만 말하지 않고 **수정 위치**를 알려준다.

```text
Asset:  hero_idle.png
Rule:   expected 64×64
Actual: 64×66
Issue:  height mismatch
```

Error message는 사람이 읽을 수 있어야 한다. 내부 error ID(`E013`)를 쓰더라도 의미가 함께 드러나야 한다.

Report의 크기는 작업 규모를 따른다. 작은 작업은 `PASS — 64×64 / alpha / PNG` 정도로 충분하고, 대량 작업에서는 상세 report가 유용하다.

```text
PASS: 108   WARNING: 8   FAIL: 4
```

---

## 20. 자동 수정과 원본 보존

Validator가 문제를 찾았다고 항상 자동 수정하는 것은 아니다.

```text
자동 수정에 적합       파일명 normalize · format conversion · resize · metadata 생성
자동 수정에 주의       crop · palette reduction · outline 변경 · aggressive compression
```

미적 결과에 영향을 줄 수 있는 수정은 **원본을 보존하고 결과를 확인한다.**

```text
approved/source.png  →  processing  →  exports/unity/source.png
```

잘못된 validator fix가 approved source를 영구 변경하지 않도록 한다.

그리고 **silent fix를 하지 않는다.** 시각 결과를 바꿀 수 있는 처리를 아무 기록 없이 적용하지 않고, 자동 수정이 일어났다면 중요한 변화는 드러나야 한다.

```text
hero.png resized: 1024 → 512
```

미적 영향 가능성이 있으면 Review를 요청한다.

개념적 흐름은 `VALIDATE → REPORT → FIX → REVALIDATE`이지만, 단순한 batch에서는 검사와 수정이 한 번에 이루어질 수 있다. 기술 문제를 고쳤다면 필요한 만큼 다시 검사한다.

---

## 21. Batch와 이상치

대량 자산에서는 batch validation의 가치가 가장 크다. 120개 sprite의 dimensions · alpha · naming · frame · palette를 한 번에 검사하고 Fail부터 처리할 수 있다.

Batch 결과는 이상치를 드러낸다.

```text
117 assets:  24–32 colors
3 assets:    70+ colors
```

세 자산을 warning 대상으로 볼 수 있다. **다만 이것이 미적 실패라는 뜻은 아니다.**

성숙한 프로젝트에서는 대표 Approved asset을 기술적 baseline으로 삼거나(dimensions · color count range · outline density · padding · texture size), 통계값으로 anomaly를 찾을 수 있다. 하지만 **baseline과 다르다는 이유만으로 자동 실패하지 않는다. 명시된 규칙이 우선이다.**

기술 검사는 가능한 한 deterministic한 것이 좋다(dimensions · alpha · palette count · hash). 변경되지 않은 파일을 매번 다시 검사하지 않도록 hash나 timestamp를 쓰는 최적화, export 전·commit 전·batch 후 같은 시점의 자동 검사는 **필요가 생겼을 때** 붙인다. CI 시스템을 Art Studio의 필수 구조로 만들지 않는다.

---

## 22. Visual Validation Sheet

일부 기술 문제는 숫자보다 이미지로 보는 것이 빠르다. 다음은 자동 생성할 수 있다.

```text
tile repeat sheet      단일 tile → 5×5 반복 preview. seam과 반복 패턴을 함께 본다.
sprite contact sheet   front/back/left/right 또는 idle/walk/attack/hit를 한 화면에.
alpha preview          checkerboard 배경. fringe · halo · 남은 배경 · 반투명 artifact.
animation strip        frame 누락과 흔들림.
bbox / pivot overlay   정렬 문제.
scale preview          100% / 50% / 25%. 작은 sprite와 icon의 readability.
```

이것은 Technical Review와 Art Review 사이를 연결하는 보조 수단이다. 다만 축소 preview가 최종 판단은 아니다. **실제 게임 화면이 더 강한 기준이다.**

---

## 23. 자동화할 수 있는 것과 없는 것

**적극 자동화한다** — dimensions · alpha · naming · file format · frame count · 누락 파일 · texture size · color count · tile edge · duplicate · manifest completeness. 반복 빈도가 높고, 오류가 명확하고, 결과가 deterministic한 검사다.

**heuristic이 필요하다** — seam · palette anomaly · edge artifact. warning 수준으로 다룬다.

**숫자로 만들지 않는다** — "얼굴이 충분히 읽혀야 함", "무기가 실루엣에서 구분되어야 함", "배경 detail이 캐릭터를 방해하면 안 됨". 명확한 규칙이지만 자동화 대상이 아니다. Review 항목으로 남긴다.

**사람이 직접 보는 편이 나은 것** — alpha edge quality · tile visual repetition · sprite baseline 인상 · compression artifact · animation smoothness · visual aliasing · 실제 작은 화면에서의 readability.

**비전 모델**은 누락된 무기 · 잘못된 방향 · 이상한 손 · reference와의 큰 mismatch · sprite family inconsistency · tile의 명백한 오브젝트 반복을 찾는 데 도움이 된다. 다만 이런 결과는 analysis · warning · review suggestion으로 다루고, **deterministic validator와 같은 권위로 취급하지 않는다.**

같은 성격으로, 분석이 Art Direction과 연결될 수 있다.

```text
Art Direction: 배경은 캐릭터보다 낮은 contrast
Analyzer:      현재 scene에서 background contrast가 unusually high
```

유용한 warning이다. 그러나 analyzer가 `Art Direction FAIL`이라고 최종 판정하는 시스템을 기본으로 하지 않는다.

**Style drift**도 일부 기술 지표로 감지할 수 있다(palette count 증가 · outline 두께 변화 · sprite height 변화 · detail density 증가 · texture resolution 증가). 이상치를 Review 대상으로 올릴 수는 있지만, 최종 drift 판단은 프로젝트 문맥과 Art Review를 포함한다.

---

## 24. Validation이 디자인을 지배하지 않는다

다음과 같은 상황을 피한다.

```text
validator가 32 colors만 지원하므로 디자인을 32 colors로 만든다.
```

프로젝트에 48 colors가 더 적합하다면 고쳐야 하는 것은 validator다.

> **검사 도구가 아트 방향을 결정하지 않는다.**

규격이 존재하는 이유도 숫자를 맞추기 위해서가 아니다. `sprite = 64×64`는 화면 표시 크기 · 픽셀 밀도 · animation · memory · atlas · camera와 연결되어 있다. 그래서 기술적으로 `64×64 PASS`인데 게임 화면에서 얼굴이 안 보인다면, 재검토 대상은 자산이 아니라 규격일 수 있다.

> **Validation은 규칙을 지키게 하지만, 규칙이 잘못되었다면 규칙을 바꿀 수 있어야 한다.**

검사 기준끼리 충돌할 수도 있다. `palette <= 16`과 `soft transparency required`가 특정 방식에서 충돌한다면 기계적으로 둘 다 강제하기보다 프로젝트의 실제 요구를 다시 확인한다.

스타일과 플랫폼 제약의 충돌(고해상도 texture detail vs mobile texture memory)은 validator가 해결할 수 없는 종류의 문제다. **Trade-off를 정리해서 디렉터 또는 프로젝트 판단으로 올린다.**

---

## 25. Failure의 원인 위치를 구분한다

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

`alpha missing`이라도 source에 alpha가 없는 것인지, export 과정에서 제거된 것인지는 다른 문제다. **수정 위치를 잘못 고르면 같은 문제가 반복된다.**

처리 도구 자체가 문제를 만들 수도 있다 — resize blur · quantization artifact · compression halo · normal map inversion · alpha premultiply 문제. processing stage도 원인 후보에 포함한다.

Validator 자체가 틀릴 수도 있다 — palette analyzer bug · alpha detection 오류 · false seam detection · 잘못된 frame parsing. 검사 결과가 실제 파일과 모순되면 **validator를 절대적인 권위로 취급하지 않는다.**

그리고 이 판단은 항상 미적 재작업이 필요한지, 단순 technical fix인지의 구분과 함께 간다. runtime에서 발견된 문제의 계층 구분은 `10_ENGINE_HANDOFF.md`가 더 상세히 다룬다.

---

## 26. Rule의 출처와 설정

중요한 규칙은 어디에서 왔는지 알 수 있어야 한다.

```text
Rule: character height = 64px      Source: STYLE_SPEC.md
Rule: PNG alpha required           Source: Unity export requirement
```

이렇게 하면 임의 규칙이 시스템 표준처럼 굳는 것을 막을 수 있다.

공통 validator가 프로젝트별 값을 읽는 구조를 쓸 수 있다.

```text
common validator + project rules = project validation
```

다만 **Config를 위한 Config를 만들지 않는다.** 규칙 세 개 때문에 거대한 schema system을 만들지 않고, Markdown · 간단한 config · script argument 중 현재 규모에 맞는 방법을 쓴다. 사람이 읽는 Style Spec이 원본 기준이고, 필요하면 일부 값을 machine-readable form으로 파생시킬 수 있다. 그 config가 디렉터의 Art Direction을 대체하지는 않는다.

**Validator가 모르는 값은 임의로 채우지 않는다.** tile size가 unknown이면 "cannot validate tile size"라고 말하는 편이 낫다.

필요하면 validator version · rule source · input file · result · timestamp를 기록할 수 있고, 도구 업데이트로 output이 바뀔 수 있는 중요한 production pipeline에서는 tool version도 남길 수 있다. 소규모 작업에는 과도한 metadata다.

검증 시스템 자체도 미리 만들지 않는다. 실제 문제가 반복되는 것을 확인하고 그때 필요한 검사를 추가한다.

> **Validation도 실제 반복에서 성장한다.**

프로토타입 단계의 미완성 규칙(naming 불통일 · 임시 texture size · placeholder format)은 즉시 해결하지 않아도 되지만, production으로 넘어갈 때 정리 대상으로 인식한다. 대규모 프로젝트에서는 일부 critical validation을 export 전 gate로 쓸 수 있으나 모든 프로젝트에 gate system을 강제하지 않는다.

---

## 27. 파일 검증과 Runtime 검증의 경계

```text
FILE VALIDATION
≠
RUNTIME VALIDATION
```

`64×64 PASS · alpha PASS · palette PASS`인 sprite가 runtime에서 너무 작거나, 배경에 묻히거나, 조명으로 색이 변하거나, VFX에 가려질 수 있다.

이 문서는 engine-specific 기술 요구를 규칙으로 다룰 수 있다.

```text
Unity export: PNG required · max 2048 · alpha required
```

하지만 Texture Type · Pixels Per Unit · Import Preset · Material setup · Prefab · scene 배치는 `10_ENGINE_HANDOFF.md`가 다룬다.

---

## 28. 디렉터에게 무엇을 보고하는가

Claude가 처리할 수 있는 technical issue는 결과만 짧게 전달하면 된다.

```text
기술 검사 완료. 2개 frame의 alpha 문제를 수정했다. Art Review에는 영향 없음.
```

반면 다음은 디렉터의 판단에 영향을 주므로 뒤에서 조용히 처리하지 않는다.

- 규격 때문에 디자인을 바꿔야 함
- platform limit로 품질이 감소함
- palette target과 현재 방향이 충돌함
- compression으로 시각적 손실이 발생함
- runtime scale 문제
- 여러 해결 방법이 서로 다른 미적 결과를 만듦

---

## 29. 다른 문서와의 관계

- **`04_ART_DIRECTION_SYSTEM.md`** — 스타일의 시각적 축과 Art Direction / Style Spec의 차이를 정의한다. 이 문서는 그중 측정 가능한 부분을 검사한다.
- **`06_ASSET_LIFECYCLE.md`** — 상태의 의미를 정의한다. Technical Fail은 미적 Rejected가 아니다.
- **`07_GENERATION_WORKFLOW.md`** — 제작 중 언제 어느 정도의 검사를 수행할지 결정한다. 순서는 작업에 따라 `Generate → Validate → Fix → Review`일 수도, `Generate → Review → 승인 전 Validate`일 수도 있다.
- **`08_REVIEW_AND_APPROVAL.md`** — Validation은 Technical Review의 주요 입력이다. Art Review와 한 화면에 놓을 수 있지만 의미는 분리한다.
- **`10_ENGINE_HANDOFF.md`** — export format · dimensions · texture limit · channel · import 호환성 등 engine-specific 검증이 handoff 과정과 연결된다.
- **`11_LEARNING_AND_REUSE.md`** — 범용 validator는 Studio 공통 능력으로 축적하고, 프로젝트별 규격 값은 스타일과 함께 프로젝트에 남긴다.
- **`STYLE_SPEC.md`** — 실제 규격 값을 기록한다. 이 문서는 그 값을 검사하는 원칙을 제공한다.
- **`ASSET_MANIFEST.md`** — validation 상태나 export readiness를 요약할 수 있다. **validator report 전체를 담는 문서가 아니다.**
- **`REVIEW_LOG.md`** — 기술 문제 때문에 방향이 바뀐 경우에만 남긴다("48px sprite가 모바일에서 지나치게 작아 64px로 변경"). 단순 alpha fix는 기록 대상이 아니다.

### 공통화할 validator와 프로젝트에 남길 validator

공통화 조건 — 여러 프로젝트에서 반복됨 · 특정 스타일에 종속되지 않음 · 입출력이 명확함 · 기술 문제를 안정적으로 탐지함 · 유지 비용보다 반복 절감 효과가 큼. **처음 한 번 썼다고 바로 공통 도구로 만들지 않는다.**

프로젝트에 남는 것 — 특정 palette membership · 특수 atlas layout · 독특한 sprite naming · 프로젝트 고유 mask packing · 특정 boss texture constraint. 범용성이 확인되면 이후 공통화할 수 있다.

공통 validator는 `studio/tools/` 같은 공통 영역에 둘 수 있으나, 이 문서가 실제 폴더나 구현을 강제하지 않는다.

---

## 30. 이 문서에서 다루지 않는 것

```text
특정 프로젝트의 실제 규격 값              STYLE_SPEC.md
최종 미적 승인                           08_REVIEW_AND_APPROVAL.md
자산 상태 정의                           06_ASSET_LIFECYCLE.md
실제 생성 루틴                           07_GENERATION_WORKFLOW.md
엔진별 상세 import 설정                   10_ENGINE_HANDOFF.md
Validator script의 실제 코드 구현         studio/tools/의 개별 도구
프로젝트별 naming convention             프로젝트 문서 또는 별도 규칙
```

이 문서는 **기술 규격과 검증의 상위 원칙**에 집중한다.

---

## 31. 핵심 원칙 요약

Asset Specification & Validation은 아트를 숫자로 평가하는 시스템이 아니다.

> **Art Direction과 Style Specification을 구분한다.**

> **Style Spec에서 내려온 측정 가능한 규칙을 Validation에서 확인한다.**

> **공통화하는 것은 검사 능력이고, 프로젝트별 실제 규격 값은 각 프로젝트에 남긴다.**

> **미정 값을 억지로 공식 규칙으로 만들지 않는다.**

> **Technical Pass와 Director Approval을 동일시하지 않는다.**

> **Validation Failure는 Director Rejection이 아니다.**

> **Concept, Candidate, Approved, Export는 필요한 검증 강도가 다르다.**

> **Dimensions, alpha, format, frame, tile seam, naming처럼 기계가 잘하는 검사는 적극 자동화한다.**

> **매력, 분위기, 세계관 적합성 같은 미적 판단을 validator가 대신하지 않는다.**

> **예외와 프로젝트별 차이를 허용한다.**

> **검사 도구에 맞추기 위해 디자인을 바꾸지 않는다. 규칙이 잘못되었다면 규칙이나 validator를 수정한다.**

> **자동 수정은 원본을 보존하고 미적 영향 가능성을 드러낸다.**

> **파일 validation과 runtime validation을 구분한다.**

> **Validation은 작업을 복잡하게 만드는 절차가 아니라, 반복적인 기술 실수를 줄여 디렉터가 아트 판단에 집중하도록 돕는 제작 기반이다.**
