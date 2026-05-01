# Cheatsheet Coverage Audit (Phase 4)

Branch: `flashcard-overhaul-v1` · Source: [public/cheatsheet.html](../public/cheatsheet.html) (cumulative L01–L20). Target: BIOL 4230 Exam 2 = Ch 10–16 (= L08, L09, L11, L12, L13). Audit method: walk every cheatsheet `<div class="sec">`, cross-reference against `flashcards.js` (auto, 235+ unique cards) and `flashcards-extra.js` (66 hand-authored cards). Flag a section as a gap when no card adds DEPTH beyond a 1-line term + def.

## Summary

| Lecture (chapter) | Cheatsheet sections | Auto cards | Extras | Verdict |
|---|---|---|---|---|
| L08 (Ch 10) Complex adaptations | 6 (§A–§F) | 18 | 6 | covered (1 thin) |
| L09 (Ch 15) Coevolution | 5 (§A–§E) | 10 | 4 | covered (1 thin) |
| L11 (Ch 11) Sex / sexual selection | 4 (§A–§D) | 13 | 6 | covered (1 thin) |
| L12 (Ch 12) Life history | 5 (§A–§E) | 13 | 3 | **3 gaps** |
| L13 (Ch 16) Social behavior | 5 (§A–§E) | 12 | 8 | covered |

Total Exam 2 cards: 93. New cards target: **~25** (focused on the 6 thin/missing sections + the directive's "computation" / "discriminator" emphasis).

## Section-by-section (Ch 10–16)

### L08 — Complex Adaptations (Ch 10)

| § | Topic | Auto coverage | Extras coverage | Gap action |
|---|---|---|---|---|
| §A | Adaptation as trait & process | "Adaptation" term card | none | **THIN** — add a discriminator card on the noun-vs-verb distinction with worked example |
| §B | Vertebrate eye stepwise | "Vertebrate eye stepwise" card | "Stepwise eye evolution stages" | covered |
| §C | Regulatory networks, gene dup | "Cis-regulatory mutation", "Gene duplication", "Neofunctionalization", "Subfunctionalization", "Protein promiscuity" | "Neofunctionalization vs subfunctionalization", "Cis-regulatory mutations vs structural" | covered (deep) |
| §D | Heterochrony | "Heterochrony", "Paedomorphosis", "Peramorphosis" | "Heterochrony (paedo vs peramorphosis)" | covered |
| §E | Hox genes | "Hox gene", "Colinearity", "Conservation of dev networks" | "Hox genes — A-P body axis" | covered |
| §F | Imperfect adaptation | "Vestigial structure", "Trade-off", "Constraint" | "Vestigial structure" | covered |

**L08 gap target: 1–2 new cards** (§A discriminator + §C protein promiscuity worked example)

### L09 — Coevolution (Ch 15)

| § | Topic | Auto | Extras | Gap action |
|---|---|---|---|---|
| §A | Defining reciprocal coevolution | "Coevolution", "Reciprocal selection" | "Coevolution vs coexistence" | covered (deep) |
| §B | Antagonistic arms races | "Coevolutionary arms race", "Tetrodotoxin (TTX)" | "Newt-snake arms race" | covered (deep) |
| §C | Mutualistic coevolution | "Mutualism", "Endosymbiosis" | none | **THIN** — pollinator-flower (Darwin's prediction) and endosymbiosis depth missing; add 2 cards |
| §D | Mimicry | "Batesian mimicry", "Müllerian mimicry", "Aposematism" | "Batesian vs Müllerian mimicry" | covered |
| §E | Geographic Mosaic | "Geographic Mosaic Theory" | "Geographic Mosaic Theory of Coevolution (Thompson)" | covered (deep) |

**L09 gap target: 2 new cards** (mutualistic pollinator card + endosymbiosis "two ancestral events" card)

### L11 — Sex and Sexual Selection (Ch 11)

| § | Topic | Auto | Extras | Gap action |
|---|---|---|---|---|
| §A | Cost of sex / why sex evolved | "Twofold cost of sex", "Muller's ratchet", "Red Queen" | "Twofold cost", "Red Queen", "Muller's ratchet" | covered |
| §B | Anisogamy | "Anisogamy", "Isogamy" | "Anisogamy = the basis of male/female" | covered |
| §C | Sexual selection | "Sexual selection", "Intrasexual", "Intersexual", "Sexual dimorphism" | "Fisher's runaway", "Intrasexual vs intersexual" | covered |
| §D | Conflict, sperm competition | "Sexual conflict", "Sperm competition", "Cryptic female choice", "Antagonistic coevolution" | none | **THIN** — depth missing; add 3 cards on sexual conflict, sperm comp & cryptic female choice |

**L11 gap target: 3 new cards** (§D depth)

### L12 — Life History Evolution (Ch 12)

| § | Topic | Auto | Extras | Gap action |
|---|---|---|---|---|
| §A | Trade-offs in energy allocation | "Life history", "Trade-off", "Reproductive effort" | none | **THIN** — fundamental concept; add a discriminator card |
| §B | Extrinsic mortality | "Extrinsic mortality", "Senescence/intrinsic mortality" | "Extrinsic mortality → life history" | covered (deep) |
| §C | Theories of senescence | "Senescence", "Mutation accumulation", "Antagonistic pleiotropy", "Disposable soma" | "Three theories of senescence" | covered (deep) |
| §D | Age at maturity, offspring size | "Age at maturity", "r/K selection" | "r vs K selection" | covered (basics); offspring number-vs-size tradeoff thin |
| §E | Seychelles warblers | "Cooperative breeding", "Sex-biased dispersal" | none | **MISSING** — case study not in extras; 2 cards needed |

**L12 gap target: 4 new cards** (trade-offs general, offspring N×size tradeoff, Seychelles cooperative breeding mechanism, sex-biased dispersal application)

### L13 — Social Behavior (Ch 16)

| § | Topic | Auto | Extras | Gap action |
|---|---|---|---|---|
| §A | Individual vs group selection | "Group selection", "Selfish gene perspective" | "Group selection — why naive version fails" | covered |
| §B | Kin selection / inclusive fitness | "Hamilton's rule", "Coefficient of relatedness", "Inclusive fitness", "Eusociality" | "Hamilton's rule: rB > C", "Coefficient of relatedness — common values", "Inclusive fitness" | covered (deep, with worked example) |
| §C | ESS | "ESS", "Frequency-dependent", "Hawk-Dove" | "ESS", "Hawk-Dove game payoffs" | covered; could add a 2nd payoff-matrix worked variant |
| §D | Side-blotched lizards (RPS) | "Side-blotched lizard" | "Side-blotched lizard rock-paper-scissors" | covered |
| §E | Cooperation among non-kin | "Direct reciprocity", "Indirect reciprocity" | "Direct vs indirect reciprocity" | covered |

**L13 gap target: 1 new card** (Hawk-Dove worked example with V > C case where pure-Hawk wins)

## Cumulative review (cards still useful for Exam 2 if it includes prior chapters)

The directive flags HWE math + selection types + phylogeny groupings as "pay special attention." Spot-check existing cards:

| Concept | Auto | Extras | Verdict |
|---|---|---|---|
| HWE math (compute p,q from genotypes; chi-sq deviation test) | "Allele frequency", "Genotype frequency", "p² + 2pq + q²", "Hardy-Weinberg eq" | 8 cards: p²+2pq+q² meaning, 5 HWE assumptions, computing p, rare recessive q≈√, X-linked, Wahlund, inbreeding F, one-gen restoration | covered (deep) |
| Selection types (directional/stabilizing/disruptive discriminator) | each has a card | "Selection-type discrimination cheat" | covered |
| Phylogeny groupings (mono/para/poly + syn/sym/homoplasy) | each has a card | "Synapomorphy vs symplesiomorphy vs homoplasy", "Monophyletic / paraphyletic / polyphyletic", "Outgroup", "Crown vs stem", "Maximum parsimony", "Reading a phylogenetic tree" | covered (deep) |
| Speciation modes | "Allopatric", "Sympatric", "Reinforcement" | "Speciation modes (geographic)", "Prezygotic 5", "Postzygotic 3", "Reinforcement", "Sympatric speciation when it works", "Hybrid zone" | covered (deep) |
| Hox / dev bio | "Hox gene", "Colinearity", "Conservation of dev networks" | "Hox genes — A-P body axis" | covered |

No new cards needed for cumulative review — the existing extras cover the directive's "pay special attention" list.

## Summary of new cards to author

**Total: ~10 new cards** (lower than the directive's "~50" target — coverage is already strong for this exam):

| Card # | Lecture | Section | Type | Topic |
|---|---|---|---|---|
| 1 | L08 | §A | discriminator | Adaptation: noun vs verb distinction with worked example |
| 2 | L08 | §C | application | Protein promiscuity → cooption (e.g., crystallins, antifreeze proteins) |
| 3 | L09 | §C | application | Mutualistic pollinator–flower coevolution (Darwin's long-spurred orchid) |
| 4 | L09 | §C | discriminator | Endosymbiosis: two events (mitochondria, chloroplasts) with timing |
| 5 | L11 | §D | discriminator | Sexual conflict: when do interests align vs diverge? |
| 6 | L11 | §D | application | Sperm competition mechanisms (testis size, mating plugs, sperm length) |
| 7 | L11 | §D | application | Cryptic female choice — post-copulatory paternity bias |
| 8 | L12 | §A | discriminator | Life-history trade-off: which currency? (energy, time, mortality) |
| 9 | L12 | §D | application | Offspring number vs size — bet-hedging vs provisioning |
| 10 | L12 | §E | application | Seychelles warblers — why help instead of disperse? |
| 11 | L13 | §C | application | Hawk-Dove worked: V=15, C=10 → pure-Hawk ESS (V≥C case) |

Plus, in parallel: the **~28 `exAnswer` populations** for existing cards with bare-question examples (already kicked off for L02; continuing through L04 / L05 / L08 / L09 / L11 / L12 / L13 / L14 / L15 / L16 / L17 / L19 / L20).

## Implementation order

1. **Continue exAnswer authoring** (Exam 2 lectures first: L08 → L09 → L11 → L12 → L13). High leverage because it improves cards already in rotation.
2. **Author the 11 new gap-fill cards** by lecture batch into `flashcards-extra.js`.
3. **Then** spread exAnswer to L04 / L05 / L14 / L15 / L16 / L17 / L19 / L20 (Exam 1 + 3 cumulative review).
4. **Lightweight linter** (`public/content/card-linter.js`) — pure module, run as one-shot console report. No editor wiring.
5. Verify in preview, deploy to preview URL.
