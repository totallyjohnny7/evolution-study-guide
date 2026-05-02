# Mobile Audit Report — BIOL 4230 Evolution

Audited at viewports: 375×812, 768×1024, 1440×900. Routes: `/`, `/match.html`, `/mastery.html`.

## Issues found

### `/mastery.html` (the new page)

| # | Viewport | Severity | Issue | Fix |
|---|---|---|---|---|
| M1 | 375 | ⚠ | Chrome nav links measure 36px tall (≥44 required for touch) | Add `min-height: 44px` on `.ch-nav a` at ≤720px |
| M2 | 375 | ⚠ | Theme `icon-btn` is 36×36 | Bump `width/height: 44px` at ≤720px |
| M3 | 375 | ⚠ | Pager buttons 32–35×40 | Bump to ≥44 at ≤720px (already had `min-height: 40px`; raise to 44 + min-width 44) |
| M4 | 375 | ⚠ | Brand link "Evol. / Mastery" wraps onto multiple lines (130×27) | Force single-line via `white-space: nowrap` and constrain hierarchy |
| M5 | 375 | minor | Inline anchor "Reset plan" (16px tall) | Acceptable as inline text link, no change |
| M6 | 375 | ⚠ | Application input — no scrollIntoView on focus → keyboard could cover input | Add scrollIntoView on focus + safe-area inset bottom |
| M7 | 375 | ⚠ | Submit button is `btn primary` (44px tall); spec wants ≥56px on mobile | Use `btn-lg` style, full-width on mobile |
| M8 | 375 | ⚠ | Match grid: tiles 169×64–78px. Already ≥70 on width but height inconsistent | Set `min-height: 80px` on mobile to give predictable touch area |
| M9 | 375 | minor | Long-press to reveal full term/def works in code; verify timing on touch | Already implemented (500ms) |
| M10 | 375 | ⚠ | Custom Block button uses `prompt()` which is mobile-hostile | Replace with a small picker UI; deferred — keep but document |
| M11 | 375 | ⚠ | Break overlay timer font is `clamp(72px, 14vw, 120px)` — works but center alignment can clip on very small screens | Accept; clamp keeps 72px minimum |
| M12 | 768 | OK | 2-column grid for plans + decks | No change |
| M13 | 1440 | OK | Layout fine |

### `/match.html`

Already has `@media (max-width: 720px)` with grid changes, but pre-existing buttons in `.controls` are 32×32. **NOT MODIFIED in this pass per "do not touch existing decks" constraint** — only smoke-tested for regression. Existing match-mode behavior unchanged; new "Mastery →" link added (44px+ via inherited anchor sizing).

### `/index.html`

Pre-existing site. Already complex with chrome nav, lots of buttons. **NOT MODIFIED in this pass** beyond the single new "Mastery" chrome button. Verified the new button matches existing `search-btn` sizing on mobile (which is already responsive in the existing CSS).

## Phase 2 — Fixes applied to mastery.html

All using existing CSS variables and tokens.

```css
/* Touch targets ≥44px at ≤720px */
@media (max-width: 720px) {
  .ch-nav a { min-height: 44px; }
  .icon-btn { width: 44px; height: 44px; }
  .browser-pager .btn { min-width: 44px; min-height: 44px; }
  .match-tile { min-height: 80px; }
  .brand { white-space: nowrap; }
  .app-input { font-size: 16px; }
  /* primary submit on application gets bumped */
  .btn-lg, button#appSubmit { min-height: 56px; }
}
@supports (padding: env(safe-area-inset-bottom)) {
  .runner-body { padding-bottom: calc(40px + env(safe-area-inset-bottom)); }
}
```

## Phase 3 — Match grid layout per viewport

- ≤480px: `grid-template-columns: repeat(2, 1fr)` (already in place; was 5×5 batches before).
- 481–720px: 3-col grid (was previously `auto-fill, minmax(140px, 1fr)`; explicit 3 col on phones gives bigger tiles).
- 721–1023px: 4-col grid (tablet).
- ≥1024px: `repeat(auto-fill, minmax(140px, 1fr))` (existing desktop behavior).

Tile content already shows ellipsized text with long-press overlay for full text.

## Phase 4 — Block runner mobile rules

- Sticky timer + progress at top of runner: ALREADY sticky via `.runner-top { position: sticky; top: 0; }`.
- Submit button: now `min-height: 56px` and full-width via `btn-block` modifier.
- End-of-block summary: already single-column on mobile; stats grid uses `auto-fit, minmax(120px, 1fr)`.
- Break screen: full-screen overlay, timer ≥72px with clamp.

## Phase 5 — Resize / orientation

- `viewport-fit=cover` set in viewport meta.
- All grids use `auto-fit / repeat` so they reflow without state loss.
- Runner state lives in `currentRun` (in-memory) plus `progress` in localStorage; resize doesn't lose state.
- Orientation suggestion deferred — keeping autosaves frequent.

## Phase 6 — Touch gestures

- Long-press (500ms) on match-tile reveals full term/def overlay (implemented).
- Swipe gestures deferred — buttons cover all paths; keeping scope to Phase 1–4 fixes given exam timing.

## Phase 7 — Performance

- Animations already `transform`/`opacity`-only.
- localStorage writes already debounced 5s + on `beforeunload`.
- No images on mastery.html → fast initial load.
- Fonts use `display: swap` via Google Fonts.

## Phase 9 — Deploy gate

After applying fixes:
- Re-verify 375×812 (no overflow, all touch targets ≥44 except inline text-only anchors).
- Re-verify 768×1024 (2-col grids).
- Re-verify 1440×900 (3-col day grid; auto-fit deck grid).
- Deploy via wrangler.
