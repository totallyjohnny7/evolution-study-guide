# Flashcard System Redesign Plan (`flashcard-overhaul-v1`)

Branch: `flashcard-overhaul-v1` · Site: https://evolution-study-guide.pages.dev/ · Cheatsheet: https://evolution-study-guide.pages.dev/cheatsheet · Target: BIOL 4230 Exam 2 (Ch 10–16) in 2–3 days.

This document covers the Phase 5 design proposal. Each subsection is labeled with implementation status:

- **DONE** — already in `master` (no work this overhaul)
- **NEW** — added in this overhaul
- **DEFERRED** — designed here, scheduled but not landed in this overhaul (post-exam)

---

## A. Schema Additions (additive, optional)

All fields are optional and additive. Existing cards work unchanged; new fields apply only where useful. No migration of the 282 existing cards is required pre-exam. Defaults shown where absent.

| Field | Type | Status | Notes |
|---|---|---|---|
| `cardType` | `"definition" \| "application" \| "cloze" \| "discriminator"` | NEW (gap-fill cards only) | Existing cards default to `"definition"` (semantically) |
| `sourceType` | `"textbook" \| "lecture" \| "studyguide" \| "ai" \| "user"` | NEW (gap-fill cards only) | Existing cards default to `"lecture"` (auto from key_terms) or `"studyguide"` (extras) |
| `hook` | `string` | NEW (alias for existing `mnem`) | The Leitner UI already renders `mnem` in a gold-bordered subsection. Keep `mnem`/`analogy` field names in the data; treat `hook` as a synonym in the linter only |
| `coreAnswer` | `string` ≤25 words | NEW (gap-fill cards only) | If absent, the renderer falls back to `def` |
| `deepDive` | `string` | DEFERRED | Collapsible expansion. Renderer support deferred. Authoring can stash the full `def` here and put a tight version in `coreAnswer` |
| `linkedCardIds` | `string[]` | DEFERRED | Cross-link refs. No id system today (cards keyed by `term` text); a stable ID scheme would need a card-ID migration first |
| `missCountLifetime` | `number` | DONE (different name) | Already tracked as `progress[cardKey].missCount` in `leitner-progress-v1` localStorage |
| `conceptId` | `string` | NEW (gap-fill cards only) | e.g., `"hwe-math"`, `"selection-types"`. Used by linter rule 6 (Definition ≠ Application sibling check). Stored on the card object directly |
| `leechFlagged` | `boolean` | NEW | Computed in linter (>5 lifetime misses or 2× consecutive Shaky); written to `leitner-progress-v1` next to `missCount` |
| `needsFrontRewrite` | `boolean` | NEW | Computed in linter when `term` lacks `?`, `___`, or `{{c#::}}` |
| `sessionState` | `"unseen" \| "miss" \| "shaky" \| "got_it"` | DONE | Already exists as `progress[cardKey].state` |

**Rationale for "DEFERRED" decisions**: with 2–3 days to exam, schema fields that require per-card retrofitting (linked refs, deep-dive split) yield nothing studyable. Authoring time is better spent on Ch 10–16 coverage gaps. The field names are reserved here so adding them later is non-breaking.

---

## B. Scheduling Replacement — Compressed Leitner-Style Loop

**STATUS: DONE.** All of Phase 5B is already implemented in [public/content/leitner-session.js](../public/content/leitner-session.js) (last commit Apr 27). Verified during the Phase 3 audit.

| Phase 5B requirement | Implementation in `leitner-session.js` |
|---|---|
| 3 buttons: 1 Miss / 2 Shaky / 3 Got it | `grade(rating)` switches on `rating === 1/2/3` |
| Miss → re-queue ~+4 (never immediate next) | `reinsertOffset(4, 1)` — yields offset of `[3, 5]`; min clamp `Math.max(2, ...)` ensures ≥2 |
| Shaky → re-queue ~+12 | `reinsertOffset(12, 2)` — yields offset of `[10, 14]` |
| Got it → leaves session, parked for tomorrow | `setCardState({ state: 'got_it' })` and not reinserted into queue |
| Hotkeys: Space/U/J/1/2/3 | Keydown listener at `leitner-session.js:1135–1154` |
| Buttons greyed until card flipped | `lzGrade1/2/3` start `disabled`; `renderCard()` toggles `b.disabled = !S.flipped` |
| Session timer 10/20/30 selector | `lzTimeChips` chips in setup screen; timer ticks at 250ms via `tickTimer()` |
| Triple-miss rescue | `if (S.missCounts[k] >= 3 && !S.currentRescue)` blocks queue and offers OpenRouter sub-card breakdown (the OpenRouter call is a `DEFERRED` placeholder — current rescue UI just acknowledges and moves on) |
| Trap cards every ~12 cards if recent miss rate high | `maybeInjectTrap()` requires `cardsSinceTrap >= 12` and ≥2 recent misses |
| Wrong trap → on-the-fly comparison card | `answerTrap('A'/'B')` injects a `Compare: X vs Y` card combining both `def`s |
| Pacing 8-min check, 60–75% soft / <60% forced break | `maybeOfferBreak()` |
| Streak counter (consecutive Got-it, resets on Miss) | `S.streak`, `S.bestStreak` |

**NEW work in scheduling**: none. The engine is already built.

The one piece marked **DEFERRED** is the OpenRouter sub-card breakdown — currently the rescue UI shows a static "you've missed this 3 times — let's slow down" prompt; an LLM-generated micro-deck would require a new API key and a paid service, which is out-of-scope per the autonomy rules ("Adding paid services or new API keys" is a STOP-AND-ASK condition).

---

## C. Back Template Layout (5 sections, conditional render)

**STATUS: PARTIAL DONE / NEW for missing pieces.**

Current Leitner card stage (`html.session()` at `leitner-session.js:1097–1107`):

```html
<div class="lz-card" id="lzCard">
  <div class="lz-ctx" id="lzCtx"></div>             <!-- ① section caption -->
  <div class="lz-question" id="lzQuestion"></div>   <!-- front -->
  <div class="lz-answer" id="lzAnswer"></div>       <!-- ② core answer (def) -->
  <div class="lz-example" id="lzExample"></div>     <!-- application scenario -->
  <div class="lz-exanswer" id="lzExAnswer"></div>   <!-- NEW: answer to scenario -->
  <div class="lz-mnem" id="lzMnemonic"></div>       <!-- ④ hook (mnem/analogy) -->
</div>
```

Mapping Phase 5C → current state:

| Phase 5C section | Current | Status | Plan |
|---|---|---|---|
| ① Section + source badge | `lz-ctx` shows section text only; no color badge | NEW (slim) | Add a small inline source badge before the ctx caption; color from `card.sourceType`. CSS: 4 small color classes (`.lz-src-textbook` green, `.lz-src-lecture` purple, `.lz-src-studyguide` gold, `.lz-src-ai` blue, `.lz-src-user` gray). Default behavior when `sourceType` absent: no badge (graceful) |
| ② Core answer (≤25 words, accent) | `lz-answer` renders `def` | DONE for layout / DEFERRED for ≤25-word rule | Renderer reads `card.coreAnswer` if present, else falls back to `card.def`. The 25-word rule is enforced via the linter (Phase 5E rule 3), warn-only |
| ③ Diagram (SVG/image/ASCII) | not present in flash mode | DEFERRED | Lecture diagrams already exist in `public/content/diagrams.js` for Study Mode. Flash-mode rendering would need a `card.diagramId` field referencing those SVGs. Deferred — non-trivial UI work; better to keep diagrams in Study Mode for the next 2–3 days |
| ④ Hook (italic, gold, 🎯 prefix) | `lz-mnem` is gold-bordered, label says "Mnemonic" or "Analogy" | NEW (cosmetic) | Update label to add 🎯 emoji prefix when `card.hook` set, keep "Mnemonic"/"Analogy" labels as-is when those fields are set (semantic preservation) |
| ⑤ Deep dive (collapsed) | not present | DEFERRED | Would need a `<details>` block with `card.deepDive`. Authoring time better spent on coverage gaps |
| ⑥ Linked cards (→ refs) | not present | DEFERRED | Requires the `linkedCardIds` field plus an ID resolution layer. Out of scope this overhaul |

**NEW (this overhaul)**:
- `card.exAnswer` — green-bordered "Answer" block under the example. Already wired in `leitner-session.js:715–774` and authored for L02 (2 cards) so far. Continuing through ~30 more cards with bare-question examples.
- Source badge (small): a 1-character color dot before the ctx caption. Skipped if `sourceType` absent.

---

## D. Card View Layout

**STATUS: DONE.** Verified in Phase 3 audit:

- Top bar (`lz-top` at `leitner-session.js:1091–1097`):
  - `lzCounter` shows `Card N · Q left`
  - `lzStreak` with 🔥 flame and counter
  - `lzTimer` counts down 10/20/30 min
  - `lzPause` (⏸) toggles pause/resume
  - `lzExit` (×) with Escape-confirm dialog
- Center: question (`lzQuestion`) is set once per card, persists after flip; answer / example / exAnswer / mnem render below on flip.
- Bottom: 3 grade buttons (greyed until flipped) + `lzFlip` / `lzUndo` / `lzSkip` row with hotkey labels.
- 200ms slide transitions: the `.lz-card` element has `transition: transform 250ms ease` and a `.lz-flipped` class — comes close to the spec. Acceptable.

**NEW work**: none.

---

## E. The 7 Card-Design Laws (Linter)

**STATUS: NEW (lightweight build, opt-in).**

Plan: ship `public/content/card-linter.js` as a pure module exporting `lintCard(card) -> { errors, warnings }`. Not wired to any editor (there isn't one). Used at build-time and in a future "Cards to Rewrite" view.

| # | Rule | Severity | Implementation |
|---|---|---|---|
| 1 | Atomicity (one fact per card) | warn | Heuristic: warn if `def.length > 320` chars, if `def.split(/\.\s/).length > 4` sentences, or if `term` includes `" and "`/`" vs "` paired with a multi-clause def |
| 2 | Front contains `?`, `___`, or `{{c#::}}` | warn | Existing `term` fields are concept-names only. Don't block; mark `needsFrontRewrite: true` for batch review |
| 3 | Core answer ≤25 words | warn | Counts whitespace-separated tokens in `card.coreAnswer ?? card.def` |
| 4 | Cloze `{{c1::...}}` support | n/a | Renderer support deferred; linter detects the syntax and marks `cardType: 'cloze'` if present |
| 5 | Hook non-empty (warn-only) | warn | Pass if `card.mnem`, `card.analogy`, or `card.hook` is set |
| 6 | Definition ≠ Application (siblings via `conceptId`) | warn | If two+ cards share `conceptId`, at least one should be `cardType:'application'`. Today's pattern (one card with `def` + `example`) violates this rule but is intentional — warn-only with a "consider splitting" message |
| 7 | Leech detection (>5 lifetime misses or 2× consecutive Shaky) | flag | Computed at runtime from `leitner-progress-v1`; sets `leechFlagged: true` and surfaces in the future "Cards to Rewrite" view |

**Decision**: ship the linter module so it's available, but don't gate authoring on it. With 2–3 days left, content beats correctness theater. The linter runs as a one-shot report when manually invoked: `linterReport.run()` in the console will print a per-card list of warnings.

---

## F. FSRS → Session State Migration (silent, on app open)

**STATUS: N/A — no FSRS to migrate from.**

The repo never used FSRS. The only legacy data are the older simple-state keys `biol-fc-progress-v2` and `evol-fc-progress-v1` (values `'missed'` / `'known'`), which are already migrated by `migrateOnce()` at `leitner-session.js:89–113` into the new `leitner-progress-v1` schema (`{ state, missCount, lastSeen }`).

A `migration_v1: 'done'` gate is *implicitly* present: `migrateOnce()` short-circuits if `KEYS.PROGRESS` already has a value. No action needed.

---

## G. End-of-Session Screen

**STATUS: DONE.** [`renderEnd()`](../public/content/leitner-session.js) at `leitner-session.js:996–1072`.

- Stats: time (`Mm Ss`), cards seen, first-try Got-it %, best streak ✅
- Top misses: top-5 by miss count, with term + truncated def preview ✅
- "Boss Mode" button (drills today's failed list, 10 min, mode='boss', skips traps) ✅
- "Close out" button ✅
- Tomorrow's deck count: `(todayMisses + todayShakies)` as the seed; fresh unseen mixes in next session via `buildQueue` ✅

**NEW work**: none.

---

## H. Persistence

**STATUS: DONE.**

- Debounced 200ms save: `persistSession()` at `leitner-session.js:135–139` ✅
- Resume prompt on tab reopen: `hasSavedSession()` + setup screen "Resume previous session?" block at `renderSetup()`, with explicit `lzResume` / `lzDiscard` buttons. No auto-resume ✅
- Session state cleared at end (`clearSession()`) + history rolled into `KEYS.HISTORY` ✅

**NEW work**: none.

---

## I. Files to Touch (this overhaul)

| File | Purpose | Status |
|---|---|---|
| [public/content/leitner-session.js](../public/content/leitner-session.js) | exAnswer rendering hook (already in working tree); no other engine changes | EDITED (in working tree) |
| [public/content/flashcards-extra.js](../public/content/flashcards-extra.js) | populate `exAnswer` for ~30 gap-fill cards with bare-question examples; add new gap-fill cards from Phase 4 audit (target ~50 new cards across L08/L09/L11/L12/L13) | EDITED (heavy) |
| `public/content/card-linter.js` | NEW — pure-function `lintCard(card)` module per Phase 5E. Not wired to any UI | NEW |
| [docs/redesign-plan.md](redesign-plan.md) | this document | NEW |
| [docs/coverage-audit.md](coverage-audit.md) | Phase 4 cheatsheet coverage gap report | NEW |

**Files NOT touched in this overhaul** (deliberately):
- `public/content/flashcards.js` — auto-generated from key_terms; regenerating would invalidate hand-authored data
- `public/data/lecture-guides/L*.json` — already complete
- `public/index.html` — no flashcard-system changes there
- Anything in `_archive/`, `_backups/`, `_work/`, `audit/`
- `public/content/qbank.js`, `stim-bank.js`, `stim-mode.js` — separate question-bank system, not flashcards

---

## Out-of-scope for `flashcard-overhaul-v1`

These items were in the directive but are deliberately deferred because they are either redundant with already-implemented features, require new paid services (out of autonomy bounds), or yield negligible exam-night value:

- Phase 6 schema migration on existing 282 cards (additive only; existing cards keep working)
- Phase 7 Leitner engine creation (already built)
- Phase 8 card-view layout refactor (already built)
- Phase 10 FSRS migration script (no FSRS)
- Phase 11 OpenRouter trap-card LLM generation (paid service)
- Phase 13 wire linter into editor (no editor exists)
- Phase 14 LLM trap-card distractor generation (paid service)
- Phase 17 admin "Cards to Rewrite" view (no live editor; the linter writes a report; the user can edit `flashcards-extra.js` directly)

These can be picked up in a follow-up branch after the exam.

---

## Cutover & deploy

This branch deploys to a **Cloudflare Pages preview URL** (default behavior of `wrangler pages deploy public --branch=<not main>`). Production push to `main` (live URL) is gated to manual approval — never auto-deployed.

To preview locally during authoring:
```bash
npx serve public -p 4201
```

To deploy preview:
```bash
npx wrangler pages deploy public --project-name=evolution-study-guide --branch=flashcard-overhaul-v1 --commit-dirty=true
```

To promote to production (manual, post-review):
```bash
./deploy.sh "ship flashcard-overhaul-v1: exAnswer + Ch 10-16 gap-fill"
```
