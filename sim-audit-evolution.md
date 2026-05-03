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
| Critical (live runtime crash) | 1 | **1** | qbank.js init type bug |
| Stale UI copy | 1 | **1** | mastery.html "Eight new decks" / "8 decks" → 9 (incl. Cloze) |
| Inconsistency | 1 | **1** | study-guide.html (cumulative final) added to both injectors and re-injected — now has Cloze + mobile blocks like the per-exam guides |
| Stale localStorage prefixes | 8 keys | **8** | All `biol-*` keys renamed to `evol-*` in index.html. One-shot migration block preserves existing user progress (copies biol-X → evol-X at boot, idempotent via `evol-ls-migrated-v1`). Legacy `biol-*` keys are left intact so leitner-session.js's own migration path keeps working. |
| Dead-weight asset | 1 | **1** | `flashcards.js.bak-pre-port-20260501` (178 KB) `git mv`'d out of `public/content/` into `_backups/`. Not in deploy. |
| All other audit checks | n/a | n/a | All pass — see "Verifications" below |

**Final score: 12/12 audit items resolved. Zero issues outstanding.**

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

## Issue 2 (FIXED): stale "Eight new decks" / "8 decks" copy in mastery.html

**File:** `public/mastery.html` (lines 924, 929 of pre-fix)

The hero sub-paragraph and the `#masteryStatHero` placeholder both said "Eight new decks" / "8 decks", listing only the original eight synthesis decks (Scenarios, Mechanisms, Game Theory, Compare/Contrast, Calculations, Empirical Examples, Phylogeny, Cause-and-Effect). The new **Cloze** deck (54 cards) makes nine decks total.

The dynamic `renderDecks()` JS at line 1250 already overwrites `#masteryStatHero` with the live count once `MASTERY_READY` resolves (so the live UX was correct after a few hundred ms). But the static fallback was visible during the FOUC window, and the prose paragraph never re-rendered.

**Fix:** Updated both strings to "Nine decks…" and "9 decks", and added "Cloze" to the enumerated list:
```html
<p class="hero-sub">Block-based study built for 90% retention at 72h. Nine decks of synthesis cards — Scenarios, Mechanisms, Game Theory, Compare/Contrast, Calculations, Empirical Examples, Phylogeny, Cause-and-Effect, Cloze — plus a three-round Match → Flashcards → Mini-Match pipeline …</p>
…
<span id="masteryStatHero">— cards across 9 decks</span>
```

**Status:** Deployed and verified via curl that the live `mastery` page now serves "Nine decks" and "9 decks".

---

## Issue 3 (FIXED): study-guide.html (Cumulative Final) lacks injected Cloze Mode + mobile CSS

**File:** `public/study-guide.html`

`scripts/inject-cloze-mode.js` and `scripts/inject-mobile-css.js` enumerated only the three per-exam guides (`study-guide-exam{1,2,3}.html`) in their `FILES` array. The Cumulative Final at `study-guide.html` shares the same DOM (`<div class="doc" id="doc" contenteditable>`) and is the page the user will reach for the May 4 final, but did not get the cloze toggle or mobile fix.

**Fix:** Added `'study-guide.html'` to the `FILES` array in both injector scripts:

```js
const FILES = [
  'study-guide-exam1.html',
  'study-guide-exam2.html',
  'study-guide-exam3.html',
  'study-guide.html', // cumulative final (added 2026-05-02 per audit Issue 3)
];
```

Re-ran both injectors:
```
✓ Injected mobile CSS into study-guide{,-exam1,-exam2,-exam3}.html  (4/4)
✓ Injected Cloze Mode into study-guide{,-exam1,-exam2,-exam3}.html  (4/4)
```

**Verified:** Cumulative-final page loads cleanly; clicking 🎯 Cloze Mode toggles **297** bolded terms into clickable blanks; clicking a blank reveals it; LS key `evolution-cloze-Cumulative-Final-All-units-BIOL-4230-Evo` persists per-page. Zero `__bootErrors`.

---

## Issue 4 (FIXED): `biol-*` localStorage keys leftover from biol3020 port

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

**Fix:** Renamed every active use of `biol-*` LS keys in `index.html` to `evol-*`. Added a one-shot migration block at the top of `index.html` (immediately after the boot-error trap) that copies each legacy `biol-X` value into `evol-X` if `evol-X` is missing — so existing user progress is preserved across the rename. Idempotent via the `evol-ls-migrated-v1` sentinel:

```js
(function migrateLsKeys() {
  try {
    if (localStorage.getItem('evol-ls-migrated-v1') === '1') return;
    const pairs = [
      ['biol-fc-progress-v2',    'evol-fc-progress-v2'],
      ['biol-fc-filter-v1',      'evol-fc-filter-v1'],
      ['biol-fcw-on',            'evol-fcw-on'],
      ['biol-fcw-deck',          'evol-fcw-deck'],
      ['biol-fcw-seen-v2',       'evol-fcw-seen-v2'],
      ['biol-tweaks-v1',         'evol-tweaks-v1'],
      ['biol-fc-cards-v1',       'evol-fc-cards-v1'],
      ['biol-fc-instructions-v1','evol-fc-instructions-v1'],
    ];
    pairs.forEach(function (p) {
      try {
        var v = localStorage.getItem(p[0]);
        if (v !== null && localStorage.getItem(p[1]) === null) {
          localStorage.setItem(p[1], v);
        }
      } catch (_) {}
    });
    localStorage.setItem('evol-ls-migrated-v1', '1');
  } catch (_) {}
})();
```

The legacy `biol-*` keys are LEFT in localStorage so `content/leitner-session.js`'s own format migration (which still reads `biol-fc-progress-v2`) continues to work — that path was never broken and changing it would risk losing flashcard mastery records.

**Verified:**
1. Seeded test biol-* values, removed evol-* equivalents, deleted the migration sentinel, then reloaded — all four evol-* keys came back populated with the biol-* contents (correct copy).
2. Set `evol-fcw-on=0` (newer user choice) but `biol-fcw-on=1` (stale legacy), reloaded with sentinel intact — the user's `evol-fcw-on=0` was preserved (no clobber). Idempotent ✓.
3. Toggled the live flashcards widget on/off — value lands in `evol-fcw-on`, not `biol-fcw-on`. New writes only touch the new key.

---

## Issue 5 (FIXED): pre-port flashcards backup ships in deploy

**File:** moved `public/content/flashcards.js.bak-pre-port-20260501` (178 KB) → `_backups/flashcards.js.bak-pre-port-20260501`

This was a backup of `flashcards.js` from before the May 1 biol→evol port. Nothing references it (no `<script src=...>`, no fetches), so it had zero runtime effect — but Cloudflare Pages deploys the entire `public/` tree, so the file was publicly downloadable from the live site as 178 KB of dead weight.

**Fix:** `git mv public/content/flashcards.js.bak-pre-port-20260501 _backups/flashcards.js.bak-pre-port-20260501` — the file is preserved in the repo (recoverable) but no longer in the deploy. Verified post-deploy: `curl -I https://evolution-study-guide.pages.dev/content/flashcards.js.bak-pre-port-20260501` returns the SPA fallback (`Content-Type: text/html`, 387 KB index.html) instead of the 178 KB JS — confirming the file is gone from `/content/` on the live site.

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

## Files modified across both audit passes

| File | Change |
|---|---|
| `public/content/qbank.js` | type-safe array init (Issue 1) |
| `public/mastery.html` | "Eight new decks"→"Nine decks · Cloze", "8 decks"→"9 decks" (Issue 2) |
| `public/scripts/inject-cloze-mode.js` | added `'study-guide.html'` to `FILES` (Issue 3) |
| `public/scripts/inject-mobile-css.js` | added `'study-guide.html'` to `FILES` (Issue 3) |
| `public/study-guide.html` | re-injected → now has CLOZE + MOBILE blocks (Issue 3) |
| `public/study-guide-exam{1,2,3}.html` | re-injected (no semantic change, regenerated for parity) |
| `public/index.html` | (a) one-shot `migrateLsKeys()` IIFE at top of head; (b) all 8 active uses of `biol-*` keys renamed to `evol-*` (Issue 4) |
| `_backups/flashcards.js.bak-pre-port-20260501` | moved out of `public/content/` (Issue 5) |

## Deploy

```
$ ./deploy.sh "audit fix: QBANK is array (was object), update '8 decks' → 9 decks in mastery hero"
✨ Success! Uploaded 0 files (98 already uploaded) (0.14 sec)
🌎 Deploying...
✨ Deployment complete! Take a peek over at https://8e39cb66.evolution-study-guide.pages.dev
✔ Deploy complete. Live URL: https://evolution-study-guide.pages.dev/
```

Commit: `b9df730 audit: window.QBANK must be Array, not {} (fixes runtime TypeError on every index.html load — bank.forEach @8341, (window.QBANK || []).forEach @7837)`

## Live verification (post-deploy curl)

| Check | Result |
|---|---|
| `https://evolution-study-guide.pages.dev/content/qbank.js` | Serves the array-safe init line: `window.QBANK = Array.isArray(window.QBANK) ? window.QBANK : [];` |
| `https://evolution-study-guide.pages.dev/mastery` hero | Shows `Nine decks of synthesis cards — … Cloze` and `— cards across 9 decks` |
| `https://evolution-study-guide.pages.dev/data/mastery/cloze.json` | HTTP 200, `deckId: cloze`, 54 cards |
| `https://evolution-study-guide.pages.dev/study-guide` | HTTP 200; HTML includes `BEGIN CLOZE MODE` + `END CLOZE MODE` + `id="mobile-responsive-styles"` markers |
| `https://evolution-study-guide.pages.dev/` (index) | Includes `migrateLsKeys` IIFE and zero active `biol-*` LS reads (only the migration source listing) |
| `https://evolution-study-guide.pages.dev/content/flashcards.js.bak-pre-port-20260501` | SPA fallback (HTML) — file is gone from `/content/` on the live deploy |

## Local simulation (preview server `localhost:4201`)

End-to-end smoke test running each fix back-to-back. Console-error count stayed at **0** throughout.

| Test | Result |
|---|---|
| Reload `index.html` after seeding `biol-*` keys, removing `evol-*` equivalents, clearing `evol-ls-migrated-v1` | All four `evol-*` keys repopulated from `biol-*` sources; `evol-ls-migrated-v1=1`; `__bootErrors=[]`. |
| Reload again with `evol-fcw-on=0` and `biol-fcw-on=1` (sentinel intact) | `evol-fcw-on` stayed at `0` — migration is idempotent and does not clobber later writes. |
| Load `mastery.html` | 9 decks loaded / 324 cards; hero shows "0 / 324 truly mastered · 9 decks"; flashcards button labeled "📚 Flashcards (Leitner)". |
| Programmatically click `#flashcardsBtn` | Runner overlay opens with title "Flashcards (Leitner) · All Decks", 30 cards across `cycle 1/3`; cloze cards (with `____`) appear in the rendered match grid alongside other deck types. |
| Load `match.html` | 4-button exam picker, splash visible, no boot errors. |
| Load `study-guide.html` (cumulative final) | Toggle 🎯 Cloze Mode on → **297** bolds → 297 `.cloze-blank` spans; click first blank → `.revealed` class added. Toggle off → 0 blanks; original DOM restored; LS key `evolution-cloze-Cumulative-Final-All-units-BIOL-4230-Evo` written. |
| Load `study-guide-exam1.html` | 82 blanks / 82 bolds, toggle on/off clean, no errors. |
| Load `study-guide-exam2.html` | 102 blanks / 102 bolds, clean. |
| Load `study-guide-exam3.html` | 113 blanks / 113 bolds, clean. |
| Toggle flashcards widget on `index.html` (`window.toggleFcw()`) | Sets `evol-fcw-on=1`; toggling off sets `evol-fcw-on=0`; `evol-fcw-deck` reads the migrated value `L05`. No writes to any `biol-*` key. |
| `preview_console_logs(level: 'error')` after full session | "No console logs." (zero errors) |
| `preview_console_logs(level: 'warn')` after full session | "No console logs." (zero warnings) |
