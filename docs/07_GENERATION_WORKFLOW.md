# 07_GENERATION_WORKFLOW

## 1. 문서의 역할

이 문서는 실제 자산 제작 요청이 들어왔을 때 사용하는 **기본 작업 루틴**을 정의한다.

이 문서는 특정 생성기의 사용법도, 특정 게임의 스타일도 정의하지 않는다. Asset Lifecycle의 상태 정의를 다시 설명하지 않고, Review & Approval의 판단 기준을 대신하지도 않는다.

핵심 질문은 하나다.

> **하나의 아트 작업 요청이 들어왔을 때, Art Studio는 무엇을 먼저 확인하고 어떤 순서로 제작·검토·수정하여 공식 자산 후보로 발전시키는가?**

절대적인 자동 파이프라인이 아니라, Claude Code와 디렉터가 반복적으로 사용할 수 있는 **실전 제작 루틴**이다.

`06_ASSET_LIFECYCLE.md`가 "이 결과물은 지금 어떤 상태인가"를 정의한다면, 이 문서는 "작업자는 실제로 무엇을 어떤 순서로 하는가"를 정의한다. 둘은 연결되지만 같은 문서가 아니다.

---

## 2. 기본 흐름

```text
프로젝트 확인
↓
Project Brief · Art Direction 확인
↓
현재 요청과 목표 확인
↓
Asset 요구 구체화
↓
기존 자산 · Reference 확인
↓
제작 방식 선택
↓
Candidate 제작
↓
단계에 맞는 기술 검사
↓
Director Review
↓
수정
↓
Approved 정리
↓
필요 시 Export / Runtime Validation
```

**이 흐름을 모든 작업에 동일하게 강제하지 않는다.** 단계를 생략할 수도, 여러 번 반복할 수도, 순서를 바꿀 수도 있다. 이미 승인된 방향을 반복하는 작업이라면 빠르게 진행한다.

핵심은 순서 자체가 아니다.

> **무엇을 만드는지, 어떤 게임을 위한 것인지, 어떤 방향을 따라야 하는지, 무엇을 비교해야 하는지, 무엇이 기술적으로 필요한지를 먼저 이해하고 제작한다.**

---

## 3. Workflow는 생성기 중심이 아니다

도구 이름으로 작업 순서를 고정하지 않는다. "모든 캐릭터는 PixelLab, 모든 배경은 FLUX" 같은 구조를 만들지 않는다.

```text
문제 → 필요한 결과 → 필요한 capability → 적절한 제작 방법 → 현재 사용 가능한 도구
```

같은 종류의 자산이라도 프로젝트마다 경로가 달라진다.

```text
캐릭터 A   이미지 생성 → 수정 → 승인
캐릭터 B   3D blockout → render → paintover → pixel conversion → 후보 비교 → 승인
```

**도구는 workflow의 주인이 아니다.**

---

## 4. 작업 시작 전 문맥 확인

### 어느 게임 프로젝트의 작업인가

여러 게임을 동시에 다루는 Art Studio에서 프로젝트를 잘못 잡는 것은 단순한 파일 위치 오류가 아니다. 다른 프로젝트의 레퍼런스 · 팔레트 · 비율 · 승인 자산 · 금지사항 · 디렉터 결정을 잘못 적용하게 된다.

필요에 따라 프로젝트 ID · 작업 공간 · 연결된 게임 저장소 · 관련 문서 · 기존 승인 자산 · 최근 중요한 디렉터 결정을 확인한다. **문맥상 프로젝트가 명확하다면 매번 다시 묻지 않는다.**

### Project Brief — 이 게임은 무엇인가

장르 · 플랫폼 · 카메라 · 플레이 구조 · 세계 · 주요 시각 대상 · 자산을 보는 거리 · 개발 단계 · 담당 범위 · 기술 제약 중 **현재 자산에 영향을 주는 정보만** 가져온다. 매번 전체를 요약하지 않는다.

```text
요청: 플레이어 캐릭터 제작
필요한 정보: 3인칭 · 모바일 대응 · 전투 중 표시 크기가 작음 · 적과 아군을 빠르게 구분해야 함
```

### Art Direction — 이 게임은 어떻게 보여야 하는가

Direction Summary · 형태 언어 · 실루엣 · 캐릭터/환경 방향 · 색 · 명암 · 질감 · 조명 · 플레이 가독성 · References · Anti-References · 금지사항 · 대표 승인 자산 중 현재 자산과 관련 있는 항목을 우선한다.

특히 다음을 구분한다.

```text
확정된 방향  ≠  탐색 중인 방향
```

**탐색 중인 아이디어를 이미 확정된 규칙처럼 사용하지 않는다.**

### Style Spec — 어떤 수치를 따라야 하는가

`STYLE_SPEC.md`가 있다면 이번 자산에 필요한 규격(sprite dimensions · tile size · palette target · outline · texture dimensions · animation frame range · filtering · alpha · rendering constraint)을 확인한다.

아직 없거나 일부 값이 미정일 수 있다. **그 경우 임의로 빈칸을 채워 프로젝트 규칙으로 확정하지 않는다.** 값이 실제로 필요하다면 기존 승인 자산에서 확인하거나, 프로젝트의 다른 자료에서 찾거나, 후보 값으로 제안하거나, 중요한 항목이면 선택지를 정리해 디렉터 판단을 받는다.

---

## 5. 요청을 이해하고 목표를 정의한다

디렉터의 요청이 짧아도 유효한 작업 요청이다.

> "주인공 얼굴 세 개만 봐보자." · "무기가 너무 크다. 줄여." · "이 스타일로 마을 건물 몇 개 더." · "배경에 묻힌다." · "좀 더 싸구려 느낌." · "이걸 실제 게임에 넣어봐."

**이런 요청을 거대한 양식으로 되묻지 않는다.** 현재 문맥을 읽고 작업 가능한 요구로 해석한다.

```text
사용자의 표현 → 현재 프로젝트 문맥 → 실무적 해석 → 제작 작업
```

```text
디렉터: "좀 더 투박하게."
해석 후보: 형태를 더 단순한 큰 덩어리로 · 표면을 지나치게 매끈하게 만들지 않음 ·
          장식 밀도 감소 · 불규칙한 edge나 재질 variation 허용
```

**원래 표현을 임의로 다른 의도로 바꾸지 않는다.**

그리고 작업 시작 전에 세 가지가 분명해야 한다. 이 셋은 서로 다를 수 있다.

- 무엇을 만드는가
- 무엇을 판단하려는가
- 결과는 어디까지 완성되어야 하는가

```text
주인공 얼굴 방향 탐색      → 최종 초상화가 아니라 비율과 인상을 결정하기 위한 Concept 비교
벽돌 타일 제작            → 게임에 바로 넣을 수 있는 seamless tile Candidate
승인 캐릭터 Roblox 테스트  → 새 디자인이 아니라 runtime scale과 readability 검증
```

**목표가 달라지면 필요한 완성도와 도구도 달라진다.**

---

## 6. 요구를 구체화한다

### Asset Brief를 만들 것인가

**모든 작업에 `ASSET_BRIEF.md`를 만들지 않는다.**

```text
유용한 경우    주인공 · 보스 · 주요 NPC · 중요한 몬스터 · 핵심 건물 · 대표 UI ·
              중요한 VFX · 여러 도구가 관여하는 자산 · 반복 수정 가능성이 높은 자산

불필요한 경우  단순한 반복 아이콘 · 명확한 규칙의 색상 variant ·
              이미 승인된 계열의 단순 파생물 · 사소한 cleanup
```

Brief가 없다면 현재 요청과 기존 문서를 바탕으로 필요한 요구를 최소한으로 정리한다.

### 정리하는 항목

현재 작업 수준에 맞게 필요한 것만 정리한다. **거대한 spec 작성으로 만들지 않는다.**

- **역할** — 이 자산이 게임에서 무엇인가
- **기능** — 플레이 중 무엇을 전달해야 하는가
- **표시 조건** — 멀리서 보는가 · 작은 아이콘인가 · 화면을 크게 차지하는가 · 빠르게 움직이는가
- **반드시 들어갈 요소** — 특정 장비 · 시대적 특징 · 팀 구분 요소 · 기능적 표식
- **피해야 할 요소** — 금지된 스타일 · 시대에 맞지 않는 요소 · 기존 승인 방향과 충돌하는 형태
- **필요한 variant** — 방향 · 색상 · 장비 · 상태 · animation
- **기술 제약** — 현재 알려진 범위만

---

## 7. 기존 자산과 Reference를 확인한다

### 새로 만들기 전에 이미 있는 것을 본다

관련 Approved asset · 같은 계열의 캐릭터 · 기존 Candidate · 이전 Concept · 기존 Export · screenshot · 사용 중인 외부 에셋.

이 확인이 막아주는 것 — 이미 만든 것을 다시 생성 · 승인된 형태 언어와의 충돌 · 불필요한 스타일 drift · 중복 제작 · 이전 디렉터 결정을 잊는 것.

**같은 asset family의 기존 승인 자산은 매우 강한 기준점이다.**

### Reference

현재 작업에 필요한 정도만 확인한다. 매번 전부 읽거나 분석할 필요는 없다. 중요한 질문은 하나다.

> **이번 자산에서 어떤 Reference의 어떤 속성을 참고하는가?**

```text
Reference A → 캐릭터 비율      Reference C → 재질 밀도
Reference B → 갑옷의 시대감    Reference D → 조명
```

**여러 Reference를 이유 없이 하나의 스타일로 섞지 않는다.** 무엇을 가져오지 않을지도 함께 정한다("A에서 실루엣은 참고, 색은 참고하지 않음").

### Research는 필요할 때만 한다

Art Direction이 명확하고, 승인 자산이 충분하고, 반복 작업이라면 추가 Reference 없이 바로 제작할 수 있다.

반대로 시대 고증이 중요하거나 · 형태를 이해하기 어렵거나 · 새로운 자산 종류이거나 · 관련 시각 자료가 부족하거나 · 디렉터가 여러 방향을 비교하려 한다면 Reference 탐색이 유용하다.

---

## 8. 제작 방식 선택

> **이 자산을 어떤 방식으로 만드는 것이 가장 적합한가?**

고려할 수 있는 요소 — 결과물 종류 · 표현 방식 · 요구 해상도 · 방향 일관성 · 동일 캐릭터 반복성 · animation 필요 여부 · tile seamlessness · 정확한 layout 필요 여부 · 예상 수정 횟수 · batch 규모 · 엔진 효과 의존도 · 사람이 직접 하는 편이 빠른가 · 기존 source 활용 가능 여부 · 사용 가능한 도구.

**도구는 이 판단 이후에 선택한다.**

### 가장 단순한 적절한 방법을 우선한다

복잡한 제작법을 전문성의 증거로 취급하지 않는다. `한 번 생성 → 간단한 cleanup → review`로 해결되는 작업을 굳이 여러 도구를 거치는 경로로 만들지 않는다.

반대로 정확한 방향 sprite나 복잡한 perspective consistency가 필요하다면 여러 단계가 오히려 더 안정적인 해법일 수 있다.

> **기준은 단계 수가 아니라 문제를 얼마나 안정적으로 해결하는가다.**

### 불확실하면 작은 테스트를 먼저 한다

```text
80개 캐릭터 생성 예정  →  먼저 2개 캐릭터 × 2개 방식 → 결과 비교 → 제작 방식 결정
타일 전체 세트 제작 전  →  대표 타일 1개로 seam / scale / engine result 검증
```

잘못된 제작법을 대량으로 반복하는 것을 막는다.

---

## 9. Concept 단계가 필요한지 판단한다

Concept이 유용한 경우 — 전체 방향이 아직 탐색 중 · 대표 캐릭터 디자인 · 새로운 몬스터 계열 · 중요한 환경 언어 · UI 그래픽 언어 · 주요 VFX 스타일 · 여러 형태 방향이 모두 가능한 경우.

Concept에서는 완성도보다 **방향 차이를 명확하게** 만든다.

```text
A  넓고 낮은 실루엣
B  길고 날카로운 실루엣
C  비대칭 장비 중심
```

거의 같은 이미지 세 개보다 서로 다른 판단 가능한 방향을 만드는 편이 낫다.

---

## 10. Candidate 제작

Candidate는 다음을 반영한다 — 현재 Art Direction · 해당 자산 요구 · 필요한 Reference · 기존 승인 자산과의 관계 · 현재 기술 제약 · 디렉터의 최신 지시.

**모든 Candidate를 같은 방식으로 만들 필요는 없다.** A는 생성 모델, B는 Blender render + paint, C는 수작업이어도 된다. 중요한 것은 제작 방법이 아니라 **비교 가능한 결과**다.

### 후보 수를 고정하지 않는다

"항상 4개" 같은 기본값을 만들지 않는다.

```text
1개       방향이 이미 명확 · 반복 제작 · 단순 수정 · 작은 자산
2~4개     중요한 디자인 비교 · 형태 방향 탐색 · 색상 방향 탐색
더 많이    자동 batch 탐색이 실제로 의미 있고 넓은 범위에서 좁혀야 할 때
```

후보가 많다고 좋은 workflow가 아니다. **디렉터가 차이를 판단할 수 있는 의미 있는 후보가 중요하다.**

### 변형에는 목적이 있어야 한다

Variation은 random seed 반복이 아니다. 각 후보의 차이를 설명할 수 있어야 한다.

```text
A  더 큰 머리 / 단순 갑옷        A  저채도
B  현실 비율 / 큰 무기      또는  B  높은 캐릭터 대비
C  짧고 넓은 몸 / 작은 무기       C  따뜻한 환경 편향
```

무엇이 다른지 알 수 없는 후보를 많이 만드는 것은 디렉터의 판단 부담만 늘린다.

### 생성 결과가 곧 Candidate는 아니다

Raw generation은 다음 단계의 source일 수 있다.

```text
raw generation → crop → cleanup → color correction → manual correction → Candidate
3D render → generator edit → pixel conversion → manual pixel cleanup → Candidate
```

**생성기가 한 번에 완성 파일을 만들어야 한다는 전제를 두지 않는다.**

### 중간 결과를 모두 보존하지 않는다

test render · intermediate mask · temporary upscale · failed crop · debug image · raw output을 모두 공식 Candidate로 관리하지 않는다. 보존 가치가 높은 것은 중요한 비교 후보 · 재현에 필요한 source · 승인 과정에 사용된 결과 · 제작법 판단에 의미 있는 테스트다.

---

## 11. 기술 검사는 단계에 맞게 한다

```text
Concept        기술 규격보다 방향 탐색이 우선한다
Candidate      비교와 판단에 필요한 기술 상태를 확보한다
Approved 직전   실제 사용에 필요한 주요 제약을 더 엄격하게 확인한다
Export         engine-specific requirement가 중요해진다
```

**모든 단계에서 최종 수준의 validation을 강제하지 않는다.**

그리고 기술 검사는 미적 리뷰를 대신하지 않는다. dimensions · alpha · palette · format이 모두 정상이라고 좋은 디자인은 아니고, 반대로 wrong dimensions에 rough edge를 가진 Concept이 방향 탐색에는 매우 유용할 수 있다.

세부 기준은 `09_ASSET_SPEC_AND_VALIDATION.md`, 판단 경계는 `08_REVIEW_AND_APPROVAL.md`가 정의한다.

---

## 12. Director Review 준비

### Claude의 중간 분석

디렉터에게 보여주기 전에 먼저 확인할 수 있다 — 명백한 누락 · 기존 Art Direction과의 충돌 · technical issue · 후보 사이의 차이 · 작은 화면 가독성 위험 · Reference와의 관계 · 기존 승인 자산과의 inconsistency.

다만 **Claude가 미적 후보를 자동으로 탈락시키는 시스템을 만들지 않는다.** 명백한 기술 실패는 걸러낼 수 있지만, 미적 판단이 필요한 결과는 디렉터가 볼 가치가 있다.

### 제시 방식

디렉터는 기술 과정 전체를 볼 필요가 없다. 판단에 필요한 결과를 정리해서 보여주고, 필요하면 차이를 짧게 설명한다.

```text
A  실루엣 가장 단순 / 장비 작음
B  얼굴 강조 / 현재 승인 캐릭터와 가장 유사
C  가장 과장됨 / 작은 화면에서 식별력이 높을 가능성
```

디렉터가 generator parameter, script log, 내부 파일 처리 순서를 매번 읽어야 하는 시스템을 목표로 하지 않는다.

### 비교 조건을 통제한다

차이가 제작 조건 때문인지 디자인 때문인지 구분할 수 있어야 한다. 가능하면 같은 canvas size · background · camera · pose · lighting · 표시 scale을 사용한다.

물론 완전히 다른 방향을 탐색하는 Concept 단계에서는 모든 조건을 같게 만들 필요가 없다. **비교 목적에 맞게 통제한다.**

---

## 13. 피드백을 수정 작업으로 변환한다

디렉터는 짧게 말한다.

> "2번이 좋은데 무기만 줄여." · "얼굴이 너무 착해." · "갑옷이 너무 비싸 보여." · "배경에 묻힌다." · "이쪽은 너무 AI 같다." · "조금 더 낡게." · "이 방향은 아니다."

Claude는 이를 현재 프로젝트 문맥과 연결해 실제 수정 가능한 요구로 변환한다.

```text
"무기만 줄여"
→ 기존 승인/선호 디자인의 나머지 비율은 유지
→ weapon silhouette과 body ratio 관계만 수정
→ 전체 스타일 변경으로 확대하지 않음
```

### 국소 피드백을 전역 규칙으로 확대하지 않는다

"이 보스는 outline 없이 가자"를 "게임 전체 캐릭터 outline 제거"로 해석하지 않는다. 수정 지시의 적용 범위를 구분한다.

```text
project-wide · category-wide · asset family · individual asset
```

범위가 명확하면 그대로 적용한다. 불명확하지만 영향이 작으면 국소적으로 처리한다. **영향이 크면 기존 Art Direction과 Review 기록을 먼저 확인한다.**

### 수정은 기존 방향을 보존하면서 한다

"무기만 줄여"인데 얼굴 · 갑옷 · 색감 · 포즈가 함께 바뀌면 비교 자체가 어려워진다. **가능하면 수정 범위를 통제한다.** 생성형 도구에서 특히 중요하다.

### 반복 실패 시 같은 방법만 고집하지 않는다

```text
문제: 동일 캐릭터의 8방향 일관성이 계속 깨짐
대응: 다른 생성 도구 · 전문 directional sprite tool · 3D source ·
      manual correction · 기존 source에서 회전/보정

문제: 생성기가 정확한 UI icon geometry를 계속 실패
대응: vector tool · code-based shape · manual drawing
```

제작 방식이 바뀌는 것은 workflow 실패가 아니라 문제에 맞는 방법을 찾아가는 정상적인 과정이다. **도구를 유지하는 것보다 결과가 중요하다.**

> **디자인 요구를 자동화 편의에 맞춰 임의로 낮추지 않는다.**

---

## 14. 승인과 정리

Candidate가 충분히 검토되면 디렉터가 채택한다. 판단 기준은 `08_REVIEW_AND_APPROVAL.md`가 다루고, 이 문서에서는 하나만 유지한다.

> **디렉터의 채택 의도가 명확할 때 Candidate를 Approved로 정리한다. Claude의 추천만으로 자동 승인하지 않는다.**

승인 후에는 필요에 따라 공식 source · 관련 제작 source · 필요한 metadata · 중요한 prompt나 parameter · 승인 대상 · asset ID · 향후 수정에 필요한 파일을 정리한다. **모든 생성 로그를 보존할 필요는 없다.** 다시 만들거나 수정하는 데 실제로 필요한 정보 위주로 남긴다.

그리고 **Approved라고 해서 항상 즉시 모든 export를 만들지 않는다.** 아직 engine integration 단계가 아니거나, 플랫폼이 확정되지 않았거나, 다른 자산을 먼저 승인해야 하거나, source library 구축 단계일 수 있다. 필요한 시점에 export한다. 반대로 실제 게임 화면 검증이 중요한 자산이라면 빠르게 export해서 runtime test를 한다.

---

## 15. Runtime Validation은 제작의 일부가 될 수 있다

캐릭터 · tile · VFX · UI icon · environment · 조명에 의존하는 자산은 이미지 파일만 보고 판단하기 어렵다.

```text
Candidate 또는 Approved source → temporary export → engine import →
actual game screenshot → review
```

**runtime test를 "제작이 끝난 후의 별도 QA"로만 보지 않는다.** 아트 제작 자체의 일부가 될 수 있다.

runtime에서 문제를 발견하면 **원인을 먼저 분리한다.** "캐릭터가 배경에 묻힌다"의 원인은 asset(silhouette · value contrast · 색 분리) · environment(배경 detail이나 contrast 과다) · engine(lighting · shader · material · post-processing) · camera(표시 크기 · distance · FOV) 중 어디든 될 수 있다.

> **무조건 캐릭터 이미지를 다시 생성하지 않는다.** 원인을 구분하고 가장 적절한 지점을 수정한다.

계층 구분의 상세는 `10_ENGINE_HANDOFF.md`가 다룬다.

---

## 16. 반복 제작과 Batch

하나의 승인 자산이나 asset family가 기준으로 잡히면 반복 생산 단계로 들어갈 수 있다.

```text
기사 기본 방향 승인 → 기사 12종 제작
```

이때 매 자산마다 처음부터 전체 Concept 과정을 반복하지 않는다. 승인된 family rule · Style Spec · Asset Brief 또는 Manifest · 기존 승인 자산을 기준으로 빠르게 제작한다. **다만 반복 생산 중에 스타일 drift가 보이면 다시 검토한다.**

자산 수가 많아지면 batch를 사용한다 — 동일 규격 resize · palette check · sprite packing · 대량 generation · variant 생성 · naming · export.

```text
샘플 → 검증 → batch
```

**잘못된 규칙을 100개 파일에 적용한 뒤 수정하는 것보다 낫다.**

새 자산을 만들 때 기존 Approved asset을 기준으로 활용할 수 있다(proportion · palette · material · silhouette family · lighting · animation timing). 다만 구분한다.

```text
기존 승인 자산을 기준으로 사용  ≠  그 자산을 그대로 복제
```

새 자산의 역할과 개성은 유지한다.

---

## 17. 자동화의 위치

**자동화에 적합한 것** — 반복 생성 호출 · 파일 수집 · rename · conversion · resize · validation · contact sheet 생성 · metadata 기록 · export · batch processing.

**자동화 목표로 삼지 않는 것** — 최종 디자인 선택 · 매력 평가 · 프로젝트 정서 결정 · 세계관 적합성의 최종 판단 · "충분히 좋은가"의 결정.

> **자동화는 workflow를 지원한다. workflow가 자동화를 위해 존재하는 것은 아니다.**

디렉터는 어떤 script를 실행했는지, 파일을 어느 임시 폴더로 옮겼는지, 어떤 API 요청 형식을 썼는지, 어떤 batch command를 사용했는지 매번 알 필요가 없다. 디렉터가 판단해야 하는 것은 방향 · 후보 · 차이 · 수정 · 최종 결과다. **Art Studio가 기술적 잡무를 흡수한다.**

반대로 결과에 직접 영향을 주는 제작 판단은 짧게 설명한다.

> 이 자산은 8방향 일관성이 중요해서 일반 이미지 생성보다 3D 기준 source를 먼저 만들었다.
> 이 타일은 반복 seam이 중요하므로 한 장 이미지보다 seamless generation + tile test 방식으로 만들었다.

장황한 도구 보고서는 필요 없다. 디렉터가 결과의 성격을 이해할 정도면 충분하다.

---

## 18. 언제 멈추고 언제 진행하는가

### 멈추고 선택지를 정리하는 경우

Claude는 다음 상황에서 큰 미적 결정을 임의로 확정하지 않는다.

- **Art Direction이 없는 상태에서 대표 스타일을 결정해야 한다** — 예: 주인공 스타일 자체가 미정
- **서로 다른 방향이 모두 합리적이다** — A와 B가 모두 가능하고 선택이 전체 방향에 큰 영향을 준다
- **기존 승인 방향과 충돌한다** — 현재 요청이 대표 캐릭터나 Art Direction을 크게 바꿀 수 있다
- **기술 제약이 디자인 자체를 바꿔야 할 정도로 크다** — 기존 방향을 유지하기 어려운 플랫폼 제약

이때는 문제와 선택지를 정리한다. 멈춘다는 것은 손을 놓는다는 뜻이 아니다.

### 묻지 않고 진행하는 경우

규칙이 명확하다면 자율적으로 처리한다.

> 승인된 asset resize · format conversion · naming 적용 · alpha cleanup · 정해진 규격의 export · 동일한 패턴의 반복 자산 · 이미 승인된 수정 지시의 적용 · 기술 검사 · 되돌릴 수 있는 파일 정리 · 후보 비교 자료 생성

> **사람 중심 디렉팅은 사람에게 모든 작은 작업을 물어보는 시스템을 의미하지 않는다.**

---

## 19. 작업 복잡도에 따라 깊이를 조절한다

```text
Level A — 단순 작업        작은 icon · color variant · format conversion · 명확한 반복 asset
요구 확인 → 제작 → 기술 확인 → 승인/사용

Level B — 일반 제작        일반 캐릭터 · 몬스터 · 환경 prop · 대표 tile
문맥 확인 → 요구 정리 → reference → candidate → review → 수정 → approved

Level C — 방향성 높은 핵심 자산   주인공 · 대표 보스 · 핵심 환경 · 전체 스타일을 결정하는 자산
Project Brief → Art Direction → reference analysis → concept exploration →
candidate comparison → director review → revision → approved →
runtime validation → refinement
```

**이 레벨을 공식 status system으로 관리하지 않는다.** 작업을 얼마나 깊게 다뤄야 하는지 판단하기 위한 사고 방식이다.

### Workflow가 무거워졌는지 확인한다

- 작은 아이콘 하나에도 별도 Brief가 필요하다
- 모든 작업에 후보 4개를 강제한다
- 매 resize마다 디렉터 승인이 필요하다
- 모든 생성 결과를 영구 보존한다 · 모든 feedback을 문서화한다
- 실제 제작보다 metadata 작성 시간이 더 길다
- 도구를 많이 쓰는 것이 품질보다 중요해진다
- 자동화하기 쉬운 방향으로 디자인을 바꾼다

### 너무 가벼워졌는지도 확인한다

- Project Brief를 보지 않고 그림부터 만든다
- 다른 게임의 스타일을 섞는다
- Reference와 Approved를 구분하지 않는다
- 모든 생성 결과를 바로 게임에 넣는다
- 디렉터가 고른 결과를 기록하지 않는다
- 실제 게임 화면에서 검증하지 않는다
- 기술 규격을 계속 잊고 같은 실패를 반복한다

> **Workflow의 목적은 절차를 늘리는 것이 아니라 이런 반복적인 실수를 막는 것이다.**

---

## 20. 기록과 완료의 의미

### 실패에서 다음 작업으로 이어지는 정보

```text
실패: 캐릭터 얼굴이 너무 사실적임
다음: 얼굴 plane 단순화 · 눈/코/입 디테일 감소 · 기존 승인 캐릭터의 facial density와 비교
```

이 정보가 반복되면 프로젝트의 아트 방향이나 제작 지식으로 남길 가치가 생긴다. **한 번의 실패를 즉시 전체 규칙으로 일반화하지 않는다.** 승격 기준은 `11_LEARNING_AND_REUSE.md`가 정의한다.

### 제작 정보의 기록 수준

재현이나 수정에 도움이 되는 정보(사용한 source · 중요한 prompt · seed · generator/model · tool version · manual edit note · render setup · 주요 parameter)는 필요에 따라 남긴다. **모든 작업을 연구 실험처럼 기록하지 않는다.**

기록 수준은 재생성 가능성 · 대표 자산 여부 · 반복 production에 쓸 방식인지 · tool-specific 재현성의 중요도 · 나중에 수정할 가능성에 따라 달라진다.

### "완료"의 의미

```text
Concept 완료          디렉터가 다음 방향을 선택할 수 있을 만큼의 탐색 결과가 준비됨
Candidate 완료        실제 채택 여부를 판단할 수 있는 결과가 준비됨
Approved source 완료  디렉터가 공식 source로 채택하고 필요한 원본이 정리됨
Engine-ready 완료     필요한 export와 runtime validation까지 끝남
```

> **"파일 하나 생성됨"을 작업 완료로 자동 해석하지 않는다.**

---

## 21. Art Studio가 직접 만들지 않은 자산

외주 · 구매 에셋 · 사람이 직접 만든 원본에도 같은 흐름이 적용된다. **Art Studio가 직접 생성하지 않았다는 이유로 Lifecycle이나 Review의 의미가 달라지지 않는다.**

```text
외부 제작    Art Direction → Asset Requirement → External Production →
            Candidate → Review → Revision → Approved

구매 에셋    필요 자산 확인 → 구매 후보 탐색 → license 확인 →
            프로젝트 적합성 검토 → 필요한 수정 → Candidate / Approved → Export

수작업 원본  hand-painted source → cleanup → technical validation → approved → export
```

**구매했다는 사실이 자동 승인은 아니다.** 프로젝트 아트 방향과 실제 게임 화면에 적합한지 확인한다. 반대로 이미 디렉터가 승인한 원본이라면 Candidate 단계를 생략하고 Approved source로 받아들일 수 있다.

이 경우 Art Studio는 Brief 정리 · Reference 정리 · 결과 비교 · technical validation · export를 담당할 수 있다.

---

## 22. 권장 기본 루틴

일반적인 자산 제작에서 사용할 수 있는 순서다.

```text
1.  프로젝트 확인
2.  Project Brief 확인
3.  Art Direction 확인
4.  Style Spec / 기존 승인 자산 확인
5.  현재 요청의 목적 파악
6.  Asset 요구 정리
7.  필요한 Reference 확인
8.  제작 방식 선택
9.  Candidate 제작
10. 단계에 맞는 기술 검사
11. 비교 가능한 형태로 정리
12. Director Review
13. 피드백을 수정 작업으로 변환
14. 수정 Candidate 제작
15. 승인 결과 정리
16. 필요 시 Export
17. 필요 시 Runtime Validation
18. 중요한 결정 / 학습 기록
```

**이 목록은 체크박스 의식이 아니다.** 빠뜨리기 쉬운 사고 순서를 정리한 것이다.

실제 작업은 훨씬 짧게 보인다.

```text
디렉터: "주인공을 시작하자."
Art Studio: 문맥 확인 → 방향 확인 → 후보 준비

디렉터: "2번. 무기만 작게."
Art Studio: 수정 범위 해석 → revised candidate

디렉터: "좋아. 게임에 넣어봐."
Art Studio: approved 정리 → export → runtime test

디렉터: "배경에 묻힌다."
Art Studio: asset / background / engine 원인 분석 → 수정안
```

이것이 이 문서가 지원하려는 실제 작업 경험이다.

---

## 23. 다른 문서와의 연결

```text
PROJECT_BRIEF.md              이 게임은 무엇인가
ART_DIRECTION.md              이 게임은 어떻게 보여야 하는가
STYLE_SPEC.md                 어떤 수치와 기술 규칙을 따라야 하는가
ASSET_BRIEF.md                이번에 무엇을 만들어야 하는가
ASSET_MANIFEST.md             무엇이 필요하고 현재 어디까지 왔는가
REVIEW_LOG.md                 무엇이 왜 채택·반려되었는가

06_ASSET_LIFECYCLE.md         이 결과물은 현재 무엇인가
08_REVIEW_AND_APPROVAL.md     무엇을 기계가 검사하고 무엇을 사람이 판단하는가
09_ASSET_SPEC_AND_VALIDATION  이 자산이 기술적으로 정상인가
10_ENGINE_HANDOFF.md          승인 자산을 실제 게임으로 어떻게 전달하고 확인하는가
11_LEARNING_AND_REUSE.md      이번 작업에서 무엇을 다시 사용할 가치가 있는가
```

---

## 24. 이 문서에서 다루지 않는 것

```text
Asset Lifecycle 상세 상태 의미            06_ASSET_LIFECYCLE.md
Technical Review / Art Review의 세부 판단  08_REVIEW_AND_APPROVAL.md
dimensions · alpha · palette · naming 등의 검증 규칙   09_ASSET_SPEC_AND_VALIDATION.md
Engine-specific export / import           10_ENGINE_HANDOFF.md
Studio 공통 지식 승격 기준                 11_LEARNING_AND_REUSE.md
특정 도구의 상세 사용법                    별도 tool guide 또는 실제 작업 문맥
특정 생성기의 prompt 공식                  tool-specific 작업 지시 · 프로젝트별 제작 자료
```

이 문서는 **실제 제작 루틴과 판단 순서**에 집중한다.

---

## 25. 핵심 원칙 요약

Generation Workflow는 고정된 생성 파이프라인이 아니다.

> **그림을 만들기 전에 어떤 게임의 어떤 문제를 해결하는 작업인지 이해한다.**

> **Project Brief와 Art Direction을 작업의 상위 문맥으로 사용한다.**

> **도구보다 필요한 capability를 먼저 판단한다.**

> **가장 단순하면서 적절한 제작 방식을 선택한다.**

> **Concept과 Candidate를 작업 목적에 따라 구분한다.**

> **후보 수와 단계 수를 고정하지 않는다.**

> **생성 결과는 필요하면 편집·가공·수작업을 거쳐 Candidate가 될 수 있다.**

> **Technical Review와 Art Review를 혼동하지 않는다.**

> **디렉터의 짧은 피드백을 실제 수정 작업으로 번역하되, 국소 지시를 전체 규칙으로 과도하게 일반화하지 않는다.**

> **반복 실패 시 프롬프트만 고집하지 않고 제작 방식이나 도구 자체를 바꿀 수 있다.**

> **필요하면 실제 게임 화면을 제작 과정의 일부로 사용한다.**

> **사람을 모든 작은 작업의 병목으로 만들지 않는다.**

> **작은 작업은 작게, 중요한 자산은 필요한 만큼 깊게 다룬다.**

> **좋은 workflow의 목적은 절차를 많이 만드는 것이 아니라, 디렉터의 판단을 실제 게임 자산으로 안정적으로 연결하는 것이다.**
