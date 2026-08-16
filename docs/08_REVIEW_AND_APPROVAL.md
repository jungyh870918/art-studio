# 08_REVIEW_AND_APPROVAL

## 1. 문서의 역할

이 문서는 제작된 Concept, Candidate, Approved source, Export 결과를 **어떻게 검토하고 어떤 판단을 누구의 권한으로 확정하는지** 정의한다.

이 문서는 Art Direction을 다시 정의하지 않는다. Asset Lifecycle의 상태 의미를 다시 설명하지 않고, 기술 규격의 수치나 validator 구현도 정의하지 않으며, 특정 생성 도구의 품질을 평가하는 매뉴얼도 아니다.

핵심 질문은 하나다.

> **무엇을 기계가 검사할 수 있고, 무엇을 Claude가 분석·의견으로 제시하며, 무엇을 디렉터가 최종적으로 승인하는가?**

Review의 목적은 사람을 제거하는 것이 아니다. **기술적 사실과 미적 판단을 분리하고 결과를 비교 가능한 상태로 만들어, 디렉터가 더 적은 혼란으로 더 나은 판단을 내리게 하는 것**이다.

---

## 2. 가장 중요한 구분

```text
TECHNICAL REVIEW
≠
ART REVIEW
```

**Technical Review** — 측정하거나 확인할 수 있는 기술 문제.

> dimensions · aspect ratio · alpha · format · file existence · naming · palette constraint · frame count · tile seam · pivot · padding · texture size · export compatibility · engine constraint

**Art Review** — 게임의 시각적 목표와 실제 화면 경험을 기준으로 하는 판단.

> 매력 · 분위기 · 캐릭터성 · 세계관 적합성 · 형태 언어 · 실루엣 · 가독성 · 시각적 우선순위 · 기존 승인 자산과의 일관성 · 최종 채택 여부

둘은 연결될 수 있지만 동일하지 않다. 그래서 두 방향의 혼동을 모두 막는다.

### 기술적으로 정상이라고 좋은 아트는 아니다

dimensions · alpha · format · palette · naming이 모두 pass여도 캐릭터가 매력적이지 않을 수 있고, 배경에서 읽히지 않을 수 있고, 세계관에 맞지 않을 수 있고, 주인공처럼 보이지 않을 수 있고, 형태 언어가 기존 자산과 충돌할 수 있다.

> **Technical Pass는 "현재 정의된 기술 규격을 만족한다"는 의미만 가진다.**
> 디자인이 좋다는 뜻도, Art Direction과 맞는다는 뜻도, 디렉터가 승인했다는 뜻도, 실제 게임 화면에서 잘 보인다는 뜻도, 공식 자산이라는 뜻도 아니다.

```text
TECH PASS
≠
DIRECTOR APPROVAL
```

### 미적 의견을 기술적 사실처럼 말하지 않는다

반대 방향도 마찬가지다. Claude나 비전 모델의 미적 판단을 객관적 수치처럼 말하지 않는다.

```text
기술적 사실:  sprite height = 96px / project target = 64px
미적 의견:    머리 비율이 조금 커지면 작은 화면에서 캐릭터성이 더 잘 읽힐 가능성이 있다.

기술적 사실:  배경 평균 luminance와 캐릭터 평균 luminance 차이가 작다.
미적 의견:    현재 장면은 캐릭터가 배경에 다소 묻혀 보인다.
```

둘을 함께 사용할 수는 있다. **의미를 섞지 않는다.**

---

## 3. Review의 흐름과 깊이

```text
Candidate 준비 → 필요한 Technical Review → 비교 자료 정리 →
Art Review → Director Decision → Approved / Revision / Rejected / On Hold
```

**모든 자산에서 같은 깊이로 수행하지 않는다.**

```text
낮은 중요도 / 반복 자산    기술 검사 중심 · 빠른 시각 확인 · 기존 family rule 적용
                        Candidate → 간단한 기술 확인 → Director 확인 → Approved

중간 중요도               Art Direction 일관성 · gameplay readability · 필요 시 비교

높은 중요도 / 대표 자산    Concept Review → Candidate Review → Technical Review →
                        Runtime Screenshot → Art Review → Revision → Final Review → Approved
                        (여러 Candidate · runtime validation · Review Log 기록)
```

> **모든 자산을 대표 캐릭터처럼 다루지 않는다.**

---

## 4. 단계마다 묻는 질문이 다르다

**Concept Review** — *이 방향을 더 발전시킬 가치가 있는가?*
형태 방향 · 인상 · 실루엣 · 비율 · 분위기 · 색 방향 · Reference와의 관계를 본다. 최종 파일 규격은 중요하지 않을 수 있다.

**Candidate Review** — *이 결과를 실제 자산으로 채택할 수 있는가?*
Art Direction 적합성 · Asset 요구 충족 · 기존 승인 자산과의 일관성 · 플레이 가독성 · 주요 기술 제약 · 디렉터가 비교해야 하는 차이를 본다.

**Approved Source Review** — *이 결과를 현재 공식 source로 사용할 수 있는가?*
채택 의도 · 중요한 수정의 완료 여부 · 기술적 오류 · source로 보존할 가치를 본다.

**Export / Runtime Review** — *실제 게임에서 의도한 대로 보이는가?*
scale · camera · lighting · shader · material · compression · filtering · animation · VFX · environment interaction · UI 관계 · gameplay readability를 본다.

---

## 5. Technical Review

가능한 한 명확하고 재현 가능한 검사를 다룬다.

```text
파일      존재 여부 · format · extension · corruption
이미지    width/height · aspect ratio · alpha · color mode · padding ·
         transparent edge · palette count
Sprite   frame count · frame dimensions · alignment · pivot · spacing · animation consistency
Tile     tile dimensions · edge seam · repeat result · border consistency
Texture  dimensions · compression requirement · channel · normal/mask 구조 · mipmap 적합성
Export   target engine format · 경로 · import 호환성 · 누락된 파생 파일
```

구체적인 검증 항목과 자동화 방식은 `09_ASSET_SPEC_AND_VALIDATION.md`가 정의한다.

**가능한 곳에서는 자동화한다.** 자동화의 장점은 속도만이 아니다. 반복 실수 감소 · 대량 작업 처리 · 재현 가능성 · 결과 비교 · **사람의 주의력을 미적 판단에 집중시키는 것**이 함께 온다. 다만 자동화 자체가 Review의 목적은 아니다.

결과는 간단하게 표현한다.

```text
Technical Review
PASS     dimensions · alpha · format
WARNING  palette 34 colors / target 32
FAIL     frame 7 missing
```

**모든 프로젝트에 같은 output format을 강제하지 않는다.** 중요한 것은 무엇이 문제인지 빠르게 알 수 있는 것이다.

---

## 6. Art Review

> **이 결과가 이 게임에서 시각적으로 적절한가?**

프로젝트에 따라 첫인상 · 정서 · 형태 언어 · 실루엣 · 비율 · 캐릭터성 · 환경 분위기 · 색 · 명암 · 질감 · 조명 · 시각적 우선순위 · gameplay readability · 캐릭터와 배경의 관계 · UI와 world의 관계 · animation feel · VFX 강도 · world consistency · 기존 Approved와의 관계를 본다.

**모든 항목을 매번 체크하지 않는다. 현재 자산에서 중요한 항목만 본다.**

### 판단의 기준이 되는 것

- **Art Direction과의 일관성** — Direction Summary와 맞는가 · 핵심 시각 키워드가 보이는가 · 금지사항을 위반하지 않는가 · 형태 언어가 맞는가 · 캐릭터/배경 관계가 맞는가 · 가독성 우선순위를 해치지 않는가 · **탐색 중인 방향을 확정 규칙처럼 사용하지 않았는가**.
  Art Direction은 기준이지만 새로운 시도가 기존 문장과 100% 동일해야 한다는 뜻은 아니다. 디렉터가 더 나은 방향을 채택하면 Art Direction이 발전할 수 있다.
- **Asset Brief와의 적합성** — 역할 · 게임 기능 · 반드시 들어갈 요소 · 피해야 할 요소 · variant · 기술 제약 · 현재 요청. **좋은 그림이라도 Brief의 핵심 기능을 충족하지 못하면 그 자산으로는 적합하지 않을 수 있다.**
- **플레이 가독성** — 적/아군 구분 · 직업 구분 · 무기 식별 · 상호작용 오브젝트 · 위험 요소 · 아이템 중요도 · 이동 경로 · 팀 색 · 보스 약점. 이 정보가 실제 플레이에서 읽히지 않으면 **개별 이미지가 아름다워도 게임 아트로는 실패할 수 있다.**

가독성과 미적 방향이 충돌할 수 있다.

```text
목표: 어두운 공포 분위기
문제: 적이 너무 안 보임
```

단순히 밝게 만드는 것만이 답은 아니다. silhouette contrast · rim light · movement cue · local highlight · material difference · background suppression 같은 선택지가 있다. **Art Review는 미적 방향을 버리지 않으면서 기능적 요구를 해결하는 방법을 찾는다.**

### 참고할 수 있는 질문

필요할 때 일부만 사용한다. **체크리스트로 쓰지 않는다.**

```text
목적    이 자산의 역할이 즉시 이해되는가 · 플레이에 필요한 정보를 전달하는가
형태    실루엣이 읽히는가 · 비율이 방향과 맞는가 · 다른 자산과 구분되는가
캐릭터성 주인공/보스/NPC의 역할이 느껴지는가 · 너무 평범하거나 과장되지 않았는가
환경    플레이 경로를 방해하지 않는가 · 랜드마크가 읽히는가 · 반복감이 지나치지 않은가
색·명암  시각적 우선순위가 맞는가 · 배경과 대상이 분리되는가 · 강조색이 남발되지 않는가
질감    재질이 의도대로 읽히는가 · texture가 형태를 방해하지 않는가
조명    asset lighting과 engine lighting이 충돌하지 않는가 · 중요한 형태가 죽지 않는가
일관성   기존 Approved와 같은 게임처럼 보이는가 · 그렇다고 복제처럼 보이지는 않는가
```

---

## 7. Claude의 역할과 권한

**최종 미적 승인 권한은 게임 디렉터에게 있다.**

Claude는 후보 비교 · Art Direction과의 일관성 분석 · Reference와의 관계 설명 · 기존 승인 자산과의 차이 설명 · 가독성 위험 지적 · 문제 후보 표시 · 추천안 제시 · 수정 방향 제안을 할 수 있다.

```text
"B가 현재 Art Direction과 가장 일관성이 높아 보인다."
≠
B = Approved
```

동시에 **Claude가 침묵하는 시스템이 되어서도 안 된다.** "어느 것이 좋은지 선택해 주세요"만 반복하지 않고 구체적으로 의견을 낸다.

```text
A  얼굴은 가장 강함 / 무기 실루엣이 작음 / 현재 기준 자산보다 장식 밀도가 높음
B  실루엣이 가장 명확함 / 작은 화면 가독성이 좋을 가능성 / 현재 방향과 가장 일관됨
C  개성은 강함 / 다른 일반 캐릭터와 형태 언어 차이가 큼
```

필요하면 "현재 기준에서는 B를 우선 추천한다"고 말할 수 있다. **최종 채택은 디렉터가 한다.**

**추천에는 근거를 붙인다.**

```text
좋은 예:   B를 추천한다. 현재 승인 캐릭터들과 비슷한 정보 밀도를 유지하면서도
          무기 실루엣이 더 잘 읽힌다.
좋지 않은 예: B가 더 좋아 보인다. / AI 점수상 B가 최상이다.
```

**확실하지 않으면 확실하지 않다고 말한다.**

> C가 더 개성 있어 보이지만, 실제 게임 크기에서는 복잡도가 과할 가능성이 있다. Runtime test가 필요하다.

**충돌하는 장점을 하나의 순위로 압축하지 않는다.**

```text
A  가독성은 가장 좋음 / 개성은 가장 약함
B  개성은 가장 강함 / 배경에서 묻힐 위험 있음
```

랭킹을 강제하지 않고 trade-off를 보여준다. 디렉터가 무엇을 우선할지 결정할 수 있어야 한다.

**점수표를 만들지 않는다.** `Style Match: 8.3 / Readability: 7.4 / Appeal: 9.1` 같은 scoring system은 숫자가 실제 판단보다 정교해 보이는 착시를 만든다. 일부 측정 지표를 쓸 수는 있지만 최종 Art Review는 **의미 있는 설명과 비교**를 중심으로 한다.

**비전 분석과 코드 분석은 함께 쓸 수 있다.**

```text
비전 분석:  배경과 캐릭터가 비슷한 밝기로 보여 분리가 약해 보임.
코드 분석:  캐릭터와 주변 배경의 평균 luminance 차이가 작음.
```

두 정보가 함께 있으면 문제를 더 구체적으로 설명할 수 있다. 다만 **비전 분석을 최종 미적 권위로 취급하지 않고, 측정 수치 하나로 디자인 판단을 대신하지도 않는다.**

Art Review 결과의 표현도 장황한 평론일 필요가 없다.

```text
강점  실루엣이 가장 잘 읽힘 · 기존 기사 계열과 일관성 좋음
주의  방패 디테일이 작은 화면에서 사라짐
추천  B를 기준으로 방패 형태만 단순화
```

---

## 8. 후보를 제시하는 방식

### 차이를 잘 보이게 한다

가능하면 비교 조건을 정리한다 — 같은 표시 크기 · 배경 · 포즈 · 카메라 · 조명 · crop · UI frame. 필요하면 contact sheet나 review sheet를 만든다.

> **목적은 결과를 예쁘게 전시하는 것이 아니라 차이를 판단하기 쉽게 만드는 것이다.**

다만 **모든 후보를 같은 조건으로 만들 필요는 없다.** 서로 다른 방향을 탐색하는 Concept 단계에서 조건을 모두 통일하면 오히려 방향 차이가 줄어든다. 반대로 최종 색상 후보를 비교할 때는 형태·포즈·카메라를 고정하는 편이 유용하다.

> **비교 조건은 무엇을 판단하려는가에 따라 정한다.**

### 후보가 너무 비슷해도, 너무 달라도 Review가 실패한다

A/B/C가 사실상 같은 결과라면 디렉터가 선택할 정보가 없다. Concept이나 초기 Candidate에서는 proportion · silhouette · equipment · density · color hierarchy · material · lighting responsibility 중 **무엇을 탐색하는지 분명히** 한다.

반대로 한 번에 얼굴·포즈·조명·색·무기가 모두 다르면 무엇 때문에 더 좋은지 원인을 알 수 없다. 최종 비교에서는 판단 축을 통제하는 편이 낫다.

### 디렉터에게 보여주는 것을 최소화한다

모든 raw generation · 실패한 intermediate · script log · API response · mask · debug image · temporary export · console output을 보여줄 필요는 없다.

```text
Candidate A / B / C
차이: silhouette · equipment size · detail density
```

기술 문제는 필요한 경우 요약한다.

### 반대로 숨기면 안 되는 것

비교 조건이 공정하지 않은 경우는 알린다.

- B만 다른 generator로 만들어 표현 특성이 다름
- C는 technical constraint를 아직 만족하지 않음
- A는 현재 엔진에서 shader 문제로 실제 색이 다르게 보임
- runtime screenshot에서 B만 scale이 잘못 적용됨
- Reference 조건이 후보마다 크게 다름

### 비교용 가공은 원본이 아니다

배경 통일 · 크기 통일 · label 추가 · crop · contact sheet는 Review material이다. **이 결과를 Approved source 자체와 혼동하지 않는다.**

Review 자료(contact sheet · side-by-side · overlay · game screenshot · before/after · zoomed detail · grayscale 비교 · silhouette 비교 · animation clip · HTML review page)는 **디렉터가 판단하기 쉬워지는 경우에만** 만든다.

---

## 9. 디렉터의 피드백과 승인

### 짧은 피드백도 유효한 Review 결과다

> "2번." · "B가 제일 낫다." · "얼굴은 A, 몸은 C." · "무기만 줄여." · "너무 깨끗하다." · "이건 아니다." · "배경에 묻힌다." · "조금 더 어두워." · "보스 같지가 않다."

**Claude는 전문 용어로 다시 말해 달라고 요구하지 않는다.** 현재 Art Direction과 자산 문맥을 기준으로 수정 가능한 작업으로 변환한다.

### 승인으로 볼 수 있는 표현

**채택 의도가 명확한 표현**을 Approved decision으로 본다.

```text
승인으로 본다      "2번으로 확정" · "B 채택" · "이걸 공식으로 쓰자" ·
                 "이 버전을 기준으로 간다" · Review Log나 Manifest에 Approved로 기록

단순 선호일 수 있다  "괜찮다" · "이게 낫다" · "이 방향이 좋네" ·
                 "일단 이걸로 보자" · "게임에 넣어봐"
```

모호한 표현 하나 때문에 모든 작업을 중단할 필요는 없다. 다만 **공식 Approved 상태로 바꾸는 것이 중요한 경우에는 채택 의도가 충분히 명확한지 확인한다.**

### 승인이 전부를 승인한 것은 아닐 수 있다

```text
실루엣 승인 / 색상 탐색 계속       캐릭터 디자인 승인 / animation 미승인
원본 일러스트 승인 / engine crop 미정   보스 형태 승인 / 재질 표현 수정 필요
```

필요하면 승인 범위를 짧게 기록한다. **모든 자산을 복잡한 partial approval schema로 관리하지 않는다.**

---

## 10. Review 결과의 종류

```text
Approved              현재 공식 자산 또는 공식 방향으로 채택
Revision              기본 방향은 유지하되 수정 필요
Rejected              현재 방향에서 채택하지 않음
On Hold               판단을 보류
Needs Technical Fix   미적 판단과 별개로 기술 문제 수정 필요
```

**이 표현을 공식 상태 enum으로 강제하지 않는다.** 상황을 명확하게 설명하기 위한 용어다. Lifecycle 상태 의미 자체는 `06_ASSET_LIFECYCLE.md`를 따른다.

### Revision과 Rejection을 구분한다

```text
"얼굴은 좋고 무기만 줄여."          → Revision. 기존 Candidate의 대부분을 보존할 수 있다.
"이 방향은 아니다. 너무 사실적이다."  → Rejection. 다른 Concept이나 제작 방식으로 돌아갈 수 있다.
```

이 구분은 이후 작업 비용과 방향을 결정한다.

### 반려 이유는 중요한 정보다

> 너무 사실적 · 너무 귀여움 · 무기 과장 과다 · 배경 detail 과다 · 얼굴이 어려 보임 · UI처럼 보임 · 시대감 부족 · AI 특유의 의미 없는 디테일 · 기존 캐릭터와 너무 유사

Rejected는 단순 실패가 아니라 아직 문서화되지 않은 기준의 노출이다. 다만 **한 번의 반려 이유를 자동으로 프로젝트 전체 Art Direction으로 승격하지 않는다.** 반복되거나 명시적으로 확정될 때 장기 규칙이 된다.

---

## 11. 실제 게임 화면을 Review input으로 사용한다

게임 아트는 개별 PNG만으로 판단되지 않는다. 필요하면 실제 게임 screenshot · gameplay capture · scene view · camera view · UI가 포함된 화면 · VFX 포함 장면 · animation playback · 모바일 화면 · 여러 캐릭터가 함께 있는 장면을 사용한다.

runtime review가 특히 중요한 자산 — 플레이어 캐릭터 · 적 · tile · UI icon · VFX · 조명 영향을 크게 받는 자산 · environment · Roblox asset.

**실제 플레이 조건을 존중한다.** 게임에서 80px로 보이는 캐릭터를 800px 확대 이미지만으로 검토하면 잘못된 판단을 하게 된다. typical camera distance · on-screen size · 모바일 화면 · 빠른 움직임 · multiplayer density · 야간 조명 · 일반적인 배경 · UI overlap을 확인한다.

중요한 자산에서는 **관점을 여러 번 바꿔서** 본다.

```text
단독 이미지     형태와 디자인
작은 표시 크기   실루엣과 정보 밀도
실제 배경       가독성
게임 UI 포함    시각적 우선순위
Animation      움직임에서 형태 유지
VFX 포함        전투 중 식별 가능성
```

### Runtime Review에서는 문제 위치를 분리한다

> "캐릭터가 배경에 묻힌다."

```text
Character Asset  value contrast 부족 · silhouette 약함 · detail 분포 문제 · outline 약함
Environment      edge density 과다 · saturation 과다 · contrast 과다 · 주변 detail 과다
Engine           lighting · post-processing · shader · material · fog · bloom
Camera           distance · scale · FOV · composition
```

> **문제를 보고 바로 source asset을 다시 만들지 않는다. 먼저 문제의 위치를 분석한다.**

계층 구분의 상세는 `10_ENGINE_HANDOFF.md`가 다룬다.

### Runtime Review는 Approved를 다시 열 수 있다

Approved source라도 실제 화면에서 문제가 발견될 수 있다. 이때 Export만 수정할지 · Engine 설정을 고칠지 · Environment를 조정할지 · Source asset을 수정할지 중 적절한 지점을 선택하고, 필요하면 수정 Candidate를 만들어 다시 승인한다.

**Approved는 현재 기준이지 영구적으로 재검토 불가능한 상태가 아니다.**

---

## 12. 기존 Approved를 보호한다

새 Candidate를 볼 때 대표 캐릭터 · 대표 환경 · 승인된 icon · 기존 animation · 현재 game screenshot과 비교할 수 있다. 스타일이 성숙한 프로젝트에서는 **Reference보다 기존 Approved asset이 더 강한 기준**이 된다.

다만 "기존 것과 다르다"는 이유만으로 자동 반려하지 않는다. 새로운 결과가 더 나은 방향을 만들 수도 있다. 큰 변화라면 디렉터가 판단한다.

그리고 **Claude가 기존 승인 결과를 임의로 뒤집지 않는다.** 더 좋은 대안을 발견해도 승인 상태를 자동 변경하지 않는다.

```text
현재 Approved는 유지.
다만 새 후보 B가 작은 화면 가독성에서 더 나아 보인다. 원하면 비교할 수 있다.
```

최신 디렉터 지시가 기존 문서보다 우선할 수 있지만, 그 범위를 먼저 구분한다.

```text
기존: 캐릭터는 hard outline
현재: "이번 주인공은 outline 없이 가자."
→ individual exception인가, project-wide change인가?
```

**국소 지시를 전체 Art Direction 변경으로 자동 확대하지 않는다.**

---

## 13. 예외를 허용한다

프로젝트 규칙과 다른 자산이 존재할 수 있다 — 보스만 훨씬 큰 실루엣 · 특정 지역만 다른 색 방향 · 특별한 UI만 다른 재질 · 한 캐릭터만 outline 없음.

**예외가 의도적이고 승인되었다면 정상이다.** Validator나 Review 시스템이 모든 예외를 오류로 되돌리지 않도록 한다.

중요한 예외는 범위와 함께 남길 수 있다.

```text
Asset:     Boss A
Exception: 전체 캐릭터는 outline 사용. Boss A는 의도적으로 outline 없음.
Scope:     individual asset
```

이 기록은 예외가 전체 규칙으로 확대되는 것도, 실수로 되돌려지는 것도 막는다.

같은 이유로 **이상치 탐지와 미적 자동 평가를 구분한다.** color count 급증 · dimensions mismatch · edge density 급증 · 파일 누락 · outline width deviation · brightness 분포 이상 · frame count mismatch 같은 결과는 Review 대상을 좁히는 데 유용하다. 하지만 `이상치 = 나쁜 아트`로 자동 결론 내리지 않는다. **의도적인 예외일 수 있다.**

---

## 14. 사람을 병목으로 만들지도, 건너뛰지도 않는다

### 자율적으로 진행하는 것

resize · naming · format conversion · 이미 승인된 rule의 적용 · 명확한 export · technical fix · batch validation은 기존 규칙이 명확하면 디렉터 승인 없이 진행한다.

### 디렉터의 판단이 필요한 것

중요한 미적 방향 · 대표 자산 채택 · 여러 합리적 방향 중의 선택 · 기존 Art Direction과 충돌하는 변화 · 큰 스타일 변경 · "충분히 좋은가"의 결정.

### 자동 승인 구조를 만들지 않는다

```text
AI 생성 → AI 평가 → AI 최고점 → 자동 승인
```

이 구조를 기본으로 만들지 않는다. 특히 주인공 · 대표 캐릭터 · 보스 · 전체 스타일 기준 자산 · 주요 환경 · 핵심 UI 비주얼 · Art Direction 변경 · 중요한 runtime 문제 해결에는 사람이 개입할 가치가 높다.

### 명백한 기술 실패는 걸러도 된다

파일 깨짐 · 완전히 잘못된 dimensions · alpha 누락 · export 실패 · frame 누락 · 잘못된 asset은 Art Review 전에 수정하거나 제외할 수 있다. **이것은 기술적으로 비교 자체가 불가능한 결과를 정리하는 것이지 미적 검열이 아니다.**

### 미적 이유로 후보를 숨기지 않는다

Claude가 마음에 들지 않는다는 이유로 Candidate를 보여주지 않는 것을 기본으로 하지 않는다. 명확한 근거가 있다면 설명을 붙여 함께 제시한다.

```text
Candidate C: 현재 Art Direction의 금지사항인 glossy plastic 표현이 강함.
             그래도 비교를 위해 포함.
```

디렉터가 "Art Direction 위반 후보는 미리 제거해"라고 명시했다면 그 기준을 적용한다.

### 과도한 승인 절차를 만들지 않는다

```text
Technical Reviewer → Art Reviewer → Senior Reviewer →
Director Approval → Final Approval → Export Approval
```

이 Art Studio는 거대한 기업 승인 시스템이 아니다. **필요한 판단만 명확히 분리한다.**

---

## 15. 반복 자산과 대량 작업

asset family가 이미 확정되었다면 매 자산마다 같은 강도의 Art Review가 필요하지 않다.

```text
기사 family 기준 승인 → 기사 20종 제작
```

이 경우 proportions · palette · dimensions · naming · family rule을 자동 또는 반자동으로 확인하고, **대표 샘플과 이상치 중심으로** Art Review를 한다. 다만 반복 중 drift가 생기면 다시 깊게 검토한다.

대량 작업의 흐름.

```text
대표 샘플 제작 → Director Review → 방향 승인 → Batch →
Technical Validation → Spot Review → 이상치 수정
```

처음부터 100개를 만든 뒤 전체 방향이 틀렸음을 발견하지 않도록 한다.

**Spot Review**에서는 랜덤 샘플 · edge case · 가장 복잡한 자산 · 가장 작게 표시되는 자산 · 자동 검사 warning이 있는 자산 · 기존 Approved와 차이가 큰 자산을 우선 본다. 다만 **중요한 대표 자산은 별도로 깊게 검토한다.**

---

## 16. 기록과 승격

### Review Log에 무엇을 남기는가

**모든 Review를 기록하지 않는다.** 남길 가치가 높은 것은 대표 캐릭터 승인 · 스타일 방향 확정 · 중요한 반려 이유 · 반복 적용할 비율 결정 · 주요 금지사항 · 조명 방향 변경 · asset family 기준 결정 · runtime test로 인한 큰 수정 · 기존 Approved 교체다. 작은 수정 하나하나는 기록하지 않아도 된다. 형식은 `REVIEW_LOG.md`가 담당한다.

### Art Direction으로 승격할 때 조심한다

한 자산의 "갑옷이 너무 복잡하다"를 즉시 "모든 캐릭터 갑옷 detail을 줄인다"로 확장하지 않는다. 프로젝트 방향으로 승격할 수 있는 경우는 다음이다.

- 디렉터가 명시적으로 전체 규칙으로 결정했다
- 같은 피드백이 반복된다
- 여러 자산에서 같은 문제가 확인된다
- 실제 게임 화면에서 구조적 문제로 확인된다

### Style Spec은 Review의 자동 산출물이 아니다

"64px보다 큰 sprite에서는 현재 게임의 밀도가 과해 보인다"는 관찰을 즉시 수치로 확정하지 않는다. 추가 테스트 · 기존 자산 비교 · 디렉터 결정을 거쳐 프로젝트 규칙으로 기록한다.

승격 기준의 상세는 `11_LEARNING_AND_REUSE.md`가 다룬다.

### Review가 방향과 제작 방법을 바꿀 수 있다

```text
기존 방향:      배경 디테일 풍부
Runtime Review: 작은 캐릭터가 배경에 계속 묻힘
Director 결정:  이동 경로 주변의 detail density를 낮춘다.
```

```text
문제: 8방향 캐릭터 일관성이 계속 깨짐
판단: 현재 생성 방식의 한계
대응: 3D 기준 source 도입
```

둘 다 정상적인 운영이다. **다만 Art Direction의 변경 권한은 디렉터에게 있다.**

그리고 **Review와 도구 평가를 구분한다.** 한 Candidate가 좋지 않았다고 그 도구 전체가 나쁘다고 결론 내리지 않고, 한 번 좋은 결과가 나왔다고 그 도구를 프로젝트 표준으로 고정하지도 않는다.

---

## 17. 종료 조건과 개발 단계

Review는 끝없이 수정하기 위한 과정이 아니다. **디렉터가 현재 목적에 충분하다고 판단하면 멈춘다** — prototype에 충분 · vertical slice 기준 만족 · production asset으로 충분 · 현재 플랫폼에서 충분 · 비용 대비 추가 수정 가치가 낮음.

"완벽한 아트"라는 추상적 목표보다 **현재 게임과 제작 단계에서 충분한지**를 본다.

```text
Prototype        방향 확인 · 빠른 가독성 · 큰 문제 탐지. 완벽한 polish는 불필요할 수 있다.
Vertical Slice   대표 품질 · 핵심 스타일 일관성 · runtime result
Production       반복 일관성 · technical compliance · 효율적인 review
Polish           작은 시각 문제 · runtime interaction · consistency · final presentation
```

같은 자산이라도 개발 단계에 따라 요구 완성도가 달라진다.

또한 라이선스나 출처 문제가 채택 가능성을 바꿀 수 있다 — 라이선스 불명확 · 사용 범위 제한 · attribution 필요 · 상업적 사용 불가. **미적으로 좋아도 Approved source로 쓸 수 없을 수 있다.** 라이선스 관리 시스템 자체는 이 문서의 범위가 아니지만, 채택 가능성에 영향을 주는 문제라면 Review에서 무시하지 않는다.

---

## 18. Review에서 가장 중요한 세 가지 질문

복잡한 상황에서 방향을 잃으면 다음으로 돌아간다.

1. **기술적으로 정상인가** — 측정 가능한 요구를 만족하는가?
2. **게임 아트로서 적절한가** — Art Direction, gameplay, 실제 화면에 맞는가?
3. **누가 최종 결정을 해야 하는가** — 기술적 문제인가, Claude가 의견을 낼 영역인가, 디렉터의 미적 결정이 필요한가?

---

## 19. 다른 문서와의 관계

- **`02_DIRECTOR_RELATIONSHIP.md`** — 사람과 Claude의 권한 원칙을 정의한다. 이 문서는 그 원칙을 실제 Review 과정에 적용한다.
- **`04_ART_DIRECTION_SYSTEM.md`** — 어떤 시각적 축을 볼 수 있는지 정의한다. 이 문서는 그 축을 실제 Candidate와 game screenshot에 적용한다.
- **`06_ASSET_LIFECYCLE.md`** — Review 결과가 어떤 상태 변화로 이어지는지 정의한다.
- **`07_GENERATION_WORKFLOW.md`** — Candidate가 어떻게 준비되고 피드백이 어떻게 수정 작업으로 이어지는지 정의한다.
- **`09_ASSET_SPEC_AND_VALIDATION.md`** — Technical Review의 구체적인 검증 대상과 자동화 원칙을 정의한다.
- **`10_ENGINE_HANDOFF.md`** — Export와 Runtime Review를 위한 실제 엔진 전달 과정을 정의한다.
- **`11_LEARNING_AND_REUSE.md`** — Review에서 반복 확인된 결정과 실패 중 무엇을 장기 지식으로 남길지 정의한다.
- **`REVIEW_LOG.md`** — 중요한 Director decision과 이유를 실제 프로젝트에 기록하는 템플릿이다.

---

## 20. 이 문서에서 다루지 않는 것

```text
기술 규격 수치와 검사 구현    09_ASSET_SPEC_AND_VALIDATION.md
엔진 import / export 상세    10_ENGINE_HANDOFF.md
자산 상태 정의               06_ASSET_LIFECYCLE.md
Candidate 제작 순서          07_GENERATION_WORKFLOW.md
프로젝트별 Style Spec        STYLE_SPEC.md
Review 기록 형식             REVIEW_LOG.md
공통 학습 승격 기준           11_LEARNING_AND_REUSE.md
```

이 문서는 **검토의 의미, 판단의 경계, 승인 권한**에 집중한다.

---

## 21. 핵심 원칙 요약

Review & Approval은 AI가 아트를 자동 채점하고 승인하는 시스템이 아니다.

> **Technical Review와 Art Review를 구분한다.**

> **기술적으로 정상이라는 사실을 좋은 아트라는 판단으로 확대하지 않는다. Technical Pass ≠ Director Approval.**

> **Claude의 미적 의견을 객관적 사실처럼 말하지 않는다.**

> **Claude는 수동적으로 침묵하지 않고 적극적으로 비교·분석·추천한다.**

> **최종 미적 승인 권한은 게임 디렉터에게 있다.**

> **후보는 디렉터가 차이를 쉽게 판단할 수 있는 형태로 제시한다.**

> **Review는 실제 게임 화면, 카메라, 조명, 배경, UI, VFX를 포함할 수 있다.**

> **Runtime에서 문제가 보이면 source, export, environment, engine, camera 중 원인을 먼저 구분한다.**

> **반려 이유는 학습 정보가 될 수 있지만 자동으로 프로젝트 전체 규칙이 되지는 않는다.**

> **기존 Approved를 Claude가 임의로 뒤집지 않는다.**

> **의도적으로 승인된 예외를 오류로 되돌리지 않는다.**

> **반복 자산에는 가볍게, 대표 자산에는 필요한 만큼 깊게 Review한다.**

> **사람을 모든 작은 작업의 병목으로 만들지 않으면서도 중요한 미적 판단은 자동화로 대체하지 않는다.**

> **Review의 목적은 점수를 만드는 것이 아니라 좋은 판단을 가능하게 만드는 것이다.**
