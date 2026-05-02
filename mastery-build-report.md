# Mastery Build Report — BIOL 4230 Evolution Study Site

Build date: 2026-05-02

## Source decks consumed

All new Mastery cards are derived from in-repo content. No outside files, no invented terms.

| Source file | Role | Cards consumed |
|---|---|---|
| `public/content/flashcards.js` | Auto-generated vocabulary cards from `data/lecture-guides/L*.json` `key_terms`. 216 cards across 18 lectures (L01–L05, L07–L09, L11–L20). Term + definition + example + ctx. | 216 |
| `public/content/flashcards-extra.js` | Hand-authored "gap-filler" cards. ~70 cards heavy on Hardy-Weinberg math, selection types, game theory, speciation, phylogenetic groupings, Hox/dev. Includes `cardType: discriminator|application` tags. | ~70 |
| `public/content/lecture-guides.js` | Hand-authored lecture guides. Sections with `key_points`, `key_terms`, `exam_traps` per lecture. | 18 lectures |
| `public/data/lecture-guides/L*.json` | Per-lecture JSON guides — section overviews, exam traps, key terms. | 18 files |
| `public/match.html` | Existing Vocabulary deck UI (Match Mode). Unchanged. Reads `FLASHCARD_DECKS` directly. | — |

## Existing decks audit (NOT modified)

- **Exam 1 deck** (L01–L05) — pulled by `match.html` from `FLASHCARD_DECKS`. Untouched.
- **Exam 2 deck** (L07–L13) — same. Untouched.
- **Exam 3 deck** (L14–L20) — same. Untouched.
- **Vocabulary deck** ("All / Final" pool in match.html) — same. Untouched.
- **Lecture content** in `index.html` — untouched.
- **Stim mode**, **Cheat sheet**, **Guides** — all untouched.

## New decks generated

All cards have only `term`, `definition`, and (internal) `sourceTag`. No mnemonics, no analogies, no SVGs. Each card is derivable from the existing in-repo content above.

| Deck | File | Cards | Notes |
|---|---|---|---|
| Mechanisms | `public/data/mastery/mechanisms.json` | 46 | Named processes, models, rules, formulas. Hardy-Weinberg, breeder's eq, Hamilton's rule, Hawk-Dove ESS, MAD senescence, prezygotic/postzygotic, MacArthur-Wilson, Geographic Mosaic, Ewald, etc. |
| Scenarios | `public/data/mastery/scenarios.json` | 46 | Setup → predict the outcome / mechanism. Direct conversion of `example` fields from existing flashcard cards plus `flashcards-extra.js` `application` cards. |
| Game Theory | `public/data/mastery/game-theory.json` | 23 | Hawk-Dove with multiple V/C parameter sets, Hamilton's rule plug-ins, side-blotched RPS, snowdrift, public-goods, Fisherian sex ratios, sneaker males. |
| Compare/Contrast | `public/data/mastery/compare-contrast.json` | 41 | "X vs Y" pairs students confuse: drift vs selection, mono/para/poly, allopatric/peripatric/parapatric/sympatric, Bates/Müller, mtDNA/chloroplast, paedo/peramorphosis, etc. |
| Calculations | `public/data/mastery/calculations.json` | 23 | Hardy-Weinberg compute, X-linked, breeder's, Hamilton's, sickle equilibrium, ¹⁴C decay, Ne sex-ratio, F under sib-mating. Numeric answers stated in definition. |
| Empirical Examples | `public/data/mastery/empirical.json` | 34 | Real species/study cases mapped to concept demonstrated. Grants' finches, peppered moth, Belyaev foxes, newt-snake TTX, Madagascar orchid, Florida panther, Hawaiian Drosophila, side-blotched lizards, etc. |
| Phylogeny / Tree-Reading | `public/data/mastery/phylogeny.json` | 23 | Closeness rule, mono/para/poly, syn/sym/homoplasy, outgroup polarization, crown vs stem, parsimony + LBA, dispersal/vicariance interpretation. |
| Cause-and-Effect | `public/data/mastery/cause-effect.json` | 34 | Observed pattern → selective explanation. Antibiotic resistance, MHC polymorphism, sickle persistence, melanism, fisheries shrinkage, cichlid radiation, vestigials, X-linkage skew. |
| **TOTAL** | | **270** | |

## Deck types not built (with reason)

The brief asked for these "if existing site content supports it":

- **Calculations deck** — built (existing content has Hardy-Weinberg math, breeder's, Hamilton's, sickle equilibrium, sex-ratio Ne, ¹⁴C dating).
- **Phylogeny / Tree-Reading deck** — built (L15 has rich tree-reading content).
- **No additional decks created.** All other deck types (Sequence/Ordering, Diagram-labeling) would require content not present in repo and would violate the "derivable entirely from in-repo content" rule.

## File layout

```
public/
├── mastery.html                       NEW — Mastery page (block plan + decks + browser + runner)
├── data/mastery/                      NEW — deck JSON files (8 files, 270 cards)
│   ├── mechanisms.json
│   ├── scenarios.json
│   ├── game-theory.json
│   ├── compare-contrast.json
│   ├── calculations.json
│   ├── empirical.json
│   ├── phylogeny.json
│   └── cause-effect.json
├── content/mastery-decks.js           NEW — fetch loader, exposes window.MASTERY_DECKS
├── index.html                         MODIFIED — chrome nav adds "Mastery" link
└── match.html                         MODIFIED — top bar adds "Mastery →" link
```

## Retention Engine — what's wired

- **3-Day Block Plan** (Day 0 evening + Day 1 + Day 2 + Day 3 morning). Day 0 evening encoding is the first non-obvious cheat from the spec; the plan encodes it directly. Block-by-block checklist with localStorage persistence. Reset plan link.
- **Block types** wired: Encoding, Consolidation, Reactivation, Application, Drill, Lapse, Warmup. Encoding/Consolidation/Drill/Reactivation/Lapse all run the **3-round pipeline** (Match 90s → Flashcards → Mini-Match 45s), repeating for 3 cycles with the surviving (non-graduated) pool. Warmup runs flashcards-only at lower count. Application runs the typed-answer grader.
- **Mandatory 10-min break overlay** between cycles (with optional 5-min override). Full-screen, eye-rest reminder.
- **Cross-Deck Mastery Run** — drill across all 8 decks, prioritizing unmastered cards, drift-shuffled pool of 30, three pipeline cycles.
- **Custom Block** — pick block type and deck (or "all").
- **Application Block prompts** — adapt per deck type:
  - Scenarios: scenario shown → user types predicted outcome
  - Mechanisms: rule named → user types formula/ordered conditions
  - Game Theory: payoff scenario → user types ESS solution
  - Compare/Contrast: parses "X vs Y" form → user types both definitions + discriminator
  - Calculations: numeric problem → user types numeric answer
  - Empirical: species/study → user types concept + mechanism it demonstrates
  - Phylogeny: tree configuration → user types implication
  - Cause-and-Effect: pattern → user types selective explanation
- **Fuzzy grading** — bag-of-tokens overlap with stop-word filter, plus numeric-token bonus (matters for Calculations and Game Theory). Score thresholds: ≥65% Got it, 35–65% Partial, <35% Miss. Gold answer always shown after grading.
- **Anti-burnout safeguards**:
  - Mastered (graduated) cards drop out of drill/reactivation/warmup pools (block diversity enforced via deck routing in plan).
  - Daily cap suggestion shown on each day card (5 blocks × 25min = ~125min/day target).
  - Block exit always saves; debounced localStorage writes (5s + on unload).
- **Lapse pool** — every wrong answer pushes a card into a persistent `evol-mastery-lapse-v1` queue. Lapse block type pulls only from this queue.
- **Speed Recall persistence** — Match round timing/errors persist via the existing `progress` state on each card.
- **Deck Browser** — paginated 50/page, deck filter, search across term + definition, source-tag display, mobile-friendly single-column on narrow viewports.

## What is intentionally NOT included

- No microphone, voice recording, or audio capture features anywhere.
- No new framework or build step. Vanilla HTML/CSS/JS only, matching existing site.
- No SVG diagrams in card definitions.
- No mnemonics or analogies in card definitions.
- No changes to existing pages other than chrome-nav links to mastery.html.

## Self-test results

- Page loads at `/mastery.html` with `[mastery] loaded 8 decks / 270 cards` in console.
- No console errors.
- Block plan renders 4 day cards with 18 total blocks.
- Deck grid renders 8 cards with progress bars.
- Encoding block opens runner overlay with 30-tile match grid (3 batches of 10).
- Cycle counter shows "1 / 3" with deck card count.
- Application block input field accepts text and grading returns gold-answer feedback.
- Cross-Deck Mastery Run pulls from all 8 decks.
- localStorage keys used: `evol-mastery-progress-v1`, `evol-mastery-plan-v1`, `evol-mastery-lapse-v1`, `evol-theme`.
- Existing match.html and index.html unchanged except for added Mastery chrome links.
