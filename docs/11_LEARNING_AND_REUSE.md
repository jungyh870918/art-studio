# 11_LEARNING_AND_REUSE

## 1. 문서의 역할

이 문서는 여러 게임 프로젝트를 수행하며 얻은 경험 중 **무엇을 재사용 가능한 스튜디오 지식으로 축적하고, 무엇을 프로젝트 고유의 결정으로 남길지** 정의한다.

이 문서는 특정 게임의 Art Direction을 다시 설명하지 않는다. 모든 작업 기록을 지식베이스로 저장하는 문서도, 경험을 자동으로 공통 규칙으로 승격하는 시스템도, 특정 도구의 사용 매뉴얼도 아니다.

핵심 질문은 하나다.

> **이번 프로젝트에서 얻은 경험 중 무엇이 다른 프로젝트에서도 재사용할 수 있고, 무엇은 이 게임에만 남아야 하는가?**

---

## 2. 가장 중요한 원칙

```text
STUDIO KNOWLEDGE                  PROJECT KNOWLEDGE
기법 · 검증 방법 · 도구 연결법       화풍 · 팔레트 · 캐릭터 비율 · 세계관
제작 방법 · 반복 작업               디자인 언어 · 특정 게임 prompt
export 경험 · runtime 검증 경험      승인된 미적 결정 · 그 게임의 정서와 분위기
```

> **기법은 학습하지만 스타일은 전염시키지 않는다.**

그리고 Learning과 Reuse는 같은 말이 아니다.

```text
Learning   작업 경험에서 무엇을 배웠는가
Reuse      그 배움을 다른 작업이나 다른 프로젝트에서도 다시 쓸 수 있는가
```

**모든 학습이 재사용 가능한 것은 아니다.**

```text
"이 게임에서는 캐릭터 머리를 크게 해야 잘 읽힌다"
→ 프로젝트별 아트 방향. 그 게임에 남는다.

"작은 화면 캐릭터 비교에서는 실제 runtime scale contact sheet가 유용했다"
→ 다른 프로젝트에서도 재사용 가능한 제작 기법.
```

---

## 3. 기술은 공통화하고 값은 프로젝트에 남긴다

이 구분이 이 문서 전체를 관통한다.

```text
공통화할 수 있는 것            프로젝트에 남는 것
1px outline을 검사하는 코드     "outline은 항상 1px이어야 한다"
palette analyzer               "모든 게임은 24 colors"
palette count 검사 능력         "Game A palette <= 24"
tile seam checker              Game A의 tile palette
```

`game-a: outline = 1px`이라고 해서 `studio default: outline = 1px`을 만들지 않는다.

같은 원칙이 Prompt에도 적용된다. `subject / view / composition / technical constraint / negative condition` 같은 **prompt assembly 방식**은 공통 기술이 될 수 있지만, 특정 게임의 스타일 표현 · 캐릭터 디자인 · palette · reference가 들어간 prompt는 그 프로젝트에 남는다.

---

## 4. 무엇을 승격하고 무엇을 남기는가

**Studio로 승격할 수 있는 것**

```text
Validator            dimensions · alpha · palette · seam · naming · frame · missing file checker
Exporter             sprite sheet exporter · image optimizer · channel packer · engine copy helper
Workflow             contact sheet 생성 · 고정 카메라 screenshot · batch candidate 수집 ·
                     sample-before-batch
Tool Integration     API wrapper · MCP connection · 인증 메모 · 파일 전달 helper
Production 지식      3D render → 2D sprite 방식 · pixel cleanup · alpha edge cleanup ·
                     runtime 비교 기법
```

**프로젝트에 남는 것**

```text
특정 게임의 prompt · palette · 캐릭터 비율 · 세계관 reference ·
approved asset · anti-reference · visual target screenshot ·
금지 스타일 · 감정적 방향 · Art Direction · Style Spec ·
asset family rule · review decision · project-specific exporter setting
```

프로젝트 안에서의 재사용(같은 계열의 제작 방식을 다음 자산에 적용하는 것)은 당연하다. **그 재사용이 다른 게임으로 자동 전파되지 않을 뿐이다.**

---

## 5. 자동으로 일반화하지 않는다

**한 번의 성공을 표준으로 만들지 않는다.**

```text
"PixelLab으로 8방향 sprite 제작 성공"
→ "PixelLab이 특정 조건에서 유용했다"        (Studio knowledge)
→ "모든 8방향 sprite는 PixelLab을 사용한다"   (잘못된 일반화)
```

**한 번의 실패를 도구의 한계로 만들지 않는다.** Generator X가 한 캐릭터에서 실패했다고 "캐릭터 작업에 부적합"이 되지 않는다. 원인이 prompt · 모델 버전 · 작업 종류 · 스타일 · 해상도 · consistency 요구 · 입력 reference · tool limitation 중 어디인지 확인한다.

**한 번의 Art Review를 프로젝트 전체 규칙으로 만들지 않는다.** "이 갑옷은 너무 복잡하다"는 그 자산에 대한 의견일 수 있다. 전체 규칙으로 승격하려면 근거가 필요하다.

- 디렉터가 명시적으로 전체 규칙으로 결정했다
- 같은 문제가 반복된다
- 여러 자산에서 구조적으로 확인된다
- 실제 게임 화면에서 반복적으로 나타난다

**Claude의 추론만으로 승격하지 않는다.** "이건 공통 규칙인 것 같다"는 판단은 후보 제안이지 승격이 아니다. 가능하면 실제 반복을 확인한다.

전형적인 실패 패턴은 다음과 같다.

```text
한 번 성공        → Studio 표준
한 번 실패        → Tool 금지
한 게임에서 승인   → 다른 게임의 기본 스타일
Validator가 편함  → 디자인을 validator에 맞춤
자동화 어려움     → 디자인 단순화
```

---

## 6. Pattern과 Rule을 구분한다

```text
Pattern          이런 상황에서 이 방법이 자주 유용했다      → 주로 Studio knowledge
Rule             이 프로젝트에서는 반드시 이렇게 한다        → Project knowledge
Recommendation   픽셀 tile 작업에서는 seam preview를 먼저 만든다   → 유용한 제안
Default          모든 tile 작업은 5×5 preview 필수              → 강제할 필요 없음
```

Studio는 주로 Pattern과 capability를 축적한다. Rule은 프로젝트가 가진다.

---

## 7. 무엇에서 배우는가

학습 정보는 여러 곳에서 온다 — Director Review · Rejected Candidate · Approved Asset · runtime screenshot · validation failure · export 문제 · tool 실험 · production batch · 외부 협업 · engine integration. **하나의 source만 보지 않는다.**

**반복 실패**는 가장 좋은 공통화 후보다.

```text
문제: alpha fringe가 자주 발생
반복: 3개 프로젝트에서 발생
대응: alpha edge checker + cleanup tool
```

**반복 성공**도 마찬가지다. "runtime screenshot을 actual display scale로 비교하면 캐릭터 가독성 판단이 빨라진다"가 여러 프로젝트에서 확인되면 Studio workflow knowledge가 된다.

다만 **학습하려면 실패의 위치를 먼저 구분해야 한다.** "캐릭터가 게임에서 흐림"의 원인이 source resolution · export resize · filtering · camera · post-processing 중 어디인지에 따라 배울 내용이 완전히 달라진다. **잘못된 원인을 학습하면 나쁜 공통 규칙이 생긴다.** 계층 구분은 `10_ENGINE_HANDOFF.md`를 따른다.

**Rejected Candidate**는 어떤 방향이 맞지 않았는지, 어떤 제작 방식이 불안정한지, 어떤 reference가 잘못 해석되었는지, 어떤 tool limitation이 있는지를 알려준다. 다만 모든 반려 후보를 영구 보존할 필요는 없다.

**Approved Asset**은 그 프로젝트 안에서 강한 기준(proportion · density · color · silhouette · material · detail level)이 된다. 하지만 **다른 게임의 기본 Reference로 자동 사용하지 않는다.** "Game A hero가 성공적이었다"는 이유로 Game B 작업에 자동으로 불러오지 않으며, 다른 프로젝트 자료를 쓸 때는 명시적인 이유가 있어야 한다.

**Runtime 경험**은 화면에서만 알 수 있는 것을 준다 — 실제 표시 크기 · background interaction · lighting · VFX overlap · UI hierarchy · movement readability. Studio는 source 제작 경험뿐 아니라 runtime 검증 경험도 축적한다.

---

## 8. 영역별 구분

각 영역에서 같은 경계가 반복된다. **능력은 공통, 값은 프로젝트.**

**Tool** — 도구 경험은 조건과 함께 기록해야 재사용 가능한 지식이 된다.

```text
나쁜 기록:  Tool X는 좋다.
좋은 기록:  Tool X는 32–64px directional sprite에서 방향 일관성이 안정적이었다.
```

도구는 model · API · 가격 · quality · feature · license · export format이 모두 바뀔 수 있으므로, **오래된 tool knowledge를 영구 진리로 취급하지 않고 필요하면 다시 검증한다.**

**Engine** — Unity pixel import helper · Godot atlas export · Roblox texture upload flow · Web image optimization은 공통 기술이 될 수 있고, "Unity pixel project에서 bilinear filtering 때문에 sprite가 흐려지는 문제가 반복된다" 같은 패턴도 마찬가지다. 반면 `Game A는 nearest filtering 사용`, game-b의 특정 shader 값은 프로젝트 규칙이다.

**Validator** — 검사 능력은 스타일과 비교적 독립적이어서 재사용성이 높다. 규격 값은 프로젝트별이다. 상세는 `09_ASSET_SPEC_AND_VALIDATION.md`를 따른다.

**Exporter** — resize · format conversion · atlas · channel packing · naming · engine copy는 공통화하기 좋고, target path와 프로젝트별 설정은 남는다.

**Reference와 Art Direction 분석** — reference 자체는 프로젝트 고유이지만, 분석 방법(어떤 속성을 참고할지 분리 · color/silhouette/lighting 개별 분석 · anti-reference 기록 · reference 간 역할 구분 · 형태 언어 분해 · density 분석 · lighting responsibility 구분)은 공통 능력이다.

**Review** — 비교 조건 통제 · contact sheet · actual runtime scale · before/after · silhouette 비교 · 기술적 사실과 미적 의견의 분리는 공통 기법이다. "B 후보가 더 좋았다"는 판단 자체는 프로젝트 기록이다.

**디렉터의 언어** — "너무 깨끗하다"를 surface variation · edge irregularity · wear · less uniform gradient 중 무엇으로 읽을지 판단하는 **해석 능력**은 축적할 수 있다. 하지만 `"귀엽게" = 머리 40% 확대` 같은 고정 번역 사전을 만들지 않는다. 같은 표현도 프로젝트마다 의미가 다르다. **학습해야 하는 것은 문맥을 보고 해석하는 방법이지 감각적 언어를 formula로 바꾸는 것이 아니다.**

---

## 9. 공통화의 조건과 비용

원칙은 `03_PROJECT_STRUCTURE.md`와 같다.

> **미리 공통화하지 말고, 반복이 확인되면 공통화한다.**

승격 전에 확인할 것.

- 여러 작업 · 여러 프로젝트에서 반복되는가
- 특정 스타일에 종속되지 않는가
- 특정 tool version에만 해당하지 않는가
- 예외가 지나치게 많지 않은가
- 입력과 출력이 비교적 명확한가
- 유지 비용보다 반복 절감 효과가 큰가
- 더 단순한 형태로 표현할 수 있는가

공통 도구에는 비용이 따른다 — API 변경 · dependency · bug · 문서 · 호환성. **한 번 시간을 절약했다고 무조건 Studio tool로 만들지 않는다.**

자연스러운 흐름은 이쪽이다.

```text
project-local  →  반복 사용  →  일반화  →  studio tool
```

`game-a/tmp/fix-red-channel.py`를 한 번 썼다고 바로 `studio/tools/`로 올리지 않는다. 승격할 때는 **프로젝트 값이 parameter로 빠져야 한다.** `if color == game_a_red`가 남아 있으면 그것은 공통 도구가 아니라 프로젝트 스크립트다.

양쪽 실패를 모두 피한다.

```text
너무 이른 추상화   universal asset framework · ontology · huge schema · generic pipeline engine
너무 늦은 공통화   같은 alpha checker를 세 프로젝트에 각각 복사
```

---

## 10. 기록의 형태

**모든 경험을 문서화하지 않는다.** 한 번만 발생한 사소한 오류, 쉽게 찾을 수 있는 기본 사용법, 프로젝트에만 의미 있는 작은 수정, 다시 쓸 가능성이 낮은 임시 방법은 굳이 남기지 않는다. **문서화 자체가 작업의 목적이 되지 않게 한다.**

기록 가치는 이렇게 판단한다. 다시 발생할 가능성이 있는가 · 다른 프로젝트에서도 쓸 수 있는가 · 해결에 시간이 많이 들었는가 · 잊으면 같은 비용을 다시 치르는가 · 자동화할 가치가 있는가 · 특정 스타일과 독립적인가.

형식은 내용에 맞춘다. 하나의 tool trick · validator · exporter · workflow pattern · engine issue · review method · production recipe가 모두 같은 형식일 필요는 없다. 반복 가능한 제작 방법은 Recipe처럼 정리할 수 있다.

```text
Low-res Character Workflow
1. silhouette concept → 2. 3D blockout → 3. 고정 카메라 render →
4. pixel conversion → 5. manual cleanup → 6. runtime test
```

**다만 이것이 모든 캐릭터 작업의 기본 workflow라는 뜻은 아니다.** 특정 문제에 유용한 선택지다.

변화가 빠른 내용에는 날짜(`Observed: 2026-08`)나 확신 정도를 자연어로 남길 수 있다("한 프로젝트에서만 확인됨", "세 프로젝트에서 반복 확인됨", "현재 tool version에서만 확인됨"). **복잡한 score system은 필요 없고, 모든 노트에 강제하지도 않는다.**

즉시 구현하지 않아도 되는 후보는 목록으로만 둘 수 있다.

```text
Studio reuse candidates:
- tile repeat preview generator
- Roblox upload helper
- character contact sheet
```

공통화된 결과는 `studio/tools/` · `studio/workflows/` · `studio/exporters/` · `studio/shared/`에 들어갈 수 있다. 특정 도구 경험이 충분히 쌓이면 별도 guide를 만들 수 있지만, **이 18개 문서 체계를 도구 매뉴얼로 채우지 않는다.**

나중에 찾을 수 있도록 이름은 **문제 중심**으로 짓는다.

```text
tile-seam-check · sprite-contact-sheet · directional-sprite-workflow
```

`tool-x-workflow` 같은 제품 중심 이름은 도구가 바뀌면 의미가 약해진다.

**Art Studio를 거대한 위키로 만들지 않는다.** 같은 내용이 여러 곳에 복사되면 합칠 수 있지만, 문서 정리 자체가 목적이 되지 않는다.

---

## 11. 스타일 오염을 막는다

Studio 공통 지식에 게임 고유의 시각 정보가 섞이지 않게 한다.

```text
나쁜 공통 문서:  캐릭터는 큰 머리를 사용한다.
좋은 공통 문서:  작은 화면 캐릭터에서는 머리 비율이 가독성에 영향을 주므로
                actual display size에서 비교한다.
```

공통 지식은 가능하면 **"어떤 문제에서 어떤 방법이 유용했는가"** 중심으로 쓴다.

```text
Problem:            8-direction consistency
Useful approaches:  3D base · directional sprite tool · fixed-camera render
```

같은 이유로 tool 지식도 제품 목록이 아니라 capability map으로 유지한다.

```text
좋은 형태:  Need: directional sprite consistency
           Possible approaches: specialized sprite generator · 3D source · manual correction
나쁜 형태:  모든 directional sprite = Tool X
```

**예외적인 스타일 재사용**은 명시적 결정으로만 이루어진다. 디렉터가 "Game A와 같은 스타일로 Game B를 만든다"고 말하거나 후속작·같은 IP라면 일부 스타일 규칙을 공유할 수 있다. 이 경우에도 무엇을 공유하고 무엇을 바꾸는지는 **프로젝트 수준에서 결정하며, Studio 전체 기본값으로 올리지 않는다.** 디렉터가 "이 방식은 앞으로 다른 게임에서도 쓰자"고 할 때도 그것이 스타일 공유인지 제작 기법 공유인지 구분한다.

여러 프로젝트가 공유하는 실제 asset library(generic texture · font · licensed icon · common material)가 있을 수 있다. 라이선스와 사용 범위를 확인하고, **스타일 고유 asset과 구분해서 둔다.** 구매 자산과 외주 협업에서도 "어떤 category는 구매가 효율적", "어떤 format이 integration에 좋았다", "Brief 형식과 revision cycle을 어떻게 잡으면 좋은가" 같은 production knowledge는 공통화할 수 있다.

템플릿은 **구조를 재사용하고 내용은 프로젝트마다 새로 채운다.** 그래서 템플릿에 특정 게임 예시를 과도하게 넣지 않는다. 예시가 기본값처럼 남을 수 있다.

---

## 12. 학습이 미적 판단을 대체하지 않는다

**공통 기술 경험이 Art Direction을 바꾸지 않는다.** "Tool X가 low-detail style에 강하다"는 이유로 프로젝트 디자인을 low-detail로 바꾸지 않는다.

**자동화 편의 때문에 스타일을 바꾸지 않는다.** "이 형태는 자동 생성하기 어렵다"가 "형태를 단순하게 바꾼다"로 이어지는 것은 `02_DIRECTOR_RELATIONSHIP.md`가 명시적으로 금지한 추론이다. 다른 제작 방법을 찾거나 디렉터에게 trade-off를 설명한다.

**미적 판단을 병목으로 보고 제거하지 않는다.** "Director review가 시간이 걸린다"를 이유로 auto-approval을 도입하지 않는다. 중요한 미적 판단은 가치 있는 시간이다. 대신 비교 자료를 더 잘 만든다. "세 후보를 같은 배경과 크기로 보여주면 선택이 빨라진다"가 바로 이 방향의 좋은 Studio knowledge다. **사람을 제거하지 않고 판단을 쉽게 한다.**

**자동 Learning System을 만들지 않는다.** 모든 review text를 분석해 AI가 규칙을 추출하고 자동 등록하는 시스템은 목표가 아니다. Claude는 후보를 제안할 수 있지만 승격은 신중하게 한다.

대규모 production에서 반복 실패 횟수 · validation warning 빈도 · export error 빈도 같은 데이터를 볼 수는 있다. 다만 모든 프로젝트에 analytics를 구축하지 않고, **숫자만으로 Learning을 결정하지 않는다.** "평균 palette count 증가"보다 "runtime에서 캐릭터 detail이 흐려짐"이 더 중요한 정보일 때가 많다.

자동화 후보를 찾을 때는 사람이 시간을 많이 쓰는 **기계적인** 구간을 본다 — background removal · naming · export · screenshot · review sheet 준비.

또한 **과거 Claude의 판단이 프로젝트의 권위가 되지 않게 한다.** "예전에 이 방식이 좋다고 했으므로 이번에도 이 방식"이라고 하지 않는다. 최신 디렉터 결정과 현재 프로젝트 문맥이 우선이다.

---

## 13. 좋은 Learning의 형태

하나의 관찰에서 세 층이 나올 수 있다. **이 셋을 섞지 않는 것이 이 문서의 실무적 핵심이다.**

```text
Observation
작은 sprite에서는 high-frequency texture가 실제 runtime에서 사라진다.

Reusable technique          → Studio
source preview와 함께 actual display scale preview를 생성한다.

Project-specific decision   → Game A
Game A에서는 texture density를 낮춘다.
```

같은 구조가 Review 결과에도 적용된다.

```text
"B 승인."                                    → Review Log
B가 승인된 이유: 작은 화면에서 실루엣이 가장 명확  → 프로젝트 아트 지식
작은 화면 비교에는 actual-size contact sheet가 유용  → Studio technique
```

하나의 작업에서 Review Log · Art Direction · Style Spec · Studio Workflow · Tool Note가 각각 다른 내용을 가져갈 수 있다. **모든 것을 한 문서에 넣지 않는다.**

승격의 흐름은 개념적으로 이렇다.

```text
PROJECT EXPERIENCE → OBSERVATION → 반복 가치가 있는가?
→ 스타일 독립적인가? → 일반화 → STUDIO KNOWLEDGE
```

**이것을 자동 workflow engine으로 구현할 필요는 없다.**

공통 지식도 영구적이지 않다. tool obsolete · API 제거 · engine 변경 · 더 나은 방법의 등장으로 deprecated되거나 archive될 수 있다.

```text
Deprecated: old FLUX endpoint integration
Reason:     API removed
```

실험 단계의 자료는 project-local이나 임시 위치에 두고, 반복 가치가 확인되면 공통화한다. **한 번의 실험 결과를 바로 공식 workflow로 만들지 않는다.**

---

## 14. 재사용은 복사가 아니라 적용이다

```text
좋은 재사용:  common tile seam checker + Game B tile size
나쁜 재사용:  Game A tile pipeline 전체를 Game B에 그대로 복사
```

공통 기법을 쓰더라도 새 프로젝트의 Project Brief · Art Direction · Style Spec · platform · engine · camera를 먼저 확인한다. **같은 기술도 적용 방식이 달라진다.**

규모 조건도 함께 기억한다. 1개 자산에는 대화형 생성이, 100개 batch에는 API batch가 적합할 수 있다. 제작 방식 비교 경험도 정확한 가격보다 **조건과 trade-off 중심**으로 남긴다("방법 A는 빠르지만 수정성이 낮다 / 방법 B는 초기 비용이 높지만 반복 생산에 유리하다").

---

## 15. Learning이 잘 되고 있는 상태와 경고 신호

**잘 되고 있는 상태**

- 새 게임에서 기본 검사기와 exporter를 다시 만들지 않는다
- 같은 engine 문제를 매번 처음부터 찾지 않는다
- 비교 자료를 빠르게 만든다
- 새로운 도구를 capability 관점에서 평가한다
- **프로젝트 스타일은 서로 섞이지 않는다**

**경고 신호**

- 모든 게임이 비슷한 palette를 사용한다
- 같은 캐릭터 비율이 반복된다
- 한 tool이 모든 작업의 기본값이 되었다
- 이전 프로젝트 prompt를 자동으로 복사한다
- validator 규칙이 디자인을 결정한다
- 과거 workflow가 새 게임을 제약한다
- 공통 문서가 특정 게임의 reference로 가득하다

이런 신호가 보이면 스타일 전염이나 과도한 표준화가 일어나고 있다.

이 경계는 `01_STUDIO_IDENTITY.md`의 정체성과 직접 연결된다. Learning이 키워야 하는 것은 **한 스타일을 더 잘 복제하는 능력**이 아니라 **서로 다른 스타일의 문제를 구분하고 각각에 맞는 방법을 선택하는 능력**이다.

---

## 16. 다른 문서와의 관계

- **`01_STUDIO_IDENTITY.md`** — 스튜디오에 축적되는 것은 스타일이 아니라 제작 능력이다. 이 문서는 그 축적의 기준을 정한다.
- **`02_DIRECTOR_RELATIONSHIP.md`** — 과거 판단과 자동화가 디렉팅 위에 서지 않게 한다.
- **`03_PROJECT_STRUCTURE.md`** — `studio/`는 공통 기술, `projects/`는 게임별 정체성. 이 문서는 그 구조 원칙을 지식 축적에 적용한다.
- **`04_ART_DIRECTION_SYSTEM.md`** — 시각 축을 분석하는 방법은 공통화하고, 실제 팔레트·형태 언어·조명 방향은 프로젝트에 남긴다.
- **`05_TOOL_ROLES.md`** — Tool 경험은 capability map을 정교하게 만들지만 특정 tool을 영구 표준으로 만들지 않는다. `문제 → capability → tool` 순서는 바뀌지 않는다.
- **`06_ASSET_LIFECYCLE.md`** — Rejected · Approved · Superseded 결과는 학습 source가 될 수 있지만, 상태 자체가 학습 규칙을 뜻하지는 않는다.
- **`07_GENERATION_WORKFLOW.md`** — 반복적으로 유용한 루틴(`sample → runtime test → batch` 등)은 Studio workflow로 승격할 수 있다.
- **`08_REVIEW_AND_APPROVAL.md`** — Review 결과 중 장기적으로 의미 있는 결정만 프로젝트 지식에 남고, 그중 범용적인 제작 방법만 Studio 후보가 된다.
- **`09_ASSET_SPEC_AND_VALIDATION.md`** — 검사 능력은 공통, 규격 값은 프로젝트. 반복되는 technical bug는 새 validator로 이어질 수 있다(sprite baseline drift 반복 → baseline checker).
- **`10_ENGINE_HANDOFF.md`** — 반복되는 export/import/runtime 문제 해결법은 Studio knowledge로 발전한다(Web export alpha 문제 반복 → export helper 개선). 프로젝트 고유 material·shader·style 값은 남긴다.
- **템플릿** — `STYLE_SPEC`은 프로젝트 기술 규칙을, `ASSET_MANIFEST`는 현재 상태를, `ASSET_BRIEF`는 개별 요구를, `REVIEW_LOG`는 중요한 결정을 보존한다. 이 문서는 **그 자료에서 무엇을 Studio 공통 지식으로 승격할지의 원칙**만 제공한다. Manifest에서 병목이나 반복 실패 경향을 읽을 수는 있지만 분석 시스템으로 확장하지 않는다.

회고는 프로젝트나 milestone(prototype 완료 · vertical slice · character batch 등)이 끝날 때 짧게 할 수 있다. 무엇이 반복적으로 잘 작동했는가 · 무엇이 계속 실패했는가 · 어떤 도구가 어떤 조건에서 유용했는가 · 무엇을 Studio로 올릴 가치가 있는가. **매번 거대한 retrospective를 강제하지 않는다.**

---

## 17. 이 문서에서 다루지 않는 것

```text
프로젝트별 실제 Art Direction     ART_DIRECTION.md
프로젝트별 Style Rule            STYLE_SPEC.md
개별 자산 상태                   ASSET_MANIFEST.md
개별 제작 요구                   ASSET_BRIEF.md
중요한 승인/반려 기록             REVIEW_LOG.md
구체적인 Tool 사용 매뉴얼         별도 tool guide
Validator / Exporter 구현        studio/tools/ · studio/exporters/
```

이 문서는 **지식을 어디에 남기고 언제 재사용할 것인지의 상위 원칙**에 집중한다.

---

## 18. 핵심 원칙 요약

Learning & Reuse는 모든 프로젝트를 같은 방식으로 만드는 표준화 시스템이 아니다.

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

> **좋은 Learning은 문서의 양이 아니라, 같은 실수를 줄이고 새 게임에서 더 빠르게 올바른 제작 방법을 선택할 수 있게 만드는 데 있다.**
