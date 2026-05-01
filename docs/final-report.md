# Flashcard Overhaul — Final Report (`flashcard-overhaul-v1`)

Branch: `flashcard-overhaul-v1` · Target: BIOL 4230 Exam 2 (Ch 10–16) in 2–3 days · 6 commits, 784 insertions, 0 deletions.

## Preview URL (live now)

**https://flashcard-overhaul-v1.evolution-study-guide.pages.dev**

(Deployed via `wrangler pages deploy` on a non-`main` branch. Production URL https://evolution-study-guide.pages.dev/ is unchanged and tracks `main`.)

## What shipped

| Phase | What | Files |
|---|---|---|
| 5 | Design proposal doc covering A–I | [docs/redesign-plan.md](redesign-plan.md) |
| 4 | Cheatsheet coverage audit for Ch 10–16 | [docs/coverage-audit.md](coverage-audit.md) |
| 7 + 9 | `exAnswer` rendering hook + green Answer block | [public/content/leitner-session.js](../public/content/leitner-session.js) (+30 lines) |
| 7 + 11 | 48 exAnswer fills + 11 new gap-fill cards | [public/content/flashcards-extra.js](../public/content/flashcards-extra.js) (+148 lines) |
| 12 | Pure-function `cardLinter` module (7 rules) | [public/content/card-linter.js](../public/content/card-linter.js) (+265 lines) |
| 12 | Wire linter into page | [public/index.html](../public/index.html) (+1 line) |

## Card stats (live preview)

| Deck | Total cards | exAnswer |
|---|---|---|
| L02 | 16 | 2 |
| L04 | 15 | 3 |
| L05 | 25 | 4 |
| **L08** | **26** (+2 gap-fill) | 7 |
| **L09** | **16** (+2 gap-fill) | 5 |
| **L11** | **22** (+3 gap-fill) | 5 |
| **L12** | **19** (+3 gap-fill) | 4 |
| **L13** | **21** (+1 gap-fill) | 4 |
| L14 | 13 | 2 |
| L15 | 19 | 4 |
| L16 | 17 | 4 |
| L17 | 12 | 3 |
| L19 | 12 | 1 |
| (other lectures) | — | — |
| **All decks (deduped)** | **293** | **48** |

Bold rows = directly Exam-2-relevant; (+N gap-fill) shows new cards added.

## Linter baseline (for future passes)

`cardLinter.report()` across all 293 cards:

- atomicity warnings: 6 cards (def too long; candidates for splitting later)
- core-answer-length warnings: 48 cards (def > 25 words; renderer falls back gracefully)
- front-probe warnings: 290 cards (terms are concept names — informational; no action)
- hook warnings: 228 cards (no mnem/analogy/exAnswer; my 48 exAnswer fills made a dent here)
- siblingType: 11 conceptId groups, 0 missing-application warnings (all gap-fill cards have `cardType: "application"` or `"discriminator"`)
- leech: 0 cards with >5 lifetime misses

Use `cardLinter.report({ deck: 'L08' })` in console to scope to one deck.

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
