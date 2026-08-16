# 03. Project Structure

이 문서는 Art Studio가 **여러 게임 프로젝트와 공통 제작 도구를 어떤 구조로 분리하고 관리하는가**를 정의한다.

앞의 두 문서가 "이 스튜디오는 무엇인가"와 "누가 무엇을 결정하는가"를 다뤘다면, 이 문서는 그 원칙이 **파일과 디렉터리 위에서 어떻게 유지되는가**를 다룬다.

이미지 생성 절차, 승인 절차, 에셋 상태 정의, 엔진별 export 규격은 이 문서의 주제가 아니다. 여기서는 **경계**만 정한다.

---

## 1. 이 문서가 답해야 하는 질문

- 스튜디오 자체의 파일과 게임별 파일은 어떻게 분리하는가
- 여러 게임의 아트셋이 서로 섞이지 않게 하려면 어떻게 하는가
- 공통 도구와 프로젝트 전용 자료의 경계는 어디인가
- 레퍼런스 · 컨셉 · 후보 · 승인본 · export는 어떤 개념으로 나뉘는가
- 실제 게임 저장소와 Art Studio 작업 공간은 어떤 관계인가
- 새 게임이 들어오면 무엇을 만드는가
- 어디까지 공통화하고 어디부터 격리하는가

---

## 2. 구조의 기본 축

Art Studio의 구조는 세 영역으로 나뉜다.

```text
ART STUDIO
│
├── studio      공통 제작 능력 — 여러 게임에서 재사용되는 기술
├── projects    게임별 아트 작업 공간 — 게임마다 격리되는 정체성
└── templates   새 프로젝트에 복제해 쓰는 문서 골격
```

핵심 원칙은 하나다.

> **공통 제작 능력과 게임별 아트 정체성을 분리한다.**

기술 · 스크립트 · 제작 방법은 공통 영역에 쌓인다.
스타일 · 레퍼런스 · 컨셉 · 후보 · 승인 자산은 해당 게임 안에 머문다.

이 분리는 파일 정리 취향이 아니라, `01_STUDIO_IDENTITY`의 "스타일은 스튜디오가 아니라 프로젝트의 속성"이라는 원칙을 디스크 위에서 유지하기 위한 장치다.

---

## 3. 최상위 구조

초기에는 이 정도로 단순하게 유지한다.

```text
art-studio/
├── CLAUDE.md
│
├── docs/
│   ├── 01_STUDIO_IDENTITY.md
│   ├── 02_DIRECTOR_RELATIONSHIP.md
│   ├── 03_PROJECT_STRUCTURE.md
│   ├── 04_ART_DIRECTION_SYSTEM.md
│   ├── 05_TOOL_ROLES.md
│   ├── 06_ASSET_LIFECYCLE.md
│   ├── 07_GENERATION_WORKFLOW.md
│   ├── 08_REVIEW_AND_APPROVAL.md
│   ├── 09_ASSET_SPEC_AND_VALIDATION.md
│   ├── 10_ENGINE_HANDOFF.md
│   └── 11_LEARNING_AND_REUSE.md
│
├── studio/
│   ├── tools/
│   ├── workflows/
│   ├── exporters/
│   └── shared/
│
├── templates/
│   ├── PROJECT_BRIEF.md
│   ├── ART_DIRECTION.md
│   ├── STYLE_SPEC.md
│   ├── ASSET_MANIFEST.md
│   ├── ASSET_BRIEF.md
│   └── REVIEW_LOG.md
│
└── projects/
```

이 문서는 **구조 원칙**을 정의하는 것이지 폴더 생성을 지시하는 것이 아니다.
아직 내용이 없는 폴더를 미리 다 만들어 둘 필요는 없다. 실제로 무언가를 넣을 때 만든다.

`docs/`와 `templates/`의 문서는 현재 모두 존재한다. `studio/` 아래의 하위 폴더와 `projects/`의 내용은 실제 작업이 생길 때 만든다.

---

## 4. `docs/`

**Art Studio 자체의 운영 원칙**을 저장한다.

여기에는 특정 게임의 아트 방향이 들어가지 않는다. `docs/` 아래의 어떤 문장도 "어느 게임에서만 참인 규칙"이어서는 안 된다.

현재 다음 운영 문서가 이 영역에 있다.

```text
01_STUDIO_IDENTITY          이 저장소는 무엇인가
02_DIRECTOR_RELATIONSHIP    누가 무엇을 결정하는가
03_PROJECT_STRUCTURE        파일 위에서 어떻게 분리하는가
04_ART_DIRECTION_SYSTEM     아트 방향을 어떤 언어로 이해하는가
05_TOOL_ROLES               어떤 도구를 어떤 문제에 쓰는가
06_ASSET_LIFECYCLE          이 결과물은 지금 어떤 상태인가
07_GENERATION_WORKFLOW      실제 제작은 어떤 순서로 진행하는가
08_REVIEW_AND_APPROVAL      무엇을 검토하고 누가 승인하는가
09_ASSET_SPEC_AND_VALIDATION  기술 규격을 어떻게 검사하는가
10_ENGINE_HANDOFF           승인 자산을 게임으로 어떻게 전달하고 확인하는가
11_LEARNING_AND_REUSE       무엇을 공통 지식으로 남기는가
```

게임별 문서는 `docs/`가 아니라 해당 프로젝트의 `brief/`에 둔다.

---

## 5. `studio/`

여러 게임에서 반복해 쓸 수 있는 **공통 제작 능력**이 쌓이는 영역이다.

```text
studio/
├── tools/
├── workflows/
├── exporters/
└── shared/
```

각 영역의 의미만 정의하고, 세부 하위 구조는 실제 도구가 생길 때 결정한다.

### `studio/tools/`

반복 사용 가능한 기술 도구와 스크립트를 둔다.

> 이미지 크기 검사 · 알파 검사 · 팔레트 분석 · 배경 제거 · 이미지 변환 · sprite sheet 처리 · tile 검사 · 파일명 검사 · 포맷 변환 · batch processing

여기에 **특정 게임의 스타일을 코드에 박아 넣지 않는다.** 타일 크기, 팔레트 수, 캐릭터 높이 같은 값은 인자나 프로젝트 설정으로 받는 쪽이 맞다. 기본값이 필요하더라도 그것이 특정 게임의 규격이 되어서는 안 된다.

### `studio/workflows/`

반복해 쓸 가치가 있는 제작 절차와 보조 스크립트를 둔다.

> 후보 이미지 정리 · review sheet 생성 · 생성 결과 수집 · 이미지 비교 · batch export

워크플로우는 모든 프로젝트에 강제되는 고정 파이프라인이 아니다.
필요한 프로젝트가 선택적으로 꺼내 쓰는 제작 능력으로 본다.

### `studio/exporters/`

승인된 자산을 특정 엔진이나 환경에서 쓸 수 있도록 변환하는 공통 기능을 둔다.

> Unity · Godot · Roblox · Web

엔진별 전달 규칙 자체는 `10_ENGINE_HANDOFF.md`가 정의한다. 여기에는 그 규칙을 실행하는 수단만 둔다.

### `studio/shared/`

게임에 종속되지 않는 공용 자료를 둔다.

> 공통 제작 참고 자료 · 범용 prompt 구조 · 색상 분석용 데이터 · 공용 테스트 이미지 · 제작 실험 결과 · 범용 기술 레퍼런스

경계는 분명하다.
**특정 게임의 화풍이나 팔레트를 공용 규칙처럼 저장하지 않는다.** 어떤 자료가 "게임 A에서는 이렇게 했다"는 사례라면 그것은 사례로 표시되어야 하며, 스튜디오의 기본값처럼 놓이지 않는다.

---

## 6. `templates/`

새 게임을 Art Studio에 등록할 때 복제해 쓰는 **문서 골격**을 둔다.

```text
templates/
├── PROJECT_BRIEF.md      이 게임은 무엇인가
├── ART_DIRECTION.md      이 게임은 어떻게 보여야 하는가
├── STYLE_SPEC.md         반복 제작을 위한 기술 규칙
├── ASSET_MANIFEST.md     무엇이 필요하고 지금 어디까지 왔는가
├── ASSET_BRIEF.md        이번 자산을 어떻게 만드는가
└── REVIEW_LOG.md         무엇을 왜 채택·반려했는가
```

템플릿은 실제 게임 데이터를 담지 않는다. 예시 값을 적더라도 그것이 다음 프로젝트의 기본값으로 굳지 않도록 한다.
각 템플릿의 항목 구성은 템플릿 파일 자체가 가지고 있고, 무엇이 어느 문서에 속하는가는 `04_ART_DIRECTION_SYSTEM.md`가 정의한다. 이 문서는 **템플릿이 놓이는 자리**만 정한다.

---

## 7. `projects/`

게임별 아트 작업의 핵심 영역이다. 각 게임은 독립된 디렉터리를 가진다.

```text
projects/
├── game-a/
├── game-b/
└── game-c/
```

다음 정보는 반드시 게임별로 분리된다.

> 게임 설명 · 아트 방향 · 레퍼런스 · 스타일 규격 · 컨셉 · 생성 후보 · 승인 자산 · export 결과 · 리뷰 기록 · 제작상의 특이사항

한 게임의 폴더만 열어도 그 게임의 아트 상태를 파악할 수 있어야 하고, 다른 게임의 폴더를 열지 않아도 작업이 가능해야 한다.

---

## 8. 게임별 기본 구조

게임 디렉터리는 다음 개념을 기본으로 삼는다.

```text
projects/<project-id>/
├── brief/         무엇을 어떤 방향으로 만드는가
├── references/    참고 자료
├── concepts/      탐색 결과
├── candidates/    채택 가능성이 있는 후보
├── approved/      디렉터가 채택한 공식 원본
├── exports/       엔진용 파생물
└── reviews/       비교와 판단을 위한 자료
```

이 형태를 절대적으로 강제하지 않는다.
프로젝트 성격에 따라 일부는 생략되고 일부는 추가된다. 레퍼런스가 필요 없는 작업도 있고, export 대상이 아직 없는 단계도 있다.

**유지해야 하는 것은 폴더 개수가 아니라 각 폴더가 나타내는 상태의 차이다.**

---

## 9. `brief/`

Art Studio가 그 게임을 이해하기 위해 필요한 상위 정보를 둔다.

```text
brief/
├── PROJECT_BRIEF.md
└── ART_DIRECTION.md
```

`STYLE_SPEC.md`, `ASSET_MANIFEST.md`, 자산별 `ASSET_BRIEF_<asset>.md`도 이 영역에 놓인다. 프로젝트에 필요해진 시점에 템플릿을 복제해 만든다.

이 폴더의 목적은 하나다.

> **이 게임에서 무엇을 만들고, 어떤 방향으로 만들어야 하는지 설명하는 것.**

`brief/`가 비어 있는 프로젝트는 방향 없이 후보만 쌓이기 쉽다.

---

## 10. `references/`

참고 자료를 저장한다.

> 디렉터가 제공한 이미지 · 게임 스크린샷 · 스타일 레퍼런스 · 시대 고증 자료 · 의상 참고 · 건축 참고 · 기존 게임의 승인 화면 · 외부 레퍼런스

레퍼런스는 공식 자산이 아니다.
그리고 **여기에 저장되었다는 사실이 그 이미지를 복제 대상으로 만들지 않는다.** 레퍼런스의 역할은 방향의 이해와 분석이다.

같은 프로젝트 안에서도 "외부에서 가져온 참고물"과 "이 게임이 이미 승인한 자산"은 구분해 두는 편이 좋다. 후자는 `approved/`에 있는 것이 원칙이며, 참고 목적으로 `references/`에 사본을 둔다면 그것이 원본이 아님을 알 수 있어야 한다.

---

## 11. `concepts/`

아직 최종 자산이 아닌 **탐색용 결과물**을 둔다.

> 스타일 탐색 · 실루엣 · 초기 디자인 · 분위기 시안 · 색상 탐색 · 맵 비주얼 스케치 · 형태 연구

`concepts/`는 방향을 찾는 단계의 산출물이고, `candidates/`는 특정 자산을 만들려는 시도의 산출물이다. 둘 다 승인 자산과 분리된다.

---

## 12. `candidates/`

실제 자산으로 채택될 가능성이 있는 후보를 둔다. 보통 자산 단위로 묶는다.

```text
candidates/
└── goblin_spearman/
    ├── a.png
    ├── b.png
    └── c.png
```

원칙은 명확하다.

> **candidate는 만들어졌다는 뜻이지 승인되었다는 뜻이 아니다.**

생성 도구가 출력했다는 사실은 승인 근거가 되지 않는다. 결과가 아무리 좋아 보여도 디렉터의 채택 없이는 후보 상태다.

후보를 지우는 판단도 여기서 하지 않는다(→ 27장).

---

## 13. `approved/`

디렉터가 명시적으로 채택한 **공식 원본 자산**을 둔다.

`approved/`는 잘 나온 후보의 보관소가 아니다. 여기 있는 것은 현재 그 게임 아트의 공식 기준으로 취급된다.

동시에 다음을 구분한다.

> **approved source와 engine-ready export는 같지 않을 수 있다.**

승인된 고해상도 원본에서 Unity용 PNG, Roblox용 텍스처, sprite atlas가 각각 파생될 수 있다. 승인된 것은 원본이지 특정 엔진용 파일이 아니다.

승인 상태의 변경은 디렉터의 권한이며, 그 절차는 `08_REVIEW_AND_APPROVAL.md`가 정의한다. 상태 자체의 의미는 `06_ASSET_LIFECYCLE.md`가 정의한다.

---

## 14. `exports/`

승인 원본을 실제 게임 환경에 전달하기 위해 가공한 결과를 둔다.

```text
exports/
├── unity/
├── godot/
├── roblox/
└── web/
```

하위 구조는 실제로 쓰는 엔진에 따라 만든다. 쓰지 않는 엔진 폴더를 미리 만들지 않는다.
모든 프로젝트가 같은 엔진을 쓴다고 가정하지 않으며, 한 프로젝트가 여러 엔진을 동시에 대상으로 할 수도 있다.

`exports/` 안의 파일은 언제나 **파생 결과물**이다. 필요하면 다시 생성할 수 있는 상태를 유지하고, 원본은 `approved/`에 보존한다.

---

## 15. `reviews/`

디렉터가 비교하고 판단하기 위한 자료를 둔다.

> candidate comparison sheet · contact sheet · 실제 게임 화면 캡처 · before/after 비교 · 리뷰용 HTML · 주요 피드백 기록

리뷰 자료는 대체로 파생물이며, 판단을 돕기 위한 임시 자료일 수도 있다.
다만 **중요한 결정의 근거가 된 자료**는 임시물로 취급하지 않는다.

검토와 승인의 판단 기준은 `08_REVIEW_AND_APPROVAL.md`가, 기록 형식은 `templates/REVIEW_LOG.md`가 정의한다.

---

## 16. 원본과 파생물의 방향

가능한 경우 다음 관계를 유지한다.

```text
SOURCE
  ↓
APPROVED SOURCE
  ↓
DERIVED EXPORT
```

```text
approved/hero.png
        ↓
exports/unity/hero.png
exports/roblox/hero.png
```

Unity용 export를 직접 수정해 그것을 새 원본으로 삼지 않는다.
수정이 필요하면 승인 자산이나 그 이전 source 단계에서 바꾸고 다시 파생시키는 것을 우선한다.

이 방향이 무너지면 어떤 파일이 진짜 원본인지 알 수 없게 되고, 그때부터 구조는 아무것도 보증하지 못한다.

---

## 17. 게임 저장소와 Art Studio 작업 공간

`projects/<project-id>/`는 실제 게임 저장소와 같은 위치일 필요가 없다.

```text
게임 저장소            ~/games/age-rush/
Art Studio 작업 공간   art-studio/projects/age-rush/
```

두 저장소의 역할은 다르다.

```text
게임 저장소                  Art Studio
──────────                  ──────────
게임 코드                    레퍼런스
씬                          컨셉
게임 데이터                  후보
실제로 사용되는 최종 자산      아트 제작 과정
                            승인 원본
                            export 준비
                            리뷰 자료
```

둘 사이에 연결이나 export 절차를 만들 수 있다.
다만 **Art Studio가 게임 저장소 전체를 복제하거나 흡수하는 구조를 기본값으로 삼지 않는다.**

`CLAUDE.md`의 「외부 게임 프로젝트를 다룰 때」에서 정한 대로, 게임 저장소 쪽 파일을 다루는 작업은 아트 작업이라는 이유만으로 확대되지 않는다. 실제 전달 절차는 `10_ENGINE_HANDOFF.md`가 다룬다.

---

## 18. 외부 게임 프로젝트와의 연결

게임 저장소 경로가 필요하면 프로젝트 설정이나 별도 문서에서 연결 정보를 관리한다.

```text
game repository:
~/games/example-game/

art workspace:
art-studio/projects/example-game/
```

연결 형식은 이 문서에서 확정하지 않는다. 중요한 것은 하나다.

> **Art Studio의 프로젝트 ID와 실제 게임 저장소의 위치는 별개의 개념이다.**

게임 저장소가 옮겨지거나 엔진이 바뀌어도 Art Studio 구조 전체가 무너지지 않아야 한다.

---

## 19. 프로젝트 ID

게임 디렉터리는 안정적인 ID를 쓴다. 권장 형태는 단순한 소문자 kebab-case다.

```text
age-rush
dice-dominion
hometown-clash
maze-zombie
```

게임 이름이 바뀌어도 내부 ID는 함부로 바꾸지 않는 편이 좋다. ID는 표시용 이름이 아니라 참조용 키에 가깝다.

지금 단계에서 별도의 ID 정책이나 메타데이터 시스템을 복잡하게 만들지 않는다.

---

## 20. 스타일 격리

이 구조의 가장 중요한 목적 중 하나는 파일 정리가 아니라 **스타일 오염 방지**다.

```text
projects/game-a/references/
projects/game-a/approved/
```

이 내용은 `game-b` 작업에서 자동으로 참고되지 않는다.
다른 프로젝트의 자료를 가져와야 한다면 그럴 만한 명시적인 이유가 있어야 하고, 그 사실이 드러나야 한다.

> 공통 도구는 공유한다.
> 게임별 미적 결정은 공유하지 않는다.

---

## 21. 무엇이 공통 영역으로 올라갈 수 있는가

`studio/`로 승격될 수 있는 것.

> 범용 이미지 검사기 · sprite sheet generator · palette analyzer · file converter · contact sheet generator · Unity/Godot export helper · 생성기 연결 코드 · 범용 prompt assembly 기술

기본적으로 프로젝트 안에 남는 것.

> 특정 게임의 prompt · palette · 캐릭터 디자인 규칙 · 레퍼런스 · 승인 에셋 · 스타일 설정

구분 기준은 단순하다. **그것을 다른 게임에 그대로 적용했을 때 이상해지는가.**
이상해진다면 그것은 스타일이고 프로젝트에 남는다.

---

## 22. 공통화는 반복이 확인된 뒤에 한다

처음부터 모든 것을 `studio/`로 추상화하지 않는다.
한 프로젝트에서 한 번 쓴 방법은 우선 그 프로젝트에 남아 있어도 된다.

여러 프로젝트에서 반복되고, 프로젝트 스타일에 종속되지 않으며, 범용적으로 유용하다는 것이 확인되면 그때 승격한다.

> **미리 공통화하지 말고, 반복이 확인되면 공통화한다.**

한 번 쓰인 코드를 공용 도구로 올리면, 아직 검증되지 않은 방식이 스튜디오의 기본값처럼 보이게 된다.

---

## 23. 생성기 중심 구조를 만들지 않는다

다음과 같은 구조를 기본으로 삼지 않는다.

```text
flux/
chatgpt/
pixellab/
retro-diffusion/
```

구조의 중심은 도구가 아니라 **게임과 자산**이기 때문이다.
같은 캐릭터가 여러 생성기를 거칠 수 있고, 도구는 프로젝트보다 훨씬 빨리 바뀐다.

기본 축은 다음과 같다.

```text
게임 → 자산 → 상태
```

어떤 도구로 만들었는지는 metadata나 기록으로 남긴다. 무엇을 어느 수준까지 남길지는 `07_GENERATION_WORKFLOW.md`가, 중요한 결정의 기록 형식은 `templates/REVIEW_LOG.md`가 다룬다.

---

## 24. 자산 종류별 고정 구조도 미리 강제하지 않는다

초기부터 이런 깊이를 강제하지 않는다.

```text
characters/
monsters/
weapons/
props/
buildings/
tiles/
ui/
vfx/
portraits/
```

자산 수가 늘고 필요성이 생기면 하위 디렉터리를 추가한다.

```text
approved/
├── characters/
├── monsters/
└── environment/
```

모든 프로젝트가 같은 자산 종류를 갖는다고 가정하지 않는다. 타일이 없는 게임도 있고, 초상화만 필요한 작업도 있다.
소규모 게임에까지 동일한 거대 구조를 강요하지 않는다.

---

## 25. 구조는 작업을 돕기 위해 존재한다

폴더 규칙을 지키는 일이 좋은 아트를 만드는 일보다 중요해지면 안 된다.

구조가 보장해야 하는 것은 이 정도다.

- 찾기 쉽다
- 섞이지 않는다
- 원본을 잃지 않는다
- 승인 여부를 알 수 있다
- 다른 게임의 스타일이 침범하지 않는다
- 도구가 안전하게 작업할 수 있다
- 반복 작업을 자동화하기 쉽다

이를 넘어서는 복잡성은 필요가 확인되기 전까지 추가하지 않는다.

---

## 26. 새 게임이 들어왔을 때

새 게임이 등록되면 기본적으로 다음을 만든다.

```text
projects/<project-id>/
```

그 안에 최소한 `PROJECT_BRIEF`와 `ART_DIRECTION`이 존재하는 상태를 목표로 한다. 이 둘이 없으면 이후의 모든 후보가 근거 없이 만들어진다.
레퍼런스가 이미 있다면 `references/`에 둔다.

나머지 폴더는 실제 제작이 시작되면서 필요할 때 추가한다.
모든 폴더를 빈 상태로 미리 만드는 것은 필수가 아니다.

`ART_DIRECTION`이 아직 비어 있다면 그것은 채워야 할 항목이지, Claude가 임의로 확정해도 된다는 뜻이 아니다.

---

## 27. 삭제와 정리

AI 기반 작업은 임시 결과물을 많이 만든다. 그렇다고 오래된 후보를 자동으로 삭제하지 않는다.

특히 다음은 명시적인 이유 없이 삭제하지 않는다.

- approved 자산
- 원본 source
- 디렉터가 비교 대상으로 남긴 candidate
- 주요 reference
- 중요한 리뷰 기록

명백한 임시 캐시나 중복 파일은 별도 정책이 정해지면 정리할 수 있다.
삭제 정책의 세부사항은 이 문서에서 확정하지 않는다.

---

## 28. 버전 관리에 대한 기본 태도

이 저장소가 Git을 사용한다면 구조가 버전 관리에 적합한 상태를 유지한다.

다음은 이 문서에서 확정하지 않는다.

- 대용량 이미지의 Git LFS 사용 여부
- generated asset의 commit 정책
- 브랜치 전략
- binary versioning
- cloud asset storage

실제 프로젝트 규모와 필요에 따라 별도로 결정한다.

---

## 29. 이 문서가 다루지 않는 것

```text
아트 방향을 어떤 속성으로 정의하는가            04_ART_DIRECTION_SYSTEM.md
어떤 도구를 어떤 작업에 쓰는가                  05_TOOL_ROLES.md
asset lifecycle의 상태 정의                    06_ASSET_LIFECYCLE.md
이미지 생성 workflow                          07_GENERATION_WORKFLOW.md
candidate가 approved가 되는 절차 · 리뷰와 승인 규칙   08_REVIEW_AND_APPROVAL.md
기술 검증 규칙 · asset naming의 세부 규칙        09_ASSET_SPEC_AND_VALIDATION.md
엔진별 export 규격                            10_ENGINE_HANDOFF.md
프로젝트 경험을 공통 노하우로 승격하는 세부 기준   11_LEARNING_AND_REUSE.md
manifest 형식                                templates/ASSET_MANIFEST.md
```

이 문서는 **구조적 경계**만 정의한다.

---

## 30. 핵심

> Art Studio는 공통 제작 능력과 게임별 아트 정체성을 분리한다.
>
> `studio/`에는 재사용 가능한 기술이 쌓이고, `projects/`에는 각 게임의 스타일과 제작 결과가 격리된다.
>
> 생성 후보와 승인 원본, 승인 원본과 엔진용 파생물을 구분한다.
>
> 구조는 프로젝트를 통제하기 위한 것이 아니라, 여러 게임을 안전하고 명확하게 다루기 위한 최소한의 질서다.
>
> 필요가 확인되기 전에 구조를 복잡하게 만들지 않는다.
