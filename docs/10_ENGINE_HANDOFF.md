# 10_ENGINE_HANDOFF

## 1. 문서의 역할

이 문서는 Art Studio에서 승인된 자산을 **실제 게임 엔진 또는 실행 환경으로 전달하고, 런타임에서 의도한 시각적 결과가 유지되는지 확인하는 방식**을 정의한다.

이 문서는 특정 엔진의 상세 import 매뉴얼이 아니다.

이 문서는 Unity, Godot, Roblox Studio 중 하나를 기본값으로 삼지 않는다.

이 문서는 Asset Lifecycle의 상태 정의를 다시 설명하지 않는다.

이 문서는 Art Review의 전체 기준을 다시 설명하지 않는다.

이 문서는 각 프로젝트의 Style Spec이나 엔진별 설정값을 대신 결정하지 않는다.

핵심 질문은 하나다.

> **Approved source를 어떻게 실제 게임에서 사용할 수 있는 형태로 전달하고, 게임 화면에서 결과가 의도대로 보이는지 어떻게 확인할 것인가?**

---

## 2. 가장 중요한 원칙

Art Studio에서는 다음을 구분한다.

```text
APPROVED SOURCE
≠
ENGINE EXPORT
≠
IMPORTED GAME ASSET
≠
ACTUAL GAME IMAGE
```

예를 들어 승인된 PNG가 있다고 해도 실제 게임에서는 다음이 추가로 영향을 줄 수 있다.

- import setting
- scale
- pivot
- material
- shader
- lighting
- post-processing
- compression
- filtering
- camera
- animation
- VFX
- UI
- environment
- platform rendering

따라서:

> **PNG 자체가 항상 최종 게임 아트는 아니다.**

게임 아트의 최종 인상은 실제 실행 환경에서 확인해야 할 수 있다.

---

## 3. 기본 Handoff 흐름

일반적인 흐름은 다음과 같이 이해한다.

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

문제가 없다면 현재 자산과 전달 방식을 유지한다.

문제가 있다면:

```text
SOURCE 문제?
EXPORT 문제?
IMPORT 문제?
ENGINE 설정 문제?
CAMERA 문제?
ENVIRONMENT 문제?
```

를 구분하고 적절한 단계로 돌아간다.

---

## 4. Handoff는 단순 파일 복사가 아니다

다음과 같은 작업이 필요할 수 있다.

- format conversion
- resize
- texture optimization
- sprite sheet packing
- atlas generation
- mesh export
- texture channel packing
- alpha processing
- platform variant generation
- naming
- engine import preset
- material 연결
- shader 연결
- pivot 설정
- animation 연결
- scene 배치
- runtime screenshot 생성

프로젝트와 자산 종류에 따라 필요한 것만 수행한다.

---

## 5. Source와 Derived Export를 구분한다

기본 관계는 다음과 같다.

```text
APPROVED SOURCE
↓
DERIVED EXPORT
```

예:

```text
approved/hero_master.png
↓
exports/unity/hero.png
exports/web/hero.webp
exports/roblox/hero_texture.png
```

또는:

```text
approved/hero.blend
↓
exports/unity/hero.fbx
exports/godot/hero.glb
```

Export는 source를 대체하지 않는다.

가능하면 source는 수정 가능한 공식 원본으로 보존한다.

---

## 6. Export 파일을 원본처럼 수정하지 않는다

예:

```text
approved/hero.png
↓
exports/unity/hero.png
```

Unity용 export에서 문제가 생겼다고
그 export를 직접 계속 수정해 새로운 공식 source로 만들지 않는다.

문제가 source에 있다면 source를 수정한다.

문제가 export 과정에 있다면 export pipeline을 수정한다.

문제가 engine에 있다면 engine 설정을 수정한다.

이 구분은 장기적으로 자산의 출처와 수정 경로를 명확하게 유지한다.

---

## 7. Handoff 전 확인

Engine Handoff를 시작하기 전에 필요에 따라 다음을 확인한다.

- Approved source가 무엇인지
- 현재 프로젝트의 목표 엔진
- 목표 플랫폼
- Style Spec의 관련 기술 규칙
- Asset Brief의 기술 요구
- 필요한 export format
- 기존 engine asset 구조
- 기존 import rule
- 기존 scene / prefab / resource
- 실제 게임 저장소 위치
- 외부 프로젝트의 기존 규칙

이미 프로젝트에 명확한 규칙이 있다면 그것을 우선한다.

---

## 8. 실제 게임 저장소의 규칙을 먼저 읽는다

Art Studio 외부의 게임 프로젝트에는 이미 다음이 존재할 수 있다.

- asset naming
- import preset
- folder structure
- texture convention
- prefab structure
- scene convention
- resource naming
- platform configuration

Art Studio는 자신의 편의를 위해 게임 저장소 규칙을 임의로 바꾸지 않는다.

특히:

> **아트 전달을 위해 게임 프로젝트의 핵심 구조를 재설계하지 않는다.**

필요한 범위만 안전하게 수정한다.

---

## 9. 게임 프로젝트와 Art Studio 작업 공간을 구분한다

예:

```text
Art Studio:
art-studio/projects/game-a/

Game Repository:
~/games/game-a/
```

두 공간의 목적은 다르다.

Art Studio:

- source
- reference
- candidate
- approved
- export preparation
- review material

Game Repository:

- 실제 사용 자산
- scene
- prefab
- resource
- game code
- runtime setting

Handoff는 두 공간 사이의 연결이다.

---

## 10. Handoff 대상은 엔진 하나로 제한되지 않는다

Art Studio는 다음과 같은 환경을 지원할 수 있다.

- Unity
- Godot
- Roblox Studio
- Web
- custom engine
- future engine

이 문서는 특정 엔진을 상위 기준으로 만들지 않는다.

공통 개념을 정의하고,
엔진별 상세 규칙은 필요할 때 별도 guide나 프로젝트 설정으로 분리할 수 있다.

---

## 11. Unity에서 볼 수 있는 것

Unity는 다음과 같은 아트 검증 환경이 될 수 있다.

- sprite import
- Pixels Per Unit
- texture filtering
- compression
- pivot
- material
- shader
- lighting
- 2D light
- post-processing
- VFX
- particle
- animation
- camera
- sorting
- scene composition
- actual scale

하지만 이 문서에서는 특정 Unity 설정값을 기본값으로 만들지 않는다.

---

## 12. Godot에서 볼 수 있는 것

Godot에서는 예를 들어 다음을 확인할 수 있다.

- texture import
- filtering
- sprite
- tilemap
- 2D/3D lighting
- material
- shader
- animation
- resource
- camera
- scene composition

프로젝트가 Godot을 사용한다면 해당 프로젝트 규칙을 따른다.

---

## 13. Roblox Studio에서 볼 수 있는 것

Roblox 프로젝트에서는 특히 다음이 중요할 수 있다.

- world scale
- character scale
- texture appearance
- SurfaceAppearance
- material
- lighting
- camera distance
- mobile readability
- UI asset readability
- world density
- platform-specific rendering

외부 이미지 자체보다 Roblox 안에서 어떻게 보이는지가 더 중요할 수 있다.

---

## 14. Web 환경에서 볼 수 있는 것

Web game 또는 browser asset에서는 다음이 중요할 수 있다.

- image format
- compression
- alpha
- CSS scaling
- canvas rendering
- pixelated filtering
- device pixel ratio
- browser color differences
- loading size
- responsive scale

Web도 단순 파일 목적지가 아니라 실제 표시 환경이다.

---

## 15. Export Format

자산 종류에 따라 export format이 달라질 수 있다.

예:

### 2D

- PNG
- WEBP
- SVG
- sprite sheet
- atlas

### 3D

- FBX
- GLB
- GLTF
- OBJ
- engine-specific resource

### Texture

- PNG
- TGA
- EXR
- compressed texture

### Data

- animation metadata
- atlas metadata
- pivot data
- mask/channel configuration

실제 format은 프로젝트와 엔진 요구에서 결정한다.

---

## 16. Export는 프로젝트별 요구를 따른다

Art Studio 전체에 다음과 같은 기본값을 만들지 않는다.

```text
모든 2D = PNG
모든 3D = FBX
모든 texture = 2048
```

게임마다 다르다.

같은 게임 안에서도 플랫폼별 export가 다를 수 있다.

---

## 17. Multi-platform Export

하나의 Approved source에서 여러 platform export가 나올 수 있다.

예:

```text
approved/source
├─ exports/pc/
├─ exports/mobile/
└─ exports/web/
```

각 platform에서 다음이 달라질 수 있다.

- texture dimensions
- compression
- format
- quality
- atlas
- mesh complexity
- shader
- material

Source의 시각적 의도는 유지하면서 각 환경의 요구를 충족한다.

---

## 18. Export 전 Validation

Export 전에 필요한 기술 검사를 할 수 있다.

예:

- source dimensions
- alpha
- format
- frame count
- texture channels
- naming
- missing files

구체적인 validation 원칙은 `09_ASSET_SPEC_AND_VALIDATION.md`를 따른다.

---

## 19. Export 후 Validation

Export 과정에서 문제가 생길 수 있다.

예:

- dimensions 변화
- aspect ratio 변화
- alpha 손실
- color profile 변화
- channel 손실
- compression artifact
- frame 누락
- crop 오류

따라서 필요한 경우 source와 export를 비교한다.

---

## 20. Import는 단순 성공 여부만 보지 않는다

파일이 엔진에 import되었다고 작업이 끝난 것은 아니다.

다음이 잘못될 수 있다.

- scale
- filtering
- pivot
- sprite slicing
- material
- shader
- texture type
- color space
- transparency
- compression
- animation mapping

Import 성공:

```text
file loaded
```

와:

```text
game art displayed correctly
```

는 다르다.

---

## 21. Import Setting은 아트의 일부가 될 수 있다

특히 다음은 시각 결과에 큰 영향을 줄 수 있다.

- nearest / bilinear filtering
- texture compression
- mipmap
- color space
- sprite mode
- alpha handling
- normal map interpretation
- material shader

따라서 import setting이 단순 개발 설정이라고만 보지 않는다.

아트가 실제로 어떻게 보이는지에 영향을 준다면
Art Studio가 검증해야 할 수 있다.

---

## 22. Scale

실제 게임 안에서의 크기는 매우 중요하다.

예:

```text
source:
캐릭터 디자인은 좋음

runtime:
너무 작아서 얼굴과 무기가 보이지 않음
```

이 경우 source가 나쁜 것이 아니라 scale 또는 camera 문제일 수 있다.

확인할 수 있는 것:

- world scale
- screen occupancy
- character height
- icon display size
- UI scale
- zoom range

---

## 23. Camera

같은 자산도 카메라에 따라 완전히 다르게 보인다.

확인할 수 있는 것:

- first-person
- third-person
- top-down
- side view
- isometric
- orthographic
- perspective
- FOV
- camera distance
- zoom
- framing

Art Direction은 카메라에 따른 디자인 방향을 정의할 수 있고,
Handoff에서는 실제 카메라에서 그 방향이 유지되는지 확인한다.

---

## 24. Pixel Art Scale

픽셀 아트 프로젝트에서는 다음 문제가 중요할 수 있다.

- integer scaling
- nearest filtering
- pixel snapping
- subpixel movement
- camera scaling
- render resolution
- UI scaling

Source sprite가 완벽해도 엔진에서 흐려질 수 있다.

따라서 실제 runtime pixel result를 확인한다.

---

## 25. Pivot과 Anchor

Pivot이 잘못되면:

- 캐릭터 발이 흔들림
- 무기 회전이 이상함
- animation이 튐
- UI 정렬이 어긋남

문제가 생길 수 있다.

Pivot은 기술적 설정이지만
움직임과 형태 인상에 영향을 줄 수 있다.

---

## 26. Sprite Slicing

Sprite sheet에서는 다음을 확인할 수 있다.

- frame dimensions
- slicing
- order
- spacing
- pivot
- missing frame

Validation 결과와 engine import 결과가 일치하는지 본다.

---

## 27. Atlas

Atlas 사용 시 다음을 확인할 수 있다.

- packing
- padding
- bleed
- filtering
- unexpected compression
- UV issue

특히 작은 sprite와 UI asset에서
atlas bleed가 시각 문제를 만들 수 있다.

---

## 28. Material

3D 또는 shader-based 2D에서는 material이 최종 인상에 큰 영향을 준다.

예:

- roughness
- metallic
- transparency
- emission
- tint
- normal intensity
- shader parameters

Approved texture가 좋아도 material 설정이 잘못되면 전혀 다른 결과가 나올 수 있다.

---

## 29. Shader

Shader는 스타일 자체의 일부가 될 수 있다.

예:

- outline
- toon shading
- dissolve
- pixelation
- palette swap
- rim light
- distortion
- water
- foliage
- lighting model

Asset source와 shader의 책임 범위를 구분한다.

---

## 30. Lighting

Runtime에서 다음을 확인한다.

- key light
- ambient
- shadow
- rim light
- 2D light
- point light
- directional light
- baked light
- dynamic light

특히 다음 질문이 중요하다.

> **이 게임의 빛은 source asset이 만드는가, engine이 만드는가, 둘이 나누어 만드는가?**

Art Direction에서 정한 역할 분담이 실제 엔진에서 유지되는지 본다.

---

## 31. Post-processing

다음이 최종 화면에 영향을 줄 수 있다.

- bloom
- color grading
- fog
- vignette
- depth of field
- motion blur
- exposure
- contrast
- saturation

Post-processing 때문에 source의 색이나 가독성이 무너질 수 있다.

---

## 32. VFX

VFX는 다음 문제를 만들 수 있다.

- 캐릭터 가림
- 과도한 brightness
- 화면 우선순위 붕괴
- team color 혼동
- attack readability 저하

따라서 중요한 전투 자산은 VFX가 포함된 실제 장면에서 볼 수 있다.

---

## 33. UI와 함께 본다

게임 월드 자산만 따로 볼 때는 정상인데
UI와 함께 보면 문제일 수 있다.

예:

- character status UI가 캐릭터 얼굴을 가림
- icon이 world보다 너무 강함
- HUD color와 faction color 충돌
- subtitle이 중요한 환경 요소를 가림

필요하면 실제 HUD가 포함된 화면에서 검토한다.

---

## 34. Environment와 함께 본다

캐릭터는 실제 배경과 함께 봐야 한다.

예:

```text
캐릭터 단독:
잘 읽힘

실제 배경:
묻힘
```

원인은:

- character
- environment
- lighting
- camera

중 하나 또는 여러 개일 수 있다.

---

## 35. Animation

정지 이미지가 좋아도 animation에서 형태가 무너질 수 있다.

확인할 수 있는 것:

- pose readability
- frame timing
- pivot consistency
- scale
- silhouette
- foot sliding
- loop
- transition

Animation의 기술 규격은 별도 Spec과 Validation에서 가져올 수 있다.

---

## 36. 3D Animation과 Rig

3D asset에서는 필요에 따라 다음을 확인한다.

- rig mapping
- scale
- root motion
- skinning
- deformation
- bone orientation
- animation compatibility

구체적인 rigging guide는 별도 문서로 분리할 수 있다.

---

## 37. Runtime Screenshot

실제 게임 screenshot은 매우 중요한 Review 자료다.

가능하면 다음 조건을 포함할 수 있다.

- typical camera
- typical background
- actual lighting
- UI
- VFX
- common gameplay distance

Screenshot은 단순 홍보 이미지가 아니라
Art Studio의 검증 자료가 될 수 있다.

---

## 38. Screenshot 비교

예:

```text
before
vs
after
```

또는:

```text
Candidate A runtime
Candidate B runtime
```

같은 비교가 유용할 수 있다.

특히 source 이미지에서는 보이지 않던 차이가
runtime에서는 크게 나타날 수 있다.

---

## 39. Actual Gameplay Capture

정지 화면만으로 부족하면 gameplay capture를 볼 수 있다.

예:

- 빠른 움직임
- camera shake
- animation
- particle
- multiplayer density
- UI transitions

특히 action game에서는 매우 중요할 수 있다.

---

## 40. Runtime Review의 목적

Runtime Review는 다음 질문에 답한다.

> **이 자산은 실제 게임에서 의도한 역할을 수행하는가?**

예:

- 플레이어가 알아볼 수 있는가?
- 중요한 정보가 읽히는가?
- Art Direction의 인상이 유지되는가?
- 다른 자산과 조화되는가?
- engine effect가 source를 망치지 않는가?
- scale이 적절한가?

---

## 41. Source 문제

Runtime에서 문제가 보였을 때 source 자체의 문제일 수 있다.

예:

- silhouette 약함
- proportion 문제
- color hierarchy 문제
- detail 과다
- texture 과다
- pose 문제

이 경우 source 수정 Candidate를 만들 수 있다.

---

## 42. Export 문제

Source는 정상인데 export 과정에서 문제일 수 있다.

예:

- resize blur
- alpha loss
- compression
- crop
- channel loss
- incorrect atlas

이 경우 source approval을 유지하고
export만 수정할 수 있다.

---

## 43. Import 문제

예:

- wrong filtering
- wrong sprite type
- wrong normal map interpretation
- color space mismatch
- wrong pivot
- wrong scale

이 경우 source나 export를 다시 만들 필요가 없을 수 있다.

---

## 44. Engine Setting 문제

예:

- lighting
- shader
- material
- fog
- post-processing
- camera

이 경우 Art Studio는 자산 자체를 수정하기 전에
runtime setting을 검토한다.

---

## 45. Environment 문제

예:

- background contrast too high
- excessive detail
- same hue/value as character
- landmarks hidden

캐릭터만 수정하는 것이 최선이 아닐 수 있다.

---

## 46. 문제 위치를 잘못 수정하지 않는다

예:

```text
문제:
캐릭터가 흐림

실제 원인:
bilinear filtering

잘못된 대응:
캐릭터 outline을 더 두껍게 다시 그림
```

이런 수정은 source를 불필요하게 왜곡한다.

먼저 원인을 찾는다.

---

## 47. Temporary Runtime Export

최종 승인 전에 임시 export를 만들어 테스트할 수 있다.

예:

```text
Candidate
↓
temporary export
↓
runtime test
↓
review
```

이 경우 temporary export를 공식 final export로 혼동하지 않는다.

---

## 48. Runtime Test가 Approval 전에 들어갈 수 있다

일부 자산은 실제 게임에서 봐야 승인할 수 있다.

예:

- character sprite
- VFX
- UI icon
- tile
- lighting-dependent asset

이 경우:

```text
Candidate
↓
Temporary Handoff
↓
Runtime Review
↓
Approved
```

가 정상적이다.

---

## 49. Runtime Test가 Approval 후에도 들어갈 수 있다

다른 경우에는 먼저 source 디자인을 승인하고
그다음 engine에서 검증할 수 있다.

```text
Candidate
↓
Approved Source
↓
Export
↓
Runtime Review
↓
필요 시 Revision
```

둘 다 가능하다.

---

## 50. Handoff의 깊이는 자산마다 다르다

### 단순 UI Icon

```text
approved PNG
↓
import
↓
display check
```

정도로 충분할 수 있다.

### Pixel Character

```text
approved sprite
↓
sheet export
↓
import
↓
filtering / scale / pivot
↓
animation test
↓
runtime screenshot
```

### 3D Character

```text
approved model
↓
export
↓
texture/material
↓
rig/animation
↓
lighting
↓
camera
↓
runtime review
```

모든 자산에 같은 handoff 절차를 강제하지 않는다.

---

## 51. 엔진별 세부 Guide

필요하면 향후 다음과 같은 별도 guide를 만들 수 있다.

```text
UNITY_ART_HANDOFF.md
GODOT_ART_HANDOFF.md
ROBLOX_ART_HANDOFF.md
WEB_ART_HANDOFF.md
```

하지만 이 문서에서는 공통 원칙만 정의한다.

특정 엔진 guide가 없어도 기본 Handoff 철학은 유지되어야 한다.

---

## 52. Engine-specific Guide는 상위 규칙을 바꾸지 않는다

예:

Unity Guide가 있다고 해서:

> 모든 프로젝트는 Unity 방식으로 asset을 준비한다.

가 되어서는 안 된다.

Engine guide는 해당 엔진에서 공통 원칙을 구현하는 하위 문서다.

---

## 53. Import Preset

반복 프로젝트에서는 import preset을 사용할 수 있다.

예:

- pixel sprite preset
- UI texture preset
- normal map preset
- mobile texture preset

Preset은 반복 오류를 줄일 수 있다.

하지만 잘못된 preset을 모든 자산에 강제하지 않는다.

---

## 54. Preset은 Art Direction을 결정하지 않는다

예:

```text
preset:
nearest filtering
```

이 존재한다고 해서
모든 프로젝트를 pixel art로 만들지 않는다.

Preset은 이미 결정된 요구를 안정적으로 적용하는 도구다.

---

## 55. Automated Export

다음은 자동화할 수 있다.

- resize
- format conversion
- atlas
- sprite sheet
- texture compression
- naming
- copy to game repository
- metadata generation

반복량이 커질수록 가치가 높다.

---

## 56. Automated Import

환경에 따라 import 자동화도 가능할 수 있다.

예:

- asset copy
- preset apply
- resource generation
- prefab update
- metadata update

하지만 자동화가 게임 프로젝트를 임의로 재구성하지 않도록 한다.

---

## 57. 자동 Handoff의 위험

다음 문제를 주의한다.

- wrong project path
- overwrite
- stale export
- wrong platform
- wrong import preset
- unintended code modification
- approved source mismatch

자동화가 강해질수록 안전한 대상 확인이 중요하다.

---

## 58. Overwrite

기존 게임 자산을 덮어쓸 때는 영향을 고려한다.

특히:

- currently used asset
- manually edited asset
- engine-generated metadata
- prefab reference
- shared texture

등을 무심코 파괴하지 않는다.

---

## 59. Original Backup

필요하면 기존 게임 자산을 교체하기 전
버전 관리 또는 backup을 확인한다.

Git이 있다면 history로 되돌릴 수 있을 수 있다.

하지만 version control이 있다고
무조건 안전하게 overwrite할 수 있다고 가정하지 않는다.

---

## 60. Handoff와 Version Control

Handoff 결과가 실제 게임 repository에 들어가면
버전 관리 대상이 될 수 있다.

하지만 다음 정책은 이 문서에서 고정하지 않는다.

- commit strategy
- LFS
- branch
- PR
- binary storage

게임 프로젝트의 기존 규칙을 따른다.

---

## 61. Source of Truth

가능하면 현재 공식 source가 무엇인지 분명해야 한다.

예:

```text
Art Studio approved source
=
hero_master.psd
```

Game Repository의 PNG는 derived asset일 수 있다.

반대로 프로젝트 구조에 따라
게임 repository의 source file이 공식 source일 수도 있다.

핵심은 혼동하지 않는 것이다.

---

## 62. 두 개의 Source of Truth를 만들지 않는다

예:

```text
art-studio approved/hero.png

game-repo Assets/hero_source.png
```

둘을 각각 수정하면 drift가 생긴다.

가능하면 한쪽을 공식 source로 정하고
다른 쪽은 derived 또는 synchronized copy로 본다.

---

## 63. Sync

프로젝트 규모가 커지면
Art Studio와 Game Repository 사이 sync가 필요할 수 있다.

예:

```text
approved
↓
export script
↓
game repository
```

Sync 자체를 거대한 시스템으로 만들 필요는 없다.

반복 오류가 실제로 생길 때 자동화한다.

---

## 64. Export Metadata

필요하면 다음을 기록할 수 있다.

- source file
- export target
- platform
- tool
- version
- date
- settings
- checksum

모든 작은 자산에 metadata를 강제하지 않는다.

재현성이 중요한 자산이나 batch에서 유용할 수 있다.

---

## 65. Engine Asset Metadata

엔진이 생성하는 metadata가 있을 수 있다.

예:

- Unity `.meta`
- Godot import data
- Roblox asset IDs
- web manifest entries

이 파일과 source asset의 관계를 이해한다.

엔진 metadata를 source art로 취급하지 않는다.

---

## 66. Asset ID와 Engine ID

프로젝트 Asset ID와 engine asset ID는 다를 수 있다.

예:

```text
Art Studio:
CHR_001

Roblox:
asset id 123456

Unity:
Assets/Characters/Hero.png
```

필요하면 연결 정보를 기록한다.

하지만 모든 프로젝트에 복잡한 registry를 만들지 않는다.

---

## 67. Roblox Asset ID

Roblox에서는 업로드된 asset이 외부 ID를 가질 수 있다.

이 경우 다음 관계를 추적할 수 있다.

```text
Approved Source
↓
Uploaded Asset
↓
Roblox Asset ID
↓
Runtime Object
```

필요하면 Manifest나 project-specific record에 연결한다.

---

## 68. Web URL Asset

Web 환경에서는 CDN 또는 asset URL이 있을 수 있다.

예:

```text
approved source
↓
web export
↓
public asset path
```

URL 자체가 공식 source가 아니다.

---

## 69. Prefab / Resource / Scene

엔진에서 최종 자산은 단순 이미지 파일보다 높은 수준의 객체일 수 있다.

예:

Unity:

```text
texture
↓
material
↓
prefab
```

Godot:

```text
texture
↓
resource
↓
scene
```

Roblox:

```text
texture / mesh
↓
instance
↓
model
```

Art Studio는 필요하면 이 구조까지 검증할 수 있다.

---

## 70. Composition Asset

일부 “자산”은 여러 source의 조합일 수 있다.

예:

- character prefab
- VFX prefab
- UI widget visual
- building set
- animated prop

이 경우 Approved source 하나가 아니라
여러 승인 요소와 runtime setting이 결합될 수 있다.

---

## 71. Runtime Assembly

최종 시각 결과가 런타임 조합으로 만들어지는 경우
그 조합 자체가 검토 대상이 될 수 있다.

예:

```text
character sprite
+
outline shader
+
team color
+
shadow
+
VFX
```

이 조합이 실제 “게임에서 보이는 캐릭터”다.

---

## 72. Runtime Variant

같은 source가 여러 상태로 보일 수 있다.

예:

- team color
- damaged
- poisoned
- selected
- stealth
- night lighting

이런 variant가 중요한 경우 실제 runtime에서 확인한다.

---

## 73. Dynamic Material

Material parameter가 runtime에서 바뀌는 경우
정적 screenshot 하나만으로 충분하지 않을 수 있다.

예:

- damage flash
- dissolve
- highlight
- faction tint

필요하면 여러 상태를 확인한다.

---

## 74. Lighting Variant

낮/밤, 실내/실외 등 조명이 달라질 수 있다.

같은 asset이 여러 lighting 조건에서
일관되게 읽히는지 확인할 수 있다.

모든 조건에서 똑같이 보여야 한다는 뜻은 아니다.

게임플레이 요구를 충족하는지 본다.

---

## 75. Camera Variant

Zoom이 있는 게임에서는
여러 거리에서 확인할 수 있다.

예:

```text
far
mid
close
```

Far에서는 silhouette,
Close에서는 detail이 중요할 수 있다.

---

## 76. Device Variant

멀티플랫폼 프로젝트에서는:

- desktop
- mobile
- tablet
- console

에서 다르게 보일 수 있다.

특히 UI, icon, small sprite는 실제 device scale 영향을 받을 수 있다.

---

## 77. Performance와 Art

일부 아트는 성능 문제를 만들 수 있다.

예:

- texture memory
- shader cost
- particle count
- mesh complexity
- overdraw

이 문제는 기술적이지만
아트 결과에 영향을 줄 수 있다.

---

## 78. Performance 때문에 디자인을 임의로 바꾸지 않는다

예:

```text
particle이 비싸므로
효과를 절반으로 줄였다.
```

가 시각적 방향을 크게 바꾸는 경우
디렉터 판단이 필요할 수 있다.

먼저:

- optimization
- batching
- shader change
- texture change
- LOD

등 다른 해결책을 검토할 수 있다.

---

## 79. LOD

3D 프로젝트에서는 LOD가 필요할 수 있다.

확인할 수 있는 것:

- distance transition
- silhouette 유지
- texture downgrade
- pop
- material change

LOD의 기술 규격은 프로젝트별로 다르다.

---

## 80. Mipmap

Texture mipmap은 먼 거리에서 품질과 성능에 영향을 준다.

픽셀 아트에서는 오히려 원하지 않을 수 있다.

프로젝트 요구에 따라 결정한다.

---

## 81. Compression Variant

플랫폼별로 compression이 다를 수 있다.

실제 runtime에서:

- color shift
- banding
- alpha artifact
- blur

가 생기는지 볼 수 있다.

---

## 82. Color Space

sRGB / linear 등 color space가
게임 화면 결과에 영향을 줄 수 있다.

Source에서는 정상인데 engine에서 색이 달라진다면
color space 문제를 확인할 수 있다.

---

## 83. Transparency

투명 자산에서는 다음 문제가 생길 수 있다.

- sorting
- premultiply
- halo
- blending
- depth

파일 alpha가 정상이어도 runtime에서 문제가 생길 수 있다.

---

## 84. Sorting / Layering

2D 게임에서는 다음을 확인할 수 있다.

- character behind wrong object
- VFX order
- foreground/background
- UI overlap

이 문제는 art source 자체의 문제가 아닐 수 있다.

---

## 85. Depth

3D 또는 2.5D에서는 depth 관계가 시각적 인상에 영향을 준다.

예:

- character clipping
- environment occlusion
- depth fog
- perspective

Runtime에서 확인한다.

---

## 86. Shadow

Shadow는 캐릭터의 접지감과 가독성에 영향을 준다.

예:

- blob shadow
- dynamic shadow
- baked shadow
- contact shadow

Source asset에 그려진 shadow와 engine shadow가 중복될 수 있다.

---

## 87. Source Lighting과 Engine Lighting 충돌

예:

```text
sprite에 강한 오른쪽 highlight
+
engine light는 왼쪽
```

이면 부자연스러울 수 있다.

이런 문제는 source와 engine 책임 분담을 다시 보게 할 수 있다.

---

## 88. Baked Effect 중복

예:

- sprite에 bloom-like glow
- engine bloom 추가

결과가 과해질 수 있다.

VFX나 shading을 source와 engine에 중복해서 넣지 않는지 본다.

---

## 89. Screenshot Baseline

프로젝트가 성숙하면
대표 runtime screenshot을 기준으로 사용할 수 있다.

예:

```text
reviews/visual-target-01.png
```

새 Handoff 결과를 이 화면과 비교할 수 있다.

---

## 90. Representative Scene

검증용 대표 scene을 둘 수 있다.

예:

- daylight
- night
- combat
- UI-heavy
- crowded scene

모든 프로젝트에 별도 test scene을 강제하지 않는다.

반복 검증 가치가 있을 때 만든다.

---

## 91. Test Harness

대규모 production에서는
아트 검증용 scene 또는 sandbox를 만들 수 있다.

예:

```text
all characters lineup
all tiles repeat
all VFX
lighting variants
```

이는 Art Studio의 runtime validation 효율을 높일 수 있다.

하지만 작은 프로젝트에서 필수는 아니다.

---

## 92. Engine을 Art Tool로 사용할 수 있다

Engine은 결과를 “받는 곳”만이 아니다.

다음 작업에 활용할 수 있다.

- lighting exploration
- camera test
- shader development
- material tuning
- VFX
- environment composition
- screenshot generation

어떤 프로젝트에서는 스타일의 일부가 엔진에서 만들어진다.

---

## 93. Engine에서 만들어진 결과도 Art Direction의 일부가 될 수 있다

예:

```text
source sprite:
단순 shading

engine:
fog + light + bloom
```

이 조합이 실제 프로젝트의 스타일일 수 있다.

따라서 Approved source만 보고 Art Direction을 완전히 판단하지 않는다.

---

## 94. Engine-specific Art Source

일부 자산은 애초에 엔진 내부에서 만들어질 수 있다.

예:

- shader
- particle system
- material
- procedural effect
- lighting setup

이 경우 “source”가 PNG 파일이 아닐 수 있다.

Art Studio는 파일 형식보다 시각 결과와 수정 가능한 source의 의미를 본다.

---

## 95. Runtime-generated Asset

일부 시각 요소는 runtime에서 생성될 수 있다.

예:

- procedural texture
- dynamic decal
- generated map
- dynamic UI effect

이 경우 Handoff는 코드/설정과 시각 검증을 함께 포함할 수 있다.

하지만 게임 로직 전체를 Art Studio가 흡수하지 않는다.

---

## 96. 아트 목적의 최소 코드 수정

필요하면 아트 검증을 위해
작은 코드 수정이 필요할 수 있다.

예:

- test scene
- asset swap
- debug toggle
- screenshot mode
- camera position

사용자의 지시나 기존 프로젝트 규칙 범위 안에서 수행한다.

게임 핵심 로직을 아트 작업이라는 이유로 재설계하지 않는다.

---

## 97. Runtime Screenshot 자동화

반복 검증이 많다면
다음 자동화를 고려할 수 있다.

- fixed camera screenshot
- asset lineup
- lighting variant capture
- before/after capture

자동화는 비교 편의를 위한 수단이다.

---

## 98. Batch Handoff

대량 자산에서는:

```text
Approved assets
↓
batch export
↓
validation
↓
game repository
↓
spot runtime review
```

가 유용할 수 있다.

전체 방향을 먼저 샘플로 검증한 후 batch를 수행하는 편이 안전하다.

---

## 99. Spot Runtime Review

대량 자산에서는 다음을 우선 볼 수 있다.

- 대표 자산
- 가장 복잡한 자산
- 가장 작은 자산
- warning이 있는 자산
- 새로운 category
- 기존 baseline과 차이가 큰 자산

모든 파일을 동일 깊이로 보는 것보다 효율적일 수 있다.

---

## 100. Handoff 실패

다음과 같은 문제가 있을 수 있다.

- export 실패
- import 실패
- missing texture
- broken material
- wrong scale
- wrong pivot
- runtime unreadable
- platform issue

실패를 하나의 “아트 실패”로 묶지 않는다.

문제 위치를 찾는다.

---

## 101. Handoff 실패 후 대응

예:

```text
문제:
캐릭터가 너무 흐림

가능 원인:
- source resolution
- export resize
- bilinear filtering
- camera scale
```

각 원인을 차례로 확인한다.

가장 위 단계부터 무조건 다시 만들지 않는다.

---

## 102. Rollback

새 export나 import가 문제를 만들면
이전 정상 상태로 돌아갈 수 있어야 한다.

방법:

- version control
- previous export
- previous import setting
- previous prefab/resource

구체적인 rollback 시스템은 프로젝트에 따라 다르다.

---

## 103. Approved Source 변경 시 Export 갱신

Source가 새로 승인되면
기존 export가 stale해질 수 있다.

예:

```text
hero_v2 approved
↓
hero_v1 unity export stale
```

필요하면 stale export를 탐지하거나 갱신한다.

---

## 104. Export Staleness

다음 정보를 이용할 수 있다.

- timestamp
- hash
- source version
- manifest
- metadata

하지만 작은 프로젝트에 복잡한 dependency system을 강제하지 않는다.

---

## 105. Engine Asset Staleness

게임 repository에 오래된 asset이 남아 있을 수 있다.

예:

```text
Art Studio approved:
hero_v3

Game runtime:
hero_v2
```

이 차이를 확인할 수 있어야 한다.

---

## 106. Manifest와 Handoff

향후 `ASSET_MANIFEST.md`에는 필요에 따라 다음이 있을 수 있다.

```text
Asset:
Hero

Status:
Approved

Unity:
Exported

Roblox:
Pending
```

하지만 Manifest에 engine import log 전체를 넣지 않는다.

---

## 107. Asset Brief와 Handoff

Asset Brief에는 필요한 경우 다음이 포함될 수 있다.

- target engine
- display context
- platform constraint
- required variant

Handoff는 그 요구를 실제 runtime으로 연결한다.

---

## 108. Review Log와 Handoff

다음과 같은 결정은 Review Log에 남길 가치가 있을 수 있다.

예:

```text
캐릭터 outline을 source에서 제거하고
engine shader에서 처리하기로 결정.
```

또는:

```text
모바일에서 48px sprite가 너무 작아
64px 기준으로 변경.
```

단순 import fix는 Review Log에 남길 필요가 없다.

---

## 109. Art Direction과 Handoff

Art Direction에는 다음과 같은 내용이 있을 수 있다.

```text
조명은 엔진 중심.
```

Handoff에서는 실제로:

- source shading 절제
- engine light
- fog
- bloom

가 의도대로 작동하는지 확인한다.

---

## 110. Style Spec과 Handoff

Style Spec의 규칙 중 일부는 engine에서 실현된다.

예:

```text
filtering = nearest
```

```text
texture max = 1024 mobile
```

```text
pivot = bottom center
```

Handoff는 이런 규칙을 실제 엔진 적용으로 연결한다.

---

## 111. Validation과 Handoff

Handoff 전후에 validation을 사용할 수 있다.

예:

```text
source validation
↓
export
↓
export validation
↓
import
↓
runtime validation
```

모든 단계에 validator를 강제하지 않는다.

문제와 반복량에 맞게 적용한다.

---

## 112. Review & Approval과 Handoff

Runtime screenshot은 Art Review input이 될 수 있다.

예:

```text
Candidate A source
Candidate B source
```

보다:

```text
Candidate A in game
Candidate B in game
```

가 더 의미 있는 경우가 있다.

---

## 113. Lifecycle과 Handoff

기본 관계:

```text
APPROVED SOURCE
↓
EXPORT
```

하지만 Runtime Review에서 문제가 생기면
다시 Candidate 단계로 돌아갈 수 있다.

상태 의미는 `06_ASSET_LIFECYCLE.md`를 따른다.

---

## 114. Learning & Reuse와 Handoff

여러 프로젝트에서 반복되는 handoff 문제는
Studio 공통 기술로 축적할 수 있다.

예:

- Unity pixel import helper
- Godot atlas exporter
- Roblox texture uploader
- Web image optimizer
- screenshot capture tool

반면 특정 게임의 material/shader/style 값은
프로젝트에 남긴다.

---

## 115. Handoff 자동화의 공통화

공통화할 가치가 있는 것은 예를 들어:

- format converter
- resize helper
- sprite sheet exporter
- texture channel packer
- engine copy helper
- validation hook
- screenshot helper

다.

실제 반복이 확인된 뒤 공통화한다.

---

## 116. Project-specific Handoff

프로젝트에 남아야 하는 것은 예를 들어:

- 특정 prefab path
- 특정 material
- 특정 shader parameter
- 특정 Roblox object structure
- 특정 scene
- 특정 project export path

등이다.

이를 Studio 전체 기본값으로 만들지 않는다.

---

## 117. Tool 교체

Engine 또는 exporter가 바뀔 수 있다.

예:

```text
Unity → Godot
```

이 경우 Art Studio의 상위 구조가 무너지지 않아야 한다.

Source와 Art Direction은 가능한 한 엔진에 종속되지 않게 유지한다.

---

## 118. Engine 변경으로 Source가 바뀔 수도 있다

완전히 독립적일 수만은 없다.

예:

- shader 지원 차이
- texture constraint
- 2D lighting capability
- platform limit

때문에 source 또는 Style Spec이 변경될 수 있다.

이 경우 변화가 기술적 요구인지
시각적 방향 변화인지 구분한다.

---

## 119. Engine Lock-in을 피한다

Studio 공통 문서에:

```text
모든 texture는 Unity 규칙
```

같은 기본값을 넣지 않는다.

Engine-specific knowledge는 별도 능력으로 축적한다.

---

## 120. Source Asset의 Engine Neutrality

가능하다면 Approved source는
특정 엔진에 지나치게 묶이지 않는 형태로 보존할 수 있다.

예:

- master texture
- editable PSD
- Blender source
- high-quality sprite source

그다음 엔진별 export를 파생한다.

항상 가능한 것은 아니다.

---

## 121. Runtime-only Style

어떤 프로젝트에서는 스타일의 중요한 부분이
engine-only일 수 있다.

예:

- shader outline
- color grading
- dynamic shadow
- fog
- procedural VFX

이 경우 Art Direction과 Handoff 문서가
source 파일만으로 프로젝트를 설명하려 하지 않는다.

---

## 122. Screenshot을 Approved Reference로 사용할 수 있다

디렉터가 특정 runtime screenshot을
대표 시각 기준으로 채택할 수 있다.

이 경우 새 자산은 source뿐 아니라
그 화면과도 비교할 수 있다.

---

## 123. 최종 Handoff의 의미

Handoff 완료는 단순히:

```text
파일 복사 완료
```

가 아니다.

프로젝트에 따라 다음 수준 중 하나일 수 있다.

### Export Ready

엔진용 파일 준비 완료.

### Imported

게임 프로젝트에 import 완료.

### Integrated

scene / prefab / resource에 연결 완료.

### Runtime Verified

실제 게임 화면에서 확인 완료.

모든 프로젝트에 이 상태들을 공식 enum으로 만들 필요는 없다.

---

## 124. “완료”의 범위를 명확히 한다

예:

```text
이번 요청:
Unity에서 실제 게임 화면까지 확인
```

이라면 Export만 하고 끝내면 부족하다.

반대로:

```text
이번 요청:
Roblox용 texture export만 준비
```

라면 runtime integration까지 필요하지 않을 수 있다.

현재 요청의 완료 범위를 이해한다.

---

## 125. Handoff 깊이를 작업 목표에 맞춘다

작은 작업:

```text
approved
→ export
```

대표 자산:

```text
approved
→ export
→ import
→ runtime
→ screenshot
→ review
```

복잡한 자산:

```text
approved source
→ multiple exports
→ material
→ animation
→ scene
→ runtime variants
→ review
```

필요한 만큼만 수행한다.

---

## 126. 디렉터가 엔진 세부사항을 기억할 필요는 없다

디렉터는 다음처럼 요청할 수 있어야 한다.

> 실제 게임에 넣어봐.

Art Studio는 필요한 경우:

- export
- import
- scale
- material
- camera
- screenshot

을 처리하거나 준비한다.

디렉터가 매번 import 옵션을 직접 지정해야 하는 시스템을 목표로 하지 않는다.

---

## 127. 중요한 선택은 설명할 수 있다

예:

> 이 프로젝트는 픽셀 스프라이트라 bilinear filtering을 끄고 nearest로 확인했다.

또는:

> 이 캐릭터는 엔진 조명이 스타일의 핵심이라 source에 강한 baked highlight를 추가하지 않았다.

결과에 중요한 설정은 짧게 설명할 수 있다.

---

## 128. Handoff를 과도한 배포 시스템으로 만들지 않는다

이 문서의 목적은:

- CI/CD
- release pipeline
- build system
- deployment system

을 설계하는 것이 아니다.

게임 개발 배포는 별도 영역이다.

Art Studio는 **아트 자산을 실제 게임 환경에서 사용할 수 있고 검증 가능한 상태로 만드는 데** 집중한다.

---

## 129. 게임 코드를 흡수하지 않는다

필요한 아트 integration은 지원할 수 있지만
Art Studio가 다음을 기본 책임으로 가져가지 않는다.

- gameplay system
- networking
- save system
- server
- AI behavior
- economy
- core architecture

Handoff 때문에 게임 개발 프로젝트 전체를 Art Studio로 끌어오지 않는다.

---

## 130. 아트 문제와 게임 로직 문제를 구분한다

예:

```text
캐릭터가 공격할 때 잘못된 sprite가 표시됨
```

이것이:

- asset mapping 문제인지
- animation controller 문제인지
- gameplay state bug인지

구분한다.

Art Studio가 해결할 수 있는 범위를 판단한다.

---

## 131. External Team Handoff

다른 개발자가 엔진 integration을 담당할 수도 있다.

이 경우 Art Studio는 다음을 제공할 수 있다.

- Approved source
- export
- technical requirements
- preview
- expected appearance
- reference screenshot
- known constraints

직접 engine project를 수정하지 않아도 Handoff는 가능하다.

---

## 132. Handoff Package

필요하면 다음을 묶을 수 있다.

```text
asset
preview
spec
notes
```

하지만 모든 작업에 formal package를 강제하지 않는다.

---

## 133. 전달 메모

복잡한 자산에서는 짧은 메모가 유용할 수 있다.

예:

```text
Hero Sprite

- nearest filtering
- bottom-center pivot
- engine outline shader 사용
- source baked outline 없음
```

이런 정보는 engine developer의 실수를 줄일 수 있다.

---

## 134. Handoff Checklist를 남발하지 않는다

모든 자산에 수십 항목의 checklist를 만들지 않는다.

반복적으로 필요한 핵심 사항만 사용한다.

---

## 135. 대표 자산의 Handoff는 더 깊게 기록할 수 있다

주인공, 대표 환경, 핵심 VFX처럼
프로젝트의 기준이 되는 자산은:

- source
- export
- material
- screenshot
- important settings

을 더 잘 보존할 가치가 있다.

---

## 136. 게임 화면에서 실패하면 돌아간다

흐름은 일방향이 아니다.

```text
Approved
↓
Export
↓
Runtime
↓
Review
↓
Revision
↓
New Approved
↓
New Export
```

이 왕복이 정상적인 게임 아트 제작 과정이다.

---

## 137. 같은 문제를 반복하지 않는다

Runtime에서 반복적으로 같은 문제가 생기면
다음 중 하나를 개선할 수 있다.

- Style Spec
- exporter
- import preset
- validation
- engine guide
- test scene

반복되는 기술적 문제는 Studio 노하우로 축적할 수 있다.

---

## 138. Handoff 문제를 Art Direction으로 잘못 일반화하지 않는다

예:

```text
Unity filtering 문제
```

를:

```text
이 프로젝트 sprite 스타일이 잘못됐다.
```

로 해석하지 않는다.

기술 문제와 시각 방향 문제를 구분한다.

---

## 139. Engine에서 더 좋은 결과가 나오면 Art Direction이 발전할 수 있다

반대로 runtime 실험이 새로운 시각 가능성을 보여줄 수도 있다.

예:

```text
engine fog + low contrast background
```

가 매우 좋은 결과를 만들었다면
디렉터가 이를 프로젝트 방향으로 채택할 수 있다.

이 경우 Art Direction이 업데이트될 수 있다.

---

## 140. Engine Experiment와 Production Setting을 구분한다

실험 설정:

```text
temporary bloom 2.0
```

을 바로 공식 프로젝트 설정으로 만들지 않는다.

좋은 결과가 확인되고 디렉터가 채택하면
프로젝트 기준으로 승격할 수 있다.

---

## 141. Handoff에서 가장 중요한 질문

복잡할 때 다음 질문으로 돌아간다.

### 1. 공식 source는 무엇인가?

현재 무엇이 Approved인가?

### 2. 어떤 환경에서 사용되는가?

엔진, 플랫폼, 카메라, 실제 표시 조건은 무엇인가?

### 3. 어떤 파생 처리가 필요한가?

Export, resize, material, shader, animation 등 무엇이 필요한가?

### 4. 실제 게임에서 의도대로 보이는가?

Runtime에서 Art Direction과 gameplay 요구를 충족하는가?

### 5. 문제가 있다면 어디에 있는가?

Source / Export / Import / Engine / Camera / Environment 중 어디를 수정해야 하는가?

---

## 142. 다른 문서와의 관계

### `03_PROJECT_STRUCTURE.md`

Approved source와 Export의 구조적 분리를 정의한다.

이 문서는 그 사이의 실제 전달과 검증을 정의한다.

---

### `04_ART_DIRECTION_SYSTEM.md`

카메라, 조명, VFX, UI, 실제 게임 화면이 스타일에 기여할 수 있음을 정의한다.

이 문서는 그것을 엔진에서 검증한다.

---

### `05_TOOL_ROLES.md`

Unity, Godot, Roblox Studio 등을 runtime validation 환경으로 정의한다.

이 문서는 그 역할을 실제 Handoff 흐름에 적용한다.

---

### `06_ASSET_LIFECYCLE.md`

Approved source와 Export 상태의 의미를 정의한다.

---

### `07_GENERATION_WORKFLOW.md`

필요할 경우 runtime test를 제작 과정에 포함한다.

---

### `08_REVIEW_AND_APPROVAL.md`

Runtime screenshot과 gameplay result를 Art Review input으로 사용한다.

---

### `09_ASSET_SPEC_AND_VALIDATION.md`

Source와 Export의 기술 규격을 검사한다.

---

### `11_LEARNING_AND_REUSE.md`

반복되는 engine handoff 지식과 exporter를 Studio 공통 능력으로 축적할 수 있다.

---

### `STYLE_SPEC.md`

프로젝트별 engine-related art constraint를 기록할 수 있다.

---

### `ASSET_MANIFEST.md`

필요한 경우 export / integration 상태를 요약할 수 있다.

---

## 143. 이 문서에서 다루지 않는 것

다음은 이 문서의 범위를 벗어난다.

### 특정 엔진의 상세 import 설정 전체

필요하면 engine-specific guide에서 다룬다.

### 게임 코드 아키텍처

게임 개발 프로젝트의 역할이다.

### 빌드와 배포

별도 개발/DevOps 영역이다.

### Asset Lifecycle 상태 의미

`06_ASSET_LIFECYCLE.md`

### Art Review의 전체 판단 기준

`08_REVIEW_AND_APPROVAL.md`

### Validator 구현

`09_ASSET_SPEC_AND_VALIDATION.md`와 `studio/tools/`

### 프로젝트별 정확한 규격

`STYLE_SPEC.md`

### 장기 학습 승격 기준

`11_LEARNING_AND_REUSE.md`

이 문서는 **Approved source를 실제 게임 환경에 전달하고 런타임에서 확인하는 원칙**에 집중한다.

---

## 144. 핵심 원칙 요약

Art Studio의 Engine Handoff는 파일을 엔진 폴더에 복사하는 작업으로 끝나지 않는다.

핵심 원칙은 다음과 같다.

> **Approved Source와 Engine Export를 구분한다.**

> **Export는 source에서 파생된 결과이며, 원본을 대신하지 않는다.**

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
