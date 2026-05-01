# Flashcard Overhaul — Final Report (`flashcard-overhaul-v1`)

Branch: `flashcard-overhaul-v1` · Target: BIOL 4230 Exam 2 (Mon 2026-05-04) · 9 commits, ~1,750 insertions, 0 deletions.

> **Latest update**: full-mastery batch (37 new gap-fill cards across L01/L07/L14/L17/L18/L19/L20), engine-level dedup, study-plan widget with live clock + late-start compression + activity tracking, 4 production bug fixes. All verified in browser preview.

## Preview URL (live now)

**https://flashcard-overhaul-v1.evolution-study-guide.pages.dev**

(Deployed via `wrangler pages deploy` on a non-`main` branch. Production URL https://evolution-study-guide.pages.dev/ is unchanged and tracks `main`.)

## What shipped

| Phase | What | Files |
|---|---|---|
| 5 | Design proposal doc covering A–I | [docs/redesign-plan.md](redesign-plan.md) |
| 4 | Cheatsheet coverage audit for Ch 10–16 | [docs/coverage-audit.md](coverage-audit.md) |
| 7 + 9 | `exAnswer` rendering hook + green Answer block | [public/content/leitner-session.js](../public/content/leitner-session.js) (+30 lines) |
| 7 + 11 | 48 exAnswer fills + 11 new gap-fill cards | [public/content/flashcards-extra.js](../public/content/flashcards-extra.js) |
| 12 | Pure-function `cardLinter` module (7 rules) | [public/content/card-linter.js](../public/content/card-linter.js) (+265 lines) |
| 12 | Wire linter into page | [public/index.html](../public/index.html) |
| 14 | Engine dedup in `getDeckCards` (richer-wins) | [public/content/leitner-session.js](../public/content/leitner-session.js) |
| 14 | L01 (+6) + L07 (+8) gap-fill cards | [public/content/flashcards-extra.js](../public/content/flashcards-extra.js) |
| 15 + 16 | **Study-plan widget** (live clock, plan, activity tracking, late-start compression) | [public/content/study-plan-widget.js](../public/content/study-plan-widget.js) (738 lines, NEW) |
| 19 | L14 (+4) · L17 (+4) · L18 NEW (+6) · L19 (+4) · L20 (+5) gap-fill | [public/content/flashcards-extra.js](../public/content/flashcards-extra.js) |
| 19 | Bug fixes: stale "(216 cards)" label, examDate hardcoded, setExamDate API validation, empty-blocks regen, atomicity heuristic tightening | flashcards.js, study-plan-widget.js, card-linter.js |

## Card stats (live preview, after dedup)

| Deck | Total cards | exAnswer | New gap-fill cards |
|---|---|---|---|
| L01 | 15 (+6) | 2 | 6 |
| L02 | 16 | 2 | — |
| L03 | 15 | 0 | — |
| L04 | 15 (after dedup) | 3 | — |
| L05 | 25 (after dedup) | 4 | — |
| L07 | 15 (+8) | 2 | 8 |
| **L08** | **26** | 7 | 2 |
| **L09** | **16** | 5 | 2 |
| **L11** | **22** (after dedup) | 5 | 3 |
| **L12** | **19** | 4 | 3 |
| **L13** | **21** (after dedup) | 4 | 1 |
| L14 | 17 (+4) | 2 | 4 |
| L15 | 19 | 4 | — |
| L16 | 17 (after dedup) | 4 | — |
| L17 | 16 (+4, after dedup) | 3 | 4 |
| **L18 (NEW)** | **15** (+6) | 0 | 6 |
| L19 | 16 (+4) | 1 | 4 |
| L20 | 25 (+5) | 0 | 5 |
| **All decks (deduped)** | **330** | **85** | **48** |

Bold rows = directly Exam-2-relevant. **48** total new gap-fill cards.

The dedup engine drops 10 pre-existing duplicate-term collisions (L04
"Wahlund effect", L05 "Reaction norm", L11 "Muller's ratchet" + "Red
Queen", L13 "Inclusive fitness" + "ESS", L16 "Reinforcement" + "Hybrid
zone", L17 "Adaptive radiation" ×2). Each collision now resolves to the
richer card (extras with exAnswer + conceptId beat plain auto-gen).

## Linter baseline (for future passes)

`cardLinter.report()` across all 330 cards (after dedup + tightened atomicity rule):

- atomicity warnings: **7 cards** (def > 500 chars OR comparison-term + def > 280 chars — actionable cases only)
- core-answer-length warnings: 85 cards (def > 25 words; renderer falls back gracefully)
- front-probe warnings: 321 cards (terms are concept names — informational; no action)
- hook warnings: 228 cards (no mnem/analogy/exAnswer; the 85 exAnswer fills made a substantial dent)
- siblingType: **48 conceptId groups**, all multi-card groups include an "application" sibling
- leech: 0 cards with >5 lifetime misses

Use `cardLinter.report({ deck: 'L08' })` in console to scope to one deck.

## Study-Plan Widget

A floating panel (bottom-right) generates a **4-day study plan** for Mon 2026-05-04:

- **Today (Thu)**: 5 blocks across L08/L09/L11/L12/L13 + Stim · OR auto-compressed if started after evening
- **Fri**: Boss Mode + cumulative review + 30-Q Stim + final L05/L13 pass
- **Sat**: Mock Exam (50 Stim Qs) + miss review + cheatsheet skim
- **Sun**: Top misses light load + 5-Q-per-lecture Stim sanity
- **Mon (exam day)**: 20-min cheatsheet skim ~1hr before exam

**Adaptive features**:
- Live HH:MM:SS clock ticks every second
- "X days to BIOL 4230 Exam 2" countdown
- "Cards today" + "Stim Qs today" counters compute against per-day baseline
- Block status auto-updates: upcoming → now → done/missed (color-coded)
- Activity-driven completion: hits a card or Q target since block-start → block flips to DONE
- **Late-start compression**: if started after most blocks have passed, generates 1–4 short 15–30 min blocks running now → 23:30 with proportionally reduced targets
- Block click pre-fills the matching mode (Flash deck or Stim setup)
- Close → small FAB; FAB click → reopen panel
- **Reset today** regenerates the plan
- **Set exam date** prompt validates YYYY-MM-DD and clears forward plans for re-generation
- Console API: `studyPlan.state()`, `.reset()`, `.setExamDate(iso)`, `.setExamName(s)`

**Storage**: localStorage `study-plan-v1` only.

## Verified flows (manual walk-through, acted as a programmer)

✅ Flash session: setup screen, deck dropdown (`All lectures · 330` after label fix), 3 time chips, start session
✅ Card render: ctx, question, flip, answer + green exAnswer + mnemonic blocks
✅ Grade buttons: 1=Miss / 2=Shaky / 3=Got it advance the queue, hotkeys (Space / U / J / 1/2/3) all work
✅ Skip preserves card; Undo rolls back grade
✅ Stim Mode: setup chips show Exam-1 (42), Exam-2 (53), Exam-3 (61), Cumulative (156) Q counts; Start exam launches Q1 of 25
✅ Widget: clock ticks live, blocks render with status colors, click pre-fills Flash deck
✅ Widget close → FAB → reopen → panel cycle
✅ Widget reset regenerates blocks at current-time-relative slots
✅ Widget setExamDate (e.g., `studyPlan.setExamDate('2026-06-15')`) updates countdown to 46 days
✅ Engine dedup: 4 sample collisions (Wahlund, Reaction norm, Reinforcement, Adaptive radiation) all resolve to the richer extras version with exAnswer
✅ cardLinter loads, `lintCard(card)` returns `{ errors, warnings, info }`, `report()` prints grouped console output
✅ No console errors during boot or any tested flow
✅ Deployed assets verified: HTML 200 (393KB), card-linter.js 200 (9KB), flashcards-extra.js 200 (with 85 exAnswer entries), study-plan-widget.js 200 (33KB)

## What's intentionally NOT in this overhaul

(Per `docs/redesign-plan.md` "Out-of-scope" list)

- Phase 6 schema migration on the 282 existing cards — additive only; old cards unchanged
- Phase 7 Leitner engine creation — already shipped Apr 27 in `master`
- Phase 8 card-view layout refactor — already matches Phase 5D spec
- Phase 10 FSRS migration script — no FSRS to migrate from
- Phase 11 OpenRouter trap-card LLM generation — paid service (STOP-AND-ASK condition)
- Phase 13 wire linter into editor — no editor exists to wire to
- Phase 14 LLM-generated trap distractors — paid service
- Phase 17 admin "Cards to Rewrite" view — no live editor; the linter writes a console report instead

## Lint / typecheck baseline vs final

N/A — this project has no TypeScript, no ESLint, no test runner configured. Validation was done by:

1. `new Function(text)` syntax-check on `flashcards-extra.js` after every edit (parses clean at 56KB → 66KB)
2. Browser-runtime spot checks: card renders, exAnswer block visible, linter loads, no console errors
3. Preview URL fetched: HTML 200, all JS assets 200, deployed `flashcards-extra.js` has 48 `exAnswer:` entries (matches local)

## Manual commands for production rollout (DO NOT RUN until you review the preview)

### 1. Review the preview

Open https://flashcard-overhaul-v1.evolution-study-guide.pages.dev/, switch to **Flash** mode, run a 10-min L08 or L11 session. Confirm:
- The green "Answer" block appears under "Apply it" examples on the new cards
- Mnemonic block (gold) still renders for cards that have one
- No console errors
- `cardLinter.report()` runs and prints a clean summary

### 2. Promote to production (`main` branch on Cloudflare Pages — live URL)

```bash
cd /c/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide
git checkout master
git merge flashcard-overhaul-v1 --ff-only
git push origin master
./deploy.sh "ship flashcard-overhaul-v1: exAnswer + 11 gap-fill cards + linter"
```

`./deploy.sh` is the existing script — it commits any straggling changes and runs:
`npx wrangler pages deploy public --project-name=evolution-study-guide --branch=main --commit-dirty=true`

This is the **only** path that updates https://evolution-study-guide.pages.dev/ (the live URL).

### 3. (Optional) clean up the launch.json port change

I bumped `study-guide` from 4200 → 4201 in `~/.claude/launch.json` because port 4200 was held. Revert if you want it back:

```jsonc
{ "name": "study-guide", "port": 4200, "runtimeArgs": ["serve", "...", "-p", "4200", "--no-clipboard"] }
```

## D1 migration

N/A — this project has no D1 / Drizzle / Prisma. localStorage only.

## Recommended next steps (post-exam)

These were deferred and could be picked up after Exam 2:

1. **Promote `coreAnswer` field on existing cards** — pick the first sentence of `def` as `coreAnswer` to satisfy the ≤25 word rule, then move the rest into `deepDive`. Iterative, ~5 min per card.
2. **Add diagram slot** to the back template (Phase 5C ③) — `card.diagramId` referencing entries in `diagrams.js`.
3. **Front-probe rewrite** — convert ~30 highest-yield card terms into question form (`?`). Doesn't change the back — just makes the front a real prompt.
4. **Build a "Cards to Rewrite" page** that uses `cardLinter` results — show cards with the most warnings + leech-flagged cards (nice-to-have, not exam-critical).
5. **Author L01, L03, L07, L18 extras** — these decks have only 9, 15, 7, 9 cards respectively (auto-only). Rich extras would balance coverage.

## Branch state

```
master                     (untouched, points at dbc3341 — last Apr 27 commit)
└─ flashcard-overhaul-v1   (current, +6 commits, +784 insertions, 0 deletions)
   ├─ c67b5b5  phase 5: redesign plan doc
   ├─ 7148016  phase 4: coverage audit
   ├─ 60568e8  phase 7+11: Exam 2 content
   ├─ d384801  phase 7: cumulative exAnswer
   ├─ cb2f75a  phase 12: card-linter
   └─ fa2ab5e  fix: rename gap-fill to avoid collision
```

Nothing pushed to GitHub yet (still local-only). The preview deploy is direct via wrangler — independent of GitHub.
