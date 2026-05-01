/* Patches group 5: L16, L17, L18 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L16: {
      "Biological Species Concept (BSC)": {
        exAnswer: "Under the BSC, the moths likely ARE distinct species — the BSC defines species by reproductive isolation in nature, and zero interbreeding is the operational test. To confirm, you'd want: (1) sympatry (overlapping ranges so they have the OPPORTUNITY to interbreed), (2) evidence of intact reproductive barriers (different pheromones, mating times, genitalia, or post-zygotic incompatibility if pairings occur), and (3) ideally, molecular evidence of no recent gene flow. Without sympatry the test is inconclusive — they could simply be allopatric populations of one species.",
        mnem: "BSC = 'Bedroom Species Concept' — if they don't mate in nature, they're separate species."
      },
      "Morphological species concept": {
        exAnswer: "The morphological species concept is most useful for paleontology because fossils preserve only hard tissues (bones, teeth, shells) — never behavior, mating calls, or DNA. The BSC is INAPPLICABLE because you cannot test interbreeding in extinct organisms; reproductive isolation isn't observable in the rock record. Paleontologists use diagnosable skeletal/dental differences as proxies for species boundaries, knowing this risks lumping cryptic species or splitting one variable species into two (e.g., sexually dimorphic forms misidentified as separate species).",
        mnem: "Morpho = 'Looks like a species' — bones and teeth, no bedroom required."
      },
      "Phylogenetic species concept": {
        exAnswer: "The threshold question is HOW MUCH genetic divergence is enough to call something a separate species — there is no objective cutoff. 1% genome divergence sounds tiny, but bacteria reproduce clonally, so even small differences may correspond to ecologically distinct lineages. The PSC is controversial because: (1) any consistent character difference can split lineages, leading to taxonomic inflation; (2) gene-tree vs species-tree conflicts (incomplete lineage sorting) can mislead; (3) different groups (bacteria vs vertebrates) need different thresholds, undermining one universal concept.",
        mnem: "PSC = 'Phylogenetic Splitter Concept' — every twig becomes a species if you squint hard enough."
      },
      "Prezygotic isolation": {
        exAnswer: "This is TEMPORAL (allochronic) prezygotic isolation — the barrier acts before fertilization because the species are reproductively active at different times and gametes never have the chance to meet. It is prezygotic because no zygote is ever formed; it is a temporal/seasonal subtype, distinct from behavioral (different courtship), mechanical (incompatible structures), gametic (sperm-egg incompatibility), or habitat isolation. Different bloom seasons effectively make pollination impossible regardless of any other compatibility.",
        mnem: "Prezygotic = 'Pre-baby' barrier — they never even make the zygote."
      },
      "Postzygotic isolation": {
        exAnswer: "POSTZYGOTIC, post-fertilization. A zygote successfully formed (so all prezygotic barriers were bypassed) and developed into a viable hybrid — but the hybrid cannot reproduce, so genes don't flow between parental species across generations. Hybrid sterility is one of three classic postzygotic outcomes (inviability, sterility, F2 breakdown). Mechanism is usually chromosomal mismatch during meiosis (e.g., mule has 63 chromosomes from horse's 64 + donkey's 62, so no balanced gamete pairing).",
        mnem: "Postzygotic = 'Post-baby' barrier — zygote forms but the line stops there."
      },
      "Hybrid sterility": {
        exAnswer: "Sterility usually arises from chromosomal mismatch because parent species have diverged in chromosome number, structure, or arrangement (inversions, translocations). During hybrid meiosis, homologous chromosomes can't pair properly, so gametes get unbalanced or no chromosomes at all — sterility. The mule (63 chromosomes from horse 64 + donkey 62) cannot produce balanced gametes. This says the parent species have already diverged enough that their genomes are mechanically incompatible at meiosis — speciation is essentially complete and irreversible.",
        mnem: "Mule rule: 64 + 62 = 63, the unlucky odd number that can't pair up."
      },
      "Allopatric speciation": {
        exAnswer: "Each island population becomes geographically isolated, and over generations drift + island-specific selection (different predators, foods, climate) accumulate genetic and phenotypic differences. Reproductive isolation evolves as a BYPRODUCT of divergence, not because it was selected for. Intermediates: closely related sister species on adjacent islands (least isolated, most similar), more distantly related species on islands separated longer, and possibly hybrid zones if islands later reconnect. Classic example: Galápagos finches, where each island holds its own descendant species from one founder.",
        mnem: "Allopatric = 'Other-place' speciation — wall goes up, populations drift apart."
      },
      "Sympatric speciation": {
        exAnswer: "It's sympatric because the new tetraploid lineage arises in the SAME geographic location as its diploid parent — no physical barrier is required. Reproductive isolation is INSTANT: tetraploid (4n) × diploid (2n) crosses produce sterile triploid (3n) offspring with unbalanced meiosis, so the tetraploid is reproductively isolated within one generation. It's more common in plants because (1) plants tolerate genome doubling well (no chromosomal sex determination to disrupt), (2) many plants self-fertilize, (3) plants can reproduce asexually until enough tetraploids accumulate to mate.",
        mnem: "Sympatric polyploidy: 'doubled chromosomes, doubled species, no barrier needed.'"
      },
      "Reinforcement": {
        exAnswer: "Selection favors STRONGER PREZYGOTIC isolation — individuals that avoid mating with the wrong species don't waste gametes on doomed hybrids, so 'discriminating' alleles increase. Traits that evolve in response are mate-recognition signals: divergent courtship songs, pheromones, color patterns, or breeding times. Diagnostic test: prezygotic differences should be GREATER in sympatric (overlap) zones than in allopatric (pure) zones — the asymmetry is the signature of active reinforcement (e.g., pied/collared flycatchers' songs differ more where they overlap).",
        mnem: "Reinforcement = 'reinforcing the wall' — selection bricks up gaps where hybrids fail."
      },
      "Hybrid zone": {
        exAnswer: "The zone is stable because two opposing forces balance: (1) selection AGAINST hybrids (lower fitness) constantly removes hybrid alleles, narrowing the zone; (2) gene flow from pure populations OUTSIDE the zone constantly replenishes hybrids by feeding pure-species individuals into the contact area. The zone's width is set by this tension-zone equilibrium (Barton & Hewitt model). Without ongoing immigration the zone would collapse via selection; without selection the zone would widen until the species merged. Bombina has held this balance for thousands of years.",
        mnem: "Hybrid zone = 'tension zone' — selection pulls in, gene flow pushes out, width stays put."
      },
      "Viable hybrid": {
        exAnswer: "Boundaries don't collapse because hybrids usually occupy NOVEL or marginal habitats where parent species don't compete with them — the sunflower hybrids thrive on salt flats, dunes, or arid soils that neither parent tolerates. Where parent habitats remain available, parents still outcompete hybrids on home ground. The result is ecological partitioning: hybrid lineages can become separate species (HOMOPLOID HYBRID SPECIATION, as in Helianthus anomalus) without erasing parents. Parent boundaries persist because each parent occupies its own niche.",
        mnem: "Viable hybrids find a NEW niche, not the parents' niches — three species, not one."
      }
    },
    L17: {
      "Biogeography": {
        exAnswer: "Marsupials in Australia and South America share a deep common ancestor that lived on Gondwana — when Gondwana broke up (~80–50 Mya), marsupial lineages were carried apart on drifting continents (vicariance), surviving on the southern landmasses while placentals dominated the north. The disjunct distribution is impossible to explain by recent dispersal across thousands of km of ocean; it makes sense only as a relict of when the continents were connected. This is classic evidence for continental drift via vicariance.",
        mnem: "Biogeography = 'where life lives' — continents drift, lineages ride along."
      },
      "Wallace line": {
        exAnswer: "It marks an ancient deep-water trench (Lombok Strait, >250 m deep) that NEVER dried out even at glacial low sea levels. Bali sat on the Asian continental shelf (Sundaland) and Lombok on the Australasian shelf (Sahul); during glacial maxima, animals could walk across exposed seabed within each shelf but could never cross the deep trench between. Tens of millions of years of separation produced two completely distinct evolutionary lineages — placental mammals/woodpeckers on the Asian side, marsupials/cockatoos on the Australasian side — separated by <30 km of water.",
        mnem: "Wallace line = a watery wall — Bali to Lombok is a 30-km hop and a 50-million-year leap."
      },
      "Dispersal": {
        exAnswer: "DISPERSAL — finch ancestors crossed the open ocean to reach the Galápagos. The Galápagos are volcanic islands that emerged from the seafloor (~3–5 Mya) and were never connected to South America by land, so vicariance is impossible. The most likely mechanism is rare long-distance dispersal: a small founding flock blown by storms or rafted on debris reached the islands and survived. Once there, the founders radiated into ~14 species. Molecular dating confirms the colonization is much younger than any geological connection.",
        mnem: "Dispersal = D for 'Drift across' — animals move to a place the barrier was already there."
      },
      "Vicariance": {
        exAnswer: "VICARIANCE. Lystrosaurus lived on Pangaea/Gondwana ~250 Mya before the continents split. As Gondwana fragmented, the original continuous range was carved up by the opening Atlantic Ocean — same lineage, now stranded on different drifting landmasses. The shared fossil record across South America, Africa, India, and Antarctica was one of the original lines of evidence for continental drift (Wegener, 1915). Vicariance is the geographic SEPARATION of an existing range by a new barrier, contrasting with dispersal (movement across an existing barrier).",
        mnem: "Vicariance = V for 'Vector splits' — the barrier appears, the lineage was already there."
      },
      "Standing diversity": {
        exAnswer: "Larger islands sustain more species because (1) they have lower extinction rates — bigger populations of each species, more habitat heterogeneity, more refugia from disturbance — and (2) larger targets for immigrants, slightly raising arrival rates. MacArthur-Wilson's species-area relationship predicts S = cAᶻ (z typically 0.2–0.35). A 10× area increase predicts roughly 2–3× more species, matching the 50→200 observation. Equilibrium standing diversity is set by the balance of immigration (declining as island fills) and extinction (rising with more species).",
        mnem: "Bigger island = lower extinction = more species at equilibrium."
      },
      "Turnover rate": {
        exAnswer: "Turnover rate = 5 species/year (constant species count, but the IDENTITIES change). It matters for conservation because protecting a fixed number of species in a reserve may not preserve the SAME species over time — natural turnover means the species composition is dynamic. Reserves must be large enough to accommodate immigration AND minimize extinction; isolated reserves with high turnover lose unique species permanently. Simberloff & Wilson's mangrove fumigation experiments confirmed turnover empirically: same total species count returned, but different species assemblage.",
        mnem: "Turnover = treadmill diversity — same count, different runners."
      },
      "Adaptive radiation": {
        exAnswer: "After the K-Pg mass extinction (~66 Mya) wiped out non-avian dinosaurs, ECOLOGICAL OPPORTUNITY exploded — empty niches across terrestrial ecosystems. Mammals, previously small and nocturnal, radiated into the vacant roles (large herbivores, apex predators, marine, flying). Conditions: (1) empty niches (no competitors), (2) genetic/morphological versatility in the founding lineage (mammals had jaw, dental, and warm-blood innovations), (3) time. The term is ADAPTIVE RADIATION — rapid lineage-splitting into ecologically distinct daughter species.",
        mnem: "Adaptive radiation = 'fill the empty rooms' — mass extinction empties the house, survivors furnish each room differently."
      },
      "Key innovation": {
        exAnswer: "FLOWERS + FRUITS are the canonical key innovation. Flowers attracted animal pollinators (more efficient than wind), and fruits enabled animal-mediated seed dispersal — both opened ecological niches unavailable to gymnosperms. Other key innovations: jaws (vertebrate radiation, ~440 Mya — opened predatory niches), wings (insect/bird/bat radiations — opened aerial niches), pharyngeal jaws in cichlids (decoupled prey capture from processing — fueled hundreds-of-species lake radiations), and tetrapod limbs (terrestrial niche). Pattern: a novel structure unlocks habitat or function previously inaccessible, triggering an adaptive radiation.",
        mnem: "Key innovation = literally a key — opens a previously locked ecological door."
      }
    },
    L18: {
      "Selective harvest": {
        exAnswer: "It's CONTEMPORARY DIRECTIONAL SELECTION imposed by humans — trophy hunting consistently removes the largest-horned rams (which are also the prime breeders), so heritable horn size shifts downward each generation. On Ram Mountain, Alberta, mean horn size declined ~25% in 30 years; horn-size heritability is ~0.7 (high). It REVERSES natural selection because under natural conditions, large horns conferred mating advantages (sexual selection); now large-horned rams die before reproducing. Net selection direction flips from 'bigger is better' to 'smaller survives.'",
        mnem: "Selective harvest = un-natural selection: big horns used to win mates, now they get you shot."
      },
      "Fisheries-induced evolution": {
        exAnswer: "It's strong size-selective directional selection acting on heritable life-history traits. Size-limit rules ('keep only fish >X cm') consistently REMOVE large, late-maturing fish; fish that mature SMALL and EARLY (below the legal size) reproduce before they're caught. Heritability of size-at-maturity is non-zero, so each generation shifts toward earlier, smaller maturation. Atlantic cod show measurable shifts within 10–20 generations (~30–40 years). This is contemporary evolution at human-managed timescales — and the management rule itself is the selective agent.",
        mnem: "Fishery rule: 'big fish go in the boat, small fish make babies' — the next generation is smaller."
      },
      "Inbreeding depression": {
        exAnswer: "With only 30 cheetahs, mating must occur between close relatives, raising HOMOZYGOSITY across the genome. Recessive deleterious alleles (normally hidden in heterozygotes) get exposed when matched with copies — embryos die, sperm are abnormal, immune systems fail. Cheetahs already had a historic bottleneck (~10 KYA), so the species carries unusually high homozygosity baseline; further inbreeding compounds it. Mechanism = expression of accumulated genetic load from recessive deleterious alleles in homozygous form. Outcome: low fertilization rates, high cub mortality, immune-system failure (cheetahs can accept skin grafts from unrelated cheetahs).",
        mnem: "Inbreeding depression = exposing the family skeletons — recessive bad alleles get matched up."
      },
      "Genetic rescue": {
        exAnswer: "It worked because the Texas pumas brought NEW alleles into the Florida panther gene pool, breaking up homozygous deleterious recessive combinations. Hybrid offspring were heterozygous at many loci, masking deleterious recessives (heterosis/hybrid vigor). Heart defects dropped, kitten survival rose, population grew from ~30 to ~200. It was successful because (1) the bottleneck was severe (high inbreeding load), (2) the donor (Texas puma) was the historic gene-flow source — same subspecies-level lineage, low risk of outbreeding depression, (3) only a small infusion (8 individuals) was enough to break inbreeding without overwhelming local adaptation.",
        mnem: "Genetic rescue = importing new genes to mask the bad recessives — heterosis to the rescue."
      },
      "Fragmentation": {
        exAnswer: "Genetic consequences: each patch's small population suffers elevated drift (random allele loss), reduced heterozygosity, and inbreeding depression as relatives become forced mates. Loss of gene flow between patches means local adaptation diverges or, more often, deleterious alleles fix randomly. Demographic consequences: smaller patches support fewer individuals → higher extinction risk from environmental stochasticity (one bad year wipes a patch); edge effects expose more individuals to predators, microclimate change, and invasive species. Without dispersal corridors connecting patches, the population becomes a collection of doomed mini-populations rather than one viable one.",
        mnem: "Fragmentation = many tiny populations bleeding diversity, each one stranded on its own island."
      },
      "Phenological shift": {
        exAnswer: "PLASTIC mechanism: trees use temperature cues to time leaf-out, so warmer springs directly produce earlier budburst — no genetic change required (phenotypic plasticity). EVOLUTIONARY mechanism: heritable variation in temperature thresholds means trees with earlier-leafing genotypes get more growing season, leading to genetic shifts over generations. MISMATCH CONCERNS: pollinators or herbivores keyed to photoperiod (which doesn't change with climate) emerge on the OLD schedule and miss the new leaf-out, breaking trophic interactions (e.g., caterpillar–bird timing). Mismatched species suffer; matched species are fine.",
        mnem: "Phenology = 'PHENO-logy of warming' — events shift earlier, but the calendar (photoperiod) doesn't."
      },
      "Range shift": {
        exAnswer: "Mountain-top species have NOWHERE TO GO because (1) they are already at the highest, coldest available habitat — going 'upslope' means going off the summit, into thin air, with no land remaining; (2) horizontal dispersal would require descending into warmer habitat first, which is the very condition they're escaping; (3) neighboring mountains are separated by warm valleys, often impassable for cold-adapted species. Result: 'mountain-top extinction' — populations literally squeezed off the top as warming pushes their thermal niche above the elevation. American pikas and high-altitude amphibians are textbook cases.",
        mnem: "Mountain-top = 'escalator to extinction' — climb up, run out of mountain, gone."
      },
      "Conservation biology": {
        exAnswer: "Because conservation must preserve EVOLUTIONARY POTENTIAL, not just current populations. Saving 30 cheetahs preserves headcount but not the genetic variation needed for future adaptation (drought, disease, climate change). Conservation requires understanding effective population size (Ne), gene flow, inbreeding depression, local adaptation, hybridization risks, and rates of contemporary evolution — all evolutionary concepts. Pure ecology says 'maintain the habitat'; evolutionary biology adds 'maintain the variation that lets the species RESPOND to changing habitat.' Without that, even healthy populations can't track environmental change.",
        mnem: "Conservation = 'evolution insurance' — you're preserving the ability to adapt, not a frozen snapshot."
      },
      "Captive breeding": {
        exAnswer: "Forces at work: (1) DRIFT — small captive populations lose alleles randomly each generation; (2) INBREEDING — limited founders force matings among relatives, raising homozygosity; (3) UNINTENTIONAL DOMESTICATION SELECTION — captive environments favor traits (tameness, breeding in cages) that may be maladaptive in the wild. Mitigations: pedigree-based mate-pairing (minimum-kinship selection) to spread founder alleles, periodic genetic infusions from wild populations, releases timed to retain wild behaviors, and largest possible founder population (>50 founders ideal). The California condor program tracked every bird's pedigree to manage these forces.",
        mnem: "Captive breeding = 'pedigree puzzle' — track every bird so drift and inbreeding don't drain the gene pool."
      }
    }
  });
})();
