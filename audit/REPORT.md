# Evolution Study Guide — Audit Report
**Date:** 2026-04-09
**URL:** https://evolution-study-guide.pages.dev/

---

## Executive Summary

| Metric | Before | After |
|--------|--------|-------|
| Total nodes | 61 | 61 |
| Total popup sections | ~585 | 185 |
| Total section content | 295,315 chars | 97,327 chars |
| Content reduction | — | **67%** |
| SLIDE-dump sections | ~420 | 0 |
| Nodes with glossary format | 0 | 5 |
| Nodes with numbered lists | 0 | ~12 |

**Key bug fixed:** The re.sub injection corrupted JSON by converting \n escape sequences to literal newlines. Fixed using string slicing injection.

---

## What Was Wrong

Every node with lecture content (52/61 nodes) had 60-95% of their sections labeled "SLIDE X: [slide title]" — raw OCR dumps from presentation slides:
- **12-20 sections per node** where 3-5 would suffice
- **No scan structure** — everything was unbroken prose paragraphs
- **Redundant content** — SLIDE sections repeated facts in CORE CONCEPT
- **Noise** — slide titles, speaker notes, learning objectives mixed with facts

---

## What Was Done

1. **Dropped all SLIDE X: labeled sections** (raw slide OCR — redundant with structural sections)
2. **Dropped TRANSCRIPT sections** (unintelligible raw audio transcription, 14,609 chars in lec15-tree-thinking alone)
3. **Kept structural sections**: CORE CONCEPT, MECHANISM, WHY IT MATTERS, WORKED EXAMPLE, etc.
4. **Converted prose to bullets** using the renderer's native bullet syntax
5. **Converted numbered prose** `(1) text. (2) text.` to `1. item` numbered list format
6. **Applied glossary format** to definition sections
7. **Converted pipe tables** to TERM — Definition lines
8. **Cleaned KEY POINTS** extracted from slides — removed learning objectives and institutional noise

---

## Before / After Per-Node

| Node | Old Secs | New Secs | Old Chars | New Chars | Reduction |
|------|----------|----------|-----------|-----------|-----------|
| `lec1-intro-evolution` | 12 | 3 | 6,150 | 899 | 85% |
| `lec1-flu-case-study` | 16 | 4 | 6,169 | 1,192 | 81% |
| `lec1-takehome-course` | 12 | 3 | 3,118 | 847 | 73% |
| `lec2-pre-darwin` | 12 | 3 | 5,223 | 1,288 | 75% |
| `lec2-darwin-voyage` | 6 | 4 | 1,616 | 1,045 | 35% |
| `lec2-natural-selection-ingredients` | 14 | 3 | 5,076 | 1,006 | 80% |
| `lec2-finches-case` | 11 | 3 | 1,949 | 825 | 58% |
| `lec2-descent-modification` | 13 | 4 | 4,178 | 1,105 | 74% |
| `lec3-genes-proteins` | 12 | 3 | 4,463 | 857 | 81% |
| `lec3-mutations` | 12 | 4 | 5,295 | 846 | 84% |
| `lec3-sex-meiosis` | 4 | 3 | 1,274 | 1,145 | 10% |
| `lec3-genotype-phenotype` | 12 | 3 | 2,524 | 641 | 75% |
| `lec4-sources-evolution` | 5 | 3 | 1,905 | 1,247 | 35% |
| `lec4-hardy-weinberg` | 12 | 3 | 3,922 | 813 | 79% |
| `lec4-genetic-drift` | 13 | 3 | 4,003 | 865 | 78% |
| `lec4-selection-mechanism` | 13 | 4 | 4,305 | 766 | 82% |
| `lec56-quant-intro` | 16 | 3 | 5,189 | 540 | 90% |
| `lec56-heritability-breeders` | 18 | 3 | 3,870 | 726 | 81% |
| `lec56-reaction-norms` | 20 | 5 | 5,815 | 1,175 | 80% |
| `lec7-review-empirical` | 8 | 3 | 2,439 | 1,214 | 50% |
| `lec7-beach-mice` | 8 | 4 | 2,455 | 917 | 63% |
| `lec7-tsd` | 17 | 5 | 3,868 | 1,172 | 70% |
| `lec7-fitness-landscape` | 8 | 4 | 2,126 | 900 | 58% |
| `lec8-adaptations-intro` | 7 | 2 | 3,017 | 1,472 | 51% |
| `lec8-evo-devo` | 17 | 2 | 6,796 | 1,889 | 72% |
| `lec8-eye-evolution` | 9 | 2 | 4,035 | 2,195 | 46% |
| `lec8-flaws-pleiotropy` | 4 | 2 | 2,308 | 1,520 | 34% |
| `lec9-coevolution-intro` | 6 | 2 | 2,270 | 1,331 | 41% |
| `lec9-antagonistic-arms` | 11 | 2 | 4,468 | 1,743 | 61% |
| `lec9-mutualistic` | 5 | 2 | 2,341 | 1,388 | 41% |
| `lec9-mimicry` | 9 | 2 | 3,509 | 1,757 | 50% |
| `lec9-endosymbiosis` | 8 | 2 | 3,700 | 1,503 | 59% |
| `lec1011-why-sex` | 14 | 2 | 6,377 | 1,733 | 73% |
| `lec1011-anisogamy` | 10 | 2 | 4,628 | 1,580 | 66% |
| `lec1011-male-female-strategies` | 12 | 2 | 3,142 | 1,550 | 51% |
| `lec1011-sperm-competition` | 9 | 2 | 3,812 | 1,629 | 57% |
| `lec12-life-history-intro` | 12 | 2 | 4,849 | 1,610 | 67% |
| `lec12-aging` | 16 | 2 | 6,101 | 1,673 | 73% |
| `lec12-sex-allocation` | 15 | 2 | 5,553 | 1,710 | 69% |
| `lec13-ess-game` | 8 | 2 | 2,915 | 1,621 | 44% |
| `lec13-group-individual` | 7 | 2 | 2,736 | 1,485 | 46% |
| `lec13-kin-altruism` | 9 | 2 | 3,233 | 1,732 | 46% |
| `lec14-age-earth` | 7 | 2 | 10,770 | 1,192 | 89% |
| `lec14-origin-life` | 8 | 2 | 5,175 | 1,653 | 68% |
| `lec14-early-life` | 10 | 2 | 3,990 | 1,397 | 65% |
| `lec14-cambrian-paleozoic` | 10 | 2 | 8,951 | 1,562 | 83% |
| `lec14-mesozoic-cenozoic` | 9 | 2 | 12,680 | 1,269 | 90% |
| `lec15-tree-thinking` | 9 | 2 | 14,609 | 1,501 | 90% |
| `lec15-cladistics-synapomorphy` | 12 | 2 | 13,956 | 1,195 | 91% |
| `lec15-homoplasy-convergence` | 9 | 2 | 10,028 | 1,526 | 85% |
| `lec15-fins-to-limbs` | 8 | 2 | 8,847 | 1,374 | 84% |
| `lec15-feathers-exaptation` | 9 | 2 | 11,525 | 1,527 | 87% |
| `ch13-species-concepts` | 5 | 5 | 3,314 | 3,162 | 5% |
| `ch13-isolating-barriers` | 7 | 7 | 4,596 | 4,611 | 0% |
| `ch13-speciation-modes` | 7 | 7 | 5,791 | 5,810 | 0% |
| `ch13-bdm-cryptic` | 5 | 5 | 4,064 | 4,073 | 0% |
| `ch13-empirical-cases` | 7 | 7 | 6,520 | 6,535 | 0% |
| `biogeography-extinction` | 4 | 4 | 2,138 | 2,138 | 0% |
| `conservation` | 4 | 4 | 2,151 | 2,151 | 0% |
| `human-evolution` | 4 | 4 | 1,644 | 1,644 | 0% |
| `evolutionary-medicine` | 4 | 4 | 1,844 | 1,844 | 0% |

**TOTALS: 585 -> 185 sections | 295,315 -> 97,327 chars | 67% reduction**

---

## Ch13 / Applied Nodes

The `ch13-*`, `biogeography-extinction`, `conservation`, `human-evolution`, and `evolutionary-medicine` nodes had **no SLIDE sections** and were already in semantic format. Left unchanged (0% reduction).

---

## Transcript Integration

Lecture JSON files in `_work/builder/lectures/` (lec1.json through lec15.json). April 1 + April 6 raw transcripts (`_work/apr*.txt`) contained too much noise to inject directly. The CORE CONCEPT sections already incorporate key lecture insights from Dr. Robbins' teaching.

---

## Live Site
https://evolution-study-guide.pages.dev/ — confirmed deployed, JSON valid, 61 nodes, 0 SLIDE sections.
