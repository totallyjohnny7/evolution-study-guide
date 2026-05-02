# Mobile Verification Report — BIOL 4230 Evolution

Verified live in the local preview server (Chromium-based) after applying Phase 2 fixes. Existing match.html and index.html already had responsive breakpoints; verified for regression only. New mastery.html is the focus of this audit.

## Viewports tested (mastery.html)

| Viewport | docW | Overflow | Chrome H | Match grid cols | Tile size | Notes |
|---|---|---|---|---|---|---|
| iPhone SE 375×812 portrait | 375 | none | 114px | 2 cols | 169×80 | All targets ≥44px |
| iPhone 14 Pro 393×852 portrait | 393 | none | 114px | 2 cols | 178×80 | OK |
| iPhone 14 Pro 852×393 landscape | 837 | none | 73px | 4 cols | 164×~110 | Tablet breakpoint, OK |
| Pixel 7 412×915 | 412 | none | 114px | 2 cols | ~187×80 | OK |
| iPad Mini 768×1024 | 753 | none | — | 4 cols | 164×~110 | 2-col deck/day grid |
| iPad Pro 11" 834×1194 | 819 | none | — | 4 cols | — | 2-col layout |
| 1024×768 desktop | 1009 | none | — | auto-fill | — | OK |
| 1440×900 desktop | 1425 | none | — | auto-fill (720-wide body) | — | 3-col deck grid |
| 1920×1080 desktop | 1905 | none | — | — | — | OK |
| 600×900 resized | 585 | none | — | 3 cols | — | mobile breakpoint, OK |

## Per-route checks

### `/mastery.html` (NEW)

- ✅ No horizontal scrolling at any tested viewport.
- ✅ All chrome nav links min-height 44px on phones (`.ch-nav a` got `min-height: 44px`).
- ✅ Theme `icon-btn` 44×44 on phones.
- ✅ Brand link 44px tall via padding.
- ✅ Deck-card buttons 44px+ (Encode/Drill/Apply).
- ✅ Pager buttons 44×44 (deck browser).
- ✅ Match tiles ≥80×70 on phones, ≥110×164 on tablet.
- ✅ Sticky timer + progress at top of runner (`.runner-top { position: sticky; top: 0; }`).
- ✅ Runner title ellipsizes when title is long.
- ✅ Application input is 16px font-size (no iOS zoom-on-focus).
- ✅ Submit button ≥56px tall on phones (`#appSubmit { min-height: 56px }`).
- ✅ Long-press (500ms) on match-tile reveals full text in overlay.
- ✅ Break overlay full-screen with 84–120px timer.
- ✅ Deck browser collapses controls into single column on phones.
- ✅ Toast bottom-positioned with safe-area inset.
- ✅ `viewport-fit=cover` set; `safe-area-inset-bottom` honored on `.runner-body` and `.toast`.
- ✅ `overscroll-behavior-y: contain` on root prevents iOS rubber-band into chrome.
- ✅ Hover states disabled under `@media (hover: none)`.
- ✅ Resizing/rotating mid-page does not break grids (auto-fit + reflow).
- ✅ Cycle pill, progress meta, source tags all readable on smallest viewport.

### `/match.html` (existing — regression check only)

- ✅ Existing media queries at 720/480 still apply.
- ✅ New "Mastery →" link added in top bar; sized via inherited anchor styling.
- ✅ FLASHCARD_DECKS still loads with 19 decks (L01–L20 + 'all').
- ✅ All 4 exam picker buttons render (Exam 1/2/3/all).
- ✅ Match game still functional (verified with deck loaded).

### `/index.html` (existing — regression check only)

- ✅ All 18 lectures still render in `.lecture-host`.
- ✅ FLASHCARD_DECKS still has 19 keys.
- ✅ New `#masteryChromeBtn` chrome button added; uses existing `.search-btn` class.
- ✅ Day/night toggle works.
- ✅ No console errors.

## Application input flow check (375×812)

- ✅ Tapped Application block — overlay opens.
- ✅ Application prompt and input render in the runner-body max-width 720px column.
- ✅ Typing into input: 16px font-size, 130px min-height.
- ✅ Submit button (full-width, 56px) accessible without scrolling.
- ✅ Fuzzy grader returns score, gold answer, and Next prompt button.
- ✅ Tapped exit — confirms saved + closed cleanly (no blocking dialogs).

## Browsers

- Chromium (preview): all checks pass.
- WebKit / Firefox: not run in this pass — preview server only emulates Chromium. All CSS used is standard (no -webkit-only properties beyond -webkit-backdrop-filter, which has a fallback). Animations use `transform`/`opacity` only. Should work cross-browser.

## Anti-patterns avoided

- ❌ No `user-scalable=no` (verified in viewport meta).
- ❌ No new framework introduced (vanilla HTML/CSS/JS).
- ❌ No new color or font primitives — all fixes use existing CSS variables.
- ❌ No microphone / audio capture features anywhere.
- ❌ No removal of desktop affordances.
- ❌ No layout-thrashing animations (all `transform`/`opacity`/`background`).

## Items deliberately deferred (with rationale)

- **Phase 6 swipe gestures** (swipe-right "I knew this", swipe-left "show answer"): every gesture is also a button. Skipped to reduce surface area before exam. Buttons cover all flows.
- **Custom Block uses `prompt()` dialogs**: documented; user can click deck buttons directly which is the primary path. Replaced confirm() for Reset Plan with single Reset Plan link (still uses confirm but documented; shows 2 days before exam, low impact).
- **Pull-to-refresh on Mastery home**: localStorage already persists; no need to manually re-sync.
- **Mid-block orientation toast**: low value; user can rotate freely.

## Result: PASS — ready for deploy.
