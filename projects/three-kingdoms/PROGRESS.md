# 중간 기록 — three-kingdoms

- 프로젝트: 삼국지 III — 웹 오마주 (`three-kingdoms`)
- 스냅샷 시점: **2026-08-17 22:10** (게임 저장소 `2b3d4e7` 까지 대조)
- 문서 성격: **진행 상황 스냅샷.** 정본이 아니다

<!--
이 문서는 판단을 담지 않는다. 판단은 REQUEST_TO_DIRECTOR · HANDOFF_TO_GAME_NN ·
reviews/ 안의 검토 본문이 갖는다. 규격은 brief/ 가 갖는다.
여기 있는 것은 «지금 어디까지 왔고 무엇이 막혀 있는가» 하나뿐이다.
값을 여기에 복사하지 않는다 — 복사하면 정본이 둘이 된다.
-->

---

## 1. 지금 어디까지 왔나

**규격 회수 → 판단 요청 → 좌표판 4회 왕복.** 앵커(수직 슬라이스)는 아직 착수하지 않았다.

```
목업 4장 측정          FINDINGS      완료 — 「목업은 픽셀 아트가 아니다」 확정
발주 판단 요청          REQUEST       완료 — Q1~Q11 제출
좌표판 D1~D4 검토       회신 03       완료
좌표판 D5·D6 검토       회신 04       완료 — ㉳(D6) 채택 «권고». 게임 저장소에 전달됨
앵커 제작              —             미착수. Q1 대기
```

**승인된 화면 자산은 0개다.** 후보도 아직 없다. `ASSET_MANIFEST` 가 거의 전부 `—` 인 것이
현재로서는 정확한 상태다.

**회신 04 이후 게임 쪽이 세 커밋을 냈고, 그중 하나가 대기 항목을 하나 닫았다** —
`919aa2c` 인물 삽화 파이프라인 · 깃발색 겹침 수정 · `b6e4607` 검사기 주석 ·
**`2b3d4e7` 원화 git-lfs 보관**. 아직 «회신 04 에 대한 답»(보고 05)은 오지 않았다.

---

## 2. 닫힌 것

게임 쪽 확인 또는 측정으로 답이 나와 **다시 묻지 않는 항목**이다.

| | 답 | 자리 |
|---|---|---|
| Q7 마커 크기 | **78×80** (회화 흉상은 60에서도 견딘다) | `brief/ASSET_MANIFEST.md` |
| Q9 두 글자 성 | 公孫·司馬·毌丘는 충돌 그룹이 아니다. **실제 충돌은 劉袁張韓 넷뿐** | `brief/IDENTIFICATION_SYSTEM.md` |
| Q10 명령 갈래 | **8갈래.** 목업의 6에는 정보·특별이 빠져 있다 | `brief/ASSET_MANIFEST.md` §1-1 |
| 보물 17종 | 글자로만 표시한다. 아이콘 요청 없음 | 같은 곳 |
| 특성 아이콘 | **범위에서 내림.** 데이터가 없고 넣을 계획도 없다 | 같은 곳 |
| 전투 격자 성격 | **정사각 top-down.** 등각이 아니다 | `brief/STYLE_SPEC.md` §9-1 |
| 성채 기본형 | 규모 3 × 지형 3 중 **실제 조합 8** | `brief/ASSET_MANIFEST.md` |
| 세력색 런타임 버그 | `alive:false` 잔류가 원인. `Events.clanColor(st)` 로 해결 — **게임 `919aa2c` 로 반영됨** | `brief/IDENTIFICATION_SYSTEM.md` §1-2 |
| **원화 보관** | **git-lfs 로 확정** (게임 `2b3d4e7`). 원화 22장 56MB · 181명이면 약 450MB. GitHub 무료 몫(저장 1GB · 월 전송 1GB)에 닿을 무렵 다시 정한다 | 게임 `.gitattributes` · `.gitignore` 주석 |

**측정으로 확정된 값** — 종횡비 **1.28** (16 시나리오 합 19쌍 · 190년 4쌍, 전부 78px 문턱 아래).

---

## 3. 열려 있는 것 — 디렉터 대기

**하나가 나머지 순서를 정한다.**

| | 무엇 | 왜 막혀 있나 |
|---|---|---|
| **1** | **지도 표시 방식 ㉠~㉳** | Studio 권고는 ㉳(D6 · 수도 20 얼굴 + 점 47). **얼굴의 뜻이 「태수」에서 「군주」로 바뀌는 것은 게임 쪽 결정**이라 Studio 가 정하지 않는다 |
| 2 | 세력 식별 체계 · 팔레트 | **1번이 ㉳ 이면 성격이 바뀐다** — 47개 도시가 14px 색점 하나에 걸리므로 팔레트 재설계가 P0 로 올라간다 |
| ~~3~~ | ~~원화 보관 (git-lfs)~~ | **닫혔다 (2026-08-17).** 게임이 `2b3d4e7` 로 git-lfs 를 택했다 → §2 |
| 4 | **Q1 논리 해상도 A·B·C** | 이 발주 전체에서 가장 종속이 많은 값. ㉳ 이면 2번보다 먼저 와야 한다 |
| 5 | 전투 격자 16×9 | 세로 화면에 안 들어간다. **아트 결정이 아니라 게임 설계 결정** |
| 6 | 착수 승인 | 「190년 식별 시트」는 **자산 0 으로 지금 만들 수 있다** |

> **㉳ 을 고르면 1 → 4 → 2 순서,  ㉲ 를 고르면 지금 순서 그대로다.**
> 근거: [`HANDOFF_TO_GAME_04.md`](HANDOFF_TO_GAME_04.md) §6
>
> **번호는 다시 매기지 않는다** — 왕복 문서 세 개가 이 번호로 서로를 가리킨다.
> **디렉터 답을 기다리는 것은 이제 다섯 건이다.**

**나머지 Q2~Q6 · Q8 · Q11 은 앵커를 막지 않는다.** 병행 가능하다.
Q11(관문 21곳)은 검산에서 나온 가장 큰 누락이고 아직 열려 있다.

---

## 4. Studio 가 다음에 낼 것

| | 내용 | 무엇을 판정하나 |
|---|---|---|
| **D7** | ㉳ 구성 · 점 지름 **14 / 20 / 24px** 세 벌 | 점 마커의 소유주 식별 |
| **D8** | 같은 구성 · **재설계 팔레트** 적용 | 팔레트가 작은 색점에서 실제로 갈리는가 |

D4(점만)는 비교 대상으로 남긴다. **D1·D2·D3·D5 는 내린다.**

### 다음 세션 과제 (Studio 몫)

- PixelLab · Retro Diffusion 의 **현재 API 제공 여부 · 요금 · 출력 규격** — 아직 확인 못 함
- ~~`2d-assets` 저장소 실제 상태 재확인~~ → **확인함 (2026-08-17).** 살아 있고 커졌다 —
  발주 입구(`02_CATALOG/CAPABILITIES.md`) · 회신 출구(`order_brief.py`) · 테스트 200.
  **판정은 여전히 하지 않는다**(`picks/`·`approved/` 없음). 부대 스프라이트 착수 때 다시 본다
- **Galmuri 도트 글꼴의 실제 표시 크기** — 아이콘 선 두께를 획 두께에 맞춰야 한 벌로 보인다. 앵커 제작 전
- claude.ai 커넥터(Drive · Gmail · Calendar)가 **여전히 미인증**이다. 원본이 Drive 에 있으면
  지금은 가져올 수 없다 — 인증은 사람이 claude.ai 설정에서 해야 한다
- **게임 쪽 초상 파이프라인이 커밋되어 눈에 보이게 됐다** (`919aa2c` — `scripts/portraits/` ·
  도트 초상 22명 · `README_PORTRAITS.md` · 원화는 `2b3d4e7` 로 lfs 에).
  **`REQUEST` §7-4 의 「절반만 흡수」 안이 이제 실물 위에서 판단 가능하다** — 디렉터 승인 대기 중인 §5 와 같은 건이다

---

## 5. 공통화 보류 중인 것

`docs/03` §22 · `docs/11` §9 대로 **반복이 확인될 때까지 옮기지 않는다.**

| 후보 | 현재 위치 | 승격 시점 |
|---|---|---|
| `lib/providers.js` (bfl·replicate·openai·dryrun) | 게임 저장소 (`919aa2c` 로 커밋됨) | **승격 조건은 이미 충족**(tteoklak 이 같은 필요를 따로 만났다). 디렉터 승인 뒤 별도 작업으로 |
| `select.js` · `make_review_sheet.js` | 같은 곳 | `REQUEST` §7-4 가 「승격」으로 가른 것들. 위와 같은 묶음 |
| `pixel_grid_probe.py` 격자 검출기 | `reviews/2026-08-17_mockup-spec-recovery/` | 두 번째 프로젝트에서 같은 검사가 필요해질 때 |
| 램프 스왑 (`dice_board` 의 `swapPalette`) | 다른 저장소 | **부대 스프라이트 착수 시점** |

화풍(`prompts/style_base.txt`)과 삼국지 고유 값은 **절대 공통화하지 않는다.**

> **이 보류가 지금 다른 프로젝트를 세우고 있다.** 떡락섬은 초상 프롬프트 5블록을 다 조립해 두고
> **사람이 생성기에 붙여 주기를 기다리는 중**이다 — `providers.js` 가 승격되면 그 왕복이 사라진다.
> 다만 `docs/03` §22 대로 **승격은 디렉터 승인을 받은 별도 작업**이고, 여기서 앞당기지 않는다.

---

## 6. 문서 지도

| 무엇 | 어디 |
|---|---|
| 게임 소개 · 범위 | [`brief/PROJECT_BRIEF.md`](brief/PROJECT_BRIEF.md) |
| 아트 방향 | [`brief/ART_DIRECTION.md`](brief/ART_DIRECTION.md) |
| 기술 규칙 | [`brief/STYLE_SPEC.md`](brief/STYLE_SPEC.md) |
| 자산 목록과 상태 | [`brief/ASSET_MANIFEST.md`](brief/ASSET_MANIFEST.md) |
| 세력 식별 | [`brief/IDENTIFICATION_SYSTEM.md`](brief/IDENTIFICATION_SYSTEM.md) |
| 앵커 발주서 | [`brief/ASSET_BRIEF_map_vertical_slice.md`](brief/ASSET_BRIEF_map_vertical_slice.md) |
| **디렉터 판단 요청 (Q1~Q11)** | [`REQUEST_TO_DIRECTOR.md`](REQUEST_TO_DIRECTOR.md) |
| 게임 쪽 왕복 | [`HANDOFF_TO_GAME.md`](HANDOFF_TO_GAME.md) · [`_02`](HANDOFF_TO_GAME_02.md) · [`_03`](HANDOFF_TO_GAME_03.md) · [`_04`](HANDOFF_TO_GAME_04.md) |
| 목업 측정 기록 | [`reviews/2026-08-17_mockup-spec-recovery/FINDINGS.md`](reviews/2026-08-17_mockup-spec-recovery/FINDINGS.md) |
| 좌표판 검토 본문 | [`reviews/2026-08-17_density-plates/REVIEW.md`](reviews/2026-08-17_density-plates/REVIEW.md) |
