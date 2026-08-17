# 중간 기록 — tteoklak-island

- 프로젝트: 떡락섬 (`tteoklak-island`)
- 스냅샷 시점: **2026-08-17**
- 문서 성격: **진행 상황 스냅샷.** 정본이 아니다

<!--
결정과 그 근거는 STUDIO_DECISIONS.md 가, 규격은 brief/ 가, 판정은 reviews/ 가 갖는다.
여기 있는 것은 «지금 어디까지 왔고 무엇이 막혀 있는가» 하나뿐이다.
값을 여기에 복사하지 않는다 — 복사하면 정본이 둘이 된다.
-->

---

## 1. 지금 어디까지 왔나

**세 프로젝트 중 유일하게 그림이 실제 화면에 올라가 있다.**

```
D1~D6 잠정 결정          STUDIO_DECISIONS   완료
목업 UI 전수 감사         MOCKUP_UI_AUDIT    완료 — 31종
파생 규격표              CANVAS_DERIVATION  완료
배경 후보 2장            황소항 · 심야지하철  완료 (장면당 1장씩만)
세로 셸 구현 · 판정       STUDIO_VERDICT     완료 — 942×1674 승인
배경 2장 게임 통합        subway-integration 완료 — 핫스폿 전부 제자리
초상 발주서 · 프롬프트     ORDER · PROMPTS    완료 — **생성 대기**
```

**막고 있는 것은 판단이 아니라 손이다** — 초상 1단계 프롬프트 5블록이 조립까지 끝나 있고,
**이 세션에 이미지 생성 수단이 없어서** 사람이 도구에 붙여야 다음 칸으로 간다.

---

## 2. 확정된 것

| | 값 · 결정 | 근거 |
|---|---|---|
| **D1 기준 캔버스** | **942×1674** (World 층만. UI 는 기기 해상도) | `STUDIO_DECISIONS` §2 · `STUDIO_VERDICT` §2 |
| **D2 세로 전환** | **세로 전용.** 배경은 한 벌만 그린다. 가로는 테두리 두른 스테이지로 | `STUDIO_DECISIONS` §3 |
| 배경 규격 | **1024×1418** — 비율은 맞다. **여유를 0으로 만들지 않는다** | `STUDIO_VERDICT` §0-B |
| 배경 후보 수 | 장면당 **4장** | `STUDIO_DECISIONS` §7 |
| **윤세라 외형** | **목업이 정본.** 다만 이긴 범위는 **외형뿐** — 이름 표기와 인물 배정은 데이터가 맞다 | 디렉터 결정 · `STUDIO_DECISIONS` §6 |
| **초상 규격** | 발주 **252×252** · 전달 **189×189** (63 설계px × 3) | `ORDER_PORTRAITS` §1 |
| 초상 범위 | **5명 15표정** — 한개미 4 · 브로커 4 · 세라 3 · 부장 2 · 박프로 2 | `ORDER_PORTRAITS` §2 |
| 상단 바 오른쪽 | 「대화 기록」 | `STUDIO_VERDICT` §0-D |

> **189 는 반올림하지 않은 값이다.** 188 은 4의 배수로 맞춘 것이었고 그 관행이 여기서는 틀렸다 —
> **UI 층은 4가 아니라 설계 픽셀 정수에 맞춘다.** 목업 실측 189×189 와 정확히 일치한다.

---

## 3. 열려 있는 것

| | 무엇 | 언제 닫히나 | 지금 막나 |
|---|---|---|---|
| **D3 · D4** | 캐릭터 제작 방식과 프레임 수 | **배경이 올라간 화면에서 인물이 몇 px 로 보이는지** 재고 나서. 판단 재료가 이미 두 장면 생겼다 | 스프라이트 145프레임을 막는다 |
| ⚠ **D5** | 수첩 흉상을 도트로 둘 것인가 | **디렉터 확인 필요.** 수첩 착수 전 (한참 뒤) | 지금은 안 막는다 |
| 배경 4장 | 회의실 · 복도 · 탕비실 · 원룸 | 주문서는 여섯 장 다 작성돼 있다. 생성만 남았다 | — |
| 배경 재수령 | 황소항 · 심야지하철 **각 3~4장** | 지금 각 1장뿐이라 **고를 것이 없다** | — |

> **D5 가 이 프로젝트에서 가장 약한 결정이다.** 목업 04 수첩 한 화면 안에 회화체 반신과
> 도트 흉상이 공존한다. Studio 는 「생성 잡음」으로 읽었지만, **「종이에 붙인 것」이라는 은유 때문에
> 의도적으로 거칠게 갈 이유도 있다.** 뒤집는 비용은 지금 0 이다.

**§6 윤세라(구 ⚠A)는 닫혔다.** 디렉터가 목업으로 결정했고 보류가 풀렸다.

---

## 4. 다음 한 걸음

1. **초상 1단계 생성** — [`brief/PROMPTS_PORTRAITS.md`](brief/PROMPTS_PORTRAITS.md) 의 5블록을
   **그대로 복사해** 붙인다. 손으로 고쳐 쓰지 않는다 (R3)
   - **인물 하나 = 새 대화 하나** (R4) · **매 대화마다 `references/02_dialogue.png` 첨부** (R2 — 필수)
   - 받은 것은 `candidates/portraits/<id>/` 에 넣는다. 폴더는 이미 만들어져 있다
2. **1단계는 얼굴만 정한다.** 표정은 고른 얼굴을 앵커로 2단계에서 파생시킨다 —
   표정마다 따로 4장씩 받으면 같은 사람으로 안 보이는 문제가 재발한다
3. 배경 나머지 4장 + 기존 2장 재수령
4. 배경이 올라간 화면에서 **인물 실측** → D3 · D4 결정
5. UI 아이콘·장식은 **시트 단위**로 받는다 (개별 왕복이 병목이 된다)

---

## 5. 겪어 둔 것

- **배경 통합은 눌러 넣으면 실패한다.** `background-integration` 에서 셋 다 실패했고,
  64px 격자를 씌워 원본 픽셀로 읽고 잘라내기 수식을 비율로 환산하는 절차로 통과했다
- **`27_harbor_hotspots.png` 같은 캡처가 이 프로젝트에서 가장 값싼 검증이다** —
  그림 위에 판정 상자를 겹쳐 보여주는 것. 배경 장면마다 짝으로 낸다
- **목업 생성기가 지어낸 숫자가 있다.** 수첩의 「3 / 18」은 받쳐 주는 시스템이 게임에 없다.
  증거 썸네일 18종은 **발주 대상이 아니다**
- **표정 목록은 추출이 아니라 설계다.** `data/dialogues/` 에 emotion·expression 필드가 없다
- **정적 핫스폿은 배경에 그린다.** 지하철의 「조는 승객」이 그 예다 — Actor 가 아니다

---

## 6. 문서 지도

| 무엇 | 어디 |
|---|---|
| **잠정 결정 D1~D6** | [`STUDIO_DECISIONS.md`](STUDIO_DECISIONS.md) |
| 제작 전략 | [`PRODUCTION_STRATEGY.md`](PRODUCTION_STRATEGY.md) |
| 게임 쪽 질문 | [`QUESTIONS_TO_STUDIO.md`](QUESTIONS_TO_STUDIO.md) · [`REQUEST_TO_DIRECTOR.md`](REQUEST_TO_DIRECTOR.md) |
| 게임 소개 · 아트 방향 | [`brief/PROJECT_BRIEF.md`](brief/PROJECT_BRIEF.md) · [`brief/ART_DIRECTION.md`](brief/ART_DIRECTION.md) |
| 자산 목록과 상태 | [`brief/ASSET_MANIFEST.md`](brief/ASSET_MANIFEST.md) |
| 파생 규격표 | [`brief/CANVAS_DERIVATION.md`](brief/CANVAS_DERIVATION.md) |
| 목업 UI 감사 31종 | [`brief/MOCKUP_UI_AUDIT.md`](brief/MOCKUP_UI_AUDIT.md) |
| **초상 발주서** | [`brief/ORDER_PORTRAITS.md`](brief/ORDER_PORTRAITS.md) |
| **붙여넣을 프롬프트** | [`brief/PROMPTS_PORTRAITS.md`](brief/PROMPTS_PORTRAITS.md) |
| 세로 셸 판정 | [`reviews/2026-08-17_portrait-shell/STUDIO_VERDICT.md`](reviews/2026-08-17_portrait-shell/STUDIO_VERDICT.md) |
| 배경 통합 기록 | [`reviews/2026-08-17_subway-integration/README.md`](reviews/2026-08-17_subway-integration/README.md) |
