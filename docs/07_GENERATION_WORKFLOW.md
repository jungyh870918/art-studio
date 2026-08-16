# 07_GENERATION_WORKFLOW

## 1. 문서의 역할

이 문서는 Art Studio에서 실제 자산 제작 요청이 들어왔을 때 사용하는 **기본 작업 루틴**을 정의한다.

이 문서는 특정 생성기의 사용법을 설명하지 않는다.

이 문서는 특정 게임의 스타일을 정의하지 않는다.

이 문서는 Asset Lifecycle의 상태 정의를 다시 설명하지 않는다.

이 문서는 Review & Approval의 판단 기준을 대신하지 않는다.

핵심 질문은 하나다.

> **하나의 아트 작업 요청이 들어왔을 때, Art Studio는 무엇을 먼저 확인하고 어떤 순서로 제작·검토·수정하여 공식 자산 후보로 발전시키는가?**

이 문서는 하나의 절대적인 자동 파이프라인을 만드는 것이 아니라,
Claude Code와 디렉터가 반복적으로 사용할 수 있는 **실전 제작 루틴**을 제공한다.

---

## 2. 가장 중요한 원칙

기본적인 사고 흐름은 다음과 같다.

```text
프로젝트 확인
↓
Project Brief 확인
↓
Art Direction 확인
↓
현재 요청 확인
↓
Asset 요구 구체화
↓
Reference 확인
↓
제작 방식 선택
↓
Candidate 제작
↓
필요한 기술 검사
↓
Director Review
↓
수정
↓
Approved 정리
↓
필요 시 Export / Runtime Validation
```

그러나 이 흐름을 모든 작업에 동일하게 강제하지 않는다.

작업에 따라:

- 일부 단계를 생략할 수 있다.
- 일부 단계를 여러 번 반복할 수 있다.
- 순서를 약간 바꿀 수 있다.
- 하나의 도구만 사용할 수 있다.
- 여러 도구를 조합할 수 있다.
- 이미 승인된 방향을 반복하는 작업이라면 빠르게 진행할 수 있다.

핵심은 순서 자체가 아니라 다음을 놓치지 않는 것이다.

> **무엇을 만드는지, 어떤 게임을 위한 것인지, 어떤 방향을 따라야 하는지, 무엇을 비교해야 하는지, 무엇이 기술적으로 필요한지를 먼저 이해하고 제작한다.**

---

## 3. Workflow는 생성기 중심이 아니다

다음과 같이 생각하지 않는다.

```text
ChatGPT
↓
FLUX
↓
PixelLab
↓
Unity
```

또는:

```text
모든 캐릭터는 PixelLab
모든 배경은 FLUX
모든 검토는 Claude
```

처럼 도구 이름을 기준으로 작업 순서를 고정하지 않는다.

기본 사고는 다음이다.

```text
문제
↓
필요한 결과
↓
필요한 capability
↓
적절한 제작 방법
↓
현재 사용 가능한 도구
```

같은 자산이라도 프로젝트마다 제작 방식이 달라질 수 있다.

예:

```text
캐릭터 A
→ 직접 이미지 생성
→ 수정
→ 승인
```

다른 프로젝트에서는:

```text
캐릭터 B
→ 3D blockout
→ render
→ paintover
→ pixel conversion
→ 후보 비교
→ 승인
```

일 수도 있다.

도구는 workflow의 주인이 아니다.

---

## 4. Workflow는 Asset Lifecycle과 다르다

`06_ASSET_LIFECYCLE.md`는 다음을 정의한다.

> 자산이 현재 어떤 의미의 상태인가?

예:

```text
REFERENCE
CONCEPT
CANDIDATE
APPROVED
EXPORT
```

반면 이 문서는 다음을 정의한다.

> 작업자는 실제로 무엇을 어떻게 진행하는가?

예:

```text
문맥 확인
→ 요구 정리
→ 제작법 선택
→ 후보 제작
→ 검토
→ 수정
```

둘은 연결되지만 같은 문서가 아니다.

---

## 5. 작업 시작 전 첫 질문

새 요청이 들어오면 가장 먼저 확인한다.

> **이 작업은 어느 게임 프로젝트의 작업인가?**

여러 게임을 동시에 다루는 Art Studio에서 프로젝트를 잘못 잡는 것은 단순 파일 위치 오류가 아니다.

다른 프로젝트의:

- 레퍼런스
- 팔레트
- 비율
- 승인 자산
- 금지사항
- 디렉터 결정

을 잘못 적용할 수 있기 때문이다.

따라서 새로운 제작 작업에서는 필요에 따라 다음을 확인한다.

- 프로젝트 ID
- 프로젝트 작업 공간
- 연결된 게임 저장소
- 현재 관련 문서
- 기존 승인 자산
- 최근 중요한 디렉터 결정

이미 문맥상 프로젝트가 명확하다면 매번 다시 질문하지 않는다.

---

## 6. Project Brief 확인

다음 질문에 답하기 위해 `PROJECT_BRIEF.md`를 확인한다.

> **이 게임은 무엇인가?**

필요한 정보는 작업에 따라 다르지만 예를 들어 다음이 중요할 수 있다.

- 장르
- 플랫폼
- 카메라
- 플레이 구조
- 게임의 세계
- 주요 시각 대상
- 플레이어가 자산을 보는 거리
- 개발 단계
- Art Studio 담당 범위
- 기술적 제약

모든 제작 요청에서 Project Brief 전체를 다시 요약하지 않는다.

현재 자산에 영향을 주는 정보만 가져온다.

예:

```text
요청:
플레이어 캐릭터 제작

중요한 Project Brief 정보:
- 3인칭
- 모바일 대응
- 전투 중 화면 표시 크기가 작음
- 적과 아군을 빠르게 구분해야 함
```

이 정보는 이후 제작 판단에 직접 영향을 준다.

---

## 7. Art Direction 확인

다음 질문에 답하기 위해 `ART_DIRECTION.md`를 확인한다.

> **이 게임은 어떻게 보여야 하는가?**

현재 자산과 관련 있는 항목을 우선한다.

예:

- Direction Summary
- 핵심 시각 키워드
- 형태 언어
- 실루엣
- 캐릭터 방향
- 환경 방향
- 색
- 명암
- 질감
- 조명
- 플레이 가독성
- References
- Anti-References
- 금지사항
- 확정된 방향
- 탐색 중인 방향
- 대표 승인 자산
- 실제 게임 screenshot

특히 다음을 구분한다.

```text
확정된 방향
≠
탐색 중인 방향
```

탐색 중인 아이디어를 이미 확정된 규칙처럼 사용하지 않는다.

---

## 8. Style Specification이 있다면 확인한다

프로젝트에 `STYLE_SPEC.md`가 존재한다면,
현재 자산에 필요한 기술 규격을 확인한다.

예:

- sprite dimensions
- tile size
- palette target
- outline
- texture dimensions
- animation frame range
- filtering
- alpha
- rendering constraints

하지만 Style Spec이 아직 없거나 일부 값이 미정일 수 있다.

그 경우 임의로 빈칸을 채워 프로젝트 규칙으로 확정하지 않는다.

필요한 값이 실제 작업에서 반드시 필요하다면:

- 기존 승인 자산에서 확인하거나
- 현재 프로젝트의 다른 자료에서 확인하거나
- 후보 값으로 제안하거나
- 디렉터 판단이 필요한 중요 항목이라면 선택지를 정리한다.

---

## 9. 현재 요청을 정확히 이해한다

디렉터의 요청이 짧아도 유효한 작업 요청으로 받아들인다.

예:

- “주인공 얼굴 세 개만 봐보자.”
- “무기가 너무 크다. 줄여.”
- “이 스타일로 마을 건물 몇 개 더.”
- “배경에 묻힌다.”
- “좀 더 싸구려 느낌.”
- “이걸 실제 게임에 넣어봐.”

Claude는 이런 요청을 다시 거대한 양식으로 되묻지 않는다.

현재 문맥을 읽고 작업 가능한 요구로 해석한다.

필요하면 내부적으로 다음을 구분한다.

```text
사용자의 표현
↓
현재 프로젝트 문맥
↓
실무적 해석
↓
제작 작업
```

예:

```text
디렉터:
"좀 더 투박하게."

실무 해석 후보:
- 형태를 더 단순한 큰 덩어리로
- 표면을 지나치게 매끈하게 만들지 않음
- 장식 밀도 감소
- 불규칙한 edge나 재질 variation 허용
```

원래 디렉터 표현을 임의로 다른 의도로 바꾸지 않는다.

---

## 10. 이번 작업의 목표를 정의한다

작업 시작 전에 최소한 다음이 분명해야 한다.

- 무엇을 만드는가?
- 무엇을 판단하려는가?
- 결과는 어디까지 완성되어야 하는가?

이 세 가지는 다를 수 있다.

예:

```text
작업:
주인공 얼굴 방향 탐색

목표:
최종 초상화 제작이 아니라
얼굴 비율과 인상을 결정하기 위한 Concept 비교
```

또는:

```text
작업:
벽돌 타일 제작

목표:
실제 게임에 바로 넣을 수 있는 seamless tile Candidate
```

또는:

```text
작업:
승인된 캐릭터를 Roblox에서 테스트

목표:
새 디자인 생성이 아니라
runtime scale과 readability 검증
```

목표가 달라지면 필요한 완성도와 도구도 달라진다.

---

## 11. Asset Brief 사용 여부를 결정한다

모든 작업에 `ASSET_BRIEF.md`를 만들지 않는다.

다음과 같은 경우 Asset Brief가 특히 유용하다.

- 주인공
- 보스
- 주요 NPC
- 중요한 몬스터
- 핵심 건물
- 대표 UI 자산
- 중요한 VFX
- 여러 도구가 관여하는 복잡한 자산
- 반복 수정 가능성이 높은 자산
- 디렉팅 요구가 많은 자산

반대로:

- 단순한 반복 아이콘
- 명확한 규칙의 색상 variant
- 이미 승인된 계열의 단순 파생물
- 사소한 cleanup

등에는 별도 Brief가 필요하지 않을 수 있다.

Asset Brief가 없다면 현재 요청과 기존 문서를 바탕으로 필요한 요구를 최소한으로 정리한다.

---

## 12. Asset 요구를 구체화한다

실제 제작에 필요한 정보를 현재 작업 수준에 맞게 정리한다.

예:

### 역할

이 자산이 게임에서 무엇인가?

### 기능

플레이 중 무엇을 전달해야 하는가?

### 표시 조건

- 멀리서 보는가?
- UI에서 작은 아이콘으로 보이는가?
- 화면을 크게 차지하는가?
- 빠르게 움직이는가?

### 반드시 들어갈 요소

- 특정 장비
- 시대적 특징
- 팀 구분 요소
- 기능적 표식

### 피해야 할 요소

- 금지된 스타일
- 시대에 맞지 않는 요소
- 기존 승인 방향과 충돌하는 형태

### 필요한 variant

- 방향
- 색상
- 장비
- 상태
- animation

### 기술 제약

현재 알려진 범위만 사용한다.

이 과정을 거대한 spec 작성으로 만들지 않는다.

---

## 13. 기존 자산을 먼저 확인한다

새로 만들기 전에 이미 존재하는 것을 확인한다.

예:

- 관련 Approved asset
- 같은 계열의 캐릭터
- 기존 Candidate
- 이전 Concept
- 기존 Export
- 기존 screenshot
- 이미 사용 중인 외부 에셋

이 확인은 다음을 방지한다.

- 이미 만든 것을 다시 생성
- 승인된 형태 언어와 충돌
- 불필요한 스타일 drift
- 동일 자산의 중복 제작
- 이전 디렉터 결정을 잊음

특히 같은 asset family의 기존 승인 자산은 매우 강한 기준점이 될 수 있다.

---

## 14. Reference를 확인한다

Reference는 현재 작업에 필요한 정도만 확인한다.

모든 Reference를 매번 전부 읽거나 분석할 필요는 없다.

다음 질문이 중요하다.

> **이번 자산에서 어떤 Reference의 어떤 속성을 참고하는가?**

예:

```text
Reference A
→ 캐릭터 비율

Reference B
→ 갑옷의 시대감

Reference C
→ 재질 밀도

Reference D
→ 조명
```

여러 Reference를 이유 없이 하나의 스타일로 섞지 않는다.

Reference에서 무엇을 가져오지 않을지도 중요할 수 있다.

예:

```text
Reference A에서:
실루엣은 참고
색은 참고하지 않음
```

---

## 15. Reference가 부족하다고 무조건 Research부터 하지 않는다

모든 작업에 별도 Research 단계가 필요한 것은 아니다.

이미:

- Art Direction이 명확하고
- 승인 자산이 충분하고
- Asset Brief가 구체적이고
- 반복 작업이라면

추가 Reference 없이 바로 제작할 수도 있다.

반대로 다음과 같은 경우에는 Reference 탐색이 유용할 수 있다.

- 시대 고증이 중요함
- 형태를 이해하기 어려움
- 새로운 자산 종류
- 기존 Art Direction에 관련 시각 자료가 부족함
- 디렉터가 여러 방향을 비교하려 함

Research는 필요할 때만 한다.

---

## 16. 제작 방식 선택

이제 다음을 판단한다.

> **이 자산을 어떤 방식으로 만드는 것이 가장 적합한가?**

고려할 수 있는 요소:

- 결과물 종류
- 표현 방식
- 요구 해상도
- 방향 일관성
- 동일 캐릭터 반복성
- animation 필요 여부
- tile seamlessness
- 정확한 layout 필요 여부
- 수정 횟수 예상
- batch 규모
- 엔진 효과 의존도
- 사람이 직접 수정하는 편이 빠른가
- 기존 source 활용 가능 여부
- 사용 가능한 도구

도구는 이 판단 이후에 선택한다.

---

## 17. 가장 단순한 적절한 방법을 우선한다

Art Studio는 복잡한 제작법을 전문성의 증거로 취급하지 않는다.

다음 정도로 해결된다면:

```text
한 번 생성
↓
간단한 cleanup
↓
review
```

굳이:

```text
3D blockout
↓
render
↓
generator
↓
pixel conversion
↓
manual paint
↓
second generator
↓
engine
```

로 만들지 않는다.

반대로 정확한 방향 sprite나 복잡한 perspective consistency가 필요하다면
여러 단계가 오히려 더 단순하고 안정적인 해법일 수 있다.

기준은 단계 수가 아니라 **문제를 얼마나 안정적으로 해결하는가**다.

---

## 18. 작은 테스트를 먼저 할 수 있다

새로운 제작 방식이나 도구의 적합성이 불확실하다면
전체 batch 전에 작은 테스트를 할 수 있다.

예:

```text
80개 캐릭터 생성 예정

먼저:
2개 캐릭터 × 2개 방식
↓
결과 비교
↓
제작 방식 결정
```

또는:

```text
타일 전체 세트 제작 전
대표 타일 1개로
seam / scale / engine result 검증
```

이 방식은 잘못된 제작법을 대량 반복하는 것을 막는다.

---

## 19. Concept 단계가 필요한지 판단한다

다음과 같은 경우 Concept 단계가 유용하다.

- 전체 방향이 아직 탐색 중
- 대표 캐릭터 디자인
- 새로운 몬스터 계열
- 중요한 환경 언어
- UI 그래픽 언어
- 주요 VFX 스타일
- 여러 형태 방향이 모두 가능

Concept에서는 완성도보다 방향 차이를 명확하게 만든다.

예:

```text
A
넓고 낮은 실루엣

B
길고 날카로운 실루엣

C
비대칭 장비 중심
```

세 개의 거의 같은 이미지를 만드는 것보다
서로 다른 판단 가능한 방향을 만드는 편이 낫다.

---

## 20. Candidate 제작

실제 채택 가능한 결과물을 제작한다.

Candidate는 다음을 반영해야 한다.

- 현재 Art Direction
- 해당 자산 요구
- 필요한 Reference
- 기존 승인 자산과의 관계
- 현재 기술 제약
- 디렉터의 최신 지시

모든 Candidate를 동일한 방식으로 만들 필요는 없다.

예:

```text
Candidate A
→ 생성 모델

Candidate B
→ Blender render + paint

Candidate C
→ 수작업
```

도 가능하다.

중요한 것은 제작 방법이 아니라 비교 가능한 결과다.

---

## 21. Candidate 수를 고정하지 않는다

기본값으로 “항상 4개” 같은 규칙을 만들지 않는다.

후보 수는 다음에 따라 달라질 수 있다.

### 1개

- 방향이 이미 명확함
- 반복 제작
- 단순 수정
- 작은 자산

### 2~4개

- 중요한 디자인 비교
- 형태 방향 탐색
- 색상 방향 탐색

### 더 많은 후보

- 자동 batch 탐색이 실제로 의미 있음
- 다양한 결과에서 좁혀야 함

후보 수가 많다고 좋은 workflow는 아니다.

디렉터가 차이를 판단할 수 있는 **의미 있는 후보**가 중요하다.

---

## 22. Candidate 변형은 목적이 있어야 한다

Variation은 단순 random seed 반복이 아니다.

가능하면 각 후보의 차이를 설명할 수 있어야 한다.

예:

```text
A
더 큰 머리 / 단순 갑옷

B
현실 비율 / 큰 무기

C
짧고 넓은 몸 / 작은 무기
```

또는:

```text
A
저채도

B
높은 캐릭터 대비

C
따뜻한 환경 편향
```

무엇이 다른지 알 수 없는 후보를 많이 만드는 것은
디렉터의 판단 부담만 늘릴 수 있다.

---

## 23. 생성 결과를 그대로 Candidate로 취급하지 않아도 된다

Raw generation은 제작 source일 수 있다.

예:

```text
raw generation
↓
crop
↓
cleanup
↓
color correction
↓
manual correction
↓
Candidate
```

또는:

```text
3D render
↓
generator edit
↓
pixel conversion
↓
manual pixel cleanup
↓
Candidate
```

생성기가 한 번에 완성 파일을 만들어야 한다는 전제를 두지 않는다.

---

## 24. 생성 중간 결과를 모두 보존할 필요는 없다

작업 중 많은 임시 결과가 생길 수 있다.

예:

- test render
- intermediate mask
- temporary upscale
- failed crop
- debug image
- generator raw output

모든 중간 결과를 공식 Candidate로 관리하지 않는다.

보존 가치가 있는 결과만 후보 또는 기록 대상으로 남긴다.

특히:

- 중요한 비교 후보
- 재현에 필요한 source
- 승인 과정에 사용된 결과
- 제작법 판단에 의미 있는 테스트

는 보존 가치가 높다.

---

## 25. 기술 검사는 단계에 맞게 한다

모든 단계에서 최종 수준의 validation을 강제하지 않는다.

Concept 단계에서는:

- 기술 규격보다 방향 탐색이 중요할 수 있다.

Candidate 단계에서는:

- 비교에 필요한 기술 상태가 확보되어야 한다.

Approved 직전에는:

- 실제 사용에 필요한 주요 기술 제약을 더 엄격하게 확인할 수 있다.

Export 단계에서는:

- engine-specific requirement가 중요해질 수 있다.

현재 단계의 목적에 맞는 검사를 한다.

---

## 26. 기술 검사는 미적 리뷰를 대신하지 않는다

다음이 모두 정상이라고 해도:

```text
dimensions correct
alpha correct
palette correct
format correct
```

좋은 디자인이라는 뜻은 아니다.

반대로 Concept 단계의 이미지가:

```text
wrong dimensions
rough edges
temporary background
```

이어도 방향 탐색에는 매우 유용할 수 있다.

Technical Review와 Art Review는 다른 문제다.

세부 기준은 `08_REVIEW_AND_APPROVAL.md`와
`09_ASSET_SPEC_AND_VALIDATION.md`에서 정의한다.

---

## 27. Claude의 중간 분석

Claude는 Candidate를 디렉터에게 보여주기 전에
필요하면 먼저 분석할 수 있다.

예:

- 명백한 누락
- 기존 Art Direction과의 충돌
- technical issue
- 후보 사이의 차이
- 작은 화면 가독성 위험
- Reference와의 관계
- 기존 승인 자산과의 inconsistency

하지만 Claude가 미적 후보를 자동으로 탈락시키는 시스템을 기본으로 만들지 않는다.

명백한 기술 실패는 걸러낼 수 있지만,
미적 판단이 필요한 결과는 디렉터가 볼 가치가 있을 수 있다.

---

## 28. Director Review를 위한 제시 방식

디렉터는 기술 과정 전체를 볼 필요가 없다.

가능하면 판단에 필요한 결과를 정리해서 보여준다.

예:

```text
A / B / C
```

와 함께 필요한 경우:

```text
A
- 실루엣 가장 단순
- 장비 작음

B
- 얼굴 강조
- 현재 승인 캐릭터와 가장 유사

C
- 가장 과장됨
- 작은 화면에서 식별력 높을 가능성
```

정도로 차이를 짧게 설명할 수 있다.

디렉터가 generator parameter, script log, 내부 파일 처리 순서를
매번 읽어야 하는 시스템을 목표로 하지 않는다.

---

## 29. 비교 조건을 가능하면 통제한다

후보를 비교할 때 차이가 제작 조건 때문인지 디자인 때문인지 구분할 수 있어야 한다.

가능하면:

- 같은 canvas size
- 같은 background
- 같은 camera
- 같은 pose
- 같은 lighting
- 같은 표시 scale

등을 사용할 수 있다.

물론 서로 완전히 다른 방향을 탐색하는 Concept 단계에서는
모든 조건을 같게 만들 필요가 없을 수 있다.

비교 목적에 맞게 통제한다.

---

## 30. 디렉터 피드백을 수정 작업으로 변환한다

디렉터는 짧게 말할 수 있다.

예:

- “2번이 좋은데 무기만 줄여.”
- “얼굴이 너무 착해.”
- “갑옷이 너무 비싸 보여.”
- “배경에 묻힌다.”
- “이쪽은 너무 AI 같다.”
- “조금 더 낡게.”
- “이 방향은 아니다.”

Claude는 이를 현재 프로젝트 문맥과 연결해
실제 수정 가능한 요구로 변환한다.

예:

```text
"무기만 줄여"
→ 기존 승인/선호 디자인의 나머지 비율은 유지
→ weapon silhouette과 body ratio 관계만 수정
→ 전체 스타일 변경으로 확대하지 않음
```

---

## 31. 국소 피드백을 전역 규칙으로 확대하지 않는다

다음 피드백:

```text
"이 보스는 outline 없이 가자."
```

를 자동으로:

```text
"게임 전체 캐릭터 outline 제거."
```

로 해석하지 않는다.

수정 지시의 적용 범위를 구분한다.

- project-wide
- category-wide
- asset family
- individual asset

범위가 명확하면 그대로 적용한다.

불명확하지만 영향이 작은 경우 국소적으로 처리할 수 있다.

영향이 큰 경우 기존 Art Direction과 Review 기록을 확인한다.

---

## 32. 수정은 기존 방향을 보존하면서 한다

디렉터가 특정 부분만 수정하라고 했다면
나머지 승인된 요소까지 무작위로 다시 생성하지 않는 것이 중요하다.

예:

```text
"무기만 줄여."
```

인데:

- 얼굴 변경
- 갑옷 변경
- 색감 변경
- 포즈 변경

이 함께 일어나면 비교가 어려워진다.

가능하면 수정 범위를 통제한다.

이것은 특히 생성형 도구에서 중요하다.

---

## 33. 반복 실패 시 같은 방법만 고집하지 않는다

수정이 반복적으로 실패하면
프롬프트만 계속 바꾸는 것 외의 방법을 고려한다.

예:

```text
문제:
동일 캐릭터의 8방향 일관성이 계속 깨짐

가능한 대응:
- 다른 생성 도구
- 전문 directional sprite tool
- 3D source
- manual correction
- 기존 source에서 회전/보정
```

또는:

```text
문제:
생성기가 정확한 UI icon geometry를 계속 실패

가능한 대응:
- vector tool
- code-based shape
- manual drawing
```

디자인 요구를 자동화 편의에 맞춰 임의로 낮추지 않는다.

---

## 34. 제작 방식 변경은 실패가 아니다

작업 중 다음처럼 바뀔 수 있다.

```text
처음:
text-to-image

↓

결과:
형태 일관성 부족

↓

변경:
3D blockout + image edit
```

이것은 workflow 실패가 아니다.

문제에 맞는 제작법을 찾아가는 정상적인 과정이다.

도구를 유지하는 것보다 결과가 중요하다.

---

## 35. 승인 시점

Candidate가 충분히 검토되면 디렉터가 채택할 수 있다.

승인의 구체적 판단 기준은 `08_REVIEW_AND_APPROVAL.md`에서 다룬다.

Generation Workflow에서는 다음만 유지한다.

> 디렉터의 채택 의도가 명확할 때 Candidate를 Approved로 정리한다.

Claude의 추천만으로 자동 승인하지 않는다.

---

## 36. 승인된 source를 정리한다

승인 후에는 필요에 따라 다음을 정리한다.

- 공식 source
- 관련 제작 source
- 필요한 metadata
- 중요 prompt 또는 parameter
- 승인 대상
- asset ID
- 향후 수정에 필요한 파일

모든 생성 과정의 모든 로그를 보존할 필요는 없다.

다시 만들거나 수정하는 데 실제로 필요한 정보 위주로 남긴다.

---

## 37. Approved 후 바로 Export가 필요하지 않을 수 있다

Approved source가 만들어졌다고
항상 즉시 모든 엔진용 export를 생성하지 않는다.

예:

- 아직 engine integration 단계가 아님
- 플랫폼이 확정되지 않음
- 다른 자산을 먼저 승인해야 함
- source library 구축 단계

필요한 시점에 export한다.

반대로 실제 게임 화면 검증이 중요한 자산이라면
빠르게 engine export를 만들어 runtime test를 할 수 있다.

---

## 38. Runtime Validation이 제작 과정에 포함될 수 있다

특정 자산은 이미지 파일만 보고 판단하기 어렵다.

예:

- 캐릭터
- tile
- VFX
- UI icon
- environment
- lighting-dependent asset

필요하면:

```text
Candidate 또는 Approved source
↓
temporary/export
↓
engine import
↓
actual game screenshot
↓
review
```

를 사용한다.

이때 runtime test를 “제작이 끝난 후의 별도 QA”로만 보지 않는다.

아트 제작 자체의 일부가 될 수 있다.

---

## 39. Runtime에서 문제를 발견하면 원인을 분리한다

예:

```text
"캐릭터가 배경에 묻힌다."
```

원인은 여러 곳에 있을 수 있다.

### Asset

- silhouette 약함
- value contrast 부족
- 색 분리 부족

### Environment

- 배경 detail 과다
- 배경 contrast 과다

### Engine

- lighting
- shader
- material
- post-processing

### Camera

- 표시 크기
- distance
- FOV

무조건 캐릭터 이미지를 다시 생성하지 않는다.

원인을 구분하고 가장 적절한 지점을 수정한다.

---

## 40. 반복 제작

하나의 승인 자산 또는 asset family가 기준으로 잡히면
반복 생산 단계로 들어갈 수 있다.

예:

```text
기사 기본 방향 승인
↓
기사 12종 제작
```

이 경우 매 자산마다 처음부터 전체 Concept 과정을 반복하지 않는다.

대신:

- 승인된 family rule
- Style Spec
- Asset Brief 또는 Manifest
- 기존 승인 자산

을 기준으로 빠르게 제작할 수 있다.

하지만 반복 생산 중에도 스타일 drift가 보이면 다시 검토한다.

---

## 41. Batch 작업

자산 수가 많아지면 batch 작업을 사용할 수 있다.

예:

- 동일 규격 resize
- palette check
- sprite packing
- 대량 generation
- variant creation
- naming
- export

Batch를 사용하기 전에는 가능한 경우 대표 샘플로 작업 방식을 검증한다.

```text
샘플
↓
검증
↓
batch
```

잘못된 규칙을 100개 파일에 적용한 뒤 수정하는 것보다 낫다.

---

## 42. 자동화의 위치

Generation Workflow에서 자동화는 다음과 같은 영역에 적합하다.

- 반복 생성 호출
- 파일 수집
- rename
- conversion
- resize
- validation
- contact sheet 생성
- metadata 기록
- export
- batch processing

반대로 다음을 자동화 목표로 삼지 않는다.

- 최종 디자인 선택
- 매력 평가
- 프로젝트 정서 결정
- 세계관 적합성의 최종 판단
- “충분히 좋은가”의 결정

자동화는 workflow를 지원한다.

workflow가 자동화를 위해 존재하는 것은 아니다.

---

## 43. 디렉터를 불필요한 과정에 노출하지 않는다

디렉터는 다음을 매번 알 필요가 없다.

- 어떤 script를 실행했는가
- 파일을 어느 임시 폴더에 옮겼는가
- 어떤 API request 형식을 썼는가
- 어떤 intermediate format을 거쳤는가
- 어떤 batch command를 사용했는가

디렉터가 판단해야 하는 것은 주로:

- 방향
- 후보
- 차이
- 수정
- 최종 결과

다.

Art Studio가 기술적 잡무를 흡수한다.

---

## 44. 반대로 중요한 제작 방식은 투명하게 설명할 수 있다

다음과 같이 결과에 직접 영향을 주는 제작 판단은
필요하면 짧게 설명한다.

예:

```text
이 자산은 8방향 일관성이 중요해서
일반 이미지 생성보다 3D 기준 source를 먼저 만들었다.
```

또는:

```text
이 타일은 반복 seam이 중요하므로
한 장 이미지보다 seamless generation + tile test 방식으로 만들었다.
```

장황한 도구 보고서는 필요하지 않다.

디렉터가 결과의 성격을 이해할 정도면 충분하다.

---

## 45. 작업을 중단해야 하는 경우

Claude는 다음과 같은 경우 큰 미적 결정을 임의로 확정하지 않는다.

### Art Direction이 없는 상태에서 대표 스타일을 결정해야 함

예:

```text
주인공 스타일 자체가 미정
```

### 서로 다른 방향이 모두 합리적임

A와 B가 모두 프로젝트에 가능하지만
선택이 전체 방향에 큰 영향을 주는 경우.

### 기존 승인 방향과 충돌함

현재 요청이 기존 대표 캐릭터 또는 Art Direction을 크게 바꿀 수 있는 경우.

### 기술 제약이 디자인 자체를 바꿔야 할 정도로 큼

예:

기존 방향을 그대로 유지하기 어려운 플랫폼 제약.

이때는 문제와 선택지를 정리한다.

---

## 46. 질문하지 않고 진행해야 하는 경우

다음은 규칙이 명확하다면 자율적으로 처리할 수 있다.

- 승인된 asset resize
- format conversion
- naming 적용
- alpha cleanup
- 정해진 규격의 export
- 동일한 패턴의 반복 자산
- 이미 승인된 수정 지시
- 기술 검사
- 되돌릴 수 있는 파일 정리
- 후보 비교 자료 생성

사람 중심 디렉팅은
사람에게 모든 작은 작업을 물어보는 시스템을 의미하지 않는다.

---

## 47. 작업 복잡도에 따라 workflow 깊이를 조절한다

### Level A — 단순 작업

예:

- 작은 icon
- color variant
- format conversion
- 명확한 반복 asset

흐름:

```text
요구 확인
→ 제작
→ 기술 확인
→ 승인/사용
```

---

### Level B — 일반 제작

예:

- 일반 캐릭터
- 몬스터
- 환경 prop
- 대표 tile

흐름:

```text
문맥 확인
→ 요구 정리
→ reference
→ candidate
→ review
→ 수정
→ approved
```

---

### Level C — 방향성 높은 핵심 자산

예:

- 주인공
- 대표 보스
- 핵심 환경
- 전체 스타일을 결정하는 자산

흐름:

```text
Project Brief
→ Art Direction
→ reference analysis
→ concept exploration
→ candidate comparison
→ director review
→ revision
→ approved
→ runtime validation
→ refinement
```

이 레벨을 공식 status system으로 관리할 필요는 없다.

작업을 얼마나 깊게 다뤄야 하는지 판단하기 위한 사고 방식이다.

---

## 48. Workflow가 과도하게 무거워졌는지 확인한다

다음 증상이 나타나면 workflow를 재검토한다.

- 작은 아이콘 하나에도 별도 Brief가 필요하다.
- 모든 작업에 후보 4개를 강제한다.
- 매 resize마다 디렉터 승인 필요.
- 모든 생성 결과를 영구 보존한다.
- 모든 feedback을 문서화한다.
- 실제 제작보다 metadata 작성 시간이 더 길다.
- 도구를 많이 쓰는 것이 품질보다 중요해진다.
- 자동화하기 쉬운 방향으로 디자인을 바꾼다.

이 경우 Art Studio의 목적에서 벗어나고 있을 가능성이 높다.

---

## 49. Workflow가 너무 가벼워졌는지도 확인한다

반대로 다음도 문제다.

- Project Brief를 보지 않고 그림부터 만든다.
- 다른 게임의 스타일을 섞는다.
- Reference와 Approved를 구분하지 않는다.
- 모든 생성 결과를 바로 게임에 넣는다.
- 디렉터가 고른 결과를 기록하지 않는다.
- 실제 게임 화면에서 검증하지 않는다.
- 기술 규격을 계속 잊는다.
- 같은 실패를 반복한다.

Workflow의 목적은 절차를 늘리는 것이 아니라
이런 반복적인 실수를 막는 것이다.

---

## 50. 실패에서 다음 작업으로 이어지는 정보

작업이 실패했더라도 모든 것이 폐기되는 것은 아니다.

예:

```text
실패:
캐릭터 얼굴이 너무 사실적임

다음 작업:
- 얼굴 plane 단순화
- 눈/코/입 디테일 감소
- 기존 승인 캐릭터의 facial density와 비교
```

이 정보가 반복되면 프로젝트의 아트 방향 또는 제작 지식으로 남길 가치가 생길 수 있다.

다만 한 번의 실패를 즉시 전체 프로젝트 규칙으로 일반화하지 않는다.

상세한 학습과 재사용 기준은 `11_LEARNING_AND_REUSE.md`에서 정의한다.

---

## 51. 제작 정보의 기록 수준

재현 또는 수정에 도움이 되는 정보는 필요에 따라 남길 수 있다.

예:

- 사용한 source
- 중요한 prompt
- seed
- generator/model
- tool version
- manual edit note
- render setup
- source file
- 주요 parameter

하지만 모든 작업을 연구 실험처럼 기록하지 않는다.

기록 수준은 다음에 따라 달라질 수 있다.

- 재생성 가능성이 높은가
- 중요한 대표 자산인가
- 반복 production에 사용할 방식인가
- tool-specific 재현성이 중요한가
- 나중에 수정할 가능성이 높은가

---

## 52. 기존 승인 결과의 재사용

새 자산 제작에서 기존 Approved asset을 적극 활용할 수 있다.

예:

- proportion reference
- palette reference
- material reference
- silhouette family
- lighting reference
- animation timing reference

하지만 다음을 구분한다.

```text
기존 승인 자산을 기준으로 사용
≠
그 자산을 그대로 복제
```

새 자산의 역할과 개성을 유지한다.

---

## 53. 외부 제작자와 협업하는 경우

외주 또는 다른 제작자가 자산을 만든다고 해도
Generation Workflow의 핵심은 동일하다.

```text
Art Direction
↓
Asset Requirement
↓
External Production
↓
Candidate
↓
Review
↓
Revision
↓
Approved
```

Art Studio가 직접 생성하지 않았다는 이유로
Lifecycle이나 Review의 의미가 달라지지 않는다.

필요하면 Art Studio는:

- Brief 정리
- Reference 정리
- 결과 비교
- technical validation
- export

를 담당할 수 있다.

---

## 54. 구매 에셋을 사용하는 경우

구매 에셋도 제작 자원이다.

흐름은 예를 들어:

```text
필요 자산 확인
↓
구매 후보 탐색
↓
license 확인
↓
프로젝트 적합성 검토
↓
필요한 수정
↓
Candidate / Approved
↓
Export
```

일 수 있다.

구매했다는 사실이 자동 승인이라는 뜻은 아니다.

프로젝트 아트 방향과 실제 게임 화면에 적합한지 확인한다.

---

## 55. 기존 사람이 만든 자산을 사용하는 경우

사람이 직접 만든 원본 역시 동일하게 취급한다.

Art Studio는 AI 생성 결과만을 대상으로 하지 않는다.

예:

```text
hand-painted source
↓
cleanup
↓
technical validation
↓
approved
↓
engine export
```

또는 이미 디렉터가 승인한 원본이라면
Candidate 단계를 생략하고 Approved source로 받아들일 수 있다.

---

## 56. 작업 완료의 의미

Generation Workflow에서 “완료”는 상황에 따라 다르다.

예:

### Concept 작업 완료

디렉터가 다음 방향을 선택할 수 있을 정도의 탐색 결과가 준비됨.

### Candidate 작업 완료

실제 채택 여부를 판단할 수 있는 결과가 준비됨.

### Approved source 작업 완료

디렉터가 공식 source로 채택하고 필요한 원본이 정리됨.

### Engine-ready 작업 완료

필요한 export와 runtime validation까지 끝남.

따라서 “파일 하나 생성됨”을 작업 완료로 자동 해석하지 않는다.

---

## 57. 권장 기본 루틴

일반적인 자산 제작에서는 다음 정도를 기본 루틴으로 사용할 수 있다.

```text
1. 프로젝트 확인
2. Project Brief 확인
3. Art Direction 확인
4. Style Spec / 기존 승인 자산 확인
5. 현재 요청의 목적 파악
6. Asset 요구 정리
7. 필요한 Reference 확인
8. 제작 방식 선택
9. Candidate 제작
10. 단계에 맞는 기술 검사
11. 비교 가능한 형태로 정리
12. Director Review
13. 피드백을 수정 작업으로 변환
14. 수정 Candidate 제작
15. 승인 결과 정리
16. 필요 시 Export
17. 필요 시 Runtime Validation
18. 중요한 결정/학습 기록
```

이 목록은 체크박스 의식이 아니다.

실제 상황에서 빠뜨리기 쉬운 중요한 사고 순서를 정리한 것이다.

---

## 58. 빠른 반복 루프

디렉터와 실제로 작업할 때는 훨씬 짧게 보일 수 있다.

```text
디렉터:
"주인공을 시작하자."

Art Studio:
문맥 확인
→ 방향 확인
→ 후보 준비

디렉터:
"2번. 무기만 작게."

Art Studio:
수정 범위 해석
→ revised candidate

디렉터:
"좋아. 게임에 넣어봐."

Art Studio:
approved 정리
→ export
→ runtime test

디렉터:
"배경에 묻힌다."

Art Studio:
asset / background / engine 원인 분석
→ 수정안
```

이것이 이 문서가 지원하려는 실제 작업 경험이다.

---

## 59. 다른 문서와의 연결

### `PROJECT_BRIEF.md`

게임 맥락을 제공한다.

> 이 게임은 무엇인가?

---

### `ART_DIRECTION.md`

시각적 방향을 제공한다.

> 이 게임은 어떻게 보여야 하는가?

---

### `STYLE_SPEC.md`

반복 제작 가능한 기술 규격을 제공한다.

> 어떤 수치와 기술 규칙을 따라야 하는가?

---

### `ASSET_BRIEF.md`

개별 중요 자산의 요구를 제공한다.

> 이번에 무엇을 만들어야 하는가?

---

### `ASSET_MANIFEST.md`

전체 자산과 진행 상태를 보여준다.

> 무엇이 필요하고 현재 어디까지 왔는가?

---

### `06_ASSET_LIFECYCLE.md`

자산 상태의 의미를 정의한다.

> 이 결과물은 현재 무엇인가?

---

### `08_REVIEW_AND_APPROVAL.md`

검토와 승인 판단을 정의한다.

> 무엇을 기계가 검사하고 무엇을 사람이 판단하는가?

---

### `09_ASSET_SPEC_AND_VALIDATION.md`

기술 규격 검사를 정의한다.

> 이 자산이 기술적으로 정상인가?

---

### `10_ENGINE_HANDOFF.md`

게임 엔진 적용과 runtime 검증을 정의한다.

> 승인 자산을 실제 게임으로 어떻게 전달하고 확인하는가?

---

### `11_LEARNING_AND_REUSE.md`

반복 경험에서 무엇을 남길지 정의한다.

> 이번 작업에서 무엇을 다시 사용할 가치가 있는가?

---

## 60. 이 문서에서 다루지 않는 것

다음 내용은 다른 문서의 역할이다.

### Asset Lifecycle 상세 상태 의미

`06_ASSET_LIFECYCLE.md`

### Technical Review / Art Review의 세부 판단

`08_REVIEW_AND_APPROVAL.md`

### Dimensions / Alpha / Palette / Naming 등의 검증 규칙

`09_ASSET_SPEC_AND_VALIDATION.md`

### Engine-specific export / import

`10_ENGINE_HANDOFF.md`

### Studio 공통 지식 승격 기준

`11_LEARNING_AND_REUSE.md`

### 특정 도구의 상세 사용법

별도 tool guide 또는 실제 작업 문맥

### 특정 생성기의 prompt 공식

tool-specific 작업 지시 또는 프로젝트별 제작 자료

이 문서는 **실제 제작 루틴과 판단 순서**에 집중한다.

---

## 61. 핵심 원칙 요약

Art Studio의 Generation Workflow는 고정된 생성 파이프라인이 아니다.

핵심은 다음과 같다.

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
