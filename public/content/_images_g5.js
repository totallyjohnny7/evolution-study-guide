/* Images + remaining content gaps (group 5: L16, L17, L18) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  // ============================================================
  // L16 — Species concepts, reproductive isolation, speciation
  // ============================================================
  window.addCardPatches('L16', {
    "Biological Species Concept (BSC)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Darwin's finches — distinct species under the BSC because they do not interbreed in nature, even though they share an ancestor and look similar.",
          credit: "Wikimedia Commons / John Gould" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Momo_260905.jpg/800px-Momo_260905.jpg",
          caption: "A mule (horse × donkey). The mule is sterile, so under the BSC horses and donkeys remain separate species despite producing viable F1 offspring.",
          credit: "Wikimedia Commons / Public domain" }
      ],
      exAnswer: "Under the BSC, species require reproductive isolation to be DIAGNOSED — looking similar isn't enough. If the two moths never interbreed in nature, they may still be a single species (e.g., behavioral barrier broken in lab) or genuinely distinct. Additional evidence: (1) lab cross-breeding tests for postzygotic compatibility, (2) molecular markers showing genetic divergence consistent with isolation, (3) field observation of mating signals/courtship differences. The BSC fails on asexual organisms and fossils — there, you fall back on morphological or phylogenetic concepts."
    },
    "Morphological species concept": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Kainops_invius_lateral_and_ventral.JPG/800px-Kainops_invius_lateral_and_ventral.JPG",
          caption: "A trilobite fossil (Kainops invius). Paleontologists rely on morphological species concepts because reproductive isolation cannot be tested in extinct organisms.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "The MORPHOLOGICAL species concept is most useful for paleontology. Fossils preserve hard parts (bones, teeth, shells) — there is no way to test interbreeding, so the BSC is inapplicable. Workers diagnose species by measurable morphology (skull dimensions, dental cusps, shell ornamentation). Limitation: cryptic species (genetically distinct, look identical) are missed; sexual dimorphism and life-stage variation can falsely split a single species into multiple."
    },
    "Phylogenetic species concept": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Speciation_modes.svg/800px-Speciation_modes.svg.png",
          caption: "Speciation modes. The PSC defines species as the smallest monophyletic group with unique derived characters — operational across asexual organisms where the BSC fails.",
          credit: "Wikimedia Commons / Ilmari Karonen" }
      ],
      exAnswer: "PSC defines species as the smallest monophyletic group with diagnosable shared derived characters. The threshold question: how much divergence (1%? 0.5%?) qualifies as 'derived enough' to constitute species rank? It's controversial because the cutoff is arbitrary and varies by group — bacteria with rapid mutation accumulate 1% divergence quickly without ecological differentiation. PSC tends to OVERSPLIT (often 2–3× more species than BSC). Useful where BSC fails (asexuals, fossils), but dataset-dependent."
    },
    "Prezygotic isolation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Speciation_by_Reinforcement_Schematic.svg/800px-Speciation_by_Reinforcement_Schematic.svg.png",
          caption: "Reinforcement schematic — selection strengthens prezygotic isolation when hybrids are unfit. Five barrier types: temporal, behavioral, mechanical, gametic, habitat.",
          credit: "Wikimedia Commons / CC BY-SA" }
      ],
      exAnswer: "TEMPORAL (= seasonal/diurnal) prezygotic isolation. The orchids never share pollinators in time because their flowering windows don't overlap, so pollen never reaches the wrong stigma. No zygote is ever formed — that's the prezygotic signature. Mnemonic T-B-M-G-H: Temporal, Behavioral, Mechanical, Gametic, Habitat — temporal is the first."
    },
    "Postzygotic isolation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Momo_260905.jpg/800px-Momo_260905.jpg",
          caption: "Mule (horse × donkey) — viable but sterile. Postzygotic isolation: the zygote forms and develops, but offspring cannot reproduce.",
          credit: "Wikimedia Commons / Public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Liger_couple.jpg/800px-Liger_couple.jpg",
          caption: "Ligers (lion × tiger hybrids) — typically infertile, another textbook postzygotic-isolation example.",
          credit: "Wikimedia Commons / Hkandy" }
      ],
      exAnswer: "POSTZYGOTIC (zygote forms successfully, but the hybrid is sterile — fertilization happened, isolation acts AFTER). Specifically: hybrid sterility (one of the three postzygotic types: inviability, sterility, breakdown). The zygote is formed, the hybrid develops normally, but meiosis fails — usually because parental chromosomes can't pair correctly. POST-fertilization."
    },
    "Hybrid sterility": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Momo_260905.jpg/800px-Momo_260905.jpg",
          caption: "A mule. Horse (64 chromosomes) × donkey (62 chromosomes) yields a 63-chromosome mule whose odd chromosome number breaks meiosis — hence sterile.",
          credit: "Wikimedia Commons / Public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Liger_couple.jpg/800px-Liger_couple.jpg",
          caption: "A liger (Panthera leo × Panthera tigris). Like the mule, parental chromosomal mismatches generally render hybrids reproductively non-functional.",
          credit: "Wikimedia Commons / Hkandy" }
      ],
      exAnswer: "Horse has 64 chromosomes, donkey 62 → mule has 63 (odd). At meiosis, chromosomes must pair as homologues; with mismatched parental sets, pairing fails, gametes are aneuploid and non-viable. This indicates the parent species' chromosomes have diverged enough that they no longer recognize one another as homologues — a strong sign that genetic divergence between horses and donkeys is well under way. The longer two lineages are separated, the more chromosomal rearrangements (inversions, fusions, fissions) accumulate, and the more decisively meiosis fails in their hybrids."
    },
    "Allopatric speciation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Allopatric_Speciation_Schematic.svg/800px-Allopatric_Speciation_Schematic.svg.png",
          caption: "Allopatric speciation: a geographic barrier divides one population; drift plus differing local selection accumulate divergence; reproductive isolation evolves as a byproduct.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Darwin's finches diversified after allopatric isolation across the Galápagos islands — the textbook allopatric radiation.",
          credit: "Wikimedia Commons / John Gould" }
      ],
      exAnswer: "Each island population is isolated from gene flow with the others. Drift + local selection (different food, predators, climate) → divergence in beak/body/behavior. Over thousands of generations, prezygotic and postzygotic isolation accumulates as a byproduct of independent evolution. Intermediates: populations on islands that were intermittently connected (during sea-level lows) may show partial isolation — a 'speciation gradient' from indistinct populations to fully separate species. Galápagos finches are the textbook case."
    },
    "Sympatric speciation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Sympatric_Speciation_Schematic.svg/800px-Sympatric_Speciation_Schematic.svg.png",
          caption: "Sympatric speciation: divergence within a single geographic range, often via niche shift, host shift, or polyploidy.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Polyploidization.svg/800px-Polyploidization.svg.png",
          caption: "Polyploidy (chromosome doubling) creates instant reproductive isolation — a tetraploid plant cannot produce viable offspring with diploid parents.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "POLYPLOIDY = sympatric because no geographic separation is needed. A tetraploid offspring (4n) crossing back with a diploid parent (2n) yields triploid (3n) gametes that meiose unevenly, producing inviable or sterile offspring. The polyploid is INSTANTLY reproductively isolated despite living among parents. More common in plants because (1) plants tolerate genome doubling better, (2) self-fertilization can establish a polyploid lineage, (3) animals' XY/ZW sex determination usually crashes under polyploidy. Estimates: ~40% of flowering plant species have polyploid origins."
    },
    "Reinforcement": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Speciation_by_Reinforcement_Schematic.svg/800px-Speciation_by_Reinforcement_Schematic.svg.png",
          caption: "Reinforcement: when hybrids are unfit in a contact zone, selection favors stronger prezygotic isolation — courtship/song/timing differences sharpen.",
          credit: "Wikimedia Commons / CC BY-SA" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg/800px-Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg",
          caption: "European pied flycatcher (Ficedula hypoleuca). Pied/collared flycatchers in Europe show stronger song differences in zones of overlap — a textbook reinforcement signature.",
          credit: "Wikimedia Commons / Andreas Trepte" }
      ],
      exAnswer: "Selection favors STRONGER prezygotic isolation. Hybrids waste reproductive effort, so any trait that helps individuals AVOID mating with the other species (different songs, mate preferences, microhabitat use, breeding times) is rewarded. Expected response: divergence of mate-recognition traits in the contact zone — exactly what's observed in pied/collared flycatchers (males' plumage and song differ more in sympatry than in allopatry)."
    },
    "Hybrid zone": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Benny_Trapp_Bombina_bombina_Rotbauchunke.jpg/800px-Benny_Trapp_Bombina_bombina_Rotbauchunke.jpg",
          caption: "European fire-bellied toad (Bombina bombina). Forms a narrow stable hybrid zone with B. variegata in central Europe.",
          credit: "Wikimedia Commons / Benny Trapp" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Hybrid_figure_resulting_from_secondary_contact.png/800px-Hybrid_figure_resulting_from_secondary_contact.png",
          caption: "Hybrid zones form via secondary contact: the geographic region where two species' ranges overlap and interbreed, typically with reduced hybrid fitness.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "The zone is in a TENSION balance: selection AGAINST hybrids removes intermediate genotypes, but continual GENE FLOW from each pure population at the zone's edges replenishes them. Net result: a narrow stable cline rather than collapse. The zone is maintained, not closed, because (a) selection against hybrids is strong but (b) parental migration from outside is constant. Bombina toad zones have been stable for ~5,000 years with this balance."
    },
    "Viable hybrid": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Helianthus_annuus_ariz.jpg/800px-Helianthus_annuus_ariz.jpg",
          caption: "Helianthus (sunflower). H. anomalus arose from hybridization of H. annuus × H. petiolaris and survives — and even outcompetes parents — on harsh substrates parents cannot occupy.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Hybrid_figure_resulting_from_secondary_contact.png/800px-Hybrid_figure_resulting_from_secondary_contact.png",
          caption: "Viable hybrids are the exception, not the rule — most show reduced fitness compared to parents.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Hybrids may be fit on a NEW substrate while still unfit on the parents' home substrates. The parent species each occupy their own niches; the hybrid colonizes a third (e.g., Helianthus anomalus on dunes that neither H. annuus nor H. petiolaris tolerate). Because the hybrid lineage diverges into its own niche, it does NOT compete directly with parents and gene flow back to parental species is selected against (hybrid offspring with parental backgrounds have reduced fitness on the new niche). Net: a stable third species, not a collapse."
    },
    // ---- flashcards-extra.js (gap-filling extras) ----
    "Speciation modes (geographic)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Speciation_modes.svg/800px-Speciation_modes.svg.png",
          caption: "Four geographic modes of speciation: allopatric, peripatric, parapatric, sympatric — gene flow runs from 0 (allopatric) to full (sympatric).",
          credit: "Wikimedia Commons / Ilmari Karonen" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Ensatina_eschscholtzii_ring_species.jpg/800px-Ensatina_eschscholtzii_ring_species.jpg",
          caption: "Ensatina ring species in California — a parapatric continuum where adjacent populations interbreed but the terminal forms do not.",
          credit: "Wikimedia Commons / public domain" }
      ]
    },
    "Prezygotic isolation barriers (5)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Speciation_by_Reinforcement_Schematic.svg/800px-Speciation_by_Reinforcement_Schematic.svg.png",
          caption: "Five prezygotic barrier types — temporal, behavioral, mechanical, gametic, habitat — all act before fertilization.",
          credit: "Wikimedia Commons / CC BY-SA" }
      ]
    },
    "Postzygotic isolation barriers (3)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Momo_260905.jpg/800px-Momo_260905.jpg",
          caption: "Mule — hybrid sterility (one of three postzygotic types: inviability, sterility, breakdown).",
          credit: "Wikimedia Commons / Public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Liger_couple.jpg/800px-Liger_couple.jpg",
          caption: "Ligers — another classic hybrid sterility example caused by chromosomal mismatch at meiosis.",
          credit: "Wikimedia Commons / Hkandy" }
      ]
    },
    "Sympatric speciation (when it actually works)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Polyploidization.svg/800px-Polyploidization.svg.png",
          caption: "Polyploidy in plants creates instant sympatric speciation — the strongest documented case of sympatric divergence.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Rhagoletis_pomonella.jpg/800px-Rhagoletis_pomonella.jpg",
          caption: "Apple maggot fly (Rhagoletis pomonella) — host shift from hawthorn to apple created an incipient sympatric race.",
          credit: "Wikimedia Commons / Joseph Berger" }
      ]
    }
  });

  // ============================================================
  // L17 — Biogeography, dispersal/vicariance, extinction, radiation
  // ============================================================
  window.addCardPatches('L17', {
    "Biogeography": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Map_of_Sunda_and_Sahul.svg/800px-Map_of_Sunda_and_Sahul.svg.png",
          caption: "Sunda and Sahul shelves with Wallace's line — biogeography reveals deep history when species distributions match continental shelf boundaries.",
          credit: "Wikimedia Commons / Maximilian Dörrbecker" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Pangaea_200Ma.jpg/800px-Pangaea_200Ma.jpg",
          caption: "Pangaea ~200 Mya. Marsupial distribution across Australia and South America makes sense only with continental drift.",
          credit: "Wikimedia Commons / Kieff" }
      ],
      exAnswer: "Marsupials reached Australia + South America during the Gondwana phase (~80–50 Mya) when Australia, Antarctica, and South America were connected. As Gondwana broke up, marsupials were 'rafted' on each continent — vicariance via continental drift. Today's distribution matches the geological history exactly. Independent creation cannot explain why both groups are marsupials AND why they share a deep ancestry shown by molecular phylogenies."
    },
    "Wallace line": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Map_of_Sunda_and_Sahul.svg/800px-Map_of_Sunda_and_Sahul.svg.png",
          caption: "Wallace's Line runs through the Lombok Strait (>250 m deep) — Bali sat on the Asian Sunda shelf, Lombok on the Australasian shelf during glacial low-sea-level periods.",
          credit: "Wikimedia Commons / Maximilian Dörrbecker" }
      ],
      exAnswer: "The boundary is the cleanest land-based biogeographic break on Earth. Despite tiny inter-island distances (Lombok Strait ~30 km), DEEP-WATER TRENCHES (>250 m) prevented colonization even at glacial lowstands. Tells us: (1) Asia and Australasia evolved separately for tens of millions of years; (2) deep-water trenches enforce isolation more strongly than wide shallow seas; (3) marsupials radiated in Australasia, placentals in Asia, with no overlap until human-mediated transport. Wallace himself recognized this in the 1850s — foundational for the field."
    },
    "Dispersal": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Darwin's finches reached the volcanic Galápagos (~1,000 km from mainland South America) by long-distance dispersal — the islands were never connected to any continent.",
          credit: "Wikimedia Commons / John Gould" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg/800px-Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg",
          caption: "Hawaiian honeycreepers (ʻIʻiwi shown) — Hawaiian biota arrived entirely by dispersal across open ocean.",
          credit: "Wikimedia Commons / USFWS" }
      ],
      exAnswer: "DISPERSAL — the ancestor of Darwin's finches blew or flew across ~1,000 km of open ocean from the South American mainland. The Galápagos are volcanic and never connected to any continent, so vicariance is impossible. Dispersal events are stochastic (one founder population at a time), often involve a small founder group (peripatric), and lead to founder-effect drift + local selection driving rapid divergence. The Galápagos finches are the canonical dispersal-then-adaptive-radiation case."
    },
    "Vicariance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Wegener_fossils-mapped.png/800px-Wegener_fossils-mapped.png",
          caption: "Wegener's fossil distribution map. Lystrosaurus, Glossopteris, Cynognathus, and Mesosaurus span Gondwanan continents — only continental connection at ~250 Mya can explain it.",
          credit: "Wikimedia Commons / Osvaldocangaspadilla" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Lystrosaurus_hedini_IMG_4469.jpg/800px-Lystrosaurus_hedini_IMG_4469.jpg",
          caption: "Lystrosaurus skeletal mount. Lystrosaurus fossils are found in South America, Africa, India, and Antarctica — direct vicariance evidence for Gondwana.",
          credit: "Wikimedia Commons / Ghedoghedo" }
      ],
      exAnswer: "VICARIANCE from Pangaean breakup. ~250 Mya, Lystrosaurus lived across Pangaea — its fossils are now found on every Gondwanan continent. The supercontinent then fragmented, isolating descendant lineages on each landmass. Distribution today reflects ancient connectivity, not present-day dispersal. Distinguished from dispersal by molecular clock: split times match the GEOLOGICAL TIMING of barrier formation. Glossopteris seed ferns (no ocean dispersal possible) reinforce the same conclusion."
    },
    "Standing diversity": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/APES_Final.svg/800px-APES_Final.svg.png",
          caption: "MacArthur-Wilson island biogeography: standing diversity is the equilibrium between immigration (decreases as species accumulate) and extinction (rises with crowding).",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Insular_Biogeography_%28Size%29.png/800px-Insular_Biogeography_%28Size%29.png",
          caption: "Larger islands sustain more species — area drives standing diversity through reduced extinction risk.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Larger islands have lower extinction rates: they support larger populations (less drift, fewer demographic stochastic crashes) and a wider variety of habitats (more niches). With extinction lower, the equilibrium standing diversity rises. Empirical: the species-area relationship S = cAᶻ where z ≈ 0.25 — log-log linear. So a 10× area increase yields roughly 10⁰·²⁵ ≈ 1.8× more species. Both islands are at equilibrium; the larger one just sustains a higher one."
    },
    "Turnover rate": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/APES_Final.svg/800px-APES_Final.svg.png",
          caption: "Equilibrium standing diversity is dynamic — species are constantly arriving and going extinct at the same rate. The turnover rate is the SHARED rate at equilibrium.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Turnover rate = 5 species/year (since immigration = extinction at equilibrium). High turnover means species composition is changing fast even when standing diversity is stable. For conservation: a static species count masks community reshuffling — protected reserves may keep S constant but lose the original endemic species. Simberloff & Wilson's mangrove fumigation experiments confirmed: total richness recovered in months, but species lists differed for years. Standing diversity is necessary but insufficient as a conservation metric."
    },
    "Adaptive radiation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Darwin's finches — ~14 species from one founder, each beak adapted to a different food source. Textbook adaptive radiation.",
          credit: "Wikimedia Commons / John Gould" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Sea_Life_Centre%2C_Blackpool_2016_009_-_Malawi_Cichlid.jpg/800px-Sea_Life_Centre%2C_Blackpool_2016_009_-_Malawi_Cichlid.jpg",
          caption: "African Rift Lake cichlids — hundreds of species in <1 Myr. Pharyngeal jaws were the key innovation enabling diet diversification.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Extinction_intensity.svg/800px-Extinction_intensity.svg.png",
          caption: "Extinction intensity through the Phanerozoic. Mammals radiated explosively after the K-Pg extinction (~66 Mya) cleared dinosaur ecospace.",
          credit: "Wikimedia Commons / SmokeyJoe" }
      ],
      exAnswer: "After K-Pg, dinosaur niches were vacant. Conditions making radiation possible: (1) ECOLOGICAL OPPORTUNITY — empty niches, no competitors. (2) ABSENCE OF PREDATORS — large terrestrial predators were extinct. (3) KEY INNOVATION already in place — endothermy, lactation, parental care made mammals adaptable. (4) GENETIC POTENTIAL — surviving lineages had enough variation to diversify. The pattern: rapid lineage-splitting into ecologically distinct species ('adaptive radiation'). Same template explains Galápagos finches (open islands), cichlid radiations (new lakes + pharyngeal jaws), and angiosperm radiation (flowers as key innovation)."
    },
    "Key innovation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Sea_Life_Centre%2C_Blackpool_2016_009_-_Malawi_Cichlid.jpg/800px-Sea_Life_Centre%2C_Blackpool_2016_009_-_Malawi_Cichlid.jpg",
          caption: "Cichlid pharyngeal jaws — a second set of throat 'jaws' independent of bite mechanics, freeing the oral jaws for diverse diets.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg/800px-Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg",
          caption: "Hawaiian honeycreeper feeding on native mint — flowers themselves were a key innovation that opened the vast pollinator niche.",
          credit: "Wikimedia Commons / USFWS" }
      ],
      exAnswer: "FLOWERS + FRUITS opened the pollinator + seed-disperser niches. Before angiosperms, gymnosperms relied on wind for pollen and lacked enclosed seeds. Flowers recruited insect (and later bird/mammal) pollinators — vastly more efficient and selective than wind. Fruits enlisted vertebrates to disperse seeds far from parents. These two innovations let angiosperms colonize habitats and form mutualisms gymnosperms couldn't, triggering the Cretaceous angiosperm radiation. Other key innovations: jaws (vertebrate radiation), wings (insect/bird/bat radiations), pharyngeal jaws (cichlid radiation)."
    },
    // ---- flashcards-extra.js (gap-filling extras) ----
    "Dispersal vs vicariance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Wegener_fossils-mapped.png/800px-Wegener_fossils-mapped.png",
          caption: "Wegener's fossil distribution map — Glossopteris, Lystrosaurus, Cynognathus, Mesosaurus span Gondwanan continents. Vicariance signature.",
          credit: "Wikimedia Commons / Osvaldocangaspadilla" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Darwin's finches reached Galápagos by dispersal — the islands were never connected to the mainland.",
          credit: "Wikimedia Commons / John Gould" }
      ]
    },
    "Equilibrium island biogeography (MacArthur-Wilson)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/APES_Final.svg/800px-APES_Final.svg.png",
          caption: "MacArthur-Wilson equilibrium model — immigration falls and extinction rises with species number; their crossing point sets S*.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Insular_Biogeography_%28Distance%29.png/800px-Insular_Biogeography_%28Distance%29.png",
          caption: "Distance effect — islands far from mainland have lower immigration, lower S*. Combined with size, predicts large-near > small-far.",
          credit: "Wikimedia Commons / public domain" }
      ]
    },
    "Wallace line — sharp biogeographic boundary": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Map_of_Sunda_and_Sahul.svg/800px-Map_of_Sunda_and_Sahul.svg.png",
          caption: "Sunda and Sahul shelves with Wallace's Line — the deep Lombok Strait (>250 m) never closed at glacial low sea levels, enforcing faunal isolation.",
          credit: "Wikimedia Commons / Maximilian Dörrbecker" }
      ]
    },
    "Hawaiian Drosophila — peripatric explosion": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg/800px-Iiwi_on_native_mint_-_Hakalau_Forest_NWR.jpg",
          caption: "Hawaiian endemics — like the ʻIʻiwi here, the Hawaiian Drosophila represent ~25% of world Drosophila diversity from one founder ~25 Mya.",
          credit: "Wikimedia Commons / USFWS" }
      ]
    },
    "Latitudinal diversity gradient": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Area_species_curve_herpetofauna.svg/800px-Area_species_curve_herpetofauna.svg.png",
          caption: "Species-area curves echo the latitudinal gradient — species richness drops with smaller area; richness peaks at the tropics.",
          credit: "Wikimedia Commons / public domain" }
      ]
    },
    "Continental drift — biogeographic evidence": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Pangaea_200Ma.jpg/800px-Pangaea_200Ma.jpg",
          caption: "Pangaea ~200 Mya — Glossopteris, Lystrosaurus, and marsupial distributions all match this configuration's vicariance signature.",
          credit: "Wikimedia Commons / Kieff" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Glossopteris_sp.%2C_seed_ferns%2C_Permian_-_Triassic_-_Houston_Museum_of_Natural_Science_-_DSC01765.JPG/800px-Glossopteris_sp.%2C_seed_ferns%2C_Permian_-_Triassic_-_Houston_Museum_of_Natural_Science_-_DSC01765.JPG",
          caption: "Glossopteris seed-fern fossil. Found across South America, Africa, India, Australia, Antarctica — seeds couldn't cross oceans, so continents must have been connected.",
          credit: "Wikimedia Commons / Daderot" }
      ]
    }
  });

  // ============================================================
  // L18 — Humans as selective force, conservation, climate change
  // ============================================================
  window.addCardPatches('L18', {
    "Selective harvest": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/New_Mexico_Bighorn_Sheep.JPG/800px-New_Mexico_Bighorn_Sheep.JPG",
          caption: "Bighorn ram with large curved horns. Trophy hunters target the largest-horned rams; horn size is heritable (h²~0.7), so selective harvest drives genetic decline.",
          credit: "Wikimedia Commons / U.S. Fish and Wildlife Service" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/USGS_ovis_canadensis_GNP_bighorn_rams_0.jpg/800px-USGS_ovis_canadensis_GNP_bighorn_rams_0.jpg",
          caption: "Ram Mountain, Alberta study: ~25% decline in mean horn size in 30 years of trophy hunting (Coltman et al. 2003).",
          credit: "Wikimedia Commons / USGS" }
      ],
      exAnswer: "DIRECTIONAL SELECTION on horn size, applied by humans. Horn size is highly heritable (h² ~0.7). Each generation, hunters remove the largest-horned (often prime-age breeding) rams BEFORE they mate fully. Mean horn size in the gene pool drops every generation. Reverses natural selection: in the wild, large horns won fights and mates → were favored. Humans now select AGAINST the very phenotype natural selection rewarded. The ironic result: hunters destroy what they value within a few decades of intense pressure."
    },
    "Fisheries-induced evolution": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Atlantic_cod.jpg/800px-Atlantic_cod.jpg",
          caption: "Atlantic cod (Gadus morhua) — under decades of size-selective fishing, mean maturation age dropped substantially. Fish that mature small and reproduce before reaching legal size escape the net.",
          credit: "Wikimedia Commons / Hans-Petter Fjeld" }
      ],
      exAnswer: "Size-selective fishing is STRONG DIRECTIONAL SELECTION on body size and age at maturity. Minimum-size limits ('keep only fish >50 cm') REMOVE all individuals that reach large size before reproducing. Fish that mature small/young and spawn before reaching legal size escape. Heritability of these life-history traits is moderate-to-high, so over 10–20 generations the population evolves earlier maturation + smaller size at first reproduction. Cod maturation age fell from ~6 to ~5 years over 30–40 years. The intended 'protection' actually selects on the wrong trait."
    },
    "Inbreeding depression": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Male_cheetah_facing_left_in_South_Africa.jpg/800px-Male_cheetah_facing_left_in_South_Africa.jpg",
          caption: "Cheetah — ancient population bottleneck (~10,000 years ago) left modern cheetahs with very low genetic diversity, low fertility, and high cub mortality.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Inbreeding_depression_in_Delphinium_nelsonii.png/800px-Inbreeding_depression_in_Delphinium_nelsonii.png",
          caption: "Inbreeding depression in Delphinium nelsonii: as inbreeding coefficient (F) rises, fitness components fall — exposed deleterious recessives.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Inbreeding raises homozygosity. Recessive deleterious alleles, normally hidden in heterozygotes, become exposed when homozygous → reduced fitness. In a 30-individual population, every individual is closely related, so any mating produces offspring homozygous for many deleterious alleles. Result: low conception rate, high embryonic + cub mortality, sperm abnormalities, structural defects. The mechanism: not allele frequency change (drift), but EXPRESSION of preexisting recessives. Population genetics fix: introduce unrelated individuals (genetic rescue)."
    },
    "Genetic rescue": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Everglades_National_Park_Florida_Panther.jpg/800px-Everglades_National_Park_Florida_Panther.jpg",
          caption: "Florida panther in Everglades National Park. The 1995 introduction of 8 Texas pumas reversed inbreeding-related defects within 2 generations.",
          credit: "Wikimedia Commons / National Park Service" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Florida_panther_family_%285164634982%29.jpg/800px-Florida_panther_family_%285164634982%29.jpg",
          caption: "Florida panther mother with cubs — population grew from ~30 (1990s) to ~200 (2010s) after genetic rescue.",
          credit: "Wikimedia Commons / U.S. Fish and Wildlife Service" }
      ],
      exAnswer: "Texas pumas were the historic gene-flow source for Florida panthers before Florida was isolated by human development — same subspecies, same ecological niche, but distinct gene pool with different alleles. The 8 introduced pumas brought NEW allelic variation. Their crosses with Florida panthers produced HETEROZYGOUS offspring, masking the deleterious recessives that had been exposed under inbreeding. Within 2 generations, kitten survival rose, heart defects + sperm abnormalities dropped, population grew ~7× (~30 → ~200). Worked because: (a) donors were genetically close (no outbreeding depression); (b) introduced enough variation; (c) the population was on an extinction trajectory without intervention."
    },
    "Fragmentation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Indiana_Dunes_Habitat_Fragmentation.jpg/800px-Indiana_Dunes_Habitat_Fragmentation.jpg",
          caption: "Habitat fragmentation at Indiana Dunes. Once-continuous forests broken into small isolated patches reduce gene flow and increase drift.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Sugarcane_Deforestation%2C_Bolivia%2C_2016-06-15_by_Planet_Labs.jpg/800px-Sugarcane_Deforestation%2C_Bolivia%2C_2016-06-15_by_Planet_Labs.jpg",
          caption: "Deforestation creates fragmentation: isolated remnant patches lose corridor connectivity, drive populations to small Ne.",
          credit: "Wikimedia Commons / Planet Labs" }
      ],
      exAnswer: "DEMOGRAPHIC: each patch supports a smaller population → more vulnerable to stochastic crashes (fire, disease, demographic chance). GENETIC: smaller Ne in each patch → drift dominates over selection (s < 1/2Ne); allelic diversity lost; inbreeding rises. CONNECTIVITY: gene flow between patches falls because the species can't fly; allele exchange that maintained shared variation stops. Long-term: each patch diverges genetically (drift); deleterious alleles fix; populations spiral toward extinction unless corridors are restored."
    },
    "Phenological shift": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg/800px-Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg",
          caption: "Pied flycatcher — migrates on photoperiod cues but European caterpillar prey peak earlier each year. Phenological mismatch reduces chick fitness.",
          credit: "Wikimedia Commons / Andreas Trepte" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Saalfeld_2021_bird_phenology.png/800px-Saalfeld_2021_bird_phenology.png",
          caption: "Arctic shorebird phenology shifts under warming — breeding events advancing earlier each decade.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Mechanisms: (a) PHENOTYPIC PLASTICITY — temperature-driven cues (degree-days, soil warmth) directly trigger leaf-out; no genetic change needed. (b) MICROEVOLUTION — selection favors earlier-leafing genotypes if early leaves capture more growing-season light. Both can act simultaneously. Mismatch concerns: (1) leafing trees may emerge before pollinators are active; (2) frost damage if leaf-out outpaces last frost dates; (3) decoupling from herbivore peaks (caterpillars, defoliators); (4) cascading effects on bird breeding timing tied to caterpillar peaks (pied flycatcher case)."
    },
    "Range shift": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bateman_2020_na_birds_shift.jpg/800px-Bateman_2020_na_birds_shift.jpg",
          caption: "Projected North American bird range shifts under warming — many species moving poleward and upslope.",
          credit: "Wikimedia Commons / Bateman et al. 2020" }
      ],
      exAnswer: "Mountain-top species are running out of altitude. As climate warms, the suitable thermal zone moves UP the mountain — but the mountain has a finite peak. Species can disperse upward, but eventually the cold-adapted species reach the summit and have NOWHERE COLDER TO GO. Lowland warm-tolerant species move up from below, compressing the cool refuge. Pikas and alpine flowers in the Rockies are already documented losing elevation. The 'escalator to extinction' problem — vertical limits cap range expansion in a way horizontal shifts don't."
    },
    "Conservation biology": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Status_iucn3.1.svg/800px-Status_iucn3.1.svg.png",
          caption: "IUCN Red List categories — conservation biology integrates evolutionary, ecological, and population-genetic principles to assess extinction risk.",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Extinction_intensity.svg/800px-Extinction_intensity.svg.png",
          caption: "Phanerozoic extinction intensity. The current 'Sixth Extinction' is human-driven; conservation biology aims to mitigate it.",
          credit: "Wikimedia Commons / SmokeyJoe" }
      ],
      exAnswer: "Conservation is fundamentally evolutionary because (1) the units of biodiversity (species, populations, genetic lineages) are products of evolution; (2) the threats (inbreeding depression, drift in small populations, adaptation to anthropogenic change) are evolutionary processes; (3) interventions like genetic rescue, captive breeding, and assisted migration require evolutionary thinking (effective population size, allele frequencies, hybridization risk); (4) climate adaptation requires understanding the species' adaptive potential. Pure ecology without evolutionary genetics gives short-term population management, not long-term species persistence."
    },
    "Captive breeding": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg/800px-California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg",
          caption: "California condor in flight. By 1987 only 22 wild birds remained — all captured for captive breeding. Population now ~500, ~half wild.",
          credit: "Wikimedia Commons / Don Graham" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Arabian_oryx_%28oryx_leucoryx%29.jpg/800px-Arabian_oryx_%28oryx_leucoryx%29.jpg",
          caption: "Arabian oryx — extinct in the wild by 1972, restored from captive populations. Demonstrates captive breeding's reintroduction success when threats are addressed.",
          credit: "Wikimedia Commons / public domain" }
      ],
      exAnswer: "Forces at work: (1) DRIFT — small Ne in captivity erodes allelic variation; rare alleles lost. (2) INBREEDING — limited founders → high relatedness → exposed recessives. (3) DOMESTICATION SELECTION — alleles favoring tameness, captive feeding, easy reproduction become enriched while wild-type alleles fade; reduces post-release fitness. (4) FOUNDER EFFECTS — initial captives capture only a sample of wild variation. Mitigations: pedigree management to minimize relatedness, large founder populations, periodic addition of wild individuals, minimize handling, limited captive duration before release, and using wild-trained breeders."
    },
    // ---- flashcards-extra.js (gap-filling extras) ----
    "Fisheries-induced evolution — size selection": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Atlantic_cod.jpg/800px-Atlantic_cod.jpg",
          caption: "Atlantic cod (Gadus morhua). Size-selective fishing removes large/late-maturing fish; the population evolves toward earlier, smaller maturation in 10–20 generations.",
          credit: "Wikimedia Commons / Hans-Petter Fjeld" }
      ]
    },
    "Bighorn sheep trophy hunting → smaller horns": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/New_Mexico_Bighorn_Sheep.JPG/800px-New_Mexico_Bighorn_Sheep.JPG",
          caption: "Bighorn ram. On Ram Mountain, Alberta, mean horn size declined ~25% over 30 years of trophy hunting (Coltman et al. 2003).",
          credit: "Wikimedia Commons / U.S. Fish and Wildlife Service" }
      ]
    },
    "Florida panther genetic rescue": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Everglades_National_Park_Florida_Panther.jpg/800px-Everglades_National_Park_Florida_Panther.jpg",
          caption: "Florida panther. By the 1990s the wild population was ~30; introduction of 8 Texas pumas in 1995 reversed inbreeding-related defects within 2 generations.",
          credit: "Wikimedia Commons / National Park Service" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Florida_panther_family_%285164634982%29.jpg/800px-Florida_panther_family_%285164634982%29.jpg",
          caption: "Florida panther family — population grew to ~200 by the 2010s following genetic rescue.",
          credit: "Wikimedia Commons / U.S. Fish and Wildlife Service" }
      ]
    },
    "Inbreeding depression mechanism": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Inbreeding_depression_in_Delphinium_nelsonii.png/800px-Inbreeding_depression_in_Delphinium_nelsonii.png",
          caption: "Inbreeding depression in Delphinium nelsonii — fitness components fall with rising inbreeding coefficient (F).",
          credit: "Wikimedia Commons / public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Male_cheetah_facing_left_in_South_Africa.jpg/800px-Male_cheetah_facing_left_in_South_Africa.jpg",
          caption: "Cheetah — ancient bottleneck left modern cheetahs with very low genetic diversity, a population-genetic textbook case.",
          credit: "Wikimedia Commons / public domain" }
      ]
    },
    "Climate change → range shifts and phenological mismatch": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg/800px-Ficedula_hypoleuca_-Wood_of_Cree_Nature_Reserve%2C_Scotland_-male-8a.jpg",
          caption: "Pied flycatcher — migrates on photoperiod cues but European caterpillar prey peaks earlier each year due to warming. Mismatch reduces chick fitness.",
          credit: "Wikimedia Commons / Andreas Trepte" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bateman_2020_na_birds_shift.jpg/800px-Bateman_2020_na_birds_shift.jpg",
          caption: "Projected North American bird range shifts under warming — many species moving poleward and upslope.",
          credit: "Wikimedia Commons / Bateman et al. 2020" }
      ]
    },
    "Captive breeding + reintroduction (California condor)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg/800px-California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg",
          caption: "California condor in flight. By April 1987, all 22 surviving wild birds had been captured. The species now numbers ~500 with ~half free-flying.",
          credit: "Wikimedia Commons / Don Graham" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Gymnogyps_californianus1.jpg/800px-Gymnogyps_californianus1.jpg",
          caption: "Condor chick fed by puppet to avoid imprinting on humans — pedigree-managed captive breeding minimized inbreeding from a 27-bird founder population.",
          credit: "Wikimedia Commons / U.S. Fish and Wildlife Service" }
      ]
    }
  });
})();
