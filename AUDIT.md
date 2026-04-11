# EvoDiagram — Phase 1 Audit

**Date:** 2026-04-09
**Target:** Evolution Study Guide (BIOL 4230, Dr. Travis Robbins)
**Live URL:** https://evolution-study-guide.pages.dev/

---

## 1. Architecture reality check

**Assumed by original prompt:**
React + Vite + TypeScript + Tailwind/CSS modules, `src/components/`, `src/pages/`, `npm run build`, Lighthouse.

**Actual stack:**
- **Single static HTML file**: `public/index.html` (~723 KB, ~2000 lines)
- **Embedded minified vanilla JavaScript** — one long line around line 49, defining helpers (`el()`, `NC`, `RL`), renderers (`rMap`, `rCards`, `rQuiz`, `rVis`, `rSheet`), state (`S`, `D`), and event wiring
- **Data as JSON blob** in `<script id="sd" type="application/json">...</script>` — 61 nodes, 659 questions, ~595 KB serialized
- **Build system** in `_work/builder/` — Python modules that assemble node dicts, serialize to JSON, and splice the blob into `index.html` and `index_prod.html` via string replacement
- **Deployment**: `npx wrangler pages deploy public/ --project-name=evolution-study-guide --branch=main --commit-dirty=true`
- **No node_modules, no TypeScript, no React, no build step, no bundler**

**Decision (per user: "Stay in the current stack"):**
Build EvoDiagram as a vanilla JS function group in the existing `<script>` tag. Diagram datasets become Python modules under `_work/builder/diagrams/` that emit JSON into each node's new `diagram` field. The popup renderer gets a small extension to detect and render `n.diagram`.

---

## 2. Design tokens (must match exactly)

### Color palette (from CSS)
| Role | Hex | Usage |
|---|---|---|
| Page background | `#0a0a0e` | root `<body>` |
| Panel background | `#0e0e14` / `#13131d` | popup-panel, cards |
| Section background | `#111118` / `#181824` | inner sections |
| Border subtle | `rgba(255,255,255,.06)` | dividers, panel borders |
| Border strong | `rgba(255,255,255,.08)` | hr, card outlines |
| Gold primary | `#d4a826` | headings, accents, mnemonic border |
| Gold bright | `#f0c840` | hover, secondary gold |
| Teal primary | `#00c9a7` | bullets, correct answer, primary accent |
| Teal soft | `#7fe8d8` | quiz answer text |
| Red trap | `#e05252` / `#e04040` | exam traps, warnings |
| Body text | `#c8c4b8` / `#e8e4d8` | paragraphs, strong text |
| Muted text | `#6e6a80` / `#55527a` / `#44416a` | section labels, dim text |
| Background strong | `#0a0a0e` | sidebar, full-dark |

### Node-color palette (NC map — one per rail color)
```
NC = {
  purple: {bg:'#0f0c1e', bdr:'#7c6cf7'},
  teal:   {bg:'#081a15', bdr:'#00c9a7'},
  coral:  {bg:'#1e100a', bdr:'#f07050'},
  amber:  {bg:'#1a1200', bdr:'#d4a826'},
  blue:   {bg:'#08111e', bdr:'#4ea8de'},
  gray:   {bg:'#121218', bdr:'#55526e'},
  green:  {bg:'#0a1708', bdr:'#4ade80'},
  red:    {bg:'#180808', bdr:'#e74c3c'},
  pink:   {bg:'#180a14', bdr:'#e860a8'},
}
```

### Typography
- Body/serif: `Georgia, 'Times New Roman', 'Palatino Linotype', serif`
- Mono: `'Courier New', monospace`
- **Note:** Original prompt says "Cormorant Garamond" — this is **incorrect**; the site uses Georgia. EvoDiagram will match Georgia.

### Spacing system
- Section label: 10px uppercase, letter-spacing 2px
- Section margin: `margin-bottom: 24px`
- Panel padding: `40px 48px`
- Border radius: small 4px, medium 8-10px, large 12-16px

### Existing animations (reusable)
- `fadeUp` (0.2s ease)
- `sectionIn` (0.28s ease with stagger)
- `slideIn` (0.26s cubic-bezier)
- `quizReveal` (0.32s with delay)
- `mnemonicPulse` (3.5s infinite golden glow)

---

## 3. Component patterns in use

### `el()` helper (the universal factory)
```
el(tag, {className, style, onClick, ...attrs}, optionalTextContent)
```
Creates a DOM element with attrs and optional text. Used for every DOM creation.

### Rendering pattern
Each tab has a single function: `rMap(ct)`, `rCards(ct)`, `rQuiz(ct)`, `rVis(ct)`, `rSheet(ct)`. Takes a container element, appends children. Container is the main content div `.ct`.

### Popup structure (current Map tab)
```
.popup-panel
  ├── .popup-header (h2 title, subtitle)
  └── .popup-body
        ├── .popup-section* (CORE CONCEPT, then slide sections)
        │     ├── .popup-section-label (tiny uppercase)
        │     └── .popup-section-body (prose with bullets/numbered/dividers)
        ├── .popup-examples (if p.examples)
        ├── .popup-warnings (if p.warnings, red callouts)
        ├── .popup-mnemonic (if p.mnemonic, gold box)
        └── .popup-quiz (if n.quiz, practice question card)
```

### Existing visual system
The node schema already has a `visual` field used by `rVis` (Visual tab) and `rSheet` (Sheet tab):
- `visual.svg` — inline SVG string, rendered directly
- `visual.extraSvgs` — array of `{title, svg}` for multiple diagrams per node
- `visual.regions` — colored-box text cards (used when there's no real diagram)
- `visual.type` — hint string for render mode
- `visual.mnemonic`, `visual.trap` — extra annotations

**Key finding:** there is **no** existing interactive (click-to-reveal) diagram component. The `visual.svg` field just dumps raw SVG. EvoDiagram will be the missing piece: a proper interactive diagram system.

**Integration strategy:** introduce a new top-level field `n.diagram` (not `n.visual`, to avoid breaking existing SVG nodes). When `n.diagram` is present, the Map popup renderer adds an extra section that invokes the new `renderEvoDiagram()` function. The Visual tab gets a similar hook.

### State management
- Single global `S` object: `{sel, qI, qSc, qDk, qO, qChapter, fI, fSide, ...}`
- Global `D` = data blob loaded once from `<script id="sd">`
- Re-render pattern: mutate `S`, then call `render()` which clears `.ct` and calls the appropriate `rX()` function

### Event model
- Click handlers passed via `el(..., {onClick: fn})`
- Sidebar item click → update `S.sel` → `render()`
- No event delegation; direct handlers

---

## 4. Build pipeline

### Source modules (`_work/builder/`)
- `helpers.py` — `load_lec()`, `slide_section()`, `slides_to_sections()`, `build_node()`, scrubbers
- `lectures_1_7.py`, `lectures_8_13.py`, `lectures_14_15.py` — node generators
- `lectures_16_speciation.py` — ch13 speciation nodes (ballistic string-concat format with custom SVGs)
- `final_extras.py` — biogeography/conservation/human-evo/evo-medicine (pulls from `_extracted_data.json`)
- `build.py` — assembles all nodes, validates, writes `data.json`, splices blob into `index.html` + `index_prod.html`
- `validate.py` — post-build sanity checks (URLs, table fragments, quiz counts, distractors)
- `_core_concepts.json` — post-hoc CORE CONCEPT section overrides (injected in `build.py.main()`)

### Deploy
```
cd C:\Users\johnn\Desktop\evolution-study-guide
npx wrangler pages deploy public/ --project-name=evolution-study-guide --branch=main --commit-dirty=true
```
**Do not use `--branch=production` or `--branch=master`** — those create Preview deployments only. Only `main` updates the canonical `*.pages.dev` URL.

---

## 5. Proposed implementation plan

### New files to write (all on disk, none inline)

**JavaScript (inside `public/index.html` inside the minified `<script>` block):**
Add these helper functions right before `function rMap(ct){`:

```
function renderEvoDiagram(containerEl, diagram, nc){...}
function _evoLayoutFlow(nodes, edges, w, h){...}
function _evoLayoutTree(nodes, edges, w, h){...}
function _evoLayoutCycle(nodes, w, h){...}
function _evoLayoutCompare(nodes, w, h){...}
function _evoLayoutTimeline(nodes, w, h){...}
function _evoLayoutPunnett(nodes, w, h){...}
function _evoLayoutMatrix(nodes, w, h){...}
function _evoExportPng(svgEl, title){...}
```

Then in `rMap(ct)`, after the `p.sections` forEach, add:
```
if(n.diagram){var dSec=el('div',{className:'popup-section'});dSec.appendChild(el('div',{className:'popup-section-label'},'INTERACTIVE DIAGRAM'));var dBody=el('div',{});renderEvoDiagram(dBody, n.diagram, nc);dSec.appendChild(dBody);pb.appendChild(dSec);}
```

**CSS (in the existing `<style>` block):**
```
.evo-diagram{...}
.evo-node{...}
.evo-node:hover{...}
.evo-node:focus{...}
.evo-edge{...}
.evo-panel{...}  (expand panel shown when node clicked)
.evo-panel-detail{...}
.evo-panel-mnemonic{...}
.evo-panel-trap{...}
.evo-export-btn{...}
@keyframes evoPanelIn{...}
```

**Python builder modules (`_work/builder/diagrams/`):**
- `__init__.py`
- `types.py` — validation helpers
- `hwe_punnett.py` — HWE Punnett square dataset (p=0.7, q=0.3 from lecture)
- `darwin_five_ingredients.py` — Darwin's 5 requirements for natural selection
- `hominin_tree.py` — Ardi → Australopithecus → Homo lineages
- `red_queen_cycle.py` — Red Queen cycle (parasite/host frequency-dependent)
- `r_vs_k_compare.py` — r-selected vs K-selected comparison matrix
- `paleozoic_timeline.py` — "COME OVER SOME DAY MAYBE PICKING UP HARD CASH" timeline
- `bdm_matrix.py` — Bateson-Dobzhansky-Muller compatibility matrix

**Builder integration:**
- Extend `helpers.py` `build_node()` to accept optional `diagram=None` kwarg
- Add `diagram` to the required-keys set in `validate()` (as optional)
- Each relevant lecture module passes `diagram=` where appropriate

### Data schema (the new `n.diagram` field)
```python
diagram = {
    'type': 'flow' | 'tree' | 'cycle' | 'compare' | 'timeline' | 'punnett' | 'matrix',
    'title': str,
    'nodes': [
        {
            'id': str,
            'label': str,         # short text on the node
            'detail': str,        # expanded text when clicked
            'mnemonic': str|None, # optional 💡 hook
            'watchOut': str|None, # optional ⚠ trap
            'x': float|None,      # optional 0-1 layout hint
            'y': float|None,
            'color': str|None,    # one of NC palette keys or hex
        },
        ...
    ],
    'edges': [  # optional
        {
            'from': str,
            'to': str,
            'label': str|None,
            'style': 'solid' | 'dashed' | 'arrow',
        },
        ...
    ],
    'mnemonic': str|None,  # overall diagram mnemonic shown at top
}
```

### Layout engines (vanilla JS)
Each layout takes `(nodes, edges, width, height)` and returns positioned nodes in the form `[{...node, _x, _y}]`. Layout decisions:

| Type | Algorithm |
|---|---|
| `flow` | Horizontal DAG: topological order × column, rank-based rows; straight-line edges |
| `tree` | Top-down tidy tree (Reingold-Tilford simplified); children centered under parents |
| `cycle` | Nodes evenly spaced on a circle; edges curve around the center |
| `compare` | Two columns (split nodes by `color` or odd/even); horizontal match-lines |
| `timeline` | Single horizontal axis, nodes spaced by `x` coordinate (0-1); events above/below to avoid collisions |
| `punnett` | 2×2 / 3×3 grid. Row/column headers from first N nodes; cells from remaining |
| `matrix` | N×N grid with row/col headers; cells render as colored intensity blocks |

### Interaction model
- Each node: `<g class="evo-node" role="button" tabindex="0" aria-label={label}>` with `<rect>` + `<text>`
- On click OR Enter key: toggle an adjacent `.evo-panel` div (not SVG) that slides down below the diagram with `detail`, `mnemonic`, `watchOut`
- On hover OR focus: gold glow via CSS filter `drop-shadow(0 0 8px #d4a826)` + tooltip
- `44px` minimum touch targets enforced by minimum rect height of 44px
- Responsive: SVG `viewBox="0 0 800 N"` with `preserveAspectRatio="xMidYMid meet"`; min 320px wrapper
- **PNG export**: serialize SVG → `btoa()` → `data:image/svg+xml` → draw to canvas → `canvas.toBlob()` → anchor download

---

## 6. Phase-by-phase file deliverables

### Phase 2 (types + layout)
```
_work/builder/diagrams/__init__.py
_work/builder/diagrams/types.py
public/index.html               (patch: add layout JS functions to existing script block)
```

### Phase 3 (rendering + interactivity)
```
public/index.html               (patch: add renderEvoDiagram fn + CSS rules)
```

### Phase 4 (7 datasets)
```
_work/builder/diagrams/hwe_punnett.py
_work/builder/diagrams/darwin_five_ingredients.py
_work/builder/diagrams/hominin_tree.py
_work/builder/diagrams/red_queen_cycle.py
_work/builder/diagrams/r_vs_k_compare.py
_work/builder/diagrams/paleozoic_timeline.py
_work/builder/diagrams/bdm_matrix.py
```

### Phase 5 (wire into real nodes)
```
_work/builder/lectures_1_7.py             (patch: lec4-hardy-weinberg diagram=hwe_punnett)
_work/builder/lectures_8_13.py            (patch: lec8-eye-evolution or lec9-antagonistic-arms diagram=red_queen_cycle; lec12-life-history-intro diagram=r_vs_k_compare)
_work/builder/lectures_14_15.py           (patch: lec14-cambrian-paleozoic diagram=paleozoic_timeline)
LIGHTHOUSE.md                              (a11y score + fixes applied)
```

---

## 7. Open questions for user before Phase 2

1. **Which nodes to wire in Phase 5?** Recommendation: HWE (`lec4-hardy-weinberg`), Red Queen (`lec1011-why-sex`), r-vs-K (`lec12-life-history-intro`), Paleozoic timeline (`lec14-cambrian-paleozoic`). That's 4 real nodes, covering 4 of the 7 layout types, spread across exam sections.

2. **Lighthouse target?** This is a static HTML on Cloudflare Pages — no dev server. I can either:
   a) Run `npx lighthouse https://<deploy-url>/ --output=json --quiet` against the deploy URL after each phase
   b) Skip Lighthouse for now and write manual a11y checks to `LIGHTHOUSE.md` (aria roles, focus order, contrast ratios, keyboard nav)
   Default: (a) against the deploy URL.

3. **PNG export libs?** The prompt says "no heavy libs." The native approach (`XMLSerializer` → `btoa` → canvas → `toBlob`) works in Chrome/Firefox/Safari/Edge without any dependency. Confirming: **no** `html2canvas`, `dom-to-image`, `d3`, etc.

4. **Typography discrepancy.** Prompt says "Cormorant Garamond serif"; the actual site uses Georgia. Confirming: **match Georgia** (the real site), not Cormorant. If you want me to swap the whole site to Cormorant Garamond, that's a separate task.

---

## 8. Status

- [x] Phase 1 audit written to disk
- [ ] Phase 2 — awaiting user approval of this plan + answers to questions 1–4 above
- [ ] Phase 3
- [ ] Phase 4
- [ ] Phase 5

**Blocker:** need approval to proceed to Phase 2.
