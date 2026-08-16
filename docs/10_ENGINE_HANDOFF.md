# 10_ENGINE_HANDOFF

## 1. 문서의 역할

이 문서는 승인된 자산을 **실제 게임 엔진 또는 실행 환경으로 전달하고, 런타임에서 의도한 시각적 결과가 유지되는지 확인하는 방식**을 정의한다.

이 문서는 특정 엔진의 상세 import 매뉴얼이 아니다. Unity · Godot · Roblox Studio 중 하나를 기본값으로 삼지 않는다. Asset Lifecycle의 상태 정의나 Art Review의 판단 기준을 다시 설명하지 않고, 각 프로젝트의 Style Spec이나 엔진 설정값을 대신 결정하지도 않는다.

핵심 질문은 하나다.

> **Approved source를 어떻게 실제 게임에서 사용할 수 있는 형태로 전달하고, 게임 화면에서 결과가 의도대로 보이는지 어떻게 확인할 것인가?**

---

## 2. 가장 중요한 원칙

```text
APPROVED SOURCE
≠
ENGINE EXPORT
≠
IMPORTED GAME ASSET
≠
ACTUAL GAME IMAGE
```

승인된 PNG가 있어도 실제 게임 화면에는 다음이 추가로 영향을 준다.

> import setting · scale · pivot · material · shader · lighting · post-processing · compression · filtering · camera · animation · VFX · UI · environment · platform rendering

따라서:

> **PNG 자체가 항상 최종 게임 아트는 아니다.**
> 게임 아트의 최종 인상은 실제 실행 환경에서 확인해야 한다.

그리고 이 계층 구분에서 이 문서의 진단 원칙이 나온다.

> **Runtime에서 문제가 보였다는 사실만으로 Approved source의 문제라고 가정하지 않는다.**

---

## 3. 기본 Handoff 흐름

```text
APPROVED SOURCE
↓
ENGINE-SPECIFIC EXPORT
↓
IMPORT
↓
SCENE / PREFAB / RESOURCE / OBJECT
↓
RUNTIME
↓
GAME SCREENSHOT / PLAY TEST
↓
REVIEW
```

문제가 없다면 현재 자산과 전달 방식을 유지한다. 문제가 있다면 먼저 **문제가 어느 계층에 있는지** 구분하고 그 지점으로 돌아간다.

```text
SOURCE  ·  EXPORT  ·  IMPORT  ·  ENGINE 설정  ·  CAMERA  ·  ENVIRONMENT
```

이 계층 구분은 13장에서 상세히 다룬다.

Handoff는 단순 파일 복사가 아니다. 프로젝트와 자산에 따라 다음이 필요할 수 있다.

> format conversion · resize · texture optimization · sprite sheet packing · atlas generation · mesh export · texture channel packing · alpha processing · platform variant 생성 · naming · import preset 적용 · material 연결 · shader 연결 · pivot 설정 · animation 연결 · scene 배치 · runtime screenshot 생성

필요한 것만 수행한다.

---

## 4. Source와 Derived Export

```text
approved/hero_master.png        approved/hero.blend
↓                               ↓
exports/unity/hero.png          exports/unity/hero.fbx
exports/web/hero.webp           exports/godot/hero.glb
exports/roblox/hero_texture.png
```

**Export는 source를 대체하지 않는다.** 가능하면 source는 수정 가능한 공식 원본으로 보존하고, export는 언제든 다시 만들 수 있는 파생물로 유지한다.

그래서 export 파일을 계속 손보아 새로운 공식 source로 만들지 않는다. 수정 위치는 문제의 위치를 따른다.

```text
문제가 source에 있다      → source를 수정하고 export를 다시 만든다
문제가 export 과정에 있다  → export pipeline을 수정한다 (source approval 유지)
문제가 engine에 있다      → engine 설정을 수정한다 (source·export 유지)
```

이 구분이 무너지면 어떤 파일이 진짜 원본인지 알 수 없게 된다.

---

## 5. Handoff 전에 확인하는 것

- 현재 Approved source가 무엇인지
- 목표 엔진과 목표 플랫폼
- Style Spec의 관련 기술 규칙과 Asset Brief의 기술 요구
- 필요한 export format
- 기존 engine asset 구조 · import rule · scene / prefab / resource
- 실제 게임 저장소 위치와 그 프로젝트의 기존 규칙

**이미 프로젝트에 명확한 규칙이 있다면 그것을 우선한다.**

게임 저장소에는 이미 asset naming · import preset · folder structure · texture convention · prefab structure · scene convention · platform configuration이 존재할 수 있다. Art Studio는 자신의 편의를 위해 그 규칙을 임의로 바꾸지 않는다.

> **아트 전달을 위해 게임 프로젝트의 핵심 구조를 재설계하지 않는다.** 필요한 범위만 안전하게 수정한다.

두 공간의 역할도 구분한다.

```text
Art Studio                      Game Repository
art-studio/projects/game-a/     ~/games/game-a/

source · reference              실제 사용 자산
candidate · approved            scene · prefab · resource
export preparation              game code
review material                 runtime setting
```

Handoff는 이 두 공간 사이의 연결이다.

---

## 6. 대상 환경은 엔진 하나로 제한되지 않는다

Unity · Godot · Roblox Studio · Web · custom engine · 앞으로 등장할 엔진 모두 대상이 될 수 있다. **이 문서는 특정 엔진을 상위 기준으로 만들지 않는다.**

각 환경에서 확인할 수 있는 것은 대체로 같은 계층에 속한다.

```text
공통          import 결과 · filtering · compression · scale · pivot · material ·
              shader · lighting · camera · animation · scene composition

Unity 예      sprite import · Pixels Per Unit · 2D light · post-processing · VFX · sorting
Godot 예      texture import · sprite · tilemap · 2D/3D lighting · resource
Roblox 예     world scale · character scale · SurfaceAppearance · material ·
              camera distance · 모바일 가독성 · world density
Web 예        image format · CSS scaling · canvas rendering · pixelated filtering ·
              device pixel ratio · browser 색 차이 · loading size · responsive scale
```

Roblox에서는 외부 이미지 자체보다 **Roblox 안에서 어떻게 보이는가**가 결정적인 경우가 많고, Web도 단순한 파일 목적지가 아니라 실제 표시 환경이다.

엔진별 상세 규칙이 필요해지면 별도 guide(`UNITY_ART_HANDOFF.md` 등)나 프로젝트 설정으로 분리할 수 있다. 다만 **engine guide는 공통 원칙을 그 엔진에서 구현하는 하위 문서이지 상위 규칙을 바꾸는 문서가 아니다.** Unity guide가 있다고 해서 "모든 프로젝트는 Unity 방식으로 자산을 준비한다"가 되지 않는다.

---

## 7. Export

**Format**은 자산과 엔진 요구에서 결정한다.

```text
2D       PNG · WEBP · SVG · sprite sheet · atlas
3D       FBX · GLB · GLTF · OBJ · engine-specific resource
Texture  PNG · TGA · EXR · compressed texture
Data     animation metadata · atlas metadata · pivot data · mask/channel configuration
```

Art Studio 전체에 "모든 2D = PNG", "모든 3D = FBX", "모든 texture = 2048" 같은 기본값을 만들지 않는다. 게임마다 다르고, 같은 게임 안에서도 플랫폼별로 다르다.

**Multi-platform** — 하나의 Approved source에서 여러 export가 나올 수 있고, platform마다 texture dimensions · compression · format · quality · atlas · mesh complexity · shader · material이 달라질 수 있다.

```text
approved/source
├─ exports/pc/
├─ exports/mobile/
└─ exports/web/
```

**Source의 시각적 의도는 유지하면서 각 환경의 요구를 충족한다.**

**Export 전후의 검사** — export 전에는 source dimensions · alpha · format · frame count · texture channels · naming · 누락 파일을, export 후에는 dimensions/aspect 변화 · alpha 손실 · color profile 변화 · channel 손실 · compression artifact · frame 누락 · crop 오류를 본다. 검사 원칙 자체는 `09_ASSET_SPEC_AND_VALIDATION.md`를 따른다.

---

## 8. Import는 성공 여부만 보지 않는다

```text
file loaded
≠
game art displayed correctly
```

import 후에 잘못될 수 있는 것 — scale · filtering · pivot · sprite slicing · material · shader · texture type · color space · transparency · compression · animation mapping.

특히 다음은 시각 결과에 직접 영향을 주므로, 단순한 개발 설정으로 보지 않는다.

> nearest / bilinear filtering · texture compression · mipmap · color space · sprite mode · alpha handling · normal map interpretation · material shader

**Import setting이 아트의 일부가 될 수 있다.** 아트가 어떻게 보이는지에 영향을 준다면 Art Studio가 검증 대상으로 삼는다.

반복 프로젝트에서는 import preset(pixel sprite · UI texture · normal map · mobile texture 등)이 반복 오류를 줄여준다. 다만 잘못된 preset을 모든 자산에 강제하지 않고, **preset이 Art Direction을 결정하지도 않는다.** `nearest filtering` preset이 존재한다고 해서 모든 프로젝트를 픽셀 아트로 만들지 않는다. Preset은 이미 결정된 요구를 안정적으로 적용하는 도구다.

---

## 9. Runtime에서 확인하는 것

**크기와 시점**

- scale — world scale · screen occupancy · character height · icon 표시 크기 · UI scale · zoom range
- camera — 시점 방식 · FOV · distance · zoom · framing
- pixel art — integer scaling · nearest filtering · pixel snapping · subpixel movement · camera scaling · render resolution · UI scaling

source sprite가 완벽해도 엔진에서 흐려질 수 있다. **실제 runtime pixel 결과를 확인한다.**

**정렬과 조립**

- pivot / anchor — 잘못되면 발이 흔들리고, 무기 회전이 이상해지고, animation이 튀고, UI 정렬이 어긋난다. 기술 설정이지만 움직임과 형태 인상에 영향을 준다.
- sprite slicing — frame dimensions · slicing · order · spacing · pivot · 누락 frame. validation 결과와 engine import 결과가 일치하는지 본다.
- atlas — packing · padding · bleed · filtering · 예상치 못한 compression · UV 문제. 작은 sprite와 UI asset에서 atlas bleed가 시각 문제를 만든다.
- sorting / layering / depth — 캐릭터가 잘못된 오브젝트 뒤에 그려짐 · VFX 순서 · foreground/background · UI overlap · clipping · occlusion · depth fog. **이 문제는 art source 자체의 문제가 아닌 경우가 많다.**

**재질과 빛**

- material — roughness · metallic · transparency · emission · tint · normal intensity · shader parameter. Approved texture가 좋아도 material 설정이 잘못되면 전혀 다른 결과가 나온다.
- shader — outline · toon shading · dissolve · pixelation · palette swap · rim light · distortion · water · foliage · lighting model. **shader는 스타일 자체의 일부가 될 수 있다.**
- lighting — key light · ambient · shadow · rim light · 2D/point/directional light · baked/dynamic light
- post-processing — bloom · color grading · fog · vignette · depth of field · motion blur · exposure · contrast · saturation. 이것 때문에 source의 색이나 가독성이 무너질 수 있다.
- color space — sRGB / linear. source에서는 정상인데 engine에서 색이 달라진다면 확인한다.
- transparency — sorting · premultiply · halo · blending · depth. **파일 alpha가 정상이어도 runtime에서 문제가 생길 수 있다.**

**함께 보이는 것들**

- VFX — 캐릭터 가림 · 과도한 brightness · 화면 우선순위 붕괴 · team color 혼동 · attack readability 저하. 중요한 전투 자산은 VFX가 포함된 실제 장면에서 본다.
- UI — status UI가 얼굴을 가림 · icon이 world보다 강함 · HUD color와 faction color 충돌 · subtitle이 중요한 환경 요소를 가림. 필요하면 실제 HUD가 포함된 화면에서 검토한다.
- environment — 캐릭터 단독으로는 잘 읽히는데 실제 배경에서는 묻힐 수 있다. 원인은 character · environment · lighting · camera 중 하나 또는 여럿이다.

**움직임**

- animation — pose readability · frame timing · pivot consistency · scale · silhouette · foot sliding · loop · transition. 정지 이미지가 좋아도 animation에서 형태가 무너질 수 있다.
- 3D rig — rig mapping · scale · root motion · skinning · deformation · bone orientation · animation 호환성

**성능 관련**

- texture memory · shader cost · particle count · mesh complexity · overdraw · LOD transition · mipmap · 플랫폼별 compression 결과(color shift · banding · alpha artifact · blur)

성능 문제는 기술적이지만 아트 결과에 영향을 준다. 다만 **성능 때문에 디자인을 임의로 바꾸지 않는다.** "particle이 비싸므로 효과를 절반으로 줄였다"가 시각적 방향을 크게 바꾼다면 디렉터의 판단이 필요하다. 먼저 optimization · batching · shader 변경 · texture 변경 · LOD 같은 다른 해결책을 검토한다.

---

## 10. Source와 Engine의 책임 분담

가장 중요한 질문 하나가 여기에 있다.

> **이 게임의 빛은 source asset이 만드는가, engine이 만드는가, 둘이 나누어 만드는가?**

Art Direction에서 정한 역할 분담이 실제 엔진에서 유지되는지 확인한다. 분담이 어긋나면 중복이 생긴다.

```text
sprite에 강한 오른쪽 highlight  +  engine light는 왼쪽     → 부자연스러움
sprite에 bloom-like glow        +  engine bloom            → 과도함
source에 그려진 shadow          +  engine shadow           → 뭉개짐
```

**VFX나 shading을 source와 engine에 중복해서 넣지 않는지 본다.** 이런 문제는 자산의 결함이 아니라 책임 분담을 다시 볼 신호다.

반대 방향도 성립한다. 어떤 프로젝트에서는 스타일의 중요한 부분이 engine에서만 만들어진다.

```text
source sprite: 단순 shading
engine:        fog + light + bloom
```

이 조합이 그 프로젝트의 실제 스타일일 수 있다. 그래서 **Approved source만 보고 Art Direction을 완전히 판단하지 않는다.**

일부 자산은 애초에 엔진 안에서 만들어진다(shader · particle system · material · procedural effect · lighting setup). 이 경우 "source"가 PNG 파일이 아닐 수 있고, Art Studio는 파일 형식보다 **시각 결과와 수정 가능한 source의 의미**를 본다. runtime에서 생성되는 요소(procedural texture · dynamic decal · generated map · dynamic UI effect)라면 Handoff는 설정과 시각 검증을 함께 포함한다. 다만 게임 로직 전체를 Art Studio가 흡수하지는 않는다.

그래서 엔진은 결과를 받는 곳만이 아니다. lighting exploration · camera test · shader development · material tuning · VFX · environment composition · screenshot 생성에 활용할 수 있는 **제작 도구이자 검증 환경**이다.

---

## 11. Runtime 조합과 Variant

엔진에서 최종 자산은 이미지 파일보다 높은 수준의 객체일 수 있다.

```text
Unity    texture → material → prefab
Godot    texture → resource → scene
Roblox   texture / mesh → instance → model
```

일부 "자산"은 여러 source의 조합이다(character prefab · VFX prefab · UI widget · building set · animated prop). 이 경우 Approved source 하나가 아니라 여러 승인 요소와 runtime setting이 결합된다.

```text
character sprite + outline shader + team color + shadow + VFX
```

이 조합이 실제 "게임에서 보이는 캐릭터"이며, 조합 자체가 검토 대상이 된다.

같은 source가 여러 상태로 보이기도 한다.

```text
runtime variant   team color · damaged · poisoned · selected · stealth
dynamic material  damage flash · dissolve · highlight · faction tint
lighting variant  낮 / 밤 · 실내 / 실외
camera variant    far(실루엣) / mid / close(디테일)
device variant    desktop · mobile · tablet · console
```

이런 variant가 중요한 프로젝트에서는 정적 screenshot 하나로 판단하지 않는다. **모든 조건에서 똑같이 보여야 한다는 뜻은 아니다.** 각 조건에서 게임플레이 요구를 충족하는지 본다.

---

## 12. Runtime Review

Runtime Review는 하나의 질문에 답한다.

> **이 자산은 실제 게임에서 의도한 역할을 수행하는가?**

- 플레이어가 알아볼 수 있는가
- 중요한 정보가 읽히는가
- Art Direction의 인상이 유지되는가
- 다른 자산과 조화되는가
- engine effect가 source를 망치지 않는가
- scale이 적절한가

**Runtime screenshot**은 홍보 이미지가 아니라 검증 자료다. 가능하면 typical camera · typical background · actual lighting · UI · VFX · 실제 플레이 거리를 포함한다. before/after 또는 후보 간 비교로 쓰면 source 이미지에서는 보이지 않던 차이가 드러난다.

정지 화면으로 부족하면 **gameplay capture**를 본다 — 빠른 움직임 · camera shake · animation · particle · multiplayer density · UI transition. 액션 게임에서 특히 중요하다.

프로젝트가 성숙하면 대표 runtime screenshot을 **baseline**으로 삼아 새 Handoff 결과를 비교할 수 있고(`reviews/visual-target-01.png`), 검증용 대표 scene(daylight · night · combat · UI-heavy · crowded)이나 test harness(캐릭터 라인업 · 타일 반복 · VFX 모음 · lighting variant)를 만들 수 있다. 다만 **모든 프로젝트에 별도 test scene을 강제하지 않는다.** 반복 검증 가치가 확인될 때 만든다. 반복이 많다면 고정 카메라 screenshot · asset lineup · before/after capture를 자동화할 수 있다.

디렉터가 특정 runtime screenshot을 대표 시각 기준으로 채택할 수도 있다. 이 경우 새 자산은 source뿐 아니라 그 화면과도 비교한다.

---

## 13. 문제 위치를 구분한다

이 문서에서 가장 중요한 절차다. Runtime에서 문제가 보였을 때 원인은 여섯 계층 중 어디든 될 수 있다.

**Source 문제** — silhouette 약함 · proportion 문제 · color hierarchy 문제 · detail 과다 · texture 과다 · pose 문제.
→ source 수정 Candidate를 만든다.

**Export 문제** — resize blur · alpha loss · compression · crop · channel loss · 잘못된 atlas.
→ **source approval을 유지한 채 export만 다시 만든다.**

**Import 문제** — wrong filtering · wrong sprite type · wrong normal map interpretation · color space mismatch · wrong pivot · wrong scale.
→ source나 export를 다시 만들 필요가 없다.

**Engine 설정 문제** — lighting · shader · material · fog · post-processing.
→ 자산을 수정하기 전에 runtime setting을 먼저 검토한다.

**Camera 문제** — scale · distance · FOV · framing.
→ 디자인이 아니라 카메라가 원인일 수 있다.

**Environment 문제** — background contrast too high · 과도한 detail · 캐릭터와 같은 hue/value · 랜드마크가 가려짐.
→ 캐릭터만 수정하는 것이 최선이 아닐 수 있다.

잘못된 계층을 수정하면 source가 불필요하게 왜곡된다.

```text
문제:        캐릭터가 흐림
실제 원인:    bilinear filtering
잘못된 대응:  캐릭터 outline을 더 두껍게 다시 그림
```

그래서 실패를 하나의 "아트 실패"로 묶지 않는다. 가능한 원인을 나열하고 차례로 확인한다.

```text
문제:     캐릭터가 너무 흐림
가능 원인: source resolution · export resize · bilinear filtering · camera scale
```

> **가장 위 단계부터 무조건 다시 만들지 않는다.**

그리고 새 export나 import가 문제를 만들었다면 이전 정상 상태로 돌아갈 수 있어야 한다 — version control · 이전 export · 이전 import setting · 이전 prefab/resource. 구체적인 rollback 방식은 프로젝트에 따라 다르다.

---

## 14. Runtime Test의 시점

Runtime test는 Approval 전에도 후에도 들어갈 수 있다.

```text
Candidate → Temporary Handoff → Runtime Review → Approved
Candidate → Approved Source → Export → Runtime Review → 필요 시 Revision
```

character sprite · VFX · UI icon · tile · 조명에 의존하는 자산처럼 **실제 게임에서 봐야 판단할 수 있는 자산**은 전자가 자연스럽다. 이때 만든 임시 export를 공식 final export로 혼동하지 않는다.

그리고 흐름은 일방향이 아니다.

```text
Approved → Export → Runtime → Review → Revision → New Approved → New Export
```

**이 왕복이 정상적인 게임 아트 제작 과정이다.**

---

## 15. Handoff의 깊이와 완료 범위

자산마다 필요한 깊이가 다르다.

```text
단순 UI icon      approved PNG → import → display check

Pixel character   approved sprite → sheet export → import →
                  filtering / scale / pivot → animation test → runtime screenshot

3D character      approved model → export → texture/material →
                  rig/animation → lighting → camera → runtime review
```

**모든 자산에 같은 handoff 절차를 강제하지 않는다.**

완료의 의미도 프로젝트와 요청에 따라 다르다.

```text
Export Ready      엔진용 파일 준비 완료
Imported          게임 프로젝트에 import 완료
Integrated        scene / prefab / resource에 연결 완료
Runtime Verified  실제 게임 화면에서 확인 완료
```

이것을 공식 상태 enum으로 만들 필요는 없다. 중요한 것은 **이번 요청의 완료 범위를 이해하는 것**이다. "Unity에서 실제 게임 화면까지 확인"이라면 export만 하고 끝내면 부족하고, "Roblox용 texture export만 준비"라면 runtime integration까지 필요하지 않다.

같은 이유로 모든 자산에 수십 항목짜리 checklist를 만들지 않는다. 반복적으로 필요한 핵심 사항만 쓴다. 다만 주인공 · 대표 환경 · 핵심 VFX처럼 프로젝트의 기준이 되는 자산은 source · export · material · screenshot · 중요한 설정을 더 잘 보존할 가치가 있다.

---

## 16. 자동화와 안전

자동화할 수 있는 것 — resize · format conversion · atlas · sprite sheet · texture compression · naming · 게임 저장소로 복사 · metadata 생성. import 쪽에서도 asset copy · preset apply · resource generation · prefab update가 가능할 수 있다. 반복량이 커질수록 가치가 높다.

대량 자산에서는 다음 흐름이 유용하다.

```text
Approved assets → batch export → validation → game repository → spot runtime review
```

**전체 방향을 샘플로 먼저 검증한 뒤 batch를 수행하는 편이 안전하다.** 그리고 모든 파일을 같은 깊이로 보기보다 대표 자산 · 가장 복잡한 자산 · 가장 작은 자산 · warning이 있는 자산 · 새로운 category · baseline과 차이가 큰 자산을 우선 본다.

자동화가 강해질수록 안전 확인이 중요해진다. 주의할 문제 — wrong project path · overwrite · stale export · wrong platform · wrong import preset · 의도치 않은 코드 수정 · approved source mismatch.

특히 **기존 게임 자산을 덮어쓸 때는 영향을 먼저 확인한다.** 현재 사용 중인 자산 · 사람이 직접 수정한 자산 · 엔진이 생성한 metadata · prefab reference · 공유 texture를 무심코 파괴하지 않는다. 필요하면 교체 전에 버전 관리나 backup을 확인하되, **version control이 있다고 무조건 안전하게 overwrite할 수 있다고 가정하지 않는다.**

commit 전략 · LFS · branch · PR · binary storage 정책은 이 문서에서 고정하지 않는다. 게임 프로젝트의 기존 규칙을 따른다.

---

## 17. Source of Truth와 Staleness

현재 공식 source가 무엇인지 분명해야 한다.

```text
Art Studio approved source = hero_master.psd
Game Repository의 PNG      = derived asset
```

프로젝트 구조에 따라 게임 저장소의 파일이 공식 source일 수도 있다. 핵심은 혼동하지 않는 것이다.

> **두 개의 Source of Truth를 만들지 않는다.**

`art-studio/approved/hero.png`와 `game-repo/Assets/hero_source.png`를 각각 수정하면 drift가 생긴다. 한쪽을 공식으로 정하고 다른 쪽은 derived 또는 synchronized copy로 본다. Sync 자체를 거대한 시스템으로 만들 필요는 없고, 반복 오류가 실제로 생길 때 자동화한다.

**Staleness** — source가 새로 승인되면 기존 export가 낡는다.

```text
hero_v2 approved → hero_v1 unity export stale
Art Studio approved: hero_v3 / Game runtime: hero_v2
```

timestamp · hash · source version · manifest · metadata로 stale export를 탐지하거나 갱신할 수 있다. 작은 프로젝트에 복잡한 dependency system을 강제하지 않는다.

**Metadata** — 필요하면 source file · export target · platform · tool · version · date · settings · checksum을 기록한다. 재현성이 중요한 자산이나 batch에서 유용하고, 모든 작은 자산에 강제하지 않는다.

엔진이 생성하는 metadata(Unity `.meta` · Godot import data · Roblox asset ID · web manifest entry)도 있다. 이 파일과 source asset의 관계를 이해하되 **엔진 metadata를 source art로 취급하지 않는다.**

ID도 계층이 다를 수 있다.

```text
Art Studio  CHR_001
Unity       Assets/Characters/Hero.png
Roblox      asset id 123456        (Approved Source → Uploaded Asset → Asset ID → Runtime Object)
Web         public asset path      (URL 자체가 공식 source가 아니다)
```

필요하면 연결 정보를 Manifest나 프로젝트 기록에 남기되, 모든 프로젝트에 복잡한 registry를 만들지 않는다.

---

## 18. 엔진 종속을 피한다

Studio 공통 문서에 "모든 texture는 Unity 규칙" 같은 기본값을 넣지 않는다. Engine-specific knowledge는 별도 능력으로 축적한다.

가능하다면 Approved source는 특정 엔진에 지나치게 묶이지 않는 형태로 보존한다 — master texture · editable PSD · Blender source · 고품질 sprite source. 그다음 엔진별 export를 파생한다. 항상 가능한 것은 아니다.

엔진이 바뀌어도(`Unity → Godot`) Art Studio의 상위 구조가 무너지지 않아야 한다. 다만 완전히 독립적일 수만은 없다. shader 지원 차이 · texture constraint · 2D lighting capability · platform limit 때문에 source나 Style Spec이 바뀔 수 있다. 이때 **그 변화가 기술적 요구인지 시각적 방향 변화인지 구분한다.**

---

## 19. 디렉터와의 관계

디렉터는 다음처럼 요청할 수 있어야 한다.

> 실제 게임에 넣어봐.

Art Studio는 필요한 export · import · scale · material · camera · screenshot을 처리하거나 준비한다. **디렉터가 매번 import 옵션을 직접 지정해야 하는 시스템을 목표로 하지 않는다.**

다만 결과에 중요한 선택은 짧게 설명할 수 있어야 한다.

> 이 프로젝트는 픽셀 스프라이트라 bilinear filtering을 끄고 nearest로 확인했다.
> 이 캐릭터는 엔진 조명이 스타일의 핵심이라 source에 강한 baked highlight를 추가하지 않았다.

복잡한 자산에서는 전달 메모가 engine developer의 실수를 줄인다.

```text
Hero Sprite
- nearest filtering
- bottom-center pivot
- engine outline shader 사용
- source baked outline 없음
```

다른 개발자가 엔진 integration을 담당하는 경우에도 Handoff는 성립한다. Approved source · export · 기술 요구 · preview · 기대하는 표시 결과 · reference screenshot · 알려진 제약을 제공하면 된다. 필요하면 asset · preview · spec · notes를 묶을 수 있지만, 모든 작업에 formal package를 강제하지 않는다.

---

## 20. Art Studio의 범위

이 문서의 목적은 CI/CD · release pipeline · build system · deployment system을 설계하는 것이 아니다. 배포는 별도 영역이다. Art Studio는 **아트 자산을 실제 게임 환경에서 사용할 수 있고 검증 가능한 상태로 만드는 데** 집중한다.

아트 검증을 위해 작은 코드 수정(test scene · asset swap · debug toggle · screenshot mode · camera position)이 필요할 수 있다. 사용자의 지시나 기존 프로젝트 규칙 범위 안에서 수행하고, **게임 핵심 로직을 아트 작업이라는 이유로 재설계하지 않는다.**

gameplay system · networking · save system · server · AI behavior · economy · core architecture는 Art Studio의 기본 책임이 아니다. Handoff를 이유로 게임 개발 프로젝트 전체를 끌어오지 않는다.

그래서 문제의 성격도 구분한다. "캐릭터가 공격할 때 잘못된 sprite가 표시됨"이 asset mapping 문제인지, animation controller 문제인지, gameplay state bug인지 구분하고 Art Studio가 해결할 수 있는 범위를 판단한다.

---

## 21. 반복되는 문제와 학습

Runtime에서 같은 문제가 반복되면 Style Spec · exporter · import preset · validation · engine guide · test scene 중 하나를 개선한다. 반복되는 기술 문제는 Studio 노하우로 축적할 수 있다.

**공통화할 가치가 있는 것** — format converter · resize helper · sprite sheet exporter · texture channel packer · engine copy helper · validation hook · screenshot helper · Unity pixel import helper · Godot atlas exporter · Roblox texture uploader · Web image optimizer. 실제 반복이 확인된 뒤 공통화한다.

**프로젝트에 남는 것** — 특정 prefab path · 특정 material · 특정 shader parameter · 특정 Roblox object 구조 · 특정 scene · 특정 export path. 이를 Studio 전체 기본값으로 만들지 않는다.

동시에 **Handoff 문제를 Art Direction 문제로 잘못 일반화하지 않는다.** "Unity filtering 문제"를 "이 프로젝트 sprite 스타일이 잘못됐다"로 해석하지 않는다.

반대 방향도 있다. runtime 실험이 새로운 시각 가능성을 보여줄 수 있다(`engine fog + low contrast background`). 결과가 좋다면 디렉터가 프로젝트 방향으로 채택할 수 있고 Art Direction이 갱신될 수 있다. 다만 실험 설정(`temporary bloom 2.0`)을 바로 공식 프로젝트 설정으로 만들지 않는다. **채택하는 것은 디렉터다.**

---

## 22. Handoff에서 가장 중요한 질문

복잡할 때 다음으로 돌아간다.

1. **공식 source는 무엇인가** — 현재 무엇이 Approved인가?
2. **어떤 환경에서 사용되는가** — 엔진 · 플랫폼 · 카메라 · 실제 표시 조건은?
3. **어떤 파생 처리가 필요한가** — export · resize · material · shader · animation 중 무엇이 필요한가?
4. **실제 게임에서 의도대로 보이는가** — Art Direction과 gameplay 요구를 충족하는가?
5. **문제가 있다면 어디에 있는가** — Source / Export / Import / Engine / Camera / Environment 중 어디를 수정해야 하는가?

---

## 23. 다른 문서와의 관계

- **`03_PROJECT_STRUCTURE.md`** — Approved source와 Export의 구조적 분리를 정의한다. 이 문서는 그 사이의 실제 전달과 검증을 정의한다.
- **`04_ART_DIRECTION_SYSTEM.md`** — 카메라 · 조명 · VFX · UI · 실제 게임 화면이 스타일에 기여함을 정의한다. 이 문서는 그것을 엔진에서 검증한다.
- **`05_TOOL_ROLES.md`** — 엔진을 runtime validation 환경으로 정의한다. 이 문서는 그 역할을 실제 흐름에 적용한다.
- **`06_ASSET_LIFECYCLE.md`** — Approved source와 Export 상태의 의미를 정의한다. Runtime Review에서 문제가 생기면 다시 Candidate 단계로 돌아갈 수 있다.
- **`07_GENERATION_WORKFLOW.md`** — 필요하면 runtime test를 제작 과정에 포함한다.
- **`08_REVIEW_AND_APPROVAL.md`** — runtime screenshot과 gameplay 결과를 Art Review input으로 사용한다. 후보 비교에서 source보다 runtime 화면이 더 의미 있는 경우가 있다.
- **`09_ASSET_SPEC_AND_VALIDATION.md`** — source와 export의 기술 규격을 검사한다. `source validation → export → export validation → import → runtime validation`을 모든 단계에 강제하지 않고, 문제와 반복량에 맞게 적용한다.
- **`11_LEARNING_AND_REUSE.md`** — 반복되는 handoff 지식과 exporter를 Studio 공통 능력으로 축적한다.
- **`STYLE_SPEC.md`** — `filtering = nearest`, `texture max = 1024 mobile`, `pivot = bottom center` 같은 규칙 중 일부는 engine에서 실현된다. Handoff는 그 규칙을 실제 적용으로 연결한다.
- **`ASSET_MANIFEST.md`** — export / integration 상태를 요약할 수 있다. **engine import log 전체를 넣지 않는다.**
- **`ASSET_BRIEF.md`** — target engine · display context · platform constraint · 필요한 variant를 담을 수 있다.
- **`REVIEW_LOG.md`** — "outline을 source에서 제거하고 engine shader에서 처리", "모바일에서 48px가 작아 64px로 변경"처럼 방향이 바뀐 결정만 남긴다. 단순 import fix는 기록 대상이 아니다.

---

## 24. 이 문서에서 다루지 않는 것

```text
특정 엔진의 상세 import 설정 전체     engine-specific guide
게임 코드 아키텍처                    게임 개발 프로젝트
빌드와 배포                          별도 개발/DevOps 영역
Asset Lifecycle 상태 의미             06_ASSET_LIFECYCLE.md
Art Review의 전체 판단 기준            08_REVIEW_AND_APPROVAL.md
Validator 구현                       09_ASSET_SPEC_AND_VALIDATION.md · studio/tools/
프로젝트별 정확한 규격                 STYLE_SPEC.md
장기 학습 승격 기준                   11_LEARNING_AND_REUSE.md
```

이 문서는 **Approved source를 실제 게임 환경에 전달하고 런타임에서 확인하는 원칙**에 집중한다.

---

## 25. 핵심 원칙 요약

Engine Handoff는 파일을 엔진 폴더에 복사하는 작업으로 끝나지 않는다.

> **Approved Source와 Engine Export를 구분한다.**

> **Export는 source에서 파생된 결과이며, 원본을 대신하지 않는다. 필요하면 다시 만들 수 있다.**

> **실제 게임에서 보이는 결과는 source asset뿐 아니라 import, scale, camera, material, shader, lighting, VFX, UI, environment의 영향을 받는다.**

> **엔진은 단순한 목적지가 아니라 Art Studio의 중요한 검증 환경이 될 수 있다.**

> **Runtime에서 문제가 보이면 source를 무조건 다시 만들지 않고 Source / Export / Import / Engine / Camera / Environment 중 원인을 구분한다.**

> **Unity, Godot, Roblox, Web 중 어느 하나를 Studio 기본값으로 만들지 않는다.**

> **프로젝트의 기존 엔진 구조와 규칙을 먼저 존중한다.**

> **Art Studio와 실제 게임 저장소의 역할을 구분한다.**

> **가능하면 수정 가능한 Approved Source를 보존하고 platform/engine별 결과를 파생한다.**

> **Runtime Review는 Approval 전에도 후에도 들어갈 수 있다.**

> **실제 게임 화면이 필요하다면 screenshot과 gameplay capture를 Review input으로 사용한다.**

> **반복되는 export/import 문제는 자동화하고 공통 기술로 축적할 수 있지만, 프로젝트별 shader·material·style 값은 해당 프로젝트에 남긴다.**

> **엔진 integration을 이유로 게임 개발 전체를 Art Studio가 흡수하지 않는다.**

> **최종 목적은 파일 전달 자체가 아니라, 디렉터가 승인한 시각적 의도가 실제 게임에서 유지되도록 하는 것이다.**
