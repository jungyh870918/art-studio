# STYLE SPEC

<!--
이 문서는 새 게임을 Art Studio에 등록할 때 복제해서 쓰는 템플릿이다.
복제 위치: projects/<project-id>/brief/STYLE_SPEC.md

목적:
ART_DIRECTION이 정한 방향을 반복해서 만들기 위해,
이 프로젝트가 실제로 사용하는 기술적 스타일 규칙을 기록한다.

역할 경계:
- 이 게임이 무엇인가(장르 · 카메라 · 플랫폼 · 플레이 구조)      → PROJECT_BRIEF.md
- 이 게임이 어떻게 보여야 하는가(인상 · 형태 언어 · 금지사항)    → ART_DIRECTION.md
- 이 문서는 그것을 반복 제작하기 위한 규칙(크기 · palette · outline
  두께 · frame 수 · texture dimensions · runtime 제약)을 담는다.
- 어떤 자산이 필요하고 지금 어디까지 왔는가                      → ASSET_MANIFEST.md
- 특정 캐릭터 하나의 요구사항                                    → ASSET_BRIEF.md
- 검토와 승인 이력                                              → REVIEW_LOG.md

작성 규칙:
- 모든 항목이 필수는 아니다. 이 프로젝트에 없는 영역은 섹션째 삭제한다.
  (2D만 쓰면 3D 섹션을, VFX를 만들지 않으면 VFX 섹션을 지운다.)
- 초기에는 적용 범위 · 표현 방식 · 해상도 · edge · palette 정도만 있어도 제작을 시작할 수 있다.
- 모르는 것은 비워두지 말고 상태를 적는다:
  미정 / 현재 탐색 중 / A/B 비교 중 / engine test required / 확인 필요 / 현재 규칙 없음
- 빈칸을 채우기 위해 규칙을 만들지 않는다. 근거 없이 채워진 수치는 빈칸보다 나쁘다.
- Art Direction의 감각을 숫자로 옮겨 적지 않는다. 반복 제작에 필요한 것만 내려온다.
- 확정된 규칙과 탐색 중인 값을 섞지 않는다. Validator는 확정된 값만 FAIL 조건으로 쓴다.
- 이 문서를 machine-readable configuration이나 거대한 schema로 만들지 않는다.
  사람이 읽고 고치는 문서다.
- 작성 후 이 주석들은 지워도 되고 남겨도 된다.
-->

- 프로젝트:
- 프로젝트 ID:
- 문서 상태: <!-- 초기 탐색 / 부분 확정 / production 기준 / 수정 중 -->
- 마지막 업데이트:
- 관련 문서: <!-- PROJECT_BRIEF.md · ART_DIRECTION.md 경로 -->

---

## 1. 현재 적용 범위

<!--
이 문서가 지금 어디까지를 규칙으로 확정했는지 먼저 밝힌다.
읽는 사람이 이 문서의 신뢰 범위를 오해하지 않기 위한 항목이다.

개별 자산 목록이나 진행 상태는 여기 적지 않는다. → ASSET_MANIFEST.md
예: "캐릭터 sprite 규칙만 확정 · UI 탐색 중 · VFX 규칙 없음"
-->

**규칙이 있는 영역:**

-
-

**아직 정의하지 않은 영역:**

-
-

---

## 2. 표현 방식

<!--
"귀엽다" "무겁다" 같은 감각은 ART_DIRECTION이 담당한다.
여기에는 제작 방식에 직접 영향을 주는 표현 체계만 적는다.
해당 없는 줄은 지운다.
-->

- 기본 표현 방식: <!-- pixel art / raster / vector / 3D / hybrid -->
- Source type: <!-- 작업 원본의 형식 -->
- Runtime 표현: <!-- 게임에 최종적으로 들어가는 형식 -->
- 2D / 3D 혼합:
- 카메라 전제: <!-- 고정 / 회전 / perspective / orthographic -->
- Color mode:
- Alpha 사용:

**보충:**

<!--
항목만으로 설명되지 않을 때만 쓴다. 없으면 삭제.
예: 캐릭터는 raster sprite지만 장비는 별도 layer로 제작한다.
    환경은 3D geometry 위에 hand-painted texture를 쓴다.
-->

---

## 3. 해상도와 크기

<!--
프로젝트 전체 또는 자산군에서 반복되는 크기 규칙만 적는다.
자산 하나만의 크기 요구는 ASSET_BRIEF.md로 보낸다.
탐색 중이면 범위와 상태를 그대로 남긴다. 예: 캐릭터 높이 48–64px A/B 비교 중
-->

**화면:**

- 기준 해상도:
- Aspect ratio:
- 내부 rendering resolution: <!-- 기준 해상도와 다르면 적는다 -->
- 기준 display scale:
- 정수 배율 필요 여부:

**Sprite:**

- 기본 canvas:
- 캐릭터 크기:
- 오브젝트 크기:
- 최대 권장 크기:
- Padding:
- Trim 허용:

**Tile / Modular:** <!-- 사용하지 않으면 삭제 -->

- Tile size:
- Grid:
- Overlap / bleed:
- Seam 규칙:

**Portrait / Illustration:** <!-- 사용하지 않으면 삭제 -->

- Dimensions:
- Aspect ratio:
- Safe area:
- Crop 규칙:

---

## 4. 형태와 엣지

<!--
형태의 감성적 방향이 아니라, 형태를 실제로 어떻게 마감하는지를 적는다.
"outline이 있다"보다 "어떤 조건에서 몇 px로 적용되는가"가 이 문서의 언어다.
-->

**Outline:**

- 사용 여부:
- 두께:
- 외곽선 / 내부선 구분:
- 색상 규칙: <!-- 단색 / 자산 색 기반 / 어두운 변형 등 -->
- 두께 변화 허용:
- 예외:

**Edge:**

- Edge 성격: <!-- hard / soft / 혼합 -->
- Antialiasing:
- Pixel snapping:
- Pixel grid 준수:
- Sub-pixel 표현 허용:

**디테일 밀도:**

<!--
"큰 형태가 먼저 읽혀야 한다"는 방향은 ART_DIRECTION에 있다.
여기에는 그것을 반복 제작할 때 쓰는 제약이 있다면 적는다. 없으면 "현재 규칙 없음".
-->

- 최소 표현 단위:
- 작은 디테일 제한:
- 축소 시 제거하는 디테일:

---

## 5. 색

<!--
색의 정서적 의미는 ART_DIRECTION이 담당한다.
여기에는 실제 제작에서 반복 적용할 수 있는 규칙만 적는다.
palette 파일이 있으면 경로를 적고 HEX 목록을 이 문서에 복사하지 않는다.
-->

**Palette:**

- Fixed palette 사용 여부:
- Palette 파일 / 출처:
- 목표 색상 수:
- 허용 범위:
- 자산군별 palette 분리:
- Palette 외 색상 사용 규칙:

**Saturation / Value:**

<!-- 정량 규칙이 없으면 "현재 정량 규칙 없음"이라고 적는다. 억지로 수치를 만들지 않는다. -->

- Saturation 범위 또는 제한:
- Value range:
- 최소 value separation:

**Transparency:**

- Alpha 허용:
- Partial alpha 허용:
- Binary alpha 필요 여부:
- 투명 영역 RGB 처리:
- Premultiplied alpha:

**Color space:**

- Color space:
- Bit depth:
- HDR 사용:

---

## 6. 명암과 조명

<!--
"극적인 조명" 같은 목표는 ART_DIRECTION이 담당한다.
여기서 가장 중요한 것은 source art와 engine의 책임 분리다.
에셋에 그림자를 그려 넣었는데 엔진이 또 얹으면 결과가 뭉개진다.
-->

**Shading:**

- 기본 방식: <!-- flat / cel / painted / dithered 등 -->
- Value step 수:
- Gradient 허용:
- Soft shading 허용:
- Ambient occlusion 표현:

**Source와 Engine의 책임:**

- Source에 baked되는 요소:
- Engine이 담당하는 요소:
- Dynamic lighting 대응 필요 여부:
- Normal map 사용:
- Emission 사용:

**Shadow:**

- Cast shadow를 source에 포함하는가:
- Contact shadow 처리:
- Opacity / 단계:
- 광원 방향 고정 여부:

**Highlight:**

- Highlight 단계:
- Specular 표현:
- Rim light 처리:

---

## 7. 질감

<!--
질감을 어떤 기술적 밀도로 유지하는지 적는다.
특정 캐릭터의 옷 재질 같은 개별 요구는 ASSET_BRIEF.md로 보낸다.
-->

- Texture density:
- Texel density: <!-- 3D 또는 texture 기반 파이프라인에서만 -->
- Grain / Noise:
- Dithering:
- Brush texture 유지 여부:
- Micro-detail 허용:
- Pattern 최소 크기:
- 반복 texture 처리:

---

## 8. 캐릭터 / 생물

<!--
프로젝트 공통으로 적용되는 기술 규칙이 있을 때만 사용한다.
캐릭터 디자인 철학과 비율의 이유는 ART_DIRECTION,
특정 캐릭터 하나의 요구는 ASSET_BRIEF가 담당한다.
-->

- 기본 canvas / bounds:
- 화면상 표시 높이:
- 기본 orientation:
- Direction 수: <!-- 4방향 / 8방향 / 좌우 flip 등 -->
- Pivot:
- Baseline / ground contact:
- Layer 분리 규칙:
- 장비 · 무기 attachment 방식:

**고정된 비율 값:** <!-- 확정된 것만. 탐색 중이면 19장으로 보낸다. -->

- Head-to-body ratio:
- 손 / 발 최소 크기:
- 무기 크기 범위:

---

## 9. 환경 / 소품 / 타일

<!--
환경의 분위기는 ART_DIRECTION이 담당한다.
여기에는 반복 제작과 조립에 필요한 규칙만 적는다.
-->

**환경:**

- 기본 단위:
- Grid 사용:
- Perspective / camera 기준:
- Depth 표현 규칙:
- Layer 구성: <!-- background / midground / foreground의 기술적 구분 -->
- 반복 배치 규칙:

**소품:**

- 기본 bounds:
- Pivot:
- Ground contact:
- Orientation:
- Variant 제작 시 공통 규칙:

**Tile / Modular:** <!-- 사용하지 않으면 삭제 -->

- Tile dimensions:
- 연결 규칙:
- Edge continuity:
- Seam tolerance:
- Corner 처리:
- Auto-tiling 고려:

---

## 10. 애니메이션

<!--
프로젝트 전체 또는 자산군에서 반복되는 규칙만 적는다.
"이 캐릭터의 공격 2는 7프레임" 같은 개별 요구는 ASSET_BRIEF가 담당한다.
-->

**기본:**

- FPS:
- Variable timing 허용:
- Frame dimensions:
- Pivot / baseline 유지 규칙:
- Frame padding:
- Loop 시작·종료 규칙:
- Hold frame 사용:
- Interpolation 허용:

**일반적인 frame 수:** <!-- 규칙이 아니라 기준선이면 그렇게 적는다. 없으면 "현재 규칙 없음". -->

- Idle:
- Walk / Run:
- Attack:
- Effect:

**Sprite sheet:** <!-- 사용하지 않으면 삭제 -->

- Sheet 구성:
- Frame order:
- Row / column 규칙:
- Empty frame 허용:
- Atlas 사용:

**3D animation:** <!-- 사용하지 않으면 삭제 -->

- FPS:
- Root motion:
- Root bone:
- Scale 유지:
- Loop 처리:

---

## 11. UI / Icon

<!--
UI 정보 구조나 UX 설계 문서가 아니다.
Art Studio가 제작하는 시각 자산의 기술 규칙만 적는다. 없으면 섹션 삭제.
-->

- Icon dimensions:
- Safe area:
- Padding:
- Stroke / outline:
- Corner 처리:
- Alpha:
- 최소 표시 크기:
- 상태 variant 규칙: <!-- normal / hover / disabled 등 -->
- Scaling 방식:
- 9-slice 사용:
- Vector 사용:

---

## 12. VFX

<!--
게임플레이 효과의 설계는 이 문서의 역할이 아니다.
VFX 자산을 Art Studio가 제작할 때만 사용한다. 없으면 섹션 삭제.
-->

- 표현 방식: <!-- sprite / flipbook / particle / mesh -->
- Texture dimensions:
- Frame 수:
- FPS:
- Blend mode:
- Alpha:
- Emission:
- Distortion / soft particle:
- 화면 점유 관련 제한:

---

## 13. 3D

<!-- 3D를 쓰지 않으면 섹션 전체를 삭제한다. -->

**Scale / Orientation:**

- World unit 기준:
- 기본 scale:
- Up axis / Forward axis:
- Origin / Pivot 규칙:

**Geometry:**

- 일반 triangle budget:
- 주요 자산 budget:
- 작은 prop budget:
- LOD 사용 / 단계:
- Hard edge / smoothing 규칙:

**UV / Texture:**

- Texture dimensions:
- Texel density:
- UV padding:
- UDIM 사용:
- Atlas 사용:
- Tiling 허용:

**Material:**

- 기본 material 방식: <!-- PBR / unlit / stylized 등 -->
- Material 수 제한:
- 사용하는 channel: <!-- base color · normal · roughness · metallic · AO · emission · opacity -->
- Packed channel 규칙:

---

## 14. 엔진 / 런타임 제약

<!--
엔진 사용법이나 import 절차 매뉴얼을 쓰는 곳이 아니다. → 10_ENGINE_HANDOFF.md
아트 결과가 runtime에서 의도대로 보이기 위해 반복적으로 지켜야 하는 제약만 적는다.
-->

- Engine / Rendering path:
- Filtering: <!-- point / bilinear 등 -->
- Compression:
- Mipmaps:
- Max texture size:
- Pixels per unit / unit scale:
- Texture wrapping:
- Color space:
- Alpha handling:
- Atlas 제한:
- Shader로 인한 art constraint:
- Camera로 인한 art constraint:

---

## 15. 플랫폼 제약

<!--
플랫폼 차이가 실제 아트 제작에 영향을 줄 때만 사용한다.
빌드 설정이나 배포 매뉴얼을 쓰지 않는다. 차이가 없으면 섹션 삭제.
-->

- 목표 플랫폼:
- 최소 / 최대 화면 크기:
- DPI / pixel density 고려:
- 메모리 · texture 관련 art 제약:

**Platform variant:** <!-- 별도 variant가 필요한 플랫폼이 있을 때만 -->

- 플랫폼:
- 달라지는 값: <!-- dimensions / texture size / compression / detail level -->

---

## 16. 표시 크기

<!--
source 파일의 크기와 실제 화면에서 보이는 크기를 혼동하지 않기 위한 영역이다.
작은 화면 · 다양한 해상도 · orthographic camera · 2D3D 혼합 프로젝트에서 특히 필요하다.
-->

- 기준 표시 크기:
- 최소 / 최대 예상 표시 크기:
- Camera distance / zoom 범위:
- Runtime 확대 허용 수준:
- 축소 시 유지되어야 하는 요소:
- Pixel-perfect requirement:
- Scaling interpolation:

---

## 17. 자산 간 일관성 규칙

<!--
여러 종류의 자산이 함께 화면에 있을 때 지켜야 하는 기술적 일관성만 적는다.
"모든 캐릭터는 개성이 있어야 한다" 같은 디자인 철학은 ART_DIRECTION이 담당한다.

후보 항목:
- 캐릭터와 소품의 outline 두께 관계
- portrait와 sprite의 palette 관계
- world asset과 UI icon의 rendering 차이
- 2D와 3D 자산 사이의 lighting 책임
- 환경과 캐릭터의 texture density 관계
-->

-
-

---

## 18. 확정된 규칙

<!--
제작 기준으로 확정된 핵심 규칙만 짧게 모은다.
위 내용을 다시 상세히 복사하는 곳이 아니라, 자주 확인하는 값의 인덱스다.

Validator가 FAIL 조건으로 쓰는 값은 원칙적으로 여기에 있거나
위 섹션에서 이미 확정된 값이어야 한다. (→ 09_ASSET_SPEC_AND_VALIDATION.md)
-->

-
-
-

---

## 19. 탐색 중 / 미정

<!--
아직 공식 규칙이 아닌 기술적 항목을 적는다.
여기 있는 값은 validator의 FAIL 조건으로 쓰지 않고, 확정된 규칙처럼 취급하지 않는다.
검토 이력을 쌓는 곳이 아니라 "지금 무엇이 미정인지" 보여주는 곳이다.
-->

**항목:**

- 상태:
- 현재 후보:
- 확인 방법:

**항목:**

- 상태:
- 현재 후보:
- 확인 방법:

---

## 20. 엔진 테스트 필요

<!--
수치만으로 결정할 수 없고 실제 runtime 확인이 필요한 항목을 적는다.
확인 결과의 상세 이력은 REVIEW_LOG.md가 담당한다. 여기에는 현재 상태만 남긴다.
-->

**항목:**

- 확인할 것:
- 현재 상태:

**항목:**

- 확인할 것:
- 현재 상태:

---

## 21. 의도적으로 규칙을 두지 않는 영역

<!--
규칙이 없다는 것도 유효한 상태다.
필요 없는 규칙을 나중에 다시 만들지 않기 위해 남긴다.
-->

-
-

---

## 빠른 확인용 요약

<!--
필요한 프로젝트에서만 유지한다.
전체 문서를 대체하는 checklist가 아니라, 제작 중 자주 확인하는 값의 짧은 인덱스다.
개별 자산의 요구나 승인 여부는 넣지 않는다.
-->

- 표현 방식:
- 크기:
- Edge:
- 색:
- 명암:
- 질감:
- 애니메이션:
- Runtime:

---

<!--
갱신 시점:
탐색 중이던 값의 확정 · 엔진 테스트 결과의 반영 · 규칙의 변경이나 폐기 ·
새 자산군이 추가되어 적용 범위가 넓어질 때

갱신하지 않는 것:
개별 자산의 피드백 · 후보 비교 결과 · 생성 파라미터 · 자산 진행 상태
-->
