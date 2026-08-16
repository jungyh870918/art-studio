# 06_ASSET_LIFECYCLE

## 1. 문서의 역할

이 문서는 Art Studio에서 하나의 자산이 **어떤 의미의 상태를 거쳐 공식 게임 자산으로 정착하는지**를 정의한다.

이 문서는 폴더 구조 문서가 아니다.

이 문서는 생성 도구 사용법 문서도 아니다.

이 문서는 리뷰 체크리스트나 엔진 import 매뉴얼도 아니다.

핵심 질문은 하나다.

> **이 결과물은 지금 어떤 상태이며, 무엇이 확인되어야 다음 상태로 넘어갈 수 있는가?**

Art Studio는 생성된 파일의 존재 자체를 진행 상태로 착각하지 않는다.

이미지가 만들어졌다는 것은 단지 무언가가 생성되었다는 뜻이다.

그 결과가 프로젝트의 방향에 맞는지, 디렉터가 채택했는지, 실제 게임에서 사용할 수 있는 형태인지에 따라 자산의 의미는 달라진다.

---

## 2. 가장 중요한 원칙

Art Studio에서는 다음 세 가지를 절대 동일시하지 않는다.

```text
생성됨
≠
승인됨
≠
게임에 바로 사용 가능함
```

따라서 다음 구분을 기본으로 유지한다.

```text
REFERENCE
↓
CONCEPT
↓
CANDIDATE
↓
APPROVED
↓
EXPORT
```

필요한 경우 다음 상태 또는 보조 상태를 사용할 수 있다.

```text
REJECTED
ON HOLD
SUPERSEDED
```

다만 이 문서는 복잡한 workflow engine을 만들기 위한 것이 아니다.

상태를 늘리는 목적은 관리 시스템을 정교하게 보이게 하는 데 있지 않다.

각 결과물이 현재 무엇을 의미하는지 혼동하지 않도록 하는 것이 목적이다.

---

## 3. Lifecycle은 절대적인 선형 파이프라인이 아니다

기본 흐름은 다음과 같이 이해한다.

```text
REFERENCE
   ↓
CONCEPT
   ↓
CANDIDATE
   ↓
APPROVED
   ↓
EXPORT
```

하지만 실제 제작에서는 다음과 같은 흐름도 정상적이다.

```text
REFERENCE
   ↓
CANDIDATE
   ↓
APPROVED
```

또는:

```text
CONCEPT
   ↓
CANDIDATE A
CANDIDATE B
CANDIDATE C
   ↓
APPROVED B
   ↓
EXPORT
   ↓
게임 화면 검토
   ↓
수정 필요
   ↓
CANDIDATE B2
   ↓
APPROVED
   ↓
EXPORT
```

또는 사람이 직접 만든 기존 에셋이 이미 충분히 검증된 경우:

```text
EXISTING SOURCE
   ↓
APPROVED
   ↓
EXPORT
```

처럼 중간 단계를 생략할 수도 있다.

Lifecycle은 모든 자산에 같은 의식을 강제하기 위한 것이 아니다.

> **필요한 구분은 유지하되, 불필요한 단계는 강제하지 않는다.**

---

## 4. REFERENCE

### 의미

`REFERENCE`는 제작 방향을 이해하거나 특정 문제를 해결하기 위해 참고하는 자료다.

예:

- 사용자가 제공한 이미지
- 기존 게임의 스크린샷
- 시대 고증 자료
- 의상 사진
- 건축 사진
- 승인된 이전 자산
- 다른 작품의 일부 시각적 특성을 참고하기 위한 자료
- 형태, 색감, 조명, 밀도, 실루엣을 이해하기 위한 자료

Reference는 공식 게임 자산이 아니다.

Reference는 채택된 디자인도 아니다.

Reference는 복제 대상이라는 뜻도 아니다.

### Reference에서 가능한 일

- 어떤 특성을 참고할지 분석한다.
- 여러 Reference의 역할을 구분한다.
- Art Direction이나 Asset Brief의 이해를 돕는다.
- 제작 후보를 만들기 위한 방향 자료로 사용한다.

### Reference에서 하면 안 되는 일

- Reference 이미지를 자동으로 승인 자산처럼 취급한다.
- 다른 작품의 이미지를 프로젝트 공식 자산으로 오인한다.
- Reference 한 장의 모든 특징을 그대로 프로젝트 규칙으로 확장한다.
- Reference의 존재만으로 프로젝트 스타일이 결정되었다고 판단한다.

### 다음 상태로 넘어가는 조건

Reference는 반드시 Concept으로 “변환”되어야 하는 상태가 아니다.

Reference는 필요에 따라 Concept이나 Candidate 제작에 사용되는 **입력 자료**다.

따라서 Reference는 다른 상태와 병렬적으로 계속 존재할 수 있다.

---

## 5. CONCEPT

### 의미

`CONCEPT`는 아직 공식 자산으로 채택하기 전의 **탐색용 시각 결과물**이다.

Concept의 목적은 완성품을 만드는 것이 아니라 방향을 찾는 것이다.

예:

- 캐릭터 실루엣 탐색
- 얼굴 방향 탐색
- 몬스터 형태 연구
- 환경 분위기 시안
- 색상 탐색
- 비율 테스트
- 조명 시안
- 맵 분위기 스케치
- UI 그래픽 언어 탐색
- VFX 방향 탐색

### Concept의 특징

Concept은 다음과 같은 상태여도 정상이다.

- 해상도가 낮다.
- 일부만 완성되어 있다.
- 기술 규격을 아직 만족하지 않는다.
- 여러 방향을 과감하게 비교한다.
- 실제 게임에 바로 넣을 수 없다.
- 디테일이 부족하다.
- 의도적으로 거친 상태다.

Concept을 기술 규격 미달이라는 이유만으로 실패로 판단하지 않는다.

Concept의 목적이 방향 탐색이라면, 방향 판단에 필요한 정보만 충분하면 된다.

### Concept와 Candidate의 차이

Concept:

> “어떤 방향으로 갈 것인가?”

Candidate:

> “실제 자산으로 채택할 가능성이 있는 구체적인 결과는 무엇인가?”

예:

```text
Concept:
- 짧고 넓은 체형
- 긴 코트
- 큰 해머
- 세 가지 얼굴 비율 탐색

Candidate:
- hero_a.png
- hero_b.png
- hero_c.png
```

Concept은 디자인 문제를 탐색할 수 있고,
Candidate는 실제 채택 가능한 결과를 비교하는 단계에 가깝다.

### 다음 상태로 넘어가는 조건

Concept이 Candidate로 발전하려면 반드시 모든 것이 확정되어야 하는 것은 아니다.

다만 다음 정도는 확인할 수 있어야 한다.

- 현재 프로젝트의 Art Direction과 명백하게 충돌하지 않는다.
- 어떤 방향을 실제 자산 후보로 발전시킬지 판단할 수 있다.
- Asset Brief가 있다면 핵심 요구를 반영할 수 있다.
- 디렉터가 비교하거나 선택할 수 있는 수준의 방향성이 존재한다.

Concept 전체를 승인할 수도 있지만,
일반적으로는 Concept에서 선택된 방향을 바탕으로 Candidate를 만든다.

---

## 6. CANDIDATE

### 의미

`CANDIDATE`는 **실제 게임 자산으로 채택할 가능성이 있는 구체적인 후보 결과물**이다.

가장 중요한 원칙:

> **Candidate는 만들어졌다는 뜻이지 승인되었다는 뜻이 아니다.**

AI 이미지 생성 결과,
Blender 렌더,
수작업 시안,
외부 제작 결과,
기존 이미지 수정본 등 어떤 방식으로 만들어졌든 동일하다.

### Candidate에 포함될 수 있는 것

- 캐릭터 디자인 후보
- 최종 스프라이트 후보
- UI 아이콘 후보
- 타일 후보
- 텍스처 후보
- 애니메이션 후보
- VFX 후보
- 환경 에셋 후보
- 수정안
- 게임 적용 테스트용 후보

### Candidate가 여러 개일 필요는 없다

모든 작업에서 A/B/C 후보를 강제하지 않는다.

다음 경우 하나의 Candidate만으로도 충분할 수 있다.

- 기존 Art Direction이 매우 명확하다.
- 단순한 자산이다.
- 이전 승인 자산의 변형이다.
- 정해진 규칙에 따라 반복 제작하는 자산이다.
- 디렉터가 명확한 수정 지시를 내렸다.

반대로 중요한 대표 자산이나 방향 탐색이 필요한 경우 여러 Candidate를 비교할 수 있다.

후보 개수는 Lifecycle의 규칙이 아니다.

### Candidate의 기술 상태

Candidate는 반드시 최종 엔진 규격을 만족할 필요는 없다.

하지만 무엇을 검토하는 Candidate인지에 따라 필요한 기술 상태는 달라진다.

예:

캐릭터 디자인 후보:

- silhouette
- proportion
- color direction
- equipment

이 중요할 수 있다.

반면 타일 Candidate라면:

- tile seam
- 반복 결과
- 실제 scale

까지 확인해야 비교가 의미 있을 수 있다.

### Candidate에서 반드시 구분할 것

가능하면 다음을 혼동하지 않는다.

```text
미적 후보
기술적 후보
엔진 적용 후보
```

예를 들어 디자인은 승인되었지만 아직 픽셀 정리나 export가 끝나지 않았을 수 있다.

이 경우 “디자인 승인”과 “최종 파일 승인”의 의미를 구분해서 이해한다.

복잡한 상태 enum으로 만들 필요는 없지만,
현재 무엇이 승인 대상인지 분명해야 한다.

---

## 7. Candidate Review

Candidate는 디렉터가 판단 가능한 형태로 제시한다.

가능하면 비교 조건을 통제한다.

예:

- 동일한 표시 크기
- 동일한 배경
- 동일한 카메라
- 동일한 조명
- 동일한 포즈 또는 유사한 조건
- 핵심 차이가 잘 보이는 배열

비교 자료 자체는 `REVIEW_AND_APPROVAL` 문서가 더 상세히 다룬다.

Lifecycle에서 중요한 것은 다음이다.

> Candidate는 검토를 거쳐 Approved가 되거나, 수정되어 새로운 Candidate가 되거나, Reject/On Hold 될 수 있다.

---

## 8. APPROVED

### 의미

`APPROVED`는 디렉터가 공식적으로 채택한 **프로젝트의 현재 공식 자산 또는 공식 source**다.

Approved는 단순히 가장 좋은 Candidate라는 뜻이 아니다.

승인된 순간부터 프로젝트의 후속 제작과 비교에서 **현재 기준으로 사용 가능한 공식 결과**가 된다.

### 승인 권한

최종 미적 승인 권한은 게임 디렉터에게 있다.

Claude는 다음을 할 수 있다.

- 후보 비교
- Art Direction과의 일관성 분석
- 기술 문제 발견
- 추천안 제시
- 차이 설명
- 위험 요소 설명

하지만 Claude의 추천을 자동 승인으로 취급하지 않는다.

### 명시적 승인

가능하면 다음과 같은 디렉터의 명확한 의사 표시를 승인으로 인정한다.

예:

- “2번으로 간다.”
- “B를 채택.”
- “이걸 공식 캐릭터로 쓰자.”
- “이 버전을 기준으로 나머지도 만들자.”
- 프로젝트 문서에서 Approved로 기록됨

반대로 다음은 자동 승인으로 간주하지 않는다.

- “괜찮네.”
- “이 방향이 낫다.”
- “일단 이걸로 봐보자.”
- “게임에 넣어봐.”
- Claude가 가장 좋다고 평가함

문맥상 명백한 경우에는 지나치게 형식적인 승인 문구를 요구하지 않는다.

핵심은 **채택 의도가 분명한가**다.

### Approved는 영구 불변이 아니다

승인된 자산은 현재 기준에서 공식 자산이다.

하지만 이후 다음 이유로 변경될 수 있다.

- 실제 게임 화면에서 가독성 문제 발견
- Art Direction의 큰 변경
- 기술 제약 발견
- 애니메이션 적용 문제
- 플랫폼 변경
- 더 나은 방향으로 디렉터가 재결정

Approved는 권위 있는 현재 기준이지만,
절대 변경 불가능한 유물이 아니다.

---

## 9. 승인 범위를 구분한다

승인은 항상 “모든 것을 승인했다”는 뜻이 아닐 수 있다.

예:

```text
디자인 승인
색상 미확정
```

```text
실루엣 승인
얼굴 수정 필요
```

```text
원본 일러스트 승인
엔진용 crop 미확정
```

```text
애니메이션 pose 승인
timing 수정 필요
```

필요하다면 승인된 범위를 짧게 기록한다.

이 원칙은 중요한 자산에서 특히 유용하다.

하지만 모든 작은 자산에 복잡한 partial approval 체계를 강제하지 않는다.

---

## 10. APPROVED SOURCE와 EXPORT를 구분한다

가장 중요한 구분 중 하나다.

```text
APPROVED SOURCE
≠
ENGINE-READY EXPORT
```

예:

```text
approved/hero_master.png
```

가 프로젝트의 공식 원본일 수 있다.

그 원본에서 다음이 파생될 수 있다.

```text
exports/unity/hero.png
exports/web/hero.webp
exports/roblox/hero_texture.png
```

또는:

```text
approved/character_model.blend
        ↓
exports/unity/hero.fbx
exports/render/hero_sprite.png
```

Approved는 공식 source의 의미를 가진다.

Export는 특정 사용 환경에 맞게 파생된 결과다.

---

## 11. EXPORT

### 의미

`EXPORT`는 Approved source를 **실제 게임 엔진, 플랫폼 또는 배포 환경에서 사용할 수 있도록 가공한 파생 결과물**이다.

예:

- Unity용 sprite
- Godot용 texture
- Roblox texture
- Web용 압축 이미지
- sprite atlas
- tileset export
- engine-specific texture
- animation sheet
- normal map
- mask
- optimized mesh
- runtime format

### Export가 새로운 미적 승인인 것은 아니다

정상적인 export는 승인된 source의 의미를 가능한 한 보존해야 한다.

예:

```text
approved source
↓
resize
↓
format conversion
↓
compression
↓
engine export
```

이 과정은 기술적 처리일 수 있다.

하지만 export 과정에서 시각적 결과가 달라지면 다시 검토가 필요할 수 있다.

예:

- 축소 후 얼굴이 읽히지 않음
- 압축으로 색이 무너짐
- alpha edge 발생
- 엔진 filtering으로 픽셀이 흐려짐
- shader와 결합했을 때 outline이 과해짐

이 경우 export는 기술적으로 성공했더라도 실제 게임 아트로서는 문제가 있을 수 있다.

---

## 12. Runtime Validation 이후의 상태

Export 이후 실제 게임에 넣어본 결과는 Lifecycle의 중요한 피드백이다.

개념적으로:

```text
APPROVED
↓
EXPORT
↓
RUNTIME TEST
↓
REVIEW
```

Runtime test 결과 문제가 없으면 현재 Approved source와 Export를 유지한다.

문제가 있다면 원인을 구분한다.

### Source 문제

예:

- 캐릭터 실루엣 자체가 약함
- 색 구조가 배경과 충돌
- 디테일이 너무 많음

이 경우 source 단계로 돌아가 수정한다.

### Export 문제

예:

- 잘못된 resize
- alpha 처리 문제
- filtering 문제
- 압축 문제

이 경우 Approved source는 유지하고 Export만 다시 만든다.

### Engine 문제

예:

- lighting
- shader
- material
- camera
- post-processing
- scale

이 경우 자산을 다시 그리기 전에 엔진 환경 문제인지 확인한다.

> **실제 화면에서 실패했다고 항상 source asset을 수정하는 것은 아니다.**

이 판단의 세부 절차는 `ENGINE_HANDOFF`와 `REVIEW_AND_APPROVAL` 문서에서 상세히 다룬다.

---

## 13. REJECTED

### 의미

`REJECTED`는 현재 방향에서 채택하지 않기로 결정한 Candidate다.

Rejected는 반드시 쓸모없는 파일이라는 뜻은 아니다.

반려 결과에는 다음 정보가 남을 수 있다.

- 어떤 방향이 맞지 않았는가
- 어떤 요소가 과했는가
- 어떤 스타일이 프로젝트와 충돌했는가
- 어떤 기술적 접근이 실패했는가
- 디렉터가 무엇을 원하지 않는가

예:

```text
Candidate B — Rejected

이유:
- 갑옷 밀도가 너무 높음
- 현재 게임의 단순한 실루엣 방향과 충돌
```

이 정보는 후속 제작에 도움이 될 수 있다.

### Rejected를 자동 삭제하지 않는다

특히 다음은 보존 가치가 있을 수 있다.

- 중요한 대표 자산의 비교 후보
- 디렉터가 명확한 이유를 남긴 후보
- 나중에 다른 방향에서 참고할 가능성이 있는 후보
- 제작 방식의 실패 원인을 보여주는 결과

하지만 모든 실패 결과를 영구 보존해야 하는 것은 아니다.

삭제 및 보관 정책은 프로젝트 규모와 필요에 따라 별도로 정할 수 있다.

---

## 14. ON HOLD

### 의미

`ON HOLD`는 현재 채택하지 않았지만 완전히 폐기하지도 않은 방향이다.

사용 예:

- 두 가지 스타일 중 하나를 먼저 검증하기로 함
- 엔진 테스트 후 판단 예정
- 개발 우선순위 때문에 일시 중단
- 다른 자산이 확정된 후 다시 비교 예정

예:

```text
고밀도 캐릭터 버전
→ ON HOLD

저밀도 버전을 prototype에서 먼저 검증한다.
```

On Hold는 Rejected와 다르다.

```text
REJECTED
= 현재 방향에서 채택하지 않음

ON HOLD
= 판단 또는 작업을 보류함
```

작은 프로젝트에서는 이 상태를 굳이 사용할 필요가 없다.

---

## 15. SUPERSEDED

### 의미

`SUPERSEDED`는 과거에는 Approved였지만 새로운 Approved 결과로 대체된 자산을 표현할 때 사용할 수 있다.

예:

```text
hero_v1
Approved

↓

hero_v2
새로 Approved

↓

hero_v1
Superseded
```

중요한 것은 과거 승인본이 “처음부터 잘못된 Candidate”로 바뀌는 것이 아니라는 점이다.

그 자산은 당시에는 실제 Approved였다.

프로젝트가 발전하면서 현재 기준이 바뀐 것이다.

### 언제 필요한가

다음과 같은 경우 유용할 수 있다.

- 대표 캐릭터 리디자인
- 큰 Art Direction 변경
- 플랫폼 변경
- 대규모 리마스터
- 게임 화면 검증 후 공식 자산 교체

작은 수정마다 Superseded 상태를 남길 필요는 없다.

Git 또는 다른 버전 관리가 충분한 경우 별도 상태 표현을 생략할 수도 있다.

---

## 16. 수정은 새로운 Candidate를 만들 수 있다

Approved 자산에 수정이 필요하다고 해서 승인 파일을 무조건 직접 덮어쓰지 않는다.

특히 미적 변화가 포함되거나 결과가 아직 확정되지 않은 경우:

```text
APPROVED
↓
수정 요청
↓
NEW CANDIDATE
↓
REVIEW
↓
APPROVED
```

로 다루는 것이 안전하다.

예:

```text
hero approved
↓
"무기를 20% 줄여"
↓
hero_weapon_small_candidate
↓
확인
↓
새 approved
```

다만 매우 단순하고 결과가 명확한 기술 수정까지 매번 별도의 복잡한 Candidate 단계로 만들 필요는 없다.

예:

- 잘못된 파일명 수정
- 승인된 기준에 따른 포맷 변환
- 명확한 padding 수정
- 규격에 맞춘 crop

처럼 미적 판단이 개입하지 않는 작업은 기존 승인 상태를 유지한 채 기술적으로 처리할 수 있다.

---

## 17. 상태와 파일 위치는 같은 개념이 아니다

프로젝트 구조에서 `references/`, `candidates/`, `approved/`, `exports/` 같은 폴더를 사용할 수 있다.

하지만 Lifecycle은 폴더 이름보다 **자산의 의미**를 정의한다.

예를 들어 아직 정리되지 않은 임시 작업 폴더에 있다고 해서 Candidate가 아닌 것은 아니다.

반대로 `approved/` 폴더에 파일을 복사했다고 자동으로 Approved가 되는 것도 아니다.

> **상태는 의미이고, 폴더는 그 의미를 관리하기 위한 구조다.**

정상적인 프로젝트에서는 둘이 일치하도록 유지하는 것이 좋지만,
Lifecycle의 본질은 파일 경로가 아니라 승인과 용도의 의미다.

---

## 18. Asset Manifest와 Lifecycle의 관계

향후 `ASSET_MANIFEST.md`는 각 자산의 현재 Lifecycle 상태를 기록하는 데 사용할 수 있다.

개념적으로:

```text
Asset:
Goblin Spearman

Status:
CANDIDATE
```

또는:

```text
Asset:
Hero Portrait

Status:
APPROVED

Export:
Unity complete
Web pending
```

하지만 Lifecycle 문서는 Manifest 형식을 정의하지 않는다.

Lifecycle은 **상태의 의미**를 정의한다.

Manifest는 **실제 프로젝트의 자산들이 현재 어느 상태인지 기록**한다.

---

## 19. Asset Brief와 Lifecycle의 관계

`ASSET_BRIEF.md`는 무엇을 만들어야 하는지를 정의한다.

Lifecycle은 그 제작물이 현재 어디까지 왔는지를 정의한다.

예:

```text
ASSET BRIEF
"주인공 기본 초상화를 제작한다."

↓

CANDIDATES
A / B / C

↓

APPROVED
B
```

Asset Brief 자체에는 상태 전이 규칙을 넣지 않는다.

---

## 20. Review Log와 Lifecycle의 관계

`REVIEW_LOG.md`는 중요한 승인과 반려 이유를 기록할 수 있다.

예:

```text
Asset:
Hero A

Decision:
Rejected

Reason:
얼굴은 좋지만 현재 게임의 거친 형태 언어보다 지나치게 매끈함.
```

또는:

```text
Asset:
Hero B

Decision:
Approved

Reason:
작은 화면에서 실루엣과 무기가 가장 잘 읽힘.
```

Lifecycle은 상태를 정의한다.

Review Log는 중요한 결정의 이유를 보존한다.

모든 상태 변경을 Review Log에 남길 필요는 없다.

---

## 21. Style Direction 변경과 Lifecycle

프로젝트의 Art Direction이 변경될 수 있다.

이 경우 기존 Approved 자산을 자동으로 전부 Rejected로 바꾸지 않는다.

먼저 영향 범위를 판단한다.

예:

```text
변경:
배경 contrast를 더 낮춘다.
```

이 변화가 캐릭터 Approved 자산에 영향을 주지 않을 수도 있다.

반대로:

```text
변경:
모든 주요 캐릭터를 현실 비율에서 3등신으로 변경한다.
```

이라면 기존 캐릭터 Approved 자산은 재검토 대상이 될 수 있다.

중요한 원칙:

> **Art Direction의 변경과 개별 자산의 상태 변경을 자동으로 동일시하지 않는다.**

영향받는 자산만 재검토한다.

---

## 22. 부분 자산과 파생 자산

하나의 자산이 다른 자산에서 파생될 수 있다.

예:

```text
Approved Hero
↓
Red Team Variant
Blue Team Variant
```

또는:

```text
Approved Portrait
↓
Small UI Portrait
Dialogue Portrait
Roster Portrait
```

파생 자산이 단순 기술 변환이면 원본 Approved 상태를 기반으로 export처럼 취급할 수 있다.

하지만 파생 과정에서 새로운 미적 판단이 필요하다면 별도 Candidate / Approved 흐름을 사용할 수 있다.

예:

팀 색상 variant가 단순 hue swap이 아니라 장비 디자인까지 바뀐다면 별도 Candidate가 적절할 수 있다.

---

## 23. Asset Family의 승인

때로는 개별 파일보다 **계열 규칙**이 먼저 승인될 수 있다.

예:

```text
기사 계열:
- 넓은 어깨
- 짧은 하체
- 큰 방패
```

이 방향이 승인되었다고 해서 이후 모든 기사 자산이 자동 Approved가 되는 것은 아니다.

승인된 것은 **계열의 방향**이다.

개별 자산은 필요에 따라 별도 검토한다.

반대로 반복 제작 규칙이 매우 명확하고 위험이 낮다면 매번 동일한 강도의 리뷰를 요구할 필요는 없다.

Lifecycle은 반복 작업에서 사람을 병목으로 만들기 위한 시스템이 아니다.

---

## 24. 기술 실패와 미적 반려를 구분한다

다음 두 상황은 다르다.

### 미적 반려

```text
실루엣이 현재 게임 방향과 맞지 않는다.
```

### 기술 실패

```text
alpha channel이 누락되었다.
```

기술 실패는 수정 후 같은 디자인을 유지할 수 있다.

미적 반려는 디자인 방향 자체의 수정이 필요할 수 있다.

따라서 “Rejected”라는 상태를 모든 문제에 기계적으로 사용하지 않는다.

단순 기술 오류는 Candidate가 실패했다기보다 **검증을 통과하지 못한 상태**일 수 있다.

세부 기술 검증은 `ASSET_SPEC_AND_VALIDATION` 문서에서 정의한다.

---

## 25. 승인 전 기술 검사의 정도는 자산마다 다를 수 있다

모든 Candidate가 같은 수준의 기술 검사를 거칠 필요는 없다.

예:

초기 Concept:

- 완전한 alpha 검사 불필요
- 정확한 padding 불필요

최종 sprite Candidate:

- dimensions
- alpha
- palette
- frame
- naming

등이 중요할 수 있다.

Lifecycle에서 중요한 것은:

> **현재 단계의 목적에 맞는 수준의 검증을 한다.**

최종 Export에 가까워질수록 기술적 요구는 일반적으로 더 엄격해질 수 있다.

---

## 26. 실제 게임 화면이 상태를 되돌릴 수 있다

이미 Approved된 자산도 실제 게임에서 문제가 발견될 수 있다.

예:

```text
APPROVED
↓
EXPORT
↓
GAME SCREENSHOT
↓
"배경에 묻힌다."
```

이 경우 Approved를 무조건 유지하지 않는다.

필요하면 다시 Candidate 단계로 돌아갈 수 있다.

```text
APPROVED
↓
RUNTIME ISSUE
↓
REVISED CANDIDATE
↓
REVIEW
↓
NEW APPROVED
```

하지만 원인이 엔진 설정에 있다면 source asset의 승인을 취소할 필요가 없을 수도 있다.

항상 문제의 위치를 먼저 구분한다.

---

## 27. 상태를 자동화할 수 있는 부분

Lifecycle의 일부는 자동화할 수 있다.

예:

- Candidate 파일 수집
- export 생성 여부 확인
- 기술 검사 결과 연결
- Manifest의 일부 상태 갱신
- 승인 원본에서 파생 export 생성
- 누락된 export 탐지

하지만 다음은 자동화 대상으로 취급하지 않는다.

- 어떤 Candidate가 가장 매력적인가
- 어떤 디자인을 공식 자산으로 채택할 것인가
- 게임의 분위기에 충분히 맞는가
- 언제 결과물이 충분히 좋은가

자동화는 상태를 관리하는 데 도움을 줄 수 있지만,
미적 승인 권한을 대신하지 않는다.

---

## 28. 상태 이름을 과도하게 늘리지 않는다

다음처럼 세밀한 상태를 끝없이 만드는 것은 기본 방향이 아니다.

```text
READY_FOR_REVIEW
REVIEWING
CHANGES_REQUESTED
READY_FOR_RECHECK
TECH_PASS
ART_PASS
WAITING_DIRECTOR
WAITING_EXPORT
...
```

대규모 제작에서 실제 필요가 있다면 별도 관리 시스템을 도입할 수 있다.

하지만 기본 Art Studio에서는 다음 정도의 개념만으로 충분해야 한다.

```text
REFERENCE
CONCEPT
CANDIDATE
APPROVED
EXPORT

선택적:
REJECTED
ON HOLD
SUPERSEDED
```

그리고 필요한 상세 정보는 메모, Manifest, Review Log에서 설명한다.

---

## 29. 작은 작업은 Lifecycle을 가볍게 적용한다

예를 들어 간단한 UI 아이콘 하나라면:

```text
CANDIDATE
↓
APPROVED
↓
EXPORT
```

정도로 충분할 수 있다.

또는 이미 규칙이 매우 명확한 반복 아이콘이라면:

```text
제작
↓
기술 확인
↓
사용
```

처럼 실무적으로 처리할 수도 있다.

반대로 대표 캐릭터처럼 중요하고 방향성이 큰 자산은:

```text
REFERENCE
↓
CONCEPT
↓
MULTIPLE CANDIDATES
↓
DIRECTOR REVIEW
↓
REVISED CANDIDATE
↓
APPROVED
↓
ENGINE TEST
↓
REVIEW
↓
FINAL EXPORT
```

처럼 더 깊게 다룰 수 있다.

> **Lifecycle의 깊이는 자산의 중요도와 불확실성에 비례할 수 있다.**

---

## 30. 상태 변경의 최소 기록

상태를 거대한 데이터베이스로 만들 필요는 없지만,
중요한 자산에서는 최소한 다음을 알 수 있으면 좋다.

- 현재 상태
- 현재 공식 Approved가 무엇인지
- 어떤 Candidate가 대체되었는지
- export가 존재하는지
- 중요한 승인 또는 반려 이유가 있는지

이 정보는 프로젝트 규모에 따라 Markdown만으로도 충분할 수 있다.

필요가 커질 경우 별도 도구나 구조를 추가할 수 있다.

---

## 31. Lifecycle과 버전 관리

Git 또는 다른 버전 관리가 존재하더라도 Lifecycle을 완전히 대체하지는 않는다.

버전 관리가 알려주는 것:

> 파일이 언제 어떻게 변경되었는가.

Lifecycle이 알려주는 것:

> 이 파일이 프로젝트에서 어떤 의미를 가지는가.

예:

```text
hero_v4.png
```

가 최신 commit이라고 해서 Approved라는 뜻은 아니다.

반대로 과거 commit의 파일이 현재 Approved일 수도 있다.

따라서 파일 버전과 Art Lifecycle 상태를 동일시하지 않는다.

---

## 32. Lifecycle에서 가장 중요한 질문

현재 자산을 볼 때 다음 질문 정도면 충분하다.

### Reference인가?

방향 이해를 위한 자료인가?

### Concept인가?

탐색을 위한 결과인가?

### Candidate인가?

실제 채택 가능한 구체적 후보인가?

### Approved인가?

디렉터가 공식 자산 또는 공식 source로 채택했는가?

### Export인가?

Approved source에서 특정 게임 환경을 위해 파생된 결과인가?

그리고 필요하면:

### Rejected인가?

현재 방향에서 채택하지 않기로 한 후보인가?

### On Hold인가?

판단을 보류한 방향인가?

### Superseded인가?

과거에는 Approved였지만 현재 공식 승인본으로 대체되었는가?

---

## 33. 이 문서에서 다루지 않는 것

다음 내용은 후속 전문 문서에서 상세화한다.

### `07_GENERATION_WORKFLOW.md`

- 실제 제작 작업의 순서
- 어떤 문서를 먼저 읽는지
- Reference를 어떻게 수집하는지
- 어떤 제작 방식을 선택하는지
- Candidate를 어떻게 만드는지
- 반복 수정 루틴

### `08_REVIEW_AND_APPROVAL.md`

- Technical Review와 Art Review의 차이
- 승인 시 무엇을 확인하는지
- 디렉터에게 결과를 어떻게 제시하는지
- 실제 승인과 반려의 판단 방식

### `09_ASSET_SPEC_AND_VALIDATION.md`

- dimensions
- alpha
- palette
- format
- frame
- tile seam
- naming
- engine constraint
- 자동 검사

### `10_ENGINE_HANDOFF.md`

- Approved source에서 export를 만드는 구체적 과정
- 엔진 import
- runtime validation
- 실제 게임 screenshot 검토

### `11_LEARNING_AND_REUSE.md`

- 반려와 수정에서 무엇을 학습으로 남길지
- 어떤 경험을 Studio 공통 지식으로 승격할지

### 후속 템플릿

- `STYLE_SPEC.md`
- `ASSET_MANIFEST.md`
- `ASSET_BRIEF.md`
- `REVIEW_LOG.md`

이 문서는 그 문서들이 공유할 **자산 상태의 의미와 경계**만 정의한다.

---

## 34. 핵심 원칙 요약

Art Studio의 Asset Lifecycle은 자산을 통제하기 위한 복잡한 승인 시스템이 아니다.

목적은 현재 결과물이 무엇을 의미하는지 분명하게 유지하는 것이다.

핵심 원칙은 다음과 같다.

> **생성된 결과는 자동으로 승인된 자산이 아니다.**

> **Candidate와 Approved를 구분한다.**

> **Approved source와 engine-ready Export를 구분한다.**

> **Reference, Concept, Candidate는 서로 목적이 다르다.**

> **실제 게임 화면에서 문제가 발견되면 Lifecycle은 다시 이전 단계로 돌아갈 수 있다.**

> **반려된 결과도 학습 정보가 될 수 있지만, 자동으로 프로젝트 전체 규칙으로 일반화하지 않는다.**

> **상태는 파일 위치가 아니라 자산의 의미다.**

> **작은 자산에는 가볍게, 중요한 자산에는 필요한 만큼 깊게 적용한다.**

> **Lifecycle은 사람의 미적 판단을 제거하기 위한 workflow engine이 아니다.**

> **최종적으로 중요한 것은 상태 관리 자체가 아니라 좋은 게임 아트를 안전하게 공식 자산으로 정착시키는 것이다.**
