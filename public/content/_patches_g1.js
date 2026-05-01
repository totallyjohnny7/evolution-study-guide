/* Patches group 1: L01, L02, L03, L04 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L01: {
      "Evolution": {
        exAnswer: "The allele frequencies in the bacterial population shifted from <1% resistant to >95% resistant — a CHANGE in the heritable trait composition of the POPULATION across generations. Individual bacteria did not evolve; each cell lived and died with its fixed genotype. Resistance alleles started rare and ended dominant because non-resistant cells couldn't reproduce in penicillin. That cross-generational change in heritable trait frequency IS evolution.",
        mnem: "Populations evolve, individuals are selected. (Allele-frequency change across generations = evolution.)"
      },
      "Population": {
        exAnswer: "Individual finches don't evolve — each finch is born with a fixed beak depth and dies with that same beak depth. What evolves is the POPULATION: the distribution of heritable beak-depth alleles across many finches changes as deeper-beaked individuals out-reproduce shallower-beaked ones. The unit of evolution is the population (allele frequencies shift); the unit of selection is the individual (some survive/reproduce more).",
        mnem: "Populations evolve, individuals are selected. (Drought selects finches; the population evolves.)"
      },
      "Heritable variation": {
        exAnswer: "NO. Selection on color cannot make the population evolve because the variation has zero genetic basis (h² = 0). If you pick only purple flowers as parents, their offspring's color is set by the new soil pH where each offspring grows — not inherited from the parent. The breeder's equation R = h²·S goes to zero when h² = 0, regardless of how strong selection is. Selection produces evolution ONLY when phenotypic differences correlate with genetic differences.",
        mnem: "No heritability, no evolution. (R = h²·S — if h² = 0, R = 0 no matter how hard you select.)"
      },
      "Common descent": {
        exAnswer: "The graded similarity reflects shared ancestry plus time-since-divergence. All four species inherited cytochrome c from a common ancestor, then accumulated independent neutral substitutions after their lineages split. The longer two lineages have been separated, the more substitutions have piled up — so % identity is roughly inversely proportional to divergence time. Humans and rhesus shared a common ancestor most recently (~25 Ma) → 95% identity; common ancestor with fruit flies was ~600 Ma → only 75% identity.",
        mnem: "More similarity = more recent common ancestor. (Cytochrome c is a molecular clock — ticks fastest where lineages diverged longest ago.)"
      },
      "Adaptation": {
        exAnswer: "(1) ADAPTATION-AS-TRAIT: the thick fur itself is the adaptation — a heritable feature that increases fitness in cold (insulation reduces heat loss → better winter survival → more offspring). (2) ADAPTATION-AS-PROCESS: 'adaptation' also names the historical process of natural selection that shaped that trait — generations of foxes with slightly thicker fur out-reproducing thinner-furred foxes in arctic conditions. The trait is the OUTCOME; the process is the CAUSE.",
        mnem: "Adaptation = trait (the noun) AND the process that built it (the verb). Same word, two meanings — context tells you which."
      },
      "Natural selection": {
        exAnswer: "(1) HERITABLE VARIATION — dark-scale color must have a genetic basis that passes to offspring. (2) DIFFERENTIAL SURVIVAL/REPRODUCTION — darker lizards must actually leave more offspring than lighter ones (water retention → survival → reproduction). (3) FITNESS DIFFERENCES TIED TO THE TRAIT — the reproductive advantage must causally link to the heritable trait, not be coincidence. All three required: remove any one (e.g., color is environmental, or all lizards reproduce equally despite color) and no evolutionary change occurs.",
        mnem: "VHS: Variation (heritable) + Heritability + Selection differential. (Or: heritable trait → fitness difference → frequency change.)"
      },
      "Genetic drift": {
        exAnswer: "Likely DRIFT, for two reasons: (1) The founding population is tiny (N=8), so 1/(2Ne) ≈ 0.06 — only alleles with selection coefficients larger than ~6% are immune to drift; most neutral loci shouldn't 'see' selection. (2) The differences are at NEUTRAL loci, where there is no selection by definition. The 8 founders carried only a tiny random sample of mainland alleles (founder effect), and chance fixation/loss in subsequent small generations amplified divergence. Selection requires a fitness difference; neutral divergence in small founder populations is the signature of drift.",
        mnem: "Drift is the lottery; selection is the resume. (Small N + neutral loci → drift wins.)"
      },
      "Gene flow": {
        exAnswer: "Gene flow will DECREASE (toward zero) because the highway blocks salamander dispersal between halves. The most likely evolutionary consequence is GENETIC DIFFERENTIATION: the two halves now evolve independently — drift pushes neutral allele frequencies apart, and any local selection or mutation accumulates differently in each. Long-term, this is the first step toward allopatric speciation. Gene flow is HOMOGENIZING — when it stops, populations diverge.",
        mnem: "Gene flow homogenizes; barriers diversify. (Migration = mixing; isolation = divergence.)"
      },
      "Mutation": {
        exAnswer: "Wrong because it implies the antibiotic INDUCES the resistance mutation in response to need. CORRECT framing: resistance mutations occur RANDOMLY (with respect to fitness) at low frequency BEFORE the drug is applied. The antibiotic doesn't create or guide the mutations — it SELECTS the rare pre-existing resistant variants by killing everyone else. Luria-Delbrück's 1943 fluctuation test demonstrated this: mutations arise spontaneously, not in response to environmental challenge. Mutation provides random raw material; selection provides the non-random direction.",
        mnem: "Random mutation + non-random selection = adaptation. (Antibiotic selects pre-existing resistance — it doesn't create it.)"
      }
    },
    L02: {
      "Great Chain of Being (Scala Naturae)": {
        exAnswer: "Two incompatible assumptions: (1) FIXITY — species are immutable, occupying eternal preordained rungs; modern evolution requires species to change over time. (2) LINEAR HIERARCHY with humans at the top — modern evolution describes a BRANCHING tree with no preferred direction or 'higher/lower' species; humans are one twig among many, not a pinnacle. (Bonus: the Chain has no shared common ancestry — each rung was created separately; evolution requires common descent.)",
        mnem: "Chain = fixed ladder. Tree = branching bush. (Pre-Darwin: ranked rungs. Darwin: relatives, not ranks.)"
      },
      "Immutability of species": {
        exAnswer: "EXTINCTION (recognized via Cuvier's mammoth/mastodon work and stratigraphy). Once it was clear that species like trilobites and ammonites had vanished entirely, the 'fixed list of created kinds' view collapsed: if some species disappear forever, then species do change over time at the global scale. Other Darwin-era evidence: fossil succession in rock strata (older rocks → simpler/different fauna), biogeographic patterns (island species resemble mainland species, not other islands), and homologous structures across 'distinct' species.",
        mnem: "Extinction broke the eternal list. (If species can vanish, they aren't immutable.)"
      },
      "Stratigraphy": {
        exAnswer: "The shellfish lived during a specific time window, and that time window corresponds to a specific rock layer everywhere it formed. Smith can use the fossil as an INDEX FOSSIL to date and correlate rock layers across England — wherever he finds that shellfish, he knows the rock is the same age, even if the rock TYPE differs. This founded the principle of faunal succession: distinct fossil assemblages mark time horizons consistently across geography.",
        mnem: "Younger on top, fossils mark the time. (Stratigraphy: rocks in order, fossils as the calendar.)"
      },
      "Faunal succession": {
        exAnswer: "Trilobites existed ONLY during the Paleozoic (Cambrian through Permian) and went extinct at the end-Permian mass extinction ~252 Ma — they appear in rocks of that age range globally and never younger. Faunal succession lets us conclude trilobites are a TIME MARKER for Paleozoic strata: any rock containing trilobite fossils is Paleozoic, and any rock above the Permian boundary (anywhere on Earth) lacks them because the lineage was extinct.",
        mnem: "Fossils stack in the same order everywhere — they ARE the calendar. (Trilobites = Paleozoic stamp.)"
      },
      "Extinction": {
        exAnswer: "Extinction shattered the immutability-of-species view: if species created in fixed form could simply disappear, then the 'list of created kinds' was not eternal — species change at the global level. It also opened the conceptual door to species ORIGINATING (replacement of extinct lineages by new ones), and it gave evolution a mechanism for losses to balance the appearances of new lineages. Without extinction, there would be no need for new species at all.",
        mnem: "Extinction was Step 1 — once species can vanish, fixity is broken."
      },
      "Inheritance of acquired characteristics (Lamarckism)": {
        exAnswer: "Lifting weights causes muscle growth in SOMATIC (body) cells via protein synthesis and tissue remodeling — but somatic changes don't reach the germline (sperm/eggs), so they aren't inherited. The Weismann barrier separates soma from germline. Even in transgenerational epigenetics (e.g., methylation patterns inherited 1-2 generations), the underlying mechanism isn't 'use induces a needed change'; it's stress-or-diet-induced epigenetic marks, randomly distributed and usually erased within a few generations. Lamarck's mechanism — DIRECTED, useful, durable acquired changes — still doesn't apply.",
        mnem: "Lamarck = use it, pass it. Reality = Weismann barrier blocks the germline. (Bigger biceps don't make bigger-bicep babies.)"
      },
      "Uniformitarianism": {
        exAnswer: "Lyell convinced Darwin that ENORMOUS time spans were available for slow processes to produce large outcomes. If river erosion alone (operating today) could carve the Grand Canyon over millions of years, then natural selection (operating today) could produce species-scale change over similar deep-time spans. Uniformitarianism gave Darwin both the TIME and the LOGIC for gradualism: small heritable changes accumulating over deep time can produce qualitatively new forms.",
        mnem: "Same forces, more time. (Lyell to Darwin: 'You don't need miracles, just deep time.')"
      },
      "Deep time": {
        exAnswer: "Kelvin's 20-40 My estimate (based on Earth cooling from a molten state) was much shorter than Darwin needed for natural selection to produce all species; if Kelvin was right, there wasn't enough time for gradual change to do the work. The discovery of RADIOACTIVITY (Becquerel 1896, applied by Rutherford to dating) resolved it two ways: (1) radioactive decay provides a heat source Kelvin didn't know about, so Earth cools much more slowly than he calculated, and (2) radiometric dating of rocks revealed Earth is ~4.54 BILLION years old — vastly more than Darwin needed.",
        mnem: "Kelvin: 40 My (too short). Radioactivity: 4.5 By (plenty). Deep time saved Darwin."
      },
      "Natural selection": {
        exAnswer: "The critical difference is the SOURCE OF VARIATION and the DIRECTION OF CHANGE. Lamarck (1809): organisms acquire useful traits during life (use/disuse) and pass them to offspring — variation is GENERATED by need, change is DIRECTED. Darwin (1859): heritable variation arises BEFORE selection acts (random with respect to fitness) and the environment merely SELECTS among pre-existing variants — variation is undirected, selection imposes the direction. Lamarck = directed inheritance. Darwin = random variation + non-random survival.",
        mnem: "Lamarck: need → trait → kids. Darwin: random variation → selection → kids. (Direction comes from selection, not need.)"
      },
      "Heritability": {
        exAnswer: "Heritability of fruit size in this population is LOW (h² near zero). The breeder's equation R = h²·S predicts response only when h² > 0. Year-after-year stagnation despite strong selection means the largest tomatoes are big mostly for ENVIRONMENTAL reasons (water, nutrients, position on the vine) — not because they carry size-promoting alleles. Picking them adds no genetic gain. The population may have already exhausted V_A through prior selection (selection limit) or the trait may simply be environment-dominated.",
        mnem: "No response = no heritability. (R = h²·S — if R ≈ 0 despite big S, then h² ≈ 0.)"
      },
      "Selection differential (S)": {
        exAnswer: "S = mean of breeders − mean of original population = 30 − 25 = 5 L/day. (S measures how 'extreme' your selected parents are relative to the starting population — it's the strength of selection in trait units.)",
        mnem: "S = how much you cherry-picked. (Breeder mean − population mean.)"
      },
      "Hypothesis": {
        exAnswer: "The second is a hypothesis. 'Evolution is true' is too broad and unfalsifiable as stated — it doesn't specify a test. 'Mosquitoes will evolve resistance to a new pesticide within 5 generations of widespread spraying' is FALSIFIABLE (you can spray, count generations, measure resistance frequency), TESTABLE (specific organism, specific treatment, specific timeframe), and SPECIFIC. The first is a broad scientific theory or claim; the second is a narrow prediction derivable from the theory.",
        mnem: "Hypothesis = specific, testable, falsifiable. Theory = broad framework. (Hypothesis is the testable child of a theory.)"
      },
      "Scientific theory": {
        exAnswer: "They're confusing 'theory' (scientific sense) with 'guess' or 'hunch' (everyday sense). In science, a theory is a broad, deeply-supported explanatory framework that has survived repeated tests and unifies many observations. Two examples at the same level: GERM THEORY of disease (microorganisms cause infectious disease) and ATOMIC THEORY (matter is composed of atoms with subatomic structure). Both are 'just theories' in the trivial sense, yet form the unquestioned foundation of medicine and chemistry — same epistemic standing as evolution.",
        mnem: "Theory ≠ guess. Theory = well-tested framework. (Germ theory, atomic theory, evolutionary theory — same tier.)"
      },
      "Falsifiability": {
        exAnswer: "A PRECAMBRIAN RABBIT FOSSIL (or any complex modern mammal in rocks older than the appearance of mammals). J.B.S. Haldane famously cited this. Common descent predicts a specific fossil order — vertebrates after invertebrates, mammals after reptiles. Finding a rabbit (or human, or angiosperm) in 500-million-year-old Cambrian rocks would shatter the nested hierarchy of life and the temporal sequence of lineage divergence. Other potential falsifiers: identical complex organs in unrelated lineages, or universally non-nested DNA sequence patterns.",
        mnem: "Cambrian rabbit = theory dead. (Falsifiability: name what would break it.)"
      }
    },
    L03: {
      "Pseudogene": {
        exAnswer: "It reveals SHARED ANCESTRY: humans, other primates, and guinea pigs all inherited the GULO gene from a vertebrate common ancestor that COULD make vitamin C. The gene was independently disabled in the primate lineage and the guinea-pig lineage by mutations (frameshifts/stop codons) that became fixed because dietary vitamin C made the gene non-essential. The fact that we still carry the broken gene at the same chromosomal locus, with shared inactivating mutations among primates, is direct molecular evidence of common descent — there's no design-based reason to keep a non-functional GULO copy.",
        mnem: "Pseudogene = molecular fossil. (Broken genes prove the working ancestor existed.)"
      },
      "Mobile genetic element (MGE)": {
        exAnswer: "It tells us genome size doesn't track 'organismal complexity' — most of our DNA is parasitic/junk by lineage history, not functional code. The 45% transposon content reflects evolutionary accumulation of selfish genetic elements over hundreds of millions of years, not added 'complexity.' The C-VALUE PARADOX: humans (~3.2 Gb) are dwarfed by salamanders (~120 Gb) and onions (~16 Gb), yet aren't 40× simpler. Genome size mostly reflects MGE/repeat dynamics, recombination rates, and effective population size — not phenotypic complexity.",
        mnem: "MGEs are genomic squatters. (45% of you is jumping-gene legacy, not 'design'.)"
      },
      "C-value paradox": {
        exAnswer: "NO — salamanders are not 40× more complex; they have 40× more mostly-noncoding/repetitive DNA. The paradox tells us GENOME SIZE is set primarily by lineage-specific accumulation/loss of TRANSPOSABLE ELEMENTS, repetitive sequences, and intron expansion — combined with effective population size (small Ne lets slightly-deleterious extra DNA accumulate). Phenotypic complexity correlates much better with gene-regulatory network depth and proteome diversity (alternative splicing, post-translational modification) than with raw DNA quantity.",
        mnem: "Big genome ≠ complex animal. (Salamander genome: mostly repeats, not extra wisdom.)"
      },
      "DNA methylation": {
        exAnswer: "Most likely EPIGENETIC regulation — chiefly DNA METHYLATION and histone modifications. Identical DNA can produce different transcriptional landscapes when methylation patterns differ at promoters/enhancers; environments (diet, stress, temperature) lay down environment-responsive methyl marks that persist through cell divisions and shift gene expression. This is PRE-TRANSCRIPTIONAL regulation: the gene sequence is the same, but it's silenced or activated based on chromatin/methylation state. Twin studies in humans show similar epigenetic divergence with age and environment.",
        mnem: "Methyl = mute. (CpG methylation typically silences nearby transcription — a chemical 'off' switch.)"
      },
      "Histone modification": {
        exAnswer: "An HDAC inhibitor blocks REMOVAL of acetyl groups from histones, so ACETYLATED histones ACCUMULATE. Acetylation neutralizes positive lysine charges → loosens histone-DNA interaction → more OPEN chromatin → more accessible to transcription machinery. Predicted effect: GENOME-WIDE INCREASE in transcription, especially at genes that were silenced by deacetylation. (This is why HDAC inhibitors are used as anticancer drugs — they reactivate tumor-suppressor genes silenced by chromatin compaction.)",
        mnem: "Acetyl = open. (HAT writes acetyl → open chromatin → transcription ON. HDAC erases → closed → OFF.)"
      },
      "MicroRNA (miRNA)": {
        exAnswer: "POST-TRANSCRIPTIONAL. The mRNA has already been transcribed; the miRNA acts on the mature transcript by base-pairing with its 3' UTR and recruiting the RISC complex to either block translation or degrade the mRNA. The gene is transcribed normally — regulation happens at the mRNA stage, after transcription but before protein production.",
        mnem: "miRNA = mRNA muffler. (Transcript made, then silenced — POST-transcriptional.)"
      },
      "Alternative splicing": {
        exAnswer: "It demolishes the gene-count = proteome-count assumption. ONE Dscam gene generates >38,000 distinct proteins via combinatorial exon usage — vastly more proteins than the ~14,000 genes in the entire Drosophila genome. Proteome complexity isn't bounded by gene count; alternative splicing, post-translational modifications, and combinatorial regulation generate orders of magnitude more functional protein diversity than gene number predicts. Humans (~20,000 genes, ~100,000 proteins via splicing) show the same pattern.",
        mnem: "One gene, many proteins. (Dscam: 1 gene → 38,000+ isoforms via splice combinatorics.)"
      },
      "Allele": {
        exAnswer: "An ALLELE is a specific variant of a gene at a given locus. At the human ABO locus, all three alleles (I^A, I^B, i) sit at the same chromosomal position on chromosome 9, but each carries a different DNA sequence: I^A and I^B encode glycosyltransferases that add different sugars to RBC surface antigens, while i is a loss-of-function variant that adds nothing. Each diploid person has TWO alleles at this locus (one from each parent); the combination determines blood group.",
        mnem: "Allele = flavor of a gene. (Same locus, different sequence → different phenotype.)"
      },
      "Dominant": {
        exAnswer: "A new dominant deleterious allele would be eliminated by selection RAPIDLY — every heterozygote (Hh) expresses the lethal phenotype, so the allele is fully exposed to selection from the moment it appears. There is no recessive 'hiding' phase. For Huntington's specifically, late onset (post-reproductive) softens this somewhat — by the time symptoms hit, carriers have often already reproduced — which is why HD persists. But for a dominant deleterious allele acting BEFORE reproduction, selection coefficient s ≈ 1 and the allele is purged in essentially one generation.",
        mnem: "Dominant deleterious = no hiding. (Selection sees every copy — rapid removal unless onset is late.)"
      },
      "Recessive": {
        exAnswer: "Because at frequency q = 0.001, almost ALL copies of the allele exist in HETEROZYGOTES (2pq ≈ 0.002 of the population) where they're MASKED by the dominant alternative — they confer no fitness advantage when paired with the wild-type. Homozygotes (q² = 10⁻⁶) are vanishingly rare, so selection rarely 'sees' the beneficial trait. Selection on a rare recessive proceeds quadratically — Δq scales with q² — until the allele becomes common enough that homozygotes appear regularly.",
        mnem: "Recessives hide in heterozygotes. (At low q, almost all copies are masked — selection is slow.)"
      },
      "Additive": {
        exAnswer: "Additive multilocus effects produce a continuous, roughly NORMAL (Gaussian) distribution by the Central Limit Theorem. Each contributing locus adds a small, independent increment; summing many small effects yields a bell-shaped distribution centered on the genotypic mean. As the number of contributing loci grows, the distribution becomes smoother and more continuous — explaining why traits like height, skin pigmentation, and grain yield show smooth bell curves rather than discrete Mendelian classes.",
        mnem: "Additive = bell curve. (Many small additive loci + Central Limit Theorem → continuous normal phenotype.)"
      },
      "Locus": {
        exAnswer: "Different LOCI evolve INDEPENDENTLY — they're inherited separately, can be on different chromosomes (or far apart on the same chromosome), and each has its own allele frequencies, mutation history, and selection regime. Hemoglobin α and β arose from a duplication of an ancestral globin gene followed by divergence at separate locations; their independent loci let them specialize (α for embryonic-to-adult transitions, etc.) while still combining in the tetrameric protein. If they were the same locus, they couldn't diverge.",
        mnem: "Locus = address. (Different addresses → independent inheritance and divergence.)"
      },
      "Mutation": {
        exAnswer: "At 10⁻⁹ per base per division and 10¹⁴ B-cells, expected number with that exact mutation ≈ 10⁵ = 100,000 cells. But these are SOMATIC mutations — they sit in B-cells, do not reach the germline (sperm/eggs), and are not passed to offspring. Only mutations in the germline contribute to evolution. Most cells with the somatic mutation don't even matter clinically because they're just one cell among 10¹⁴ — sickle-cell disease arises only when the same mutation hits the germline and is inherited.",
        mnem: "Somatic ≠ heritable. (Only germline mutations evolve; somatic mutations die with you.)"
      },
      "Mutation rate": {
        exAnswer: "Mutation rate sets the SUPPLY of new variation. Selection can only act on alleles that exist; if mutation introduces beneficial alleles too slowly relative to the need, adaptation stalls (mutation-limited evolution). Higher mutation rates accelerate adaptation under strong novel selection (e.g., HIV evolves drug resistance fast partly because reverse-transcriptase mutation rate is ~10⁻⁴/base — 10,000× higher than mammalian rates). At the population level, expected new beneficial mutations per generation ≈ 2 N μ U_b, where N is population size, μ is mutation rate, U_b is fraction beneficial — if any factor is small, response stalls.",
        mnem: "Mutation = the supplier; selection = the buyer. (No supply, no adaptation, no matter how desperate the demand.)"
      },
      "Random with respect to fitness": {
        exAnswer: "NO. Lactose-utilization mutations occur at the same baseline rate regardless of whether lactose is present. Starvation does not 'aim' mutations toward useful targets. Luria-Delbrück's 1943 fluctuation test proved this: if mutations were induced by need, all cultures would show similar resistant counts; instead, counts fluctuated dramatically, consistent with mutations arising spontaneously BEFORE the selective challenge. The starvation environment SELECTS pre-existing lactose-utilizing variants by killing the rest — it does not direct mutation.",
        mnem: "Mutation is blind to need. (Luria-Delbrück: variants exist BEFORE selection, not BECAUSE of it.)"
      }
    },
    L04: {
      "Allele frequency": {
        exAnswer: "Total alleles = 2 × 100 = 200. A copies = 2(16) + 1(48) = 32 + 48 = 80. p = 80/200 = 0.4. (Equivalently, q = 1 − p = 0.6.) The allele frequency tells you the COMPOSITION of the gene pool — what fraction of all gene copies in the population are A — independent of how those copies are packaged into genotypes. Two populations with very different genotype distributions can have identical allele frequencies.",
        mnem: "p = (2·#AA + #Aa) / (2·N). (Each AA gives 2 A's; each Aa gives 1.)"
      },
      "Genotype frequency": {
        exAnswer: "f(AA) = 16/100 = 0.16; f(Aa) = 48/100 = 0.48; f(aa) = 36/100 = 0.36. (Sum = 1.) These tell you how alleles are PAIRED in actual individuals — i.e., the population's genetic STRUCTURE — whereas allele frequencies tell you only the marginal abundance of each allele. Inbreeding, assortative mating, or population subdivision can shift genotype frequencies dramatically while leaving allele frequencies unchanged.",
        mnem: "Allele freq = pool composition. Genotype freq = pairing pattern. (Same alleles, many pairing arrangements possible.)"
      },
      "Hardy-Weinberg equilibrium (HWE)": {
        exAnswer: "HWE is the NULL MODEL because it predicts what allele/genotype frequencies will look like when NO evolutionary force is acting (no mutation, no migration, no drift, no selection, no non-random mating). When a population FITS HWE, you canNOT conclude evolution is absent — you can only say the data don't reveal any deviation from neutral expectations. (Multiple forces can also cancel out — e.g., mutation balanced by drift — producing apparent HWE.) When a population DEVIATES from HWE, that's diagnostic: at least one force is acting, and the type of deviation hints at which.",
        mnem: "HWE = the null hypothesis. (Fit ≠ no evolution; deviation = evolution detected.)"
      },
      "Random mating (panmixia)": {
        exAnswer: "NO, the population is NOT in HWE for tail-length-related loci. Random mating (panmixia) requires that every individual is equally likely to mate with every other, regardless of genotype. Peahens preferring long-tailed peacocks is ASSORTATIVE/SEXUAL SELECTION — long-tail genotypes get more matings than short-tail genotypes. This violates assumption (5) of HWE. Result: at tail-length loci, genotype frequencies will deviate from p², 2pq, q² (typically excess homozygosity in the favored direction), and allele frequencies for long-tail alleles will rise across generations.",
        mnem: "Random mating means choice-blind mating. (Mate preference → not HWE.)"
      },
      "Inbreeding": {
        exAnswer: "Observed homozygote frequencies will be ABOVE HWE expectation (p² + Fpq for AA; q² + Fpq for aa) — and heterozygotes correspondingly DEPRESSED at 2pq(1−F). Close-kin matings increase the probability that the two alleles at a locus are identical by descent (inbreeding coefficient F > 0). Likely fitness consequence: INBREEDING DEPRESSION — exposure of normally-masked deleterious recessive alleles in the homozygous state, reducing offspring viability and fertility (lower hatch rates, smaller body size, reduced fecundity).",
        mnem: "Inbreeding = homozygosity ↑ + heterozygosity ↓. (Recessive load surfaces — inbreeding depression.)"
      },
      "Heterozygote advantage": {
        exAnswer: "HbS persists because heterozygotes (HbA/HbS) have higher fitness in malaria-endemic regions than either homozygote: HbA/HbA dies of malaria, HbS/HbS dies of sickle-cell anemia, HbA/HbS survives both with mild sickle-cell trait + malaria resistance. This balanced polymorphism HOLDS HbS at intermediate equilibrium frequency (~10%) despite homozygote lethality. HWE deviation pattern: EXCESS HETEROZYGOTES relative to p² + 2pq + q² expectation — observed Aa > 2pq, observed aa < q².",
        mnem: "Het advantage = het excess. (Sickle: HbA/HbS beats both homozygotes — kept at ~10% by malaria selection.)"
      },
      "Wahlund effect": {
        // exAnswer already provided in flashcards-extra.js — only adding mnem
        mnem: "Subdivision fakes inbreeding. (Pool different-frequency populations → apparent homozygote excess, no actual inbreeding.)"
      }
    }
  });
})();
