# Game Art Studio

> **This document is written for LLM agents, not for humans.**
> It is not an introduction meant to be read and relayed by a person. It is an **interface specification**:
> everything an agent needs to decide, without human mediation, what this repository is for, where its
> boundaries are, and how to make a request against it.
> There is no marketing copy here. Every section answers one question only — *what can you decide with this?*

> ⚠️ **Language warning, read this before anything else.**
> This README is in English. **The rules themselves are not.** All 18 governance documents
> (`CLAUDE.md`, `docs/01`–`11`, `templates/`) are written in Korean — roughly 233,000 characters.
> If you cannot read Korean you cannot operate this studio; you can still use §7 (companion factories),
> §11 (machine-readable summary), and this README as a protocol description.

<details>
<summary><b>한국어 요약</b></summary>

이 저장소는 **게임이 아니고, 이미지 생성 서비스가 아니고, 에셋 라이브러리가 아니다.**
사람 디렉터가 정한 시각적 의도를 실제 게임에서 쓸 수 있는 **결정 · 규격 · 후보 관리 · 검증 · 엔진 전달**로
바꾸는 **Game Art Studio** — 문서와 도구로 이루어진 시스템이다. 서로 화풍이 전혀 다른 여러 게임을 동시에 담당한다.

한 줄 계약: **`art-studio` 는 결정하고 기억한다. 에셋 팩토리는 증폭한다. 상하는 승인에만 있고, 승인은 사람의 것이다.**

이 README 의 한국어판은 git 이력에 남아 있다 (`git log -- README.md`). 정본을 둘로 만들지 않기 위해 별도 파일로 유지하지 않는다.
</details>

---

## 0. Thirty-second triage — read on, or leave

If your problem is in the left column, this repository has something for you. If it is in the right column, **do not come here.**

| Come here for this | Not this |
|---|---|
| Art direction exists as words only, with no numbers | Game logic, servers, networking, balance |
| You have mockups/references but not their specs (tile size? palette count? portrait resolution?) | "Draw me a picture" (→ §6-2. **no image generator is wired into this repo**) |
| Several candidates exist and you have no basis for choosing | Where to download free assets (→ §7, factories) |
| You cannot tell "approved" from "merely generated" | Code review, refactoring |
| An asset looks wrong on screen and you cannot tell if the cause is the source or the engine | Overall game design, systems, fun |
| Multiple games in flight and their styles are bleeding into each other | Sound, music, text, localization |
| You hand-check dimensions/alpha/palette/frames on bulk assets every time | Project scheduling |
| Approval records do not exist, so nobody remembers why anything was decided | Monetization, store policy |

**The one line that matters:**

> This repository is **not where art gets made. It is where decisions about art get structured, remembered, and verified.**

---

## 1. What this repository actually is

| Property | Fact |
|---|---|
| Kind | A documentation system plus a small amount of Python tooling. **Not** a game repository |
| Size | 18 governance documents (~233,000 characters) + project documents + tools |
| Code | `studio/tools/contact_sheet.py` (shared) + several project-scoped tools |
| Images | **Not in the repository.** `.gitignore` excludes `projects/**/*.png|jpg|webp|psd|…`. A clone gives you **documents and code only** |
| Projects under management | 3 (`three-kingdoms`, `dice-dominion`, `tteoklak-island`) — §9 |
| House style | **None.** Style is a property of each project, never of the studio |
| Final authority | **The human director.** Agents do not replace that decision |
| Document language | Korean, throughout |

### What this repository has actually accumulated

Method, not style. Style stays with the project; only the following is promoted to the studio level:

```
image-processing methods · validation methods · file conversion · generator wiring ·
how candidates are presented for review · engine handoff procedures ·
repeat-work tooling · state vocabulary · the shape of an approval record
```

---

## 2. Reading path — **do not read all of it**

Reading all 233,000 characters is almost always waste. **Go from your question straight to the document.**

### 2-1. Always read this first (~4,100 characters)

```
CLAUDE.md          Role definition and operating principles. The constitution for any agent working here
```

Claude Code loads `CLAUDE.md` automatically when this directory is opened. **Any other agent must read it explicitly.**

### 2-2. Question → document routing table

| Your question | Document | Size |
|---|---|---|
| What is this studio, and what is it not? | `docs/01_STUDIO_IDENTITY.md` | 5.4k chars |
| May I decide this myself, or must I ask the human? | `docs/02_DIRECTOR_RELATIONSHIP.md` | 8.0k |
| Where do files go? How do I register a project? | `docs/03_PROJECT_STRUCTURE.md` | 12.5k |
| How do I take style from *words* down to *numbers*? | `docs/04_ART_DIRECTION_SYSTEM.md` | 15.2k |
| Which tool for which job (generators, Blender, engines, MCP, APIs)? | `docs/05_TOOL_ROLES.md` | 16.4k |
| What state is this artifact in — candidate? approved? export? | `docs/06_ASSET_LIFECYCLE.md` | 16.3k |
| The full procedure for producing one asset | `docs/07_GENERATION_WORKFLOW.md` | 17.9k |
| What does the machine check, and what does the human judge? | `docs/08_REVIEW_AND_APPROVAL.md` | 18.6k |
| How do I validate dimensions, alpha, palette, frames, tiles, atlases? | `docs/09_ASSET_SPEC_AND_VALIDATION.md` | 23.2k |
| How do I hand off to an engine, and where do I look when the screen is wrong? | `docs/10_ENGINE_HANDOFF.md` | 23.4k |
| May I carry this experience over to another project? | `docs/11_LEARNING_AND_REUSE.md` | 16.0k |
| Where does this studio sit in the wider org (director, ChatGPT, developer)? | `STUDIO_USAGE_CONTEXT.md` | 6.2k |
| How does work split between this repo and the asset factory? | `CAPABILITY_2D_ASSET_FACTORY.md` | 11.2k |

### 2-3. Templates to copy when a document must be created

| Template | Question it answers |
|---|---|
| `templates/PROJECT_BRIEF.md` | What is this game? |
| `templates/ART_DIRECTION.md` | How should this game look? (words, direction) |
| `templates/STYLE_SPEC.md` | Which numbers and technical rules apply? (values, specs) |
| `templates/ASSET_MANIFEST.md` | What is needed, and how far along is each item? |
| `templates/ASSET_BRIEF.md` | What exactly is being produced this time? |
| `templates/REVIEW_LOG.md` | What was adopted or rejected, and why? |

### 2-4. Precedence (when documents disagree)

```
CLAUDE.md · docs/01–11 · templates/     ← always wins (the 18)
        ↑
STUDIO_USAGE_CONTEXT.md · CAPABILITY_2D_ASSET_FACTORY.md   ← thin auxiliary docs; they never override the above
        ↑
projects/<id>/ documents                 ← valid inside that project only; never contagious to other projects
        ↑
this README                              ← an interface guide, not the source of truth for any rule
```

**If this README and `docs/` read differently, `docs/` is right.**

---

## 3. Vocabulary contract — break these five and everything downstream breaks

This is the rule visiting agents violate most often.

```
generated  ≠  approved  ≠  ready to use in the game
```

| State | Meaning | Common misreading |
|---|---|---|
| `REFERENCE` | Input material. Exists **in parallel** with the entire production process | "It's in the reference folder, so copy it" → no |
| `CONCEPT` | Exploratory output for finding direction | "A concept exists, so candidates follow automatically" → no |
| `CANDIDATE` | Something that **might** be adopted | **"Validation passed, so it's approved" → absolutely not** |
| `APPROVED` | The official source the director explicitly adopted | "A shelf for candidates that came out well" → no |
| `EXPORT` | Derived from an approved source for a specific runtime | "The export is the original" → no; it must always be regenerable |

Auxiliary states: `REJECTED` · `ON HOLD` · `SUPERSEDED` — these mark **the result of a judgement**, not a position in the pipeline.

There are three axes, not one list:

```
source axis    CONCEPT → CANDIDATE → APPROVED     exactly one at a time
derived axis   APPROVED SOURCE → EXPORT           many targets may coexist
input material REFERENCE                          runs in parallel with both
```

> **A technical pass is not an adoption.** Ten green checks from a validator mean "it is not broken." They never mean "we are using this."

---

## 4. Directory contract

```text
art-studio/
├── CLAUDE.md                       role definition — read first
├── README.md                       this file (agent-facing interface)
├── LICENSE                         MIT
├── STUDIO_USAGE_CONTEXT.md         position within the organization (auxiliary)
├── CAPABILITY_2D_ASSET_FACTORY.md  division of labor with the asset factory (auxiliary)
├── docs/01–11                      11 studio rule documents
├── templates/                      6 project document templates
├── studio/
│   └── tools/contact_sheet.py      shared tool — candidate contact sheet
└── projects/<project-id>/          per-game workspace (below)
```

### Per-game structure

```text
projects/<project-id>/
├── brief/          PROJECT_BRIEF · ART_DIRECTION · STYLE_SPEC · ASSET_MANIFEST · ASSET_BRIEF_<asset>
├── references/     reference material (images are not committed)
├── concepts/       exploration output
├── candidates/     candidates (not approvals)
├── approved/       official sources the director adopted
├── exports/        engine-bound derivatives (unity/ godot/ roblox/ web/ — only what is actually used)
├── reviews/        <date>_<topic>/ review bundles + REVIEW_LOG
├── orders/         <date>_<asset>.md production orders
├── tools/          scripts scoped to this project only
└── PROGRESS.md     how far along, and what is blocked (a snapshot; never the source of truth)
```

**The folder count is not enforced. What must be preserved is the *difference in state* each folder represents.**

### File protocol between a game repository and the studio

If you are an agent on the game side, these filenames *are* the protocol.

| File | Direction | Purpose |
|---|---|---|
| `projects/<id>/PROGRESS.md` | studio-internal | Progress snapshot. **Never copy authoritative values into it** |
| `projects/<id>/QUESTIONS_TO_STUDIO.md` | game → studio | What the game side is asking the studio |
| `projects/<id>/HANDOFF_TO_GAME_NN.md` | studio → game | Replies; the number increments |
| `projects/<id>/REQUEST_TO_DIRECTOR.md` | studio → human | Questions **only a human can answer** |
| `projects/<id>/STUDIO_DECISIONS.md` | studio-internal | Technical decisions the studio made, with rationale |
| `projects/<id>/orders/<date>_<asset>.md` | studio → production means | The order |
| `projects/<id>/reviews/<date>_<topic>/` | studio → director | Comparison material plus the written verdict |
| `ART_STUDIO_LIAISON.md` in the game repo | game → studio | Where the game side records what is blocking it |

---

## 5. Request protocol

### 5-1. Five request types

Nearly every request collapses into one of these five. **Naming the type makes the reply far more precise.**

#### ① DIAGNOSE — "why does this look wrong?"
> Input: screenshots, mockups, live game frames, asset file listings
> Output: **cause isolated to a layer** (Source / Export / Import / Engine) + evidence + next action

Example: "portraits look mushy on screen" → is it source resolution, export compression, an engine filter setting, or display scale?

#### ② SPECIFY — "turn words into numbers"
> Input: reference images, mockups, a description of "this kind of feel"
> Output: draft `ART_DIRECTION.md` (direction) + `STYLE_SPEC.md` (numbers), with measurement evidence

Recoverable by measurement: tile grid, palette actually in use and its ramp structure, real marker/icon sizes, canvas ratio, outline presence and weight, density.
**What measurement cannot answer is labeled as such** (appeal, emotional tone, fit with the fiction).

#### ③ PRODUCE — "make it producible"
> Input: the asset requirement (what, how many, used where)
> Output: `ASSET_BRIEF` + prompt blocks + candidate folder structure + contact sheet

⚠️ **This repository cannot produce images itself.** No generator is wired in (§6-2).
Output stops at "an order and prompts in a form that can be generated." The actual pixels come from external tools, a human, or a factory (§7).

#### ④ VALIDATE — "does it meet spec?"
> Input: file paths + expected spec (or `STYLE_SPEC.md`)
> Output: `PASS / WARNING / FAIL` list + where each failure originates

Axes: dimensions · aspect ratio · alpha · transparent edges · padding · bounding box · pivot · color and palette · pixels and edges · frame consistency · tile seams · texture specs · file-set completeness · export results.
Rule strength splits into `Required / Recommended / Informational`. **Not every deviation becomes a FAIL.**

#### ⑤ HANDOFF — "let me get this into the engine"
> Input: approved sources + target runtime (Unity / Godot / Roblox / Web)
> Output: export specs · import requirements · runtime checklist · screenshot-based review

---

### 5-2. Minimum order form (copy and fill)

```markdown
## Request
- Type: DIAGNOSE | SPECIFY | PRODUCE | VALIDATE | HANDOFF
- Project: <project-id>   (if new, write "new" and also fill in §5-5)
- One-line purpose: <what this artifact does inside the game>

## Context
- Target asset: <name · count · use>
- Actual on-screen size: <how many px it really occupies>   ← frequently omitted, frequently decisive
- Camera / viewing distance: <top-down / isometric / side-on / portrait close-up>
- Engine and resolution: <Unity 2022 / 1920x1080 / pixel-perfect yes-no>
- Existing decisions: <values already fixed; "none" if none>
- Reference material: <paths or links, and which axis you want referenced>

## Constraints
- Do not touch: <approved assets that must not change · forbidden depictions>
- Nature of the deadline: exploration | finalization | mass production

## Judgement
- Final judge for this request: human director | technical validation alone suffices
- Success criterion: <what state counts as done>
```

### 5-3. Good requests vs bad requests

| ❌ This forces a round trip | ✅ This moves immediately |
|---|---|
| "Make a cool character" | "Three soldier types shown at 40px top-down. Faction must read from silhouette, not color alone" |
| "Extract the style of this image" | "Recover tile grid, palette and measured icon sizes from this mockup. The director judges style" |
| "Tell me if this is okay" | "Lay these 8 out comparably on the *readability* axis. The director picks" |
| "Put it in the game" | "Unity, pixel-perfect, PPU 32, atlas capped at 2048. Give me export specs and import requirements" |
| "Just decide" (while style is undecided) | "Put A/B/C side by side so the differences show. The director finalizes" |

### 5-4. Reply contract — the shape of what comes back

These are the rules the studio holds itself to when responding. **Agents may parse against them.**

1. **Fact, judgement, and assumption are never blended.** Measurements are presented as measurements; opinions as opinions.
2. **Aesthetic decisions are never delivered as settled.** When several directions are viable, they are placed side by side.
3. **Candidates arrive in comparable form** — contact sheets, renders at true display size, anchored against the reference.
4. **Points requiring approval are named.** "A human must decide this" is never hidden.
5. **The location of the source of truth is stated.** Values are not allowed to exist in two places.
6. **Unknowns are not silently resolved.** An assumption is labeled an assumption.

### 5-5. Minimum information to register a new project

```
1. project-id           (kebab-case; becomes the folder name)
2. One-line description  genre · viewpoint · platform
3. Engine and target resolution
4. The size assets are actually displayed at
5. Reference material or current build screenshots
6. Where the source of truth for art direction lives  ← if the game repo already owns it, that side is authoritative
7. The single thing most blocked right now
```

If #7 is empty, the project gets registered and nothing moves.

---

## 6. Boundaries — what is refused, and what is impossible

### 6-1. Refused by policy

- **Final aesthetic decisions are not made here.** Style, adoption, whether a character is appealing, the emotional tone of the game, "is it good enough yet" — the director's territory.
- **Game logic is not redesigned.** Art work is never a license to change rules.
- **One game's style is never carried into another.** Technique is reused; style is isolated.
- **Generated output is never promoted to approved.** Without explicit adoption by the director, it is a candidate.
- **A second source of truth is never created.** Point at the location instead of copying the value.
- **Purchased or licensed assets are never fed into generative AI.** Most licenses forbid it.
- **Purchased pack parts never ship as-is.** Placeholders are the exception, and must be visibly placeholders.
- **Approved assets are never silently overwritten.**

### 6-2. Impossible today (facts about current capability)

| Cannot | Status |
|---|---|
| **Generate images directly** | No generator is connected to the studio. Output stops at orders and prompts; pixels come from external tools or a human |
| Precise ramp palette swapping (as a shared tool) | Exists in project tooling; not yet promoted to shared — it gets promoted when it is actually needed |
| Automatic "is this really pixel art?" judgement (as a shared tool) | Same reason; not yet shared |
| 3D modeling, rigging, animation production | Out of scope. Textures, specs, and handoff are in scope |

**This table exists so that nothing is hidden.** Rather than imitating a capability it lacks, the studio routes the work to something that genuinely has it — an external generator, a factory, or a person.

### 6-3. Conditions that force a stop and a question to the human

```
the project's style is not yet decided        ← the first artifact would silently define it
several directions are all defensible
there is a possible conflict with a prior director decision
the identity of a major character or signature asset would change
the result would affect the art direction of the whole project
```

Stopping does not mean downing tools. **Framing the problem, laying out the options, and showing how they differ is part of the stop.**

### 6-4. Conditions for proceeding without asking

```
the existing rule is unambiguous · it is repetition of an established pattern ·
it is technical cleanup · it is easily reversible ·
it applies an already-approved result as-is · the decision is already recorded
```

Even then, **what was done is recorded.** Acting autonomously and acting silently are different things.

---

## 7. Companion repositories — the asset factories

> This section **keeps growing.** Every new factory adds a row here. Registration spec: Appendix A.

### 7-1. Factory list

| # | Repository | URL | Access | What it does | When to use it |
|---|---|---|---|---|---|
| 1 | **2d-assets** — 2D Art Factory | `https://github.com/jungyh870918/2d-assets`<br>`git@github.com:jungyh870918/2d-assets.git` | Private (permission required) | Leaves purchased/CC0 modular 2D assets untouched and mass-produces game art through composition, palette and layer rules alone. Seed-deterministic. Includes a validator and Unity export | Building a **population** — villagers, mobs, soldiers, props, faction color variants, crowds |
| 2 | **game-sandbox** — consumer-side fixture | `https://github.com/jungyh870918/game-sandbox`<br>`git@github.com:jungyh870918/game-sandbox.git` | Private (permission required) | A minimal Unity project that consumes factory output. An integration fixture proving the output runs in an outside project **without the factory repo present** | Verifying the export contract and the consumer boundary |

*(For private repositories, request access from the owner. Without access, understand the interface from this README and ask rather than attempting a clone.)*

### 7-2. Division of labor between `art-studio` and `2d-assets` — the one line that matters

> **`art-studio` decides and remembers. `2d-assets` amplifies.
> Neither outranks the other, and exactly one thing has a hierarchy — approval.**

| | `art-studio` | `2d-assets` |
|---|---|---|
| Substance | Governance documents + light tooling | A working Python pipeline + real source assets |
| Good at | Boundaries of judgement · meaning of states · style isolation · approval records | Deterministic composition · palettes · validation · Unity wiring |
| Cannot | **Make images at all** | **Decide anything** — it has no place to record "we picked this" |
| Concept of approval | Yes (`approved/` + `REVIEW_LOG`) | **None** — its own README states that it does not judge |

### 7-3. What goes to a factory and what does not

| | **Population** | **Identity** |
|---|---|---|
| Examples | Villagers, mobs, soldiers, props, faction color variants, crowds | Protagonist, boss, signature landmark, UI language, title screen |
| Requirement | Many, mutually distinct, and consistent | One thing that is exactly *that* thing |
| Means | **The factory** — composition, palette, seed | Generator + hand work + director round trips |
| Candidate presentation | Contact sheet | Individual comparison |

> **A factory recombines what already exists; it cannot create a new visual identity.**
> That single line determines the entire division of labor.

### 7-4. The contract for feeding parts to a factory (style-independent)

```
composable = parts_separable ∧ pre_aligned ∧ animation_compatible
```

| Requirement | Why |
|---|---|
| **A separate PNG per slot** (no pre-merged finished sheets) | Without separation, composition is impossible |
| All parts on the **same logical cell and same origin** | Misalignment detaches arms from bodies |
| Animation and frame counts consistent across slots (or a declared subset) | Frame mismatch surfaces at runtime |
| **Declare z-order** | Transcribed by hand, it drifts |
| Colors follow a **ramp structure** | Palette swapping only works on top of that |

**This contract has nothing to do with style.** Meet it with your own parts and the same machine runs without anyone else's pack.

### 7-5. The biggest risk in using a factory

> **Ship a purchased or CC0 pack's parts as-is and the art direction of your game was decided by the pack's author.**

Packs carry style with them. Growing the subset does not fix it — LPC looks like LPC.
Hence: **population through the factory, identity through the directing loop.**

### 7-6. Approval does not hang on the PNG

Factory generation is deterministic — identical `(pack hash, rules, seed)` yields byte-identical PNGs. Therefore:

```
APPROVED SOURCE  =  pack hash + rule file + seed      (text, a few lines)
EXPORT           =  PNGs · sheets · prefabs           (regenerable at any time)
```

"The director adopted seed 4007" becomes a complete approval record on its own.
**The moment a part is retouched by hand, this property breaks.** That file then becomes the approved source and moves into `approved/`.

---

## 8. Setup

### 8-1. Clone

```bash
git clone https://github.com/jungyh870918/art-studio.git
cd art-studio
```

What you get: **documents and code.** Images are excluded by `.gitignore` and will not arrive.
(Ask the director if you need them. If storing them becomes necessary, set up Git LFS first and then revise the rule.)

### 8-2. Opening it with an agent

```bash
# Claude Code — CLAUDE.md loads automatically
claude

# Any other agent — read these yourself, in this order
#   1) CLAUDE.md
#   2) one or two documents from the §2-2 routing table, no more
#   3) projects/<target>/PROGRESS.md
```

### 8-3. Dependencies

```bash
python3 -m pip install --user pillow      # required by studio/tools/contact_sheet.py
```

There is no build or install step. **This repository is not a running application.**

### 8-4. Shared tooling

```bash
# Collect candidates onto one sheet so they can actually be compared
python3 studio/tools/contact_sheet.py projects/<game>/candidates/backgrounds

# Pin a reference anchor to the far left — far more accurate than viewing them separately
python3 studio/tools/contact_sheet.py <folder> --ref projects/<game>/references/01_explore.png
```

> This tool **does not judge.** It assigns no scores and no ranking. It does exactly one thing — put things side by side.
> That design *is* the character of this studio: **the machine prepares the comparison, the human makes the call.**

Project tools (`projects/<id>/tools/`) are valid only inside that project. Do not copy them sideways; promote to `studio/tools/` only after the repetition is confirmed.

---

## 9. Case studies — the three projects under management

The three are **stylistically unrelated**. That is the proof of "no house style."
The authoritative current state lives in each `PROGRESS.md`; the table below characterizes the work, it does not report state.

| Project | Character | What the studio actually did |
|---|---|---|
| **`three-kingdoms`** — a web homage to Romance of the Three Kingdoms III | Many character portraits, a coordinate map, an identification system | Measured 4 mockups and established that **"this mockup is not pixel art"** (replacing assumption with data) · recovered the real 78×80 marker size · measured which surname groups actually collide · four review round trips on the coordinate plate |
| **`dice-dominion`** — board plus combat | Precise rendered illustration, ivory UI frames, flat tiles on a Unity 3D ring | Measured **16 ivory color tokens** · supported the decision on how the board is built · assembled 3 sets of panel parts twice and diagnosed the seam problem · the color values landed in game code and were pinned by tests |
| **`tteoklak-island`** | Illustrated backgrounds, painterly portraits, portrait-orientation only | Fixed the **942×1674 reference canvas** · audited all 31 mockup UI elements · produced the derived spec table · two backgrounds integrated into the live game with hotspots aligned |

### The patterns worth extracting

1. **Measurement replaces assumption.** Overturning "it looks like pixel art" with real measurements was the single most valuable output.
2. **The source of truth is one place.** `dice-dominion`'s game repo already owns the art documents, so the studio keeps **the judgement and its reasons** rather than duplicating values.
3. **The bottleneck moves.** Sometimes the game side, sometimes the studio, sometimes "no image generation available, waiting on a human." That is why `PROGRESS.md` exists.
4. **Approvals are rare.** Having many candidates and having an approval are entirely different states.

---

## 10. Common failure modes (for the requesting agent)

| Failure | Why it matters | Do this instead |
|---|---|---|
| "Validation passed, so let's ship it" | Technical pass ≠ adoption | Report "technical pass; adoption is the director's" |
| Presenting a single candidate while style is undecided | **That one image silently fixes the project's style** | Present A/B/C so the differences show |
| Judging from the isolated PNG | Game art is seen with camera, display size, background, lighting, UI | Render at **true display size**, or check in the running game |
| Applying one game's rules to another | Style contamination — the warning sign is every game starting to look alike | Promote technique, leave values with the project |
| Copying values into several documents | Two sources of truth, which then diverge | Point at the location |
| Turning every deviation into a FAIL | Validation starts governing design | Split into `Required / Recommended / Informational` |
| Fixing undecided values arbitrarily (32px tiles, 32-color palettes) | The assumption hardens into fact | Label it an assumption and offer it as a candidate |
| Asking the human about everything | The human becomes the bottleneck | If §6-4 applies, proceed and leave a record |
| Silently overwriting an approved asset | Not recoverable | Create a new candidate and present it with rationale |

---

## 11. Machine-readable summary

```yaml
repo: art-studio
kind: game-art-studio            # not a game, not an image generator, not an asset library
owner_decision_authority: human-director
readme_language: en
document_language: ko             # all governance docs are Korean (~233k chars)
style_policy: no-fixed-style      # style is a property of each project
license: MIT
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
  - generate images itself            # no generator is wired into this repo
  - decide aesthetics or approve assets
  - redesign game logic
  - transfer one project's style to another

tools:
  shared: [studio/tools/contact_sheet.py]
  deps: [python3, pillow]
  note: "images are gitignored; a clone yields documents and code only"

companion_repos:
  - name: 2d-assets
    url: https://github.com/jungyh870918/2d-assets
    role: population-scale modular 2D generation (deterministic, seed-based)
    visibility: private
  - name: game-sandbox
    url: https://github.com/jungyh870918/game-sandbox
    role: consumer-side Unity integration fixture for factory output
    visibility: private

division_of_labor: "art-studio decides and remembers; factories amplify; approval belongs to the human director"
```

---

## 12. Glossary — English to the Korean you will meet inside the docs

| English | Korean (as written in the documents) | Meaning |
|---|---|---|
| candidate | 후보 | Made, but not adopted |
| approved | 승인 | The official source the director explicitly adopted |
| export / derivative | 파생물 · 내보내기 | Derived from an approved source for an engine |
| asset brief / order | 발주서 | The document stating what is being produced this time |
| contact sheet | 대조 시트 | One sheet with candidates side by side for comparison |
| anchor | 앵커 | The single reference held as the standard |
| source of truth | 정본 | The one and only origin of a value |
| population | 모집단 | Assets that must be numerous and varied |
| identity | 정체성 | Assets where one thing must be exactly that thing |
| silhouette | 실루엣 | Whether form alone distinguishes it |
| color ramp | 램프 | The shading series structure of a palette |
| spec recovery | 규격 회수 | Measuring a mockup or reference to recover its numbers |
| style isolation | 스타일 격리 | Keeping one game's style from spreading to another |
| director | 디렉터 | The human with final authority |

---

## Appendix A. Registering a new factory

Add one row to the §7-1 table. Do not register it until all six cells are filled.

```markdown
| # | <name> — <one-line character> | `<https url>`<br>`<ssh url>` | public/private | <what it does — input and output> | <when to use it — population / identity / validation / handoff> |
```

Decide these alongside the row:

1. **Does this factory decide, or amplify?** If it decides, the approval boundary (§7-2) must be redrawn.
2. **What is its input contract?** Write it as a technical contract independent of style (§7-4 form).
3. **Does it bring style along?** If so, restrict it to population work (§7-5).
4. **What does approval hang on?** Deterministic generation → `(hash + rules + seed)`; otherwise the file itself (§7-6).
5. **If it is private, say so in the table.** It stops agents without access from spinning.

---

## License

**MIT** — see [`LICENSE`](LICENSE). It applies uniformly to the documents, the tools, and the project records.

What an agent needs to know:

- **Copy, modify, redistribute, and use commercially, freely.** Retain the copyright notice and the license text.
- **There is no warranty.** The numbers, specs and judgements here came out of specific project contexts; nothing guarantees they fit another game — the same reason §6 insists on style isolation.
- **This license covers the contents of this repository only.** Assets in the companion factories (§7) carry their own licenses, and many of them forbid redistribution and use as generative-AI input. **Do not treat this MIT as covering pack licenses.**
- `projects/` holds art decisions for games in progress. Reuse is permitted, but **do not cite them as approved assets or official direction for those games.** The state vocabulary (§3) exists for exactly that distinction.

## How this README is maintained

- **Every new factory adds a row** to the §7-1 table (Appendix A).
- **If `docs/` and this README read differently, `docs/` is right.** This is an interface guide, not the source of truth for any rule.
- When implementation or governance changes and a factual statement here becomes wrong, **fix it inside the same change.**
- The README is maintained in English only. A Korean edition is not kept as a second file — two files would become two sources of truth, which §10 forbids. The previous Korean edition remains in history (`git log -- README.md`).
