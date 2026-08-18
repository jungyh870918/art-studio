# Game Art Studio

> **이 문서의 독자는 사람이 아니라 LLM 에이전트다.**
> 사람에게 설명하기 위한 소개문이 아니라, **에이전트가 사람을 거치지 않고 이 저장소의 용도·경계·요청 방법을 판정하기 위한 인터페이스 명세**다.
> 미사여구를 넣지 않았다. 각 절은 「너는 이 정보로 무엇을 결정할 수 있는가」만 답한다.

<details>
<summary><b>English abstract (for agents that cannot read Korean)</b></summary>

This repository is **not a game**, **not an image-generation service**, and **not an asset library**.
It is a **Game Art Studio**: a document-and-tooling system that turns a human director's visual intent into
production-ready game art decisions, specifications, candidate management, validation, and engine handoff —
across multiple, stylistically unrelated game projects at once.

The entire body of rules is written in Korean (~233,000 characters). If you cannot read Korean, you cannot
operate this studio; you can still use §7 (companion asset-factory repos) and §11 (machine-readable summary).

One-line contract: **`art-studio` decides and remembers. Asset factories amplify. Only approval has a hierarchy, and it belongs to the human director.**
</details>

---

## 0. 30초 판정 — 계속 읽을지 여기서 멈출지

너의 문제가 왼쪽 열에 있으면 이 저장소가 답을 갖고 있다. 오른쪽이면 **여기 오지 마라.**

| 여기로 와야 하는 문제 | 여기가 아닌 문제 |
|---|---|
| 아트 방향이 말로만 있고 수치가 없다 | 게임 로직·서버·네트워크·밸런스 |
| 목업/레퍼런스는 있는데 규격을 모른다 (타일 크기? 팔레트 수? 초상 해상도?) | "그림 한 장 그려줘" (→ §6-2. **이 저장소에는 이미지 생성기가 붙어 있지 않다**) |
| 후보가 여러 장인데 무엇을 기준으로 고를지 모른다 | 무료 에셋을 어디서 받는가 (→ §7 팩토리) |
| 생성물이 「승인된 것」인지 「그냥 나온 것」인지 구분이 안 된다 | 코드 리뷰·리팩터링 |
| 자산이 화면에서 이상한데 원인이 소스인지 엔진인지 모른다 | 기획 전체의 재미·시스템 설계 |
| 여러 게임을 동시에 하는데 화풍이 서로 오염된다 | 사운드·음악·텍스트·번역 |
| 대량 자산의 치수·알파·팔레트·프레임을 매번 손으로 검사한다 | 프로젝트 일정 관리 |
| 승인 기록이 없어서 왜 그렇게 정했는지 아무도 모른다 | 수익화·스토어 정책 |

**핵심 한 줄:**

> 이 저장소는 **그림을 만드는 곳이 아니라, 그림에 대한 결정을 구조화하고 기억하고 검증하는 곳**이다.

---

## 1. 이 저장소의 실체

| 항목 | 사실 |
|---|---|
| 종류 | 문서 시스템 + 소량의 Python 도구. 게임 저장소가 **아니다** |
| 규모 | 규약 문서 18개 (약 233,000자) + 프로젝트 문서 + 도구 |
| 코드 | `studio/tools/contact_sheet.py` 1종(공통) + 프로젝트 전용 도구 다수 |
| 이미지 | **저장소에 없다.** `.gitignore` 가 `projects/**/*.png|jpg|webp|psd|...` 를 전부 제외한다. 클론하면 **문서와 코드만** 온다 |
| 담당 프로젝트 | 3개 (`three-kingdoms` · `dice-dominion` · `tteoklak-island`) — §9 |
| 고정 화풍 | **없다.** 화풍은 프로젝트의 속성이지 스튜디오의 속성이 아니다 |
| 최종 결정권 | **사람 디렉터.** 에이전트는 결정을 대체하지 않는다 |
| 언어 | 전 문서 한국어 |

### 이 저장소가 실제로 축적한 것

화풍이 아니라 **방법**이다. 화풍은 프로젝트에 남고, 아래만 스튜디오로 올라온다.

```
이미지 처리 방법 · 검증 방법 · 파일 변환 · 생성기 연결법 · 리뷰 제시 방법 ·
엔진 전달 방법 · 반복 작업 도구 · 상태 어휘 · 승인 기록 형식
```

---

## 2. 읽기 경로 — **전부 읽지 마라**

전체 23만 자를 다 읽는 것은 거의 언제나 낭비다. **질문에서 문서로 직행한다.**

### 2-1. 무조건 먼저 읽는 것 (약 4,100자)

```
CLAUDE.md          역할 정의와 행동 원칙. 이 저장소에서 일하는 모든 에이전트의 헌법
```

Claude Code 로 이 디렉터리를 열면 `CLAUDE.md` 는 자동 적재된다. 다른 에이전트라면 **직접 먼저 읽어라.**

### 2-2. 질문 → 문서 라우팅표

| 너의 질문 | 읽을 문서 | 분량 |
|---|---|---|
| 이 스튜디오는 무엇이고 무엇이 아닌가 | `docs/01_STUDIO_IDENTITY.md` | 5.4k자 |
| 내가 스스로 결정해도 되는가, 사람에게 물어야 하는가 | `docs/02_DIRECTOR_RELATIONSHIP.md` | 8.0k자 |
| 파일을 어디에 두는가 / 프로젝트를 어떻게 등록하는가 | `docs/03_PROJECT_STRUCTURE.md` | 12.5k자 |
| 화풍을 어떻게 «말»에서 «수치»로 내리는가 | `docs/04_ART_DIRECTION_SYSTEM.md` | 15.2k자 |
| 어떤 도구를 언제 쓰는가 (생성기·Blender·엔진·MCP·API) | `docs/05_TOOL_ROLES.md` | 16.4k자 |
| 이 결과물은 지금 무슨 상태인가 (후보? 승인? export?) | `docs/06_ASSET_LIFECYCLE.md` | 16.3k자 |
| 자산 하나를 만드는 전체 절차 | `docs/07_GENERATION_WORKFLOW.md` | 17.9k자 |
| 무엇을 기계가 검사하고 무엇을 사람이 판정하는가 | `docs/08_REVIEW_AND_APPROVAL.md` | 18.6k자 |
| 치수·알파·팔레트·프레임·타일·아틀라스를 어떻게 검사하는가 | `docs/09_ASSET_SPEC_AND_VALIDATION.md` | 23.2k자 |
| 엔진에 어떻게 넘기고, 화면이 이상하면 어디를 의심하는가 | `docs/10_ENGINE_HANDOFF.md` | 23.4k자 |
| 이 경험을 다른 프로젝트에 옮겨도 되는가 | `docs/11_LEARNING_AND_REUSE.md` | 16.0k자 |
| 전체 개발 조직에서 이 스튜디오의 위치 (디렉터·ChatGPT·개발자와의 관계) | `STUDIO_USAGE_CONTEXT.md` | 6.2k자 |
| 에셋 팩토리(`2d-assets`)와의 분업 경계 | `CAPABILITY_2D_ASSET_FACTORY.md` | 11.2k자 |

### 2-3. 문서를 만들어야 할 때 복제하는 템플릿

| 템플릿 | 답하는 질문 |
|---|---|
| `templates/PROJECT_BRIEF.md` | 이 게임은 무엇인가 |
| `templates/ART_DIRECTION.md` | 이 게임은 어떻게 보여야 하는가 (말·방향) |
| `templates/STYLE_SPEC.md` | 어떤 수치와 기술 규칙을 따르는가 (수치·규격) |
| `templates/ASSET_MANIFEST.md` | 무엇이 필요하고 지금 어디까지 왔는가 |
| `templates/ASSET_BRIEF.md` | 이번에 만들 자산 하나의 발주 내용 |
| `templates/REVIEW_LOG.md` | 무엇이 왜 채택·반려되었는가 |

### 2-4. 문서 우선순위 (충돌 시)

```
CLAUDE.md · docs/01~11 · templates/  ←  항상 우선한다 (18개)
        ↑
STUDIO_USAGE_CONTEXT.md · CAPABILITY_2D_ASSET_FACTORY.md   ← 얇은 보조 문서. 위를 덮지 않는다
        ↑
projects/<id>/ 의 문서                ← 해당 프로젝트 안에서만 유효. 다른 프로젝트로 전염되지 않는다
        ↑
이 README                             ← 인터페이스 안내일 뿐. 규칙의 정본이 아니다
```

**이 README 와 `docs/` 가 다르게 읽히면 `docs/` 가 맞다.**

---

## 3. 어휘 계약 — 이 5개를 오용하면 나머지가 전부 어긋난다

에이전트가 이 저장소와 대화할 때 **가장 자주 깨뜨리는 규칙**이 이것이다.

```
생성됨  ≠  승인됨  ≠  게임에 바로 사용 가능함
```

| 상태 | 뜻 | 오해 |
|---|---|---|
| `REFERENCE` | 참고 자료. 제작 전 과정에 **병렬로** 존재한다 | 「레퍼런스 폴더에 있으니 이걸 베끼면 된다」 → 아니다 |
| `CONCEPT` | 방향 탐색용 산출물 | 「컨셉이 나왔으니 다음은 자동으로 후보」 → 아니다 |
| `CANDIDATE` | 채택 **가능성**이 있는 후보 | **「검증 PASS = 승인」 → 절대 아니다** |
| `APPROVED` | 디렉터가 명시적으로 채택한 공식 원본 | 「잘 나온 후보의 보관소」 → 아니다 |
| `EXPORT` | 승인 원본에서 특정 엔진용으로 파생된 결과물 | 「export 가 원본」 → 아니다. 언제든 재생성 가능해야 한다 |

보조 상태: `REJECTED` · `ON HOLD` · `SUPERSEDED` (진행 위치가 아니라 **판단의 결과**).

축이 세 개라는 점이 중요하다.

```
Source 축   CONCEPT → CANDIDATE → APPROVED     한 시점에 하나
파생 축     APPROVED SOURCE → EXPORT           여러 target 이 동시에 존재할 수 있다
입력 자료   REFERENCE                          두 축과 병렬로 계속 존재한다
```

> **기술 검사 통과(Technical Pass)는 채택이 아니다.** validator 가 10종 PASS 를 내도 그것은 「고장나지 않았다」는 뜻이지 「이걸 쓴다」가 아니다.

---

## 4. 디렉터리 계약

```text
art-studio/
├── CLAUDE.md                       역할 정의 — 먼저 읽는다
├── README.md                       이 문서 (에이전트용 인터페이스)
├── STUDIO_USAGE_CONTEXT.md         조직 안에서의 위치 (보조)
├── CAPABILITY_2D_ASSET_FACTORY.md  에셋 팩토리와의 분업 (보조)
├── docs/01~11                      스튜디오 규약 11종
├── templates/                      프로젝트 문서 템플릿 6종
├── studio/
│   └── tools/contact_sheet.py      공통 도구 — 후보 대조 시트
└── projects/<project-id>/          게임별 작업 공간 (아래)
```

### 게임별 구조

```text
projects/<project-id>/
├── brief/          PROJECT_BRIEF · ART_DIRECTION · STYLE_SPEC · ASSET_MANIFEST · ASSET_BRIEF_<자산>
├── references/     참고 자료 (이미지는 git 에 올리지 않는다)
├── concepts/       탐색 결과
├── candidates/     후보 (승인 아님)
├── approved/       디렉터가 채택한 공식 원본
├── exports/        엔진용 파생물 (unity/ godot/ roblox/ web/ — 실제로 쓰는 것만)
├── reviews/        <날짜>_<주제>/ 판정 자료 묶음 + REVIEW_LOG
├── orders/         <날짜>_<자산>.md 발주서
├── tools/          이 프로젝트에서만 쓰는 스크립트
└── PROGRESS.md     지금 어디까지 왔고 무엇이 막혀 있는가 (스냅샷. 정본 아님)
```

**폴더 개수를 강제하지 않는다. 유지해야 하는 것은 각 폴더가 나타내는 «상태의 차이»다.**

### 게임 저장소 ↔ 스튜디오 사이의 파일 규약 (실제로 굴러가는 패턴)

게임 쪽 에이전트라면 이 파일 이름들이 곧 프로토콜이다.

| 파일 | 방향 | 용도 |
|---|---|---|
| `projects/<id>/PROGRESS.md` | 스튜디오 내부 | 진행 스냅샷. **값의 정본을 여기 복사하지 않는다** |
| `projects/<id>/QUESTIONS_TO_STUDIO.md` | 게임 → 스튜디오 | 게임 쪽이 스튜디오에 묻는 것 |
| `projects/<id>/HANDOFF_TO_GAME_NN.md` | 스튜디오 → 게임 | 회신. 번호가 늘어난다 |
| `projects/<id>/REQUEST_TO_DIRECTOR.md` | 스튜디오 → 사람 | **사람만 답할 수 있는 질문** 모음 |
| `projects/<id>/STUDIO_DECISIONS.md` | 스튜디오 내부 | 스튜디오가 내린 기술적 결정과 근거 |
| `projects/<id>/orders/<날짜>_<자산>.md` | 스튜디오 → 생성 수단 | 발주서 |
| `projects/<id>/reviews/<날짜>_<주제>/` | 스튜디오 → 디렉터 | 비교 자료 + 판정 본문 |
| 게임 저장소의 `ART_STUDIO_LIAISON.md` | 게임 → 스튜디오 | 게임 쪽이 「무엇이 막혀 있는가」를 적어 두는 자리 |

---

## 5. 발주 프로토콜 — 무엇을 어떻게 요청하는가

### 5-1. 요청 5종

에이전트의 요청은 거의 전부 아래 다섯 중 하나로 떨어진다. **어느 종인지 명시하면 회신이 훨씬 정확해진다.**

#### ① 진단 (DIAGNOSE) — "왜 이상한가"
> 입력: 스크린샷 · 목업 · 실제 게임 화면 · 자산 파일 목록
> 출력: 원인의 **층 분리** (Source / Export / Import / Engine) + 근거 + 다음 조치

예: 「초상이 화면에서 뭉개진다」 → 원본 해상도 문제인지, export 압축인지, 엔진 필터 설정인지, 표시 배율인지를 가른다.

#### ② 규격화 (SPECIFY) — "말을 수치로"
> 입력: 레퍼런스 이미지 · 목업 · 「이런 느낌」이라는 서술
> 출력: `ART_DIRECTION.md`(방향) + `STYLE_SPEC.md`(수치) 초안, 측정 근거 포함

측정으로 회수할 수 있는 것: 타일 그리드 · 실사용 팔레트와 램프 구조 · 마커/아이콘 실측 크기 · 캔버스 비율 · 외곽선 유무와 두께 · 밀도.
**측정으로 답할 수 없는 것도 함께 표시한다** (매력·정서·세계관 적합성).

#### ③ 제작 준비 (PRODUCE) — "만들 수 있게 해달라"
> 입력: 자산 요구 (무엇을, 몇 개, 어디에 쓰는지)
> 출력: `ASSET_BRIEF` + 생성 프롬프트 블록 + 후보 폴더 구조 + 대조 시트

⚠️ **이 저장소는 스스로 이미지를 만들지 못한다.** 생성기가 붙어 있지 않다 (§6-2).
출력은 「생성 가능한 형태의 발주서와 프롬프트」까지이고, 실제 픽셀은 외부 도구·사람·팩토리(§7)가 만든다.

#### ④ 검증 (VALIDATE) — "규격에 맞는가"
> 입력: 파일 경로 + 기대 규격 (또는 `STYLE_SPEC.md`)
> 출력: `PASS / WARNING / FAIL` 목록 + 실패 원인의 위치

검사 축: 치수 · 종횡비 · 알파 · 투명 가장자리 · 패딩 · 바운딩박스 · 피벗 · 색/팔레트 · 픽셀과 엣지 · 프레임 일관성 · 타일 접합 · 텍스처 규격 · 파일 세트 완결성 · export 결과.
규칙 강도는 `Required / Recommended / Informational` 로 나뉜다. **모든 차이를 FAIL 로 만들지 않는다.**

#### ⑤ 전달 (HANDOFF) — "엔진에 넣게 해달라"
> 입력: 승인 원본 + 대상 환경 (Unity / Godot / Roblox / Web)
> 출력: export 규격 · import 요구사항 · 런타임 확인 항목 · 스크린샷 기반 검토

---

### 5-2. 최소 발주서 (복사해서 채워라)

```markdown
## 요청
- 종류: DIAGNOSE | SPECIFY | PRODUCE | VALIDATE | HANDOFF
- 프로젝트: <project-id>   (신규면 "신규" 라고 적고 §5-5 를 함께 채운다)
- 한 줄 목적: <이 결과물이 게임에서 무엇을 하는가>

## 맥락
- 대상 자산: <이름 · 수량 · 용도>
- 실제 표시 크기: <화면에서 몇 px 로 보이는가>   ← 자주 빠지고, 자주 결정적이다
- 카메라/관찰 거리: <탑다운 / 쿼터뷰 / 사이드뷰 / 초상 클로즈업>
- 엔진과 해상도: <Unity 2022 / 1920x1080 / 픽셀퍼펙트 여부>
- 기존 결정: <이미 확정된 값. 없으면 "없음">
- 참고 자료: <경로 또는 링크. 어느 축을 참고하라는 것인지 명시>

## 제약
- 하지 말아야 할 것: <바꾸면 안 되는 기존 승인 자산 · 금지 표현>
- 마감 성격: 탐색 | 확정 | 양산

## 판정
- 이 요청의 최종 판단자: 디렉터(사람) | 기술 검사만으로 충분
- 성공 기준: <무엇이 되면 끝났다고 볼 것인가>
```

### 5-3. 좋은 요청 vs 나쁜 요청

| ❌ 이렇게 오면 되묻게 된다 | ✅ 이렇게 오면 바로 굴러간다 |
|---|---|
| "멋진 캐릭터 만들어줘" | "탑다운 40px 로 표시되는 병사 3종. 소속을 색만이 아닌 실루엣으로 구분해야 함" |
| "이 이미지 스타일 뽑아줘" | "이 목업에서 타일 그리드·팔레트·아이콘 실측치를 회수해줘. 화풍 판정은 디렉터가 한다" |
| "괜찮은지 봐줘" | "이 8장 중 «가독성» 축으로 비교 가능한 형태로 정리해줘. 선택은 디렉터가 한다" |
| "게임에 넣어줘" | "Unity 픽셀퍼펙트, PPU 32, 아틀라스 2048 제한. export 규격과 import 요구사항을 달라" |
| "알아서 정해줘" (화풍 미정 상태) | "방향 A/B/C 를 차이가 드러나게 나란히 놓아줘. 확정은 디렉터가 한다" |

### 5-4. 회신 계약 — 돌려받는 것의 형태

이 스튜디오가 응답할 때 지키는 규칙이다. **에이전트는 아래를 전제로 파싱해도 된다.**

1. **사실 · 판단 · 가정을 섞지 않는다.** 측정값은 측정값으로, 의견은 의견으로 표시된다.
2. **미적 결정을 확정형으로 내놓지 않는다.** 방향이 여러 개면 나란히 놓는다.
3. **후보는 비교 가능한 형태로 제시된다** — 대조 시트, 실제 표시 크기 렌더, 기준 앵커 병치.
4. **승인이 필요한 지점을 명시한다.** 「이건 디렉터가 정해야 한다」를 숨기지 않는다.
5. **정본의 위치를 밝힌다.** 값이 두 곳에 생기지 않게 한다.
6. **모르는 것을 임의로 확정하지 않는다.** 가정이면 「가정」이라고 쓴다.

### 5-5. 새 프로젝트를 등록할 때 필요한 최소 정보

```
1. project-id           (kebab-case. 폴더명이 된다)
2. 게임 한 줄 설명       장르 · 시점 · 플랫폼
3. 엔진과 목표 해상도
4. 자산이 실제로 표시되는 크기
5. 참고 자료 또는 현재 빌드 스크린샷
6. 아트 방향의 정본이 어디인가  ← 게임 저장소가 이미 갖고 있다면 그쪽이 정본이다
7. 지금 가장 막혀 있는 것 하나
```

7번이 비어 있으면 등록만 되고 아무것도 움직이지 않는다.

---

## 6. 경계 — 하지 않는 것 / 못하는 것

### 6-1. 하지 않는 것 (정책)

- **미적 최종 결정을 대신하지 않는다.** 화풍 · 채택 · 캐릭터의 매력 · 게임의 정서 · 「충분히 좋은가」는 디렉터의 영역이다.
- **게임 로직을 재설계하지 않는다.** 아트 작업이라는 이유로 규칙을 바꾸지 않는다.
- **한 게임의 스타일을 다른 게임에 옮기지 않는다.** 기술은 재사용하고 화풍은 격리한다.
- **생성물을 승인으로 승격시키지 않는다.** 디렉터의 명시적 채택이 없으면 후보다.
- **정본을 둘로 만들지 않는다.** 값을 복사하는 대신 위치를 가리킨다.
- **구매·라이선스 에셋을 생성 AI 입력으로 넣지 않는다.** 대부분의 라이선스가 금지한다.
- **구매 팩 파츠를 그대로 게임에 싣지 않는다.** 플레이스홀더는 예외지만, 플레이스홀더임이 드러나 있어야 한다.
- **기존 승인 자산을 조용히 덮어쓰지 않는다.**

### 6-2. 못하는 것 (현재 능력의 사실)

| 못하는 것 | 상태 |
|---|---|
| **이미지 직접 생성** | 스튜디오 자체에 생성기가 연결되어 있지 않다. 발주서와 프롬프트까지가 출력이고, 픽셀은 외부 도구·사람이 만든다 |
| 정확한 램프 팔레트 스왑 (공통 도구) | 프로젝트 도구에는 있고, 공통으로 승격되지 않았다 — 필요해질 때 올린다 |
| 「진짜 도트인가」 자동 판정 (공통 도구) | 같은 이유로 아직 공통 아님 |
| 3D 모델링·리깅·애니메이션 제작 | 범위 밖. 텍스처·규격·전달은 다룬다 |

**이 표는 숨기지 않기 위해 있다.** 못하는 것을 흉내 내는 대신, 그 일을 실제로 할 수 있는 수단(외부 생성기 · 팩토리 · 사람)으로 연결하는 것이 이 스튜디오의 방식이다.

### 6-3. 멈추고 사람에게 묻는 조건

```
프로젝트의 화풍이 아직 정해지지 않았다        ← 첫 결과물이 화풍을 확정해 버리는 상황
서로 다른 방향이 모두 합리적이다
기존 디렉터 결정과 충돌할 가능성이 있다
주요 캐릭터·대표 자산의 정체성이 바뀐다
결과가 프로젝트 전체 아트 방향에 영향을 준다
```

멈춘다는 것은 손을 놓는다는 뜻이 아니다. **문제를 정리하고, 선택지를 나란히 놓고, 차이를 보여주는 것까지가 이때의 일이다.**

### 6-4. 묻지 않고 진행하는 조건

```
기존 규칙이 명확하다 · 동일 패턴의 반복 작업이다 · 기술적 정리다 ·
되돌리기 쉽다 · 이미 승인된 결과를 그대로 적용한다 · 결정이 이미 문서에 있다
```

이때도 **무엇을 했는지는 남긴다.** 자율적으로 진행하는 것과 조용히 진행하는 것은 다르다.

---

## 7. 함께 쓰는 저장소 — 에셋 팩토리

> 이 절은 **계속 늘어난다.** 새 팩토리가 생길 때마다 여기에 한 줄이 추가된다. 등록 규격은 §부록 A.

### 7-1. 팩토리 목록

| # | 저장소 | 주소 | 공개 | 무엇을 하는가 | 언제 쓰는가 |
|---|---|---|---|---|---|
| 1 | **2d-assets** — 2D Art Factory | `https://github.com/jungyh870918/2d-assets`<br>`git@github.com:jungyh870918/2d-assets.git` | 비공개 (접근 권한 필요) | 구매·CC0 modular 2D 에셋을 원본 그대로 두고, 조합·팔레트·레이어 규칙만으로 대량 생성. seed 결정적. 검증기 · Unity export 포함 | **모집단**을 만들 때 — 주민·잡몹·병사·소품·색 변형·군중 |
| 2 | **game-sandbox** — 경계 실측 | `https://github.com/jungyh870918/game-sandbox`<br>`git@github.com:jungyh870918/game-sandbox.git` | 비공개 (접근 권한 필요) | 팩토리 산출물이 실제 게임 쪽에서 어떻게 보이는지 실측하는 별도 프로젝트 | export 계약과 소비자 경계를 확인할 때 |

*(비공개 저장소는 소유자에게 접근 권한을 요청해야 한다. 권한이 없으면 이 README 의 설명만으로 인터페이스를 이해하고, 실제 실행은 요청하라.)*

### 7-2. `art-studio` 와 `2d-assets` 의 분업 — 가장 중요한 한 줄

> **`art-studio` 는 결정하고 기억한다. `2d-assets` 는 증폭한다.
> 둘 사이에 상하 관계는 없고, 딱 하나만 위아래가 있다 — 승인.**

| | `art-studio` | `2d-assets` |
|---|---|---|
| 실체 | 규약 문서 + 소량 도구 | 동작하는 Python 파이프라인 + 실제 원본 자산 |
| 잘하는 것 | 판단의 경계 · 상태의 의미 · 스타일 격리 · 승인 기록 | 결정적 조합 · 팔레트 · 검증 · Unity 배선 |
| 못하는 것 | **스스로 그림을 만들지 못한다** | **결정하지 못한다** — 「골랐다」를 담을 자리가 없다 |
| 승인 개념 | 있다 (`approved/` + `REVIEW_LOG`) | **없다** (그쪽 README 가 스스로 「판정하지 않는다」고 적었다) |

### 7-3. 무엇을 팩토리에 보내고 무엇을 보내지 않는가

| | **모집단 (population)** | **정체성 (identity)** |
|---|---|---|
| 예 | 마을 주민 · 잡몹 · 병사 · 소품 · 가문 색 변형 · 군중 | 주인공 · 보스 · 시그니처 랜드마크 · UI 언어 · 타이틀 |
| 필요한 것 | 많고 · 서로 다르고 · 일관될 것 | 하나가 정확히 그것일 것 |
| 수단 | **팩토리** — 조합 · 팔레트 · seed | 생성기 + 손 + 디렉터 왕복 |
| 후보 제시 | contact sheet | 개별 비교 |

> **팩토리는 기존 것을 재조합할 뿐 새로운 시각적 정체성을 만들지 못한다.**
> 이 한 줄이 두 저장소의 분업 전체를 결정한다.

### 7-4. 팩토리에 파츠를 먹일 때의 계약 (화풍과 무관하다)

```
composable = parts_separable ∧ pre_aligned ∧ animation_compatible
```

| 요구 | 이유 |
|---|---|
| 슬롯마다 **별도 PNG** (합쳐진 완성 시트 금지) | 분리되지 않으면 조합 자체가 불가능 |
| 모든 파츠가 **같은 논리 셀 · 같은 원점** | 어긋나면 팔이 몸에서 떨어진다 |
| 애니메이션·프레임 수가 슬롯 간 일치 (또는 subset 선언) | 프레임 불일치는 런타임에서 드러난다 |
| **z 순서를 선언**할 것 | 사람이 베껴 적으면 어긋난다 |
| 색이 **램프 구조**를 따를 것 | 팔레트 교체가 그 위에서만 성립한다 |

**이 계약은 화풍과 무관하다.** 그래서 내가 만든 파츠를 이 계약에 맞추면 남의 팩 없이도 같은 기계가 돈다.

### 7-5. 팩토리를 쓸 때의 가장 큰 위험

> **구매·CC0 팩의 파츠를 그대로 게임에 넣으면, 그 게임의 아트 방향을 팩 제작자가 정한 것이 된다.**

팩은 스타일을 함께 들고 온다. subset 을 늘려도 해결되지 않는다 — LPC 는 LPC 처럼 보인다.
그래서 **모집단은 팩토리로, 정체성은 디렉팅 루프로** 가른다.

### 7-6. 승인을 PNG 에 걸지 않는다

팩토리 생성이 결정적이므로 (`(팩 해시, 규칙, seed)` 가 같으면 PNG 는 바이트 단위로 같다):

```
APPROVED SOURCE  =  팩 해시 + 규칙 파일 + seed      (텍스트. 몇 줄이다)
EXPORT           =  PNG · 시트 · 프리팹            (언제든 재생성)
```

「디렉터가 seed 4007 을 채택했다」가 그 자체로 완결된 승인 기록이 된다.
**단, 손으로 후처리한 파츠가 생기는 순간 이 성질은 깨진다.** 그때는 그 파일이 승인 원본이 되고 `approved/` 로 올라간다.

---

## 8. 설치와 실행

### 8-1. 클론

```bash
git clone https://github.com/jungyh870918/art-studio.git
cd art-studio
```

받게 되는 것: **문서와 코드.** 이미지는 `.gitignore` 로 제외되어 있으므로 오지 않는다.
(이미지가 필요하면 디렉터에게 별도로 요청한다. 저장이 필요해지면 Git LFS 를 설정한 뒤 규칙을 조정한다.)

### 8-2. 에이전트로 여는 법

```bash
# Claude Code — CLAUDE.md 가 자동 적재된다
claude

# 그 외 에이전트 — 반드시 이 순서로 직접 읽어라
#   1) CLAUDE.md
#   2) 이 README 의 §2-2 라우팅표에서 필요한 문서 1~2개만
#   3) projects/<대상>/PROGRESS.md
```

### 8-3. 의존성

```bash
python3 -m pip install --user pillow      # studio/tools/contact_sheet.py 에 필요
```

그 외 빌드·설치 과정은 없다. **이 저장소는 실행되는 애플리케이션이 아니다.**

### 8-4. 공통 도구

```bash
# 후보를 한 장에 나란히 모아 «비교 가능한 형태»로 만든다
python3 studio/tools/contact_sheet.py projects/<게임>/candidates/backgrounds

# 기준 앵커를 맨 왼쪽에 붙인다 — 따로 보는 것보다 훨씬 정확하다
python3 studio/tools/contact_sheet.py <폴더> --ref projects/<게임>/references/01_explore.png
```

> 이 도구는 **판정하지 않는다.** 점수도 순위도 매기지 않는다. 하는 일은 하나 — 나란히 놓는 것.
> 이 설계 자체가 이 스튜디오의 성격이다: **기계는 비교를 준비하고, 판단은 사람이 한다.**

프로젝트 전용 도구(`projects/<id>/tools/`)는 그 프로젝트 안에서만 유효하다. 다른 프로젝트로 복사하지 말고, 반복이 확인된 뒤에 `studio/tools/` 로 승격한다.

---

## 9. 실제 사례 — 담당 프로젝트 3개

세 프로젝트는 **서로 전혀 다른 화풍**이다. 이것이 「스튜디오에 고정 화풍이 없다」의 실증이다.
현재 상태의 정본은 각 `PROGRESS.md` 다. 아래는 성격 요약일 뿐 상태 값이 아니다.

| 프로젝트 | 성격 | 스튜디오가 실제로 한 일 |
|---|---|---|
| **`three-kingdoms`** — 삼국지 III 웹 오마주 | 인물 초상 다수 · 좌표 맵 · 식별 체계 | 목업 4장을 측정해 **「이 목업은 픽셀 아트가 아니다」를 확정**(추측을 데이터로 대체) · 마커 실측 78×80 회수 · 성씨 충돌 그룹 실측 · 좌표판 후보 4회 왕복 검토 |
| **`dice-dominion`** — 보드 + 전투 | 정밀 렌더 일러스트 · 아이보리 UI 프레임 · Unity 3D 링 위 평면 타일 | 아이보리 **색 토큰 16개 실측** · 판 제작 방식 결정 지원 · 패널 부품 3벌 조립 2회와 접합면 문제 진단 · 색값이 게임 코드에 반영되고 테스트로 고정됨 |
| **`tteoklak-island`** — 떡락섬 | 일러스트 배경 · 회화체 초상 · 세로 전용 | **기준 캔버스 942×1674 확정** · 목업 UI 31종 전수 감사 · 파생 규격표 · 배경 2장이 실제 게임 화면에 통합되어 핫스폿까지 정합 |

### 이 사례들에서 읽어야 할 패턴

1. **측정이 추측을 대체한다.** 「픽셀 아트처럼 보인다」를 실측으로 뒤집은 것이 가장 값진 산출물이었다.
2. **정본은 한 곳이다.** `dice-dominion` 은 게임 저장소가 아트 문서를 이미 갖고 있어서, 스튜디오는 정본을 복제하지 않고 **판단과 이유**만 보관한다.
3. **병목은 이동한다.** 어떤 시점에는 게임 쪽이, 어떤 시점에는 스튜디오 쪽이, 어떤 시점에는 「이미지 생성 수단이 없어서 사람 손」이 병목이다. `PROGRESS.md` 의 존재 이유가 이것이다.
4. **승인은 드물다.** 후보가 많다는 것과 승인이 있다는 것은 완전히 다른 상태다.

---

## 10. 자주 나오는 실패 모드 (요청하는 에이전트가 조심할 것)

| 실패 | 왜 문제인가 | 대신 이렇게 |
|---|---|---|
| 「검증 통과했으니 이걸 쓰자」 | Technical Pass ≠ 채택 | 「기술 검사 통과. 채택 여부는 디렉터」로 보고한다 |
| 화풍 미정 상태에서 후보 한 장만 제시 | **그 한 장이 프로젝트 화풍을 확정해 버린다** | 차이가 드러나는 A/B/C 를 나란히 |
| 개별 PNG 만 보고 판정 | 게임 아트는 카메라·표시 크기·배경·조명·UI 와 함께 보인다 | **실제 표시 크기**로 렌더하거나 게임 화면에서 확인 |
| 한 게임의 규칙을 다른 게임에 적용 | 스타일 오염. 모든 게임이 비슷해지는 경고 신호 | 기술만 승격하고 값은 프로젝트에 남긴다 |
| 값을 여러 문서에 복사 | 정본이 둘이 되고 곧 어긋난다 | 위치를 가리킨다 |
| 모든 차이를 FAIL 로 만듦 | 검증이 디자인을 지배하기 시작한다 | `Required / Recommended / Informational` 로 나눈다 |
| 미정값을 임의 확정 (타일 32px, 팔레트 32색 등) | 가정이 사실로 굳는다 | 「가정」이라고 표시하고 후보로 제시 |
| 모든 판단을 사람에게 묻기 | 사람이 병목이 된다 | §6-4 조건이면 진행하고 기록으로 남긴다 |
| 승인 자산을 조용히 덮어쓰기 | 되돌릴 수 없다 | 새 후보로 만들고 근거와 함께 제시 |

---

## 11. 기계 판독용 요약

```yaml
repo: art-studio
kind: game-art-studio            # not a game, not an image generator, not an asset library
owner_decision_authority: human-director
language: ko
style_policy: no-fixed-style      # style is a property of each project
docs:
  constitution: CLAUDE.md
  rules: docs/01..11
  templates: templates/*.md
  auxiliary: [STUDIO_USAGE_CONTEXT.md, CAPABILITY_2D_ASSET_FACTORY.md]
  precedence: [CLAUDE.md+docs+templates, auxiliary, projects/<id>, README.md]

request_types: [DIAGNOSE, SPECIFY, PRODUCE, VALIDATE, HANDOFF]

lifecycle_states:
  source_axis: [CONCEPT, CANDIDATE, APPROVED]     # mutually exclusive, one at a time
  derived_axis: [EXPORT]                          # many targets can coexist
  parallel_input: [REFERENCE]
  judgement_flags: [REJECTED, ON_HOLD, SUPERSEDED]
  hard_rule: "generated != approved != engine-ready"

can:
  - reverse-engineer specs from mockups/screenshots (grid, palette, sizes, density)
  - draft ART_DIRECTION / STYLE_SPEC / ASSET_MANIFEST / ASSET_BRIEF
  - write generation orders and prompt blocks
  - organize candidates and build comparison contact sheets
  - validate dimensions, alpha, palette, frames, tiles, atlases, exports
  - post-process and batch-convert images
  - prepare engine handoff and review runtime screenshots
  - separate failure cause into Source / Export / Import / Engine
  - review game-design proposals from an art-readability standpoint
  - record decisions and promote reusable technique

cannot:
  - generate images itself            # no generator wired into this repo
  - decide aesthetics or approve assets
  - redesign game logic
  - transfer one project's style to another

tools:
  shared: [studio/tools/contact_sheet.py]
  deps: [python3, pillow]
  note: "images are gitignored; clone yields documents and code only"

companion_repos:
  - name: 2d-assets
    url: https://github.com/jungyh870918/2d-assets
    role: population-scale modular 2D generation (deterministic, seed-based)
    visibility: private
  - name: game-sandbox
    url: https://github.com/jungyh870918/game-sandbox
    role: measure consumer-side boundary of factory output
    visibility: private

division_of_labor: "art-studio decides and remembers; factories amplify; approval belongs to the human director"
```

---

## 12. 용어 대조표

| 한국어 | English | 뜻 |
|---|---|---|
| 후보 | candidate | 만들어졌지만 채택되지 않은 것 |
| 승인 | approved | 디렉터가 명시적으로 채택한 공식 원본 |
| 파생물 / 내보내기 | export | 승인 원본에서 엔진용으로 파생된 것 |
| 발주서 | asset brief / order | 이번에 무엇을 만들지 적은 문서 |
| 대조 시트 | contact sheet | 후보를 나란히 놓은 비교용 한 장 |
| 앵커 | anchor | 기준으로 삼는 레퍼런스 한 장 |
| 정본 | source of truth | 값의 유일한 출처 |
| 모집단 | population | 많고 다양해야 하는 자산군 |
| 정체성 | identity | 하나가 정확히 그것이어야 하는 자산 |
| 실루엣 | silhouette | 형태만으로 구분되는가 |
| 램프 | color ramp | 팔레트의 명암 계열 구조 |
| 규격 회수 | spec recovery | 목업/레퍼런스에서 수치를 측정해 되찾는 일 |
| 스타일 격리 | style isolation | 한 게임의 화풍이 다른 게임으로 번지지 않게 하는 것 |

---

## 부록 A. 새 팩토리를 등록하는 법

§7-1 표에 한 줄을 추가한다. 아래 6칸이 채워지지 않으면 등록하지 않는다.

```markdown
| # | <이름> — <한 줄 성격> | `<https 주소>`<br>`<ssh 주소>` | 공개/비공개 | <무엇을 하는가 — 입력과 출력> | <언제 쓰는가 — 모집단/정체성/검증/전달 중 어디> |
```

추가할 때 함께 판단할 것:

1. **이 팩토리는 결정하는가, 증폭하는가?** 결정한다면 승인 경계(§7-2)를 다시 그어야 한다.
2. **입력 계약이 무엇인가?** 화풍과 무관한 기술 계약으로 적는다 (§7-4 형식).
3. **스타일을 함께 들고 오는가?** 들고 온다면 모집단 전용으로 제한한다 (§7-5).
4. **승인을 무엇에 거는가?** 결정적 생성이면 `(해시 + 규칙 + seed)`, 아니면 파일 자체 (§7-6).
5. **비공개라면 그 사실을 표에 적는다.** 접근 권한 없는 에이전트가 헛도는 것을 막는다.

---

## 라이선스 · 사용 조건

**MIT License** — [`LICENSE`](LICENSE). 문서·도구·프로젝트 기록 전부에 동일하게 적용된다.

에이전트가 알아야 할 것만 추리면:

- **자유롭게 복사·수정·재배포·상업적 이용이 가능하다.** 저작권 표시와 라이선스 전문을 함께 남기면 된다.
- **보증은 없다.** 여기 적힌 수치·규격·판단은 특정 프로젝트의 맥락에서 나온 것이고, 다른 게임에서 그대로 맞는다는 보장이 없다 — 이 저장소가 §6 에서 스타일 격리를 강조하는 이유와 같다.
- **이 라이선스는 이 저장소의 내용물에만 적용된다.** 함께 쓰는 팩토리(§7)의 에셋은 각자의 라이선스를 따르며, 그중 상당수는 재배포와 생성 AI 입력을 금지한다. **팩 라이선스를 이 MIT 로 갈음하지 마라.**
- `projects/` 의 문서는 진행 중인 게임의 아트 결정 기록이다. 재사용은 허용되지만, **그 게임의 승인 자산이나 공식 방향으로 인용하지 마라.** 상태 어휘(§3)가 그 구분을 위해 있다.

## 이 README 의 갱신 규칙

- **팩토리가 추가될 때마다** §7-1 표에 한 줄이 늘어난다 (§부록 A).
- **`docs/` 와 이 README 가 다르게 읽히면 `docs/` 가 맞다.** 이 문서는 인터페이스 안내이지 규칙의 정본이 아니다.
- 구현이나 규약이 바뀌어 이 문서의 사실 설명이 틀리게 되면 **같은 변경 안에서 함께 고친다.**
