/* Gap-filling cards keyed off the cheatsheet (L01-L20).
   Heavy on the user-flagged topics: Hardy-Weinberg math, selection types,
   game theory, speciation modes, phylogenetic groupings, Hox / dev.
   Each card may include a `mnem` field that the new view renders in a
   separate gold-bordered subsection. */
(function () {
  const EXTRA = {
    "L02": [
      {
        term: "Darwin's three observations + one inference",
        def: "OBS 1: Heritable variation exists. OBS 2: More offspring produced than survive. OBS 3: Survival/reproduction is non-random. INFERENCE: Heritable variants that raise reproduction become more common — natural selection.",
        example: "Asked on an exam to 'list the logical structure of natural selection,' you must give 3 observations and 1 inference. What would a missing piece (e.g., no heritable variation) do to the argument?",
        ctx: "L02 §D — Darwin, Wallace, natural selection",
        mnem: "VOS→S: Variation · Overproduction · Survival differs → Selection."
      },
      {
        term: "Falsifiability (Popper)",
        def: "A scientific claim must specify observations that would prove it wrong. Evolution is falsifiable; e.g., a Cambrian rabbit fossil would shatter the tree.",
        example: "An exam asks why 'all living things were created perfectly' is not a scientific claim. Frame the answer in falsifiability terms.",
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
        ctx: "L04 §C — Detecting deviations",
        mnem: "X-male = q · X-female = q² (males get the rare allele cheap)."
      },
      {
        term: "Wahlund effect",
        def: "Pooling two subpopulations with different allele frequencies produces APPARENT excess of homozygotes vs HWE expectation, even if each subpop is in HWE internally.",
        example: "Subpop A: p=0.9. Subpop B: p=0.1. Pooled p=0.5 → expected 2pq=0.5. Observed heterozygotes ≈ 0.18. Excess homozygotes — but no inbreeding inside either subpop. Diagnosis?",
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
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Directional → Distribution Drifts (mean moves)."
      },
      {
        term: "Stabilizing selection",
        def: "Favors the mean / intermediate phenotype; extremes selected against; mean unchanged but variance shrinks.",
        example: "Human birth weight: very small AND very large babies have higher mortality. Mean stays at ~3.5 kg. What happens to variance under sustained stabilizing selection?",
        ctx: "L05 §C — Selection on quantitative traits",
        mnem: "Stabilizing → Squashes the distribution (variance ↓)."
      },
      {
        term: "Disruptive selection",
        def: "Favors BOTH extremes; intermediates selected against; variance increases; can produce bimodal distribution and seed sympatric divergence.",
        example: "African finch with bimodal beak distribution — small beaks crack soft seeds, large beaks crack hard seeds. Intermediates are bad at both. What long-term outcome may this lead to?",
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
        ctx: "L05 §D — Phenotypic plasticity, reaction norms"
      }
    ],
    "L08": [
      {
        term: "Stepwise eye evolution stages",
        def: "(1) Light-sensitive patch (photoreceptors). (2) Cupped patch — directional sensitivity. (3) Pinhole eye (Nautilus) — image without lens. (4) Lensed eye — sharp focus via co-opted crystallins.",
        example: "Each stage must be functional — selection cannot 'plan' a future eye. Eyes have evolved >40 times independently. What does this convergence imply about complexity?",
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
        ctx: "L08 §D — Heterochrony",
        mnem: "Paedo = Pediatric (juvenile features kept) · Pera = Past (development extended)."
      },
      {
        term: "Hox genes — A-P body axis",
        def: "Cluster of TFs that pattern the anterior-posterior axis of bilaterians. Colinearity: chromosomal order matches body-axis expression order.",
        example: "Vertebrates have 4 Hox clusters (HoxA, B, C, D) from two whole-genome duplications. Flies have 1 cluster. What body-plan transitions correlate with cluster duplications?",
        ctx: "L08 §E — Hox genes and conserved networks",
        mnem: "Hox = Head-to-tail patterning (linear order on chromosome = linear order on body)."
      },
      {
        term: "Cis-regulatory mutations vs structural",
        def: "Cis = changes WHEN/WHERE a gene is expressed (enhancer/promoter); structural = changes the protein itself. Cis is the leading edge of body-plan evolution because it's modular and tissue-specific.",
        example: "Stickleback fish lost pelvic spines via repeated cis-regulatory loss in the Pitx1 gene. The protein still works in teeth and elsewhere. Why is cis-regulatory evolution favored over structural change in pleiotropic genes?",
        ctx: "L08 §C — Regulatory networks"
      },
      {
        term: "Vestigial structure (definition + examples)",
        def: "An ancestral structure with reduced or no current function. Whale pelvis, human appendix, snake hind-limb buds, ostrich wings, blind cave-fish eyes.",
        example: "Why isn't the human appendix 'evidence against evolution'? What does it positively support?",
        ctx: "L08 §F — Imperfect adaptation"
      }
    ],
    "L09": [
      {
        term: "Coevolution vs coexistence",
        def: "Coevolution = RECIPROCAL evolutionary change in interacting lineages. Coexistence ≠ coevolution; both species could be in their own equilibria without reciprocal pressure.",
        example: "Two species have lived in the same forest for a million years and look co-adapted. What evidence would show coevolution rather than mere coexistence?",
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
        ctx: "L09 §D — Mimicry",
        mnem: "Bates = Bluff (one liar) · Müller = Mutual (both honest)."
      },
      {
        term: "Geographic Mosaic Theory of Coevolution (Thompson)",
        def: "Coevolution intensity varies across the range — HOTSPOTS (intense reciprocal selection) + COLDSPOTS (weak/none). Gene flow + local trait evolution → mosaic of coevolutionary states; mismatch is positive evidence of dynamic process.",
        example: "Crossbill bird beaks match local pine cone shapes in some valleys but not others. Trait MISMATCH is consistent with the Mosaic Theory rather than refuting coevolution. Why?",
        ctx: "L09 §E — Geographic Mosaic Theory"
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
        ctx: "L11 §C — Sexual selection",
        mnem: "Intra = Inside-the-sex contest · Inter = Inter-sex choice."
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
        ctx: "L12 §B — Extrinsic mortality"
      },
      {
        term: "r vs K selection",
        def: "r-selected: high reproductive rate, many small offspring, little parental care, short life — favored in unstable/empty environments. K-selected: low rate, few large offspring, parental care, long life — favored in saturated, competitive environments.",
        example: "Mice, weeds, and most insects → r. Elephants, oaks, humans → K. What predicts where on the r-K continuum a species sits? (Density and stability of resources.)",
        ctx: "L12 §D — Age at maturity, offspring size",
        mnem: "r = Rapid (many small) · K = Carrying-capacity (few big)."
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
        ctx: "L13 §D — Side-blotched lizards (rock-paper-scissors)",
        mnem: "O→B→Y→O: Orange beats Blue beats Yellow beats Orange."
      },
      {
        term: "Direct vs indirect reciprocity",
        def: "DIRECT: tit-for-tat between two individuals; needs repeated encounters & memory. INDIRECT: reputation-based; helping earns help from third parties; needs visibility/communication.",
        example: "Vampire bats regurgitate blood to non-relatives — direct reciprocity, well-documented. Why does indirect reciprocity scale better in large groups?",
        ctx: "L13 §E — Cooperation among non-kin"
      },
      {
        term: "Group selection — why naive version fails",
        def: "Within a group, individual cheaters have HIGHER fitness than altruistic group-helpers; cheating spreads, cooperation collapses — even if altruistic groups outproduce selfish groups, within-group selection wins on faster timescale.",
        example: "Modern view accepts multilevel selection in narrow conditions (frequent extinction, strict subdivision), but mostly explains 'group benefits' via individual or kin selection. Why is haystack-mouse selection a textbook valid case?",
        ctx: "L13 §A — Individual vs group selection"
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
        ctx: "L14 §D — Mass extinctions",
        mnem: "OD-PTC: Ordovician · Devonian · Permian · Triassic · Cretaceous (in time order)."
      },
      {
        term: "Radiometric dating logic",
        def: "Parent isotope decays to daughter at known half-life. Age = ln(1+D/P)/λ where D/P = daughter/parent ratio, λ = decay constant. Different isotope systems for different timescales.",
        example: "¹⁴C: ~5,730 yr half-life — useful to ~50 KYR. K-Ar: 1.25 GYR half-life — millions to billions. U-Pb: zircons date Earth at 4.4 GYA. Why can't ¹⁴C date a dinosaur fossil?",
        ctx: "L14 §A — Earth's age, dating methods"
      }
    ],
    "L15": [
      {
        term: "Reading a phylogenetic tree — closeness rule",
        def: "Closeness of relationship is determined by RECENCY OF COMMON ANCESTOR (depth of shared node), NOT by horizontal distance on the page. Trees can be rotated at any node without changing relationships.",
        example: "On a tree of (mouse, (human, chimp)), human and chimp are more closely related to each other than either is to mouse — even if mouse is drawn 'right next to' human. Why is rotation allowed?",
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
        ctx: "L15 §B — Synapomorphy / symplesiomorphy / homoplasy"
      },
      {
        term: "Crown group vs stem group",
        def: "CROWN group = all descendants of the most recent common ancestor of all LIVING members of a clade. STEM group = extinct lineages that branched off before the crown but are part of the broader clade (e.g., 'feathered theropods are stem-birds').",
        example: "All living birds + their MRCA + descendants = crown Aves. Archaeopteryx and other early feathered dinosaurs = stem birds. Why is this distinction vital for fossil evidence?",
        ctx: "L15 §A — Reading phylogenetic trees"
      },
      {
        term: "Maximum parsimony",
        def: "Tree-building criterion: prefer the tree requiring the FEWEST evolutionary changes. Assumes evolution is rare — works when homoplasy is uncommon; fails for fast-evolving genes.",
        example: "Two trees: one needs 5 character changes, the other needs 8. Which does parsimony prefer? Why does parsimony underperform when long branches accumulate convergent changes?",
        ctx: "L15 §A — Reading phylogenetic trees"
      }
    ],
    "L16": [
      {
        term: "Speciation modes (geographic)",
        def: "ALLOPATRIC: separated by barrier; most common in animals. PERIPATRIC: small founder pop isolated; drift + selection accelerate. PARAPATRIC: partial separation; gene flow ongoing. SYMPATRIC: same range; via niche shift, polyploidy (mostly plants).",
        example: "Squirrels split by Grand Canyon → Kaibab and Abert squirrels = allopatric. Apple maggot fly (Rhagoletis) shifted host from hawthorn to apple = sympatric. What environmental signature distinguishes peripatric from allopatric?",
        ctx: "L16 §C — Speciation modes",
        mnem: "APPS: Allopatric · Peripatric · Parapatric · Sympatric (gene-flow level: 0 → 0 → some → full)."
      },
      {
        term: "Prezygotic isolation barriers (5)",
        def: "TEMPORAL (different breeding times), BEHAVIORAL (different courtship signals), MECHANICAL (incompatible genitalia/flowers), GAMETIC (sperm/pollen don't fertilize), HABITAT (don't meet because of niche).",
        example: "Two cricket species sing at different times of day = behavioral. Two mosquito species breed in different seasons = temporal. Why are prezygotic barriers more 'efficient' than postzygotic?",
        ctx: "L16 §B — Reproductive isolation",
        mnem: "T-B-M-G-H: Temporal · Behavioral · Mechanical · Gametic · Habitat."
      },
      {
        term: "Postzygotic isolation barriers (3)",
        def: "HYBRID INVIABILITY (zygote/embryo fails). HYBRID STERILITY (mules — develops but can't reproduce). HYBRID BREAKDOWN (F1 fine but F2/backcross weak).",
        example: "Horse × donkey → mule (sterile, viable). Two cotton species → F1 fine, F2 collapses. Why is hybrid breakdown evidence of accumulated incompatibilities (Dobzhansky-Muller)?",
        ctx: "L16 §B — Reproductive isolation",
        mnem: "I-S-B: Inviable · Sterile · Breakdown."
      },
      {
        term: "Reinforcement",
        def: "When two diverged populations resume contact and produce unfit hybrids, selection favors STRONGER PREZYGOTIC isolation — barriers reinforce because hybrids waste reproductive effort.",
        example: "Pied/collared flycatchers in Europe show stronger song differences in zones of overlap than in pure-population zones — classic reinforcement signature. What does the prediction look like in pure vs sympatric zones?",
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
        ctx: "L17 §B — Dispersal vs. vicariance",
        mnem: "Dispersal moves; Vicariance divides."
      },
      {
        term: "Adaptive radiation",
        def: "Rapid diversification of one lineage into many ecologically distinct species. Conditions: open niches + key innovation + ecological opportunity (post-extinction, new habitat).",
        example: "Galápagos finches: ~14 species from one founding ancestor, each a beak/diet specialist. Cichlid fish in African lakes: hundreds of species in <1 MYR. What 'opens niches' for radiations?",
        ctx: "L17 §E — Adaptive radiations"
      },
      {
        term: "Equilibrium island biogeography (MacArthur-Wilson)",
        def: "Standing species count = balance between IMMIGRATION (declines as island fills) and EXTINCTION (rises with more species). Equilibrium S* depends on island size (extinction) and distance from source (immigration).",
        example: "Predict: large island near mainland vs small island far away. Which has higher S*? (Large/near.) Why does the model predict TURNOVER even at equilibrium?",
        ctx: "L17 §C — Standing diversity, turnover"
      }
    ],
    "L19": [
      {
        term: "Hominin bipedality timing",
        def: "Bipedalism predates large brains by millions of years. Sahelanthropus (~7 MYA) and Ardipithecus (~4.4 MYA) show foramen magnum forward, pelvic & lower-limb adaptations for upright walking — large brains evolved much later in Homo (~2 MYA).",
        example: "Why is the order 'bipedal first, big brain later' surprising relative to popular reconstructions? What does it imply about selective pressures driving each?",
        ctx: "L19 — Human evolution"
      }
    ],
    "L20": [
      {
        term: "Antibiotic resistance — evolution by selection",
        def: "Resistant variants pre-exist in populations at low frequency (mutation). Antibiotic use selects them; sensitive cells die. Stop-and-start dosing leaves survivors that proliferate; full courses minimize survivors. Resistance genes spread by horizontal transfer.",
        example: "Why does 'finishing the antibiotic course' have an evolutionary rationale? (Eliminates partially-resistant survivors before they can multiply.)",
        ctx: "L20 §A — Drug resistance evolution"
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
})();
