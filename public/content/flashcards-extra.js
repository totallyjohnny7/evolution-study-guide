/* Gap-filling cards keyed off the cheatsheet (L01-L20).
   Heavy on the user-flagged topics: Hardy-Weinberg math, selection types,
   game theory, speciation modes, phylogenetic groupings, Hox / dev.
   Each card may include a `mnem` field that the new view renders in a
   separate gold-bordered subsection. */

// Helper exposed for downstream patch files to merge content per-term without overwriting.
window.addCardPatches = function (lectureId, terms) {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  if (!window.FLASHCARD_PATCHES[lectureId]) window.FLASHCARD_PATCHES[lectureId] = {};
  Object.entries(terms || {}).forEach(function (entry) {
    var term = entry[0]; var patch = entry[1];
    if (!window.FLASHCARD_PATCHES[lectureId][term]) window.FLASHCARD_PATCHES[lectureId][term] = {};
    Object.assign(window.FLASHCARD_PATCHES[lectureId][term], patch);
  });
};

(function () {
  const EXTRA = {
    "L01": [
      {
        term: "Heritable vs non-heritable variation",
        def: "HERITABLE: trait differences with a genetic basis; passable to offspring; the only kind selection can act on across generations. NON-HERITABLE: differences from environment alone (nutrition, learning, accident); not passed on; invisible to evolution.",
        example: "A field of dandelions varies in flower color. If color is set by soil pH (no genetic variation), can selection on color make the population evolve?",
        exAnswer: "NO. Without heritable variation in color, selecting purple-only flowers will leave the next generation back at the original color distribution (each new plant's color is set by soil where it grows, not its parent's color). Selection produces evolution ONLY when phenotypic differences correlate with genetic differences. This is why the breeder's equation R = h²·S goes to zero when h² = 0.",
        ctx: "L01 §A — Defining evolution",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "heritable-variation"
      },
      {
        term: "Population vs individual — what actually evolves?",
        def: "POPULATIONS evolve (allele frequencies change across generations). INDIVIDUALS are SELECTED (some survive/reproduce more) but do NOT evolve — they live and die with their fixed genotype. Easy to confuse the two.",
        example: "An exam asks: 'During the drought, the finches evolved deeper beaks.' Identify what's wrong with this sentence and rewrite it correctly.",
        exAnswer: "Wrong: individuals don't evolve. Each finch had whatever beak depth it was born with — no individual finch's beak got deeper during its life. CORRECTED: 'During the drought, the population's mean beak depth increased — deeper-beaked finches survived and reproduced more, so the next generation had a higher frequency of deep-beak alleles.' The unit of evolution is the POPULATION; the unit of selection is the INDIVIDUAL.",
        ctx: "L01 §A — Defining evolution",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "unit-of-evolution"
      },
      {
        term: "Mutation: random or directed by need?",
        def: "Mutations are RANDOM with respect to fitness — they occur regardless of whether they would be useful. The environment SELECTS pre-existing variants; it does not 'create' or 'guide' the mutations themselves.",
        example: "A claim: 'Antibiotic exposure causes bacteria to mutate so they can survive.' What's wrong with this statement, and what's the correct version?",
        exAnswer: "Wrong implication: that the antibiotic INDUCES the resistance mutation. CORRECT: Resistance mutations occur randomly at low frequency in the population BEFORE the drug is applied. The antibiotic doesn't generate mutations — it selects pre-existing resistant variants by killing the rest. Luria-Delbrück (1943) demonstrated this experimentally with their fluctuation test using bacteriophage. Selection ≠ direction of mutation.",
        ctx: "L01 §C — The four evolutionary mechanisms",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "mutation-randomness",
        mnem: "Random mutation + non-random selection = adaptation (NOT directed mutation)."
      },
      {
        term: "Selection vs drift — when does each dominate?",
        def: "SELECTION dominates when (selection coefficient s) >> 1/N. DRIFT dominates when s << 1/N. In LARGE populations, even weak selection beats drift. In SMALL populations, drift can override moderate selection. Threshold: |s| ≈ 1/(2Ne) for diploids.",
        example: "An island population of 50 individuals carries a slightly beneficial allele (s = +0.005). Will selection or drift dominate the allele's fate?",
        exAnswer: "DRIFT will dominate. The threshold is roughly 1/(2Ne) = 1/100 = 0.01. Since s = 0.005 < 0.01, the allele is effectively neutral; chance fluctuations (births/deaths) determine whether it fixes or is lost. The same allele in a population of 10,000 (threshold 1/20,000) would be strongly under selection. Population size sets which evolutionary force is decisive.",
        ctx: "L01 §C — The four evolutionary mechanisms",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "selection-vs-drift-threshold"
      },
      {
        term: "Common descent — strongest evidence",
        def: "All life shares one ancestor. Strongest lines of evidence: (1) UNIVERSAL genetic code (same DNA → amino acid mapping in everything from E. coli to whales), (2) homologous proteins (cytochrome c, ribosomal RNA), (3) shared metabolic pathways, (4) nested hierarchy of traits matching molecular phylogenies.",
        example: "If life had multiple independent origins, what genetic-code pattern would you expect? What do we actually observe?",
        exAnswer: "Independent origins would predict DIFFERENT genetic codes (different codon→amino acid mappings) per origin lineage — there's no chemical reason CGU has to mean Arginine. We observe ONE near-universal code across ALL domains (with only minor variations in some mitochondria and ciliates), implying a single ancestor that locked in this code billions of years ago. The code's frozen-accident pattern is one of biology's strongest lines of evidence for common descent.",
        ctx: "L01 §B — Why evolution unifies biology",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "common-descent-evidence"
      },
      {
        term: "Adaptation — three things selection requires",
        def: "For natural selection to produce adaptation: (1) HERITABLE VARIATION in a trait, (2) DIFFERENTIAL SURVIVAL or REPRODUCTION based on the trait, (3) CONSEQUENT FITNESS DIFFERENCES (genetic copies of trait in next generation differ from random expectation). All three are necessary.",
        example: "Identify which of the three requirements is missing in each of these scenarios: (a) Striking variation in beak shape, all environment-driven. (b) Heritable beak variation, but random mating and equal survival. (c) Beak heritable, deeper beaks survive better, but they all leave equal offspring numbers anyway.",
        exAnswer: "(a) MISSING (1) heritable variation — variation exists but isn't passed on. (b) MISSING (2) differential survival/reproduction — variation exists, but selection isn't acting. (c) MISSING (3) consequent fitness differences — survival differs but TOTAL reproduction is equal, so allele freqs don't change. All three pieces must align; remove any one and adaptation stops.",
        ctx: "L01 §C — The four evolutionary mechanisms",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "selection-three-requirements"
      }
    ],
    "L02": [
      {
        term: "Darwin's three observations + one inference",
        def: "OBS 1: Heritable variation exists. OBS 2: More offspring produced than survive. OBS 3: Survival/reproduction is non-random. INFERENCE: Heritable variants that raise reproduction become more common — natural selection.",
        example: "Asked on an exam to 'list the logical structure of natural selection,' you must give 3 observations and 1 inference. What would a missing piece (e.g., no heritable variation) do to the argument?",
        exAnswer: "The conclusion fails. If variation is non-heritable (purely environmental), survivors can't transmit their winning traits → no shift across generations. Each observation is a necessary premise; remove any one and the inference doesn't follow. Drop overproduction → no differential survival to select on. Drop non-random survival → no selection signal at all.",
        ctx: "L02 §D — Darwin, Wallace, natural selection",
        mnem: "VOS→S: Variation · Overproduction · Survival differs → Selection."
      },
      {
        term: "Falsifiability (Popper)",
        def: "A scientific claim must specify observations that would prove it wrong. Evolution is falsifiable; e.g., a Cambrian rabbit fossil would shatter the tree.",
        example: "An exam asks why 'all living things were created perfectly' is not a scientific claim. Frame the answer in falsifiability terms.",
        exAnswer: "No observation could disprove 'created perfectly' — perfection accommodates any data, including imperfections (just call them 'optimal trade-offs'). Scientific claims must specify what would refute them; this one refuses. Compare evolution: a Precambrian rabbit, identical complex organs in unrelated lineages, or stable allele frequencies under measurable selection would all break the theory.",
        ctx: "L02 §E — Hypothesis vs. theory"
      }
    ],
    "L04": [
      {
        term: "p² + 2pq + q² = 1 — what each term means",
        def: "p² = expected freq(AA); 2pq = expected freq(Aa); q² = expected freq(aa). p+q=1 for a biallelic locus.",
        example: "A population has p=0.7. Compute expected genotype frequencies. (AA=0.49, Aa=0.42, aa=0.09.) Sum should equal 1.",
        ctx: "L04 §B — Hardy-Weinberg equation",
        mnem: "PAQ-squared: Pure-A · A-and-q heterozygotes · pure-q. p² + 2pq + q²."
      },
      {
        term: "Five HWE assumptions (the disequilibrium menu)",
        def: "(1) No mutation, (2) no migration/gene flow, (3) infinite N (no drift), (4) no selection, (5) random mating. Violation of any one → allele or genotype frequencies shift away from HWE.",
        example: "If observed AA homozygotes exceed p²N, which assumption is most likely violated? (Inbreeding / population subdivision — Wahlund effect.)",
        ctx: "L04 §B — Hardy-Weinberg equation",
        mnem: "MM-DSR: Mutation · Migration · Drift · Selection · Random mating."
      },
      {
        term: "Computing p from genotype counts",
        def: "p = (2·N_AA + N_Aa) / (2·N_total). Each AA contributes 2 A alleles; each Aa contributes 1.",
        example: "100 individuals: 36 AA, 48 Aa, 16 aa. p = (72+48)/200 = 0.6. q = 0.4. Expected: p²=0.36, 2pq=0.48, q²=0.16 — observed = expected → in HWE.",
        ctx: "L04 §A — Allele freq vs genotype freq"
      },
      {
        term: "Rare recessive disease → allele frequency",
        def: "When a disease is recessive and rare, q ≈ √(disease frequency); carrier frequency ≈ 2pq. Heterozygotes vastly outnumber homozygotes when q is small.",
        example: "Cystic fibrosis frequency ≈ 1/2,500 in NW Europeans. q² = 1/2500 → q = 1/50 = 0.02. Carrier freq = 2(0.98)(0.02) ≈ 0.039 ≈ 1/25. ~100× more carriers than affected individuals.",
        ctx: "L04 §C — Detecting deviations",
        mnem: "Square-root the rare: q = √(aa-freq). Then 2pq for carriers."
      },
      {
        term: "X-linked Hardy-Weinberg",
        def: "Hemizygous males show recessive at frequency q (they have only one X). Females show recessive at q². Disease vastly more common in males.",
        example: "Color blindness q ≈ 0.08. Male affected freq ≈ 0.08; female ≈ 0.0064 — males ~12× more often affected. Why does X-linkage skew sex ratios in disease prevalence?",
        exAnswer: "Males are HEMIZYGOUS — only one X copy, so a recessive allele at frequency q is fully expressed at q (males get the rare allele 'cheap'). Females need TWO copies, expressed at q². Since q < 1, q ≫ q² → males are affected far more often. Numerically: q = 0.08 → males 8% affected, females 0.64% affected → 12.5× ratio. Increases with rarer alleles (q = 0.01 → 100× ratio).",
        ctx: "L04 §C — Detecting deviations",
        mnem: "X-male = q · X-female = q² (males get the rare allele cheap)."
      },
      {
        term: "Wahlund effect",
        def: "Pooling two subpopulations with different allele frequencies produces APPARENT excess of homozygotes vs HWE expectation, even if each subpop is in HWE internally.",
        example: "Subpop A: p=0.9. Subpop B: p=0.1. Pooled p=0.5 → expected 2pq=0.5. Observed heterozygotes ≈ 0.18. Excess homozygotes — but no inbreeding inside either subpop. Diagnosis?",
        exAnswer: "POPULATION SUBDIVISION (Wahlund effect). Pooling subpops with different allele frequencies produces apparent homozygote excess vs HWE — even though each subpop is internally in HWE. No inbreeding required. Distinguish from true inbreeding by looking for spatial structure (sample subpops separately, compute FST). The math: pooled heterozygosity = 2 p̄ q̄ − 2·Var(p) — variance in p across subpops directly reduces apparent heterozygosity.",
        ctx: "L04 §C — Detecting deviations"
      },
      {
        term: "Inbreeding coefficient (F)",
        def: "Probability that the two alleles at a locus are identical by descent. F=0 → random mating; F=1 → fully inbred. Raises homozygosity by F·2pq above HWE expectation.",
        example: "Self-fertilizing plant lineages drive F toward 1 within a few generations. Compute genotype freqs as p²+Fpq, 2pq(1−F), q²+Fpq.",
        ctx: "L04 §C — Detecting deviations"
      },
      {
        term: "One generation of random mating restores HWE",
        def: "From any starting genotype frequencies (assuming no other forces), a single generation of random mating produces HWE proportions p², 2pq, q². The other 4 forces must be absent.",
        example: "A population has 80% AA and 20% aa (no Aa). After one round of random mating with p=0.8: expected 0.64 AA, 0.32 Aa, 0.04 aa. Why does this happen instantly?",
        exAnswer: "Allele frequencies don't change under random mating — only genotype frequencies redistribute. Each new offspring's genotype is drawn from independent gamete sampling at frequencies p and q, so genotype frequencies converge to p², 2pq, q² in a single round (no time-decay term). The 'memory' of previous genotype distributions is wiped because gametes are independent. This is what makes HWE a strong predictive baseline.",
        ctx: "L04 §B — Hardy-Weinberg equation"
      }
    ],
    "L05": [
      {
        term: "V_P = V_A + V_D + V_I + V_E",
        def: "Phenotypic variance partitioned: V_A additive (predictably heritable), V_D dominance (same-locus), V_I epistatic (cross-locus), V_E environmental (not inherited). Selection acts on V_P; only V_A predictably evolves.",
        example: "If a tomato's height variance is 60% V_A, 10% V_D, 30% V_E, what's narrow-sense h²? (h² = V_A/V_P = 0.6.) What's broad-sense H²? (H² = (V_A+V_D)/V_P = 0.7.)",
        ctx: "L05 §A — Variance partitioning",
        mnem: "PADIE: P = A + D + I + E. Add Dominance, Interaction, Environment to Additive."
      },
      {
        term: "Directional selection",
        def: "Favors one extreme of a trait distribution; mean shifts toward favored end; variance often decreases.",
        example: "Drought favors deep beaks in Galápagos finches; mean beak depth shifts deeper across one generation. What does the trait distribution look like before vs after?",
        exAnswer: "BEFORE: roughly bell-shaped, centered on the original mean. AFTER one generation: bell SHIFTED toward the favored extreme (deeper beaks); shape similar but center moved by R = h²·S. Variance often shrinks slightly because lower-fitness extreme individuals were removed, and the favored extreme is bounded by the original distribution's tail. Sustained selection eventually depletes V_A and slows further response.",
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Directional → Distribution Drifts (mean moves)."
      },
      {
        term: "Stabilizing selection",
        def: "Favors the mean / intermediate phenotype; extremes selected against; mean unchanged but variance shrinks.",
        example: "Human birth weight: very small AND very large babies have higher mortality. Mean stays at ~3.5 kg. What happens to variance under sustained stabilizing selection?",
        exAnswer: "Variance DECREASES — extremes are pruned each generation, the distribution narrows around the mean. Mean unchanged. Long-term variance is set by mutation–selection balance: new mutations introduce variance, stabilizing selection prunes it. Cannot drive variance to zero unless mutation stops. Note: this is the opposite of what new students often guess — selection here removes phenotypic extremes, not allele frequencies.",
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Stabilizing → Squashes the distribution (variance ↓)."
      },
      {
        term: "Disruptive selection",
        def: "Favors BOTH extremes; intermediates selected against; variance increases; can produce bimodal distribution and seed sympatric divergence.",
        example: "African finch with bimodal beak distribution — small beaks crack soft seeds, large beaks crack hard seeds. Intermediates are bad at both. What long-term outcome may this lead to?",
        exAnswer: "SYMPATRIC SPECIATION (potentially) — IF assortative mating evolves so that small-beaked birds preferentially mate with small-beaked birds (and likewise for large), the bimodal distribution can split into two reproductively isolated lineages. Without assortative mating, the bimodality is unstable: random mating between morphs continually regenerates intermediates, which selection then prunes — costly equilibrium. Disruptive selection alone is necessary but not sufficient.",
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Disruptive → Divides the distribution (two peaks)."
      },
      {
        term: "Selection-type discrimination cheat",
        def: "Mean shifts → directional. Mean same, variance ↓ → stabilizing. Variance ↑, two peaks → disruptive.",
        example: "Trait distribution before/after: mean shifts right, variance similar. Which type? (Directional.) Mean same, variance shrinks. Which? (Stabilizing.)",
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Mean-Move = Directional · Squeeze = Stabilizing · Split = Disruptive."
      },
      {
        term: "Breeder's equation R = h²·S",
        def: "Response to selection (R) = narrow-sense heritability (h²) × selection differential (S). If h²=0, R=0 — no evolution from any selection strength.",
        example: "Mean height 170 cm, breeders 178 cm → S = 8. h² = 0.5. Predict R = 4 cm; next-gen mean 174 cm. If h²=0 (all environment), R = 0 regardless of S.",
        ctx: "L05 §C — Breeder's equation",
        mnem: "Response = how heritable × how strongly selected (R = h²·S)."
      },
      {
        term: "Narrow vs broad heritability",
        def: "h² = V_A/V_P (narrow; predicts response to selection). H² = V_G/V_P = (V_A+V_D+V_I)/V_P (broad; total genetic share).",
        example: "Why does selection respond only to h², not H²? Because dominance & epistasis variance don't pass faithfully — they depend on which alleles meet which.",
        ctx: "L05 §B — Heritability"
      },
      {
        term: "Parent-offspring regression estimates h²",
        def: "Slope of offspring trait vs midparent trait ≈ h². Steeper slope = trait more heritable.",
        example: "Slope of 0.6 of offspring height on midparent height → h² ≈ 0.6. What slope would tell you a trait is purely environmental? (≈ 0.)",
        ctx: "L05 §B — Heritability"
      },
      {
        term: "Reaction norm",
        def: "Plot of phenotype vs environment for a single genotype; flat line = canalized; sloped = plastic; non-parallel between genotypes = G×E.",
        example: "Genotype A: yields 5 vs 8 across temperatures. Genotype B: yields 8 vs 4 (opposite slope). Lines cross — that's G×E. Why does this matter for predicting which genotype 'is best'?",
        exAnswer: "There is NO context-free 'best' — fitness depends on environment. G×E means the rank order of genotypes can FLIP across environments. A breeder picking the 'best' line in one site can lose the actual best in another site. Practical implication: selection or breeding programs must match the deployment environment; lab-raised crops can fail in field conditions because G×E was ignored. Heritability is also environment-specific.",
        ctx: "L05 §D — Phenotypic plasticity, reaction norms"
      }
    ],
    "L07": [
      {
        term: "Three requirements for measurable evolution in nature",
        def: "(1) HERITABLE variation in a trait. (2) DIFFERENTIAL reproduction — some variants leave more offspring. (3) Trait FREQUENCY changes across generations. All three observable in the field — that's what makes selection a measurable, testable process, not just a story.",
        example: "A field study shows 'darker beetles in polluted areas.' What additional data would you need to claim natural selection (vs. plasticity, drift, or sampling bias)?",
        exAnswer: "Need ALL of: (1) heritability test — do dark beetles' offspring tend to be dark? Mid-parent regression slope. (2) Differential reproduction — count surviving offspring of each color. (3) Frequency change over time — track the dark-allele frequency across multiple generations and compare to drift expectation. One of these without the others is just an observation, not selection. The Grants did all three on Daphne Major.",
        ctx: "L07 §A — Measuring selection in nature",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "selection-measurement-requirements"
      },
      {
        term: "Grants' Galápagos finches — predicted vs observed R",
        def: "After the 1977 Daphne Major drought, only deeper-beaked Geospiza fortis survived. Pre-drought mean beak depth ~9.31 mm; post-drought survivors ~9.84 mm → S ≈ 0.53 mm. Heritability h² ≈ 0.78 (parent-offspring regression). Predicted R = h²·S ≈ 0.41 mm. Observed next-generation mean shift matched the prediction.",
        example: "Why is the Grants' study a textbook example of measurable evolution in real time?",
        exAnswer: "Because every variable in the breeder's equation was MEASURED INDEPENDENTLY: h² from parent-offspring regression (~0.78), S from comparing survivors to pre-drought mean (~0.53 mm), and R from the actual next-generation mean. The predicted R (~0.41 mm) matched observation closely, confirming the theory's predictive power on a 1-year timescale. Evolution-by-natural-selection caught in action with no gaps in the causal chain.",
        ctx: "L07 §B — Grants' Galápagos finches",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "grants-finches"
      },
      {
        term: "Peppered moth industrial melanism — what was actually selected?",
        def: "Pre-industrial: light morph dominant on lichen-covered trunks. Industrial pollution killed lichen + blackened trunks → melanic morph rose to >95% in polluted areas. Mechanism: differential bird PREDATION on visible morphs. Genetic basis: a transposon insertion in the cortex gene.",
        example: "Why does this case decisively rule out 'mutation directed by environment' as an alternative to natural selection?",
        exAnswer: "Because the melanic mutation existed in the population BEFORE industrialization (low frequency). Pollution didn't induce the cortex-transposon insertion — it shifted the visibility-vs-bird-predation balance, selecting pre-existing dark variants. Confirmed by: (1) clean-air laws → light morphs rebounded as lichen returned (selection reverses, not mutation), (2) recent genomics showing the SAME transposon insertion across all melanic individuals (single ancient origin, then selection).",
        ctx: "L07 §C — Peppered moths",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "peppered-moth"
      },
      {
        term: "Antibiotic resistance — speed and predictability",
        def: "Strong directional selection by humans. Resistant variants pre-exist at low frequency; antibiotic kills susceptibles → resistant strains take over. Time to resistance often <2 years after a new drug's introduction. Mechanism: enzymatic destruction (β-lactamases), efflux pumps, target-protein mutations, alternative pathways.",
        example: "Why does FINISHING the antibiotic course have an evolutionary rationale?",
        exAnswer: "Stopping early leaves PARTIALLY-resistant survivors that aren't fully susceptible (their MIC was just below your peak dose). Those survivors then proliferate and acquire additional resistance mutations. A full course wipes out partial-resistants too — fewer survivors → less raw material for further evolution. Combination therapy multiplies this: needing simultaneous mutations in two targets reduces resistance probability from 10⁻⁹ to ~10⁻¹⁸.",
        ctx: "L07 §D — Antibiotic resistance",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "antibiotic-resistance"
      },
      {
        term: "Domestication = artificial selection (greyhound case)",
        def: "Humans choose breeders; resulting trait shifts are evolution by selection — same mechanism, different agent. Greyhounds: speed selected over centuries; modern racing greyhounds run ~64 km/h, ~20% faster than dog ancestors. Selection differential is intense and continuous.",
        example: "Compare the rate of greyhound speed evolution to natural-selection rates in wild populations. What sets the rate difference?",
        exAnswer: "Domestication rates are typically 10–100× faster than natural rates. Two reasons: (1) SELECTION DIFFERENTIAL is much stronger — humans pick a tiny fraction of top performers each generation, so S is huge; in the wild, S is bounded by ecology. (2) Generation time is uniform and short. Same h²·S formula applies, but S in domestication is artificially inflated. Belyaev's silver-fox tameness: visible behavioral evolution in 10 generations.",
        ctx: "L07 §D — Domestication, artificial selection",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "artificial-selection"
      },
      {
        term: "Why field selection studies need longitudinal data",
        def: "A snapshot 'darker individuals are more common today than yesterday' could be selection, drift, migration, sampling, or plasticity. To distinguish, you need: (1) tracked individuals across years, (2) measured heritability via parent-offspring, (3) replicate populations to control for drift, (4) genetic data ruling out migration.",
        example: "A field biologist sees 'beetles are darker this year than last.' What four alternative explanations must be ruled out before claiming natural selection?",
        exAnswer: "(1) DRIFT — small populations can shift by chance; need population-size estimate and replicate sites. (2) MIGRATION — dark beetles moved in; check genetic markers. (3) PLASTICITY — same beetles, different environments → darker due to temperature, not selection; common-garden experiment needed. (4) SAMPLING bias — different sampling effort/method captured a different cohort. Ruling each out requires longitudinal individual tracking, not snapshots.",
        ctx: "L07 §A — Measuring selection in nature",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "field-selection-confounds"
      },
      {
        term: "Influenza antigenic drift vs antigenic shift",
        def: "DRIFT: gradual mutational change in HA/NA surface proteins → escape from prior immunity → annual flu vaccines. SHIFT: dramatic reassortment when two flu strains co-infect one cell, swapping genome segments → pandemic potential. Drift = small, continuous; shift = big, episodic.",
        example: "Why do you need a flu shot every year, but not (typically) annual measles boosters?",
        exAnswer: "Influenza HA/NA evolves rapidly under SELECTION from human immune memory — drift accumulates ~0.5% sequence change per year, enough to escape antibodies. Last year's vaccine targets last year's epitopes. Measles HA/NA evolve much slower (long generation, lower mutation rate, immune-cost trade-off) — childhood vaccine confers near-lifelong immunity because the virus can't escape it. Faster pathogen evolution → shorter vaccine validity.",
        ctx: "L07 §D — Other examples — flu",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "flu-antigenic-evolution"
      },
      {
        term: "When does R = h²·S fail to predict the next generation?",
        def: "The breeder's equation assumes: (1) only V_A matters (no shared environment), (2) no covariance between trait and environment, (3) selection acts only on the focal trait, (4) no genotype-by-environment correlation, (5) no major shifts in the environment between generations.",
        example: "Predicted R from S = 8 cm and h² = 0.5 gives 4 cm response. Observed: 1 cm. What might explain the shortfall?",
        exAnswer: "Several common culprits: (a) PARENT-OFFSPRING ENVIRONMENT correlation inflated h² estimate (same nutrition makes parents AND offspring tall — looks heritable but isn't). (b) Inbreeding depression in the next gen reduced offspring fitness. (c) ENVIRONMENT changed between gens (drought reduced growth). (d) Selection actually targeted a different correlated trait. (e) Frequency-dependent selection eroded the additive variance. The breeder's equation is an idealization; field deviations point to which assumption broke.",
        ctx: "L07 §A — Measuring selection in nature",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "breeders-eqn-failures"
      }
    ],
    "L08": [
      {
        term: "Stepwise eye evolution stages",
        def: "(1) Light-sensitive patch (photoreceptors). (2) Cupped patch — directional sensitivity. (3) Pinhole eye (Nautilus) — image without lens. (4) Lensed eye — sharp focus via co-opted crystallins.",
        example: "Each stage must be functional — selection cannot 'plan' a future eye. Eyes have evolved >40 times independently. What does this convergence imply about complexity?",
        exAnswer: "Complex 'irreducible' structures aren't barriers to evolution — eyes have evolved >40 times because each step (light sensitivity, directionality, image, focus) confers fitness on its own. Convergence shows the gradient is climbable from many starting points. Complexity emerges from cumulative selection on functional intermediates, not from design.",
        ctx: "L08 §B — Vertebrate eye — stepwise model",
        mnem: "Patch → Cup → Pinhole → Lens (four functional steps)."
      },
      {
        term: "Neofunctionalization vs subfunctionalization",
        def: "After gene duplication: NEO — one copy gains a NEW function, the other keeps the original. SUB — duplicates SPLIT the ancestral function (each performs a subset).",
        example: "Hemoglobin alpha and beta arose by duplication, then specialized for adult vs fetal oxygen — that's subfunctionalization. The MYC family of TFs accumulated new tissue-specific roles — that's neofunctionalization.",
        ctx: "L08 §C — Regulatory networks, gene duplication",
        mnem: "Neo = Novelty · Sub = Split (the existing job)."
      },
      {
        term: "Heterochrony (paedo vs peramorphosis)",
        def: "Heterochrony = evolution of developmental TIMING. Paedomorphosis: adult retains juvenile traits (axolotl reproduces while gilled). Peramorphosis: development extends past ancestor (large antlers, exaggerated size).",
        example: "Human cranial proportions resemble juvenile chimps — that's paedomorphic. Irish elk antlers are 4 m wide — that's peramorphic. Why are timing changes such a powerful source of morphological novelty?",
        exAnswer: "Because timing is REGULATORY — flipping when/how long developmental programs run rewires the body without inventing new genes. A small heterochronic shift (extending growth, retaining a juvenile shape) cascades through every downstream tissue and produces dramatically different adult forms cheaply. Strong morphological change from minimal genetic change.",
        ctx: "L08 §D — Heterochrony",
        mnem: "Paedo = Pediatric (juvenile features kept) · Pera = Past (development extended)."
      },
      {
        term: "Hox genes — A-P body axis",
        def: "Cluster of TFs that pattern the anterior-posterior axis of bilaterians. Colinearity: chromosomal order matches body-axis expression order.",
        example: "Vertebrates have 4 Hox clusters (HoxA, B, C, D) from two whole-genome duplications. Flies have 1 cluster. What body-plan transitions correlate with cluster duplications?",
        exAnswer: "Two whole-genome duplications in early vertebrates (1R, 2R) created the four Hox clusters. This coincided with vertebrate body-plan elaboration: head, jaws, paired appendages, complex CNS. Teleost fish later underwent a third duplication (3R), correlated with their >30,000-species radiation. More Hox copies → more regulatory degrees of freedom → more body-plan complexity.",
        ctx: "L08 §E — Hox genes and conserved networks",
        mnem: "Hox = Head-to-tail patterning (linear order on chromosome = linear order on body)."
      },
      {
        term: "Cis-regulatory mutations vs structural",
        def: "Cis = changes WHEN/WHERE a gene is expressed (enhancer/promoter); structural = changes the protein itself. Cis is the leading edge of body-plan evolution because it's modular and tissue-specific.",
        example: "Stickleback fish lost pelvic spines via repeated cis-regulatory loss in the Pitx1 gene. The protein still works in teeth and elsewhere. Why is cis-regulatory evolution favored over structural change in pleiotropic genes?",
        exAnswer: "Structural changes alter the protein everywhere it's used, breaking other essential functions (pleiotropy → fitness cost, often lethal). Cis-regulatory changes are MODULAR — flipping one enhancer alters expression in one tissue/timepoint only. Pitx1 still works in teeth; only the pelvic enhancer was lost. Lower pleiotropic cost → cis is more evolvable for body-plan tweaks.",
        ctx: "L08 §C — Regulatory networks"
      },
      {
        term: "Vestigial structure (definition + examples)",
        def: "An ancestral structure with reduced or no current function. Whale pelvis, human appendix, snake hind-limb buds, ostrich wings, blind cave-fish eyes.",
        example: "Why isn't the human appendix 'evidence against evolution'? What does it positively support?",
        exAnswer: "Imperfect/'leftover' parts are EXPECTED if structures are inherited from ancestors and modified, not designed from scratch. The appendix supports common descent (cecum-derived, large in herbivorous ancestors) AND modification by descent (reduced as diet shifted). A pure-design hypothesis would predict no vestiges — vestigials are positive evidence FOR evolution.",
        ctx: "L08 §F — Imperfect adaptation"
      },
      {
        term: "Adaptation — noun vs verb (trait vs process)",
        def: "TRAIT use: 'the wing is an adaptation' — a heritable feature shaped by past selection FOR a current function. PROCESS use: 'the population is undergoing adaptation' — the verb-act of evolving under selection. Same word, two distinct claims.",
        example: "An exam asks: 'Bat wings are an adaptation for flight.' Identify which sense is meant, and explain why claiming a trait IS an adaptation is a strong claim that needs evidence.",
        exAnswer: "Trait sense (noun). Calling something AN adaptation FOR X commits to: (1) heritable variation in the trait, (2) historical fitness benefit specifically in function X, (3) ideally a comparative or experimental test. Otherwise the trait may be an EXAPTATION (co-opted from another role — feathers were thermoregulatory before flight) or a BYPRODUCT (no selection at all — chin shape in humans). The verb sense just labels change; the noun sense commits to a function.",
        ctx: "L08 §A — Adaptation as trait & process",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "adaptation-noun-vs-verb"
      },
      {
        term: "Protein promiscuity → cooption",
        def: "Promiscuity = a protein has weak side-activities beyond its main function. Selection can refine those weak activities into new primary roles. Major source of evolutionary novelty without inventing new genes from scratch.",
        example: "Eye-lens crystallins were co-opted from heat-shock proteins and metabolic enzymes. Antarctic notothenioid antifreeze glycoprotein co-opted from a digestive enzyme. What does cooption tell you about how 'novel' traits are usually built?",
        exAnswer: "Novelty rarely comes from de novo gene invention. The existing protein toolkit, with its built-in promiscuous side-activities, provides raw material that selection sharpens into new functions. Complex 'new' organs (lenses, antifreeze, venoms) often share deep homology with seemingly unrelated machinery. The real innovation is regulatory tweaking + sequence refinement, not creation. This is also why so many enzymes have moonlighting roles.",
        ctx: "L08 §C — Regulatory networks, gene duplication",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "cooption"
      }
    ],
    "L09": [
      {
        term: "Coevolution vs coexistence",
        def: "Coevolution = RECIPROCAL evolutionary change in interacting lineages. Coexistence ≠ coevolution; both species could be in their own equilibria without reciprocal pressure.",
        example: "Two species have lived in the same forest for a million years and look co-adapted. What evidence would show coevolution rather than mere coexistence?",
        exAnswer: "RECIPROCAL trait change tracked across populations or time: where species A's defense is strong, species B's offense is also strong; where A's defense is weak, B's offense is weak. Static co-adaptation could be coincidence. Matched DYNAMIC variation (e.g., newt TTX matches snake resistance across the range) is the diagnostic for mutual selective pressure. Look for geographic correlation, not just coexistence.",
        ctx: "L09 §A — Defining reciprocal coevolution"
      },
      {
        term: "Newt-snake arms race (TTX example)",
        def: "Newts (Taricha) make tetrodotoxin (TTX) blocking Na channels. Snakes (Thamnophis) evolve TTX-resistant Na channels. Toxic newt populations occur where resistant snakes are; mismatched populations have neither.",
        example: "A garter-snake population is highly TTX-resistant but slow as a result. What evolutionary force caps the escalation? (Trade-off: resistance reduces locomotion → predation by birds.)",
        ctx: "L09 §B — Antagonistic arms races"
      },
      {
        term: "Batesian vs Müllerian mimicry",
        def: "BATESIAN: harmless mimic resembles harmful model; mimic must stay rare or predators learn to ignore signal. MÜLLERIAN: multiple HARMFUL species converge on a shared warning signal — all gain protection together.",
        example: "Viceroy butterfly looks like monarch. Both are noxious — that's Müllerian. A non-toxic fly looks like a wasp — that's Batesian. Why does mimic frequency matter only for Batesian?",
        exAnswer: "Predators learn from costly experiences. In BATESIAN (mimic is harmless), predators that attack mimics get rewarded — so if mimics outnumber models, the warning signal stops working and the bluff fails. Frequency-dependent: mimic must stay rare. In MÜLLERIAN (both noxious), every encounter teaches the SAME lesson — both species reinforce the signal. Frequency doesn't matter; both can be common.",
        ctx: "L09 §D — Mimicry",
        mnem: "Bates = Bluff (one liar) · Müller = Mutual (both honest)."
      },
      {
        term: "Geographic Mosaic Theory of Coevolution (Thompson)",
        def: "Coevolution intensity varies across the range — HOTSPOTS (intense reciprocal selection) + COLDSPOTS (weak/none). Gene flow + local trait evolution → mosaic of coevolutionary states; mismatch is positive evidence of dynamic process.",
        example: "Crossbill bird beaks match local pine cone shapes in some valleys but not others. Trait MISMATCH is consistent with the Mosaic Theory rather than refuting coevolution. Why?",
        exAnswer: "Gene flow between populations + locally varying selection → trait combinations chase local conditions imperfectly. The Mosaic Theory PREDICTS mismatch in some places (coldspots, recent immigration, weak selection) and tight matching in others (hotspots). Mismatch is therefore a SIGNATURE of dynamic coevolution, not a refutation. A frozen, perfectly-co-adapted pair would actually be unusual under this model.",
        ctx: "L09 §E — Geographic Mosaic Theory"
      },
      {
        term: "Pollinator-flower mutualism (Darwin's orchid prediction)",
        def: "Reciprocal coevolution where flower morphology and pollinator anatomy track each other tightly — both partners gain fitness. Flower gets pollen transfer; pollinator gets food. Tight matches are evidence of past coevolutionary feedback.",
        example: "Darwin saw the long-spurred Madagascar orchid (Angraecum sesquipedale, 25-cm spur) and PREDICTED a hawkmoth with that exact tongue must exist. Decades after his death, Xanthopan morganii praedicta was discovered with a 25-cm tongue. What evolutionary process produced the tight match?",
        exAnswer: "Reciprocal selection. Flowers with longer spurs forced moths to push deeper, increasing pollen contact → flower fitness rewarded longer spurs. Moths with longer tongues reached more nectar with less effort → moth fitness rewarded longer tongues. Each lineage's selection pressure was generated BY the other lineage's traits — coevolutionary feedback loop. The match isn't coincidence; it's a steady state shaped by mutual escalation.",
        ctx: "L09 §C — Mutualistic coevolution",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "mutualism-pollinator"
      },
      {
        term: "Endosymbiosis: two distinct organelle origins",
        def: "Eukaryotes acquired organelles by engulfing free-living bacteria. MITOCHONDRIA: alphaproteobacterium ancestor, ~2.0–1.6 GYA, in the eukaryotic stem (universal). CHLOROPLASTS: cyanobacterium ancestor, ~1.5 GYA, in the Archaeplastida lineage (plants + algae) only — happened in cells that already had mitochondria.",
        example: "Animals have mitochondria but no chloroplasts; plants have both; some protists have neither in functional form. What does this distribution tell you about the order and exclusivity of the two endosymbiotic events?",
        exAnswer: "Mitochondrial endosymbiosis happened FIRST in the eukaryotic stem lineage — universal across surviving eukaryotes (animals, plants, fungi, protists). Chloroplast endosymbiosis happened LATER in only ONE daughter lineage (Archaeplastida → plants and algae). Animals branched off before that event, so they never inherited chloroplasts. The two events are nested in the eukaryotic tree, not parallel. (Tertiary endosymbiosis later spread chloroplasts to other lineages by engulfing algae whole.)",
        ctx: "L09 §C — Mutualistic coevolution",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "endosymbiosis-events"
      }
    ],
    "L11": [
      {
        term: "Twofold cost of sex (Maynard Smith)",
        def: "An asexual female passes 100% of her genes; a sexual female passes 50% (half from male). Per-offspring gene transmission is HALVED in sexual species — sex must produce ≥2× the benefit to break even.",
        example: "Despite the twofold cost, sex is nearly universal in eukaryotes. Name three benefits proposed to outweigh the cost. (Recombination · Muller's ratchet relief · Red Queen against parasites.)",
        ctx: "L11 §A — Cost of sex / why sex evolved",
        mnem: "2× cost: sex passes ½ the genes per offspring."
      },
      {
        term: "Red Queen hypothesis",
        def: "Sex (recombination) is favored because parasites coevolve rapidly; new allele combinations help hosts stay one step ahead. Named for Lewis Carroll's queen who must run to stay in place.",
        example: "Why are asexual lineages over-represented in young Daphnia clones but rare in old phylogenetic lineages? (They lose to parasites over evolutionary time — Red Queen extinction filter.)",
        ctx: "L11 §A — Cost of sex / why sex evolved"
      },
      {
        term: "Muller's ratchet",
        def: "Asexual lineages cannot purge slightly deleterious mutations efficiently; mutations accumulate one-way (the 'ratchet' clicks but never unclicks) → mutational meltdown over time.",
        example: "Why is recombination needed to escape this fate? Crossover can generate offspring chromosomes free of the worst mutations the parent carried.",
        ctx: "L11 §A — Cost of sex / why sex evolved"
      },
      {
        term: "Anisogamy = the basis of male/female",
        def: "Anisogamy = unequal gamete sizes. The sex producing larger, costlier gametes is FEMALE; the sex producing smaller, cheaper gametes is MALE. Behavior follows from gamete asymmetry, not the reverse.",
        example: "Some algae are isogamous (equal gametes); these don't have 'males/females' in the usual sense. Why does anisogamy lead to selective females and competing males?",
        exAnswer: "Females invest more per gamete (larger, costlier eggs) → reproductive output is limited by their RESOURCES, so they should be choosy to ensure good outcomes. Males produce many cheap sperm → reproductive output is limited by ACCESS TO EGGS (i.e., females), so they compete for matings. Asymmetric investment drives asymmetric strategies. The behavioral pattern follows from the gamete-size economics, not the reverse.",
        ctx: "L11 §B — Anisogamy"
      },
      {
        term: "Fisher's runaway",
        def: "Arbitrary female preference + heritable male trait → offspring inherit BOTH preference and trait → preferred trait amplifies generationally even if costly. Self-reinforcing loop.",
        example: "Peacock tail. Females prefer long tails; sons inherit long tails AND daughters inherit the preference. The trait runs away until natural-selection cost balances sexual-selection benefit.",
        ctx: "L11 §C — Sexual selection"
      },
      {
        term: "Intrasexual vs intersexual selection",
        def: "INTRA = competition WITHIN one sex (usually male-male combat → weapons, large body). INTER = mate CHOICE by the other sex (usually females choosing → ornaments).",
        example: "Elk antlers (intrasexual, weapons) vs peacock tail (intersexual, ornament). Both are sexual selection but with very different signatures. Which targets survival more?",
        exAnswer: "Both impose survival costs but in different ways. INTRASEXUAL weapons (antlers) divert energy and risk injury during contests. INTERSEXUAL ornaments (peacock tails) increase predation risk AND metabolic cost — and they signal honest underlying viability. Ornaments are 'handicaps' (Zahavi): costly precisely BECAUSE they reduce survival, which is what makes them honest signals of fitness. Ornaments push survival costs harder; weapons push contest costs harder.",
        ctx: "L11 §C — Sexual selection",
        mnem: "Intra = Inside-the-sex contest · Inter = Inter-sex choice."
      },
      {
        term: "Sexual conflict — when do interests diverge?",
        def: "Sexual conflict = males and females have OPPOSING optimal strategies. Conflict arises whenever a male's optimum (more matings, more paternity assurance) reduces female fitness (cost of remating, harassment, harmful traits).",
        example: "Bedbug 'traumatic insemination': males pierce the female abdomen to inseminate. Females evolve thickened spermalege organs to absorb damage. Duck drakes: corkscrew penises; females: counter-coiled vaginas redirecting unwanted sperm. What general pattern drives these morphologies?",
        exAnswer: "Antagonistic coevolution WITHIN a species. Male traits evolve to maximize male fitness even when they lower female fitness; female counter-traits evolve to neutralize the male trait. Each side's adaptation imposes new selection on the other → arms race within the species. Common signatures: male coercion structures, female resistance morphology, rapid divergence of genitalia even between closely-related species.",
        ctx: "L11 §D — Conflict, sperm competition",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "sexual-conflict"
      },
      {
        term: "Sperm competition — male anatomical responses",
        def: "When females mate with multiple males, sperm of different males compete to fertilize. Selection has produced large testes (more sperm), long sperm (faster), mating plugs (block rivals), removal devices (scoop out rival sperm), and copulation-extension behaviors (mate-guard).",
        example: "Chimpanzees (promiscuous mating) have testes ~3× the size of human testes for body weight; gorillas (single-male harems) have small testes for their body size. What does testis size predict, and why?",
        exAnswer: "Testis size scales with the INTENSITY of sperm competition. Promiscuous mating systems → high competition → bigger testes (more sperm = better lottery odds). Monogamous or harem systems → low competition → small testes (no rival sperm in there with yours). Comparative anatomy across primates is a clean test of the prediction. Humans (intermediate testes) suggest moderate ancestral sperm competition.",
        ctx: "L11 §D — Conflict, sperm competition",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "sperm-competition"
      },
      {
        term: "Cryptic female choice — why it matters",
        def: "Females bias paternity AFTER copulation via reproductive-tract mechanisms — sperm storage organs, sperm rejection or digestion, differential sperm transport. 'Cryptic' because the choice happens internally, invisible to outside observers.",
        example: "In some insects, females have multiple sperm-storage organs (spermathecae). After mating with several males, the female can preferentially fertilize from one organ. Why does this matter beyond pre-copulatory choice?",
        exAnswer: "Pre-copulatory choice (mate selection) is the visible part of female choice; cryptic female choice extends female preference into the period AFTER mating. Critical when females can't fully avoid mating with all males (coercion, random encounters, sperm storage from past matings). Allows post-hoc filtering of sperm by quality, novelty (preferring genetically dissimilar sperm), or compatibility. Now considered a major component of sexual selection in many taxa.",
        ctx: "L11 §D — Conflict, sperm competition",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "cryptic-female-choice"
      }
    ],
    "L12": [
      {
        term: "Three theories of senescence",
        def: "(1) MUTATION ACCUMULATION (Medawar): late-life deleterious mutations escape selection because few individuals reach old age. (2) ANTAGONISTIC PLEIOTROPY (Williams): one allele helps young, hurts old; selection net-favors it. (3) DISPOSABLE SOMA (Kirkwood): maintenance vs reproduction trade-off — invest in reproduction, not body upkeep.",
        example: "These theories are NOT mutually exclusive. Huntington's (late-life dominant lethal) fits which? (Mutation accumulation — selection blind to it because onset post-reproductive.)",
        ctx: "L12 §C — Theories of senescence",
        mnem: "MAD: Mutation accumulation · Antagonistic pleiotropy · Disposable soma."
      },
      {
        term: "Extrinsic mortality → life history",
        def: "HIGH extrinsic mortality (predation, disease) selects for FAST life history: early maturity, many small offspring, short life. LOW extrinsic mortality selects for SLOW: delayed maturity, fewer large offspring, long life.",
        example: "Mainland opossums (with predators) mature ~2 yr earlier than island opossums (no predators). This shift evolves in tens of generations. Predict expected life-history of a long-isolated, predator-free island species.",
        exAnswer: "SLOW life history: delayed maturity, fewer/larger offspring, longer life, often greater body size. Examples: Galápagos tortoises (~100 yr lifespan), kakapos (the heaviest parrot), dodos. CRITICAL VULNERABILITY: this slow strategy collapses when predators arrive — selection can't 'reverse' fast enough. Introduced rats, cats, and humans decimated island faunas precisely because of this evolved response to predator-free conditions.",
        ctx: "L12 §B — Extrinsic mortality"
      },
      {
        term: "r vs K selection",
        def: "r-selected: high reproductive rate, many small offspring, little parental care, short life — favored in unstable/empty environments. K-selected: low rate, few large offspring, parental care, long life — favored in saturated, competitive environments.",
        example: "Mice, weeds, and most insects → r. Elephants, oaks, humans → K. What predicts where on the r-K continuum a species sits? (Density and stability of resources.)",
        ctx: "L12 §D — Age at maturity, offspring size",
        mnem: "r = Rapid (many small) · K = Carrying-capacity (few big)."
      },
      {
        term: "Life-history trade-offs — what's the currency?",
        def: "Trade-offs are inverse fitness relationships between traits, mediated by SHARED LIMITED RESOURCES. Currencies: ENERGY (calories), TIME (development vs reproduction), MORTALITY RISK (current vs future). One pool can't fund two competing demands.",
        example: "Salmon swim upstream and reproduce ONCE, expending nearly all energy → die. Albatrosses reproduce slowly across decades. Both are stable, evolved life histories. What single concept explains why both work?",
        exAnswer: "Both maximize LIFETIME reproduction given their extrinsic mortality regime. Salmon face high marine mortality during return migration → big-bang reproduction is optimal (don't bank on a second chance). Albatrosses face low adult mortality → slow steady reproduction across decades pays off. The trade-off CURRENCY (energy + mortality) balances differently because the constraints differ. Selection navigates trade-offs; it can't break them.",
        ctx: "L12 §A — Trade-offs in energy allocation",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "life-history-tradeoffs"
      },
      {
        term: "Offspring number vs size (bet-hedging vs provisioning)",
        def: "Fixed reproductive budget can be split many ways. MANY-SMALL: each gets less per-offspring; variance averaged across many; bet-hedging in unpredictable environments. FEW-LARGE: each well-provisioned; higher per-offspring survival; pays off when environment is stable AND offspring face intense competition.",
        example: "Trout lay thousands of small unprotected eggs. Sharks lay a few large eggs (some live-born after gestation). Predict each species' selective environment from its strategy.",
        exAnswer: "Trout: high & unpredictable juvenile mortality (predation, dispersal lottery) → many small eggs hedge against any one cohort being wiped out. Sharks: stable predator/competitive environment, slow growth, high parental investment → each large offspring is competitive at hatching. The OPTIMUM is set by the offspring survival curve as a function of size. Flat curves favor many-small; steep curves favor few-large.",
        ctx: "L12 §D — Age at maturity, offspring size",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "offspring-size-tradeoff"
      },
      {
        term: "Seychelles warblers — why help, not disperse?",
        def: "Seychelles warblers are cooperative breeders. Adult offspring (especially daughters on high-quality territories) STAY at the natal nest and help raise siblings instead of dispersing to breed independently. Helpers gain inclusive fitness AND can inherit the territory.",
        example: "On low-quality territories, helpers leave to breed elsewhere. On high-quality territories, helpers stay and assist. What two evolutionary forces is this consistent with?",
        exAnswer: "(1) KIN SELECTION — helping siblings (r=0.5) raises indirect fitness; on a saturated high-quality territory, the daughter's expected own-offspring (if she dispersed to a poor territory) may be LOWER than the kin-fitness she earns by helping. (2) ECOLOGICAL CONSTRAINT — when good territories are saturated, dispersing to a marginal one is worse than waiting. Hamilton's rule (rB > C) is satisfied because C of staying is low (no breeding territory available anyway). Two forces, same direction.",
        ctx: "L12 §E — Seychelles warblers",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "cooperative-breeding"
      }
    ],
    "L13": [
      {
        term: "Hamilton's rule: rB > C",
        def: "An altruistic act is favored when r·B > C. r = relatedness coefficient, B = benefit to recipient (in offspring units), C = cost to actor.",
        example: "Saving a sibling (r=0.5) at cost C=1 to actor is favored if benefit B > 2 (because 0.5·B > 1 requires B>2). Saving a cousin (r=0.125)? Need B > 8.",
        ctx: "L13 §B — Kin selection / inclusive fitness",
        mnem: "rB beats C: Relatedness × Benefit > Cost."
      },
      {
        term: "Coefficient of relatedness — common values",
        def: "Identical twins: r=1.0. Parent-offspring: r=0.5. Full sib: r=0.5. Half-sib: r=0.25. First cousin: r=0.125. Hymenopteran sisters (haplodiploid): r=0.75.",
        example: "Why are female workers in bee colonies more related to their sisters (r=0.75) than to their own potential offspring (r=0.5)? This was Hamilton's haplodiploidy explanation for eusociality.",
        ctx: "L13 §B — Kin selection / inclusive fitness",
        mnem: "Twin 1.0 · Sib 0.5 · Half 0.25 · Cousin 0.125 · Bee-sis 0.75."
      },
      {
        term: "Inclusive fitness",
        def: "Total genetic contribution to next generation = direct fitness (own offspring) + indirect fitness (extra offspring of relatives, weighted by r). Captures evolutionary success of an allele, not just an individual.",
        example: "A worker bee leaves no direct offspring. How can her behavior be evolutionarily favored? (All her contribution is indirect — through the queen's offspring weighted by r.)",
        ctx: "L13 §B — Kin selection / inclusive fitness"
      },
      {
        term: "Evolutionarily Stable Strategy (ESS)",
        def: "A strategy that, once common in a population, cannot be invaded by any rare alternative — i.e., a Nash equilibrium for evolutionary games. Fitness depends on what others do (frequency-dependent).",
        example: "All-Hawk is unstable (everyone gets injured). All-Dove is unstable (a Hawk invades easily). The ESS is a MIXED population at frequency p* = V/(V+C) Hawks where V=resource value, C=injury cost.",
        ctx: "L13 §C — Evolutionarily stable strategies",
        mnem: "ESS = 'no rare invader can break in.'"
      },
      {
        term: "Hawk-Dove game payoffs",
        def: "Hawk vs Hawk: ½(V−C) each (fight, ½ chance win/lose). Hawk vs Dove: V (Hawk takes), 0 (Dove flees). Dove vs Dove: V/2 each (share). When V<C, mixed ESS at p_Hawk = V/C.",
        example: "V=10, C=20. ESS Hawk frequency = 10/20 = 0.5. What if V > C? (Pure-Hawk ESS — fighting is worth it always.)",
        ctx: "L13 §C — Evolutionarily stable strategies",
        mnem: "p_Hawk* = V/C when V<C; pure Hawk when V≥C."
      },
      {
        term: "Side-blotched lizard rock-paper-scissors",
        def: "Three male morphs of Uta stansburiana cycle in frequency: ORANGE (aggressive territory) > BLUE (mate-guarding) > YELLOW (sneaker) > ORANGE again. No single ESS — stable cyclic dynamic from negative frequency-dependent selection.",
        example: "When orange males are common, yellow sneakers exploit them. Yellows rise → blues catch sneakers → blues common → oranges defeat blues. Why doesn't selection drive ANY morph to fixation?",
        exAnswer: "NEGATIVE frequency-dependent selection: each morph's fitness depends on what's currently common. Whichever morph is at high frequency gets exploited by its predator-strategy; rarity is rewarded. The rock-paper-scissors structure means no strategy is 'best' independent of frequency — fixation is impossible because the loser-of-fixation is always the morph currently winning. Result: stable cycles of ~5–6 years, not equilibrium.",
        ctx: "L13 §D — Side-blotched lizards (rock-paper-scissors)",
        mnem: "O→B→Y→O: Orange beats Blue beats Yellow beats Orange."
      },
      {
        term: "Direct vs indirect reciprocity",
        def: "DIRECT: tit-for-tat between two individuals; needs repeated encounters & memory. INDIRECT: reputation-based; helping earns help from third parties; needs visibility/communication.",
        example: "Vampire bats regurgitate blood to non-relatives — direct reciprocity, well-documented. Why does indirect reciprocity scale better in large groups?",
        exAnswer: "Direct reciprocity requires REPEAT encounters with the SAME individual — viable in small groups where everyone meets everyone (pair-bonded primates, vampire bat roosts). In large or fluid groups, you may never re-encounter a partner, so tit-for-tat fails. Indirect reciprocity uses REPUTATION (third-party observers, gossip, public scoring), which scales because helpers earn help from anyone in the group, not just the recipient. Language and norms supercharge it.",
        ctx: "L13 §E — Cooperation among non-kin"
      },
      {
        term: "Group selection — why naive version fails",
        def: "Within a group, individual cheaters have HIGHER fitness than altruistic group-helpers; cheating spreads, cooperation collapses — even if altruistic groups outproduce selfish groups, within-group selection wins on faster timescale.",
        example: "Modern view accepts multilevel selection in narrow conditions (frequent extinction, strict subdivision), but mostly explains 'group benefits' via individual or kin selection. Why is haystack-mouse selection a textbook valid case?",
        exAnswer: "Maynard Smith's haystack scenario: mice colonize haystacks, breed in isolation for several generations, then disperse and recolonize new haystacks. Selection runs at TWO LEVELS with limited mixing — within-haystack (selfish wins) AND among-haystack (cooperative haystacks produce more colonizers because cheaters eat their groupmates and starve). When inter-group structure is STRONG and extinction is FREQUENT, the among-group component can outpace the within-group component, and cooperation fixes despite individual disadvantage.",
        ctx: "L13 §A — Individual vs group selection"
      },
      {
        term: "Hawk-Dove ESS when V ≥ C (pure-Hawk case)",
        def: "When the resource value V ≥ injury cost C, Hawk strategy dominates regardless of opponent. Pure-Hawk is the ESS. The mixed equilibrium p* = V/C only applies when V < C (cost exceeds value).",
        example: "V = 15, C = 10. Compute the would-be mixed-ESS Hawk frequency p* = V/C. Why is the answer not biologically meaningful, and what's the actual ESS?",
        exAnswer: "p* = 15/10 = 1.5 — but a frequency can't exceed 1.0, signaling the formula is OUT OF ITS VALID DOMAIN (V < C). Interpretation: when the resource is worth more than the injury cost, fighting always pays in expectation, so every individual should escalate. Pure-Hawk is the unique ESS. No Doves can invade because Hawks beat Doves head-to-head AND Hawk vs Hawk still nets positive payoff (½(V−C) = +2.5 > 0). The mixed formula presumes V<C; outside that, fix-Hawk wins.",
        ctx: "L13 §C — Evolutionarily stable strategies",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "hawk-dove-ess",
        mnem: "p* > 1 means 'always Hawk.' p* < 0 means 'always Dove.' Mixed ESS only inside [0,1]."
      }
    ],
    "L14": [
      {
        term: "Major life-history milestones (timeline)",
        def: "~3.5–3.8 GYA: first cells. ~2.4 GYA: Great Oxidation Event (cyanobacteria). ~2.1–1.6 GYA: first eukaryotes (mitochondrial endosymbiosis). ~1.0 GYA: multicellularity. ~541 MYA: Cambrian explosion. ~252 MYA: end-Permian. ~66 MYA: K-Pg.",
        example: "Order these from oldest to youngest: K-Pg, Cambrian, GOE, eukaryotes, multicellularity, end-Permian. Answer: GOE → eukaryotes → multicellularity → Cambrian → end-Permian → K-Pg.",
        ctx: "L14 §B — Major milestones",
        mnem: "GEM-CPK: GOE · Eukaryotes · Multicell · Cambrian · Permian · K-Pg."
      },
      {
        term: "Big Five mass extinctions",
        def: "End-Ordovician, Late Devonian, end-Permian (largest, ~95% marine), end-Triassic, end-Cretaceous (K-Pg, ~66 MYA, dinos).",
        example: "Causes vary: end-Permian (Siberian Traps + acidification + climate), K-Pg (Chicxulub asteroid → iridium layer). Why does each event reshape post-event radiations?",
        exAnswer: "Mass extinctions empty niches NON-RANDOMLY — surviving lineages diversify into the suddenly-vacant ecospace (adaptive radiation). K-Pg cleared dinosaurs → mammalian radiation into large-body and arboreal niches. End-Permian wiped most marine clades → modern fauna originated from a few survivors. The 'who survives' is partly luck (small body, generalist diet, deep-water refuge), so post-event radiations are CONTINGENT on whichever subset happened to make it through.",
        ctx: "L14 §D — Mass extinctions",
        mnem: "OD-PTC: Ordovician · Devonian · Permian · Triassic · Cretaceous (in time order)."
      },
      {
        term: "Radiometric dating logic",
        def: "Parent isotope decays to daughter at known half-life. Age = ln(1+D/P)/λ where D/P = daughter/parent ratio, λ = decay constant. Different isotope systems for different timescales.",
        example: "¹⁴C: ~5,730 yr half-life — useful to ~50 KYR. K-Ar: 1.25 GYR half-life — millions to billions. U-Pb: zircons date Earth at 4.4 GYA. Why can't ¹⁴C date a dinosaur fossil?",
        exAnswer: "¹⁴C half-life is ~5,730 yr, useful range ~10 half-lives = ~50 KYR. After ~10 half-lives, parent isotope is below detection (~0.1% remaining). Dinosaurs went extinct ~66 MYA → ~11,500 ¹⁴C half-lives ago → effectively zero ¹⁴C left. Need a longer-half-life system: K-Ar (1.25 GYR half-life) or U-Pb in zircons (~4.5 GYR), which work across millions to billions of years. Match the system to the timescale.",
        ctx: "L14 §A — Earth's age, dating methods"
      },
      {
        term: "Great Oxidation Event — cause and consequence",
        def: "~2.4 GYA. Cyanobacteria evolved oxygenic photosynthesis ~3 GYA; for 600 MY, O₂ was buffered by reactions with dissolved Fe²⁺ (banded iron formations). Once Fe²⁺ ran out, free O₂ accumulated → oxidized atmosphere → mass extinction of obligate anaerobes + opened door to aerobic metabolism + multicellularity.",
        example: "Why did the GOE take ~600 MY between cyanobacterial origin (~3.0 GYA) and atmospheric O₂ rise (~2.4 GYA)?",
        exAnswer: "BUFFER: ferrous iron (Fe²⁺) dissolved in Earth's oceans reacted with the new O₂ to precipitate as iron oxide on the seafloor — visible today as banded iron formations (BIFs). For 600 MY, O₂ was scrubbed almost as fast as it was produced. Only when this iron sink was depleted did O₂ start accumulating in the atmosphere. Geochemistry, not biology, set the timeline.",
        ctx: "L14 §B — Major milestones",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "great-oxidation-event"
      },
      {
        term: "Cambrian explosion — what drove the radiation?",
        def: "~541–520 MYA. Most animal phyla appear in the fossil record within ~20 MY. Proposed drivers: (1) O₂ rose past a threshold enabling large active animals; (2) emergence of Hox-based body-plan toolkit allowed regulatory experimentation; (3) ecological positive-feedback (predators select for armor, vision, sediment-burrowing) — the 'arms-race' hypothesis.",
        example: "Why is the Cambrian called an 'explosion' but seen as a continuation of pre-Cambrian trends in molecular phylogenies?",
        exAnswer: "FOSSILS appear suddenly because hard parts (shells, exoskeletons) preserve well; soft-bodied ancestors had been diversifying for >100 MY (cf. Ediacaran biota). MOLECULAR clocks date most phylum splits to 700+ MYA — so the 'explosion' is partly a fossilization artifact (the appearance of armor + body plans). Hox + Pax + Wnt regulatory toolkits were already in place; the Cambrian saw their first explorations of complex morphology.",
        ctx: "L14 §B — Major milestones",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "cambrian-explosion"
      },
      {
        term: "Geological eras — Paleozoic / Mesozoic / Cenozoic",
        def: "PALEOZOIC (541–252 MYA): 'old life' — Cambrian explosion through end-Permian; trilobites, fishes, amphibians, early reptiles. MESOZOIC (252–66 MYA): 'middle life' — Triassic, Jurassic, Cretaceous; age of dinosaurs. CENOZOIC (66 MYA–now): 'new life' — mammalian radiation post-K-Pg.",
        example: "An exam asks: 'In which era did jawed fishes first dominate? Mammals first appear? Mammals first dominate?'",
        exAnswer: "Jawed fishes dominated the DEVONIAN ('Age of Fishes,' Paleozoic, ~416–359 MYA). Mammals first appeared in the late TRIASSIC (early Mesozoic, ~225 MYA) — but stayed small and nocturnal under dinosaurs. Mammals first DOMINATED in the early CENOZOIC after the K-Pg extinction (~66 MYA) emptied dinosaur niches. Same lineage, three different ecological roles across the eras.",
        ctx: "L14 §C — Geological periods",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "geo-eras",
        mnem: "PMC = Paleo · Meso · Ceno (oldest to newest)."
      },
      {
        term: "Endosymbiosis evidence (Margulis)",
        def: "Mitochondria and chloroplasts have: (1) circular DNA like bacteria, (2) ribosomes more similar to bacterial than eukaryotic, (3) double membranes (outer = host vesicle, inner = bacterial), (4) divide by binary fission, (5) sequenced rRNA places mitochondria with alphaproteobacteria, chloroplasts with cyanobacteria.",
        example: "Margulis' hypothesis was rejected for 15 years before becoming consensus. What single line of evidence finally convinced most skeptics?",
        exAnswer: "DNA SEQUENCING — when mitochondrial 16S rRNA was sequenced in the 1980s, it grouped CLEANLY with alphaproteobacteria (specifically Rickettsia-related lineages), not with any eukaryotic gene. Chloroplast rRNA grouped with cyanobacteria. The phylogenetic placement was unambiguous and could only be explained by an actual horizontal-merger ancestry, not by convergent evolution of organelle features.",
        ctx: "L14 §B — Major milestones",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "endosymbiosis-evidence"
      }
    ],
    "L15": [
      {
        term: "Reading a phylogenetic tree — closeness rule",
        def: "Closeness of relationship is determined by RECENCY OF COMMON ANCESTOR (depth of shared node), NOT by horizontal distance on the page. Trees can be rotated at any node without changing relationships.",
        example: "On a tree of (mouse, (human, chimp)), human and chimp are more closely related to each other than either is to mouse — even if mouse is drawn 'right next to' human. Why is rotation allowed?",
        exAnswer: "A tree's information lives in its TOPOLOGY (which nodes connect to which) and BRANCH LENGTHS (time/divergence) — NOT in the left/right ordering at branch points. Spinning a node 180° preserves all this information; only the page layout changes. Two trees that look different but rotate into each other are the SAME tree. Reflex check: count nodes between taxa, not pixels.",
        ctx: "L15 §A — Reading phylogenetic trees",
        mnem: "Look at the NODE, not the page-distance."
      },
      {
        term: "Synapomorphy vs symplesiomorphy vs homoplasy",
        def: "SYNAPOMORPHY = shared DERIVED state — defines a clade (informative). SYMPLESIOMORPHY = shared ANCESTRAL state — uninformative for grouping. HOMOPLASY = independently evolved similarity (convergence/parallelism/reversal) — misleading.",
        example: "Feathers in birds are a synapomorphy (defines bird clade). Vertebrae in birds are a symplesiomorphy (shared with all vertebrates). Wings in bats and birds are homoplasy (independent flight evolution).",
        ctx: "L15 §B — Synapomorphy / symplesiomorphy / homoplasy",
        mnem: "SYN-derived = clade-defining · SYM-ancestral = useless for grouping · HOMO-convergent = misleading."
      },
      {
        term: "Monophyletic / paraphyletic / polyphyletic",
        def: "MONOPHYLETIC (clade) = ancestor + ALL descendants (only valid group). PARAPHYLETIC = ancestor + SOME descendants (excludes some — e.g., 'reptiles' without birds). POLYPHYLETIC = members lacking shared immediate ancestor (built on convergence — e.g., 'warm-blooded animals').",
        example: "Reptilia excluding birds is paraphyletic (birds are also descended from the reptile ancestor). 'Flying vertebrates' (bats + birds + pterosaurs) is polyphyletic. Modern systematics rejects both.",
        ctx: "L15 §C — Mono / para / polyphyletic",
        mnem: "MONO = M-all (ancestor + ALL) · PARA = P-art (ancestor + part) · POLY = P-ick-and-mix (no shared ancestor)."
      },
      {
        term: "Outgroup",
        def: "A taxon known to lie outside the clade being studied — used to root the tree and polarize character states (which is ancestral, which derived).",
        example: "Studying primate phylogeny: tree shrews or mice as outgroup. Why is outgroup choice critical for distinguishing synapomorphy from symplesiomorphy?",
        exAnswer: "An outgroup tells you which character state is ANCESTRAL (the state shared with the outgroup) vs DERIVED (the state new in the ingroup). Without polarization, you can't tell whether a shared trait is informative (shared derived = synapomorphy = clade) or uninformative (shared ancestral = symplesiomorphy). A bad outgroup (too close to ingroup, or itself nested in ingroup) biases or misroots the entire tree. Outgroup must be confidently outside the ingroup AND share enough characters to be alignable.",
        ctx: "L15 §B — Synapomorphy / symplesiomorphy / homoplasy"
      },
      {
        term: "Crown group vs stem group",
        def: "CROWN group = all descendants of the most recent common ancestor of all LIVING members of a clade. STEM group = extinct lineages that branched off before the crown but are part of the broader clade (e.g., 'feathered theropods are stem-birds').",
        example: "All living birds + their MRCA + descendants = crown Aves. Archaeopteryx and other early feathered dinosaurs = stem birds. Why is this distinction vital for fossil evidence?",
        exAnswer: "Stem fossils preserve INTERMEDIATE stages between the broader clade's origin and the modern crown — their mosaic of ancestral + derived traits documents the assembly of modern body plans. Conflating crown and stem makes fossils look like 'misfits' (e.g., Archaeopteryx with bird wings + dinosaur teeth). The distinction lets paleontology and molecular phylogenetics agree on the origin TIMING of features (feathers ~150 MYA, beaks ~70 MYA) vs the origin of the modern crown (~70 MYA) — they're separate events.",
        ctx: "L15 §A — Reading phylogenetic trees"
      },
      {
        term: "Maximum parsimony",
        def: "Tree-building criterion: prefer the tree requiring the FEWEST evolutionary changes. Assumes evolution is rare — works when homoplasy is uncommon; fails for fast-evolving genes.",
        example: "Two trees: one needs 5 character changes, the other needs 8. Which does parsimony prefer? Why does parsimony underperform when long branches accumulate convergent changes?",
        exAnswer: "Parsimony picks the 5-change tree (fewest changes wins). But when long branches evolve fast, multiple changes per site become common; parsimony interprets convergent identical states as shared ancestry, ATTRACTING unrelated long branches together (LONG BRANCH ATTRACTION — a systematic error). Maximum likelihood and Bayesian methods that explicitly model rate variation across sites and branches handle this; parsimony does not. Use parsimony for slow-evolving morphological/genomic data; use likelihood for fast-evolving sites.",
        ctx: "L15 §A — Reading phylogenetic trees"
      }
    ],
    "L16": [
      {
        term: "Speciation modes (geographic)",
        def: "ALLOPATRIC: separated by barrier; most common in animals. PERIPATRIC: small founder pop isolated; drift + selection accelerate. PARAPATRIC: partial separation; gene flow ongoing. SYMPATRIC: same range; via niche shift, polyploidy (mostly plants).",
        example: "Squirrels split by Grand Canyon → Kaibab and Abert squirrels = allopatric. Apple maggot fly (Rhagoletis) shifted host from hawthorn to apple = sympatric. What environmental signature distinguishes peripatric from allopatric?",
        exAnswer: "ALLOPATRIC: large barrier divides population into two roughly equal halves; both maintain effective size; divergence by drift + diverging selection over many generations. PERIPATRIC: a SMALL founder group is isolated at the periphery — drift is much stronger (small Ne), novel selection regimes hit a small Ne, and trait changes can fix rapidly. SIGNATURE: rapid divergence + lower diversity in the peripheral population, often on islands or range edges (e.g., Hawaiian Drosophila).",
        ctx: "L16 §C — Speciation modes",
        mnem: "APPS: Allopatric · Peripatric · Parapatric · Sympatric (gene-flow level: 0 → 0 → some → full)."
      },
      {
        term: "Prezygotic isolation barriers (5)",
        def: "TEMPORAL (different breeding times), BEHAVIORAL (different courtship signals), MECHANICAL (incompatible genitalia/flowers), GAMETIC (sperm/pollen don't fertilize), HABITAT (don't meet because of niche).",
        example: "Two cricket species sing at different times of day = behavioral. Two mosquito species breed in different seasons = temporal. Why are prezygotic barriers more 'efficient' than postzygotic?",
        exAnswer: "Prezygotic barriers prevent reproduction from being ATTEMPTED — no gametes wasted, no inviable offspring produced, no parental care invested in doomed young. Postzygotic barriers (hybrid inviability/sterility/breakdown) waste all of those resources. Because waste is costly, selection FAVORS strengthening prezygotic isolation (REINFORCEMENT) wherever postzygotic isolation already exists. Result: in zones of secondary contact, prezygotic barriers tend to evolve fast.",
        ctx: "L16 §B — Reproductive isolation",
        mnem: "T-B-M-G-H: Temporal · Behavioral · Mechanical · Gametic · Habitat."
      },
      {
        term: "Postzygotic isolation barriers (3)",
        def: "HYBRID INVIABILITY (zygote/embryo fails). HYBRID STERILITY (mules — develops but can't reproduce). HYBRID BREAKDOWN (F1 fine but F2/backcross weak).",
        example: "Horse × donkey → mule (sterile, viable). Two cotton species → F1 fine, F2 collapses. Why is hybrid breakdown evidence of accumulated incompatibilities (Dobzhansky-Muller)?",
        exAnswer: "F1 hybrids are HETEROZYGOUS for both species' alleles → most incompatibilities are buffered (one functioning copy is enough). F2 segregation creates novel HOMOZYGOUS COMBINATIONS of alleles that were never co-tested in either parent species — and those combinations expose negative epistasis between independently-evolved alleles (alleles 'incompatible' because they evolved in different genetic backgrounds). Multiple loci → exponential exposure in F2; that's the Dobzhansky-Muller signature: F1 fine, F2 collapse.",
        ctx: "L16 §B — Reproductive isolation",
        mnem: "I-S-B: Inviable · Sterile · Breakdown."
      },
      {
        term: "Reinforcement",
        def: "When two diverged populations resume contact and produce unfit hybrids, selection favors STRONGER PREZYGOTIC isolation — barriers reinforce because hybrids waste reproductive effort.",
        example: "Pied/collared flycatchers in Europe show stronger song differences in zones of overlap than in pure-population zones — classic reinforcement signature. What does the prediction look like in pure vs sympatric zones?",
        exAnswer: "PURE-population zones (allopatric): prezygotic differences are at the 'background' level inherited from ancestral divergence — not strongly selected for distinctness. SYMPATRIC (overlap) zones: stronger prezygotic differences because hybrid offspring are unfit and selection favors stronger discrimination. The asymmetric pattern (greater divergence in sympatry than allopatry) is the diagnostic signature for ACTIVE reinforcement. Without postzygotic costs, no reinforcement happens.",
        ctx: "L16 §C — Speciation modes"
      },
      {
        term: "Sympatric speciation (when it actually works)",
        def: "Speciation in same geographic area, no barrier. Strong cases: POLYPLOIDY in plants (instant reproductive isolation via chromosome doubling). HOST RACES (Rhagoletis on apple vs hawthorn). Strong disruptive selection + assortative mating.",
        example: "Why is polyploidy nearly instant speciation in plants but rare/lethal in animals? (Animals' sex determination can't tolerate doubled chromosome sets.)",
        ctx: "L16 §C — Speciation modes"
      },
      {
        term: "Hybrid zone",
        def: "Geographic region where two species' ranges overlap and they interbreed. Hybrids typically have reduced fitness; zone may be stable (selection vs gene flow) or shift over time. Hybrid speciation (sunflowers) is a special case.",
        example: "European fire-bellied toad × yellow-bellied toad: narrow stable zone. What balances the zone? (Selection against hybrids vs continual gene flow from outside.)",
        ctx: "L16 §D — Hybrid zones"
      }
    ],
    "L17": [
      {
        term: "Dispersal vs vicariance",
        def: "DISPERSAL: organisms move across an existing barrier (lineage now in multiple regions). VICARIANCE: a NEW barrier (mountain rise, sea, continental drift) splits a continuous range. Molecular dating distinguishes.",
        example: "South American + African biotas share Gondwanan ancestry — vicariance from continental rifting (~120 MYA). Hawaiian birds arrived by dispersal across open ocean (no land bridge ever). Why does timing test these hypotheses?",
        exAnswer: "Vicariance PREDICTS splits matching the timing of the geological barrier (continental rift, mountain rise). Dispersal can occur at any time after a barrier exists. Molecular dating gives split times to test: if South American + African primate sister taxa split ~120 MYA when the Atlantic was opening → vicariance fits. If they split ~35 MYA (long after the Atlantic was wide open) → vicariance fails; dispersal (rafting, island hops) is required. The clock decides between hypotheses.",
        ctx: "L17 §B — Dispersal vs. vicariance",
        mnem: "Dispersal moves; Vicariance divides."
      },
      {
        term: "Adaptive radiation",
        def: "Rapid diversification of one lineage into many ecologically distinct species. Conditions: open niches + key innovation + ecological opportunity (post-extinction, new habitat).",
        example: "Galápagos finches: ~14 species from one founding ancestor, each a beak/diet specialist. Cichlid fish in African lakes: hundreds of species in <1 MYR. What 'opens niches' for radiations?",
        exAnswer: "Four classic openers: (1) MASS EXTINCTION clearing ecospace (mammals after K-Pg). (2) COLONIZING a new geographic area lacking competitors (Galápagos finches, Hawaiian honeycreepers). (3) KEY INNOVATION that opens new niches (jaws → vertebrate radiation; flight → bird/bat/insect radiations; flowers → angiosperm radiation; pharyngeal jaws → cichlid radiation). (4) GEOLOGICAL/CLIMATIC SHIFTS creating new habitats (cichlids in young Rift lakes; alpine plants after glaciation).",
        ctx: "L17 §E — Adaptive radiations"
      },
      {
        term: "Equilibrium island biogeography (MacArthur-Wilson)",
        def: "Standing species count = balance between IMMIGRATION (declines as island fills) and EXTINCTION (rises with more species). Equilibrium S* depends on island size (extinction) and distance from source (immigration).",
        example: "Predict: large island near mainland vs small island far away. Which has higher S*? (Large/near.) Why does the model predict TURNOVER even at equilibrium?",
        exAnswer: "Large-and-near has the highest S* (large = low extinction; near = high immigration; both push the curves favorably). Equilibrium is DYNAMIC, not static — at S*, the extinction rate EQUALS the immigration rate, so species are constantly being lost and replaced even though the total count is stable. Empirically confirmed by Simberloff & Wilson's mangrove fumigation experiments: same total species count returned within months, but different species assemblage years later.",
        ctx: "L17 §C — Standing diversity, turnover"
      },
      {
        term: "Wallace line — sharp biogeographic boundary",
        def: "An invisible line through Indonesia (between Bali/Lombok, Borneo/Sulawesi) that separates Asian biota (placental mammals, woodpeckers) from Australasian biota (marsupials, cockatoos). Dramatic faunal switch in <30 km — the cleanest land-based biogeographic boundary in the world.",
        example: "What geological feature explains why species don't cross the Wallace line, even though the islands are close together?",
        exAnswer: "Deep-water TRENCHES. The Lombok Strait is >250m deep and never closed during glacial low-sea-level periods. Bali (Asian) and Lombok (Australasian) sat on different continental shelves with deep water between them — animals could walk between Bali, Java, and Borneo across exposed seabed at glacial maxima, but never crossed to Lombok. Geographic isolation by deep water enforced the faunal split for tens of millions of years.",
        ctx: "L17 §A — What is biogeography?",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "wallace-line"
      },
      {
        term: "Hawaiian Drosophila — peripatric explosion",
        def: "~1,000 endemic Hawaiian Drosophila species (>25% of world's Drosophila diversity) in a chain <2,000 km long. All descend from a single colonizer ~25 MYA. Each new island colonized by a few founders → drift + new selection → rapid speciation. Textbook peripatric radiation.",
        example: "Why are Hawaiian Drosophila phylogenetically nested in island age order (older islands carry older species)?",
        exAnswer: "Each new volcanic island emerges from the hotspot fresh and unpopulated; it's colonized by a handful of flies from the adjacent older island. That FOUNDER population then radiates independently. Phylogenies show 'island progression': flies on the youngest island (Hawai'i Big Island) are nested inside flies from Maui; Maui flies are nested inside O'ahu, and so on. Each peripatric founder event is a step in the phylogeny.",
        ctx: "L17 §E — Adaptive radiations",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "hawaiian-drosophila"
      },
      {
        term: "Latitudinal diversity gradient",
        def: "Species richness peaks at the tropics and declines toward the poles for nearly every taxonomic group. Hypotheses: (1) more solar energy → more productivity → more niches; (2) longer time since glaciation → more accumulated diversity; (3) climate stability → more specialization possible.",
        example: "Why is the latitudinal diversity gradient considered 'one of biology's oldest unsolved problems'?",
        exAnswer: "Multiple hypotheses (energy, time, stability, area) all PREDICT the same gradient, so the pattern alone can't distinguish among them. Each is partially supported by some taxa or systems and contradicted by others. No single mechanism cleanly explains both terrestrial AND marine gradients, both vertebrates AND insects. Likely a combination of factors with weighting that varies by clade — but consensus on the weights remains elusive after 150+ years.",
        ctx: "L17 §C — Standing diversity, turnover",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "latitudinal-gradient"
      },
      {
        term: "Continental drift — biogeographic evidence",
        def: "Species distributions match Pangaean breakup timing. Marsupials in Australia/S.America (split via Antarctica ~50 MYA). Lungfish in S.America/Africa/Australia (Gondwanan). Glossopteris fossils (a Permian seed fern) on every Gondwanan continent. Phylogenies AND geology AND paleomagnetism converge.",
        example: "Why is glossopteris distribution stronger evidence for continental drift than marsupial distribution alone?",
        exAnswer: "Glossopteris is a SEED PLANT — its seeds couldn't disperse across modern oceans, ruling out 'rare dispersal' as an explanation. Its fossils on South America, Africa, India, Australia, and Antarctica require those landmasses to have been connected when it lived (Permian, ~280 MYA). Marsupials could conceivably have rafted; seed ferns couldn't have. The plant evidence forced 19th-century geologists to reckon with drifting continents.",
        ctx: "L17 §B — Dispersal vs. vicariance",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "drift-evidence"
      }
    ],
    "L18": [
      {
        term: "Fisheries-induced evolution — size selection",
        def: "Size-limit fishing rules ('keep only fish >X cm') consistently REMOVE LARGE INDIVIDUALS. Result: heritable size at maturity decreases over generations. Fish mature earlier and smaller. Atlantic cod, sole, and many commercial species show measurable shrinkage over 30-40 years.",
        example: "A fishery sets a 50-cm minimum size. Why does this seemingly 'protective' rule actually drive small-size evolution?",
        exAnswer: "It's STRONG DIRECTIONAL SELECTION against large body size and late maturity. Fish that mature small and reproduce BEFORE reaching 50 cm escape the net entirely; fish that grow large and mature late are caught before reproducing. Heritable size-at-maturity drops within ~10–20 generations. The rule is well-intentioned but selects on the wrong trait. Better: total quotas + slot limits (protect both small AND large fish).",
        ctx: "L18 §A — Humans as selective force",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "fisheries-evolution"
      },
      {
        term: "Bighorn sheep trophy hunting → smaller horns",
        def: "Trophy hunters select for the largest-horned rams. Over 30 years on Ram Mountain, Alberta, mean horn size declined ~25% — heritability of horn size ~0.7. Body size and age at first reproduction also shifted as correlated traits.",
        example: "What's the evolutionary irony of trophy hunting management?",
        exAnswer: "By selecting only the largest-horned rams (often the prime-age breeders), trophy hunting REMOVES the very phenotype it values. Large horns are heritable, so each generation's gene pool shifts toward smaller. Hunters then complain about declining trophy quality without recognizing they're causing it. Compare natural-selection ornament evolution: peacock tails grew because females PREFERRED large; here, hunters prefer large but kill rather than mate, so the direction reverses.",
        ctx: "L18 §A — Humans as selective force",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "trophy-hunting"
      },
      {
        term: "Florida panther genetic rescue",
        def: "By 1990s, the Florida panther was reduced to ~30 individuals. Severe inbreeding caused heart defects, undescended testicles, sperm abnormalities. In 1995, 8 Texas pumas were introduced — genetic rescue. Within 2 generations, defects dropped, kitten survival rose, population grew to ~200.",
        example: "Why is genetic rescue controversial despite the Florida panther success?",
        exAnswer: "Two concerns: (1) OUTBREEDING DEPRESSION — introduced individuals may carry alleles incompatible with locally-adapted ones, causing F1 hybrid problems. (2) LOSS OF GENETIC IDENTITY — introducing a closely-related subspecies dilutes the original population's distinctness, blurring conservation units. Florida worked because the Texas puma was the historic gene-flow source, but other rescues need careful donor selection.",
        ctx: "L18 §B — Habitat fragmentation, conservation genetics",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "genetic-rescue"
      },
      {
        term: "Inbreeding depression mechanism",
        def: "Mating between close relatives raises homozygosity. Recessive deleterious alleles (normally hidden in heterozygotes) become exposed → reduced fitness. Severity depends on genetic load (mutation accumulation) and how many recessives the population carries.",
        example: "Why does inbreeding hurt small populations more than large ones — and what counterintuitive long-term outcome can it produce?",
        exAnswer: "Small pops have less standing variation, so close-relative mating is more likely. Inbreeding exposes recessives → low fitness. COUNTERINTUITIVELY, sustained extreme inbreeding can PURGE deleterious recessives over generations (every aa homozygote that dies removes 2 a alleles from the gene pool). Surviving lineages emerge 'inbred but cleaned' — explains why some self-fertilizing plant species or eusocial Hymenoptera tolerate high homozygosity.",
        ctx: "L18 §B — Habitat fragmentation, conservation genetics",
        cardType: "discriminator",
        sourceType: "studyguide",
        conceptId: "inbreeding-depression"
      },
      {
        term: "Climate change → range shifts and phenological mismatch",
        def: "Many species track climate by shifting ranges poleward and upslope. PHENOLOGY (timing of seasonal events: flowering, migration, breeding) also shifts. Mismatches occur when interacting species track climate at DIFFERENT rates — pollinator emerges before flower blooms, predator misses prey peak.",
        example: "European Pied flycatchers migrate from Africa on photoperiod cues but their caterpillar prey peak earlier each year due to warmer European springs. Predict the effect on flycatcher fitness.",
        exAnswer: "REDUCED FITNESS from a mismatch the birds can't easily fix. Photoperiod is FIXED (day length doesn't shift with climate), so flycatchers arrive on schedule — but caterpillar peak is now WEEKS earlier and gone before chick-feeding. Result: fewer chicks fledged, population decline. Some flycatcher populations are evolving earlier arrival, but at much slower rates than the climate is shifting. Phenological mismatch is a major modern extinction-risk mechanism.",
        ctx: "L18 §C — Climate change as selective pressure",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "phenological-mismatch"
      },
      {
        term: "Captive breeding + reintroduction (California condor)",
        def: "By April 1987 only 22 California condors remained in the wild — ALL were captured (controversial), joining ~5 already in captivity for a total breeding population of 27. Through careful pedigree management (each bird's lineage tracked) to minimize inbreeding, the population rebuilt. Reintroduced from 1992; ~500 alive today, ~half wild.",
        example: "Why is the California condor case both a conservation success and a cautionary tale?",
        exAnswer: "SUCCESS: extinction averted; population recovered ~25-fold; reintroduction works. CAUTION: condors die from LEAD POISONING (eating bullet-shot carcasses) and trash ingestion. The original threat (lead) wasn't fully solved; reintroduced condors require ongoing veterinary chelation therapy + supplemental feeding. Without addressing the underlying anthropogenic cause, reintroduction is just expensive maintenance, not recovery. Also: severe genetic bottleneck (founders < 30) → reduced variation, future inbreeding risk.",
        ctx: "L18 §D — Conservation strategies",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "captive-breeding"
      }
    ],
    "L19": [
      {
        term: "Hominin bipedality timing",
        def: "Bipedalism predates large brains by millions of years. Sahelanthropus (~7 MYA) and Ardipithecus (~4.4 MYA) show foramen magnum forward, pelvic & lower-limb adaptations for upright walking — large brains evolved much later in Homo (~2 MYA).",
        example: "Why is the order 'bipedal first, big brain later' surprising relative to popular reconstructions? What does it imply about selective pressures driving each?",
        exAnswer: "SURPRISING because pop-culture reconstructions imply intelligence came first ('we got smart, THEN we stood up'). The fossil order is REVERSED: ~7 MYA bipedal Sahelanthropus with chimp-sized brain. IMPLIES bipedality wasn't selected for tool-use or to support a heavy head — likely thermoregulation (less surface area to direct sun), energy efficiency over long walking distances, or freed hands for carrying food/infants. Brain expansion came ~5 MYA later, riding on different selective pressures (tools, social cognition, dietary shifts).",
        ctx: "L19 — Human evolution"
      },
      {
        term: "Australopithecus afarensis (Lucy) — anatomy",
        def: "~3.9–2.9 MYA, eastern Africa. Adult brain ~400 cc (chimp-sized). Bipedal pelvis, valgus knee, longitudinal foot arch — fully bipedal on the ground. BUT retained curved fingers, long arms, and a divergent toe — still capable in trees. Mosaic anatomy.",
        example: "What does Lucy's mosaic of bipedal + arboreal traits tell us about the early hominin lifestyle?",
        exAnswer: "Bipedal but NOT obligate ground-dweller. Lucy walked on the ground (efficient bipedalism) but slept in trees and could climb fluently. Mosaic anatomy resists 'pure' interpretations: bipedalism evolved for energy-efficient walking + freed hands, but the arboreal traits weren't yet abandoned. Selection acted on the COMBINATION because trees were still a refuge from predators on the open savanna. Full ground commitment came later (Homo erectus).",
        ctx: "L19 §B — Australopithecines",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "lucy-anatomy"
      },
      {
        term: "Out-of-Africa + Neanderthal introgression",
        def: "Modern Homo sapiens originated in Africa ~300 KYA. Major out-of-Africa wave ~70 KYA met Neanderthals in the Middle East/Europe. Interbreeding ~50–60 KYA left ~1–4% Neanderthal DNA in all NON-AFRICAN modern humans. African populations have ~0% Neanderthal DNA (the ancestors never met them).",
        example: "Why is the absence of Neanderthal DNA in sub-Saharan Africans strong evidence FOR the Out-of-Africa model?",
        exAnswer: "Out-of-Africa predicts: (1) modern humans originated in Africa, (2) only those who LEFT met Neanderthals, (3) interbreeding happened OUTSIDE Africa, (4) the ancestral population that stayed in Africa never gained Neanderthal alleles. The observed pattern (Neanderthal DNA in non-Africans, ~0% in Africans) matches all four. A multiregional model would predict mixing throughout the species' range — wrong. (Note: very recent back-migration to Africa has introduced trace Neanderthal DNA to some African populations, but the gradient is dramatic.)",
        ctx: "L19 §C — Out-of-Africa, Neanderthal/Denisovan",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "out-of-africa"
      },
      {
        term: "EPAS1 — Tibetan high-altitude adaptation via Denisovan introgression",
        def: "Tibetans tolerate high altitude (low O₂) because they have a variant EPAS1 gene that doesn't trigger pathological hemoglobin overproduction at altitude. This protective allele was acquired by INTROGRESSION from Denisovans during interbreeding ~30–50 KYA, then strongly selected in Tibetan populations.",
        example: "Why is the EPAS1 case considered the 'cleanest example' of adaptive introgression in modern humans?",
        exAnswer: "Three lines of evidence converge cleanly: (1) the Tibetan EPAS1 haplotype is much more divergent from other modern humans than expected — indicating an external origin. (2) The same haplotype is found in the Denisovan genome from Siberia. (3) The frequency in Tibetans (~87%) is FAR higher than in neighboring populations, indicating strong recent positive selection. Hybrid origin + selection signature + functional benefit at altitude = textbook adaptive introgression.",
        ctx: "L19 §C — Out-of-Africa, Neanderthal/Denisovan",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "epas1-introgression"
      },
      {
        term: "Homo habilis — first stone tools (Oldowan)",
        def: "~2.5–1.5 MYA. Brain ~600 cc (50% larger than Australopithecus). Associated with Oldowan tools — simple stone flakes for cutting flesh from carcasses. The lithic tradition is the diagnostic feature defining the genus Homo.",
        example: "Why do paleoanthropologists treat the Oldowan toolkit as evolutionarily significant despite its 'crude' appearance?",
        exAnswer: "Because it represents the first stable cultural/cumulative tradition in the hominin lineage. (1) STANDARDIZED design across regions — not random rock-bashing. (2) Selection of suitable raw material (specific stone types). (3) Persistent transmission across generations — implying social learning/teaching. (4) CONSEQUENCES: cut-marks on bones show new dietary niches (scavenging meat). The Oldowan opened a feedback loop: tools → meat → larger brains → better tools. Crude in form, profound in evolutionary signal.",
        ctx: "L19 §B — Australopithecines and early Homo",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "oldowan-tools"
      }
    ],
    "L20": [
      {
        term: "Antibiotic resistance — evolution by selection",
        def: "Resistant variants pre-exist in populations at low frequency (mutation). Antibiotic use selects them; sensitive cells die. Stop-and-start dosing leaves survivors that proliferate; full courses minimize survivors. Resistance genes spread by horizontal transfer.",
        example: "Why does 'finishing the antibiotic course' have an evolutionary rationale? (Eliminates partially-resistant survivors before they can multiply.)",
        ctx: "L20 §A — Drug resistance evolution"
      },
      {
        term: "Virulence-transmission trade-off (Ewald)",
        def: "Pathogen virulence (host damage) trades off against transmission. High virulence kills the host fast → may limit spread. Low virulence keeps host alive → more chances to transmit. Optimum depends on TRANSMISSION MODE: respiratory/STI pathogens need mobile hosts (low virulence favored); vector-borne or waterborne don't (high virulence tolerated).",
        example: "Ewald predicted that improving water sanitation would select for LOWER virulence in diarrheal pathogens like cholera. Why?",
        exAnswer: "Cholera transmits via contaminated water (host doesn't need to be mobile to spread). High virulence = high cholera-toxin output → severe diarrhea → more pathogen excreted into water → more transmission. SANITATION breaks the contaminated-water loop. Now pathogens need a mobile host to find new water sources, so high-virulence strains (host bedridden) lose; lower-virulence strains win. Ewald's prediction was confirmed: V. cholerae in better-sanitation regions evolves toward less-virulent strains.",
        ctx: "L20 §C — Virulence and transmission mode",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "virulence-tradeoff"
      },
      {
        term: "MHC and balancing selection",
        def: "Major Histocompatibility Complex (MHC) genes encode antigen-presenting receptors. They're the most polymorphic genes in vertebrates — hundreds of alleles per locus. Maintained by BALANCING selection: heterozygotes present a wider range of pathogen peptides than homozygotes (heterozygote advantage) AND rare alleles are favored when common ones evolve into being recognized by pathogens (negative frequency-dependent selection).",
        example: "Why are MHC alleles MORE polymorphic in vertebrate populations than the genome average?",
        exAnswer: "Two flavors of balancing selection compound. (1) HETEROZYGOTE ADVANTAGE: an Aa heterozygote presents both A's peptide repertoire AND a's, expanding pathogen recognition. (2) NEGATIVE FREQUENCY-DEPENDENT: as a common allele's peptide-binding profile gets 'figured out' by parasites that evolve to evade it, rare alleles regain advantage — keeping all alleles rotating. Result: alleles persist for tens of millions of years (trans-species polymorphism), and humans share some MHC alleles with chimps.",
        ctx: "L20 §D — Host-pathogen coevolution",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "mhc-balancing"
      },
      {
        term: "Sickle-cell heterozygote advantage (HbA/HbS) vs malaria",
        def: "HbS homozygotes have severe sickle-cell anemia (fitness ↓). HbA homozygotes are vulnerable to severe malaria. HbA/HbS HETEROZYGOTES are RESISTANT to severe malaria with mild symptoms only — highest fitness in malaria-endemic regions. Stable polymorphism maintained by selection.",
        example: "Why does HbS persist at ~5–15% in malaria-endemic regions but is rare elsewhere?",
        exAnswer: "Classic balancing selection (heterozygote advantage). In malaria-endemic regions, the heterozygote is the fittest genotype (resistance with mild anemia). HWE breaks: at equilibrium, allele frequency q* = (s_AA-AA)/(s_AA-AA + s_SS-SS) ≈ 0.10. Wherever malaria pressure is absent (Europe, North America), HbS provides no benefit and the s_SS cost selects it OUT. Population-genetics models predict the geographic gradient observed in real frequency data.",
        ctx: "L20 §D — Host-pathogen coevolution",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "sickle-cell-malaria"
      },
      {
        term: "Cancer as somatic evolution + adaptive therapy",
        def: "Tumor cells are subject to mutation + selection like any population — heritable variation among clones, differential growth rates, resource competition. Standard chemo selects HARDEST against susceptible clones, leaving resistant subclones to dominate → relapse. ADAPTIVE THERAPY: maintain susceptibles at sub-lethal doses to suppress resistant clones via competition.",
        example: "Why does 'maximum tolerated dose' chemotherapy often fail in late-stage cancers, and how does adaptive therapy reframe the goal?",
        exAnswer: "Maximum-dose chemo creates the strongest possible selection FOR resistance — kill the susceptibles entirely → resistant clones face no competition → expand fast → relapse. ADAPTIVE THERAPY uses the susceptibles as biological competitors: modest doses keep them alive enough to crowd out the resistant clones (ecological control). Goal shifts from 'cure by elimination' to 'control by competition.' Trials show prolonged stable disease in some metastatic cancers (e.g., prostate). It's evolutionary medicine applied to oncology.",
        ctx: "L20 §F — Cancer as somatic evolution",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "adaptive-therapy"
      },
      {
        term: "Hygiene hypothesis",
        def: "Modern environments lack the diverse microbial exposure of ancestral conditions. Without childhood exposure to a normal microbe load, the immune system 'mis-trains' — over-reacting to harmless allergens (asthma, hay fever) or self (autoimmunity, T1D, Crohn's). Mismatch between evolved immune development and modern hygiene.",
        example: "Why are children raised on farms or with multiple older siblings less likely to develop asthma than only-children in sterile suburbs?",
        exAnswer: "Both farm exposure and older siblings DELIVER MORE MICROBIAL DIVERSITY to the developing immune system: farm dust, animal microbes, sibling-vectored infections. The immune system's regulatory arm (Treg cells, Th1/Th2 balance) needs early diverse exposure to calibrate properly. Without it, the response defaults to over-active Th2 (allergic/atopic). Confirmed in epidemiological cohorts and Amish vs Hutterite comparison: same European ancestry, different microbial environments → vastly different asthma rates.",
        ctx: "L20 §E — Mismatch hypothesis",
        cardType: "application",
        sourceType: "studyguide",
        conceptId: "hygiene-hypothesis"
      }
    ]
  };

  // Merge into the existing decks (FLASHCARD_DECKS already loaded by flashcards.js)
  if (!window.FLASHCARD_DECKS) {
    console.warn('[flashcards-extra] FLASHCARD_DECKS not present — loading flashcards.js first is required.');
    return;
  }
  let added = 0;
  Object.entries(EXTRA).forEach(([deckId, cards]) => {
    if (!Array.isArray(window.FLASHCARD_DECKS[deckId])) {
      window.FLASHCARD_DECKS[deckId] = [];
    }
    cards.forEach(c => {
      window.FLASHCARD_DECKS[deckId].push(c);
      added++;
    });
  });
  // Also add into the 'all' deck if it exists
  if (Array.isArray(window.FLASHCARD_DECKS.all)) {
    Object.values(EXTRA).forEach(cards => {
      cards.forEach(c => window.FLASHCARD_DECKS.all.push(c));
    });
  }
  console.log('[flashcards-extra] +' + added + ' gap-filling cards merged into decks.');

  // === PATCHES MERGE ===
  // Apply window.FLASHCARD_PATCHES (filled by _patches_g*.js files) to existing cards.
  // Schema: window.FLASHCARD_PATCHES = { L01: { "Term name": { exAnswer, mnem, analogy } } }
  // Patches only fill EMPTY fields (won't overwrite existing exAnswer / mnem).
  function applyPatches() {
    const patches = window.FLASHCARD_PATCHES;
    if (!patches) return;
    const stripTerm = (t) => (t || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();

    const flatLookup = {};
    Object.entries(patches).forEach(([lectureId, byTerm]) => {
      if (!byTerm || typeof byTerm !== 'object') return;
      Object.entries(byTerm).forEach(([term, patch]) => {
        const k = stripTerm(term);
        if (!flatLookup[k]) flatLookup[k] = [];
        flatLookup[k].push({ lectureId, patch });
      });
    });

    let patchedFields = 0;
    const applyOne = (card, patch) => {
      if (!card || !patch) return;
      if (patch.exAnswer && !card.exAnswer) { card.exAnswer = patch.exAnswer; patchedFields++; }
      if (patch.mnem && !card.mnem && !card.mnemonic) { card.mnem = patch.mnem; patchedFields++; }
      if (patch.analogy && !card.analogy && !card.mnem && !card.mnemonic) { card.analogy = patch.analogy; patchedFields++; }
      if (patch.importance && !card.importance) { card.importance = patch.importance; patchedFields++; }
      if (patch.images && !card.images) { card.images = patch.images; patchedFields++; }
    };

    Object.entries(patches).forEach(([lectureId, byTerm]) => {
      const deck = window.FLASHCARD_DECKS[lectureId];
      if (!Array.isArray(deck) || !byTerm) return;
      const termMap = {};
      Object.entries(byTerm).forEach(([term, patch]) => { termMap[stripTerm(term)] = patch; });
      deck.forEach(card => {
        const patch = termMap[stripTerm(card.term)];
        if (patch) applyOne(card, patch);
      });
    });

    const allDeck = window.FLASHCARD_DECKS.all;
    if (Array.isArray(allDeck)) {
      allDeck.forEach(card => {
        const k = stripTerm(card.term);
        const candidates = flatLookup[k];
        if (!candidates) return;
        const ctxPrefix = (card.ctx || '').match(/^(L\d+)/);
        const lectureId = ctxPrefix ? ctxPrefix[1] : null;
        const match = candidates.find(c => c.lectureId === lectureId) || candidates[0];
        applyOne(card, match.patch);
      });
    }

    console.log('[flashcards-patches] applied ' + patchedFields + ' field(s) across decks.');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyPatches);
  } else {
    Promise.resolve().then(applyPatches);
  }
})();
