# 08_REVIEW_AND_APPROVAL

## 1. 문서의 역할

이 문서는 Art Studio에서 제작된 Concept, Candidate, Approved source, Export 결과를 **어떻게 검토하고 어떤 판단을 누구의 권한으로 확정하는지** 정의한다.

이 문서는 Art Direction을 다시 정의하지 않는다.

이 문서는 Asset Lifecycle의 상태 의미를 다시 설명하지 않는다.

이 문서는 기술 규격의 구체적인 수치나 validator 구현을 정의하지 않는다.

이 문서는 특정 생성 도구의 품질을 평가하는 매뉴얼도 아니다.

핵심 질문은 다음과 같다.

> **무엇을 기계가 검사할 수 있고, 무엇을 Claude가 분석·의견으로 제시하며, 무엇을 디렉터가 최종적으로 승인하는가?**

Review의 목적은 사람을 제거하는 것이 아니다.

Review의 목적은 디렉터가 더 적은 혼란으로 더 나은 판단을 내릴 수 있도록,
기술적 사실과 미적 판단을 분리하고 결과를 비교 가능한 상태로 만드는 것이다.

---

## 2. 가장 중요한 구분

Art Studio의 Review는 기본적으로 다음 두 영역을 구분한다.

```text
TECHNICAL REVIEW
≠
ART REVIEW
```

### Technical Review

측정하거나 확인할 수 있는 기술적 문제를 다룬다.

예:

- dimensions
- aspect ratio
- alpha
- format
- file existence
- naming
- palette constraint
- frame count
- tile seam
- pivot
- padding
- texture size
- export compatibility
- engine constraint

### Art Review

게임의 시각적 목표와 실제 화면 경험을 기준으로 판단한다.

예:

- 매력
- 분위기
- 캐릭터성
- 세계관 적합성
- 형태 언어
- 실루엣
- 가독성
- 시각적 우선순위
- 기존 승인 자산과의 일관성
- 최종 채택 여부

Technical Review와 Art Review는 서로 연결될 수 있지만 동일하지 않다.

---

## 3. 기술적으로 정상이라고 좋은 아트는 아니다

다음 결과가 모두 정상이어도:

```text
dimensions: pass
alpha: pass
format: pass
palette: pass
naming: pass
```

다음 문제가 있을 수 있다.

- 캐릭터가 매력적이지 않다.
- 배경에서 읽히지 않는다.
- 세계관에 맞지 않는다.
- 주인공처럼 보이지 않는다.
- 형태 언어가 기존 자산과 충돌한다.
- 화면의 우선순위가 잘못되었다.

따라서 validator 결과를 Art Review의 대체물로 사용하지 않는다.

> **검사기를 통과했다는 것은 기술 규격을 만족했다는 뜻이지 좋은 게임 아트라는 뜻이 아니다.**

---

## 4. 미적 의견을 기술적 사실처럼 말하지 않는다

반대로 Claude나 비전 모델의 미적 판단을 객관적 수치처럼 말하지 않는다.

예:

```text
기술적 사실:
sprite height = 96px
project target = 64px
```

```text
미적 의견:
현재 머리 비율이 조금 커지면
작은 화면에서 캐릭터성이 더 잘 읽힐 가능성이 있다.
```

또는:

```text
기술적 사실:
배경 평균 luminance와 캐릭터 평균 luminance 차이가 작다.
```

```text
미적 의견:
현재 장면은 캐릭터가 배경에 다소 묻혀 보인다.
```

둘을 함께 사용할 수는 있다.

하지만 의미를 섞지 않는다.

---

## 5. Review의 기본 흐름

일반적인 검토 흐름은 다음과 같이 이해할 수 있다.

```text
Candidate 준비
↓
필요한 Technical Review
↓
비교 자료 정리
↓
Art Review
↓
Director Decision
↓
Approved / Revision / Rejected / On Hold
```

그러나 모든 자산에서 같은 깊이로 수행하지 않는다.

작은 작업은 다음처럼 끝날 수도 있다.

```text
Candidate
↓
간단한 기술 확인
↓
Director 확인
↓
Approved
```

대표 캐릭터나 핵심 환경처럼 중요한 자산은:

```text
Concept Review
↓
Candidate Review
↓
Technical Review
↓
Runtime Screenshot
↓
Art Review
↓
Revision
↓
Final Review
↓
Approved
```

처럼 더 깊게 진행할 수 있다.

---

## 6. Review는 작업 단계에 따라 달라진다

### Concept Review

질문:

> 이 방향을 더 발전시킬 가치가 있는가?

주로 보는 것:

- 형태 방향
- 인상
- 실루엣
- 비율
- 분위기
- 색 방향
- Reference와의 관계

이 단계에서는 최종 파일 규격이 중요하지 않을 수 있다.

---

### Candidate Review

질문:

> 이 결과를 실제 자산으로 채택할 수 있는가?

주로 보는 것:

- Art Direction 적합성
- Asset 요구 충족
- 기존 승인 자산과의 일관성
- 플레이 가독성
- 주요 기술 제약
- 디렉터가 비교해야 하는 차이

---

### Approved Source Review

질문:

> 이 결과를 현재 공식 source로 사용할 수 있는가?

주로 보는 것:

- 채택 의도
- 중요한 수정이 끝났는가
- 필요한 기술적 오류가 없는가
- source로 보존할 가치가 있는가

---

### Export / Runtime Review

질문:

> 실제 게임에서 의도한 대로 보이는가?

주로 보는 것:

- scale
- camera
- lighting
- shader
- material
- compression
- filtering
- animation
- VFX
- environment interaction
- UI relation
- gameplay readability

---

## 7. Technical Review의 역할

Technical Review는 가능한 한 명확하고 재현 가능한 검사를 다룬다.

예:

### 파일

- 파일 존재 여부
- format
- extension
- corruption 여부

### 이미지

- width / height
- aspect ratio
- alpha
- color mode
- padding
- transparent edge
- palette count

### Sprite

- frame count
- frame dimensions
- alignment
- pivot
- spacing
- animation consistency

### Tile

- tile dimensions
- edge seam
- repeat result
- border consistency

### Texture

- dimensions
- compression requirement
- channel
- normal / mask structure
- mipmap suitability

### Export

- target engine format
- expected path
- import compatibility
- missing derived files

구체적인 검증 항목과 자동화 방식은 `09_ASSET_SPEC_AND_VALIDATION.md`에서 정의한다.

---

## 8. Technical Review는 가능한 곳에서 자동화한다

다음과 같은 작업은 자동화에 적합할 수 있다.

- dimensions 검사
- alpha 검사
- file naming 검사
- frame count 검사
- palette count
- texture size
- missing export 탐지
- duplicate filename 탐지
- tile seam test
- format 확인

자동화의 장점은 단순히 빠른 것이 아니다.

다음에도 도움이 된다.

- 반복 실수 감소
- 대량 작업
- 재현 가능성
- 결과 비교
- 사람의 주의력을 미적 판단에 집중

하지만 자동화 자체가 Review의 목적은 아니다.

---

## 9. Technical Pass의 의미

Technical Pass는 다음 의미만 가진다.

> 현재 정의된 기술 규격을 만족한다.

다음을 의미하지 않는다.

- 디자인이 좋다.
- Art Direction과 맞다.
- 디렉터가 승인했다.
- 실제 게임 화면에서 잘 보인다.
- 공식 자산이다.

따라서 다음 관계를 유지한다.

```text
TECH PASS
≠
ART APPROVAL
```

---

## 10. Art Review의 역할

Art Review는 다음 질문을 다룬다.

> **이 결과가 이 게임에서 시각적으로 적절한가?**

현재 프로젝트에 따라 다음을 볼 수 있다.

- 첫인상
- 정서
- 형태 언어
- 실루엣
- 비율
- 캐릭터성
- 환경 분위기
- 색의 방향
- 명암
- 질감
- 조명
- 시각적 우선순위
- gameplay readability
- 캐릭터와 배경 관계
- UI와 world의 관계
- animation feel
- VFX의 강도
- world consistency
- 기존 Approved와의 관계

모든 항목을 매번 체크하지 않는다.

현재 자산에서 중요한 항목만 본다.

---

## 11. Art Review의 최종 권한

최종 미적 승인 권한은 게임 디렉터에게 있다.

Claude는 다음을 할 수 있다.

- 후보 비교
- Art Direction과의 일관성 분석
- Reference와의 관계 설명
- 기존 승인 자산과 차이 설명
- 가독성 위험 지적
- 문제 후보 표시
- 추천안 제시
- 수정 방향 제안

하지만 Claude의 추천을 자동 승인으로 취급하지 않는다.

예:

```text
Claude 의견:
B가 현재 Art Direction과 가장 일관성이 높아 보인다.
```

이 문장은:

```text
B = Approved
```

와 같지 않다.

---

## 12. Claude는 적극적으로 의견을 낸다

사람이 최종 판단자라는 이유로 Claude가 단순히:

> “어느 것이 좋은지 선택해 주세요.”

만 반복하는 시스템이 되어서는 안 된다.

필요하면 구체적으로 의견을 제시한다.

예:

```text
A
- 얼굴은 가장 강함
- 무기 실루엣이 작음
- 현재 주인공 기준 자산보다 장식 밀도가 높음

B
- 실루엣이 가장 명확함
- 작은 화면 가독성이 좋을 가능성이 큼
- 현재 Art Direction과 가장 일관됨

C
- 개성은 강함
- 다른 일반 캐릭터와 형태 언어 차이가 큼
```

그리고 필요하다면:

> 현재 기준에서는 B를 우선 추천한다.

라고 말할 수 있다.

최종 채택은 디렉터가 한다.

---

## 13. 의견의 근거를 짧게 보여준다

Claude가 추천할 때는 가능한 경우 이유를 설명한다.

좋은 예:

> B를 추천한다. 현재 승인 캐릭터들과 비슷한 정보 밀도를 유지하면서도 무기 실루엣이 더 잘 읽힌다.

좋지 않은 예:

> B가 더 좋아 보인다.

또는:

> AI 점수상 B가 최상이다.

Art Review는 숨겨진 미적 score를 권위처럼 사용하지 않는다.

---

## 14. 후보 비교는 차이를 잘 보이게 한다

디렉터가 판단해야 할 때는 가능한 한 비교 조건을 정리한다.

예:

- 같은 표시 크기
- 같은 배경
- 같은 포즈
- 같은 카메라
- 같은 조명
- 같은 crop
- 같은 UI frame

필요하면 contact sheet나 review sheet를 만든다.

목적은 결과를 예쁘게 전시하는 것이 아니라 **차이를 판단하기 쉽게 만드는 것**이다.

---

## 15. 모든 후보를 같은 조건으로 만들 필요는 없다

Concept 단계에서 서로 다른 방향을 탐색하는 경우
모든 조건을 동일하게 만들면 오히려 방향 차이가 줄어들 수 있다.

예:

```text
A
거대한 실루엣 중심

B
현실적 비율 중심

C
장비 과장 중심
```

이런 Concept 비교에서는 차이가 커도 된다.

반면 최종 캐릭터 색상 후보를 비교할 때는
형태, 포즈, 카메라를 고정하는 편이 더 유용할 수 있다.

비교 조건은 **무엇을 판단하려는가**에 따라 정한다.

---

## 16. Director Review의 입력을 최소화한다

디렉터에게 다음을 모두 보여줄 필요는 없다.

- 모든 raw generation
- 실패한 intermediate
- script log
- API response
- mask
- debug image
- temporary export
- technical console output

디렉터가 판단해야 할 것만 정리한다.

예:

```text
Candidate A
Candidate B
Candidate C

차이:
- silhouette
- equipment size
- detail density
```

기술 문제는 필요한 경우 요약한다.

---

## 17. 반대로 숨기면 안 되는 문제도 있다

다음과 같은 문제는 미적 판단에 직접 영향을 줄 수 있으므로
디렉터에게 알려야 한다.

예:

- B만 다른 generator로 만들어 표현 특성이 다름
- C는 technical constraint를 아직 만족하지 않음
- A는 현재 엔진에서 shader 문제로 실제 색이 다르게 보임
- runtime screenshot에서 B만 scale이 잘못 적용됨
- Reference 조건이 후보마다 크게 다름

비교 조건이 공정하지 않은 경우 숨기지 않는다.

---

## 18. Director의 짧은 피드백을 유효한 Review 결과로 본다

다음과 같은 피드백도 충분히 유효하다.

- “2번.”
- “B가 제일 낫다.”
- “얼굴은 A, 몸은 C.”
- “무기만 줄여.”
- “너무 깨끗하다.”
- “이건 아니다.”
- “배경에 묻힌다.”
- “조금 더 어두워.”
- “보스 같지가 않다.”

Claude는 전문 용어로 다시 말해 달라고 요구하지 않는다.

현재 Art Direction과 자산 문맥을 기준으로
수정 가능한 작업으로 변환한다.

---

## 19. 승인으로 볼 수 있는 표현

가능하면 **채택 의도가 명확한 표현**을 Approved decision으로 본다.

예:

- “2번으로 확정.”
- “B 채택.”
- “이걸 공식으로 쓰자.”
- “이 버전을 기준으로 간다.”
- “이걸 승인본으로.”
- Review Log 또는 Manifest에 Approved로 기록

반대로 다음은 문맥에 따라 단순 선호일 수 있다.

- “괜찮다.”
- “이게 낫다.”
- “이 방향이 좋네.”
- “일단 이걸로 보자.”
- “게임에 넣어봐.”

모호한 표현 하나 때문에 모든 작업을 중단할 필요는 없다.

하지만 공식 Approved 상태로 바꾸는 것이 중요한 경우
채택 의도가 충분히 명확한지 확인한다.

---

## 20. Approval은 모든 것을 승인했다는 뜻이 아닐 수 있다

다음과 같은 부분 승인이 가능하다.

```text
실루엣 승인
색상 탐색 계속
```

```text
캐릭터 디자인 승인
animation 미승인
```

```text
원본 일러스트 승인
engine crop 미정
```

```text
보스 형태 승인
재질 표현 수정 필요
```

필요하면 승인 범위를 짧게 기록한다.

모든 자산을 복잡한 partial approval schema로 관리하지는 않는다.

---

## 21. Review 결과의 기본 종류

Review 결과는 개념적으로 다음과 같이 정리할 수 있다.

### Approved

현재 공식 자산 또는 공식 방향으로 채택.

### Revision

기본 방향은 유지하되 수정 필요.

### Rejected

현재 방향에서 채택하지 않음.

### On Hold

판단을 보류.

### Needs Technical Fix

미적 판단과 별개로 기술 문제 수정 필요.

이 표현을 모두 공식 상태 enum으로 강제하지 않는다.

상황을 명확하게 설명하기 위한 용어로 사용할 수 있다.

---

## 22. Revision과 Rejection을 구분한다

예:

```text
"얼굴은 좋고 무기만 줄여."
```

는 보통 Revision에 가깝다.

반면:

```text
"이 방향은 아니다. 너무 사실적이다."
```

는 Rejection에 가깝다.

이 구분은 이후 작업 비용과 방향을 결정하는 데 중요하다.

Revision이면 기존 Candidate의 대부분을 보존할 수 있다.

Rejection이면 다른 Concept 또는 제작 방식으로 돌아갈 수 있다.

---

## 23. 반려 이유는 중요한 정보다

Rejected 결과는 단순 실패가 아니다.

다음과 같은 피드백은 이후 제작에 도움이 된다.

- 너무 사실적
- 너무 귀여움
- 무기 과장 과다
- 배경 detail 과다
- 얼굴이 어려 보임
- UI처럼 보임
- 시대감 부족
- AI 특유의 의미 없는 디테일
- 기존 캐릭터와 너무 유사

하지만 한 번의 반려 이유를 자동으로 프로젝트 전체 Art Direction으로 승격하지 않는다.

반복되거나 명시적으로 확정될 때 장기 규칙이 될 수 있다.

---

## 24. Review Log에 무엇을 남길 것인가

모든 Review를 기록하지 않는다.

Review Log에 남길 가치가 높은 것은 예를 들어:

- 대표 캐릭터 승인
- 스타일 방향 확정
- 중요한 반려 이유
- 반복 적용할 비율 결정
- 주요 금지사항
- 조명 방향 변경
- asset family 기준 결정
- runtime test로 인한 큰 수정
- 기존 Approved 교체

작은 수정 하나하나는 기록하지 않아도 된다.

상세 형식은 `REVIEW_LOG.md` 템플릿이 담당한다.

---

## 25. 실제 게임 화면을 Review input으로 사용한다

게임 아트는 개별 PNG만으로 판단되지 않는다.

필요하면 다음을 Review input으로 사용한다.

- 실제 게임 screenshot
- gameplay capture
- scene view
- camera view
- UI가 포함된 화면
- VFX 포함 장면
- animation playback
- 모바일 표시 화면
- 여러 캐릭터가 함께 있는 장면

특히 다음 자산에서는 runtime review가 중요할 수 있다.

- 플레이어 캐릭터
- 적
- tile
- UI icon
- VFX
- 조명 영향을 크게 받는 자산
- environment
- Roblox asset

---

## 26. Runtime Review에서는 문제 위치를 분리한다

예:

> 캐릭터가 배경에 묻힌다.

가능한 원인:

### Character Asset

- value contrast 부족
- silhouette 약함
- detail distribution 문제
- outline 약함

### Environment

- edge density 과다
- saturation 과다
- contrast 과다
- character 주변 detail 과다

### Engine

- lighting
- post-processing
- shader
- material
- fog
- bloom

### Camera

- distance
- scale
- FOV
- composition

문제를 보고 바로 source asset을 다시 만들지 않는다.

먼저 문제의 위치를 분석한다.

---

## 27. Runtime Review는 Approved를 다시 열 수 있다

Approved source라도 실제 게임 화면에서 문제가 발견될 수 있다.

예:

```text
APPROVED
↓
EXPORT
↓
RUNTIME REVIEW
↓
readability failure
```

이 경우:

- Export만 수정
- Engine 설정 수정
- Environment 수정
- Source asset 수정

중 적절한 지점을 선택한다.

필요하면 수정 Candidate를 만들고 다시 승인한다.

Approved는 현재 기준이지 영구적으로 재검토 불가능한 상태가 아니다.

---

## 28. 기존 Approved 자산은 강한 Review 기준이다

새 Candidate를 볼 때 다음과 비교할 수 있다.

- 대표 캐릭터
- 대표 환경
- 승인된 icon
- 기존 animation
- 현재 game screenshot

특히 스타일이 성숙한 프로젝트에서는 Reference보다
기존 Approved asset이 더 강한 기준이 될 수 있다.

하지만 “기존 것과 다르다”는 이유만으로 자동 반려하지 않는다.

새로운 결과가 더 나은 방향을 만들 수도 있다.

큰 변화라면 디렉터가 판단한다.

---

## 29. Art Direction과의 일관성을 본다

Art Review에서는 필요하면 다음 질문을 한다.

- 현재 Direction Summary와 맞는가?
- 핵심 시각 키워드가 보이는가?
- 금지사항을 위반하지 않는가?
- 형태 언어가 맞는가?
- 캐릭터/배경 관계가 맞는가?
- 가독성 우선순위를 해치지 않는가?
- 탐색 중인 방향을 확정 규칙처럼 사용하지 않았는가?

Art Direction은 Review의 기준이지만,
새로운 시도가 항상 기존 문장과 100% 동일해야 한다는 뜻은 아니다.

디렉터가 더 나은 방향을 채택하면 Art Direction이 발전할 수 있다.

---

## 30. Asset Brief와의 적합성을 본다

개별 중요 자산에서는 Asset Brief가 Review 기준이 된다.

예:

- 역할
- 게임 기능
- 반드시 들어갈 요소
- 피해야 할 요소
- variant
- technical constraint
- current request

좋은 그림이라도 Asset Brief의 핵심 기능을 충족하지 못하면
해당 자산으로는 적합하지 않을 수 있다.

---

## 31. 플레이 가독성을 미적 품질의 일부로 본다

게임 아트에서 가독성은 단순 기술 문제가 아니다.

예:

- 적/아군 구분
- 직업 구분
- 무기 식별
- 상호작용 오브젝트 식별
- 위험 요소 식별
- 아이템 중요도
- 이동 경로
- 팀 색
- 보스 약점

이 정보가 실제 플레이에서 읽히지 않으면
개별 이미지가 아름다워도 게임 아트로는 실패할 수 있다.

---

## 32. 가독성과 미적 방향이 충돌할 수 있다

예:

```text
목표:
어두운 공포 분위기

문제:
적이 너무 안 보임
```

이 경우 단순히 밝게 만드는 것만이 답은 아닐 수 있다.

가능한 해결:

- silhouette contrast
- rim light
- movement cue
- local highlight
- material difference
- background suppression

Art Review는 미적 방향을 버리지 않으면서
기능적 요구를 해결하는 방법을 찾는다.

---

## 33. Review 기준을 숫자 점수표로 과도하게 만들지 않는다

예:

```text
Style Match: 8.3
Readability: 7.4
Appeal: 9.1
```

같은 scoring system을 기본으로 만들지 않는다.

숫자가 실제 판단보다 정교해 보이는 착시를 만들 수 있다.

필요하면 일부 측정 지표를 사용할 수 있지만
최종 Art Review는 의미 있는 설명과 비교를 중심으로 한다.

---

## 34. 랭킹을 강제하지 않는다

항상:

```text
1위 B
2위 C
3위 A
```

로 정리할 필요는 없다.

다음처럼 말할 수 있다.

```text
A:
가장 단순하고 읽기 쉬움

B:
현재 방향과 가장 일관됨

C:
개성은 가장 강하지만 기존 family와 차이가 큼
```

서로 다른 장단점을 보여주고
디렉터가 무엇을 우선할지 선택할 수 있게 한다.

---

## 35. 후보가 너무 비슷하면 Review 자체가 실패할 수 있다

A/B/C가 사실상 같은 결과라면
디렉터가 선택할 정보가 없다.

Concept 또는 초기 Candidate 단계에서는
의미 있는 차이를 만들도록 한다.

예:

- proportion
- silhouette
- equipment
- density
- color hierarchy
- material
- lighting responsibility

중 무엇을 탐색하는지 분명히 한다.

---

## 36. 후보가 너무 달라도 판단 목적을 잃을 수 있다

반대로 한 번에 모든 요소가 다르면
무엇이 더 좋은지 원인을 알기 어렵다.

예:

```text
A:
다른 얼굴
다른 포즈
다른 조명
다른 색
다른 무기

B:
모든 요소 완전히 다름
```

최종 비교에서는 특정 판단 축을 통제하는 편이 더 유용할 수 있다.

Review 목적에 맞게 비교 설계를 한다.

---

## 37. Claude의 비전 분석을 활용할 수 있다

Claude가 이미지를 볼 수 있다면 다음을 도울 수 있다.

- 누락 요소 탐지
- 후보 차이 정리
- silhouette 비교
- detail density 차이
- 배경과 캐릭터 관계
- Art Direction 충돌 후보
- screenshot 가독성 문제
- Reference와 차이

하지만 비전 분석을 최종 미적 권위로 취급하지 않는다.

---

## 38. 코드 기반 분석과 비전 분석을 함께 사용할 수 있다

예:

```text
비전 분석:
배경과 캐릭터가 비슷한 밝기로 보여 분리가 약해 보임.

코드 분석:
캐릭터와 주변 배경의 평균 luminance 차이가 작음.
```

두 정보가 함께 있으면 문제를 더 구체적으로 설명할 수 있다.

하지만 측정 수치 하나로 최종 디자인 판단을 대신하지 않는다.

---

## 39. Art Review에서 확인할 수 있는 질문

필요할 때 다음 질문 중 일부를 사용할 수 있다.

### 목적

- 이 자산의 역할이 즉시 이해되는가?
- 플레이 중 필요한 정보를 전달하는가?

### 형태

- 실루엣이 읽히는가?
- 비율이 현재 방향과 맞는가?
- 다른 자산과 구분되는가?

### 캐릭터성

- 주인공 / 보스 / NPC의 역할이 느껴지는가?
- 너무 평범하거나 과장되지 않았는가?

### 환경

- 플레이 경로를 방해하지 않는가?
- 랜드마크가 필요한 만큼 읽히는가?
- 반복감이 지나치지 않은가?

### 색 / 명암

- 시각적 우선순위가 맞는가?
- 배경과 대상이 분리되는가?
- 강조색이 남발되지 않는가?

### 질감

- 재질이 의도대로 읽히는가?
- texture가 형태를 방해하지 않는가?

### 조명

- asset lighting과 engine lighting이 충돌하지 않는가?
- 중요한 형태가 죽지 않는가?

### 전체 일관성

- 기존 Approved와 같은 게임처럼 보이는가?
- 그렇다고 모두 복제처럼 보이지는 않는가?

이 질문을 모든 리뷰에서 체크리스트처럼 사용하지 않는다.

---

## 40. 중요한 자산에서는 Review 관점을 여러 번 바꿀 수 있다

예:

### 단독 이미지

형태와 디자인 확인.

### 작은 표시 크기

실루엣과 정보 밀도 확인.

### 실제 배경

가독성 확인.

### 게임 UI 포함

시각적 우선순위 확인.

### Animation

움직임에서 형태 유지 확인.

### VFX 포함

전투 중 식별 가능성 확인.

대표 자산에서는 한 장의 정지 이미지보다
여러 조건에서 보는 것이 유용하다.

---

## 41. Review는 실제 플레이 조건을 존중한다

게임에서 캐릭터가 80px 높이로 보이는데
800px 확대 이미지만 검토하면 잘못된 판단을 할 수 있다.

가능하면 실제 사용 조건을 확인한다.

예:

- typical camera distance
- on-screen size
- mobile screen
- fast movement
- multiplayer density
- night lighting
- common background
- UI overlap

아트는 최종 사용 조건에서 평가해야 한다.

---

## 42. 기술 문제와 미적 문제를 함께 수정할 수 있다

둘을 구분한다고 해서 항상 순차적으로만 처리해야 하는 것은 아니다.

예:

```text
문제 1:
sprite dimensions 잘못됨

문제 2:
무기 silhouette 약함
```

한 번의 수정 작업에서 함께 해결할 수 있다.

다만 어떤 문제가 기술 문제였고 어떤 문제가 미적 판단이었는지
의미를 혼동하지 않는다.

---

## 43. 명백한 기술 실패는 디렉터에게 보여주지 않아도 된다

예:

- 파일 깨짐
- 완전히 잘못된 dimensions
- alpha 누락
- export 실패
- frame 누락
- 잘못된 asset

처럼 명백한 기술 오류는
Art Review 전에 수정하거나 제외할 수 있다.

이것은 Claude가 미적 후보를 임의로 검열하는 것과 다르다.

기술적으로 비교 자체가 불가능한 결과를 정리하는 것이다.

---

## 44. 미적 이유로 Claude가 후보를 숨기지 않는다

Claude가 개인적으로 마음에 들지 않는다는 이유로
Candidate를 디렉터에게 보여주지 않는 것을 기본으로 하지 않는다.

다만 다음처럼 명확한 근거가 있다면 설명할 수 있다.

```text
Candidate C:
현재 Art Direction의 금지사항인 glossy plastic 표현이 강함.
그래도 비교를 위해 포함.
```

또는 디렉터가:

> Art Direction 위반 후보는 미리 제거해.

라고 명시했다면 그 기준을 적용할 수 있다.

---

## 45. Review는 사람을 병목으로 만들지 않는다

모든 작은 기술 작업마다 디렉터 승인을 요구하지 않는다.

예:

- resize
- naming
- format conversion
- 이미 승인된 rule 적용
- 명확한 export
- technical fix
- batch validation

은 기존 규칙이 명확하면 자율적으로 진행할 수 있다.

디렉터의 판단이 필요한 지점은 주로:

- 중요한 미적 방향
- 대표 자산 채택
- 여러 합리적 방향 중 선택
- 기존 Art Direction과 충돌하는 변화
- 큰 스타일 변경
- “충분히 좋은가”의 결정

이다.

---

## 46. 반대로 사람의 판단을 건너뛰지 않는다

자동화가 가능하다는 이유로:

```text
AI 생성
↓
AI 평가
↓
AI 최고점
↓
자동 승인
```

하는 구조를 기본으로 만들지 않는다.

특히 다음은 사람이 개입할 가치가 높다.

- 주인공
- 대표 캐릭터
- 보스
- 전체 스타일 기준 자산
- 주요 환경
- 핵심 UI 비주얼
- 프로젝트 Art Direction 변경
- 중요한 runtime 문제 해결

---

## 47. 동일 계열 반복 자산의 Review

asset family가 이미 확정된 경우
매 자산마다 동일한 강도의 Art Review가 필요하지 않을 수 있다.

예:

```text
기사 family 기준 승인
↓
기사 20종 제작
```

이 경우 다음을 자동 또는 반자동으로 확인할 수 있다.

- proportions
- palette
- dimensions
- naming
- family rule

그리고 대표 샘플 또는 이상치 중심으로 Art Review를 할 수 있다.

하지만 반복 작업 중 drift가 생기면 다시 깊게 검토한다.

---

## 48. Sample Review와 Batch Review

대량 작업에서는 다음 흐름이 유용하다.

```text
대표 샘플 제작
↓
Director Review
↓
방향 승인
↓
Batch
↓
Technical Validation
↓
Spot Review
↓
이상치 수정
```

처음부터 100개를 만든 뒤 전체 방향이 틀렸음을 발견하지 않도록 한다.

---

## 49. Spot Review

대량 자산에서는 모든 파일을 동일한 깊이로 볼 필요가 없을 수 있다.

예:

- 랜덤 샘플
- edge case
- 가장 복잡한 자산
- 가장 작은 표시 자산
- 자동 검사 warning이 있는 자산
- 기존 Approved와 차이가 큰 자산

등을 우선 볼 수 있다.

다만 중요한 대표 자산은 별도로 깊게 검토한다.

---

## 50. 이상치 탐지와 미적 자동 평가를 구분한다

자동화는 다음과 같은 이상치를 찾는 데 유용할 수 있다.

- color count 급증
- dimensions mismatch
- edge density 급증
- 파일 누락
- outline width deviation
- brightness distribution 이상
- frame count mismatch

이런 결과는 Review 대상을 좁히는 데 도움을 준다.

하지만:

> 이상치 = 나쁜 아트

로 자동 결론 내리지 않는다.

의도적인 예외일 수도 있다.

---

## 51. 예외는 허용한다

프로젝트 규칙과 다른 자산이 존재할 수 있다.

예:

- 보스만 훨씬 큰 실루엣
- 특정 지역만 다른 색 방향
- 특별한 UI만 다른 재질
- 한 캐릭터만 outline 없음

예외가 의도적이고 승인되었다면 정상이다.

Validator나 Review 시스템이 모든 예외를 오류로 되돌리지 않도록 한다.

---

## 52. 예외의 범위를 기록할 수 있다

중요한 예외는 다음처럼 남길 수 있다.

```text
Asset:
Boss A

Exception:
전체 캐릭터는 outline 사용.
Boss A는 의도적으로 outline 없음.

Scope:
individual asset
```

이런 정보는 향후 Claude가 예외를 전체 규칙으로 확대하거나
반대로 실수로 수정하는 것을 막는다.

---

## 53. Review에서 최신 디렉터 지시를 반영한다

기존 문서보다 최신의 명확한 디렉터 지시가 우선할 수 있다.

예:

```text
기존:
캐릭터는 hard outline

현재:
이번 주인공은 outline 없이 가자.
```

이 경우 이것이:

- individual exception인지
- project-wide change인지

구분한다.

국소 지시를 전체 Art Direction 변경으로 자동 확대하지 않는다.

---

## 54. 기존 승인 결과를 Claude가 임의로 뒤집지 않는다

이미 Approved된 자산에 대해
Claude가 더 좋은 대안을 발견했다고 해서
현재 승인 상태를 자동 변경하지 않는다.

가능한 행동:

```text
현재 Approved는 유지.

다만:
새 후보 B가 작은 화면 가독성에서 더 나아 보인다.
원하면 비교할 수 있다.
```

최종 변경은 디렉터가 결정한다.

---

## 55. Review의 종료 조건

Review는 끝없이 수정하기 위한 과정이 아니다.

디렉터가 현재 목적에 충분하다고 판단하면 멈춘다.

예:

- prototype에 충분
- vertical slice 기준 만족
- production asset으로 충분
- 현재 플랫폼에서 충분
- 비용 대비 추가 수정 가치 낮음

“완벽한 아트”라는 추상적 목표보다
현재 게임과 제작 단계에서 충분한지를 본다.

---

## 56. 개발 단계에 따라 Review 기준이 달라질 수 있다

### Prototype

중요:

- 방향 확인
- 빠른 가독성
- 큰 문제 탐지

완벽한 polish는 필요하지 않을 수 있다.

### Vertical Slice

중요:

- 대표 품질
- 핵심 스타일 일관성
- runtime result

### Production

중요:

- 반복 일관성
- technical compliance
- 효율적인 review

### Polish

중요:

- 작은 시각 문제
- runtime interaction
- consistency
- final presentation

같은 자산이라도 개발 단계에 따라 요구 완성도가 달라질 수 있다.

---

## 57. Review 자료는 필요할 때만 만든다

다음과 같은 자료를 사용할 수 있다.

- contact sheet
- side-by-side image
- overlay
- actual game screenshot
- before / after
- zoomed detail
- grayscale comparison
- silhouette comparison
- animation clip
- HTML review page

모든 Review에 별도 자료를 만들 필요는 없다.

디렉터가 판단하기 쉬워지는 경우에만 사용한다.

---

## 58. Review를 위한 이미지 가공은 원본을 바꾸지 않는다

예:

- 배경 통일
- 크기 통일
- label 추가
- crop
- contact sheet

같은 비교용 가공은 Review material일 수 있다.

이 결과를 Approved source 자체와 혼동하지 않는다.

---

## 59. Review 결과를 Asset Lifecycle에 반영한다

개념적으로:

```text
CANDIDATE
↓
REVIEW
↓
APPROVED
```

또는:

```text
CANDIDATE
↓
REVIEW
↓
REVISION
↓
NEW CANDIDATE
```

또는:

```text
CANDIDATE
↓
REVIEW
↓
REJECTED
```

또는:

```text
CANDIDATE
↓
REVIEW
↓
ON HOLD
```

Lifecycle 상태 의미 자체는 `06_ASSET_LIFECYCLE.md`를 따른다.

---

## 60. Review 결과를 Art Direction에 반영할 때 조심한다

한 자산에서:

> “갑옷이 너무 복잡하다.”

라는 피드백이 나왔다고 해서
즉시:

> 모든 캐릭터 갑옷 detail을 줄인다.

로 확장하지 않는다.

다음 경우에 프로젝트 방향으로 승격할 수 있다.

- 디렉터가 명시적으로 전체 규칙으로 결정
- 같은 피드백이 반복됨
- 여러 자산에서 같은 문제 확인
- 실제 게임 화면에서 구조적 문제로 확인

세부 학습 승격 기준은 `11_LEARNING_AND_REUSE.md`에서 다룬다.

---

## 61. Review 결과와 Style Spec

Review 중 반복적으로 확인된 기술 규칙이 있을 수 있다.

예:

```text
64px보다 큰 sprite에서는
현재 게임의 밀도가 과해 보임.
```

하지만 이것을 즉시 Style Spec의 수치로 확정하지 않는다.

필요하면:

- 추가 테스트
- 기존 자산 비교
- 디렉터 결정

을 거쳐 프로젝트 규칙으로 기록한다.

Style Spec은 Review의 자동 산출물이 아니다.

---

## 62. Technical Review 결과의 표현

가능하면 간단하게 표현한다.

예:

```text
Technical Review

PASS
- dimensions
- alpha
- format

WARNING
- palette 34 colors / target 32

FAIL
- frame 7 missing
```

하지만 모든 프로젝트에 같은 output format을 강제하지 않는다.

중요한 것은 디렉터나 작업자가
무엇이 문제인지 빠르게 알 수 있는 것이다.

---

## 63. Art Review 결과의 표현

예:

```text
Art Review

강점
- 실루엣이 가장 잘 읽힘
- 기존 기사 계열과 일관성 좋음

주의
- 방패 디테일이 작은 화면에서 사라짐

추천
- B를 기준으로 방패 형태만 단순화
```

또는 간단히:

```text
B 추천.
현재 방향과 가장 일관되고
작은 화면에서 무기 구분이 가장 명확함.
```

Review 문서를 장황한 평론으로 만들 필요는 없다.

---

## 64. 확실하지 않은 판단은 확실하지 않다고 말한다

예:

> C가 더 개성 있어 보이지만, 실제 게임 크기에서는 복잡도가 과할 가능성이 있다. Runtime test가 필요하다.

이런 표현은 정상이다.

Claude가 모든 미적 문제에 확정적인 답을 가진 것처럼 행동하지 않는다.

---

## 65. 충돌하는 장점을 숨기지 않는다

예:

```text
A
가독성은 가장 좋음
개성은 가장 약함

B
개성은 가장 강함
배경에서 묻힐 위험 있음
```

둘을 억지로 하나의 순위로 압축하지 않는다.

디렉터가 무엇을 우선하는지 결정할 수 있도록 trade-off를 보여준다.

---

## 66. Review가 Art Direction을 발전시킬 수 있다

실제 제작을 통해 기존 방향의 한계가 보일 수 있다.

예:

```text
기존 방향:
배경 디테일 풍부

Runtime Review:
작은 캐릭터가 배경에 계속 묻힘

Director Decision:
이동 경로 주변의 detail density를 낮춘다.
```

이 경우 Review는 Art Direction 발전의 근거가 된다.

하지만 변경 권한은 디렉터에게 있다.

---

## 67. Review가 제작 방법을 바꿀 수 있다

Review 결과가 단순 이미지 수정이 아니라
제작 방식 자체의 문제를 드러낼 수 있다.

예:

```text
문제:
8방향 캐릭터 일관성이 계속 깨짐

판단:
현재 생성 방식의 한계

대응:
3D 기준 source 도입
```

이런 결정은 정상적인 Art Studio 운영이다.

---

## 68. Review와 도구 평가를 구분한다

특정 Candidate가 좋지 않았다고 해서
즉시 해당 생성 도구 전체가 나쁘다고 결론 내리지 않는다.

반대로 한 번 좋은 결과가 나왔다고
그 도구를 프로젝트 표준으로 고정하지 않는다.

도구 평가는 반복 경험을 통해 별도로 축적한다.

---

## 69. Review에서 라이선스나 출처 문제가 발견될 수 있다

외부 에셋이나 Reference 기반 작업에서는
사용 조건이 실제 자산 채택에 영향을 줄 수 있다.

예:

- 라이선스 불명확
- 사용 범위 제한
- attribution 필요
- 상업적 사용 불가

이 경우 미적으로 좋아도 Approved source로 사용할 수 없을 수 있다.

구체적인 라이선스 관리 시스템은 이 문서의 핵심 범위가 아니지만,
실제 채택 가능성에 영향을 주는 문제라면 Review에서 무시하지 않는다.

---

## 70. Review의 깊이는 자산 중요도에 맞춘다

### 낮은 중요도 / 반복 자산

- 기술 검사 중심
- 빠른 시각 확인
- 기존 family rule 적용

### 중간 중요도

- Art Direction 일관성
- gameplay readability
- 필요 시 비교

### 높은 중요도 / 대표 자산

- Concept Review
- 여러 Candidate
- runtime validation
- 상세 비교
- Director decision
- 필요 시 Review Log

모든 자산을 대표 캐릭터처럼 다루지 않는다.

---

## 71. Review를 위한 과도한 승인 절차를 만들지 않는다

다음과 같은 구조를 기본값으로 만들지 않는다.

```text
Technical Reviewer
↓
Art Reviewer
↓
Senior Reviewer
↓
Director Approval
↓
Final Approval
↓
Export Approval
```

이 Art Studio는 거대한 기업 승인 시스템이 아니다.

필요한 판단만 명확히 분리한다.

---

## 72. Review에서 가장 중요한 세 가지 질문

복잡한 상황에서 방향을 잃으면 다음으로 돌아간다.

### 1. 기술적으로 정상인가?

측정 가능한 요구를 만족하는가?

### 2. 게임 아트로서 적절한가?

Art Direction, gameplay, 실제 화면에 맞는가?

### 3. 누가 최종 결정을 해야 하는가?

기술적 문제인가,
Claude가 의견을 낼 영역인가,
디렉터의 미적 결정이 필요한가?

이 세 질문이면 대부분의 Review 문제를 정리할 수 있다.

---

## 73. 다른 문서와의 관계

### `02_DIRECTOR_RELATIONSHIP.md`

사람과 Claude의 권한 원칙을 정의한다.

이 문서는 그 원칙을 실제 Review 과정에 적용한다.

---

### `04_ART_DIRECTION_SYSTEM.md`

어떤 시각적 축을 볼 수 있는지 정의한다.

이 문서는 그 축을 실제 Candidate와 game screenshot에 적용한다.

---

### `06_ASSET_LIFECYCLE.md`

Review 결과가 어떤 자산 상태 변화로 이어지는지 정의한다.

---

### `07_GENERATION_WORKFLOW.md`

Review 이전에 Candidate가 어떻게 준비되고,
피드백이 다시 수정 작업으로 어떻게 이어지는지 정의한다.

---

### `09_ASSET_SPEC_AND_VALIDATION.md`

Technical Review의 구체적인 검증 대상과 자동화 원칙을 정의한다.

---

### `10_ENGINE_HANDOFF.md`

Export와 Runtime Review를 위한 실제 엔진 전달 과정을 정의한다.

---

### `11_LEARNING_AND_REUSE.md`

Review에서 반복적으로 확인된 결정과 실패 중
무엇을 장기 지식으로 남길지 정의한다.

---

### `REVIEW_LOG.md`

중요한 Director decision과 이유를 실제 프로젝트에 기록하는 템플릿이다.

---

## 74. 이 문서에서 다루지 않는 것

다음은 다른 문서에서 상세화한다.

### 기술 규격 수치와 검사 구현

`09_ASSET_SPEC_AND_VALIDATION.md`

### 엔진 import / export 상세

`10_ENGINE_HANDOFF.md`

### 자산 상태 정의

`06_ASSET_LIFECYCLE.md`

### Candidate 제작 순서

`07_GENERATION_WORKFLOW.md`

### 프로젝트별 Style Spec

`STYLE_SPEC.md`

### Review 기록 형식

`REVIEW_LOG.md`

### 공통 학습 승격 기준

`11_LEARNING_AND_REUSE.md`

이 문서는 **검토의 의미, 판단의 경계, 승인 권한**에 집중한다.

---

## 75. 핵심 원칙 요약

Art Studio의 Review & Approval은
AI가 아트를 자동 채점하고 승인하는 시스템이 아니다.

핵심 원칙은 다음과 같다.

> **Technical Review와 Art Review를 구분한다.**

> **기술적으로 정상이라는 사실을 좋은 아트라는 판단으로 확대하지 않는다.**

> **Claude의 미적 의견을 객관적 사실처럼 말하지 않는다.**

> **Claude는 수동적으로 침묵하지 않고 적극적으로 비교·분석·추천한다.**

> **최종 미적 승인 권한은 게임 디렉터에게 있다.**

> **후보는 디렉터가 차이를 쉽게 판단할 수 있는 형태로 제시한다.**

> **Review는 실제 게임 화면, 카메라, 조명, 배경, UI, VFX를 포함할 수 있다.**

> **Runtime에서 문제가 보이면 source, export, environment, engine, camera 중 원인을 먼저 구분한다.**

> **반려 이유는 학습 정보가 될 수 있지만 자동으로 프로젝트 전체 규칙이 되지는 않는다.**

> **기존 Approved를 Claude가 임의로 뒤집지 않는다.**

> **반복 자산에는 가볍게, 대표 자산에는 필요한 만큼 깊게 Review한다.**

> **사람을 모든 작은 작업의 병목으로 만들지 않으면서도 중요한 미적 판단은 자동화로 대체하지 않는다.**

> **Review의 목적은 점수를 만드는 것이 아니라 좋은 판단을 가능하게 만드는 것이다.**
