# Sim Audit — Evolution Study Guide

**Date:** 2026-05-02
**Live URL:** https://evolution-study-guide.pages.dev
**Repo:** `C:\Users\johnn\Desktop\School\Evolution_EVOL4230\evolution-study-guide\`
**Method:** Line-by-line audit of `public/` HTML files plus all referenced JS / JSON.
            Cross-checked against `__bootErrors` reported in localStorage (two real
            uncaught TypeErrors at runtime).

## Summary

| Severity | Found | Fixed | Notes |
|---|---|---|---|
| Critical (live runtime crash) | 1 | 1 | qbank.js init type bug |
| Inconsistency | 1 | 0 | study-guide.html (cumulative final) lacks Cloze + mobile injectors — flagged, not fixed (out of scope per task) |
| Stale localStorage prefixes | 8 keys | 0 | `biol-*` keys leftover from biol3020 port — flagged, NOT fixed (would lose user progress) |
| All other audit checks | n/a | n/a | All pass — see "Verifications" below |

---

## Issue 1 (CRITICAL — fixed): `window.QBANK` initialized as object, not array

**File:** `public/content/qbank.js` (lines 3-4 of original)

**Reproduction:** Every page load of `index.html` (the main study site).

**Root cause:** The stub initialized `window.QBANK = window.QBANK || {}` (object). Three locations in `index.html` consume QBANK with `.forEach`:
- L6829 — `bank.forEach(q => { (byCh[q.chapter] = byCh[q.chapter] || []).push(q); });`
- L7837 — `(window.QBANK || []).forEach(q => { ... });`
- L8341 — `bank.forEach(q => { if (q.id) byId[q.id] = q; });`

L6829 is gated by `if (!bank.length) return;` (line 6823) which short-circuits because `{}.length` is `undefined`, so it never crashes.
But **L7837 and L8341** have no such guard, so they call `.forEach` on `{}` → `TypeError: bank.forEach is not a function`. These are the exact two errors reported in `__bootErrors`.

**Fix:** Already on disk (had been edited locally pre-audit but never committed/deployed). Confirmed via `curl https://evolution-study-guide.pages.dev/content/qbank.js` that the LIVE site still has the broken `{}` version. Final fix:

```js
/* QBANK must be an Array — index.html iterates with .forEach (lines ~6829, 7837, 8341).
   Initializing as {} caused TypeError "forEach is not a function" on every page load. */
window.QBANK = Array.isArray(window.QBANK) ? window.QBANK : [];
```

**Status:** Deployed in this audit pass.

---

## Issue 2 (FLAGGED — not fixed): study-guide.html (Cumulative Final) lacks injected Cloze Mode + mobile CSS

**File:** `public/study-guide.html`

`scripts/inject-cloze-mode.js` and `scripts/inject-mobile-css.js` enumerate only the three per-exam guides (`study-guide-exam{1,2,3}.html`) in their `FILES` array. The Cumulative Final at `study-guide.html` shares the same DOM (`<div class="doc" id="doc" contenteditable>`) and is the page user will reach for the May 4 final, but does not get cloze toggle or mobile fix.

**Why not fixed:** The audit task explicitly enumerates "3 study guides" and "Don't add features." Adding the file to both injectors is functionally a parity fix, but is a feature increase relative to the task scope. Flagging here so user can decide.

**Suggested fix (not applied):** add `'study-guide.html'` to the `FILES` arrays in both injector scripts and re-run.

---

## Issue 3 (FLAGGED — not fixed): `biol-*` localStorage keys leftover from biol3020 port

`NEXT_STEPS.md` notes the prefix should have been renamed `biol-` → `evol-`. Eight key prefixes still use `biol-` and would cross-pollute localStorage if user visits both the cell-bio and evolution sites in the same browser:

| File:Line | Key |
|---|---|
| index.html:6558 | `biol-fc-progress-v2` |
| index.html:6559 | `biol-fc-filter-v1` |
| index.html:7546 | `biol-fcw-deck` |
| index.html:7602 | `biol-fcw-on` |
| index.html:7615 | `biol-fcw-deck` (second use) |
| index.html:7742 | `biol-fcw-on` (second use) |
| index.html:7749 | `biol-fcw-seen-v2` |
| index.html:8776 | `biol-tweaks-v1` |
| index.html:9325 | `biol-fc-cards-v1` |
| index.html:9326 | `biol-fc-instructions-v1` |
| content/leitner-session.js:123 | `biol-fc-progress-v2` (intentional migration source — leave alone) |

**Why not fixed:** Renaming would silently drop any user's existing flashcard progress, widget state, and authored tweaks unless coupled with a migration. That's a refactor with risk; the audit task is "fix what's broken." The current keys ARE functional. Flagging only.

---

## Verifications (all PASS)

### A. Cloze deck JSON sanity (54 cards)
Validated via Node:
```
deckId: cloze
label: Cloze
cards: 54
issues: 0   (every card has term, definition, sourceTag; every term contains "____")
```

### B. `content/mastery-decks.js` DECK_FILES order
`['mechanisms','scenarios','game-theory','compare-contrast','calculations','empirical','phylogeny','cause-effect','cloze']` — cloze added at the end.

### C. Flashcards (Leitner) button — mastery.html
`document.getElementById('flashcardsBtn')` exists at line 946.
Click handler at line 1300 calls `beginRun({ type: 'drill', deckId: 'all', crossDeck: true, title: 'Flashcards (Leitner) · All Decks' })`. `beginRun` at line 1411 handles the `'all' / crossDeck` branch correctly. No errors.

### D. study-guide-exam{1,2,3}.html — injected blocks intact
- All 3 files have exactly 1 occurrence of `BEGIN CLOZE MODE`, 1 of `END CLOZE MODE`, 1 of `mobile-responsive-styles`.
- `escapeRe` function at line 1676 / 1836 / 1906 correctly ends on `'\\$&'`.

### E. `bank.forEach` and `QBANK` references — full grep
Only locations are the three index.html references already covered by the qbank.js fix (Issue 1) and the qbank.js stub itself.

### F. No duplicate function definitions in mastery.html
Each function (`beginRun`, `runMatchRound`, `runFlashRound`, `runApplicationRound`, `fuzzyGrade`, `escapeHtml`, etc.) defined exactly once.

### G. No TODO / FIXME / HACK / XXX / deprecated in code
Single hit is the literal word "deprecated" inside lecture content (`_importance_g4.js:582`, "Old name K-T (Tertiary, deprecated)") — content text, not code.

### H. Mastery.html storage keys are evol-prefixed
`STORAGE.PROGRESS = 'evol-mastery-progress-v1'`, `PLAN = 'evol-mastery-plan-v1'`, `LAPSE = 'evol-mastery-lapse-v1'`. Theme key `evol-theme`. No collisions.

### I. Cross-references — match.html
Linked from mastery.html (chrome nav + "Match Mode" inline link), guides.html (implicit via index nav), index.html. All references work; no broken redirects.

### J. APP_PROMPTS deck coverage
Mastery.html `APP_PROMPTS` dict (line 1760) covers 8 of 9 decks. The new `cloze` deck falls through to the default `{ prompt: c.term, gold: c.definition, ask: 'Recall and explain.' }` — works correctly because cloze cards are already a sentence with a blank, and the gold answer is the missing word.

---

## Files modified this pass

- `public/content/qbank.js` — type-safe initialization (Issue 1 fix).

## Files NOT modified (intentionally)

- `public/study-guide.html` — Issue 2, flagged.
- `public/index.html` — Issue 3, flagged (10 stale `biol-` keys).
- All other public/ files — verified clean.

## Deploy

`./deploy.sh "audit: ensure window.QBANK is array (fixes runtime TypeError on every index.html load)"`
