/* Importance content (group 1: L01-L04) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  /* ============================================================ */
  /* L01 — What Is Evolution? Course Intro                         */
  /* ============================================================ */
  window.addCardPatches('L01', {
    "Evolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Evolution is a POPULATION-LEVEL, MULTI-GENERATIONAL change in allele frequencies — not anything that happens to a single organism. Robbins will absolutely test the unit-of-evolution distinction.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Definition: change in heritable trait (allele) frequencies in a population across generations</li>
  <li>Three required ingredients: heritable variation, differential reproduction, the change must be across generations</li>
  <li>Time scale: at least one generation; often many</li>
  <li>Unit of EVOLUTION = population. Unit of SELECTION = individual. (Two different units — easy mix-up.)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the operational definition.</strong> Every later lecture (HWE, drift, selection, speciation) reduces to "what changes the allele frequencies and by how much." Without this anchor, none of the math means anything.</li>
  <li><strong>It rules out individual-scale claims.</strong> "The finch evolved a longer beak during the drought" is wrong — finches don't evolve, populations do. Catching this on an exam = easy points.</li>
  <li><strong>Heritability is non-negotiable.</strong> If trait variation is purely environmental (h² = 0), selection produces ZERO evolutionary change no matter how strong. Connects directly to the breeder's equation R = h²·S in L05.</li>
  <li><strong>Frames the course.</strong> The four mechanisms (selection, drift, gene flow, mutation) are all defined as "what shifts allele frequencies." Robbins-bait phrase: "the unifying theory of biology" (Dobzhansky 1973).</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Evolution = progress / improvement" — WRONG. Drift can fix harmful alleles in small populations. Evolution is just frequency change, directionless on its own.</li>
  <li>"Individuals evolve over their lifetime" — WRONG. They develop, learn, age — but their genotype is fixed at conception.</li>
</ul>`
    },

    "Population": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The POPULATION is the unit of evolution — a group of interbreeding individuals sharing a gene pool. This distinction (population vs. individual) is exam gold.</p>
<h4>The numbers</h4>
<ul>
  <li>Effective population size (Ne) determines drift strength: 1/(2Ne) is the threshold below which selection is overwhelmed by drift</li>
  <li>Small Ne (&lt;100) → strong drift; large Ne (&gt;10,000) → drift is weak relative to even mild selection</li>
  <li>Ne is usually MUCH smaller than census size (sex ratio, variance in offspring number, bottlenecks all reduce Ne)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Sets up Hardy-Weinberg.</strong> HWE predicts allele frequencies in an ideal infinite-sized population — population is the math object the rest of pop-gen operates on.</li>
  <li><strong>Decides which forces dominate.</strong> Small populations → drift wins. Large populations → selection wins. Population size is itself a parameter in the algebra.</li>
  <li><strong>Speciation needs reproductive isolation between populations</strong> — so defining "population" matters for biological species concept (L13).</li>
  <li><strong>Lets you talk about gene flow.</strong> Gene flow only makes sense as movement BETWEEN populations.</li>
</ol>
<h4>Robbins-bait</h4>
<ul>
  <li>"Population evolves; individual is selected" is the punchline phrase to memorize — likely on a multiple-choice or short-answer item.</li>
</ul>`
    },

    "Heritable variation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Without HERITABLE variation, selection produces NO evolutionary change — h² = 0 means R = 0, period. This is the breeder's-equation gotcha.</p>
<h4>The numbers</h4>
<ul>
  <li>R = h²·S — response to selection equals heritability times selection differential</li>
  <li>h² = V_A / V_P — ratio of additive genetic variance to total phenotypic variance</li>
  <li>h² ranges from 0 (purely environmental) to 1 (entirely additive-genetic)</li>
  <li>Most fitness-relevant traits: h² typically 0.1–0.5 (modest)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the missing piece in pre-Darwinian thought.</strong> Lamarckism failed because it assumed acquired (non-heritable) traits could pass on. Darwin succeeded because he stuck to heritable variation.</li>
  <li><strong>The classic exam trap.</strong> "Strong selection on tomato size produces no response after 10 generations." Why? Heritability is near zero — variation is from soil/water, not genes. Diagnose by R = h²·S with h² ≈ 0.</li>
  <li><strong>Sets up the breeder's equation (L05).</strong> The whole quantitative-genetics edifice rests on partitioning variance into heritable (V_A) vs. non-heritable (V_E) components.</li>
  <li><strong>Connects environment to evolution.</strong> Even a perfectly designed selection regime can fail if the trait isn't genetic. This is also why "purely epigenetic" inheritance is contested as an evolutionary force.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>L02 — Lamarck (acquired vs. heritable)</li>
  <li>L03 — alleles, mutation, the GENETIC basis of heritable variation</li>
  <li>L05 — V_A, V_E, h² and R = h²·S (the actual math)</li>
</ul>`
    },

    "Common descent": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> ALL life shares ONE common ancestor — this is one of biology's most heavily evidenced claims, and Robbins will test the lines of evidence.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Universal genetic code: ~64 codons → ~20 amino acids, NEAR-IDENTICAL across all domains (only minor variants in mitochondria, some ciliates)</li>
  <li>Cytochrome c percent identity: humans-rhesus ~95%, humans-dog ~90%, humans-fly ~75% — tracks divergence time</li>
  <li>Last Universal Common Ancestor (LUCA) lived ~3.5–4.0 billion years ago</li>
  <li>Conserved core: ribosomal RNA, ATP synthase, DNA polymerase — same in bacteria, archaea, eukaryotes</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the second meaning of "evolution."</strong> Beyond microevolutionary frequency change, evolution as a HISTORICAL CLAIM = common descent. Both senses are tested.</li>
  <li><strong>Lines of evidence (memorize the list):</strong> universal genetic code, homologous proteins (cyt c, rRNA), shared metabolic pathways, nested phylogenetic hierarchy, fossil progression, biogeography, vestigial structures, pseudogenes (broken-gene fossils — see L03).</li>
  <li><strong>Falsifier you should be ready to name.</strong> A Precambrian rabbit fossil. Identical complex organs in unrelated lineages. Different genetic codes per domain. None of these have ever been found.</li>
  <li><strong>Frames every later phylogeny lecture.</strong> Trees, synapomorphies, monophyletic groups (L08, L09) all assume common descent.</li>
</ol>
<h4>Robbins-bait</h4>
<ul>
  <li>Cytochrome c is a classic exam example — be ready to interpret a percent-identity table.</li>
  <li>"What would falsify common descent?" is a textbook short-answer.</li>
</ul>`
    },

    "Adaptation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> "Adaptation" has TWO meanings — a TRAIT (the noun) and the PROCESS that produced it (the verb). Robbins explicitly flags this in the lecture-guide exam_traps.</p>
<h4>The numbers / requirements</h4>
<ul>
  <li>Three requirements for adaptation by natural selection: heritable variation, differential reproduction, fitness differences linked to the trait</li>
  <li>Adaptation requires a HERITABLE basis — not just a trait that "fits" the environment</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The two-meanings ambiguity is a Robbins trap.</strong> "Arctic fox fur is an adaptation" can mean (a) the fur itself = heritable trait raising fitness in cold, OR (b) the historical process of selection that made it. Context tells you which — both meanings are correct.</li>
  <li><strong>Distinguishes from mere correlation.</strong> A trait that LOOKS useful isn't automatically an adaptation. Need evidence of (i) heritability, (ii) historical selection for that trait, (iii) function in the relevant environment.</li>
  <li><strong>Sets up exaptation (L11).</strong> Some "adaptations" were originally selected for a different function — feathers (insulation → flight). The word "adaptation" carries a built-in claim about WHY a trait exists.</li>
  <li><strong>Just-so stories.</strong> Critics (Gould, Lewontin 1979 "spandrels" paper) warn against assuming every trait is an adaptation. Some are by-products, drift, or developmental constraints.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>L11 — exaptation, spandrels, vestigial traits</li>
  <li>L07 — measuring selection in the wild (Grant finches)</li>
</ul>`
    },

    "Natural selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Natural selection is the ONLY mechanism that systematically increases fitness — drift, mutation, and gene flow can change frequencies, but only selection is non-random with respect to fitness.</p>
<h4>The numbers / requirements</h4>
<ul>
  <li>Three required ingredients: (1) heritable variation, (2) variation correlates with reproductive success, (3) fitness differences propagate across generations</li>
  <li>Selection coefficient (s): the relative fitness disadvantage; s = 0 (neutral) to s = 1 (lethal)</li>
  <li>Selection dominates drift when |s| &gt;&gt; 1/(2Ne)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's THE engine of adaptation.</strong> Mutation provides raw material; drift is random; gene flow is homogenizing. Only selection has a direction (toward higher fitness in the current environment).</li>
  <li><strong>The mechanism distinguishing Darwin from Lamarck.</strong> Darwin: variation arises before selection (random); selection acts on it. Lamarck: variation is generated BY need (directed). Robbins will test this.</li>
  <li><strong>Operationally testable.</strong> The Grants' Galápagos finch work (L07) shows selection in real time — beak depth shifted measurably across one drought.</li>
  <li><strong>Three modes (L05): directional, stabilizing, disruptive.</strong> Each shifts the trait distribution differently. Be ready to ID from a graph.</li>
</ol>
<h4>vs. drift</h4>
<ul>
  <li>Both change allele frequencies</li>
  <li>Selection is DIRECTIONAL (toward higher fitness); drift is RANDOM</li>
  <li>Selection works in any population size; drift dominates only in small populations</li>
  <li>Selection requires fitness differences; drift requires only chance sampling</li>
</ul>`
    },

    "Genetic drift": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Drift is RANDOM allele-frequency change driven by chance sampling — strongest in SMALL populations, where it can override selection. Robbins will test the small-N condition.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Drift dominates when |s| &lt; 1/(2Ne) — for Ne = 100, alleles with s &lt; 0.5% drift like neutrals</li>
  <li>Probability a NEW neutral allele fixes = 1/(2N) (very small in big populations)</li>
  <li>Probability of fixation of an allele at frequency p = p (for neutral alleles — the Kimura result)</li>
  <li>Time to fixation of a neutral allele ≈ 4Ne generations</li>
  <li>Heterozygosity decays at rate 1/(2Ne) per generation</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Drift can override selection in small populations.</strong> A slightly beneficial allele (s = 0.005) is effectively NEUTRAL in a population of 50 (1/(2·50) = 0.01 &gt; s). This is THE key small-population result.</li>
  <li><strong>Founder effects and bottlenecks are drift events.</strong> A handful of founders carries a non-random sample of source-population alleles → instant divergence. Classic example: Galápagos finches founded by &lt;10 birds.</li>
  <li><strong>Drift removes variation.</strong> Heterozygosity decays geometrically — a population of 100 loses ~0.5% of heterozygosity per generation. Long isolation in small groups → fixation of alleles via drift alone.</li>
  <li><strong>Underpins the neutral theory (Kimura, L19).</strong> Most observed molecular variation is invisible to selection and drifts neutrally — drift is the dominant force at most loci, not selection.</li>
</ol>
<h4>vs. selection</h4>
<ul>
  <li>Both change allele frequencies</li>
  <li>Drift is undirected; selection has direction toward fitness</li>
  <li>Drift is strong when N is small; selection works at any N</li>
  <li>Drift fixes alleles randomly; selection fixes higher-fitness alleles preferentially</li>
</ul>`
    },

    "Gene flow": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Gene flow HOMOGENIZES populations — when migration stops, populations diverge. This sets up speciation.</p>
<h4>The numbers</h4>
<ul>
  <li>One migrant per generation (Nm ≥ 1) is enough to prevent significant differentiation by drift between populations</li>
  <li>Wright's island model: F_ST ≈ 1/(1 + 4Nm) — high migration → low differentiation</li>
  <li>Gene flow homogenizes; isolation diversifies</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It opposes drift and local selection.</strong> Even a trickle of migration (one per generation) can keep populations genetically similar across vast geographic distances.</li>
  <li><strong>Required to STOP for speciation.</strong> The biological species concept (Mayr) defines species as reproductively isolated — i.e., NO gene flow. Allopatric speciation (L13) starts with a barrier blocking gene flow.</li>
  <li><strong>Conservation relevance.</strong> Habitat fragmentation reduces gene flow → smaller effective populations, drift, inbreeding (Florida panther). Genetic rescue restores gene flow to recover variation.</li>
  <li><strong>Quantified by F_ST.</strong> A measure of among-population genetic differentiation — high F_ST = low gene flow. Standard tool in molecular ecology.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Migration always introduces new variation" — partly true but the main effect is HOMOGENIZING, reducing differences between populations.</li>
  <li>Gene flow is via gametes too (pollen, sperm) — not just whole-organism migration.</li>
</ul>`
    },

    "Mutation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutation is RANDOM with respect to fitness — and it's the ONLY source of new genetic variation. Robbins will test "mutation is not directed by need."</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mutation rate per base per generation: ~10⁻⁸ to 10⁻⁹ in mammals</li>
  <li>Per-genome new mutations per individual per generation: dozens (humans: ~70 new mutations)</li>
  <li>HIV reverse-transcriptase rate ~10⁻⁴/base — 10,000× higher than mammals → fast drug resistance</li>
  <li>Most mutations are neutral or slightly deleterious; beneficial mutations are rare</li>
  <li>Luria-Delbrück (1943) fluctuation test PROVED mutations arise BEFORE selection, not in response to it</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the ultimate source of new alleles.</strong> Selection cannot create alleles; it only sorts existing variants. Without mutation, selection eventually exhausts variation and adaptation halts.</li>
  <li><strong>RANDOM with respect to fitness.</strong> Mutations don't appear because they would be useful. Antibiotic resistance mutations arise BEFORE the antibiotic is applied; the antibiotic just selects pre-existing variants. THE classic Robbins-trap question.</li>
  <li><strong>Luria-Delbrück 1943 is testable lore.</strong> Fluctuation test on bacteriophage resistance — distributions of mutant counts proved mutations are spontaneous, not induced. Be ready to name the experiment.</li>
  <li><strong>Mutation rate sets adaptation speed.</strong> Higher μ → faster adaptation to novel selection (HIV evolves drug resistance fast partly because of high μ). Lower μ → mutation-limited evolution.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Antibiotics CAUSE bacteria to mutate to resist" — WRONG. Antibiotics SELECT pre-existing resistance variants.</li>
  <li>"Mutation rates can be elevated by stress" — TRUE for some hotspots, but the random-with-respect-to-fitness claim is about DIRECTION (no preference for useful changes), not about uniform per-base probability.</li>
</ul>`
    },

    "Heritable vs non-heritable variation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection only produces evolution when variation is HERITABLE — h² = 0 → R = 0, full stop. Robbins exam staple.</p>
<h4>The numbers</h4>
<ul>
  <li>R = h²·S — the breeder's equation</li>
  <li>h² = V_A / V_P</li>
  <li>If V_A = 0 (no additive genetic variance) → h² = 0 → no response to selection</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinguishes evolutionary change from non-evolutionary change.</strong> A field of dandelions varies in color from soil pH alone — selecting purple won't produce a purple population, because the variation isn't transmitted. Pop changes within a generation (developmental plasticity) ≠ evolution.</li>
  <li><strong>Why Lamarck failed.</strong> Acquired characteristics aren't (generally) heritable — the Weismann barrier separates somatic changes from the germline. Lifting weights doesn't make stronger babies.</li>
  <li><strong>Why epigenetic inheritance is contested.</strong> Some methylation marks transmit across 1–2 generations, but they're usually erased and not directional — debates whether this counts as "evolution by epigenetic inheritance."</li>
  <li><strong>Diagnosis tool on exams.</strong> "Why does selection on a trait produce no response?" → check heritability first.</li>
</ol>`
    },

    "Population vs individual — what actually evolves?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> POPULATIONS evolve; INDIVIDUALS are selected. This sentence-level distinction is THE most common exam-trap in L01.</p>
<h4>The numbers</h4>
<ul>
  <li>Time scale of evolution: at least 1 generation, usually many</li>
  <li>Time scale of selection (acting): within one generation</li>
  <li>What changes during evolution: allele frequencies (population property)</li>
  <li>What changes during selection: number of offspring contributed by individuals</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Catches sloppy phrasing.</strong> "The finch evolved a longer beak during the drought" — wrong. Each finch had a fixed beak; what evolved was the population mean across generations. Catching this = easy points.</li>
  <li><strong>Foundational for Hardy-Weinberg.</strong> HWE describes a POPULATION's allele/genotype frequencies. The math doesn't even apply to individuals.</li>
  <li><strong>Levels-of-selection debates.</strong> Group selection vs. individual selection vs. kin selection (L18) all turn on which level the selection process operates at.</li>
  <li><strong>Robbins explicitly flags this</strong> in the L01 exam_traps.</li>
</ol>
<h4>Memorize the punchline phrase</h4>
<ul>
  <li>"Populations evolve, individuals are selected."</li>
</ul>`
    },

    "Mutation: random or directed by need?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutations are RANDOM with respect to fitness — the environment SELECTS pre-existing variants, it doesn't create them. The Luria-Delbrück 1943 experiment is canonical.</p>
<h4>The numbers</h4>
<ul>
  <li>Luria-Delbrück 1943: fluctuation test on E. coli resistance to bacteriophage T1</li>
  <li>If mutations were INDUCED by phage exposure → similar resistant counts across cultures</li>
  <li>Observed: huge variance in resistant counts across cultures → mutations arose SPONTANEOUSLY, before exposure</li>
  <li>Won Luria the 1969 Nobel Prize</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinguishes Darwinian from Lamarckian thinking.</strong> Lamarck: need induces useful trait. Darwin: random variation, then selection. The randomness is about FITNESS DIRECTION, not uniform per-base probability.</li>
  <li><strong>The exam classic:</strong> "Antibiotics cause bacteria to mutate to resist." WRONG — antibiotics select pre-existing resistant cells. Memorize the framing.</li>
  <li><strong>Naming the Luria-Delbrück experiment</strong> elevates a short answer. Be ready to describe the fluctuation test in one sentence.</li>
  <li><strong>Connects to mutation hotspots and stress-induced mutagenesis.</strong> Some local rate-elevations exist, but the claim is still that mutations don't preferentially produce useful alleles.</li>
</ol>`
    },

    "Selection vs drift — when does each dominate?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection wins when |s| &gt;&gt; 1/(2Ne); drift wins when |s| &lt;&lt; 1/(2Ne). Population size sets which force is decisive.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Threshold: 1/(2Ne)</li>
  <li>Ne = 50 → threshold s ≈ 0.01 (1%); Ne = 10,000 → threshold s ≈ 0.00005</li>
  <li>"Effectively neutral" zone: |s| &lt; 1/(2Ne) — alleles drift even if slightly beneficial/deleterious</li>
  <li>Probability a new neutral allele fixes = 1/(2N)</li>
  <li>Probability a new beneficial allele (small s) fixes ≈ 2s</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Single most useful pop-gen heuristic.</strong> Tells you which force matters in any given scenario before you do any algebra.</li>
  <li><strong>Why small populations lose adaptation.</strong> Beneficial alleles can be lost to drift. Bottlenecks erode hard-won adaptations.</li>
  <li><strong>Conservation: small Ne → drift dominates → genetic load accumulates.</strong> Florida panther, cheetahs are textbook examples (L17).</li>
  <li><strong>Underpins Kimura's neutral theory.</strong> Most molecular variation has |s| below the drift threshold → evolves neutrally. Drift is the dominant molecular force at most loci.</li>
</ol>
<h4>Quick exam diagnosis</h4>
<ul>
  <li>Given Ne and s? Compute 1/(2Ne); compare to s; whichever is larger wins.</li>
</ul>`
    },

    "Common descent — strongest evidence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The UNIVERSAL GENETIC CODE is the single strongest piece of evidence for common descent — there's no chemical reason CGU has to mean Arginine, yet it does in everything from E. coli to whales.</p>
<h4>The numbers</h4>
<ul>
  <li>~64 codons → ~20 amino acids (with start/stop)</li>
  <li>Genetic code is universal across all 3 domains (bacteria, archaea, eukaryotes) with only minor exceptions in some mitochondria/ciliates</li>
  <li>Cytochrome c: humans-rhesus 95%, humans-fly 75% — tracks divergence time</li>
  <li>~1,500 universal genes across all life (LUCA's toolkit)</li>
  <li>LUCA: ~3.5–4.0 billion years ago</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The "frozen accident" argument.</strong> Independent origins would predict different genetic codes (no chemical necessity to which amino acid each codon encodes). One near-universal code → one ancestor.</li>
  <li><strong>Multi-line argument.</strong> Don't rely on one piece — common descent is supported by molecular code + homologous proteins (cyt c, rRNA) + nested phylogenetic hierarchy + fossil progression + biogeography + pseudogenes.</li>
  <li><strong>Robbins likely tests "name 3 pieces of evidence for common descent."</strong> Have your list ready.</li>
  <li><strong>Falsifier: a species with a fundamentally different genetic code that fits no nested hierarchy.</strong> Never observed.</li>
</ol>`
    },

    "Adaptation — three things selection requires": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection produces adaptation only with ALL THREE: heritable variation, differential reproduction, and fitness causally linked to the trait. Miss any one → no adaptation.</p>
<h4>The numbers / requirements</h4>
<ul>
  <li>(1) Heritable variation — h² &gt; 0</li>
  <li>(2) Differential survival/reproduction — different individuals leave different numbers of offspring</li>
  <li>(3) Causal link — the fitness difference is BECAUSE of the trait, not coincidence</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's a diagnostic checklist.</strong> Given an exam scenario, identify which of the three is missing if the population fails to evolve.</li>
  <li><strong>Mismatched definitions trip students.</strong> "Survival differences" alone aren't enough — you need REPRODUCTIVE differences. Survival without reproduction = no genetic legacy.</li>
  <li><strong>Causal vs. correlational.</strong> If deeper-beaked finches happen to live in better habitat, the apparent selection on beak depth could be confounded — the trait must causally drive the fitness difference.</li>
  <li><strong>The Grants' work (L07)</strong> documented all three: heritable beak depth, differential survival in drought, and the deep-beaked offspring inherited the trait.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Variation exists" — necessary but not sufficient. Add the heritability and reproduction parts.</li>
  <li>"Heritable variation + fitness differences" without causal link → can produce spurious selection signals.</li>
</ul>`
    }
  });

  /* ============================================================ */
  /* L02 — Evolutionary Thinking — Pre-Darwinian to Natural Sel.   */
  /* ============================================================ */
  window.addCardPatches('L02', {
    "Great Chain of Being (Scala Naturae)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The Scala Naturae is a FIXED LADDER (no branching, no descent, humans on top) — the OPPOSITE of an evolutionary tree. Robbins flags this as an exam trap.</p>
<h4>The numbers / dates</h4>
<ul>
  <li>Aristotle's Scala Naturae: ~350 BCE</li>
  <li>Dominant Western view from antiquity through ~1800</li>
  <li>Three core assumptions: (1) species are FIXED (immutable), (2) life is a LINEAR HIERARCHY with humans at the apex, (3) NO common ancestry</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Provides the "before" picture.</strong> Understanding pre-Darwinian thought lets you appreciate what Darwin's tree of life replaced.</li>
  <li><strong>Persistent misconception.</strong> Many students still implicitly think evolution "progresses toward humans." It doesn't — evolution has no goal or direction.</li>
  <li><strong>Three contrasts to memorize:</strong> Chain = ladder, fixed, ranked, separate creations. Tree = branching, change, no ranks, common descent.</li>
  <li><strong>Robbins-bait.</strong> Likely tested via "which assumption of Scala Naturae is incompatible with evolution?" Answer: all three core ones.</li>
</ol>
<h4>vs. evolutionary tree</h4>
<ul>
  <li>Chain: fixed positions, hierarchy, no relatedness</li>
  <li>Tree: branching descent, no inherent hierarchy, all branches share ancestry</li>
  <li>Chain says species are eternal types; tree says species change and split</li>
</ul>`
    },

    "Immutability of species": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The pre-Darwinian assumption that species DON'T CHANGE — broken first by EXTINCTION (Cuvier, Smith) and finally by Darwin's natural selection.</p>
<h4>The numbers / timeline</h4>
<ul>
  <li>Dominant view through ~1800</li>
  <li>Cuvier (~1800) demonstrated extinction by comparing fossil mammoths to all known living mammals</li>
  <li>William Smith (1815) published "the map that changed the world" using fossil-based stratigraphy</li>
  <li>Darwin overturned with On the Origin (1859)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Extinction broke immutability.</strong> If species could vanish, the "fixed list of created kinds" view collapsed. Cuvier was a creationist but his extinction work fatally undermined fixity.</li>
  <li><strong>Frames Darwin's contribution.</strong> Lamarck and Darwin both proposed species change; what Darwin added was the MECHANISM (natural selection) and weight of evidence.</li>
  <li><strong>Diagnostic tool.</strong> If asked "what was the dominant view before Darwin?" — fixed species, no extinction, no shared ancestry.</li>
  <li><strong>Connects to faunal succession (Smith)</strong> — by showing fossil assemblages CHANGE through rock layers, Smith made fixed species untenable.</li>
</ol>`
    },

    "Stratigraphy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> William Smith's stratigraphy + faunal succession ESTABLISHED EXTINCTION as a real phenomenon, breaking the immutability-of-species view. Robbins explicitly flags Smith.</p>
<h4>The numbers / dates</h4>
<ul>
  <li>William Smith: early 1800s; "Map of the Strata of England and Wales" published 1815</li>
  <li>Principle of superposition: younger rocks lie atop older ones (Steno, 1669)</li>
  <li>Principle of faunal succession: distinct fossil assemblages mark distinct strata in CONSISTENT order globally</li>
  <li>Cuvier independently established extinction ~1800 using fossil mammals</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundational for paleontology.</strong> Without stratigraphy, fossils have no temporal context — and evolutionary history is unrecoverable.</li>
  <li><strong>Smith was a CIVIL ENGINEER, not an academic.</strong> His maps were practical (canal construction) but his data overturned a centuries-old worldview. Be ready to name him.</li>
  <li><strong>Index fossils:</strong> a fossil characteristic of a specific time period, used to date rocks anywhere on Earth. Trilobites = Paleozoic. Ammonites = Mesozoic.</li>
  <li><strong>Provided "deep time evidence" for Darwin.</strong> Smith's stratigraphy + Lyell's deep time gave Darwin both the temporal framework and the evidence base for slow change.</li>
</ol>
<h4>Robbins-bait</h4>
<ul>
  <li>Specifically links William Smith to extinction — be ready to attribute him.</li>
</ul>`
    },

    "Faunal succession": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> FOSSIL ASSEMBLAGES OCCUR IN A CONSISTENT VERTICAL ORDER worldwide — Smith's principle that lets rocks be dated by their fossils.</p>
<h4>The numbers / examples</h4>
<ul>
  <li>Smith's principle: distinct fossil assemblages occur in a consistent order in rock strata</li>
  <li>Trilobites: Cambrian-Permian (~540–252 Ma) — Paleozoic only</li>
  <li>Ammonites: Devonian-end Cretaceous (~419–66 Ma)</li>
  <li>Dinosaurs (non-avian): Triassic-end Cretaceous (~252–66 Ma)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's how we know fossil order.</strong> Faunal succession lets paleontologists correlate rock layers across continents — same fossils = same time.</li>
  <li><strong>Made extinction undeniable.</strong> If trilobites are present in lower (older) rocks but absent in upper (younger) rocks worldwide, they must have gone extinct.</li>
  <li><strong>Index fossils:</strong> A fossil with restricted temporal range used to date rocks. Trilobites are textbook example.</li>
  <li><strong>Distinct from explanations.</strong> Faunal succession is DESCRIPTIVE — it doesn't explain WHY species disappear. The pattern motivated extinction-as-explanation.</li>
</ol>
<h4>Robbins-bait</h4>
<ul>
  <li>Trilobites → Paleozoic stamp. Ammonites → Mesozoic. Memorize at least one example.</li>
</ul>`
    },

    "Extinction": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Recognizing extinction (Cuvier ~1800, Smith ~1815) shattered the immutability-of-species view and opened the door to evolutionary thinking.</p>
<h4>The numbers / events</h4>
<ul>
  <li>Cuvier (~1800) used fossil mammoths/mastodons to demonstrate extinction</li>
  <li>5 major mass extinctions in Earth history: end-Ordovician, end-Devonian, end-Permian, end-Triassic, end-Cretaceous</li>
  <li>End-Permian (~252 Ma) is the largest: ~95% marine species lost</li>
  <li>End-Cretaceous (~66 Ma): non-avian dinosaurs, ammonites — Chicxulub asteroid + Deccan volcanism</li>
  <li>Background extinction rate: ~1 species per million per year</li>
  <li>Current "Sixth Extinction" rates may be 100–1000× background</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Step 1 in dismantling immutability.</strong> Without extinction, species are eternal; with it, the fixed-list view collapses.</li>
  <li><strong>Without extinction, no need for new species.</strong> Extinction creates ecological openings that adaptive radiation fills (mammals after K-Pg).</li>
  <li><strong>Fossil record = log of extinctions.</strong> Rock-layer absences mark where lineages ended.</li>
  <li><strong>Mass extinctions reset evolution.</strong> The K-Pg mammalian radiation is impossible without dinosaur extinction.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>Faunal succession (the descriptive pattern)</li>
  <li>L11 — adaptive radiation following extinction</li>
  <li>L17 — current Sixth Extinction / conservation</li>
</ul>`
    },

    "Inheritance of acquired characteristics (Lamarckism)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Lamarck (1809) was first with an EVOLUTIONARY MECHANISM — but the mechanism (use/disuse + heritable acquired traits) was wrong. Robbins explicitly tests Lamarck attribution.</p>
<h4>The numbers / dates</h4>
<ul>
  <li>Jean-Baptiste Lamarck published Philosophie Zoologique in 1809 (50 years before Darwin's Origin)</li>
  <li>The classic example: giraffe stretched its neck → offspring inherit longer necks</li>
  <li>Weismann's barrier (~1890) blocks somatic→germline information transfer in animals</li>
  <li>Modern transgenerational epigenetics: 1–2 generations, usually erased — NOT Lamarckian</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Wrong mechanism, right intuition.</strong> Lamarck was right that species change; wrong about HOW. Acknowledging him correctly = exam points.</li>
  <li><strong>Foil for Darwin.</strong> The contrast Lamarck (directed by need) vs. Darwin (random variation, then selection) is the conceptual heart of L02.</li>
  <li><strong>The Weismann barrier is the answer to "why doesn't Lamarckism work."</strong> Soma and germline are separated; muscle changes don't reach the eggs/sperm.</li>
  <li><strong>Epigenetic inheritance is NOT Lamarckism.</strong> Modern epigenetic marks aren't directed by need, aren't durable across many generations. Don't get confused.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>Don't dismiss Lamarck as "just wrong." His contribution was proposing a mechanism at all — name him as the "first systematic evolutionary mechanism."</li>
</ul>`
    },

    "Uniformitarianism": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Charles Lyell's principle — the SAME GRADUAL PROCESSES operating today shaped Earth over deep time — gave Darwin the time and the logic for slow evolution.</p>
<h4>The numbers / dates</h4>
<ul>
  <li>Charles Lyell published Principles of Geology in 1830–1833</li>
  <li>Lyell brought a copy on the Beagle voyage; Darwin read it during the 5-year trip</li>
  <li>Earth's actual age: ~4.54 billion years (vastly more than Lyell could quantify, but his concept was right)</li>
  <li>Lyell explicitly contrasted with CATASTROPHISM (sudden, often biblical, events shaping Earth)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Lyell's gift to Darwin: deep time.</strong> The Origin of Species would be impossible without enormous time spans for slow change to accumulate. Lyell provided the conceptual framework.</li>
  <li><strong>Uniformitarianism vs. catastrophism.</strong> Pre-Lyell view (catastrophism, Cuvier) was that big changes came from sudden global events. Lyell argued for gradual, ongoing processes — same forces, more time.</li>
  <li><strong>Same logic for evolution.</strong> If everyday river erosion built the Grand Canyon over millions of years, then everyday selection could build species-scale change.</li>
  <li><strong>Lyell himself wasn't an evolutionist initially</strong> — he was a geologist. His contribution to evolution was indirect via deep time.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>Lyell ≠ Lamarck (different L's, different L names — easy to confuse).</li>
  <li>Lyell didn't propose evolutionary mechanism; he provided the temporal framework.</li>
</ul>`
    },

    "Deep time": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Earth is ~4.54 BILLION years old — vast deep time is required for gradual evolutionary change to accumulate. Lyell gave Darwin the concept; radioactivity confirmed the magnitude.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Earth's age: 4.54 billion years (radiometric dating of meteorites)</li>
  <li>Origin of life: ~3.5–4.0 Ga</li>
  <li>Cambrian explosion: 538 Ma</li>
  <li>Lord Kelvin's flawed estimate: ~20–40 million years (1862, based on Earth cooling)</li>
  <li>Radioactivity discovered: 1896 (Becquerel); applied to dating: Rutherford ~1905</li>
  <li>Holmes 1913 estimate: 1.6 billion years (close enough)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Without deep time, evolution doesn't work.</strong> Darwin needed enormous spans for slow accumulation. Kelvin's short Earth was a major late-19th-century challenge to Darwin.</li>
  <li><strong>Radioactivity solved it twice.</strong> (1) It's an internal heat source Kelvin didn't know about → Earth cools much more slowly. (2) Radiometric dating directly measures rock age, confirming billions of years.</li>
  <li><strong>Robbins-bait timeline:</strong> Lyell concept (1830) → Darwin (1859) → Kelvin objection (1862) → Becquerel (1896) → resolution.</li>
  <li><strong>Sets scale for everything.</strong> 3.5 Ga of life, 540 Ma of multicellular animals, 65 Ma since dinosaurs, 6 Ma since human-chimp split, 200 Ka since modern Homo sapiens.</li>
</ol>`
    },

    "Natural selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Darwin (1859) provided the MECHANISM for evolution — random heritable variation + non-random differential reproduction = directional change. Independently co-discovered by Wallace (1858).</p>
<h4>The numbers / dates</h4>
<ul>
  <li>Darwin's voyage on HMS Beagle: 1831–1836</li>
  <li>Wallace's letter to Darwin: 1858 (from the Malay Archipelago, on Ternate)</li>
  <li>Joint Darwin-Wallace paper: 1858 Linnean Society</li>
  <li>On the Origin of Species: November 24, 1859 (sold out first day)</li>
  <li>Three observations + one inference framework</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The breakthrough that beat Lamarck.</strong> Darwin: variation arises BEFORE selection (random); selection acts on it. Lamarck: variation generated BY need (directed). Robbins will test the contrast.</li>
  <li><strong>Three observations + one inference</strong> (memorize structure): (1) heritable variation, (2) overproduction of offspring, (3) non-random survival/reproduction → (4) heritable variants associated with reproductive success increase in frequency.</li>
  <li><strong>Wallace independently.</strong> Robbins explicitly tests "which naturalist spurred Darwin to publish" — answer: WALLACE, via 1858 letter.</li>
  <li><strong>The unifying mechanism.</strong> Operates in any system with replication, variation, and differential reproduction — not just biology.</li>
</ol>
<h4>vs. Lamarck</h4>
<ul>
  <li>Lamarck: need → trait → kids (directed inheritance)</li>
  <li>Darwin: random variation → selection → kids (direction comes from selection, not need)</li>
  <li>Lamarck: variation generated by need; Darwin: variation pre-exists need</li>
</ul>`
    },

    "Heritability": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Heritability (h²) is the FRACTION of phenotypic variance that's heritable additive genetic — h² controls how much a population responds to selection per generation.</p>
<h4>The numbers</h4>
<ul>
  <li>h² = V_A / V_P (narrow-sense)</li>
  <li>H² = V_G / V_P (broad-sense)</li>
  <li>R = h² · S (breeder's equation — the response equation)</li>
  <li>h² ranges 0 (purely environmental) to 1 (entirely additive-genetic)</li>
  <li>Most fitness traits: h² ≈ 0.1–0.5</li>
  <li>Morphological traits: often higher h² (~0.4–0.7)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Predicts response to selection.</strong> If h² = 0.5 and S = 10, R = 5 (units = trait units). Direct exam computation.</li>
  <li><strong>Heritability is POPULATION- and ENVIRONMENT-specific.</strong> NOT a property of the trait alone. IQ heritability differs between well-fed and malnourished populations because V_E differs, not because IQ is "more genetic" anywhere.</li>
  <li><strong>Why selection sometimes fails.</strong> If h² ≈ 0 (variation is purely environmental), no response despite strong S.</li>
  <li><strong>Set up for L05 quantitative genetics.</strong> Variance partitioning, breeder's equation, narrow vs. broad heritability.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"High h² means trait is determined by genes" — WRONG. h² describes VARIATION within a population, not the cause of any individual's phenotype.</li>
  <li>"h² = 0 means no genetic basis" — WRONG. Could mean every individual is genetically identical (no V_A) or that V_E is overwhelming.</li>
</ul>`
    },

    "Selection differential (S)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> S = mean of selected breeders − mean of original population. It measures HOW HARD you selected. Combined with h², it predicts evolutionary response: R = h²·S.</p>
<h4>The numbers</h4>
<ul>
  <li>S = (mean of breeders) − (population mean)</li>
  <li>R = h² · S</li>
  <li>R = (next-generation population mean) − (current population mean)</li>
  <li>If S = 5 cm and h² = 0.4, then R = 2 cm</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Quantifies selection strength.</strong> Lets you compare selection across studies — same S, different h², different responses.</li>
  <li><strong>Plug-and-chug exam math.</strong> Robbins likely gives population mean, breeder mean, h² → ask for R or next-gen mean. Memorize the formula.</li>
  <li><strong>Foundation of artificial selection.</strong> Breeders manipulate S directly (choose extreme breeders); h² is a property of the population.</li>
  <li><strong>Connects to fitness differential.</strong> In nature, S emerges from differential survival/reproduction — but the math is identical.</li>
</ol>
<h4>Worked computation</h4>
<ul>
  <li>Population mean weight = 100 g; breeders' mean = 120 g → S = 20 g</li>
  <li>If h² = 0.5, predicted R = 10 g; next-gen mean = 110 g</li>
</ul>`
    },

    "Hypothesis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A HYPOTHESIS is a tentative, testable, FALSIFIABLE explanation — narrow in scope, designed to be proven wrong. Robbins explicitly tests hypothesis-vs-theory distinction.</p>
<h4>Properties of a good hypothesis</h4>
<ul>
  <li>Testable: specifies an observation to make</li>
  <li>Falsifiable: specifies an observation that would PROVE IT WRONG (Popper)</li>
  <li>Specific: narrow in scope</li>
  <li>Tentative: provisional until tested</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinct from "theory."</strong> Theory = broad, well-supported framework. Hypothesis = narrow, testable prediction.</li>
  <li><strong>"Evolution is true" is too vague to be a hypothesis.</strong> "Mosquitoes will evolve resistance to a new pesticide within 5 generations" IS a hypothesis — testable, falsifiable, specific.</li>
  <li><strong>Falsifiability (Popper) is the key.</strong> A claim that can't be disproved by ANY observation isn't scientific.</li>
  <li><strong>Hypotheses derive from theories.</strong> Evolutionary theory generates testable hypotheses about specific organisms, traits, time periods.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Theory" in everyday speech ≠ "theory" in science. Saying evolution is "just a theory" confuses the senses.</li>
  <li>A hypothesis must SPECIFY what would falsify it. "Evolution happens" doesn't.</li>
</ul>`
    },

    "Scientific theory": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A SCIENTIFIC THEORY is a broad, well-supported explanation — NOT a "guess." Evolution, germ theory, atomic theory, plate tectonics — all theories with overwhelming evidence.</p>
<h4>Properties</h4>
<ul>
  <li>Broad explanatory scope</li>
  <li>Supported by large body of independent evidence</li>
  <li>Generates testable hypotheses</li>
  <li>Has survived repeated attempts at falsification</li>
  <li>Unifies many observations under one framework</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Counters the "just a theory" complaint.</strong> In science, "theory" is the strongest tier of explanation. Be ready to rebut this on an essay.</li>
  <li><strong>Other theories at the same tier:</strong> germ theory of disease (Pasteur, Koch), atomic theory of matter, plate tectonics, cell theory, theory of relativity.</li>
  <li><strong>Theory generates hypotheses.</strong> "Evolution by natural selection" is the framework; "mosquitoes will evolve resistance" is a hypothesis derived from it.</li>
  <li><strong>Robbins-bait short answer.</strong> "What's the difference between a hypothesis and a theory?" — be ready.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>Theory ≠ guess. The everyday usage misleads. Evolution is "just a theory" only in the same sense germ theory and atomic theory are.</li>
</ul>`
    },

    "Falsifiability": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Falsifiability (Popper) is the criterion that a SCIENTIFIC CLAIM MUST SPECIFY what would prove it wrong. The Cambrian rabbit is the canonical evolution falsifier.</p>
<h4>The numbers / examples</h4>
<ul>
  <li>Karl Popper formalized falsifiability (1934, The Logic of Scientific Discovery)</li>
  <li>Falsifiers for evolution: a Precambrian rabbit, identical complex organs in unrelated lineages, fundamentally different genetic code, stable allele frequencies under measurable selection</li>
  <li>None ever observed</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinguishes science from pseudoscience.</strong> Astrology, "intelligent design as creationism" claims that fit any data aren't testable — they're not science.</li>
  <li><strong>"Cambrian rabbit" is the J.B.S. Haldane line.</strong> When asked "What would falsify evolution?" — Precambrian mammals would shatter the temporal sequence required by common descent. Memorize this.</li>
  <li><strong>Connects to hypothesis design.</strong> A good hypothesis names what would falsify it — not just what would confirm it.</li>
  <li><strong>Robbins-bait essay.</strong> Be ready to argue evolution IS falsifiable by listing 2–3 specific falsifiers.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"All living things were created perfectly" — unfalsifiable (any imperfection can be re-explained as "optimal trade-off"). Not scientific by Popper's criterion.</li>
  <li>Falsifiability is about what would PROVE WRONG, not what would CONFIRM. Confirmation is easy; refutation criteria are what matter.</li>
</ul>`
    },

    "Darwin's three observations + one inference": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Darwin's logical structure — THREE observations + ONE inference — is the syllogism for natural selection. Each observation is necessary; the conclusion follows.</p>
<h4>The structure (memorize this)</h4>
<ul>
  <li>OBS 1: Heritable variation exists in populations</li>
  <li>OBS 2: More offspring are produced than can survive (overproduction)</li>
  <li>OBS 3: Survival/reproduction is non-random with respect to traits</li>
  <li>INFERENCE: Heritable trait variants associated with higher reproduction increase in frequency over generations → natural selection</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's THE framework Robbins will test.</strong> Be ready to list and explain each piece. Each observation maps to a measurable empirical claim.</li>
  <li><strong>Diagnostic checklist.</strong> When natural selection FAILS to produce evolution, identify which premise is missing.</li>
  <li><strong>Darwin's empirical insight: Malthus.</strong> The overproduction premise (OBS 2) came from Thomas Malthus's 1798 essay on population — Darwin acknowledged the influence directly.</li>
  <li><strong>Necessary AND sufficient.</strong> All three premises are NECESSARY (drop any → conclusion fails); together they're SUFFICIENT to derive natural selection.</li>
</ol>
<h4>What goes wrong if you drop one</h4>
<ul>
  <li>No heritable variation → can't transmit winning traits → no shift across generations</li>
  <li>No overproduction → no scarcity → no differential reproduction</li>
  <li>Random survival → no selection signal at all</li>
</ul>`
    },

    "Falsifiability (Popper)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Karl Popper's criterion: a SCIENTIFIC CLAIM MUST SPECIFY observations that would prove it wrong. This is what separates evolution from "creation" claims.</p>
<h4>The numbers / context</h4>
<ul>
  <li>Karl Popper, The Logic of Scientific Discovery (1934)</li>
  <li>"Evolution is falsifiable" — list of potential falsifiers includes Cambrian rabbit, identical complex organs in unrelated lineages, fundamentally different genetic codes, stable allele frequencies under measured selection</li>
  <li>"Created perfectly" claims are unfalsifiable — any data can be re-described as "intended"</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Demarcates science from pseudoscience.</strong> Popper's criterion is the test: can you specify what would refute the claim?</li>
  <li><strong>Robbins-bait essay topic.</strong> "Why is evolution scientific but creationism is not?" Answer in falsifiability terms.</li>
  <li><strong>Cambrian rabbit (Haldane) is the canonical falsifier.</strong> Memorize the example.</li>
  <li><strong>Demands intellectual honesty.</strong> A scientist must specify what would change their mind. "Evolution would be wrong if X..." should be answerable.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>Falsifiability is about what would PROVE WRONG, not what would CONFIRM. Confirmation is cheap; refutation criteria are the test.</li>
  <li>"Evolution is true / it just is" doesn't satisfy falsifiability. Specifying refutation conditions does.</li>
</ul>`
    }
  });

  /* ============================================================ */
  /* L03 — Genes and Heritable Variation                           */
  /* ============================================================ */
  window.addCardPatches('L03', {
    "Pseudogene": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Pseudogenes are MOLECULAR FOSSILS — broken former genes — and they provide direct evidence of common descent. The GULO pseudogene in primates is canonical.</p>
<h4>The numbers / examples</h4>
<ul>
  <li>Humans have ~14,000–20,000 pseudogenes (more than functional genes by some counts)</li>
  <li>GULO pseudogene: vitamin C synthesis gene, broken in primates AND guinea pigs (independent inactivations)</li>
  <li>Pseudogenes are typically disabled by stop codons, frameshifts, or loss of regulation</li>
  <li>Olfactory receptor pseudogenes: humans have ~400 functional + ~600 pseudogenized — primates have lost smell genes as we became more visual</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strong evidence for common descent.</strong> Why would humans, chimps, gorillas, and orangs all carry the SAME broken GULO gene at the SAME locus with shared inactivating mutations? Only common ancestry explains this.</li>
  <li><strong>Refutes "design" framings.</strong> A designer wouldn't include broken non-functional copies of genes; an evolutionary process inevitably leaves them.</li>
  <li><strong>Sets up genome architecture.</strong> Eukaryotic genomes are mostly NOT functional protein-coding sequence — pseudogenes, repeats, and noncoding DNA dominate.</li>
  <li><strong>Robbins-bait short answer:</strong> "What does the GULO pseudogene tell us about primate evolution?" — be ready with shared ancestry framing.</li>
</ol>`
    },

    "Mobile genetic element (MGE)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> About 45% OF YOUR GENOME is derived from transposable elements — repetitive selfish DNA, not "design." This is a key C-value paradox piece.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>~45% of human genome is from transposons / mobile elements</li>
  <li>~17% LINEs (Long Interspersed Nuclear Elements)</li>
  <li>~11% SINEs (Short Interspersed Nuclear Elements; Alu elements ~10% alone)</li>
  <li>~8% LTR retrotransposons (endogenous retroviruses)</li>
  <li>~3% DNA transposons</li>
  <li>Protein-coding genes: only ~1–2% of genome</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Reveals genome architecture.</strong> Most eukaryotic DNA is REPETITIVE/PARASITIC, not coding. The genome is ecological — selfish elements compete with host control.</li>
  <li><strong>Dispels "complexity = genome size" intuition.</strong> Big genomes (salamander 40× bigger than human) are mostly transposon expansions, not extra information.</li>
  <li><strong>Source of new genes.</strong> Some transposons are domesticated (RAG1/RAG2 in immune system; syncytin in placenta) — became host genes.</li>
  <li><strong>Insertional mutagenesis.</strong> MGE jumps can disrupt or activate genes — source of mutations in cancer and inherited disease.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>C-value paradox</li>
  <li>Pseudogenes (some are processed pseudogenes from retrotransposition)</li>
  <li>Mutation rate (MGE jumps are a class of mutations)</li>
</ul>`
    },

    "C-value paradox": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Genome size DOES NOT correlate with organismal complexity. Salamanders have 40× more DNA than humans. This is THE C-value paradox Robbins flags directly.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Human genome: ~3.2 Gb (gigabases)</li>
  <li>Salamander (Necturus): ~120 Gb (~40× human)</li>
  <li>Lungfish: up to ~130 Gb</li>
  <li>Onion: ~16 Gb (5× human)</li>
  <li>Fugu (pufferfish): ~0.4 Gb (1/8 human)</li>
  <li>Human gene count: ~20,000 — similar to many "simpler" animals</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Robbins explicitly flags this.</strong> The exam-trap line: "genome size does not necessarily correlate with organismal complexity."</li>
  <li><strong>Refutes "more genes = more complex."</strong> Humans have similar gene count to nematodes (~20,000) but vastly different proteomes via alternative splicing.</li>
  <li><strong>Genome size is set by lineage-specific dynamics.</strong> MGE accumulation, recombination rates, effective population size — not "complexity."</li>
  <li><strong>Mukherjee/Lynch hypothesis:</strong> small Ne lets slightly-deleterious extra DNA accumulate → big genomes in vertebrates with small Ne.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>MGEs (most genome-size variation is MGE expansion)</li>
  <li>Alternative splicing (proteome complexity from limited gene count)</li>
  <li>Pseudogenes (junk DNA accumulates over time)</li>
</ul>`
    },

    "DNA methylation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> DNA methylation is PRE-TRANSCRIPTIONAL regulation — adds methyl groups to CpG sites, usually SILENCING transcription. Robbins tests level-of-regulation discrimination.</p>
<h4>The numbers</h4>
<ul>
  <li>Methyl marks added to cytosine in CpG dinucleotides</li>
  <li>~80% of CpG sites in mammals are methylated</li>
  <li>CpG islands at gene promoters are typically UNmethylated (active)</li>
  <li>Methylation persists through cell divisions (heritable epigenetic mark)</li>
  <li>Hyper-methylation of tumor-suppressor promoters is a hallmark of cancer</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Pre-transcriptional level.</strong> Methylation controls whether a gene is even ACCESSIBLE — it acts BEFORE RNA polymerase binds. Don't confuse with post-transcriptional miRNA.</li>
  <li><strong>Mechanism: methyl groups + chromatin compaction.</strong> Methylated CpGs recruit MBD proteins → recruit HDACs → chromatin compaction → no transcription.</li>
  <li><strong>X-inactivation, imprinting, cancer silencing</strong> all involve methylation. It's the master pre-transcriptional regulator.</li>
  <li><strong>Heritable across cell divisions.</strong> Daughter cells inherit methylation patterns — explaining stable cell-type identity.</li>
</ol>
<h4>vs. miRNA (the key discrimination)</h4>
<ul>
  <li>Methylation = PRE-transcriptional (controls gene access)</li>
  <li>miRNA = POST-transcriptional (degrades mRNA after it's made)</li>
  <li>Both repress; different LEVELS of action — Robbins-bait</li>
</ul>`
    },

    "Histone modification": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Histone modifications (acetylation, methylation) ALTER CHROMATIN packing — pre-transcriptional regulation. HDAC inhibitors are a classic exam scenario.</p>
<h4>The numbers / mechanisms</h4>
<ul>
  <li>4 core histones: H2A, H2B, H3, H4 (octamer = 2 of each)</li>
  <li>147 bp DNA wrapped around each octamer = nucleosome</li>
  <li>Modifications on histone N-terminal "tails": acetylation, methylation, phosphorylation, ubiquitination</li>
  <li>Acetylation (HAT enzymes) — typically OPENS chromatin (active)</li>
  <li>Deacetylation (HDAC enzymes) — typically CLOSES chromatin (silent)</li>
  <li>Methylation can activate (H3K4) or repress (H3K27) depending on residue</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Pre-transcriptional regulation.</strong> Like DNA methylation, histone marks control gene ACCESS before transcription.</li>
  <li><strong>HDAC inhibitor exam scenario.</strong> Block deacetylation → acetyl marks accumulate → chromatin opens → transcription INCREASES genome-wide. Used as anticancer drugs.</li>
  <li><strong>Histone code hypothesis.</strong> Combinations of histone marks act as a "code" specifying chromatin state — read by reader proteins.</li>
  <li><strong>Heritable through mitosis.</strong> Like DNA methylation, histone marks can persist across cell divisions, explaining cell-type stability.</li>
</ol>
<h4>Memory aid</h4>
<ul>
  <li>HAT writes acetyl → chromatin OPEN → transcription ON</li>
  <li>HDAC erases acetyl → chromatin CLOSED → transcription OFF</li>
</ul>`
    },

    "MicroRNA (miRNA)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> miRNAs are POST-TRANSCRIPTIONAL regulators — small RNAs that bind mature mRNAs to suppress translation or trigger degradation. Don't confuse with pre-transcriptional methylation.</p>
<h4>The numbers</h4>
<ul>
  <li>~22 nt long (mature form)</li>
  <li>Humans express ~2,500 miRNAs</li>
  <li>Each miRNA targets dozens to hundreds of mRNAs</li>
  <li>miRNAs regulate ~60% of human protein-coding genes</li>
  <li>Bind 3' UTR via partial complementarity (seed match: 6–8 nt)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>POST-transcriptional level — Robbins-bait.</strong> The mRNA is already made; miRNA acts on the mature transcript. Methylation acts BEFORE transcription. Don't mix them up.</li>
  <li><strong>Mechanism: RISC complex.</strong> miRNA + Argonaute proteins → RISC → binds mRNA → block translation OR cleave the mRNA.</li>
  <li><strong>Massively parallel regulation.</strong> One miRNA can fine-tune hundreds of transcripts simultaneously — major driver of network-level gene expression.</li>
  <li><strong>Cancer relevance.</strong> miRNAs targeting oncogenes act as tumor suppressors; loss of miRNA = oncogene overexpression.</li>
</ol>
<h4>vs. methylation (the key discrimination)</h4>
<ul>
  <li>miRNA = POST-transcriptional (acts on mRNA)</li>
  <li>Methylation = PRE-transcriptional (acts on DNA)</li>
  <li>Both repress; different LEVELS</li>
</ul>`
    },

    "Alternative splicing": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Alternative splicing produces MULTIPLE PROTEIN ISOFORMS from a single gene by combining exons differently — POST-TRANSCRIPTIONAL regulation. Dscam holds the record.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Drosophila Dscam: 38,016 possible mRNA isoforms from 1 gene</li>
  <li>~95% of multi-exon human genes undergo alternative splicing</li>
  <li>Human genome: ~20,000 genes → ~100,000+ proteins (via splicing)</li>
  <li>Spliceosome: 5 snRNAs + ~150 proteins</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Demolishes "gene count = proteome size" assumption.</strong> Humans have similar gene counts to worms but vastly more protein diversity via splicing.</li>
  <li><strong>POST-transcriptional regulation.</strong> Acts on pre-mRNA after transcription, before translation. Don't confuse with methylation (pre-T) or post-translational modifications.</li>
  <li><strong>Tissue specificity.</strong> Many genes have tissue-specific splice forms — explains how the same gene serves different roles in different cell types.</li>
  <li><strong>Disease relevance.</strong> ~15% of disease-causing mutations affect splicing. Splicing factors are cancer hotspots.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>C-value paradox (proteome complexity not bounded by gene count)</li>
  <li>Levels of regulation (post-transcriptional)</li>
</ul>`
    },

    "Allele": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> An ALLELE is a specific variant of a gene at a given locus. Alleles are what allele-frequency math operates on — the fundamental population-genetic unit.</p>
<h4>The numbers / examples</h4>
<ul>
  <li>Diploid individual: 2 alleles per locus (one per chromosome)</li>
  <li>Population at biallelic locus: many copies of two alleles (A and a)</li>
  <li>Multi-allelic loci (ABO blood group): 3 main alleles (I^A, I^B, i)</li>
  <li>HLA loci: hundreds of alleles in human populations</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The unit of population genetics.</strong> Allele frequencies (p, q) are the fundamental quantities; everything reduces to "how do allele frequencies change?"</li>
  <li><strong>Distinct from gene.</strong> A GENE is a locus; ALLELES are variants AT that locus. Don't conflate.</li>
  <li><strong>Distinct from genotype.</strong> A GENOTYPE is a combination of alleles at a locus (AA, Aa, aa). Allele frequencies and genotype frequencies are related (HWE) but distinct.</li>
  <li><strong>ABO blood-group example.</strong> I^A and I^B are CODOMINANT (both expressed in heterozygote), i is RECESSIVE. Memorize for dominance discriminations.</li>
</ol>`
    },

    "Dominant": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> DOMINANT alleles are FULLY EXPRESSED in heterozygotes. Beneficial dominants spread fast; deleterious dominants are eliminated fast. Robbins tests dominance vs. recessive selection efficiency.</p>
<h4>The numbers</h4>
<ul>
  <li>Dominant beneficial allele at frequency q: increases at rate ≈ q·s per generation</li>
  <li>Dominant deleterious allele: eliminated nearly in one generation if expressed pre-reproductively</li>
  <li>Huntington's disease (HD): dominant; persists because onset is post-reproductive (~40s)</li>
  <li>Achondroplasia (dwarfism): dominant; new mutations balance loss</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Selection efficiency depends on dominance.</strong> Beneficial dominants spread fast (every Aa expresses them). Beneficial recessives spread slowly (most copies hide in Aa).</li>
  <li><strong>Deleterious dominants are purged fast.</strong> Unless onset is late (Huntington's). Selection sees every copy.</li>
  <li><strong>Mode of dominance:</strong> CLASSICAL dominance (full expression in Aa), CODOMINANCE (both alleles expressed, e.g., AB blood type), INCOMPLETE (Aa intermediate).</li>
  <li><strong>Common exam discrimination:</strong> "How does selection efficiency differ for dominant vs. recessive beneficial alleles when rare?" — Dominant fast (Δp ≈ pqs), recessive slow (Δp ≈ pq²s).</li>
</ol>`
    },

    "Recessive": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> RECESSIVE alleles are HIDDEN in heterozygotes — only expressed in aa. Beneficial recessives spread SLOWLY when rare; deleterious recessives PERSIST when rare. Hardy-Weinberg explains both.</p>
<h4>The numbers</h4>
<ul>
  <li>At allele frequency q, fraction in homozygotes = q²; fraction in heterozygotes = 2pq</li>
  <li>When q is small: q² &lt;&lt; 2pq — most copies are hidden</li>
  <li>q = 0.01: q² = 0.0001 (0.01% homozygotes); 2pq ≈ 0.0198 (~2% carriers) — ~200× more carriers than affected</li>
  <li>Cystic fibrosis (NW Europe): q ≈ 0.02; q² ≈ 1/2,500; carriers ≈ 1/25</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Selection on rare recessives is INEFFICIENT.</strong> Most copies hide in heterozygotes, invisible to selection. Δq scales with q² when rare.</li>
  <li><strong>Why deleterious recessives persist.</strong> They sit in carriers without harming anyone — only homozygotes (q²) suffer. Hard to eliminate completely.</li>
  <li><strong>Why beneficial recessives spread slowly initially.</strong> Until q rises enough that q² is non-trivial, the trait is rarely expressed.</li>
  <li><strong>Heterozygote-advantage exception.</strong> Sickle-cell (HbS) is recessive for disease but heterozygotes have malaria resistance — keeps q at ~0.1 in malaria zones.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Selection eliminates rare recessives quickly" — WRONG. Slowly. Most copies hide.</li>
  <li>Carrier frequency vastly exceeds affected frequency for rare recessives.</li>
</ul>`
    },

    "Additive": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> ADDITIVE alleles each contribute INCREMENTALLY — phenotype scales LINEARLY with allele dose. Additive variance (V_A) is the only variance that responds predictably to selection. Sets up L05.</p>
<h4>The numbers</h4>
<ul>
  <li>Additive: AA = a, Aa = a/2 (intermediate), aa = 0 — linear dose-response</li>
  <li>V_A: portion of genetic variance that's predictably heritable</li>
  <li>h² = V_A / V_P (narrow-sense heritability)</li>
  <li>R = h² · S — only additive variance produces predictable response to selection</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Predicts response to selection.</strong> Only additive effects pass faithfully from parents to offspring; dominance and epistatic effects depend on which alleles meet which.</li>
  <li><strong>Continuous-trait basis.</strong> Many additive loci → Central Limit Theorem → bell-curve trait distribution. Height is a textbook example.</li>
  <li><strong>vs. dominant and recessive.</strong> Dominant: Aa = AA. Recessive: Aa = aa. Additive: Aa = (AA + aa)/2 — the linear case.</li>
  <li><strong>Sets up L05 quantitative genetics.</strong> Variance partitioning, breeder's equation all hinge on additive vs. non-additive variance.</li>
</ol>
<h4>vs. codominant</h4>
<ul>
  <li>Additive: linear dose-response (Aa is INTERMEDIATE)</li>
  <li>Codominant: BOTH allele phenotypes visible in Aa (e.g., AB blood type — both A and B antigens)</li>
  <li>Often confused; not the same thing</li>
</ul>`
    },

    "Locus": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A LOCUS is the chromosomal LOCATION of a gene. Different loci evolve INDEPENDENTLY — the basis of multi-gene inheritance and recombination.</p>
<h4>The numbers</h4>
<ul>
  <li>Human genome: ~20,000 protein-coding loci across 23 chromosome pairs</li>
  <li>Loci on different chromosomes: independent assortment (Mendel's Second Law)</li>
  <li>Loci on same chromosome: linked, but recombine via crossing over</li>
  <li>Recombination frequency = genetic distance (1 cM ≈ 1% recombination)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The basis of independent inheritance.</strong> Each locus has its own allele frequencies, mutation history, selection regime — they evolve separately (modulo linkage).</li>
  <li><strong>Sets up recombination.</strong> Loci are reshuffled each generation; new combinations are generated. Without recombination (asexual lineages), loci can't escape unfavorable backgrounds.</li>
  <li><strong>Enables independent specialization.</strong> Hemoglobin α and β arose by gene duplication, then diverged at separate loci. If they were one locus, they couldn't differentiate.</li>
  <li><strong>QTL mapping = locus identification.</strong> Quantitative Trait Loci — finding which loci contribute to a trait — depends on the locus concept.</li>
</ol>
<h4>vs. allele</h4>
<ul>
  <li>Locus = address (where on the chromosome)</li>
  <li>Allele = variant at that address</li>
  <li>Don't confuse: the gene IS the locus; alleles are variants of it</li>
</ul>`
    },

    "Mutation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutation is the ULTIMATE source of new alleles — point mutations, indels, duplications, inversions, etc. Random with respect to fitness. Robbins-bait.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Point mutation rate: ~10⁻⁸ to 10⁻⁹ per base per generation in mammals</li>
  <li>Per individual per generation: ~70 new mutations in humans</li>
  <li>Most mutations are NEUTRAL or slightly deleterious</li>
  <li>Beneficial mutations: rare, perhaps 1 in 10⁶ mutations (varies wildly with environment)</li>
  <li>Categories: SNPs (point), indels, CNVs (copy-number), translocations, inversions</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The ONLY source of new genetic variation.</strong> Selection sorts existing alleles; mutation creates them. Without mutation, evolution stalls.</li>
  <li><strong>Random with respect to fitness.</strong> Mutations don't appear because they would be useful. Luria-Delbrück 1943 proved this experimentally.</li>
  <li><strong>Somatic vs. germline.</strong> Only germline mutations are heritable. Somatic mutations cause cancer but die with you.</li>
  <li><strong>Rate sets adaptation speed.</strong> HIV's high RT mutation rate (~10⁻⁴) explains rapid drug resistance.</li>
</ol>
<h4>Robbins-bait</h4>
<ul>
  <li>"Antibiotics cause bacteria to mutate" — WRONG. Antibiotics SELECT pre-existing variants.</li>
</ul>`
    },

    "Mutation rate": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutation rate (~10⁻⁸ to 10⁻⁹ per base per generation in mammals) sets the SUPPLY of new variation. Fast-evolving viruses have rates 10,000× higher.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mammals: ~10⁻⁸ to 10⁻⁹ per base per generation</li>
  <li>Bacteria: ~10⁻⁹ to 10⁻¹⁰ per base per generation</li>
  <li>RNA viruses (HIV): ~10⁻⁴ to 10⁻⁵ per base per replication</li>
  <li>Per genome per individual per generation in humans: ~70 new mutations</li>
  <li>Eukaryotic genome size × mutation rate per base = total mutational input</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Sets adaptation speed.</strong> Higher μ → faster supply of beneficial variants → faster adaptation under strong selection. Why HIV evolves drug resistance fast.</li>
  <li><strong>Mutation-selection balance.</strong> Equilibrium frequency of deleterious alleles ≈ μ/s — directly proportional to mutation rate.</li>
  <li><strong>Mutation-limited evolution.</strong> If beneficial mutations are too rare, populations can't adapt fast enough. Common in small populations and slow-mutating species.</li>
  <li><strong>Rate is itself evolved.</strong> Selection on mutator alleles tunes the rate — too low → no innovation, too high → mutational meltdown.</li>
</ol>
<h4>Connects to</h4>
<ul>
  <li>Random with respect to fitness</li>
  <li>Drug resistance evolution (combination therapy works because P(several mutations together) = μ^n)</li>
</ul>`
    },

    "Random with respect to fitness": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutations DON'T preferentially produce useful alleles — they're directionally random. Luria-Delbrück 1943 is THE canonical experiment Robbins may test.</p>
<h4>The numbers / experiments</h4>
<ul>
  <li>Luria-Delbrück fluctuation test (1943): E. coli + bacteriophage T1 resistance</li>
  <li>If mutations INDUCED by phage → similar resistant counts across cultures (Poisson distribution)</li>
  <li>Observed: huge variance across cultures (Luria distribution) → mutations arose SPONTANEOUSLY</li>
  <li>Won Luria the 1969 Nobel Prize in Physiology or Medicine</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinguishes Darwinian from Lamarckian thinking.</strong> Lamarck: need induces adaptation. Darwin: random variation, then selection. Mutations are NOT directed.</li>
  <li><strong>The "antibiotic exposure causes mutation" trap.</strong> Wrong. Antibiotics SELECT pre-existing variants. Robbins-bait.</li>
  <li><strong>Luria-Delbrück is named-experiment territory.</strong> Be ready to describe the fluctuation test in 1–2 sentences.</li>
  <li><strong>Doesn't mean uniform per-base.</strong> Mutation hotspots, stress-induced rate elevation exist — the claim is about FITNESS DIRECTION, not uniform probability.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>"Stress increases mutation rate, therefore mutations are non-random" — these are different claims. Rate elevation is real; fitness-direction randomness still holds.</li>
  <li>"Bacteria evolved resistance because of antibiotic exposure" — phrase carefully. They evolved resistance from random pre-existing variants selected by exposure.</li>
</ul>`
    }
  });

  /* ============================================================ */
  /* L04 — Hardy-Weinberg Equilibrium                              */
  /* ============================================================ */
  window.addCardPatches('L04', {
    "Allele frequency": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Allele frequency = the proportion of all gene copies in a population that are a given allele. p + q = 1 for a biallelic locus. The fundamental population-genetics quantity.</p>
<h4>The numbers / formulas</h4>
<ul>
  <li>p = freq(A), q = freq(a); p + q = 1</li>
  <li>p = (2·N_AA + N_Aa) / (2·N_total)</li>
  <li>q = (2·N_aa + N_Aa) / (2·N_total) = 1 − p</li>
  <li>Each AA contributes 2 A alleles; each Aa contributes 1 A + 1 a; each aa contributes 2 a</li>
  <li>Diploid pop of N: total allele copies = 2N</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Plug-and-chug exam staple.</strong> Robbins will give you genotype counts → ask for p. Memorize the formula.</li>
  <li><strong>The unit of evolution.</strong> Evolution = change in allele frequencies. Without computing them, you can't quantify evolution.</li>
  <li><strong>Different from genotype frequency.</strong> Two populations can have identical p but very different genotype distributions (e.g., due to inbreeding).</li>
  <li><strong>Foundation for HWE.</strong> Hardy-Weinberg predicts genotype frequencies (p², 2pq, q²) FROM allele frequencies under random mating.</li>
</ol>
<h4>Worked computation</h4>
<ul>
  <li>100 individuals: 16 AA, 48 Aa, 36 aa</li>
  <li>A copies = 2(16) + 1(48) = 80</li>
  <li>p = 80 / 200 = 0.4 (and q = 0.6)</li>
</ul>`
    },

    "Genotype frequency": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Genotype frequency = proportion of individuals with a given genotype (AA, Aa, aa). Sum to 1. Sensitive to mating system in a way allele frequencies aren't.</p>
<h4>The numbers / formulas</h4>
<ul>
  <li>f(AA) + f(Aa) + f(aa) = 1</li>
  <li>Under HWE: f(AA) = p², f(Aa) = 2pq, f(aa) = q²</li>
  <li>Inbreeding: f(AA) = p² + Fpq, f(Aa) = 2pq(1 − F), f(aa) = q² + Fpq</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>HWE expectations are GENOTYPE frequencies.</strong> p², 2pq, q² are GENOTYPE frequencies derived from allele frequencies under random mating.</li>
  <li><strong>Sensitive to mating system.</strong> Inbreeding raises homozygosity (more AA + aa, fewer Aa) without changing allele frequencies.</li>
  <li><strong>Diagnostic of evolutionary forces.</strong> Excess homozygotes → inbreeding or Wahlund. Excess heterozygotes → heterozygote advantage. The patterns tell you which force is acting.</li>
  <li><strong>Distinct from allele frequency.</strong> Allele freq tells you "what's in the gene pool"; genotype freq tells you "how alleles are paired in individuals."</li>
</ol>
<h4>Worked computation</h4>
<ul>
  <li>16 AA, 48 Aa, 36 aa out of 100 individuals</li>
  <li>f(AA) = 0.16, f(Aa) = 0.48, f(aa) = 0.36 — sum = 1.0 ✓</li>
</ul>`
    },

    "Hardy-Weinberg equilibrium (HWE)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> HWE is THE NULL MODEL of population genetics — predicts p², 2pq, q² genotype frequencies under no evolution. Deviations diagnose which evolutionary force is acting. Robbins will math-grade this hard.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>HWE equation: p² + 2pq + q² = 1</li>
  <li>FIVE assumptions: (1) no mutation, (2) no migration/gene flow, (3) infinite population (no drift), (4) no selection, (5) random mating</li>
  <li>HWE achieved in ONE generation of random mating from any starting genotype frequencies</li>
  <li>Allele frequencies don't change under random mating (only genotype frequencies redistribute)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The null hypothesis of pop-gen.</strong> If observed = HWE expected, you can't conclude evolution is absent — you can only fail to reject the null. If observed ≠ expected, at least one assumption is violated.</li>
  <li><strong>Diagnostic deviations:</strong> Excess homozygotes → inbreeding/Wahlund. Excess heterozygotes → heterozygote advantage. Allele-freq drift → selection or random drift.</li>
  <li><strong>Computational backbone of L04.</strong> Robbins will give genotype counts → ask for HWE expected → ask if it fits → identify violation.</li>
  <li><strong>One generation suffices to reach HWE.</strong> Even if starting genotype frequencies are weird, random mating snaps to p², 2pq, q² in ONE generation.</li>
</ol>
<h4>The 5 assumptions (memorize this list)</h4>
<ul>
  <li>1. No mutation</li>
  <li>2. No migration / gene flow</li>
  <li>3. Infinite N (no drift)</li>
  <li>4. No selection</li>
  <li>5. Random mating</li>
</ul>`
    },

    "Random mating (panmixia)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Panmixia = every individual is equally likely to mate with every other, regardless of genotype. The 5th HWE assumption. Sexual selection violates it.</p>
<h4>The numbers / requirements</h4>
<ul>
  <li>Required for HWE assumption #5</li>
  <li>Mating must be CHOICE-BLIND with respect to genotype</li>
  <li>Violations: assortative mating, sexual selection, inbreeding, Wahlund effect (population subdivision)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>One of the 5 HWE assumptions.</strong> Violation → genotype frequencies deviate from p², 2pq, q² even without selection or drift.</li>
  <li><strong>Different deviation patterns:</strong>
    <ul>
      <li>Inbreeding (mate with relatives): excess homozygotes</li>
      <li>Disassortative mating (mate with opposite genotypes): excess heterozygotes</li>
      <li>Sexual selection (peahens choose long-tailed peacocks): allele frequencies SHIFT</li>
    </ul>
  </li>
  <li><strong>Real populations rarely panmix.</strong> Most have geographic structure, mate preferences, kin recognition. HWE is the null even when violated.</li>
  <li><strong>Sexual selection ≠ random mating.</strong> Robbins likely tests this with a peacock/peahen scenario.</li>
</ol>`
    },

    "Inbreeding": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Inbreeding = mating between RELATIVES. Raises HOMOZYGOSITY without changing allele frequencies. Exposes deleterious recessives → INBREEDING DEPRESSION.</p>
<h4>The numbers / formulas</h4>
<ul>
  <li>Inbreeding coefficient F: probability the two alleles at a locus are identical by descent</li>
  <li>F = 0 → random mating; F = 1 → fully inbred</li>
  <li>Genotype frequencies under inbreeding: f(AA) = p² + Fpq, f(Aa) = 2pq(1 − F), f(aa) = q² + Fpq</li>
  <li>Self-fertilization: F doubles each generation toward 1</li>
  <li>Sibling mating: F = 0.25 per generation</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Raises homozygosity, NOT allele frequencies.</strong> A common exam trap. Inbreeding redistributes genotype frequencies; allele frequencies don't change.</li>
  <li><strong>Exposes deleterious recessives → inbreeding depression.</strong> Hidden recessives (in heterozygotes) become homozygous and expressed. Reduces fitness, fertility, viability.</li>
  <li><strong>Conservation relevance.</strong> Florida panther had severe inbreeding (heart, reproductive issues); Texas puma genetic rescue restored fitness. (L17.)</li>
  <li><strong>Diagnostic of HWE deviation.</strong> Observed homozygote excess + reduced heterozygosity → suspect inbreeding (or Wahlund effect).</li>
</ol>
<h4>vs. Wahlund effect</h4>
<ul>
  <li>Both produce APPARENT homozygote excess</li>
  <li>Inbreeding: real, within-population mating between relatives</li>
  <li>Wahlund: artifact of pooling distinct subpopulations</li>
  <li>Distinguish by checking spatial structure (compute F_ST)</li>
</ul>`
    },

    "Heterozygote advantage": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> When Aa is FITTER than both AA and aa, BOTH alleles are maintained at intermediate frequencies. Sickle-cell + malaria is THE textbook example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Sickle-cell allele HbS: ~10% in some West African populations</li>
  <li>HbA/HbA: dies of malaria at high rates</li>
  <li>HbA/HbS: malaria resistance + only mild sickle trait → highest fitness</li>
  <li>HbS/HbS: dies of sickle-cell anemia (~4–5% of African children before treatment)</li>
  <li>Equilibrium allele frequency: q* = s_AA / (s_AA + s_aa) where s's are selection coefficients</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Maintains balanced polymorphism.</strong> Both alleles persist indefinitely instead of one fixing.</li>
  <li><strong>Explains "why deleterious alleles persist."</strong> The HbS allele kills homozygotes — but heterozygote advantage in malarial environments keeps it at ~10%.</li>
  <li><strong>HWE deviation pattern: EXCESS HETEROZYGOTES.</strong> Observed Aa &gt; 2pq expected.</li>
  <li><strong>Geographic correlation.</strong> HbS frequency mirrors malaria distribution — direct evidence of selection. Where malaria isn't endemic, HbS drops to near-zero.</li>
</ol>
<h4>Other examples</h4>
<ul>
  <li>CFTR (cystic fibrosis carrier) + cholera/typhoid resistance (debated)</li>
  <li>Tay-Sachs heterozygotes + tuberculosis resistance (debated)</li>
  <li>G6PD deficiency + malaria resistance (well-established)</li>
</ul>`
    },

    "Wahlund effect": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Pooling distinct subpopulations with different allele frequencies produces an APPARENT excess of homozygotes — even if each subpopulation is internally in HWE. Easily confused with inbreeding.</p>
<h4>The numbers / mechanism</h4>
<ul>
  <li>Subpop A: p = 0.9 → expected genotypes 0.81 / 0.18 / 0.01</li>
  <li>Subpop B: p = 0.1 → expected genotypes 0.01 / 0.18 / 0.81</li>
  <li>Pooled: average p = 0.5 → expected (under HWE on pool) = 0.25 / 0.50 / 0.25</li>
  <li>Pooled OBSERVED: 0.41 / 0.18 / 0.41 (just averaged) — apparent EXCESS homozygotes (0.82 vs 0.50 expected)</li>
  <li>Math: pooled heterozygosity = 2 p̄ q̄ − 2·Var(p) — variance in p REDUCES heterozygosity</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Trap for unwary samplers.</strong> If you pool fish from two different ponds and treat as one population, the data look "inbred" — but the inbreeding is illusory.</li>
  <li><strong>Distinguishes from real inbreeding.</strong> Compute F_ST (variance among subpopulations) to detect Wahlund. Sample subpops separately to confirm each is in internal HWE.</li>
  <li><strong>Robbins-bait scenario.</strong> "A biologist samples fish from two ponds combined. Observed homozygote excess. Inbreeding or population subdivision?" — answer: probably Wahlund.</li>
  <li><strong>Common in cryptic species.</strong> If two species are mistakenly pooled, Wahlund signature appears at every locus.</li>
</ol>
<h4>vs. inbreeding</h4>
<ul>
  <li>Both: excess homozygotes</li>
  <li>Inbreeding: real, mating between relatives within a population</li>
  <li>Wahlund: artifact of pooling distinct populations</li>
  <li>Diagnose: spatial sampling + F_ST analysis</li>
</ul>`
    },

    "p² + 2pq + q² = 1 — what each term means": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> p² = AA, 2pq = Aa, q² = aa. THE Hardy-Weinberg equation. Robbins will math-grade this.</p>
<h4>The numbers / formulas</h4>
<ul>
  <li>p² = expected frequency of homozygous AA</li>
  <li>2pq = expected frequency of heterozygous Aa (×2 because A from mother + a from father OR a from mother + A from father)</li>
  <li>q² = expected frequency of homozygous aa</li>
  <li>p + q = 1; p² + 2pq + q² = (p + q)² = 1 — perfect square</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Plug-and-chug exam math.</strong> Given p, compute three genotype frequencies. Given genotype counts, compute p, then expected, then compare.</li>
  <li><strong>The "why 2pq" intuition.</strong> Heterozygotes can be made two ways (A·a or a·A) — the factor of 2 is combinatorial.</li>
  <li><strong>Foundation for detecting violations.</strong> Compute expected; compare to observed; deviations diagnose force.</li>
  <li><strong>Worked example:</strong> p = 0.7 → AA = 0.49, Aa = 0.42, aa = 0.09; sum = 1.00 ✓</li>
</ol>
<h4>Memory aid</h4>
<ul>
  <li>"Pure-A · A-and-q heterozygotes · pure-q" = p² + 2pq + q²</li>
</ul>`
    },

    "Five HWE assumptions (the disequilibrium menu)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The FIVE HWE assumptions are the menu of evolutionary forces — violation of any one drives a population AWAY from HWE. Memorize this list cold.</p>
<h4>The five (memorize these)</h4>
<ul>
  <li>1. No MUTATION</li>
  <li>2. No MIGRATION / gene flow</li>
  <li>3. Infinite N (no DRIFT)</li>
  <li>4. No SELECTION</li>
  <li>5. RANDOM MATING (panmixia)</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the syllabus.</strong> The four mechanisms (mutation, migration, drift, selection) are violations 1–4. Random mating is the 5th separate assumption.</li>
  <li><strong>Each violation produces distinct deviations:</strong>
    <ul>
      <li>Selection: allele freq shifts directionally; genotype frequencies skew</li>
      <li>Drift: allele freq drifts randomly; small populations only</li>
      <li>Mutation: slow allele freq input; usually weak relative to other forces</li>
      <li>Migration: allele freq converges across populations</li>
      <li>Non-random mating: allele freq unchanged but genotype freq distorted (more homozygotes for inbreeding)</li>
    </ul>
  </li>
  <li><strong>Diagnostic checklist.</strong> Given an HWE deviation, identify which assumption is violated. Robbins-bait.</li>
  <li><strong>Mnemonic: MM-DSR.</strong> Mutation, Migration, Drift, Selection, Random mating.</li>
</ol>`
    },

    "Computing p from genotype counts": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> p = (2·N_AA + N_Aa) / (2·N_total). The plug-and-chug formula every population-genetics exam uses.</p>
<h4>The numbers / formula</h4>
<ul>
  <li>Each AA contributes 2 A alleles</li>
  <li>Each Aa contributes 1 A allele</li>
  <li>Each aa contributes 0 A alleles</li>
  <li>Total alleles in pop of N diploids = 2N</li>
  <li>p = total A copies / total allele copies</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The most common pop-gen exam computation.</strong> Robbins gives genotype counts → first step is computing p. Get this and you can do everything else (HWE expected, deviation tests, etc.).</li>
  <li><strong>Don't confuse with genotype frequencies.</strong> Genotype freq (f(AA), f(Aa), f(aa)) sum to 1 over individuals. Allele freq sums to 1 over allele copies (2 per individual).</li>
  <li><strong>Heterozygotes split.</strong> Each Aa contributes 1 A AND 1 a — count each individual's contribution to BOTH allele tallies.</li>
  <li><strong>Worked example:</strong> 100 fish: 36 AA, 48 Aa, 16 aa → A copies = 72 + 48 = 120; p = 120/200 = 0.6.</li>
</ol>
<h4>Common arithmetic slips</h4>
<ul>
  <li>Forgetting heterozygotes contribute to BOTH p and q tallies</li>
  <li>Using individual counts instead of allele counts (off by factor of 2)</li>
</ul>`
    },

    "Rare recessive disease → allele frequency": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> For rare recessive diseases, q ≈ √(disease frequency); carrier frequency ≈ 2pq. Carriers VASTLY OUTNUMBER affected. Cystic fibrosis is the canonical example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Cystic fibrosis (NW Europeans): disease freq ≈ 1/2,500</li>
  <li>q² = 1/2,500 → q = 1/50 = 0.02</li>
  <li>Carrier freq = 2pq = 2(0.98)(0.02) ≈ 0.039 = 1/25</li>
  <li>~100× more carriers than affected</li>
  <li>Tay-Sachs (Ashkenazi Jews): disease freq ≈ 1/3,600 → q ≈ 0.017 → carrier ≈ 1/30</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Plug-and-chug genetic counseling math.</strong> Given disease frequency, compute carrier frequency in one step. Robbins will likely test this.</li>
  <li><strong>Why deleterious recessives persist.</strong> Most copies hide in carriers, invisible to selection. q² is small; 2pq is huge.</li>
  <li><strong>Hardy-Weinberg in clinical genetics.</strong> Used routinely to estimate carrier frequencies for genetic screening.</li>
  <li><strong>Memorize the shortcut.</strong> q ≈ √(rare-disease-freq); 2pq ≈ 2q (since p ≈ 1 when q is small).</li>
</ol>
<h4>Worked computation</h4>
<ul>
  <li>Disease 1/10,000 → q² = 1/10,000 → q = 0.01 → carrier ≈ 2(0.99)(0.01) = 0.0198 ≈ 1/50</li>
</ul>`
    },

    "X-linked Hardy-Weinberg": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Males are HEMIZYGOUS for X — they show recessives at frequency q (not q²). Disease vastly more common in males. Color blindness is canonical.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Males: hemizygous, 1 X copy → recessive expressed at q</li>
  <li>Females: 2 X copies → recessive expressed at q² (same as autosomal)</li>
  <li>Color blindness q ≈ 0.08; males ~8% affected; females ~0.64%; ratio ~12.5×</li>
  <li>Hemophilia A: males ~1/5,000; females ~1/25 million</li>
  <li>Duchenne muscular dystrophy: males ~1/3,500; females extremely rare</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Explains sex bias in genetic disease.</strong> X-linked recessives hit males far more often — a quantitative HWE prediction.</li>
  <li><strong>Cheap allele exposure.</strong> Males get the rare allele "cheap" — only need one copy to express. Females need two (q²).</li>
  <li><strong>Ratio increases with rarity.</strong> q = 0.01 → 100× male:female ratio. Rarer = more skewed.</li>
  <li><strong>Plug-and-chug pedigree exam item.</strong> Given disease male frequency, infer q, predict female frequency.</li>
</ol>
<h4>Worked computation</h4>
<ul>
  <li>X-linked recessive q = 0.05</li>
  <li>Males affected: 0.05 = 5%</li>
  <li>Females affected: q² = 0.0025 = 0.25%</li>
  <li>Ratio: 5/0.25 = 20×</li>
</ul>`
    },

    "Inbreeding coefficient (F)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> F = probability that the two alleles at a locus are IDENTICAL BY DESCENT. F = 0 → random mating; F = 1 → fully inbred. Quantifies departure from HWE due to non-random mating.</p>
<h4>The numbers / formulas</h4>
<ul>
  <li>F = (H_expected − H_observed) / H_expected</li>
  <li>Genotype frequencies under inbreeding: f(AA) = p² + Fpq, f(Aa) = 2pq(1 − F), f(aa) = q² + Fpq</li>
  <li>Selfing: F starts at 0, doubles toward 1 each generation (1, 0.5, 0.75, 0.875, ...)</li>
  <li>Sibling mating: F per generation = 1/4</li>
  <li>Cousin mating: F = 1/16</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Quantifies inbreeding rigorously.</strong> F &gt; 0 raises homozygosity above HWE. The math lets you predict expected genotype frequencies in self-fertilizing or cousin-mating populations.</li>
  <li><strong>Inbreeding depression scales with F.</strong> Every increase in F exposes more deleterious recessives → fitness cost proportional to F.</li>
  <li><strong>Pedigrees give F directly.</strong> First cousins F = 1/16; full siblings F = 1/4; parent-offspring F = 1/4.</li>
  <li><strong>Population-level F (F_IS, F_ST).</strong> Distinguishes within-population inbreeding (F_IS) from population subdivision (F_ST). Connects to Wahlund effect.</li>
</ol>
<h4>Common exam traps</h4>
<ul>
  <li>F doesn't change allele frequencies — only genotype frequencies. The allele pool is the same; just paired differently.</li>
</ul>`
    },

    "One generation of random mating restores HWE": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> From any starting genotype frequencies, ONE generation of random mating produces HWE proportions p², 2pq, q². The "memory" of past distributions is wiped instantly. Counterintuitive but exam-tested.</p>
<h4>The numbers / mechanism</h4>
<ul>
  <li>Allele frequencies don't change under random mating</li>
  <li>Genotype frequencies redistribute to p², 2pq, q² in 1 generation (no time decay)</li>
  <li>Why: each new offspring's genotype is from independent gamete sampling at frequencies p and q</li>
  <li>Worked example: starting 80% AA, 20% aa, 0% Aa with p = 0.8 → after 1 random-mating round: 0.64 AA, 0.32 Aa, 0.04 aa</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Explains why HWE is the null model.</strong> Random mating is so powerful at redistributing genotypes that any non-evolution population should be at HWE.</li>
  <li><strong>Counterintuitive instant snap.</strong> Most equilibria approach asymptotically; HWE jumps in one generation. Robbins-bait.</li>
  <li><strong>Why allele frequencies are conserved.</strong> Random mating doesn't favor any allele — only repackages combinations. The pool of A's and a's is unchanged.</li>
  <li><strong>If you observe HWE for one trait but not another, the issue is locus-specific.</strong> Random mating is a population-wide property; deviations at one locus point to that locus's selection or linkage.</li>
</ol>`
    }
  });
})();
