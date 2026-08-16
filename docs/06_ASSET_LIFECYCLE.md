# 06_ASSET_LIFECYCLE

## 1. 문서의 역할

이 문서는 하나의 자산이 **어떤 의미의 단계를 거쳐 공식 게임 자산으로 정착하는지**를 정의한다.

이 문서는 폴더 구조 문서가 아니고, 생성 도구 사용법이나 리뷰 체크리스트, 엔진 import 매뉴얼도 아니다.

핵심 질문은 하나다.

> **이 결과물은 지금 어떤 상태이며, 무엇이 확인되어야 다음 상태로 넘어갈 수 있는가?**

Art Studio는 파일이 존재한다는 사실을 진행 상태로 착각하지 않는다. 이미지가 만들어졌다는 것은 무언가가 생성되었다는 뜻일 뿐이고, 그 결과가 프로젝트 방향에 맞는지 · 디렉터가 채택했는지 · 실제 게임에서 쓸 수 있는 형태인지에 따라 자산의 의미는 완전히 달라진다.

---

## 2. 가장 중요한 원칙

다음 셋을 절대 동일시하지 않는다.

```text
생성됨
≠
승인됨
≠
게임에 바로 사용 가능함
```

그래서 다음 구분을 기본으로 유지한다.

```text
REFERENCE
CONCEPT
CANDIDATE
APPROVED
EXPORT
```

필요한 경우 보조 상태를 사용할 수 있다.

```text
REJECTED · ON HOLD · SUPERSEDED
```

이 문서는 workflow engine을 만들기 위한 것이 아니다. 상태를 두는 목적은 관리 시스템을 정교하게 보이게 하는 데 있지 않고, **각 결과물이 현재 무엇을 의미하는지 혼동하지 않게 하는 데** 있다.

---

## 3. 이 다섯 개는 같은 종류의 값이 아니다

위 목록이 하나의 일렬 상태값처럼 읽히기 쉽지만, 실제로는 성격이 다른 세 가지가 섞여 있다. 이 구분이 이 문서에서 가장 자주 혼동되는 지점이다.

### Source 제작 상태 — 서로 배타적이다

```text
CONCEPT  →  CANDIDATE  →  APPROVED
```

한 자산의 **현재 공식 source**는 한 시점에 이 중 하나의 위치에 있다. `ASSET_MANIFEST.md`의 `상태` 칸이 가리키는 것이 바로 이 축이다. 그 자산의 source 제작이 지금 어디까지 왔는지를 나타낸다.

### REFERENCE — 병렬로 존재하는 입력 자료

Reference는 "Concept 이전 단계"가 아니다. **제작 전 과정에 걸쳐 계속 옆에 존재하는 참고 자료**다. Candidate를 만드는 중에도, Approved가 나온 뒤에도 Reference는 그대로 남아 있고 새로 늘어날 수도 있다.

Manifest의 상태 칸에 `REFERENCE`를 쓸 수 있는 경우는 하나다. **참고 자료만 모였고 아직 어떤 제작 결과도 없는 자산**을 표시할 때다. 그때도 그 자산이 "Reference라는 물건"이라는 뜻이 아니라 source 제작이 아직 시작되지 않았다는 뜻이다.

> **Reference에 저장되어 있다는 사실은 승인과 아무 관계가 없다.**

### EXPORT — Source에서 파생된 결과물

Export는 source 제작 축의 다음 칸이 아니다. **Approved source(또는 필요한 source)에서 특정 실행 환경을 위해 파생된 결과물**이다. 그래서 Manifest에서도 상태 칸이 아니라 별도의 Export 칸에서 본다.

```text
Source 축   CONCEPT → CANDIDATE → APPROVED     한 시점에 하나
파생 축     APPROVED SOURCE → EXPORT           여러 target이 동시에 존재할 수 있다
입력 자료   REFERENCE                          두 축과 병렬로 계속 존재한다
```

같은 자산이 `APPROVED` 상태이면서 unity export는 있고 web export는 없을 수 있다. 이것은 상태가 두 개인 것이 아니라 **축이 다른 것**이다.

### 보조 상태 — 판단의 결과를 표시한다

`REJECTED` · `ON HOLD` · `SUPERSEDED`는 제작 진행 위치가 아니라 그 결과에 대한 판단을 나타낸다. 필요할 때만 쓴다.

여기서 새로운 필드나 데이터 모델을 만들지 않는다. 이 구분은 사람이 읽고 이해하기 위한 것이다.

---

## 4. Lifecycle은 절대적인 선형 파이프라인이 아니다

기본 흐름은 `REFERENCE → CONCEPT → CANDIDATE → APPROVED → EXPORT`로 이해하되, 실제 제작에서는 다음도 모두 정상이다.

```text
REFERENCE → CANDIDATE → APPROVED                     Concept 생략

CONCEPT → CANDIDATE A/B/C → APPROVED B → EXPORT
       → 게임 화면 검토 → 수정 필요 → CANDIDATE B2
       → APPROVED → EXPORT                           승인 이후의 왕복

EXISTING SOURCE → APPROVED → EXPORT                  이미 검증된 기존 에셋
```

Lifecycle은 모든 자산에 같은 의식을 강제하기 위한 것이 아니다.

> **필요한 구분은 유지하되, 불필요한 단계는 강제하지 않는다.**

---

## 5. REFERENCE

제작 방향을 이해하거나 특정 문제를 해결하기 위해 참고하는 자료다.

> 디렉터가 제공한 이미지 · 기존 게임의 스크린샷 · 시대 고증 자료 · 의상과 건축 사진 · 승인된 이전 자산 · 형태·색감·조명·밀도·실루엣을 이해하기 위한 자료

**Reference는 공식 게임 자산이 아니고, 채택된 디자인도 아니며, 복제 대상이라는 뜻도 아니다.**

Reference로 할 수 있는 일 — 어떤 특성을 참고할지 분석하기 · 여러 Reference의 역할을 구분하기 · Art Direction이나 Asset Brief의 이해를 돕기 · Concept과 Candidate 제작의 입력 자료로 쓰기.

하지 않는 일 — Reference를 승인 자산처럼 취급하기 · 다른 작품의 이미지를 프로젝트 공식 자산으로 오인하기 · Reference 한 장의 모든 특징을 프로젝트 규칙으로 확장하기 · Reference가 있다는 사실만으로 프로젝트 스타일이 정해졌다고 판단하기.

Reference를 어떻게 읽고 무엇을 참고할지는 `04_ART_DIRECTION_SYSTEM.md`가 다룬다.

---

## 6. CONCEPT

아직 공식 자산으로 채택하기 전의 **탐색용 시각 결과물**이다. 목적은 완성품을 만드는 것이 아니라 방향을 찾는 것이다.

> 캐릭터 실루엣 탐색 · 얼굴 방향 탐색 · 몬스터 형태 연구 · 환경 분위기 시안 · 색상 탐색 · 비율 테스트 · 조명 시안 · UI 그래픽 언어 탐색 · VFX 방향 탐색

Concept은 해상도가 낮거나, 일부만 완성되었거나, 기술 규격을 만족하지 않거나, 의도적으로 거친 상태여도 정상이다. **기술 규격 미달이라는 이유만으로 Concept을 실패로 판단하지 않는다.** 방향 판단에 필요한 정보만 충분하면 된다.

Concept과 Candidate의 차이는 던지는 질문이 다르다는 데 있다.

```text
Concept    "어떤 방향으로 갈 것인가?"
           짧고 넓은 체형 · 긴 코트 · 큰 해머 · 세 가지 얼굴 비율 탐색

Candidate  "실제 자산으로 채택할 가능성이 있는 구체적인 결과는 무엇인가?"
           hero_a.png · hero_b.png · hero_c.png
```

**Concept 단계는 항상 필요한 것이 아니다.** 방향이 이미 명확한 작업, 반복 제작, 단순한 자산에서는 생략한다. Concept이 필요한지 판단하는 기준은 `07_GENERATION_WORKFLOW.md`가 다룬다.

Concept에서 Candidate로 넘어갈 때 모든 것이 확정되어 있어야 하는 것은 아니다. 다만 현재 Art Direction과 명백히 충돌하지 않고, 어떤 방향을 자산 후보로 발전시킬지 판단할 수 있으며, 디렉터가 비교하거나 선택할 수 있는 수준의 방향성은 있어야 한다.

---

## 7. CANDIDATE

**실제 게임 자산으로 채택할 가능성이 있는 구체적인 후보 결과물**이다.

> **Candidate는 만들어졌다는 뜻이지 승인되었다는 뜻이 아니다.**

AI 생성 결과든, Blender 렌더든, 수작업 시안이든, 외부 제작 결과든, 기존 이미지의 수정본이든 동일하다. **생성 도구가 출력했다는 사실은 승인 근거가 되지 않는다.**

동시에 **raw generation이 곧 Candidate인 것도 아니다.** 생성 결과는 다음 단계의 source인 경우가 많고, cleanup·보정·수작업을 거쳐 비교 가능한 상태가 되었을 때 Candidate가 된다. Candidate는 **디렉터가 판단할 수 있을 만큼 준비된 결과**를 뜻한다.

### 후보가 여러 개일 필요는 없다

모든 작업에서 A/B/C를 강제하지 않는다. Art Direction이 매우 명확하거나 · 단순한 자산이거나 · 이전 승인 자산의 변형이거나 · 정해진 규칙에 따른 반복 제작이거나 · 디렉터가 명확한 수정 지시를 내린 경우에는 하나로 충분하다.

**후보 개수는 Lifecycle의 규칙이 아니다.** 몇 개를 어떻게 만들지는 `07_GENERATION_WORKFLOW.md`가 다룬다.

### 어떤 Candidate인지에 따라 필요한 기술 상태가 다르다

Candidate가 반드시 최종 엔진 규격을 만족해야 하는 것은 아니다. 다만 무엇을 비교하려는 후보인지에 따라 확보되어야 하는 상태가 달라진다. 캐릭터 디자인 후보라면 실루엣·비율·색 방향·장비가, 타일 후보라면 seam과 반복 결과와 실제 scale까지 확인되어야 비교가 의미 있다.

단계별 검증 강도는 `09_ASSET_SPEC_AND_VALIDATION.md`가 다룬다.

### 무엇에 대한 승인인지 구분한다

디자인은 승인되었지만 아직 픽셀 정리나 export가 끝나지 않았을 수 있다. 이때 "디자인 승인"과 "최종 파일 승인"의 의미를 구분해서 이해한다. 복잡한 상태 enum을 만들 필요는 없지만 **현재 무엇이 승인 대상인지는 분명해야 한다.**

---

## 8. APPROVED

디렉터가 공식적으로 채택한 **프로젝트의 현재 공식 자산 또는 공식 source**다.

Approved는 단순히 가장 좋은 Candidate라는 뜻이 아니다. 승인된 순간부터 후속 제작과 비교에서 **현재 기준으로 사용되는 공식 결과**가 된다.

### 승인 권한

**최종 미적 승인 권한은 게임 디렉터에게 있다.**

Claude는 후보를 비교하고, Art Direction과의 일관성을 분석하고, 기술 문제를 찾아내고, 추천안을 제시하고, 차이와 위험 요소를 설명할 수 있다. 하지만 **Claude의 추천을 자동 승인으로 취급하지 않는다.**

같은 이유로, 이미 Approved된 자산에 대해 Claude가 더 나은 대안을 발견했다고 해서 **승인 상태를 임의로 바꾸지 않는다.** 문제를 설명하고 대안을 제시할 수는 있지만 승인을 철회할 수 있는 것은 디렉터뿐이다.

그리고 기술 검사 결과는 승인이 아니다.

```text
TECHNICAL PASS
≠
DIRECTOR APPROVAL
```

검사를 통과했다는 것은 기술 규격을 만족했다는 뜻이지 채택되었다는 뜻이 아니다.

### 무엇을 승인으로 볼 것인가

채택 의도가 분명한 표시를 승인으로 인정한다.

```text
승인으로 본다      "2번으로 간다" · "B를 채택" · "이걸 공식 캐릭터로 쓰자" ·
                 "이 버전을 기준으로 나머지도 만들자" · 프로젝트 문서에 Approved로 기록

자동 승인이 아니다  "괜찮네" · "이 방향이 낫다" · "일단 이걸로 봐보자" ·
                 "게임에 넣어봐" · Claude가 가장 좋다고 평가함
```

문맥상 명백한 경우 지나치게 형식적인 승인 문구를 요구하지 않는다. **핵심은 채택 의도가 분명한가다.** 판단의 세부 기준은 `08_REVIEW_AND_APPROVAL.md`가 다룬다.

### 승인 범위를 구분한다

승인이 항상 "모든 것을 승인했다"는 뜻은 아니다.

```text
디자인 승인 / 색상 미확정      실루엣 승인 / 얼굴 수정 필요
원본 일러스트 승인 / 엔진용 crop 미확정      애니메이션 pose 승인 / timing 수정 필요
```

필요하면 승인된 범위를 짧게 기록한다. 중요한 자산에서 특히 유용하다. 다만 **모든 작은 자산에 복잡한 partial approval 체계를 강제하지 않는다.**

### Approved는 영구 불변이 아니다

승인된 자산은 현재 기준에서 공식 자산이지만, 실제 게임 화면에서 가독성 문제가 발견되거나 · Art Direction이 크게 바뀌거나 · 기술 제약이 발견되거나 · 플랫폼이 바뀌거나 · 디렉터가 재결정하면 바뀔 수 있다.

**Approved는 권위 있는 현재 기준이지 변경 불가능한 유물이 아니다.** 다만 변경하는 것은 디렉터다.

---

## 9. APPROVED SOURCE와 EXPORT를 구분한다

가장 중요한 구분 중 하나다.

```text
APPROVED SOURCE
≠
ENGINE-READY EXPORT
```

```text
approved/hero_master.png          approved/character_model.blend
        ↓                                  ↓
exports/unity/hero.png            exports/unity/hero.fbx
exports/web/hero.webp             exports/render/hero_sprite.png
exports/roblox/hero_texture.png
```

**Approved는 공식 source의 의미를 가진다. Export는 특정 사용 환경에 맞게 파생된 결과다.**

Export는 Source of Truth가 아니며, 필요하면 다시 만들 수 있다. 그래서 export 파일을 직접 수정해 새로운 원본으로 삼지 않는다. 이 방향이 무너지면 어떤 파일이 진짜 원본인지 알 수 없게 된다.

---

## 10. EXPORT

Approved source를 **실제 게임 엔진, 플랫폼, 배포 환경에서 사용할 수 있도록 가공한 파생 결과물**이다.

> Unity용 sprite · Godot용 texture · Roblox texture · Web용 압축 이미지 · sprite atlas · tileset export · animation sheet · normal map · mask · optimized mesh · runtime format

### Export는 새로운 미적 승인이 아니다

정상적인 export는 승인된 source의 의미를 가능한 한 보존한다. resize · format conversion · compression 같은 기술적 처리다.

하지만 export 과정에서 시각적 결과가 달라지면 다시 검토가 필요할 수 있다.

> 축소 후 얼굴이 읽히지 않음 · 압축으로 색이 무너짐 · alpha edge 발생 · 엔진 filtering으로 픽셀이 흐려짐 · shader와 결합했을 때 outline이 과해짐

이 경우 export는 **기술적으로 성공했더라도 게임 아트로서는 문제가 있을 수 있다.** 실제 전달과 검증 절차는 `10_ENGINE_HANDOFF.md`가 다룬다.

---

## 11. Runtime 결과는 Lifecycle의 피드백이다

```text
APPROVED → EXPORT → RUNTIME TEST → REVIEW
```

문제가 없으면 현재 Approved source와 Export를 유지한다. 문제가 있으면 **원인의 위치부터 구분한다.**

```text
Source 문제   실루엣이 약함 · 색 구조가 배경과 충돌 · 디테일 과다
              → source 단계로 돌아가 수정한다

Export 문제   잘못된 resize · alpha 처리 · filtering · 압축
              → Approved source는 유지하고 Export만 다시 만든다

Engine 문제   lighting · shader · material · camera · post-processing · scale
              → 자산을 다시 그리기 전에 엔진 환경 문제인지 확인한다
```

> **실제 화면에서 실패했다고 항상 source asset을 수정하는 것은 아니다.**

이미 Approved된 자산이라도 게임 화면에서 문제가 발견되면 다시 Candidate 단계로 돌아갈 수 있다.

```text
APPROVED → RUNTIME ISSUE → REVISED CANDIDATE → REVIEW → NEW APPROVED
```

하지만 원인이 엔진 설정에 있다면 source의 승인을 취소할 필요가 없다. **항상 문제의 위치를 먼저 구분한다.** 계층별 진단의 상세는 `10_ENGINE_HANDOFF.md`가, 판단 기준은 `08_REVIEW_AND_APPROVAL.md`가 다룬다.

---

## 12. REJECTED · ON HOLD · SUPERSEDED

### REJECTED

현재 방향에서 채택하지 않기로 결정한 Candidate다. **쓸모없는 파일이라는 뜻은 아니다.** 반려 결과에는 어떤 방향이 맞지 않았는지, 어떤 요소가 과했는지, 어떤 기술적 접근이 실패했는지, 디렉터가 무엇을 원하지 않는지에 대한 정보가 남는다.

```text
Candidate B — Rejected
이유: 갑옷 밀도가 너무 높음 · 현재 게임의 단순한 실루엣 방향과 충돌
```

**Rejected를 자동으로 삭제하지 않는다.** 중요한 대표 자산의 비교 후보, 디렉터가 명확한 이유를 남긴 후보, 나중에 다른 방향에서 참고할 가능성이 있는 후보는 보존 가치가 있다. 다만 모든 실패 결과를 영구 보존해야 하는 것은 아니다.

그리고 **모든 실패가 Rejected는 아니다.** 17장을 참조한다.

### ON HOLD

현재 채택하지 않았지만 완전히 폐기하지도 않은 방향이다.

```text
REJECTED   현재 방향에서 채택하지 않음
ON HOLD    판단 또는 작업을 보류함
```

두 스타일 중 하나를 먼저 검증하기로 했거나 · 엔진 테스트 후 판단할 예정이거나 · 우선순위 때문에 일시 중단했거나 · 다른 자산이 확정된 후 다시 비교할 때 쓴다. **작은 프로젝트에서는 굳이 사용할 필요가 없다.**

### SUPERSEDED

과거에는 Approved였지만 새로운 Approved로 대체된 자산이다.

```text
hero_v1 Approved  →  hero_v2 새로 Approved  →  hero_v1 Superseded
```

중요한 것은 **과거 승인본이 "처음부터 잘못된 Candidate"로 바뀌는 것이 아니라는 점**이다. 그 자산은 당시에 실제로 Approved였고, 프로젝트가 발전하면서 현재 기준이 바뀐 것뿐이다. Superseded는 그 사실을 지우지 않는다.

대표 캐릭터 리디자인 · 큰 Art Direction 변경 · 플랫폼 변경 · 대규모 리마스터 · 게임 화면 검증 후 자산 교체 같은 경우에 유용하다. **작은 수정마다 Superseded를 남길 필요는 없고**, 버전 관리로 충분하다면 생략할 수 있다.

---

## 13. 수정은 새로운 Candidate를 만들 수 있다

Approved 자산에 수정이 필요하다고 해서 승인 파일을 무조건 덮어쓰지 않는다. 미적 변화가 포함되거나 결과가 아직 확정되지 않은 경우에는 다음이 안전하다.

```text
APPROVED → 수정 요청 → NEW CANDIDATE → REVIEW → APPROVED
```

```text
hero approved → "무기를 20% 줄여" → hero_weapon_small_candidate → 확인 → 새 approved
```

이때 **국소 수정 지시를 전체 재생성으로 확대하지 않는다.** "무기만 줄여"라는 지시에 얼굴·색감·포즈까지 함께 바뀌면 비교 자체가 불가능해지고, 이미 승인된 요소가 조용히 사라진다. 수정 범위를 어떻게 통제하는지는 `07_GENERATION_WORKFLOW.md`가 다룬다.

반대로 미적 판단이 개입하지 않는 단순 기술 수정 — 잘못된 파일명 수정 · 승인된 기준에 따른 포맷 변환 · 명확한 padding 수정 · 규격에 맞춘 crop — 은 기존 승인 상태를 유지한 채 처리할 수 있다. **모든 수정에 별도의 Candidate 단계를 만들 필요는 없다.**

---

## 14. 상태와 파일 위치는 같은 개념이 아니다

프로젝트 구조에서 `references/` · `candidates/` · `approved/` · `exports/` 폴더를 사용할 수 있다. 하지만 Lifecycle은 폴더 이름이 아니라 **자산의 의미**를 정의한다.

아직 정리되지 않은 임시 폴더에 있다고 해서 Candidate가 아닌 것은 아니고, 반대로 **`approved/` 폴더에 파일을 복사했다고 자동으로 Approved가 되는 것도 아니다.**

> **상태는 의미이고, 폴더는 그 의미를 관리하기 위한 구조다.**

정상적인 프로젝트에서는 둘을 일치시키는 것이 좋다. 폴더 구조 자체는 `03_PROJECT_STRUCTURE.md`가 정의한다.

---

## 15. Art Direction 변경과 Lifecycle

프로젝트의 Art Direction이 바뀌어도 **기존 Approved 자산을 자동으로 전부 Rejected로 바꾸지 않는다.** 먼저 영향 범위를 판단한다.

```text
"배경 contrast를 더 낮춘다"          → 캐릭터 Approved 자산에는 영향이 없을 수 있다
"모든 주요 캐릭터를 3등신으로 변경"    → 기존 캐릭터 Approved 자산은 재검토 대상이다
```

> **Art Direction의 변경과 개별 자산의 상태 변경을 자동으로 동일시하지 않는다.** 영향받는 자산만 재검토한다.

---

## 16. 파생 자산과 Asset Family

하나의 자산이 다른 자산에서 파생될 수 있다.

```text
Approved Hero → Red Team Variant · Blue Team Variant
Approved Portrait → Small UI Portrait · Dialogue Portrait · Roster Portrait
```

파생이 단순 기술 변환이면 원본 Approved 상태를 기반으로 export처럼 취급할 수 있다. 하지만 **파생 과정에 새로운 미적 판단이 필요하다면 별도의 Candidate / Approved 흐름을 거친다.** 팀 색상 variant가 단순 hue swap이 아니라 장비 디자인까지 바뀐다면 별도 Candidate가 적절하다.

계열 규칙이 개별 파일보다 먼저 승인될 수도 있다.

```text
기사 계열: 넓은 어깨 · 짧은 하체 · 큰 방패
```

이 방향이 승인되었다고 해서 **이후 모든 기사 자산이 자동으로 Approved가 되지는 않는다.** 승인된 것은 계열의 방향이고, 개별 자산은 필요에 따라 검토한다. 반대로 반복 제작 규칙이 매우 명확하고 위험이 낮다면 매번 같은 강도의 리뷰를 요구할 필요도 없다.

> **Lifecycle은 반복 작업에서 사람을 병목으로 만들기 위한 시스템이 아니다.**

---

## 17. 기술 실패와 미적 반려를 구분한다

```text
미적 반려   "실루엣이 현재 게임 방향과 맞지 않는다"   → 디자인 방향 자체의 수정이 필요할 수 있다
기술 실패   "alpha channel이 누락되었다"           → 수정 후 같은 디자인을 유지할 수 있다
```

따라서 `REJECTED`를 모든 문제에 기계적으로 사용하지 않는다. 단순 기술 오류는 Candidate가 실패했다기보다 **아직 검증을 통과하지 못한 상태**다.

그리고 검증의 강도는 단계에 따라 다르다. 초기 Concept에는 완전한 alpha 검사나 정확한 padding이 필요하지 않지만, 최종 sprite Candidate에서는 dimensions · alpha · palette · frame · naming이 중요해진다.

> **현재 단계의 목적에 맞는 수준의 검증을 한다.** 최종 Export에 가까워질수록 기술적 요구는 엄격해진다.

세부 검증 규칙은 `09_ASSET_SPEC_AND_VALIDATION.md`가 정의한다.

---

## 18. 자동화할 수 있는 부분과 없는 부분

```text
자동화할 수 있다    Candidate 파일 수집 · export 생성 여부 확인 · 기술 검사 결과 연결 ·
                  Manifest 일부 상태 갱신 · 승인 원본에서 파생 export 생성 · 누락 export 탐지

자동화하지 않는다   어떤 Candidate가 가장 매력적인가 · 어떤 디자인을 공식 자산으로 채택할 것인가 ·
                  게임의 분위기에 충분히 맞는가 · 언제 결과물이 충분히 좋은가
```

자동화는 상태를 관리하는 데 도움을 줄 수 있지만 **미적 승인 권한을 대신하지 않는다.**

---

## 19. 상태 이름을 늘리지 않는다

다음처럼 세밀한 상태를 끝없이 만드는 것은 이 체계의 방향이 아니다.

```text
READY_FOR_REVIEW · REVIEWING · CHANGES_REQUESTED · TECH_PASS · ART_PASS ·
WAITING_DIRECTOR · WAITING_EXPORT · RUNTIME_TESTED · NEEDS_FIX ...
```

기본 상태는 다음으로 충분해야 한다.

```text
REFERENCE · CONCEPT · CANDIDATE · APPROVED · EXPORT
선택적: REJECTED · ON HOLD · SUPERSEDED
```

그 밖의 상황 — 기술 검사를 통과했는지, 리뷰를 기다리는지, 수정 중인지, runtime 확인이 끝났는지 — 은 **기존 상태 + 검증 정보 + Review Log**로 표현한다. `ASSET_MANIFEST.md`의 검증 칸과 메모가 그 자리이며, 그 칸의 내용은 상태 칸을 바꾸지 않는다.

이 체계의 장점은 lifecycle을 과도하게 세분화하지 않는 데 있다.

---

## 20. 깊이는 자산의 중요도에 비례한다

간단한 UI 아이콘 하나라면 이 정도로 충분하다.

```text
CANDIDATE → APPROVED → EXPORT
```

규칙이 이미 명확한 반복 아이콘이라면 실무적으로 `제작 → 기술 확인 → 사용`으로 처리할 수도 있다.

반대로 대표 캐릭터처럼 중요하고 방향성이 큰 자산은 더 깊게 다룬다.

```text
REFERENCE → CONCEPT → MULTIPLE CANDIDATES → DIRECTOR REVIEW →
REVISED CANDIDATE → APPROVED → ENGINE TEST → REVIEW → FINAL EXPORT
```

> **Lifecycle의 깊이는 자산의 중요도와 불확실성에 비례한다.**

기록도 마찬가지다. 거대한 데이터베이스를 만들 필요는 없지만, 중요한 자산에서는 현재 상태 · 현재 공식 Approved가 무엇인지 · 어떤 Candidate가 대체되었는지 · export가 존재하는지 · 중요한 승인이나 반려 이유가 있는지 정도는 알 수 있는 것이 좋다. Markdown만으로 충분한 경우가 많다.

---

## 21. Lifecycle과 버전 관리

Git이 있어도 Lifecycle을 대체하지 않는다.

```text
버전 관리   파일이 언제 어떻게 변경되었는가
Lifecycle  이 파일이 프로젝트에서 어떤 의미를 가지는가
```

`hero_v4.png`가 최신 commit이라고 해서 Approved라는 뜻이 아니고, 반대로 과거 commit의 파일이 현재 Approved일 수도 있다. **파일 버전과 Lifecycle 상태를 동일시하지 않는다.**

---

## 22. 다른 문서와의 관계

이 문서는 **상태의 의미와 경계**만 정의한다. 나머지는 각 담당 문서를 따른다.

- **`03_PROJECT_STRUCTURE.md`** — 상태를 담는 폴더 구조와 원본·파생물의 분리를 정의한다.
- **`07_GENERATION_WORKFLOW.md`** — 실제 제작 순서, 어떤 문서를 먼저 읽는지, Candidate를 어떻게 준비하는지, 반복 수정 루틴을 정의한다.
- **`08_REVIEW_AND_APPROVAL.md`** — Technical Review와 Art Review의 차이, 승인 시 무엇을 확인하는지, 디렉터에게 결과를 어떻게 제시하는지를 정의한다. `CANDIDATE → APPROVED`는 이 문서가 정의하는 **Director Approval**을 통해 일어난다.
- **`09_ASSET_SPEC_AND_VALIDATION.md`** — dimensions · alpha · palette · format · frame · tile seam · naming 등 기술 검증을 정의한다. **Technical Fail은 미적 Rejected를 의미하지 않는다.**
- **`10_ENGINE_HANDOFF.md`** — Approved source에서 export를 만드는 과정, 엔진 import, runtime 검증, 문제 계층의 구분을 정의한다.
- **`11_LEARNING_AND_REUSE.md`** — 반려와 수정에서 무엇을 학습으로 남기고 무엇을 Studio 공통 지식으로 승격할지 정의한다.
- **`templates/ASSET_MANIFEST.md`** — 실제 자산들이 현재 어느 상태인지 기록한다. 상태 이름은 이 문서의 것을 그대로 쓰고, 새 상태를 만들지 않는다.
- **`templates/ASSET_BRIEF.md`** — 무엇을 만들어야 하는지를 정의한다. **Brief에는 상태 전이 규칙을 넣지 않는다.**
- **`templates/REVIEW_LOG.md`** — 중요한 승인과 반려의 이유를 보존한다. Lifecycle은 상태를 정의하고 Review Log는 그 상태에 이른 판단을 남긴다. **모든 상태 변경을 Review Log에 남길 필요는 없고, Review 결과 자체가 새로운 lifecycle 상태가 되지도 않는다.**

---

## 23. Lifecycle에서 가장 중요한 질문

현재 자산을 볼 때 이 정도면 충분하다.

```text
REFERENCE?   방향 이해를 위한 참고 자료인가
CONCEPT?     탐색을 위한 결과인가
CANDIDATE?   실제 채택 가능한 구체적 후보인가
APPROVED?    디렉터가 공식 자산 또는 공식 source로 채택했는가
EXPORT?      Approved source에서 특정 환경을 위해 파생된 결과인가
```

필요하면 다음을 덧붙인다.

```text
REJECTED?    현재 방향에서 채택하지 않기로 한 후보인가
ON HOLD?     판단을 보류한 방향인가
SUPERSEDED?  과거에는 Approved였지만 현재 승인본으로 대체되었는가
```

---

## 24. 핵심 원칙 요약

Asset Lifecycle은 자산을 통제하기 위한 승인 시스템이 아니다. 목적은 현재 결과물이 무엇을 의미하는지 분명하게 유지하는 것이다.

> **생성된 결과는 자동으로 승인된 자산이 아니다.**

> **Reference와 Approved를 혼동하지 않는다. Reference는 제작 과정에 병렬로 존재하는 입력 자료다.**

> **Candidate와 Approved를 구분한다. Technical Pass는 Director Approval이 아니다.**

> **Approved source와 engine-ready Export를 구분한다. Export는 파생물이며 다시 만들 수 있다.**

> **Approved source는 보호 대상이며, 승인을 바꿀 수 있는 것은 디렉터뿐이다.**

> **실제 게임 화면에서 문제가 발견되면 Lifecycle은 이전 단계로 돌아갈 수 있다. 다만 원인이 source인지 export인지 engine인지 먼저 구분한다.**

> **국소 수정 지시를 전체 재생성으로 확대하지 않는다.**

> **반려된 결과도 학습 정보가 될 수 있지만, 자동으로 프로젝트 전체 규칙으로 일반화하지 않는다.**

> **Superseded는 과거의 승인 사실을 지우지 않는다.**

> **상태는 파일 위치가 아니라 자산의 의미다.**

> **상태 이름을 불필요하게 늘리지 않는다.**

> **작은 자산에는 가볍게, 중요한 자산에는 필요한 만큼 깊게 적용한다.**

> **Lifecycle은 사람의 미적 판단을 제거하기 위한 workflow engine이 아니다.**

> **최종적으로 중요한 것은 상태 관리 자체가 아니라, 좋은 게임 아트를 안전하게 공식 자산으로 정착시키는 것이다.**
