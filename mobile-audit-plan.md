# Mobile Audit Plan — BIOL 4230 Evolution Study Site

Operating on: **evolution-study-guide** (live at https://evolution-study-guide.pages.dev)

## Site identity

- Vanilla HTML/CSS/JS (no framework, no build step).
- Deployed to Cloudflare Pages via Wrangler.
- Routes (one HTML file = one route):
  - `/` (index.html) — main study guide, lecture content, study/quiz/flash/comp/stim modes
  - `/match.html` — Match Mode (timed vocab pairs game)
  - `/mastery.html` — NEW: 3-day block plan + 8 synthesis decks + retention engine + deck browser (the focus of this audit)
  - `/cheatsheet.html` — print-ready cheat sheet
  - `/guides.html` — editable study guides

## Design system extracted

### Color tokens (CSS variables, defined on `:root` and `body.day-mode`)

```
--bg #0c0e12  (day: #f5f1e8 cream)
--bg-elev #14171d (day: #ffffff)
--bg-sunk #090a0e (day: #eae4d5)
--rule #22262f (day: #d4cdb8)
--rule-strong #2e333d (day: #a89f85)
--ink #e6dfd0 (day: #1a1814)
--ink-dim #a59a83 (day: #4a4538)
--ink-faint #6b6353 (day: #7a7158)
--ink-ghost #3f3a32 (day: #c4bba0)
--accent #c89b2e   (consistent across modes)
--accent-soft #5b4412 (day: #f5e6c2)
--accent-ink #f1d278 (day: #6b4a0a)
--correct #5fa871 / --correct-soft #1a2a1e
--wrong #c86462 / --wrong-soft #2a1616
--info #7a8fa8
--warn = --accent
```

### Typography

- Display: `Fraunces` (serif, italic for emphasis)
- Body: same — `Fraunces` for long-read content
- UI: `Inter` for buttons, labels, kickers
- Mono: `JetBrains Mono` for numbers, timers, source tags
- Base size: `16px`, line-height `1.5–1.6`
- Display sizes use `clamp()` (e.g., hero title `clamp(36px, 5vw, 60px)`)
- UI labels are uppercase with `letter-spacing: 0.14–0.22em`
- Mono is tabular-numeric for stats

### Spacing & geometry

- Mastery page uses spacing tokens `--space-2..8` (8/12/16/20/24/32 px)
- index.html uses arbitrary px values inline
- Border radius: `--radius-sm 4px`, `--radius-md 8px`, `--radius-lg 12px`
- Cards: `1px solid var(--rule)` border, `--bg-elev` background, ~22px padding

### Animations

- `transition: all .15s` on hover-able elements
- Match-tile: `transform .1s, border-color .1s, background .15s`
- `@keyframes shake` for wrong-match feedback
- All keep to `transform`/`opacity`/`background` (no layout-thrash)

### Existing breakpoints

- match.html already has `@media (max-width: 720px)` and `@media (max-width: 480px)` and `@media (hover: none)`.
- mastery.html uses the same three breakpoints.
- index.html does NOT have explicit responsive breakpoints in the chrome — relies on flex-wrap.

### Component patterns

- `.btn` / `.btn.primary` / `.btn.ghost` / `.btn.danger` / `.btn-lg` / `.btn-block` (mastery.html)
- `.search-btn` and `.icon-btn` for chrome nav (index.html)
- `.tile` / `.match-tile` for grids
- `.fc-card` / `.summary-card` / `.deck-card` / `.day-card` for content cards
- `.runner-overlay` and `.break-screen` for full-screen modals
- `.app-prompt` / `.app-input` / `.app-feedback` for application blocks
- `.toast` for transient bottom-center notifications

### Existing JS state

- localStorage keys: `evol-mastery-progress-v1`, `evol-mastery-plan-v1`, `evol-mastery-lapse-v1`, `evol-theme`, `evol-match-best-*`, `evol-match-mastered-*`, `evol-mastery-*` (per-section collapses).
- No external dependencies for core UI. fonts.googleapis.com for typography only.

## Routing map for audit

| Route | Primary screens | Mobile-critical UI |
|---|---|---|
| `/index.html` | hero dashboard, chapter chips, lecture renderer, search palette | Sticky chrome bar (lots of nav buttons), search palette, lecture content readability, day/night toggle |
| `/match.html` | timed match game | 6/10/14/20/30-pair grid, mastery tracker bar, win screen |
| `/mastery.html` | 3-day plan board, 8-deck grid, runner overlay (Match → Flashcards → Mini-Match), application input, break screen, deck browser | EVERY block runner screen, match-batch grid (3 batches × 5 pairs), flashcard input keyboard handling, sticky timer in runner, break overlay |
| `/cheatsheet.html` | print sheet | Mostly print-targeted |
| `/guides.html` | editable rich-text guides | Editor on small screens |

## Mobile-critical user flows (for verification)

1. Land on `/mastery.html` → tap Day 0's first block → runner opens → match grid plays → flashcards round → mini-match → break overlay → cycle 2 → finish summary → mark block done.
2. Tap Application block → typed input → keyboard appears → input visible → Submit → fuzzy feedback → next prompt.
3. Cross-Deck Mastery Run from Mastery home.
4. Deck browser: filter by deck, search, paginate.

## Constraints and rules for fixes

- Use only existing CSS tokens. Do NOT introduce new color/font values.
- Use only existing button classes; if extending, add modifier classes that use the same tokens.
- Keep desktop unchanged — mobile fixes are additive via media queries.
- Touch targets ≥ 48 × 48 px on phones.
- Body & input font-size ≥ 16 px on mobile (prevents iOS zoom-on-focus).
- No `user-scalable=no` on viewport meta.
- No hover-only interactions.
- No microphone / audio capture.
- Match grid: 3 batches × (4×5 or 5×4) on mobile, 5×8 on tablet, 6×10 (or current responsive grid) on desktop. Tile content shows first 3–4 words ellipsized; long-press reveals full text in overlay.
- Sticky timer + progress at top of runner.
- Submit button ≥ 56 px tall, full-width.
- Break screen: timer ≥ 96 px font, full-screen overlay.
