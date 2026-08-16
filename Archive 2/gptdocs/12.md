# 11_LEARNING_AND_REUSE

## 1. 문서의 역할

이 문서는 Art Studio가 여러 게임 프로젝트를 수행하면서 얻은 경험 중 **무엇을 재사용 가능한 스튜디오 지식으로 축적하고, 무엇을 프로젝트 고유의 결정으로 남길지** 정의한다.

이 문서는 특정 게임의 Art Direction을 다시 설명하지 않는다.

이 문서는 모든 작업 기록을 지식베이스로 저장하는 문서도 아니다.

이 문서는 자동으로 모든 경험을 공통 규칙으로 승격하는 시스템도 아니다.

이 문서는 특정 도구의 사용법을 정리하는 매뉴얼도 아니다.

핵심 질문은 다음과 같다.

> **이번 프로젝트에서 얻은 경험 중 무엇이 다른 프로젝트에서도 재사용할 수 있고, 무엇은 이 게임에만 남아야 하는가?**

---

## 2. 가장 중요한 원칙

Art Studio가 장기적으로 기억해야 하는 것은 주로 다음이다.

```text
기법
검증 방법
도구 연결법
제작 방법
반복 작업
export 경험
runtime 검증 경험
```

반대로 다음은 기본적으로 프로젝트 안에 남긴다.

```text
화풍
팔레트
캐릭터 비율
세계관
디자인 언어
특정 게임 prompt
승인된 미적 결정
특정 게임의 감정과 분위기
```

핵심 원칙:

> **기법은 학습하지만 스타일은 전염시키지 않는다.**

---

## 3. Learning과 Reuse는 같은 말이 아니다

Learning은:

> 작업 경험에서 무엇을 배웠는가?

Reuse는:

> 그 배움을 다른 작업이나 다른 프로젝트에서도 다시 사용할 수 있는가?

이다.

모든 학습이 재사용 가능한 것은 아니다.

예:

```text
학습:
이 게임에서는 캐릭터 머리를 크게 해야 잘 읽힌다.
```

이것은 프로젝트별 아트 방향일 수 있다.

반면:

```text
학습:
작은 화면 캐릭터 비교에서는 실제 runtime scale contact sheet가 매우 유용했다.
```

이것은 다른 프로젝트에서도 재사용 가능한 제작 기법일 수 있다.

---

## 4. 프로젝트 지식과 Studio 지식을 구분한다

### Project Knowledge

특정 게임의 시각적 정체성과 직접 연결된 지식.

예:

- 이 게임은 낮은 채도를 사용한다.
- 기사 계열은 넓은 어깨를 가진다.
- 배경은 캐릭터보다 contrast가 낮다.
- 주인공은 큰 머리 비율을 사용한다.
- 특정 보스만 outline이 없다.
- 특정 지역은 붉은 조명을 사용한다.

이런 정보는 해당 프로젝트 안에 남긴다.

---

### Studio Knowledge

다른 프로젝트에서도 재사용할 수 있는 제작 능력과 경험.

예:

- alpha fringe를 찾는 방법
- tile seam checker
- sprite contact sheet generator
- Unity pixel import 문제 해결법
- 8방향 캐릭터를 3D source로 만드는 방법
- batch export helper
- palette analyzer
- runtime screenshot automation
- generator API integration 경험

이런 정보는 반복성과 범용성이 확인되면 Studio 공통 지식이 될 수 있다.

---

## 5. 스타일은 프로젝트의 자산이다

다음은 Studio 기본값으로 올리지 않는다.

- 특정 색상표
- 특정 캐릭터 비율
- 특정 outline
- 특정 조명
- 특정 texture density
- 특정 animation feel
- 특정 UI 형태
- 특정 게임 Reference
- 특정 세계관 고증 방식
- 특정 게임의 금지사항

예:

```text
game-a:
outline = 1px
```

이라고 해서:

```text
studio default:
outline = 1px
```

로 만들지 않는다.

---

## 6. 기술은 공통화할 수 있다

예:

```text
1px outline을 검사하는 코드
```

자체는 범용 기술이 될 수 있다.

하지만:

```text
outline은 항상 1px이어야 한다.
```

는 Studio 규칙이 아니다.

같은 방식으로:

```text
palette analyzer
```

는 공통화할 수 있지만:

```text
모든 게임은 24 colors
```

로 만들지 않는다.

---

## 7. 성공한 결과를 자동으로 일반화하지 않는다

한 프로젝트에서 잘 작동했다고
다른 프로젝트에서도 기본값으로 사용하지 않는다.

예:

```text
PixelLab으로 8방향 sprite 제작 성공
```

이 경험은:

> PixelLab이 특정 조건에서 유용했다.

라는 Studio knowledge가 될 수 있다.

하지만:

> 모든 8방향 sprite는 PixelLab을 사용한다.

로 일반화하지 않는다.

---

## 8. 실패도 자동으로 일반화하지 않는다

예:

```text
Generator X가 한 캐릭터에서 실패
```

했다고 해서:

> Generator X는 캐릭터 작업에 부적합하다.

로 결론 내리지 않는다.

실패 원인이 다음일 수 있다.

- prompt
- 모델 버전
- 작업 종류
- 스타일
- 해상도
- consistency requirement
- 입력 reference
- tool limitation

반복된 경험과 조건을 확인한다.

---

## 9. 한 번의 Art Review를 전체 규칙으로 만들지 않는다

예:

```text
"이 갑옷은 너무 복잡하다."
```

라는 디렉터 피드백은
그 자산에 대한 의견일 수 있다.

이를:

```text
모든 갑옷 detail을 줄인다.
```

로 자동 일반화하지 않는다.

프로젝트 전체 규칙으로 승격하려면:

- 디렉터가 명시적으로 전체 규칙으로 결정하거나
- 같은 문제가 반복되거나
- 여러 자산에서 구조적으로 확인되거나
- 실제 게임 화면에서 반복적으로 문제가 나타나는

등의 근거가 필요하다.

---

## 10. 공통화는 반복이 확인된 후 한다

원칙:

> **미리 공통화하지 말고, 반복이 확인되면 공통화한다.**

다음 조건을 고려한다.

- 여러 작업에서 반복됨
- 여러 프로젝트에서 반복됨
- 특정 스타일에 종속되지 않음
- 재사용 가치가 있음
- 유지 비용보다 효과가 큼
- 입력과 출력이 비교적 명확함

한 프로젝트에서 한 번 사용한 방법은
우선 그 프로젝트에 남아 있어도 된다.

---

## 11. 공통화 수준

재사용은 여러 수준에서 일어날 수 있다.

### 개인 작업 수준

한 자산 안에서 반복.

예:

```text
같은 character의 4 variant
```

---

### Project 수준

같은 게임 안에서 반복.

예:

```text
기사 계열 제작 방식
```

---

### Studio 수준

여러 게임에서 재사용.

예:

```text
sprite sheet generator
```

---

### Tool-specific 수준

특정 도구에 대한 사용 경험.

예:

```text
FLUX API batch 호출법
```

이 정보는 tool guide나 공통 기술 노트가 될 수 있다.

---

## 12. Project 내부에서 재사용하는 것

특정 게임 안에서는 다음을 재사용할 수 있다.

- Art Direction
- Style Spec
- approved asset
- asset family rule
- palette
- character proportion
- prompt
- reference
- review decision
- runtime screenshot
- project-specific exporter setting

이 재사용은 다른 게임으로 자동 전파하지 않는다.

---

## 13. Studio로 승격할 수 있는 것

예:

### Validator

- dimensions checker
- alpha checker
- palette analyzer
- seam checker
- naming checker

### Exporter

- sprite sheet exporter
- image optimizer
- channel packer
- engine copy helper

### Workflow

- contact sheet generation
- fixed-camera screenshot capture
- batch candidate collection
- sample-before-batch workflow

### Tool Integration

- API wrapper
- MCP connection
- authentication note
- file transfer helper

### Production Knowledge

- 3D render → 2D sprite 방식
- pixel cleanup method
- alpha edge cleanup
- runtime comparison technique

---

## 14. 공통화하면 안 되는 것

다음은 기본적으로 Studio common으로 올리지 않는다.

- 특정 게임 prompt
- 특정 게임 palette
- 특정 캐릭터 비율
- 특정 세계관 reference
- 특정 프로젝트 approved asset
- 특정 게임의 anti-reference
- 특정 게임의 visual target screenshot
- 특정 게임의 금지 스타일
- 특정 게임의 감정적 방향

---

## 15. Prompt의 재사용

Prompt는 두 종류로 구분할 수 있다.

### 범용 Prompt 구조

예:

```text
subject
view
composition
technical constraint
negative condition
```

이런 prompt assembly 방식은 공통 기술이 될 수 있다.

### 프로젝트 고유 Prompt

예:

```text
특정 게임의 스타일 표현
특정 캐릭터 디자인
특정 palette
특정 reference
```

이것은 프로젝트에 남긴다.

---

## 16. Tool Knowledge

도구에 대한 경험은 Studio에 축적할 수 있다.

예:

```text
Tool:
PixelLab

Observed strength:
- directional sprite
- low-resolution control

Observed weakness:
- 특정 고밀도 스타일에서 디테일 한계
```

하지만 도구는 업데이트될 수 있다.

따라서 이런 기록을 영구적인 진리처럼 취급하지 않는다.

---

## 17. Tool Knowledge에는 조건을 남긴다

좋지 않은 기록:

```text
Tool X는 좋다.
```

좋은 기록:

```text
Tool X:
32–64px directional sprite에서
방향 일관성이 안정적이었다.
```

조건이 있어야 재사용 가능한 지식이 된다.

---

## 18. Tool Version 변화

AI 도구와 엔진은 빠르게 변한다.

다음이 바뀔 수 있다.

- model
- API
- 가격
- quality
- feature
- license
- export format

따라서 오래된 tool knowledge는
필요하면 다시 검증한다.

---

## 19. Recipe 형태의 지식

반복 가능한 제작 방법을 Recipe처럼 정리할 수 있다.

예:

```text
Low-res Character Workflow

1. silhouette concept
2. 3D blockout
3. fixed camera render
4. pixel conversion
5. manual cleanup
6. runtime test
```

하지만 이 Recipe가 모든 캐릭터 작업의 기본 workflow라는 뜻은 아니다.

특정 문제에 유용한 선택지다.

---

## 20. Pattern과 Rule을 구분한다

Pattern:

> 이런 상황에서 이 방법이 자주 유용했다.

Rule:

> 이 프로젝트에서는 반드시 이렇게 한다.

둘은 다르다.

Studio knowledge는 주로 Pattern과 capability를 축적한다.

Project knowledge는 필요한 경우 Rule을 가진다.

---

## 21. Recommendation과 Default를 구분한다

예:

```text
Recommendation:
픽셀 tile 작업에서는 seam preview를 먼저 만든다.
```

는 유용한 Studio knowledge일 수 있다.

하지만:

```text
Default:
모든 tile 작업은 5×5 preview 필수
```

로 강제할 필요는 없다.

---

## 22. 반복 실패에서 학습한다

같은 문제가 반복되면
공통 개선 후보가 된다.

예:

```text
문제:
alpha fringe가 자주 발생

반복:
3개 프로젝트에서 발생

대응:
alpha edge checker + cleanup tool
```

이런 경우 Studio tool로 승격할 가치가 높다.

---

## 23. 반복 성공에서 학습한다

예:

```text
runtime screenshot을
actual display scale로 비교하면
캐릭터 가독성 판단이 빨라짐.
```

여러 프로젝트에서 효과가 확인된다면
Studio workflow knowledge로 남길 수 있다.

---

## 24. 실패 원인을 분리한다

학습하려면 실패의 위치를 구분해야 한다.

예:

```text
실패:
캐릭터가 게임에서 흐림
```

원인이:

- source resolution
- export resize
- filtering
- camera
- post-processing

중 어디인지에 따라 학습 내용이 다르다.

잘못된 원인을 학습하면
나쁜 공통 규칙이 생긴다.

---

## 25. Runtime 경험은 중요한 학습이다

게임 화면에서만 알 수 있는 것이 있다.

예:

- 실제 표시 크기
- background interaction
- lighting
- VFX overlap
- UI hierarchy
- movement readability

따라서 Studio는 source 제작 경험뿐 아니라
runtime validation 경험도 축적할 수 있다.

---

## 26. Engine Knowledge

다음은 Studio 공통 기술로 축적할 수 있다.

예:

- Unity pixel import helper
- Godot atlas export
- Roblox texture upload flow
- Web image optimization

하지만:

```text
game-a specific material
game-b specific shader value
```

는 프로젝트 안에 남긴다.

---

## 27. Engine-specific Pattern

예:

```text
Unity pixel project에서
bilinear filtering 때문에 sprite가 흐려지는 문제가 반복된다.
```

이것은 Studio 기술 지식이 될 수 있다.

반면:

```text
Game A는 nearest filtering 사용
```

은 프로젝트 규칙이다.

---

## 28. Validator Knowledge

공통 validator는 매우 좋은 재사용 대상이다.

예:

- alpha
- dimensions
- palette count
- tile seam
- frame count
- naming
- missing file

이런 검사는 스타일과 비교적 독립적이다.

---

## 29. Validator Rule과 Validator Capability를 구분한다

예:

```text
Capability:
palette count 검사
```

는 Studio knowledge.

```text
Rule:
Game A palette <= 24
```

는 Project knowledge.

이 구분을 유지한다.

---

## 30. Exporter Knowledge

다음은 공통화하기 좋다.

- resize
- format conversion
- atlas
- channel packing
- naming
- engine copy

하지만 target path나 specific setting은 프로젝트별일 수 있다.

---

## 31. Reference 분석 방법

Reference 자체는 프로젝트 고유일 수 있다.

하지만 다음 방법은 공통 지식이 될 수 있다.

- 어떤 속성을 참고하는지 분리
- color / silhouette / lighting을 따로 분석
- anti-reference 기록
- reference 간 역할 구분

---

## 32. Art Direction 분석 방법

다음은 공통 능력이다.

- 감각적 표현을 기술 언어로 보조
- 형태 언어 분해
- silhouette 분석
- density 분석
- lighting responsibility 구분
- camera와 asset 관계 분석

하지만 실제 방향 값은 프로젝트에 남긴다.

---

## 33. 디렉터의 자연어 해석 경험

다음과 같은 표현을 실제 작업 언어로 번역하는 경험도 Studio 능력이 될 수 있다.

예:

```text
"너무 깨끗하다"
```

가능한 해석 방법:

- surface variation
- edge irregularity
- wear
- less uniform gradient

하지만 실제 해석은 항상 프로젝트 문맥을 다시 확인한다.

한 번의 해석을 사전처럼 고정하지 않는다.

---

## 34. Director Phrase Dictionary를 과도하게 만들지 않는다

예:

```text
"귀엽게" = 머리 40% 확대
```

같은 자동 번역 규칙을 만들지 않는다.

같은 표현도 프로젝트마다 의미가 다르다.

Studio가 학습해야 하는 것은
문맥을 보고 해석하는 방법이지
감각적 언어를 고정 formula로 바꾸는 것이 아니다.

---

## 35. Review Knowledge

다음은 공통화할 수 있다.

- 비교 조건 통제
- contact sheet
- actual runtime scale
- before / after
- silhouette comparison
- technical fact vs aesthetic opinion 분리

하지만:

```text
B 후보가 더 좋았다
```

라는 판단 자체는 프로젝트 기록이다.

---

## 36. Rejected Candidate에서 배우는 것

반려된 Candidate는 다음을 알려줄 수 있다.

- 어떤 방향이 맞지 않는가
- 어떤 제작 방식이 불안정한가
- 어떤 Reference가 잘못 해석되었는가
- 어떤 tool limitation이 있는가

하지만 모든 반려 Candidate를 영구 보존할 필요는 없다.

장기적으로 의미 있는 정보만 남긴다.

---

## 37. Approved Asset에서 배우는 것

Approved asset은 프로젝트 내부에서 강한 기준이 된다.

예:

- proportion
- density
- color
- silhouette
- material
- detail level

하지만 다른 게임의 기본 Reference로 자동 사용하지 않는다.

---

## 38. Cross-project Reference를 자동화하지 않는다

예:

```text
Game A hero가 성공적이었다.
```

고 해서 Game B 캐릭터 제작 시 자동 Reference로 불러오지 않는다.

다른 프로젝트 자료를 사용할 때는
명시적인 이유가 있어야 한다.

---

## 39. 스타일 오염 방지

Studio 공통 지식에는
게임 고유 시각 정보가 섞이지 않도록 주의한다.

예:

나쁜 공통 문서:

```text
캐릭터는 큰 머리를 사용한다.
```

좋은 공통 문서:

```text
작은 화면 캐릭터에서는
머리 비율이 가독성에 영향을 줄 수 있으므로
actual display size에서 비교한다.
```

---

## 40. 공통 지식은 문제 해결 방식 중심으로 만든다

Studio knowledge는 가능하면:

> 어떤 문제에서 어떤 방법이 유용했는가?

를 중심으로 한다.

예:

```text
Problem:
8-direction consistency

Useful approaches:
- 3D base
- directional sprite tool
- fixed-camera render
```

특정 스타일을 공통 규칙으로 만들지 않는다.

---

## 41. 학습의 단위

학습 단위는 다음처럼 다양할 수 있다.

- 하나의 tool trick
- validator
- exporter
- workflow pattern
- engine issue
- review method
- file management method
- production recipe

모든 학습을 같은 형식으로 저장할 필요는 없다.

---

## 42. 모든 경험을 문서화하지 않는다

다음은 굳이 장기 기록할 필요가 없을 수 있다.

- 한 번만 발생한 사소한 오류
- 쉽게 검색 가능한 기본 사용법
- 프로젝트에만 의미 있는 작은 수정
- 다시 사용할 가능성이 낮은 임시 방법

문서화 자체가 작업의 목적이 되지 않도록 한다.

---

## 43. 기록 가치 판단

다음 질문이 유용하다.

### 다시 발생할 가능성이 있는가?

### 다른 프로젝트에서도 쓸 수 있는가?

### 문제 해결 시간이 많이 들었는가?

### 다시 잊으면 같은 비용을 치를 가능성이 있는가?

### 반복 자동화할 가치가 있는가?

### 특정 스타일과 독립적인가?

여러 질문에 Yes라면 Studio knowledge 후보가 될 수 있다.

---

## 44. 공통화 전 검증

Studio 공통으로 승격하기 전에
가능하면 다음을 확인한다.

- 한 프로젝트에만 맞는 것은 아닌가?
- 특정 스타일에 묶여 있지 않은가?
- 특정 tool version에만 해당하지 않는가?
- 예외가 많은가?
- 재사용 가치가 실제로 있는가?
- 더 단순한 형태로 표현할 수 있는가?

---

## 45. 공통화의 비용

공통 도구는 유지해야 한다.

예:

- API 변경
- dependency
- bug
- documentation
- compatibility

따라서 한 번 시간을 절약했다고
무조건 Studio tool로 만들지 않는다.

---

## 46. 임시 Script와 공통 Tool을 구분한다

예:

```text
game-a/tmp/fix-red-channel.py
```

가 한 번 사용되었다고
바로:

```text
studio/tools/red-channel-fixer
```

로 승격하지 않는다.

반복 사용이 확인되면 이동할 수 있다.

---

## 47. Project Prototype Tool

특정 프로젝트에서 먼저 만들어 사용하고
범용성이 확인되면 Studio로 승격할 수 있다.

흐름:

```text
project-local
↓
repeated use
↓
generalize
↓
studio tool
```

이 방식이 자연스럽다.

---

## 48. 공통화 시 스타일 의존성을 제거한다

예:

Project script:

```text
if color == game_a_red:
...
```

를 Studio로 올리려면
프로젝트 값이 parameter로 빠져야 할 수 있다.

```text
input palette
```

처럼 일반화한다.

---

## 49. 너무 이른 추상화를 피한다

처음부터:

- universal asset framework
- ontology
- huge schema
- generic pipeline engine

을 만들지 않는다.

실제 반복 문제를 먼저 본다.

---

## 50. 너무 늦은 공통화도 피한다

반대로 여러 프로젝트에서
같은 작업을 계속 복사하고 있다면
공통화 가치가 있을 수 있다.

예:

```text
같은 alpha checker를
세 프로젝트에 각각 복사
```

이런 경우 Studio tool이 더 적절할 수 있다.

---

## 51. Learning Source

학습 정보는 다음에서 올 수 있다.

- Director Review
- Rejected Candidate
- Approved Asset
- runtime screenshot
- validation failure
- export problem
- tool experiment
- production batch
- external collaboration
- engine integration

하나의 source만 보지 않는다.

---

## 52. Review Log와 Learning

`REVIEW_LOG.md`는 중요한 프로젝트 결정을 기록한다.

그 기록 중 일부가 반복되면
Studio learning의 근거가 될 수 있다.

하지만 Review Log 전체를
Studio knowledge로 복사하지 않는다.

---

## 53. Style Spec과 Learning

Style Spec은 프로젝트 규칙이다.

예:

```text
palette <= 24
```

이 값 자체는 다른 프로젝트로 재사용하지 않는다.

다만:

```text
palette count validator
```

는 Studio 기술로 재사용할 수 있다.

---

## 54. Asset Manifest와 Learning

Manifest는 작업 규모와 상태를 보여줄 수 있다.

이를 통해 다음을 학습할 수 있다.

예:

- 어떤 자산 종류에서 반복 병목이 생기는가
- 어떤 export가 자주 실패하는가
- 어떤 batch가 반복되는가

하지만 Manifest를 분석 시스템으로 과도하게 확장하지 않는다.

---

## 55. Asset Brief와 Learning

Asset Brief가 반복적으로 같은 요구를 가진다면
asset family template이나 제작 패턴이 생길 수 있다.

예:

```text
모든 일반 적:
front/back/left/right 필요
```

이것은 해당 프로젝트 family rule일 수 있다.

다른 프로젝트로 자동 전파하지 않는다.

---

## 56. Engine Handoff와 Learning

반복적인 handoff 문제는 매우 좋은 공통 학습 대상이다.

예:

```text
Godot tile import에서
특정 padding 문제가 반복
```

이 문제 해결법이 여러 프로젝트에서 유효하면
Studio knowledge로 남길 수 있다.

---

## 57. Runtime Validation과 Learning

실제 게임 화면에서 반복적으로 나타난 문제는
공통 제작 방법을 발전시킬 수 있다.

예:

```text
작은 캐릭터는 source review보다
runtime scale review가 더 중요하다.
```

이런 경험은 다른 프로젝트에도 적용 가능한 원칙이 될 수 있다.

---

## 58. Art Direction 변경과 Learning

Art Direction이 바뀐 이유는 중요할 수 있다.

예:

```text
배경 detail 감소
이유:
runtime에서 character readability 부족
```

이 결정은 해당 프로젝트 기록이다.

다만:

```text
실제 display size에서 background density를 검증하는 방법
```

은 Studio technique이 될 수 있다.

---

## 59. 프로젝트 종료 시 회고

프로젝트나 milestone이 끝날 때
필요하면 짧게 회고할 수 있다.

질문 예:

- 무엇이 반복적으로 잘 작동했는가?
- 무엇이 계속 실패했는가?
- 어떤 도구가 어떤 조건에서 유용했는가?
- 어떤 validator가 필요했는가?
- 어떤 workflow가 반복되었는가?
- 무엇을 Studio로 올릴 가치가 있는가?

매 프로젝트마다 거대한 retrospective를 강제하지 않는다.

---

## 60. Milestone Learning

프로젝트 종료까지 기다리지 않아도 된다.

예:

- prototype 완료
- vertical slice 완료
- character batch 완료
- environment batch 완료

같은 milestone에서 공통화 후보를 찾을 수 있다.

---

## 61. Learning Backlog를 만들 수 있다

필요하면 다음처럼 후보만 적어둘 수 있다.

```text
Studio reuse candidates:
- tile repeat preview generator
- Roblox upload helper
- character contact sheet
```

즉시 구현하지 않아도 된다.

반복 가치가 확인되면 정식 공통 도구로 만든다.

---

## 62. 공통 지식의 위치

공통화된 결과는 필요에 따라 다음에 들어갈 수 있다.

```text
studio/tools/
studio/workflows/
studio/exporters/
studio/shared/
```

구체적인 하위 구조는 필요에 따라 결정한다.

---

## 63. Tool Guide

특정 도구 경험이 충분히 쌓이면
별도 guide를 만들 수 있다.

예:

```text
PIXELLAB_NOTES.md
BLENDER_2D_SOURCE.md
UNITY_ART_NOTES.md
```

하지만 이 문서 체계의 핵심 18개 문서를
도구 매뉴얼로 채우지 않는다.

---

## 64. Knowledge가 너무 오래된 경우

다음 경우 재검증할 수 있다.

- tool major update
- engine version change
- API change
- pricing change
- new model
- platform rule change

오래된 경험을 절대 규칙으로 유지하지 않는다.

---

## 65. Knowledge에 날짜를 붙일 수 있다

도구 정보처럼 변화가 빠른 내용은
필요하면 날짜를 기록할 수 있다.

예:

```text
Observed:
2026-08
```

모든 기술 노트에 날짜를 강제하지 않는다.

---

## 66. Knowledge에 Confidence를 남길 수 있다

필요하면 자연어로 표현할 수 있다.

예:

```text
한 프로젝트에서만 확인됨.
```

```text
세 프로젝트에서 반복 확인됨.
```

```text
현재 tool version에서만 확인됨.
```

복잡한 score system은 필요하지 않다.

---

## 67. Provenance

중요한 공통 지식이 어디서 왔는지
알 수 있으면 좋을 수 있다.

예:

```text
Derived from:
game-a character batch
game-c tile production
```

하지만 특정 프로젝트의 시각 정보까지
공통 문서에 복사하지 않는다.

---

## 68. Learning은 자동 추론만으로 승격하지 않는다

Claude가:

> 이건 공통 규칙인 것 같다.

고 판단했다고
즉시 Studio rule로 만들지 않는다.

가능하면 실제 반복을 확인한다.

---

## 69. Director가 공통화 여부를 직접 지시할 수 있다

디렉터가:

> 이 방식은 앞으로 다른 게임에서도 쓰자.

라고 명확히 말할 수 있다.

그 경우 공통화 후보로 적극 반영할 수 있다.

다만 스타일 자체를 공유하라는 뜻인지
제작 기법을 공유하라는 뜻인지 구분한다.

---

## 70. 프로젝트 스타일을 의도적으로 재사용하는 경우

예외적으로 사용자가:

> Game A와 같은 스타일로 Game B를 만든다.

고 명시할 수 있다.

이 경우 스타일 재사용이 의도된 것이다.

하지만 Studio가 자동으로 그런 관계를 만들지 않는다.

명시적 프로젝트 결정으로 처리한다.

---

## 71. Franchise / Sequel

후속작이나 같은 IP에서는
일부 스타일 규칙을 공유할 수 있다.

예:

```text
Game A
↓
Game A2
```

이 경우에도 무엇을 공유하고
무엇을 바꾸는지 프로젝트 수준에서 결정한다.

Studio 전체 기본값으로 올리지 않는다.

---

## 72. Asset Library

여러 프로젝트에서 공통으로 사용할 수 있는
실제 asset library가 있을 수도 있다.

예:

- generic texture
- font
- licensed icon
- common material

하지만 이런 공용 asset의 라이선스와 사용 범위를 확인한다.

스타일 고유 asset과 구분한다.

---

## 73. 구매 자산에서 배우는 것

구매 asset을 사용하면서 다음을 학습할 수 있다.

- 어떤 category는 구매가 효율적
- 어떤 format이 integration에 좋음
- 어떤 license가 유용함

이런 production knowledge는 공통화할 수 있다.

특정 구매 asset 자체는 별도 라이선스 자산이다.

---

## 74. 외주 경험에서 배우는 것

외부 제작자와 협업하면서:

- Brief 형식
- review 방식
- 전달 format
- revision cycle

에 대한 경험이 쌓일 수 있다.

범용적인 협업 방법은 Studio knowledge가 될 수 있다.

---

## 75. 비용과 시간 정보

필요하면 제작 방식 비교에 다음 경험을 활용할 수 있다.

예:

```text
방법 A:
빠르지만 수정성이 낮음

방법 B:
초기 비용 높지만 반복 생산에 유리
```

정확한 가격과 tool cost는 변할 수 있으므로
영구적인 수치보다 조건과 trade-off 중심으로 기록한다.

---

## 76. 생산 규모와 Learning

작은 작업에서 유용한 방법과
100개 batch에서 유용한 방법은 다를 수 있다.

예:

```text
1 asset:
대화형 생성

100 assets:
API batch
```

규모 조건을 함께 기억한다.

---

## 77. Tool Choice Learning

Studio는 시간이 지나며
문제 유형과 tool capability의 관계를 더 잘 이해하게 된다.

예:

```text
seamless tile
→ specialized tile tool often useful

exact layout
→ generator alone unreliable
```

이런 것은 capability map으로 발전할 수 있다.

---

## 78. Capability Map을 제품 목록으로 만들지 않는다

예:

좋은 형태:

```text
Need:
directional sprite consistency

Possible approaches:
- specialized sprite generator
- 3D source
- manual correction
```

나쁜 형태:

```text
모든 directional sprite = Tool X
```

제품은 바뀔 수 있다.

---

## 79. Learning은 Tool Roles를 갱신할 수 있다

새로운 도구가 등장하면
Studio의 capability 이해가 넓어질 수 있다.

하지만 Art Studio 철학은 유지된다.

```text
문제
↓
capability
↓
tool
```

순서는 바뀌지 않는다.

---

## 80. Learning은 Workflow를 개선할 수 있다

반복 경험을 통해
Generation Workflow의 실전 방법이 개선될 수 있다.

예:

```text
batch 전 sample runtime test
```

가 여러 프로젝트에서 유용했다면
공통 workflow pattern으로 남길 수 있다.

---

## 81. Learning은 Validation을 개선할 수 있다

반복되는 technical bug는
새 validator로 연결될 수 있다.

예:

```text
sprite baseline drift 반복
↓
baseline checker 개발
```

---

## 82. Learning은 Handoff를 개선할 수 있다

예:

```text
Web export에서 alpha issue 반복
↓
export helper 개선
```

---

## 83. Learning은 Art Direction을 자동 수정하지 않는다

공통 기술 경험이 생겼다고
현재 프로젝트의 Art Direction을 바꾸지 않는다.

예:

```text
Tool X가 low-detail style에 강함
```

이라고 해서
프로젝트 디자인을 low-detail로 바꾸지 않는다.

---

## 84. 자동화 편의 때문에 스타일을 바꾸지 않는다

예:

```text
이 형태는 자동 생성하기 어려움
```

을 이유로:

```text
형태를 단순하게 바꿈
```

이 자동 결정이 되어서는 안 된다.

필요하면 다른 제작 방법을 찾거나
디렉터에게 trade-off를 설명한다.

---

## 85. Learning의 실패 패턴

다음은 잘못된 Learning이다.

```text
한 번 성공
→ Studio 표준
```

```text
한 번 실패
→ Tool 금지
```

```text
한 게임에서 승인
→ 다른 게임 기본 스타일
```

```text
Validator가 편함
→ 디자인을 validator에 맞춤
```

```text
자동화 어려움
→ 디자인 단순화
```

---

## 86. 좋은 Learning의 형태

예:

```text
Observation:
작은 sprite에서는
high-frequency texture가 실제 runtime에서 사라짐.

Reusable technique:
source preview와 함께
actual display scale preview를 생성한다.

Project-specific decision:
Game A에서는 texture density를 낮춘다.
```

이렇게:

```text
관찰
↓
범용 기법
↓
프로젝트별 결정
```

을 구분하면 좋다.

---

## 87. Knowledge Promotion

공통 지식으로 승격하는 흐름은 개념적으로 다음과 같다.

```text
PROJECT EXPERIENCE
↓
OBSERVATION
↓
REPEATED VALUE?
↓
STYLE-INDEPENDENT?
↓
GENERALIZE
↓
STUDIO KNOWLEDGE
```

이것을 자동 workflow engine으로 구현할 필요는 없다.

---

## 88. Knowledge Demotion

과거에 공통화한 방법이
더 이상 유용하지 않을 수 있다.

예:

- tool obsolete
- API removed
- engine changed
- better method exists

이 경우 deprecated 또는 archive할 수 있다.

공통 지식도 영구 불변이 아니다.

---

## 89. Deprecated Knowledge

예:

```text
Deprecated:
old FLUX endpoint integration

Reason:
API removed
```

정도로 남길 수 있다.

완전히 삭제할지 보존할지는 필요에 따라 결정한다.

---

## 90. 실험 결과와 공식 공통 지식을 구분한다

Studio에서 새로운 방법을 실험할 수 있다.

예:

```text
Experiment:
new pixel generator
```

한 번의 실험 결과를 바로 공식 workflow로 만들지 않는다.

---

## 91. Sandbox Knowledge

실험 단계의 자료는
project-local 또는 temporary/shared experiment 형태로 둘 수 있다.

반복 가치가 확인되면 공통화한다.

---

## 92. Learning 문서를 거대한 위키로 만들지 않는다

Art Studio가 모든 정보를 한 곳에 모으는 거대한 knowledge base가 될 필요는 없다.

실제 작업에 필요한 정도로:

- tools
- workflows
- exporters
- shared notes

에 분산할 수 있다.

---

## 93. 중복 지식 정리

같은 방법이 여러 곳에 복사되면
공통 문서나 tool로 합칠 수 있다.

하지만 문서 정리 자체가 목적이 되지 않는다.

---

## 94. 검색 가능성

공통 지식은 나중 Claude가 찾을 수 있어야 한다.

따라서 이름과 위치를 너무 임의적으로 만들지 않는다.

예:

```text
tile-seam-check
sprite-contact-sheet
unity-pixel-import
```

처럼 문제 중심 이름이 유용할 수 있다.

---

## 95. Tool 이름보다 문제 이름을 우선할 수 있다

예:

```text
directional-sprite-workflow
```

는 특정 제품이 바뀌어도 유지될 수 있다.

반면:

```text
tool-x-workflow
```

는 도구 교체 시 의미가 약해질 수 있다.

Tool-specific 내용이 중요하면 별도 문서로 둔다.

---

## 96. Reuse할 때 현재 프로젝트를 다시 확인한다

공통 기법을 재사용하더라도
새 프로젝트의:

- Project Brief
- Art Direction
- Style Spec
- platform
- engine
- camera

를 먼저 본다.

같은 기술도 적용 방식이 달라질 수 있다.

---

## 97. Reuse는 복사가 아니라 적용이다

좋은 재사용:

```text
common tile seam checker
+
Game B tile size
```

나쁜 재사용:

```text
Game A tile pipeline 전체를
Game B에 그대로 복사
```

새 프로젝트 조건에 맞게 조정한다.

---

## 98. Template Reuse

템플릿은 구조를 재사용한다.

예:

- PROJECT_BRIEF
- ART_DIRECTION
- STYLE_SPEC
- ASSET_MANIFEST
- ASSET_BRIEF
- REVIEW_LOG

내용은 프로젝트마다 새로 채운다.

---

## 99. Template의 예시가 스타일을 오염시키지 않게 한다

템플릿에 특정 게임 예시를 과도하게 넣지 않는다.

예시가 기본값처럼 남을 수 있기 때문이다.

---

## 100. Cross-project Learning의 대표 예

### 예 1 — Tile

Game A:

```text
tile seam 문제 반복
```

Game B:

```text
같은 문제 발생
```

Studio Learning:

```text
tile repeat preview generator 공통화
```

공통화하지 않는 것:

```text
Game A tile palette
```

---

### 예 2 — Character

Game A:

```text
작은 화면에서 무기 식별 어려움
```

Game C:

```text
비슷한 문제
```

Studio Learning:

```text
actual display scale comparison을
character review technique로 사용
```

공통화하지 않는 것:

```text
무기는 항상 크게 만든다.
```

---

### 예 3 — Engine

여러 프로젝트:

```text
pixel sprite filtering 오류 반복
```

Studio Learning:

```text
pixel import validation helper
```

공통화하지 않는 것:

```text
모든 프로젝트 filtering = nearest
```

---

## 101. Project-specific Learning의 대표 예

예:

```text
Game A:
캐릭터가 화면에서 작기 때문에
머리와 무기를 크게 한다.
```

이것은 Game A의 Art Direction 또는 Style Spec에 남긴다.

Studio에는:

```text
작은 화면 캐릭터에서
실루엣 비율을 runtime scale로 검증한다.
```

같은 기법만 남길 수 있다.

---

## 102. Review Decision과 Studio Learning을 분리한다

예:

```text
Director:
B 승인.
```

이것은 Review Log.

```text
B가 승인된 이유:
작은 화면에서 실루엣이 가장 명확.
```

이것은 프로젝트 아트 지식.

```text
작은 화면 비교 시
actual-size contact sheet가 유용.
```

이것은 Studio technique.

---

## 103. 여러 층의 기록이 동시에 존재할 수 있다

하나의 작업에서:

```text
Review Log
Project Art Direction
Style Spec
Studio Workflow
Tool Note
```

가 각각 다른 내용을 가져갈 수 있다.

모든 것을 한 문서에 넣지 않는다.

---

## 104. 자동 Learning System을 만들지 않는다

예:

```text
모든 review text 분석
↓
AI가 규칙 추출
↓
자동 Studio rule 등록
```

같은 시스템을 기본 목표로 하지 않는다.

Claude가 후보를 제안할 수는 있지만
공통 규칙 승격은 신중하게 한다.

---

## 105. 통계적 학습을 사용할 수 있다

대규모 production에서는:

- repeated failure count
- validation warning frequency
- export error frequency

같은 데이터를 볼 수 있다.

하지만 모든 프로젝트에 analytics system을 구축하지 않는다.

---

## 106. Data보다 관찰이 중요한 경우

예:

```text
평균 palette count가 증가
```

보다:

```text
runtime에서 캐릭터 detail이 흐려짐
```

이 더 중요한 정보일 수 있다.

숫자만으로 Learning을 결정하지 않는다.

---

## 107. Production Bottleneck Learning

반복적으로 사람이 시간을 많이 쓰는 구간을 찾을 수 있다.

예:

- background removal
- naming
- export
- screenshot
- review sheet

이 중 기계적인 부분은 자동화 후보가 된다.

---

## 108. 미적 판단을 Bottleneck으로 보고 제거하지 않는다

예:

```text
Director review가 시간이 걸림
```

을 이유로:

```text
AI auto-approval 도입
```

을 기본 해결책으로 만들지 않는다.

중요한 미적 판단은 가치 있는 시간일 수 있다.

대신 비교 자료를 더 잘 만들 수 있다.

---

## 109. Director Efficiency Learning

예:

```text
세 후보를 같은 배경/크기로 보여주면
선택이 빨라짐.
```

이것은 좋은 Studio workflow knowledge다.

사람을 제거하지 않고 판단을 쉽게 한다.

---

## 110. 학습의 최종 목적

Learning의 목적은 문서를 많이 만드는 것이 아니다.

목적은:

- 같은 기술 실수를 반복하지 않기
- 반복 작업을 줄이기
- 새 프로젝트 시작 속도 높이기
- 도구 선택을 더 잘하기
- runtime 문제 해결을 빠르게 하기
- 디렉터가 미적 판단에 집중하게 하기

이다.

---

## 111. Reuse의 최종 목적

Reuse의 목적은 모든 게임을 같은 방식으로 만드는 것이 아니다.

오히려:

> **다른 게임을 더 잘 다르게 만들기 위해 공통 기술을 재사용한다.**

Studio가 기술적 기반을 갖고 있기 때문에
새 게임의 고유 스타일에 더 집중할 수 있어야 한다.

---

## 112. Learning이 잘 되고 있는 상태

Art Studio가 성숙하면:

- 새 게임에서 기본 검사기를 다시 만들지 않는다.
- exporter를 반복해서 새로 만들지 않는다.
- 같은 engine 문제를 매번 처음부터 찾지 않는다.
- 비교 자료를 빠르게 만든다.
- 새로운 도구를 capability 관점에서 평가한다.
- 프로젝트 스타일은 서로 섞이지 않는다.

이 상태가 이상적이다.

---

## 113. Learning이 잘못된 상태

다음은 경고 신호다.

- 모든 게임이 비슷한 palette를 사용
- 같은 캐릭터 비율이 반복
- 한 tool이 모든 작업의 기본값
- 이전 프로젝트 prompt를 자동 복사
- validator 규칙이 디자인을 결정
- 과거 workflow가 새로운 게임을 제약
- 공통 문서가 특정 게임 reference로 가득함

이 경우 스타일 전염이나 과도한 표준화가 일어나고 있을 수 있다.

---

## 114. Studio Identity와 Learning

Art Studio는 특정 화풍 전문 스튜디오가 아니다.

Learning은 이 정체성을 강화해야 한다.

즉:

```text
한 스타일을 더 잘 복제하는 능력
```

보다:

```text
서로 다른 스타일의 문제를 구분하고
각각에 맞는 방법을 선택하는 능력
```

을 키워야 한다.

---

## 115. Director Relationship과 Learning

Claude의 과거 판단이
프로젝트 권위가 되지 않도록 한다.

예:

```text
예전에 내가 이 방식이 좋다고 했으므로
이번에도 이 방식이다.
```

라고 하지 않는다.

최신 디렉터 결정과 현재 프로젝트 문맥이 우선이다.

---

## 116. Project Structure와 Learning

기본 구분:

```text
studio/
= 공통 기술

projects/
= 게임별 정체성
```

Learning & Reuse는 이 구조 원칙을 실제 지식 축적에 적용한다.

---

## 117. Art Direction System과 Learning

Art Direction에서 반복되는 시각 축 분석 방법은 공통화할 수 있다.

하지만:

- 실제 팔레트
- 실제 형태 언어
- 실제 조명 방향

은 프로젝트에 남긴다.

---

## 118. Tool Roles와 Learning

Tool 경험은 capability map을 더 정교하게 만든다.

하지만 특정 tool을 영구 표준으로 만들지 않는다.

---

## 119. Asset Lifecycle과 Learning

Rejected, Approved, Superseded 결과는
학습 source가 될 수 있다.

하지만 Lifecycle 상태 자체가
자동 학습 규칙을 의미하지 않는다.

---

## 120. Generation Workflow와 Learning

반복적으로 유용한 제작 루틴은
Studio workflow로 승격할 수 있다.

예:

```text
sample
→ runtime test
→ batch
```

---

## 121. Review & Approval과 Learning

Review 결과 중
장기적으로 의미 있는 결정만 프로젝트 지식에 남긴다.

그중 범용적인 제작 방법만 Studio knowledge 후보가 된다.

---

## 122. Asset Spec & Validation과 Learning

공통 validator는 재사용성이 높다.

실제 규격 값은 프로젝트별이다.

---

## 123. Engine Handoff와 Learning

반복되는 export/import/runtime 문제 해결법은
Studio knowledge로 발전할 수 있다.

프로젝트 고유 material/shader/style은 프로젝트에 남긴다.

---

## 124. 후속 Template과 Learning

### STYLE_SPEC

프로젝트별 기술 스타일 규칙을 보존한다.

### ASSET_MANIFEST

현재 production 상태를 관리한다.

### ASSET_BRIEF

개별 자산 요구를 전달한다.

### REVIEW_LOG

중요한 디렉터 결정을 보존한다.

이 문서는 그 자료에서 무엇을 Studio 공통 지식으로 승격할지의 원칙을 제공한다.

---

## 125. 이 문서에서 다루지 않는 것

다음은 다른 문서의 역할이다.

### 프로젝트별 실제 Art Direction

`ART_DIRECTION.md`

### 프로젝트별 Style Rule

`STYLE_SPEC.md`

### 개별 자산 상태

`ASSET_MANIFEST.md`

### 개별 제작 요구

`ASSET_BRIEF.md`

### 중요한 승인/반려 기록

`REVIEW_LOG.md`

### 구체적인 Tool 사용 매뉴얼

별도 tool guide

### Validator 구현

`studio/tools/`

### Exporter 구현

`studio/exporters/`

이 문서는 **지식을 어디에 남기고 언제 재사용할 것인지에 대한 상위 원칙**에 집중한다.

---

## 126. 핵심 원칙 요약

Art Studio의 Learning & Reuse는
모든 프로젝트를 같은 방식으로 만드는 표준화 시스템이 아니다.

핵심 원칙은 다음과 같다.

> **기법은 학습하지만 스타일은 전염시키지 않는다.**

> **프로젝트의 화풍, 팔레트, 캐릭터 비율, 세계관, 승인된 미적 결정은 기본적으로 프로젝트 안에 남긴다.**

> **Validator, exporter, tool integration, review method, runtime validation technique처럼 스타일과 독립적인 능력은 재사용할 수 있다.**

> **한 번의 성공을 Studio 표준으로 만들지 않는다.**

> **한 번의 실패를 Tool의 영구적인 한계로 일반화하지 않는다.**

> **공통화는 실제 반복과 범용성이 확인된 뒤 수행한다.**

> **Project-local 방법이 반복되면 일반화하여 Studio tool이나 workflow로 승격할 수 있다.**

> **공통화할 때 프로젝트 고유 값을 parameter나 project config로 분리한다.**

> **도구 경험은 조건과 버전을 함께 기억하며 영구 진리로 만들지 않는다.**

> **Rejected와 Approved 결과 모두 학습 source가 될 수 있지만, 개별 미적 판단은 자동으로 다른 게임에 적용하지 않는다.**

> **Runtime에서 얻은 경험도 중요한 Studio knowledge가 될 수 있다.**

> **자동화가 어렵다는 이유로 디자인을 단순화하지 않는다.**

> **과거 Claude의 판단이나 기존 workflow가 새로운 프로젝트의 디렉팅 권한보다 위에 서지 않는다.**

> **재사용의 목적은 모든 게임을 같게 만드는 것이 아니라, 공통 기술을 바탕으로 각 게임의 고유한 시각적 정체성을 더 잘 구현하는 것이다.**

> **좋은 Learning은 문서의 양이 아니라 같은 실수를 줄이고 새로운 게임에서 더 빠르게 올바른 제작 방법을 선택할 수 있게 만드는 데 있다.**
