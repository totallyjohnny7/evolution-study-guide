# Phase 0 Discovery — evolution-study-guide

## Repo tree (depth 3, abbrev)
- `/public/` — static files served directly by Cloudflare Pages
  - `exam3_review.html` (4338 lines, 152 `.fc2` cards, chapter-grouped DOM)
  - `exam3_lecture.html` (3725 lines, 197 cards in JS `FLASH` array)
  - `exam3_lecture.html` uses `SEC_META` for 7 sections (s1..s7)
  - other review pages: `exam1_review.html`, `exam2_review.html`, `textbook.html`, `index.html`
  - `/public/exam3/` → supplemental assets (figures, index)
  - `/public/images/`, `/public/img/`, `/public/textbook_images/`
  - no existing `/public/js/` directory — will be created for `esg-db.js`
- `package.json` — tiny; only runtime dep `minisearch`. Not a bundler manifest.
- `deploy.sh` — `npx wrangler pages deploy public --project-name=evolution-study-guide --branch=main`

## Build system: STATIC
No bundler. Plain HTML delivered from `/public`. Cloudflare Pages, branch `main`.

## Service worker: NONE
`grep -r 'serviceWorker\|sw.js' public/` → 0 matches. Nothing to bump.

## Key-state grep across both HTML files
Scanned for: `localStorage, sessionStorage, setItem, getItem, fsrs, FSRS, stability, difficulty, interval, reps, lapses, lastReview, due, pass, fail, correct, rating, grade, queue, learning, relearning, leech, suspend, step, answerTime, timeSpent, dk-pass, dk-miss, _score, Pass, Miss`

Results:
- **No** localStorage / sessionStorage / setItem / getItem for review state
- **No** fsrs / FSRS / stability / difficulty / lapses / lastReview / leech / suspend / answerTime / timeSpent
- `_score` — in-memory only counter object `{pass, miss, streak, best}` in both deck IIFEs
- `.dk-pass`, `.dk-miss` — UI class names for Pass/Miss buttons (matching in both files)
- `#dk-pass-btn`, `#dk-miss-btn` — button IDs wired in both files via `addEventListener('click', ...)` to `flashGrade(true|false)`
- `flashGrade(pass)` — pure UI animation + `_score` counter increment; no persistence

### Rating handlers verified (both files)
Both `#dk-pass-btn` and `#dk-miss-btn` click handlers call `flashGrade(true|false)`. `flashGrade` increments `_score`, plays animation, advances index. No persistence. Confirms **Case A (greenfield)**.

## Rating encoding
Runtime only: `_score.pass++` / `_score.miss++`. We will persist as binary string `'pass'`/`'fail'` (instruction preserves fail semantic label even though UI says Miss).

## Scheduler features present
NONE. No scheduler at all. Everything below is new.

## Sharing case: A (greenfield)
Both routes share origin `evolution-study-guide.pages.dev`. No review-state localStorage keys anywhere to migrate. We'll create ONE Dexie DB `evolution_study_guide` shared across both routes, card IDs prefixed with source: `review_<ch>_<i>` and `lecture_<sec>_<i>`. No cross-source collisions.

## UI touch-points
- `exam3_review.html`:
  - Deck engine IIFE starts at line 3852 (`// ── DECK ENGINE (v6...)`)
  - `$('dk-pass-btn').addEventListener('click', ...)` at **line 4012**
  - `$('dk-miss-btn').addEventListener('click', ...)` at **line 4013**
  - `buildDeck(filter)` at line 3875 — iterates `.fc2[data-ch=...]`
  - `_score` init at line 3871
  - `dkRender` at line 3909 (where we'll stamp `_cardShownAt`)
- `exam3_lecture.html`:
  - Deck engine IIFE starts at line 3156 (`// --- Deck engine (v6...)`)
  - Pass/Miss button wiring at **lines 3291/3292**
  - `buildDeckFromFlash(filter)` at line 3162 — iterates global `FLASH` array
  - `_score` init at line 3158
  - `dkRender` at line 3194

## Mnemonic-agent coordination
Marker string `fc-mn` was NOT present after 5 × 30s retries. Per instructions, proceeding anyway. Our edits use very specific anchors (IIFE-level Pass/Miss handler wiring) and do not touch fc2 card markup, SVG regions, or the expected `.fc-mn*` containers — non-colliding.

## Card counts
- review: 152 `.fc2` elements tagged by `data-ch` (ch3, ch4, ch13, ch14, ch19, ch20, ch21).
- lecture: 197 entries in `FLASH` tagged by `sec` (s1..s7).
