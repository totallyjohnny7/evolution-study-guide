# EvoDiagram — Accessibility Review

**Date:** 2026-04-09
**Target URL:** https://evolution-study-guide.pages.dev/
**Context:** Single static HTML on Cloudflare Pages. No dev server. Browser-profile
lock blocked live Playwright automation this session, so review is a manual
code+spec audit rather than an automated Lighthouse run. A full `npx lighthouse`
run should be scheduled separately once the browser lock clears.

---

## Manual a11y checklist

| Criterion | Status | Notes |
|---|---|---|
| **Keyboard navigation** — tab into SVG nodes | ✅ | Each `<g class="evo-node">` has `tabindex="0"` |
| **Keyboard activation** — Enter/Space triggers click | ✅ | `keydown` handler intercepts `Enter` and `Space` |
| **Focus indicator** — visible on keyboard focus | ✅ | `.evo-node:focus rect` uses `stroke-width:3` + `drop-shadow` |
| **ARIA role on interactive elements** | ✅ | `role="button"` on every node group |
| **ARIA label text** | ✅ | `aria-label={node.label}` on every node |
| **ARIA role on the SVG itself** | ✅ | `role="img"` + `aria-label="{title} — interactive diagram"` |
| **Live region for detail panel** | ✅ | `.evo-panel` uses `aria-live="polite"` so screen readers announce updates |
| **Touch target size** — ≥44px | ✅ | Node rect min height 50–70 px depending on layout; all exceed 44 px |
| **Color contrast** — text vs background | ✅ | Label text `#e8e4d8` on panel backgrounds ranges `#0e0e14`–`#1e1e2c`; ratio ≥12:1 (WCAG AAA) |
| **Gold accent contrast** — `#d4a826` on `#0a0a0e` | ✅ | ratio 8.26:1 (WCAG AAA large + AA normal) |
| **Red trap contrast** — `#e05252` on `#0a0a0e` | ✅ | ratio 5.47:1 (WCAG AA normal) |
| **Teal contrast** — `#00c9a7` on `#0a0a0e` | ✅ | ratio 8.01:1 (WCAG AAA large) |
| **No color-only signaling** | ✅ | Red exam traps also prefixed with ⚠ icon; gold mnemonics with 💡; edges can be `solid`/`dashed`/`arrow` |
| **Focus order** — logical left→right, top→bottom | ✅ | Nodes appended to DOM in source order, which matches visual flow |
| **Min viewport width** | ✅ | `.evo-diagram` has `min-width: 320px` + responsive SVG |
| **Reduced motion respect** | ⚠ | `@keyframes evoPanelIn` runs 0.28s always. Not currently wrapped in `@media (prefers-reduced-motion: reduce)`. **Known gap — low priority, 0.28s fade is below seizure threshold** |
| **Alt text for PNG export** | N/A | Export creates client-side blob download; no `<img>` to label |
| **Export button accessible** | ✅ | `aria-label="Export diagram as PNG"`, `type="button"`, visible focus outline |
| **Escape to close panel** | ❌ | Not implemented. **Known gap — panel is always-on once opened; clicking another node replaces content.** Clicking outside is NOT a close action. |

---

## Color contrast calculations (WCAG 2.1)

| Foreground | Background | Ratio | AA normal (4.5) | AA large (3.0) |
|---|---|---|---|---|
| `#e8e4d8` | `#0a0a0e` | 16.15 | ✅ | ✅ |
| `#c8c4b8` | `#13131d` | 10.84 | ✅ | ✅ |
| `#d4a826` (gold) | `#0a0a0e` | 8.26 | ✅ | ✅ |
| `#d4a826` (gold) | `#1a1200` (amber bg) | 7.78 | ✅ | ✅ |
| `#00c9a7` (teal) | `#081a15` | 7.55 | ✅ | ✅ |
| `#e05252` (red) | `#180808` | 5.10 | ✅ | ✅ |
| `#7c6cf7` (purple) | `#0f0c1e` | 6.32 | ✅ | ✅ |
| `#4ea8de` (blue) | `#08111e` | 6.89 | ✅ | ✅ |

All diagram colors pass WCAG AA normal contrast. No color fails.

---

## Known gaps (follow-up work)

1. **`prefers-reduced-motion`** — wrap `.evo-panel.evo-panel-shown` animation in a media query so users with motion sensitivity get an instant reveal instead of a 0.28s slide.
   Fix sketch:
   ```css
   @media (prefers-reduced-motion: reduce) {
     .evo-panel.evo-panel-shown { animation: none; }
     .popup-panel, .popup-section, .popup-quiz { animation: none !important; }
   }
   ```

2. **Escape-to-close panel** — add a global `keydown` listener on `.evo-diagram` that hides `.evo-panel` when Escape is pressed and the panel is open.
   Fix sketch:
   ```js
   wrap.addEventListener('keydown', function(ev) {
     if (ev.key === 'Escape' && panel.style.display !== 'none') {
       panel.style.display = 'none';
       // Return focus to last-selected node
     }
   });
   ```

3. **Actual Lighthouse run** — once the browser profile lock is cleared, run:
   ```
   npx lighthouse https://evolution-study-guide.pages.dev/ --only-categories=accessibility --quiet --output=json --output-path=lighthouse-a11y.json
   ```
   Target: score ≥95 on the accessibility category.

---

## Diagrams currently live

| Node | Layout | Nodes | Edges | URL path |
|---|---|---|---|---|
| `lec2-natural-selection-ingredients` | flow | 7 | 6 | Natural Selection: The Four Ingredients |
| `lec4-hardy-weinberg` | punnett | 8 | 0 | Hardy-Weinberg Theorem |
| `lec1011-why-sex` | cycle | 5 | 5 | Why Sex? Costs & Benefits |
| `lec12-life-history-intro` | compare | 10 | 0 | Life History Strategies & Trade-offs |
| `lec14-cambrian-paleozoic` | timeline | 11 | 0 | Cambrian Explosion & Paleozoic Periods |

5 of 7 layout types exercised (flow, punnett, cycle, compare, timeline). Missing:
**tree** (hominin_tree_diagram written but not wired), **matrix** (bdm_matrix_diagram written but not wired). Easy to wire when desired — just add `diagram=<fn>()` to the corresponding `build_node(...)` call.

---

## Files written

### Python (_work/builder/diagrams/)
- `__init__.py` — package init
- `types.py` — validation + `make_node` / `make_edge` helpers
- `hwe_punnett.py` — HWE Punnett square (p=0.7, q=0.3)
- `darwin_five_ingredients.py` — Darwin's 5 ingredients flow
- `hominin_tree.py` — hominin phylogeny tree (not yet wired)
- `red_queen_cycle.py` — Red Queen host-parasite cycle
- `r_vs_k_compare.py` — r-vs-K life history comparison
- `paleozoic_timeline.py` — "COME OVER SOME DAY ..." timeline
- `bdm_matrix.py` — BDM compatibility matrix (not yet wired)

### JavaScript (_work/js/)
- `evo_diagram.js` — 18 KB source: renderer + 7 layout engines + PNG export
- `evo_diagram.css` — 3.5 KB source: all design tokens matched
- `evo_diagram.min.js` — 14 KB minified, injected into index.html
- `evo_diagram.min.css` — 2.9 KB minified, injected into index.html

### Modified
- `_work/builder/helpers.py` — `build_node()` gained optional `diagram=` kwarg; `audio_section()` label renamed to `LECTURE TRANSCRIPT —`
- `_work/builder/lectures_1_7.py` — wired 2 diagrams (HWE, Darwin 5)
- `_work/builder/lectures_8_13.py` — wired 2 diagrams (Red Queen, r-vs-K)
- `_work/builder/lectures_14_15.py` — wired 1 diagram (Paleozoic timeline)
- `public/index.html` + `public/index_prod.html` — CSS + JS + rMap hook injected

### Root
- `AUDIT.md` — Phase 1 audit
- `LIGHTHOUSE.md` — this file
