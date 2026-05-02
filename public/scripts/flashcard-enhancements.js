/* ============================================================
   Flashcard enhancements for BIOL 4230 Evolution
   1. Robust tap-to-flip — works on touch + mouse, even if the
      original click listener was lost (e.g. fcCard re-rendered).
   2. "Explain" overlay — auto-parses the current term into
      Greek/Latin morphemes, surfaces a plain-English ELI5
      summary, and shows curated overrides for evolution acronyms.
   ============================================================ */
(function() {
  'use strict';

  /* ============================================================
     1. ROBUST TAP-TO-FLIP
     ============================================================ */
  let downXY = null;
  function isInteractive(t) {
    return t.closest && t.closest('button, input, select, textarea, a, .fc-pre-grade, .fc-grade-buttons, .fc-control-bar');
  }
  function getCard(t) {
    return t.closest && t.closest('#fcCard, .fc-card');
  }
  document.addEventListener('pointerdown', e => {
    const card = getCard(e.target);
    if (!card || isInteractive(e.target)) return;
    downXY = { x: e.clientX, y: e.clientY, t: Date.now(), card };
  }, true);

  document.addEventListener('pointerup', e => {
    if (!downXY) return;
    const card = getCard(e.target);
    if (!card || card !== downXY.card || isInteractive(e.target)) { downXY = null; return; }
    const dx = Math.abs(e.clientX - downXY.x);
    const dy = Math.abs(e.clientY - downXY.y);
    const dt = Date.now() - downXY.t;
    downXY = null;
    if (dx < 12 && dy < 12 && dt < 700) {
      let before = card.classList.contains('flipped');
      try { if (typeof window.fcFlip === 'function') window.fcFlip(); } catch(_){}
      if (card.classList.contains('flipped') === before) {
        card.classList.toggle('flipped');
      }
    }
  }, true);

  /* ============================================================
     2. WORD-BREAKDOWN DICTIONARY
     ============================================================
     Greek/Latin morphemes common in evolutionary biology.
     Order matters — longest matches checked first.
     ============================================================ */
  const PREFIXES = [
    ['phylogen','tribe + origin (relationships through descent)'],
    ['heterozyg','different (hetero) + yoke (zyg) — different alleles paired'],
    ['homozyg','same (homo) + yoke (zyg) — identical alleles paired'],
    ['ortholog','straight/correct (ortho) — homologous genes separated by speciation'],
    ['paralog','beside (para) — homologous genes within a genome (gene duplication)'],
    ['xenolog','foreign (xeno) — homolog acquired by horizontal transfer'],
    ['plesiomorph','near (plesi) + form (morph) — ancestral character state'],
    ['apomorph','away from (apo) + form (morph) — derived character state'],
    ['synapomorph','together (syn) + derived — shared derived character'],
    ['symplesiomorph','together (sym) + ancestral — shared ancestral character'],
    ['autapomorph','self (auto) + derived — uniquely derived in one lineage'],
    ['homoplas','same (homo) + form (plas) — convergent / parallel similarity'],
    ['monophyl','one (mono) + tribe (phyl) — single ancestor and all descendants'],
    ['paraphyl','beside (para) + tribe — ancestor + some but not all descendants'],
    ['polyphyl','many (poly) + tribe — multiple separate ancestors grouped together'],
    ['cryptic','hidden — used for cryptic species that look identical'],
    ['parapatric','beside (para) + homeland (patric) — adjacent populations'],
    ['allopatric','other (allo) + homeland (patric) — geographically isolated populations'],
    ['sympatric','together (sym) + homeland (patric) — same geographic area'],
    ['peripatric','around (peri) + homeland — small isolated peripheral population'],
    ['allopolyploid','other (allo) + many (poly) + form (ploid) — polyploid from hybrid'],
    ['autopolyploid','self (auto) + many (poly) + form (ploid) — polyploid within one species'],
    ['eukaryot','true (eu) + nucleus (karyon)'],
    ['prokaryot','before (pro) + nucleus (karyon)'],
    ['extinc','out + put out (extinguish)'],
    ['neo','new'],
    ['paleo','ancient'],
    ['proto','first / earliest'],
    ['phylo','tribe / lineage'],
    ['phyl','tribe / lineage'],
    ['ana','up / again'],
    ['cata','down'],
    ['hetero','different'],
    ['homo','same'],
    ['homologue','same proportion / origin'],
    ['eu','true / well'],
    ['endo','inside'],
    ['exo','outside'],
    ['epi','on / upon'],
    ['extra','outside / beyond'],
    ['hyper','above / over'],
    ['hypo','below / under'],
    ['inter','between'],
    ['intra','within'],
    ['iso','equal'],
    ['macro','large'],
    ['meso','middle'],
    ['micro','small'],
    ['mono','one'],
    ['multi','many'],
    ['oligo','few'],
    ['ortho','straight / correct'],
    ['para','beside'],
    ['peri','around'],
    ['poly','many'],
    ['post','after'],
    ['pre','before'],
    ['pro','before / in front'],
    ['pseudo','false'],
    ['sub','under'],
    ['super','above'],
    ['syn','together'],
    ['sym','together'],
    ['tele','far / end'],
    ['trans','across'],
    ['anti','against'],
    ['auto','self'],
    ['allo','other'],
    ['xeno','foreign'],
    ['bi','two'],
    ['bio','life'],
    ['di','two'],
    ['un','not'],
    ['re','again'],
    ['a','not / without'],
  ];

  const SUFFIXES = [
    ['speciation','process of becoming species'],
    ['adaptation','process of fitting (Latin ad- + apt)'],
    ['phylogeny','origin / formation of a lineage'],
    ['ation','process / action'],
    ['genesis','origin / formation'],
    ['logy','study of'],
    ['lysis','breakdown / splitting'],
    ['lytic','breaking down'],
    ['osis','condition / state'],
    ['otic','condition / state (adjective)'],
    ['troph','nourishment'],
    ['phile','one that loves'],
    ['phobe','one that fears'],
    ['ploid','set / fold (chromosome count)'],
    ['morph','form / shape'],
    ['type','impression / form (genotype, phenotype)'],
    ['gen','producing / generating'],
    ['plast','formed thing'],
    ['oma','tumor / mass'],
    ['cide','to kill'],
    ['phyte','plant'],
    ['cyte','cell'],
    ['sphere','globe / region'],
    ['stasis','standing / equilibrium'],
    ['some','body / structure'],
  ];

  /* ============================================================
     3. ELI5 — plain-English explanations for evolution terms
     ============================================================ */
  const ELI5 = {
    /* ===== UNIT 1 · MECHANISMS ============================= */
    'evolution': {
      gist: 'Change in the genetic makeup (allele frequencies) of a population from one generation to the next. Populations evolve, individuals do not.',
      why: 'It is biology\'s unifying theory — Dobzhansky said "nothing in biology makes sense except in the light of evolution." Antibiotic resistance, vaccine design, conservation, agriculture all rely on evolutionary thinking.',
      more: 'Four mechanisms: natural selection, genetic drift, gene flow, mutation. Selection is the only one that systematically produces adaptation; the others change frequencies but not in any goal-directed way.'
    },
    'natural selection': {
      gist: 'Differential reproductive success: individuals carrying heritable trait variants that help them survive or breed leave more offspring, so those variants increase in frequency.',
      why: 'It is the ONLY mechanism that produces adaptive fit between organism and environment. Drift, gene flow, and mutation all change allele frequencies but not in any goal-directed way.',
      more: 'Three requirements (Darwin): (1) variation, (2) heritability, (3) differential reproductive success. Take any one away and selection cannot drive evolutionary change.'
    },
    'genetic drift': {
      gist: 'Random change in allele frequencies due to sampling — like flipping a coin only a few times and getting more heads than tails by chance.',
      why: 'Drift dominates in small populations and at neutral loci. It can fix harmful alleles and lose beneficial ones; it explains why founder events and bottlenecks reshape populations so dramatically.',
      more: 'Two famous flavors: founder effect (small group colonizes a new area) and bottleneck (population crashes and recovers). Both reduce genetic variation.'
    },
    'gene flow': {
      gist: 'Movement of alleles between populations through migration of individuals or gametes — like dye spreading between two ponds connected by a stream.',
      why: 'Gene flow homogenizes populations and counteracts local adaptation. Cut it off (mountain rises, river forms) and populations diverge; restore it and they merge.',
      more: 'A little gene flow can prevent speciation entirely. Wright\'s rule of thumb: even ~1 migrant per generation (Nm ≥ 1) keeps populations from diverging by drift alone.'
    },
    'mutation': {
      gist: 'A change in DNA sequence — the ultimate source of all new genetic variation.',
      why: 'Without mutation there would be nothing for selection or drift to act on. Mutations are random with respect to fitness — they arise regardless of what would be helpful.',
      more: 'Most mutations are neutral; a few are harmful, even fewer are beneficial. The classic experiment: Luria-Delbrück fluctuation test (1943) showed bacterial mutations arise BEFORE exposure to phages, not in response to them.'
    },
    'fitness': {
      gist: 'A genotype\'s expected reproductive success — how many offspring it leaves, scaled relative to the most successful genotype.',
      why: 'Fitness is the currency selection trades in. "Survival of the fittest" really means "differential reproductive success of the fittest." A trait that helps you survive but reduces reproduction is selected AGAINST.',
      more: 'Two flavors: absolute fitness (W = total offspring) and relative fitness (w = W / W_max, scaled 0–1). Selection coefficient s = 1 − w.'
    },
    'allele': {
      gist: 'A variant version of a gene — like flavors of the same recipe.',
      why: 'Evolution is just allele frequencies changing. Tracking which alleles are common, rare, fixed, or lost across generations IS the empirical study of evolution.',
      more: 'Alternative alleles arise by mutation. "Wild-type" is whichever allele is most common; "fixed" means frequency = 100%; "lost" means frequency = 0%.'
    },
    'population': {
      gist: 'A group of interbreeding individuals of the same species in a defined area.',
      why: 'Evolution happens at the population level, not in individuals. An individual\'s genes do not change — but the proportion of carriers in the next generation can.',
      more: 'Defining the boundaries matters: too narrow and you ignore gene flow, too broad and you average across local adaptations.'
    },
    'hardy-weinberg': {
      gist: 'A null model: in an idealized population (no selection, no drift, no migration, no mutation, random mating), allele frequencies stay the same forever and genotype frequencies satisfy p² + 2pq + q² = 1.',
      why: 'It\'s the "nothing-is-happening" baseline. Any deviation from HW expectations is evidence that one of the assumptions is violated — meaning evolution IS happening at that locus.',
      more: 'Five assumptions: (1) random mating, (2) no selection, (3) no mutation, (4) no migration, (5) infinite (or large) population — i.e., no drift. Real populations almost never satisfy all five.'
    },
    'heritability': {
      gist: 'The fraction of phenotypic variation in a population that is genetic — how much of the variability you see is passed from parents to offspring.',
      why: 'Selection only produces evolutionary change to the extent that traits are heritable. Heritability ≈ 0 → no response to selection. h² is what determines the speed of adaptation.',
      more: 'Two flavors: broad-sense H² (V_G / V_P) and narrow-sense h² (V_A / V_P). Breeder\'s equation: R = h²S — response equals heritability times selection differential.'
    },
    'phenotype': {
      gist: 'The observable traits of an organism — what you can measure (color, size, behavior, biochemistry).',
      why: 'Selection acts on phenotypes, not directly on genotypes. The phenotype is the bridge between genes and the environment that does the actual filtering.',
      more: 'Phenotype = genotype + environment (+ genotype-by-environment interactions). The same genotype can produce different phenotypes in different environments (plasticity).'
    },
    'genotype': {
      gist: 'The genetic makeup of an individual — the specific alleles it carries at each locus.',
      why: 'Genotypes are heritable; phenotypes only matter for evolution to the extent they reflect genotypes (h²).',
      more: 'A locus with two alleles A and a has three genotypes: AA, Aa, aa. Their frequencies follow Hardy-Weinberg under the five assumptions.'
    },
    'plasticity': {
      gist: 'The ability of one genotype to produce different phenotypes in different environments.',
      why: 'Plasticity decouples genotype from phenotype — so selection on phenotypes does not always produce evolutionary change at the genetic level.',
      more: 'Reaction norms plot phenotype as a function of environment. Examples: Daphnia helmets in response to predator cues, sex determination by temperature in turtles.'
    },
    'directional selection': {
      gist: 'Selection that favors one extreme of a trait — population mean shifts in that direction over generations.',
      why: 'This is the kind of selection most people picture. It produces directional adaptive change: longer beaks in finches during droughts, antibiotic resistance in bacteria.',
      more: 'Compared to stabilizing (favors the mean) and disruptive (favors both extremes). Directional selection reduces genetic variance for the trait being selected.'
    },
    'stabilizing selection': {
      gist: 'Selection against both extremes — the population mean stays put but variance shrinks.',
      why: 'Most traits in stable environments are under stabilizing selection. Human birth weight is a classic example: very small AND very large babies have higher mortality.',
      more: 'Reduces phenotypic variance without changing the mean. Strong stabilizing selection on highly heritable traits is the reason "long-stable" features (e.g., body plan) are so conserved.'
    },
    'disruptive selection': {
      gist: 'Selection that favors both extremes and acts against the middle — population becomes bimodal.',
      why: 'Disruptive selection is one of the few mechanisms that can drive sympatric speciation by maintaining two distinct trait clusters in one geographic area.',
      more: 'Cameroon black-bellied seedcracker finches: two beak sizes, each specialized on a different seed type, intermediate beaks starve. Classic textbook case.'
    },
    'sexual selection': {
      gist: 'Selection on traits that improve mating success rather than survival — peacock\'s tail, deer antlers, bird songs.',
      why: 'Sexual selection can produce traits that REDUCE survival but increase reproduction. It explains many ornaments and weapons that look "wasteful" from a survival standpoint.',
      more: 'Two flavors: intrasexual (male-male combat, e.g., antlers) and intersexual (female choice, e.g., peacock tail). Bateman\'s principle: female reproductive success is limited by eggs/offspring, male by mates.'
    },
    'speciation': {
      gist: 'The origin of two species from one — when a population splits into two reproductively isolated groups.',
      why: 'It is HOW biodiversity is generated. Without speciation, life would be one giant interbreeding swarm.',
      more: 'Three geographic modes: allopatric (geographic isolation, most common), sympatric (within range, e.g., polyploidy in plants), peripatric (small peripheral population). Reproductive isolation can be prezygotic or postzygotic.'
    },
    'reproductive isolation': {
      gist: 'Anything that prevents two populations from successfully interbreeding — the test of separate species under the BSC.',
      why: 'Without reproductive isolation, gene flow homogenizes populations and prevents speciation. With it, lineages diverge and become independent.',
      more: 'Prezygotic: habitat, temporal, behavioral, mechanical, gametic isolation. Postzygotic: hybrid inviability (zygote dies), hybrid sterility (mule), hybrid breakdown (F2 weak).'
    },
    'phylogeny': {
      gist: 'A branching diagram showing the evolutionary relationships among taxa — like a family tree for species.',
      why: 'Phylogenies organize all comparative biology. Want to study trait evolution, biogeography, coevolution, or epidemiology? You need a tree first.',
      more: 'Read trees from tips back to root. Sister taxa share a most recent common ancestor not shared with any other taxon. Branch length can represent time, change, or nothing depending on the method.'
    },
    'monophyletic': {
      gist: 'A group consisting of a common ancestor and ALL its descendants — a complete clade.',
      why: 'Monophyletic groups are the only "natural" groups in cladistics. Birds + their ancestor IS monophyletic; "reptiles" excluding birds is paraphyletic.',
      more: 'Greek: mono (one) + phylon (tribe). Monophyly is identified by shared derived characters (synapomorphies).'
    },
    'paraphyletic': {
      gist: 'A group containing a common ancestor and SOME but not all of its descendants — incomplete clade.',
      why: 'Traditional groups like "reptiles" (excluding birds) and "fish" (excluding tetrapods) are paraphyletic. Modern systematics avoids them in formal classification.',
      more: 'Greek: para (beside) + phylon. Sign that you are looking at a paraphyletic group: members defined by ancestral characters rather than shared derived ones.'
    },
    'polyphyletic': {
      gist: 'A group whose members come from MULTIPLE separate ancestors — wrong group, defined by convergent traits.',
      why: 'Polyphyletic groups reflect classification errors that lump unrelated lineages by superficial similarity (e.g., "warm-blooded animals" pools birds + mammals separately).',
      more: 'Greek: poly (many) + phylon. Once a group is recognized as polyphyletic, taxonomy revises to make groups monophyletic.'
    },
    'synapomorphy': {
      gist: 'A shared derived character — the kind of evidence cladists use to recognize monophyletic groups.',
      why: 'Synapomorphies are the ONLY characters useful for grouping in cladistics. Shared ancestral characters (symplesiomorphies) cannot tell you which taxa are most closely related.',
      more: 'Example: feathers are a synapomorphy uniting all birds. Vertebrae are a symplesiomorphy of birds (shared with all vertebrates) — useless for separating birds from other vertebrates.'
    },
    'homology': {
      gist: 'Similarity due to shared ancestry — same structure inherited from a common ancestor.',
      why: 'Homologies are the raw data of phylogeny. Distinguishing them from analogies (similar but unrelated) is the central challenge of comparative biology.',
      more: 'Example: the bones of bat wings, whale flippers, and human arms are homologous (same skeletal plan). Bird wings and bat wings are analogous as wings, but homologous as forelimbs.'
    },
    'analogy': {
      gist: 'Similarity due to convergent evolution — same function, independent origin.',
      why: 'Analogies trick naive classifiers into grouping unrelated lineages. Modern systematics uses synapomorphies (shared derived) and ignores convergence.',
      more: 'Example: octopus eyes and vertebrate eyes are analogous as eyes — independently evolved camera-type optics. Both are useful, neither implies common ancestry.'
    },
    'convergent evolution': {
      gist: 'Independent evolution of similar traits in unrelated lineages, usually because they face similar selective pressures.',
      why: 'It is the source of most analogies. Selection finds similar solutions when faced with similar problems — wings (birds, bats, insects), camera eyes (vertebrates, cephalopods), C4 photosynthesis (many plant lineages).',
      more: 'Distinguishable from homology by mapping characters onto a phylogenetic tree: convergent traits appear in distantly related lineages with intervening lineages that lack the trait.'
    },
    'kin selection': {
      gist: 'Selection on traits that help close relatives reproduce, even at a cost to the actor — because relatives share alleles by descent.',
      why: 'It explains apparently altruistic behavior (worker bees, alarm calls) without invoking group selection. Helping a relative is selectively favored if it propagates copies of your alleles.',
      more: 'Hamilton\'s rule: rB > C, where r = coefficient of relatedness (0.5 sibs, 0.25 nephews), B = recipient\'s benefit, C = actor\'s cost. Eusociality in bees + ants is a textbook case (haplodiploidy → sisters share 0.75).'
    },
    'inclusive fitness': {
      gist: 'The total reproductive success of an individual\'s alleles — direct (own offspring) PLUS indirect (relatives\' offspring weighted by relatedness).',
      why: 'It is the proper currency for evaluating altruism. The classic Haldane quip: "I would jump into a river to save two brothers or eight cousins."',
      more: 'Hamilton (1964) put kin selection on a quantitative footing using inclusive fitness. The math is just (direct fitness) + Σ r_i × (indirect fitness contributions).'
    },
    'eusociality': {
      gist: 'The most extreme social system: overlapping generations, cooperative care of young, AND a reproductive division of labor (most adults don\'t breed).',
      why: 'It is striking because most colony members are sterile — a paradox that kin selection (Hamilton 1964) finally explained.',
      more: 'Found in some bees, ants, wasps (haplodiploid), termites (diploid), and naked mole rats (mammals!). Workers help raise siblings instead of producing their own offspring.'
    },
    'coevolution': {
      gist: 'Reciprocal evolutionary change in two interacting species — each one\'s adaptations drive the other\'s response.',
      why: 'Most ecological interactions (predator/prey, parasite/host, plant/pollinator, mutualisms) are coevolutionary. The result is often an arms race or matched specialization.',
      more: 'Classic examples: Crossbills + lodgepole pine (bill shape vs. cone shape), garter snakes + newt tetrodotoxin, fig + fig-wasp pollination. Red Queen hypothesis: must keep evolving just to stay in place.'
    },
    'lamarck': {
      gist: 'Jean-Baptiste Lamarck (1809) proposed that organisms inherit traits acquired during their lifetime — the giraffe stretches its neck, and its offspring inherit a slightly longer neck.',
      why: 'Lamarck was right that species change over time but wrong about the mechanism. Acquired (somatic) traits do not enter the germline. He is the famous "wrong example" but get him for: FIRST systematic mechanism of evolution.',
      more: 'Lamarck did not say "use it or lose it" with intent — he proposed it as a natural mechanism. His misstep was thinking somatic changes could be heritable. The Weismann barrier (germ plasm theory) later refuted this.'
    },
    'darwin': {
      gist: 'Charles Darwin (1809–1882) developed natural selection as the mechanism of evolution after his 1831–1836 Beagle voyage and decades of subsequent work.',
      why: 'Origin of Species (1859) is the foundational text. Darwin assembled evidence from biogeography, embryology, comparative anatomy, breeding, and the fossil record.',
      more: 'Darwin and Wallace are CO-discoverers — Wallace\'s 1858 letter from the Malay Archipelago described the same idea independently and prompted Darwin to publish. The 1858 Linnean Society paper was joint Darwin-Wallace.'
    },
    'wallace': {
      gist: 'Alfred Russel Wallace (1823–1913) co-discovered natural selection independently of Darwin while working in the Malay Archipelago.',
      why: 'His 1858 letter to Darwin describing essentially the same theory is what finally pushed Darwin to publish. The 1858 Linnean Society paper credits both.',
      more: 'Wallace also founded biogeography — the Wallace Line through Indonesia separates Asian from Australian faunas. He stayed Darwinian on selection but later parted ways on human evolution.'
    },
    'lyell': {
      gist: 'Charles Lyell (1797–1875) was a geologist who argued for UNIFORMITARIANISM — modern, gradual processes operating over deep time produced Earth\'s features.',
      why: 'Lyell\'s gift to Darwin was DEEP TIME. Without millions of years, slow accumulation of small changes by selection cannot produce observed diversity.',
      more: 'Principles of Geology (1830–1833) was on Darwin\'s Beagle reading list. Uniformitarianism was opposed to catastrophism (Cuvier\'s view that Earth\'s features required sudden catastrophes).'
    },
    'biogeography': {
      gist: 'The study of where species live and why — the geographic patterns of biodiversity.',
      why: 'Biogeography is one of Darwin\'s strongest lines of evidence: islands have endemic species most closely related to mainland forms, similar habitats on different continents have unrelated species filling similar niches.',
      more: 'Wallace founded the field. Famous examples: Galápagos finches (one ancestor → many species), Australian marsupials filling placental-mammal niches, the Wallace Line.'
    },
    'fossil': {
      gist: 'The preserved remains, traces, or impressions of an organism from a past geological age.',
      why: 'Fossils provide the only direct record of extinct lineages and the order in which life forms appeared. Stratigraphic order = relative age; radiometric dating = absolute age.',
      more: 'Smith (1810s) used faunal succession to map rock strata and helped establish extinction as real. Cuvier independently confirmed extinction by comparing extinct mastodons to extant elephants.'
    },
    'extinction': {
      gist: 'The complete and permanent disappearance of a species or lineage from Earth.',
      why: 'Extinction is normal — most species that have ever lived are now extinct. But mass extinctions (e.g., end-Permian, K-Pg) wipe out a huge fraction of biodiversity in a short time and reset the tape.',
      more: 'Five "Big Five" mass extinctions: end-Ordovician, late-Devonian, end-Permian (worst, ~96% of marine species), end-Triassic, end-Cretaceous (K-Pg, killed non-avian dinosaurs). Many call current human-caused extinction the sixth.'
    },
    'molecular clock': {
      gist: 'The idea that DNA sequences accumulate substitutions at a roughly constant rate over time — so genetic distance ≈ divergence time, given a calibration.',
      why: 'Molecular clocks let us date divergence events (e.g., when humans split from chimps) when the fossil record is silent or ambiguous.',
      more: 'Different sites and genes evolve at different rates; clocks are usually calibrated against fossils. Strict clock vs. relaxed clock methods. Mutation rate × time × 2 lineages → expected substitutions.'
    },
    'genetic distance': {
      gist: 'A numerical measure of how different two sequences (or populations) are at the genetic level.',
      why: 'Genetic distance is the basis of most molecular phylogenetics — UPGMA, neighbor-joining, and likelihood methods all turn alignments into numerical distances.',
      more: 'Simple distances (p-distance) just count differences; corrected distances (Jukes-Cantor, Kimura, etc.) account for multiple hits at the same site.'
    },
    'parsimony': {
      gist: 'A tree-building principle: choose the phylogenetic tree that requires the FEWEST evolutionary changes to explain the data.',
      why: 'Parsimony is the cladist\'s default principle. It is fast and simple, but performs poorly when rates vary widely (long-branch attraction).',
      more: 'Maximum likelihood and Bayesian methods now dominate, but parsimony is still useful for morphological data where probabilistic models are hard to specify.'
    },
    'lateral gene transfer': {
      gist: 'Movement of DNA between organisms by something other than parent-to-offspring inheritance — the rule in bacteria, exception in eukaryotes.',
      why: 'LGT messes up the "tree of life" metaphor for prokaryotes — in bacteria, the tree is more like a web. LGT is also how antibiotic resistance spreads.',
      more: 'Three mechanisms in bacteria: transformation (uptake of free DNA), transduction (phage-mediated), conjugation (plasmid transfer). Eukaryotes acquire LGT mostly via endosymbiosis (mitochondria, plastids).'
    },
    /* ===== UNIT 2 · ADAPTATIONS, SEX, LIFE HISTORY, SOCIAL ============ */
    'galapagos finches': {
      gist: 'Darwin\'s finches — 15 species on the Galápagos Islands, descended from a single mainland ancestor, with bills specialized to different food sources.',
      why: 'They are the textbook adaptive radiation. Peter and Rosemary Grant\'s 30+ years on Daphne Major documented evolution by natural selection in real time during droughts.',
      more: 'Bill depth is highly heritable; during drought-induced food scarcity, finches with deeper bills survive better → bill depth shifts measurably in one generation. ALX1 and HMGA2 are major bill-shape genes.'
    },
    'guppies': {
      gist: 'Trinidad guppies — Endler\'s and Reznick\'s field experiments showing predation drives the evolution of male coloration and life history in real time.',
      why: 'Move guppies to high- vs low-predation streams and observe selection within ~10–15 generations. One of the cleanest natural experiments in evolution.',
      more: 'High predation: drab males, fast maturity, smaller offspring. Low predation: bright males, late maturity, fewer-but-bigger offspring. Both directions tested by transplants.'
    },
    'sexual dimorphism': {
      gist: 'Males and females of the same species look different — antlers in deer, plumage in birds, body size in elephant seals.',
      why: 'Strong dimorphism usually means sexual selection is intense. Big antlers + brawl-fighting → male-biased dimorphism in body and weapon size.',
      more: 'Bateman\'s principle predicts the more competitive sex (usually males) evolves bigger ornaments/weapons. Reverse dimorphism (e.g., raptors, sea horses) signals reversed sex roles or different selection regimes.'
    },
    'handicap principle': {
      gist: 'Zahavi\'s idea: costly ornaments are honest signals of quality precisely BECAUSE they are costly — only high-quality individuals can afford to grow them.',
      why: 'It explains why peacock tails do not just spiral into ever-bigger uselessness. Costly handicaps are the signal\'s guarantee of honesty.',
      more: 'Mathematical foundation: Grafton (1990). Cheap signals can be faked; expensive signals cannot. Examples: peacock train, stalk-eyed flies, warning coloration in poison frogs.'
    },
    'runaway selection': {
      gist: 'Fisher\'s self-reinforcing process: female preference for a male trait + heritability of both → preference and trait coevolve in tandem to extreme values.',
      why: 'It explains how peacock tails get so absurd. Once preference exists, choosing flashy mates produces flashy SONS — so the preference benefits its bearer through their sons.',
      more: 'Two-locus model: a "trait" locus and a "preference" locus. As preference allele rises, trait allele rides along by sexy-son effect. Runs until counter-selection (predation, energy) catches up.'
    },
    'r-selection': {
      gist: 'A life history strategy: many small offspring, fast maturity, short life — bet-hedge against unstable environments by playing the lottery many times.',
      why: 'r-selected species (mice, cod, mosquitoes) thrive in disturbed or unpredictable environments. Population size oscillates; rapid population growth recolonizes after crashes.',
      more: 'Contrast K-selection: few large offspring, late maturity, long life, parental care. r/K is a continuum, not a dichotomy — most species sit somewhere along it.'
    },
    'k-selection': {
      gist: 'A life history strategy: few large offspring, slow growth, late maturity, long life, heavy parental care — investment in quality over quantity.',
      why: 'K-selected species (humans, elephants, whales, oaks) dominate stable, crowded environments where competition matters more than density-independent shocks.',
      more: 'Contrast r-selection. The carrying capacity (K) of the environment is more constraining; selection favors competitive ability and survival of established individuals over fast reproduction.'
    },
    'semelparity': {
      gist: 'Reproducing once in a lifetime in a single big burst, then dying — Pacific salmon, mayflies, agave plants, century plants.',
      why: 'Semelparity makes sense when juveniles have low survival but a single big reproductive event has high payoff. The organism puts ALL its remaining resources into one shot.',
      more: 'Latin "semel" = once. Compare iteroparity (repeated reproduction). Models predict semelparity when adult survival is low or reproductive payoff scales nonlinearly with effort.'
    },
    'iteroparity': {
      gist: 'Reproducing multiple times across a lifetime — humans, most birds, most mammals, perennial plants.',
      why: 'Iteroparity wins when adult survival is good and reproductive payoff is roughly linear with effort. Parents survive and breed again.',
      more: 'Latin "itero" = repeat. The shift between semelparity and iteroparity is one of the most studied life-history transitions.'
    },
    'haplodiploidy': {
      gist: 'A sex-determination system where females are diploid and males are haploid — found in bees, ants, wasps, and a few other arthropods.',
      why: 'Under haplodiploidy, sisters share 75% of their genes (vs. 50% in diploids), which Hamilton showed could favor the evolution of eusociality (sterile worker castes).',
      more: 'Females develop from fertilized eggs, males from unfertilized eggs. Workers are female; queens lay eggs. Note: termites are eusocial but DIPLOID — haplodiploidy is sufficient but not necessary for eusociality.'
    },
    /* ===== UNIT 3 · HISTORY, PHYLOGENY, SPECIATION, HUMANS, MEDICINE = */
    'last universal common ancestor': {
      gist: 'LUCA — the most recent population from which all current cellular life on Earth descends. Probably lived ~3.5–4 billion years ago.',
      why: 'LUCA is the root of the tree of life — every gene that is universal among modern organisms traces back to LUCA. Reconstructing LUCA tells us what early cellular life was like.',
      more: 'Probably had DNA, ribosomes, ATP, the genetic code, and core metabolism. LUCA was likely a prokaryote, possibly thermophilic, perhaps near hydrothermal vents.'
    },
    'cambrian explosion': {
      gist: 'The geologically rapid (~30 Myr) appearance of nearly all major animal phyla starting ~541 Myr ago.',
      why: 'Most modern animal body plans show up in the Cambrian fossil record without obvious Precambrian precursors. It is the most famous diversification in Earth\'s history.',
      more: 'Major sites: Burgess Shale (Canada), Chengjiang (China). Drivers proposed: rising O₂, predator-prey arms races, evolution of eyes, novel Hox gene deployments.'
    },
    'mass extinction': {
      gist: 'A short geological interval during which a high fraction of species (typically >50% of marine families) goes extinct.',
      why: 'Mass extinctions reset evolutionary opportunities and are followed by adaptive radiations of survivors. They show that lineage success depends on chance + environment, not just adaptedness.',
      more: 'Big Five: end-Ordovician (~445 Mya), Late Devonian, end-Permian (~252 Mya, the worst), end-Triassic, end-Cretaceous (K-Pg, 66 Mya — killed non-avian dinosaurs, opened mammal radiation).'
    },
    'biological species concept': {
      gist: 'BSC — a species is a group of populations whose members can interbreed and produce viable, fertile offspring, but cannot interbreed with members of other such groups.',
      why: 'BSC (Mayr 1942) is the dominant species concept in zoology. It defines species by REPRODUCTIVE ISOLATION rather than morphology.',
      more: 'Limitations: doesn\'t apply to asexual organisms, fossils, or many bacteria. Hybridizing species (e.g., wolves × coyotes) violate strict BSC. Alternatives: Ecological SC, Phylogenetic SC, Morphological SC.'
    },
    'phylogenetic species concept': {
      gist: 'PSC — a species is the smallest monophyletic group whose members share a derived character state (or whose members all descend from a single common ancestor).',
      why: 'PSC is widely used in modern systematics — it works for asexuals, fossils, and bacteria where BSC fails. But it tends to recognize many more "species" than BSC because every diagnosable lineage qualifies.',
      more: 'Two flavors: monophyly-based (Mishler/Donoghue) and diagnosability-based (Cracraft). Often produces ~2× the species count of the BSC for the same group.'
    },
    'allopatric speciation': {
      gist: 'Speciation in geographic isolation — a barrier (mountain, river, ocean) splits a population, the halves diverge in isolation, and become reproductively incompatible.',
      why: 'Allopatric speciation is the most common geographic mode and the easiest to explain. Drift + local selection + no gene flow → divergence over time.',
      more: 'Vicariance (barrier rises in the middle of a range) vs. dispersal (founders cross a barrier). Galápagos finches = dispersal; Panama Isthmus closure (~3 Mya) is a famous vicariance event.'
    },
    'sympatric speciation': {
      gist: 'Speciation WITHOUT geographic isolation — two populations diverge while in the same area, usually via assortative mating + disruptive selection or polyploidy.',
      why: 'Sympatric speciation is rarer and harder to demonstrate, but documented in cichlids (lake morphs), apple maggot flies (host shifts), and many polyploid plants.',
      more: 'Polyploidy is the cleanest mechanism: a tetraploid offspring is instantly reproductively isolated from its diploid parents. Most flowering plants have polyploid ancestry.'
    },
    'adaptive radiation': {
      gist: 'Rapid diversification of a single ancestor into many descendant species occupying different ecological niches.',
      why: 'Adaptive radiations are evolution at its most spectacular: Galápagos finches, Hawaiian honeycreepers, Lake Victoria cichlids, the post-K-Pg mammal radiation.',
      more: 'Triggered by ecological opportunity (new continent, mass extinction, key innovation). Often involves quick morphological diversification with minimal genetic distance — the radiation outpaces the molecular clock.'
    },
    'hominin': {
      gist: 'The evolutionary lineage of humans after the split from chimpanzees — includes Australopithecus, Homo, Paranthropus, etc. (chimps and bonobos are NOT hominins).',
      why: 'The hominin record is what we use to reconstruct human evolution. Hundreds of fossils, dozens of named species, many uncertainties about which are direct ancestors.',
      more: 'Hominid (broader) = great apes + humans. Hominin (narrower) = humans + extinct close relatives only. Split from chimps ~6–7 Mya based on molecular and fossil data.'
    },
    'out of africa': {
      gist: 'The dominant model: anatomically modern Homo sapiens arose in Africa ~300 kya and spread out, replacing earlier hominin species (Neanderthals, Denisovans) across Eurasia.',
      why: 'Strongly supported by mitochondrial DNA (mtDNA) tracing African origin, Y chromosome data, archaeological dispersal patterns, and ancient DNA from Neanderthals.',
      more: 'There WAS some interbreeding — non-Africans carry ~1–2% Neanderthal DNA, and Asians/Oceanians carry small amounts of Denisovan DNA. So strict "replacement" is now "replacement with admixture."'
    },
    'antibiotic resistance': {
      gist: 'The classic real-time example of natural selection: bacterial populations evolve resistance to antibiotics within years, sometimes weeks.',
      why: 'It is the costliest evolutionary problem in modern medicine. Mechanisms: efflux pumps, modified target sites, antibiotic-degrading enzymes (β-lactamase). Resistance genes spread via horizontal transfer.',
      more: 'Drives evolutionary medicine. Solutions: combination therapy, antibiotic stewardship, narrow-spectrum drugs, phage therapy, vaccines that prevent infection (so the antibiotic isn\'t needed).'
    },
    'mismatch hypothesis': {
      gist: 'The idea that many modern diseases (obesity, diabetes, anxiety, myopia) reflect a mismatch between Pleistocene-adapted human bodies and modern environments.',
      why: 'It explains why "natural" no longer aligns with "healthy" for many traits. Selection optimized human physiology for ancestral conditions of food scarcity, high activity, etc.',
      more: 'Examples: thrifty-genotype hypothesis for obesity, lactase persistence as a recent (~5–10 kya) adaptation, allergy/autoimmunity from hygiene mismatch (loss of helminths and microbial diversity).'
    },
  };

  const OVERRIDES = {
    'bsc': [['B','Biological'], ['S','Species'], ['C','Concept']],
    'psc': [['P','Phylogenetic'], ['S','Species'], ['C','Concept']],
    'msc': [['M','Morphological'], ['S','Species'], ['C','Concept']],
    'esc': [['E','Ecological'], ['S','Species'], ['C','Concept']],
    'mrca': [['M','Most'], ['R','Recent'], ['C','Common'], ['A','Ancestor']],
    'luca': [['L','Last'], ['U','Universal'], ['C','Common'], ['A','Ancestor']],
    'lca': [['L','Last'], ['C','Common'], ['A','Ancestor']],
    'qtl': [['Q','Quantitative'], ['T','Trait'], ['L','Locus']],
    'snp': [['S','Single'], ['N','Nucleotide'], ['P','Polymorphism']],
    'gwas': [['G','Genome'], ['W','Wide'], ['A','Association'], ['S','Study']],
    'lgt': [['L','Lateral'], ['G','Gene'], ['T','Transfer']],
    'hgt': [['H','Horizontal'], ['G','Gene'], ['T','Transfer']],
    'mtdna': [['mt','mitochondrial'], ['DNA','Deoxyribonucleic Acid']],
    'ne': [['N','Effective'], ['e','population size — for population-genetic calculations']],
    'fst': [['F','fixation index'], ['ST','between Subpopulations relative to Total']],
    'k-pg': [['K','Cretaceous (German Kreide)'], ['Pg','Paleogene']],
    'k/t': [['K','Cretaceous'], ['T','Tertiary (older name for Pg)']],
    'r-selection': [['r','intrinsic rate of increase']],
    'k-selection': [['K','carrying capacity']],
    'h-w': [['H','Hardy'], ['W','Weinberg']],
    'rb': [['R','reproductive'], ['b','barrier — used loosely; do not confuse with cell-bio Rb']],
    'sry': [['S','Sex-determining'], ['R','Region'], ['Y','of Y chromosome']],
    'pcr': [['PCR','Polymerase Chain Reaction']],
    'eea': [['E','Environment of'], ['E','Evolutionary'], ['A','Adaptedness']],
  };

  function breakdownTerm(rawTerm) {
    if (!rawTerm) return null;
    const term = rawTerm.toLowerCase().trim();
    if (OVERRIDES[term]) return OVERRIDES[term];
    const cleaned = term.replace(/\(.*?\)/g, '').replace(/[\s/]+/g, '').trim();
    if (OVERRIDES[cleaned]) return OVERRIDES[cleaned];
    let s = cleaned;
    let result = [];
    let prefixHit = null;
    let suffixHit = null;
    for (const [p, m] of PREFIXES) {
      if (s.length > p.length + 1 && s.startsWith(p)) {
        prefixHit = [p, m]; break;
      }
    }
    if (prefixHit) s = s.slice(prefixHit[0].length);
    for (const [su, m] of SUFFIXES) {
      if (s.length > su.length + 1 && s.endsWith(su)) {
        suffixHit = [su, m]; break;
      }
    }
    if (suffixHit) s = s.slice(0, s.length - suffixHit[0].length);
    if (!prefixHit && !suffixHit) return null;
    if (prefixHit) result.push([prefixHit[0] + '-', prefixHit[1]]);
    if (s) result.push([s, '(root / stem)']);
    if (suffixHit) result.push(['-' + suffixHit[0], suffixHit[1]]);
    return result.length >= 2 ? result : null;
  }

  function escapeHtml(s){ return ('' + s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

  function ensureBreakdownUI() {
    if (document.getElementById('bdStyles')) return;
    const style = document.createElement('style');
    style.id = 'bdStyles';
    style.textContent = `
      .bd-launch{position:fixed;bottom:18px;right:18px;z-index:8000;background:#c89b2e;color:#0c0e12;border:none;border-radius:22px;padding:9px 16px;font-family:"Inter",system-ui,sans-serif;font-size:13px;font-weight:700;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,0.45);display:none;letter-spacing:0.02em}
      .bd-launch:hover{background:#e0b145}
      body.fc-mode .bd-launch{display:block}
      .bd-modal{position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:8500;display:none;align-items:center;justify-content:center;padding:20px;font-family:"Inter",system-ui,sans-serif}
      .bd-modal.show{display:flex}
      .bd-card{background:#fdfaf2;color:#1a1814;max-width:540px;width:100%;border-radius:12px;padding:22px 24px;box-shadow:0 16px 48px rgba(0,0,0,0.55);max-height:88vh;overflow:auto}
      .bd-card h3{margin:0 0 4px;font-size:18px}
      .bd-card .bd-term{font-size:22px;font-weight:700;color:#a8651a;margin-bottom:10px;font-family:"Fraunces",Georgia,serif}
      .bd-card .bd-row{display:flex;gap:12px;padding:8px 0;border-top:1px solid #d8d2c5;align-items:baseline}
      .bd-card .bd-row:first-of-type{border-top:none}
      .bd-card .bd-part{font-family:"Consolas",monospace;font-weight:700;color:#3a2e15;min-width:100px}
      .bd-card .bd-mean{flex:1;color:#3a2e15}
      .bd-card .bd-meaning{margin-top:14px;padding-top:10px;border-top:2px solid #c89b2e;font-size:14px;color:#3a2e15;line-height:1.5}
      .bd-card .bd-close{margin-top:14px;background:#f1ead9;border:1px solid #d8d2c5;border-radius:6px;padding:7px 14px;cursor:pointer;font-size:13px;float:right;font-weight:600}
      .bd-card .bd-close:hover{background:#e6dcc4}
      .bd-card .bd-empty{color:#7a7158;font-style:italic;padding:8px 0}
      .bd-card h4{margin:14px 0 4px;color:#a8651a;font-size:14px;font-family:"Inter",system-ui,sans-serif}
      .bd-card .bd-section{margin-top:14px}
    `;
    document.head.appendChild(style);

    const launch = document.createElement('button');
    launch.className = 'bd-launch';
    launch.id = 'bdLaunch';
    launch.title = 'Explain the current flashcard term — plain English + word breakdown (Ctrl+Shift+B)';
    launch.textContent = '🔍 Explain';
    launch.onclick = openBreakdownForCurrent;
    document.body.appendChild(launch);

    const modal = document.createElement('div');
    modal.className = 'bd-modal';
    modal.id = 'bdModal';
    modal.onclick = e => { if (e.target === modal) modal.classList.remove('show'); };
    modal.innerHTML = '<div class="bd-card" id="bdCardBody"></div>';
    document.body.appendChild(modal);
  }

  function getCurrentTerm() {
    const tEl = document.getElementById('fcTerm');
    if (tEl && tEl.textContent.trim()) return tEl.textContent.trim();
    const f = document.querySelector('.fc-card .fc-term, .fc-card .term, .fc-card h2, .fc-card h3');
    return f ? f.textContent.trim() : '';
  }

  function openBreakdownForCurrent() {
    const term = getCurrentTerm();
    showBreakdown(term);
  }

  function getEli5(term) {
    if (!term) return null;
    const t = term.toLowerCase().trim();
    if (ELI5[t]) return ELI5[t];
    const cleaned = t.replace(/\(.*?\)/g, '').trim();
    if (cleaned !== t && ELI5[cleaned]) return ELI5[cleaned];
    const keys = Object.keys(ELI5).sort((a,b) => b.length - a.length);
    for (const k of keys) {
      if (t.includes(k)) return ELI5[k];
    }
    return null;
  }

  function showBreakdown(term) {
    ensureBreakdownUI();
    const body = document.getElementById('bdCardBody');
    if (!term) {
      body.innerHTML = '<h3>Explain</h3><div class="bd-empty">No flashcard term currently visible.</div><button class="bd-close" onclick="document.getElementById(\'bdModal\').classList.remove(\'show\')">Close</button>';
      document.getElementById('bdModal').classList.add('show');
      return;
    }
    const display = term;
    const parts = breakdownTerm(term);
    const eli = getEli5(term);
    let html = '<div class="bd-term">' + escapeHtml(display) + '</div>';

    if (eli) {
      html += '<div class="bd-section"><h4>In plain English</h4>';
      html += '<div class="bd-meaning" style="margin-top:0;border:none;padding:0"><b>What it is:</b> ' + escapeHtml(eli.gist) + '</div>';
      if (eli.why) html += '<div class="bd-meaning" style="margin-top:6px;border:none;padding:0"><b>Why it matters:</b> ' + escapeHtml(eli.why) + '</div>';
      if (eli.more) html += '<div class="bd-meaning" style="margin-top:6px;border:none;padding:0;color:#5b554b;font-size:13px"><b>More:</b> ' + escapeHtml(eli.more) + '</div>';
      html += '</div>';
    }

    const wordCount = (term.match(/\S+/g) || []).length;
    const shouldShowAutoBreakdown = wordCount <= 3 && term.length <= 30 && parts && parts.length >= 2;
    if (shouldShowAutoBreakdown) {
      html += '<div class="bd-section"><h4>Breaking down the word</h4>';
      parts.forEach(([p, m]) => {
        html += '<div class="bd-row"><div class="bd-part">' + escapeHtml(p) + '</div><div class="bd-mean">= ' + escapeHtml(m) + '</div></div>';
      });
      const literal = parts.map(([p, m]) => m.split(/[—(–]/)[0].trim()).join(' + ');
      html += '<div class="bd-meaning"><b>Literal:</b> "' + escapeHtml(literal) + '"</div>';
      html += '</div>';
    }

    if (!eli && !parts) {
      html = '<div class="bd-term">' + escapeHtml(display) + '</div>' +
        '<div class="bd-empty">No explainer content yet for this card. Add an entry to <code>scripts/flashcard-enhancements.js</code> ELI5 to populate it.</div>';
    }

    html += '<button class="bd-close" onclick="document.getElementById(\'bdModal\').classList.remove(\'show\')">Close</button>';
    body.innerHTML = html;
    document.getElementById('bdModal').classList.add('show');
  }

  document.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'b') {
      e.preventDefault();
      openBreakdownForCurrent();
    }
    if (e.key === 'Escape') {
      const m = document.getElementById('bdModal');
      if (m && m.classList.contains('show')) m.classList.remove('show');
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureBreakdownUI);
  } else {
    ensureBreakdownUI();
  }

  window.bdBreakdown = breakdownTerm;
  window.bdShow = showBreakdown;
})();
