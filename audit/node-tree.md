# Evolution Study Guide — Full Node Tree
**URL:** https://evolution-study-guide.pages.dev/
**Date:** 2026-04-09
**Stack:** Single static `index.html` — vanilla JS + JSON data blob (61 nodes, 659 questions)

---

## Architecture

```
index.html
+-- Sidebar (fixed left) — scrollable node list grouped by row/lecture
|   +-- Click node -> popup overlay (right panel)
|       +-- Heading + subtitle
|       +-- Sections (label + body prose)
|       +-- Quotes
|       +-- Examples
|       +-- Warnings
|       +-- Mnemonic
|   +-- Flashcard tab
|   +-- Quiz tab (10-13 MCQs per node)
+-- Visual tab (SVG diagram or map)
```

---

## Node Tree (61 nodes total)

### Row 1 — Lec 1: Intro to Evolution (3 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec1-intro-evolution | What Is Evolution? Course Intro | purple | 12 | 11 |
| lec1-flu-case-study | Flu Virus: Evolution in Action | coral | 16 | 11 |
| lec1-takehome-course | Lecture 1 Take-Home & Course Info | gray | 12 | 11 |

### Row 2 — Lec 2: Darwin / Natural Selection (5 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec2-pre-darwin | Pre-Darwin Evolutionary Thinking | amber | 12 | 11 |
| lec2-darwin-voyage | Darwin's Voyage of the Beagle | teal | 6 | 10 |
| lec2-natural-selection-ingredients | Natural Selection: The Four Ingredients | blue | 14 | 11 |
| lec2-finches-case | Galapagos Finches: Selection Case Study | coral | 11 | 11 |
| lec2-descent-modification | Descent with Modification & Common Ancestry | purple | 13 | 10 |

### Row 3 — Lec 3: Genetics Foundations (4 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec3-genes-proteins | Genes, Proteins & Gene Expression | teal | 12 | 10 |
| lec3-mutations | Mutations: Raw Material of Evolution | coral | 12 | 11 |
| lec3-sex-meiosis | Sex Cells & Meiotic Variation | blue | 4 | 10 |
| lec3-genotype-phenotype | Genotype-Phenotype Map: Polygenic Traits & Environment | amber | 12 | 10 |

### Row 4 — Lec 4: Population Genetics (4 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec4-sources-evolution | Sources of Evolutionary Change | gray | 5 | 10 |
| lec4-hardy-weinberg | Hardy-Weinberg Theorem | purple | 12 | 10 |
| lec4-genetic-drift | Genetic Drift, Bottlenecks & Founder Effects | teal | 13 | 10 |
| lec4-selection-mechanism | Natural Selection as Mechanism | blue | 13 | 10 |

### Row 5 — Lec 5-6: Quantitative Genetics (3 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec56-quant-intro | Qualitative vs Quantitative Traits | amber | 16 | 10 |
| lec56-heritability-breeders | Heritability & Breeders Equation | coral | 18 | 10 |
| lec56-reaction-norms | Phenotypic Plasticity & Reaction Norms | purple | 20 | 10 |

### Row 6 — Lec 7: Empirical Evidence (4 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec7-review-empirical | Empirical Natural Selection: Overview | teal | 8 | 10 |
| lec7-beach-mice | Beach Mice: Parallel Evolution of Camouflage | blue | 8 | 10 |
| lec7-tsd | Temperature-Dependent Sex Determination | amber | 17 | 10 |
| lec7-fitness-landscape | Fitness Landscapes | coral | 8 | 11 |

### Row 7 — Lec 8: Adaptations (4 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec8-adaptations-intro | Adaptations: Trait vs Process | gray | 7 | 12 |
| lec8-evo-devo | Evo-Devo & Regulatory Networks | purple | 17 | 12 |
| lec8-eye-evolution | Eye Evolution: From Photoreceptors to Camera Eyes | teal | 9 | 11 |
| lec8-flaws-pleiotropy | Imperfect Adaptations & Antagonistic Pleiotropy | blue | 4 | 11 |

### Row 8 — Lec 9: Coevolution (5 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec9-coevolution-intro | Coevolution: Species as Selective Agents | amber | 6 | 11 |
| lec9-antagonistic-arms | Antagonistic Coevolution & Arms Races | coral | 11 | 12 |
| lec9-mutualistic | Mutualistic Coevolution | purple | 5 | 12 |
| lec9-mimicry | Mullerian & Batesian Mimicry | teal | 9 | 12 |
| lec9-endosymbiosis | Endosymbiosis & Microbes | blue | 8 | 12 |

### Row 9 — Lec 10-11: Sexual Selection (4 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec1011-why-sex | Why Sex? Costs & Benefits | amber | 14 | 13 |
| lec1011-anisogamy | Anisogamy: The Origin of Sexual Selection | coral | 10 | 12 |
| lec1011-male-female-strategies | Male Strategies & Female Choice | purple | 12 | 13 |
| lec1011-sperm-competition | Sperm Competition & Sexual Conflict | teal | 9 | 12 |

### Row 10 — Lec 12: Life History (3 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec12-life-history-intro | Life History Strategies & Trade-offs | blue | 12 | 12 |
| lec12-aging | Extrinsic Mortality, Aging, & Senescence | amber | 16 | 12 |
| lec12-sex-allocation | Parental Investment & Sex Allocation | coral | 15 | 12 |

### Row 11 — Lec 13: Social Evolution / ESS (3 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec13-ess-game | Game Theory & Evolutionarily Stable Strategies | purple | 8 | 11 |
| lec13-group-individual | Levels of Selection: Group vs Individual | teal | 7 | 12 |
| lec13-kin-altruism | Kin Selection, Inclusive Fitness & Altruism | blue | 9 | 13 |

### Row 12 — Lec 14: Paleontology (5 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec14-age-earth | Age of the Earth & Deep Time | amber | 7 | 10 |
| lec14-origin-life | Origin of Life & Prebiotic Soup | coral | 8 | 10 |
| lec14-early-life | Early Life, Stromatolites & Multicellularity | purple | 10 | 10 |
| lec14-cambrian-paleozoic | Cambrian Explosion & Paleozoic Periods | teal | 10 | 11 |
| lec14-mesozoic-cenozoic | Mesozoic, K-T Extinction & Cenozoic | blue | 9 | 10 |

### Row 13 — Lec 15: Phylogenetics (5 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| lec15-tree-thinking | Tree Thinking: Phylogeny Basics | amber | 9 | 10 |
| lec15-cladistics-synapomorphy | Cladistics, Synapomorphies & Monophyletic Groups | coral | 12 | 10 |
| lec15-homoplasy-convergence | Parsimony, Homoplasy & Convergence | purple | 9 | 10 |
| lec15-fins-to-limbs | Fins to Limbs: Tiktaalik as Transitional Fossil | teal | 8 | 10 |
| lec15-feathers-exaptation | Feathers Evolved BEFORE Flight: Exaptation | blue | 9 | 10 |

### Row 14 — Ch 13: Speciation (6 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| ch13-species-concepts | Species Concepts — The Big Three | amber | 5 | 10 |
| ch13-isolating-barriers | Reproductive Isolating Barriers | coral | 7 | 10 |
| ch13-speciation-modes | Speciation Models | purple | 7 | 10 |
| ch13-bdm-cryptic | BDM Incompatibilities + Cryptic Species | teal | 5 | 10 |
| ch13-empirical-cases | Speciation in Action — Case Studies | blue | 7 | 10 |
| biogeography-extinction | Biogeography, Speciation & Extinction | gray | 4 | 10 |

### Row 15 — Applied Topics (3 nodes)
| ID | Title | Color | Sections | Quiz Qs |
|----|-------|-------|----------|---------|
| conservation | Conservation & Humans as Selective Force | amber | 4 | 11 |
| human-evolution | Human Evolution | coral | 4 | 11 |
| evolutionary-medicine | Evolutionary Medicine | purple | 4 | 11 |

---

## Summary Stats
- **Total nodes:** 61
- **Total quiz questions:** ~659
- **Candidates for inlining (<=3 facts):** lec3-sex-meiosis (4sec), lec8-flaws-pleiotropy (4sec), biogeography-extinction (4sec), conservation (4sec), human-evolution (4sec), evolutionary-medicine (4sec)
- **Largest nodes (>=16 sections):** lec56-reaction-norms (20), lec56-heritability-breeders (18), lec56-quant-intro (16), lec1-flu-case-study (16), lec12-aging (16)
- **Transcripts available:** apr1 (5 parts), apr6 (5 parts) + lecture JSON files (lec1-lec15)
