/* Importance content (group 5: L16, L17, L18) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  window.addCardPatches('L16', {
    "Biological Species Concept (BSC)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> The BSC (Mayr 1942) defines species by reproductive isolation — gene flow is the test, not looks.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>1942</strong> — Ernst Mayr formalized the BSC in <em>Systematics and the Origin of Species</em>.</li>
  <li>Two failure modes: <strong>asexual organisms</strong> (no interbreeding to test) and <strong>fossils</strong> (can't run mating trials).</li>
  <li>The criterion is <strong>reproductive isolation</strong>, not morphology — cryptic species can look identical and still be separate.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the default species concept in animal biology.</strong> Robbins will hit you on this — when an exam question doesn't specify a concept and the organism is sexually reproducing, BSC is the answer.</li>
  <li><strong>Mechanistic, not descriptive.</strong> Unlike morphological or phylogenetic concepts, BSC tells you WHY species are distinct: gene flow has stopped.</li>
  <li><strong>Failure cases are exam-trap territory.</strong> Bacteria, asexual lizards, and fossils can't be diagnosed by BSC — that's where alternative concepts step in.</li>
</ol>
<h4>Watch for</h4>
<ul>
  <li>Hybridization does NOT automatically falsify species status — partial gene flow with reduced hybrid fitness still satisfies "reproductively isolated" in the long run.</li>
</ul>
`
    },
    "Morphological species concept": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Diagnose species by visible (or measurable) form differences — the only concept that works for fossils.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Pre-Mayr (pre-1942), morphology was the ONLY species concept available — Linnaeus through Darwin used it.</li>
  <li>Two failure modes: <strong>cryptic species</strong> (genetically distinct, look identical) and <strong>polymorphic species</strong> (one species, many morphs).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Paleontology runs on this.</strong> You can't test interbreeding in a 250-million-year-old trilobite — bones, teeth, and shells are all you have.</li>
  <li><strong>Quick and operational.</strong> Field biologists triage species this way before molecular work confirms.</li>
  <li><strong>Robbins will hit you on this:</strong> when the question is about fossils, morphological is the answer; when the question is about reproductive isolation, BSC is the answer.</li>
</ol>
<h4>Key takeaway</h4>
<ul>
  <li>Morphological errors are systematic — sexual dimorphism, life-stage differences, and cryptic species all produce wrong species counts.</li>
</ul>
`
    },
    "Phylogenetic species concept": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> A species = the smallest monophyletic group with shared derived characters — works for everything, including asexuals.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Tends to <strong>SPLIT</strong> lineages aggressively: any diagnosable monophyletic group qualifies.</li>
  <li>Often produces 2-3× more species than BSC for the same group.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Universal applicability.</strong> Bacteria, fungi, asexual rotifers — PSC handles them all because it's based on cladistic logic, not interbreeding.</li>
  <li><strong>Cladistic rigor.</strong> Forces you to identify shared derived characters (synapomorphies) — defensible even when reproductive data are missing.</li>
  <li><strong>Exam-trap territory:</strong> PSC and BSC can disagree about the same population pair. PSC will often "see" species the BSC misses.</li>
</ol>
<h4>Watch for</h4>
<ul>
  <li>Sensitive to which characters and which taxa you sample — different datasets can yield different "species" boundaries.</li>
</ul>
`
    },
    "Prezygotic isolation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Anything that prevents fertilization between species is prezygotic — no zygote is ever formed.</p>
<h4>The five barrier types (memorize these)</h4>
<ul>
  <li><strong>Temporal</strong> — different breeding times (different seasons, day vs night).</li>
  <li><strong>Behavioral</strong> — different courtship signals, songs, displays.</li>
  <li><strong>Mechanical</strong> — incompatible reproductive structures (insect genitalia, flower morphology).</li>
  <li><strong>Gametic</strong> — sperm/pollen can't fertilize the egg (incompatible surface proteins).</li>
  <li><strong>Habitat/Ecological</strong> — different microhabitats; rarely encounter each other.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Prezygotic barriers are "efficient."</strong> No gametes wasted, no parental investment in doomed embryos. That's why selection (reinforcement) tends to strengthen them.</li>
  <li><strong>The dividing line is fertilization.</strong> Robbins will hit you on this — if a barrier acts BEFORE the zygote forms, it's prezygotic; AFTER, postzygotic.</li>
  <li><strong>Categorization is the classic exam question:</strong> "Two orchids bloom at different seasons — what type of isolation?" → temporal prezygotic.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>T-B-M-G-H</strong>: Temporal, Behavioral, Mechanical, Gametic, Habitat.</li>
</ul>
`
    },
    "Postzygotic isolation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Zygote forms but the cross fails — hybrid problems prevent gene flow despite successful fertilization.</p>
<h4>The three types (memorize these)</h4>
<ul>
  <li><strong>Hybrid inviability</strong> — embryo fails to develop or dies young.</li>
  <li><strong>Hybrid sterility</strong> — hybrid lives but cannot reproduce (mules, ligers).</li>
  <li><strong>Hybrid breakdown</strong> — F1 fine and fertile, but F2/backcross collapse (Dobzhansky-Muller incompatibilities exposed by segregation).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Wasteful, hence selection pressure for prezygotic barriers.</strong> Postzygotic costs (failed embryos, sterile young) drive REINFORCEMENT in secondary contact.</li>
  <li><strong>Hybrid breakdown is the Dobzhansky-Muller signature.</strong> F1 is heterozygous and buffered; F2 segregation creates novel homozygous combinations that expose negative epistasis.</li>
  <li><strong>Robbins will hit you on this:</strong> inviability ≠ sterility. Inviability means the hybrid DIES; sterility means it LIVES but can't reproduce.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>I-S-B</strong>: Inviable, Sterile, Breakdown.</li>
</ul>
`
    },
    "Hybrid sterility": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> The mule is the textbook example — hybrid lives but can't pass genes on.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Mule</strong> = horse (64 chromosomes) × donkey (62 chromosomes) → mule (63 chromosomes). Odd number → meiosis fails → sterile.</li>
  <li>Liger, tigon, zorse — same pattern: chromosomal mismatch breaks meiosis.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Chromosomal evidence of divergence.</strong> Hybrid sterility tells you the parent species have accumulated independent karyotype changes — pairing fails because chromosomes can't synapse correctly.</li>
  <li><strong>It's a postzygotic barrier — gene flow is blocked even though hybrids exist.</strong> Robbins exam-trap: a sterile hybrid does NOT mean the parents are the same species under the BSC.</li>
  <li><strong>Haldane's rule territory:</strong> in many crosses, the heterogametic sex (XY in mammals, ZW in birds) is preferentially sterile or inviable.</li>
</ol>
`
    },
    "Allopatric speciation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Geography splits the population, divergence accumulates, reproductive isolation evolves — the DEFAULT mode in animals.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Most common mode</strong> in animals — assume it unless told otherwise.</li>
  <li>Two flavors: <strong>vicariance</strong> (a barrier rises within the range) and <strong>dispersal</strong> (founders cross an existing barrier).</li>
  <li>Classic example: <strong>Kaibab vs Abert squirrels</strong> split by the Grand Canyon.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Geography eliminates gene flow.</strong> Once gene flow stops, drift and divergent selection can do their work without being homogenized.</li>
  <li><strong>It's the null hypothesis</strong> for most speciation questions — if Robbins doesn't say otherwise, allopatric is the safe answer.</li>
  <li><strong>Sets up reinforcement.</strong> When allopatric populations later come back into contact, partial isolation can be completed by selection against unfit hybrids.</li>
</ol>
<h4>Watch for</h4>
<ul>
  <li>Don't confuse allopatric (geographic separation) with peripatric (small founder pop). Peripatric is a SUBTYPE of allopatric where founders are few — drift is much stronger.</li>
</ul>
`
    },
    "Sympatric speciation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> New species form in the SAME geographic range — rare in animals, common in plants via polyploidy.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Polyploidy</strong> (chromosome doubling) → instant reproductive isolation in ONE generation. Common in plants.</li>
  <li><strong>~50-70%</strong> of flowering plant species are estimated to have polyploid origins.</li>
  <li>Animal example: <strong>Rhagoletis pomonella</strong> (apple maggot fly) — host shift from hawthorn to apple, partial reproductive isolation by host preference.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Challenges the "geography required" intuition.</strong> Sympatric speciation requires strong disruptive selection + assortative mating — and polyploidy provides both at once.</li>
  <li><strong>Why plants and not animals?</strong> Animal sex determination (XY/ZW) usually can't tolerate doubled chromosome sets. Plants are far more permissive.</li>
  <li><strong>Robbins will hit you on this:</strong> "Polyploid speciation in plants" → sympatric. The trap is thinking sympatric = no isolation; the isolation is genetic (chromosomes), not geographic.</li>
</ol>
`
    },
    "Reinforcement": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Selection STRENGTHENS prezygotic isolation when populations meet again and hybrids are unfit — Dobzhansky's idea, completes speciation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Coined by <strong>Dobzhansky (1940)</strong>.</li>
  <li>Diagnostic signature: <strong>greater prezygotic divergence in sympatric (overlap) zones than in allopatric zones</strong> of the same species pair.</li>
  <li>Classic example: <strong>pied vs collared flycatchers</strong> in Europe — song differences are stronger in overlap zones than in pure-population zones.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Completes speciation that allopatry started.</strong> Initial divergence happens in geographic isolation; reinforcement finishes the job in secondary contact.</li>
  <li><strong>Requires unfit hybrids.</strong> No postzygotic cost → no selection for stronger prezygotic barriers → no reinforcement.</li>
  <li><strong>Robbins will hit you on this:</strong> reinforcement is a SECONDARY-CONTACT phenomenon. Without prior allopatric divergence, there's nothing to reinforce.</li>
</ol>
<h4>Key takeaway</h4>
<ul>
  <li>The asymmetric pattern (more divergence in sympatry than allopatry) is the diagnostic test for active reinforcement.</li>
</ul>
`
    },
    "Hybrid zone": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> A geographic strip where two species meet, interbreed, and produce reduced-fitness hybrids — a natural lab for studying speciation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Bombina bombina × B. variegata</strong> (fire-bellied vs yellow-bellied toads): a narrow zone in Central Europe, stable for thousands of years, ~10 km wide.</li>
  <li>This is a <strong>tension zone</strong> — selection against hybrids balanced by gene flow from outside.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Hybrid zones reveal incomplete reproductive isolation in real time.</strong> They're snapshots of speciation in progress.</li>
  <li><strong>Stable doesn't mean static.</strong> Tension zones persist because hybrid mortality continually removes hybrids while gene flow continually replenishes them.</li>
  <li><strong>Hybrids existing does NOT collapse species status.</strong> Robbins will hit you on this — reduced hybrid fitness keeps the parental species genetically distinct.</li>
</ol>
<h4>Watch for</h4>
<ul>
  <li>Sometimes hybrids THRIVE in intermediate environments — that's where hybrid speciation can occur (sunflowers, see Helianthus).</li>
</ul>
`
    },
    "Viable hybrid": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Hybrids that survive but typically have reduced fitness — and occasionally found new lineages (Helianthus).</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Helianthus anomalus, H. paradoxus, H. deserticola</strong> — three sunflower species formed by ancient HOMOPLOID hybrid speciation (no chromosome doubling) between H. annuus × H. petiolaris.</li>
  <li>Hybrid sunflowers thrive in EXTREME habitats (sand dunes, salt marshes, deserts) where neither parent does well.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Hybrids aren't always failures.</strong> In NOVEL ecological niches, hybrid genotypes can outperform both parents — opening the door to hybrid speciation.</li>
  <li><strong>Allopolyploid hybrid speciation</strong> (with chromosome doubling) is even more common in plants — wheat, cotton, tobacco are all polyploid hybrids.</li>
  <li><strong>Exam-trap territory:</strong> "viable hybrids exist" doesn't mean the parents are one species — it means reproductive isolation is incomplete or that hybrid speciation is occurring.</li>
</ol>
`
    },
    "Speciation modes (geographic)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Four modes ranked by gene flow during divergence: allopatric (none) → peripatric (none, small founder) → parapatric (some) → sympatric (full).</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Allopatric</strong>: full geographic separation. Most common in animals. Example: Kaibab/Abert squirrels (Grand Canyon).</li>
  <li><strong>Peripatric</strong>: small founder population isolated. Drift dominates. Example: <strong>Hawaiian Drosophila — ~1,000 endemic species</strong> from one ancestor in ~25 MYA.</li>
  <li><strong>Parapatric</strong>: adjacent ranges with cline/contact zone. Some gene flow. Example: grass populations adapted to mine tailings vs uncontaminated soil.</li>
  <li><strong>Sympatric</strong>: same range. Example: Rhagoletis apple maggot fly host shift; plant polyploidy.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Geography is the master variable.</strong> The amount of geographic mixing during divergence determines what mechanisms operate (drift, selection, assortative mating).</li>
  <li><strong>Peripatric speciation is fastest.</strong> Small Ne → strong drift → rapid fixation of novel alleles. Hawaiian Drosophila are the textbook example.</li>
  <li><strong>Robbins will hit you on this:</strong> match the mode to the example. Polyploidy → sympatric. Founder on remote island → peripatric. Contact zone with cline → parapatric.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>APPS</strong>: Allopatric · Peripatric · Parapatric · Sympatric (gene-flow level: 0 → 0 → some → full).</li>
</ul>
`
    },
    "Prezygotic isolation barriers (5)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Five barrier categories prevent fertilization — memorize them with the T-B-M-G-H mnemonic.</p>
<h4>The five barriers (memorize these)</h4>
<ul>
  <li><strong>Temporal</strong> — different breeding seasons or daily times. Example: Eastern vs Western spotted skunks breed at different times.</li>
  <li><strong>Behavioral</strong> — different mating displays/songs. Example: blue-footed vs red-footed boobies have different courtship dances.</li>
  <li><strong>Mechanical</strong> — incompatible structures. Example: snail genitalia chirality (left- vs right-coiled).</li>
  <li><strong>Gametic</strong> — sperm/eggs don't recognize. Example: sea urchin bindin proteins are species-specific.</li>
  <li><strong>Habitat/Ecological</strong> — different microhabitats. Example: parasite host specificity.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Prezygotic barriers are evolutionarily efficient.</strong> No gametes wasted; selection FAVORS strengthening them whenever postzygotic costs exist.</li>
  <li><strong>Categorization is THE classic exam question.</strong> Robbins will give you a scenario and ask which barrier — memorize the five.</li>
  <li><strong>Reinforcement targets prezygotic barriers</strong> in secondary contact, especially behavioral and gametic ones.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>T-B-M-G-H</strong>: Temporal · Behavioral · Mechanical · Gametic · Habitat.</li>
</ul>
`
    },
    "Postzygotic isolation barriers (3)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Three types of post-fertilization failure — memorize the I-S-B sequence.</p>
<h4>The three barriers (memorize these)</h4>
<ul>
  <li><strong>Hybrid inviability</strong> — embryo dies. Example: many fish/frog crosses.</li>
  <li><strong>Hybrid sterility</strong> — F1 lives but can't reproduce. Example: <strong>mule</strong> (horse 64 chr × donkey 62 chr → 63 chr, odd, meiosis fails).</li>
  <li><strong>Hybrid breakdown</strong> — F1 fine, F2/backcross collapse. Example: cotton, rice species crosses.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Hybrid breakdown is the Dobzhansky-Muller signature.</strong> F1 heterozygotes mask incompatibilities; F2 segregation exposes them as homozygous combinations selection has never tested.</li>
  <li><strong>Postzygotic costs drive reinforcement.</strong> Without them, no selection for stronger prezygotic barriers.</li>
  <li><strong>Robbins will hit you on this:</strong> inviability ≠ sterility. Memorize the distinction — embryo death vs adult sterility.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>I-S-B</strong>: Inviable · Sterile · Breakdown.</li>
</ul>
`
    },
    "Sympatric speciation (when it actually works)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Sympatric speciation needs polyploidy, host shifts, or strong disruptive selection — rare in animals, common in plants.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>~50-70%</strong> of flowering plants are polyploid in origin — instant reproductive isolation in ONE generation.</li>
  <li><strong>Rhagoletis pomonella</strong> shifted from hawthorn to apple in ~150 years (since apple introduction in North America).</li>
  <li><strong>Cichlids in Lake Victoria</strong>: hundreds of species in <15,000 years — possibly via sexual selection and ecological niche differentiation.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Polyploidy = instant speciation.</strong> Tetraploid × diploid → triploid (sterile). Reproductive isolation appears in ONE generation, no geography required.</li>
  <li><strong>Host shifts create assortative mating</strong> — Rhagoletis flies mate on the host plant they emerged from, partially isolating apple-race from hawthorn-race.</li>
  <li><strong>Why animals struggle:</strong> XY/ZW sex determination usually breaks under polyploidy. Plants tolerate genome duplication far better.</li>
</ol>
`
    }
  });

  window.addCardPatches('L17', {
    "Biogeography": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Biogeography studies WHERE species live and WHY — and the patterns are clues to deep history.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Founded by <strong>Alfred Russel Wallace</strong> (independent co-discoverer of natural selection) — his 1876 <em>Geographical Distribution of Animals</em> is the foundational text.</li>
  <li>Modern biogeography integrates <strong>plate tectonics, climate history, dispersal ability, and ecology</strong>.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Geographic patterns are evidence for evolution.</strong> Marsupials in Australia/S. America, finches on the Galápagos, lungfish in three Gondwanan continents — none make sense under independent creation.</li>
  <li><strong>Tests vicariance vs dispersal hypotheses.</strong> Molecular dating + paleogeography show which pattern produced which distribution.</li>
  <li><strong>Robbins will hit you on this:</strong> any question about why X lives in Y is a biogeography question. Always think history (vicariance/dispersal) + ecology (climate/niche).</li>
</ol>
`
    },
    "Wallace line": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> A sharp faunal boundary in Indonesia — placental mammals on the west, marsupials and cockatoos on the east — separated by deep ocean trenches.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Runs <strong>between Bali (Asian biota) and Lombok (Australasian biota)</strong>, and between Borneo (Asian) and Sulawesi (Australasian).</li>
  <li>The <strong>Lombok Strait is &gt;250 m deep</strong> and never closed during glacial sea-level lows — animals couldn't walk across.</li>
  <li>Discovered by <strong>Alfred Russel Wallace</strong> in the 1850s during his Malay Archipelago travels.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The cleanest land-based biogeographic boundary on Earth.</strong> Faunas switch in &lt;30 km — placental mammals vs marsupials, woodpeckers vs cockatoos.</li>
  <li><strong>Deep-water trenches enforce isolation</strong> over geological timescales — Bali was connected to Asia at glacial maxima; Lombok never was.</li>
  <li><strong>Exam-trap territory:</strong> the line isn't about distance, it's about geological history. Two islands close in space can be on opposite sides of the boundary.</li>
</ol>
`
    },
    "Dispersal": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Organisms cross an EXISTING barrier to reach a new place — the lineage moved, the geography didn't.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Galápagos finches</strong> reached the islands by dispersal across ~1,000 km of open ocean from mainland South America.</li>
  <li><strong>Hawaiian biota</strong> arrived entirely by dispersal — the islands are volcanic and never connected to any continent.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Dispersal is one of two explanations</strong> for related species in different places (the other is vicariance).</li>
  <li><strong>Diagnostic test:</strong> dispersal can occur ANY time after the barrier exists, while vicariance must match the timing of barrier formation.</li>
  <li><strong>Robbins will hit you on this:</strong> if you see "remote island," think dispersal. If you see "ancient continental connection," think vicariance.</li>
</ol>
<h4>Key takeaway</h4>
<ul>
  <li>Birds, oceanic taxa, and wind-dispersed plants are dispersal-prone. Flightless mammals and freshwater fish rarely disperse — vicariance fits them better.</li>
</ul>
`
    },
    "Vicariance": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> A NEW barrier rises within a continuous range — the lineage didn't move, the geography did.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Pangaea breakup</strong> began ~200 MYA; Atlantic Ocean opened ~120 MYA → splits African and South American biotas.</li>
  <li><strong>Glossopteris</strong> seed-fern fossils on every Gondwanan continent (S. America, Africa, India, Australia, Antarctica) — this plant could NOT cross oceans, so the continents must have been connected.</li>
  <li><strong>Lystrosaurus</strong> fossils (~250 MYA) on three continents — same vicariance signature.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Continental drift evidence.</strong> Wegener's drift hypothesis was confirmed in part by biogeographic distributions that demanded ancient land connections.</li>
  <li><strong>Test:</strong> vicariant splits should match the GEOLOGICAL TIMING of barrier formation. Molecular clocks can falsify or confirm.</li>
  <li><strong>Robbins will hit you on this:</strong> Gondwanan biota = vicariance. Volcanic island fauna = dispersal.</li>
</ol>
<h4>Key takeaway</h4>
<ul>
  <li>Mnemonic: <strong>Dispersal moves; Vicariance divides</strong>.</li>
</ul>
`
    },
    "Standing diversity": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> The number of species in a region at one time — a SNAPSHOT, not a rate.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Standing diversity = (cumulative origination + immigration) − (cumulative extinction + emigration).</li>
  <li><strong>Larger islands</strong> hold more species (lower extinction rate); <strong>islands closer to mainland</strong> hold more species (higher immigration).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Equilibrium island biogeography (MacArthur-Wilson)</strong> predicts S* from immigration and extinction curves.</li>
  <li><strong>It's a snapshot.</strong> Two communities can have the same standing diversity but very different turnover rates — don't conflate them.</li>
  <li><strong>Robbins will hit you on this:</strong> "Standing diversity stable" does NOT mean "no extinction" — at equilibrium, extinctions and immigrations balance.</li>
</ol>
`
    },
    "Turnover rate": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> The RATE at which species replace each other — a different concept from standing diversity.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Standing diversity = static count. Turnover rate = species per unit time entering/leaving.</li>
  <li><strong>Simberloff & Wilson's mangrove fumigation experiment (1969):</strong> after defaunation, total species count returned within months but identity of the species was different — equilibrium standing diversity, high turnover.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Equilibrium is dynamic, not static.</strong> At MacArthur-Wilson equilibrium, immigration rate = extinction rate, but species are constantly being lost and replaced.</li>
  <li><strong>Conservation implication:</strong> protecting a species count is not the same as protecting the SPECIES. Turnover means membership changes even when totals are stable.</li>
  <li><strong>Robbins will hit you on this:</strong> standing diversity is a snapshot; turnover is a rate. Two communities with identical species counts can differ wildly in turnover.</li>
</ol>
`
    },
    "Adaptive radiation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> One lineage rapidly diversifies into many ecologically distinct species — the textbook examples are Galápagos finches, Hawaiian honeycreepers, and African cichlids.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Galápagos finches</strong>: ~14-18 species from a single founder ancestor in &lt;3 MYA.</li>
  <li><strong>Hawaiian honeycreepers</strong>: ~50 species from one ancestor in ~5 MYA.</li>
  <li><strong>African cichlids (Lake Victoria)</strong>: ~500 species in &lt;15,000 years (yes, thousands not millions).</li>
  <li><strong>Mammals after K-Pg (~66 MYA)</strong>: explosive radiation into dinosaur-vacated niches.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Four classic triggers:</strong> (1) mass extinction clearing niches, (2) colonization of unfilled habitat, (3) key innovation opening new niches, (4) geological/climatic shifts.</li>
  <li><strong>Different from regular speciation.</strong> Adaptive radiation = fast diversification INTO DIFFERENT NICHES. Speciation alone doesn't require ecological differentiation.</li>
  <li><strong>Robbins will hit you on this:</strong> if a question asks about post-extinction biodiversity recovery or island endemic explosions, "adaptive radiation" is the answer.</li>
</ol>
<h4>Key takeaway</h4>
<ul>
  <li>Mammals existed before the K-Pg — they were just small and ecologically restricted. The extinction REMOVED dinosaur competitors and let mammals diversify into the empty niches.</li>
</ul>
`
    },
    "Key innovation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> An evolutionary novelty that opens new ecological possibilities — and often triggers an adaptive radiation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Jaws</strong> → vertebrate radiation (~440 MYA).</li>
  <li><strong>Flowers + fruits</strong> → angiosperm radiation (~130 MYA, now ~300,000 species).</li>
  <li><strong>Pharyngeal jaws</strong> (second set of jaws in throat) → cichlid radiation (~500 species in Lake Victoria alone).</li>
  <li><strong>Powered flight</strong> → bird/bat/insect radiations.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Innovations open new ecological space.</strong> Without flowers, no fruit-eating birds, no pollinator-plant coevolution, no angiosperm dominance.</li>
  <li><strong>One trigger of adaptive radiation</strong> alongside mass extinction, colonization, and climate shifts.</li>
  <li><strong>Robbins will hit you on this:</strong> match the innovation to the radiation. Cichlids → pharyngeal jaws. Angiosperms → flowers. Beetles → wings + sclerotization.</li>
</ol>
`
    },
    "Dispersal vs vicariance": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Two competing explanations for related species in different places — molecular dating decides between them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Dispersal</strong>: organism moves across an EXISTING barrier. Any timing.</li>
  <li><strong>Vicariance</strong>: a NEW barrier (mountain rise, ocean opening, continental drift) splits a continuous range. Timing must match the geological event.</li>
  <li><strong>Atlantic Ocean opening</strong>: ~120 MYA — vicariant splits between African and South American biota should date here.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Mnemonic: Dispersal moves; Vicariance divides.</strong></li>
  <li><strong>The molecular clock decides.</strong> If sister taxa split at ~120 MYA matching Atlantic opening → vicariance fits. If at ~30 MYA → dispersal required.</li>
  <li><strong>Robbins will hit you on this:</strong> not every continental disjunct distribution is vicariance — birds, primates, and rodents have all been shown to disperse across major barriers.</li>
</ol>
`
    },
    "Equilibrium island biogeography (MacArthur-Wilson)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Standing species count = balance between immigration (decreasing as island fills) and extinction (increasing with more species).</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>1967</strong>: MacArthur & Wilson publish <em>The Theory of Island Biogeography</em>.</li>
  <li>Two predictors of S*: <strong>island size</strong> (bigger = lower extinction) and <strong>distance from source</strong> (closer = higher immigration).</li>
  <li><strong>Highest S*</strong>: large island close to mainland. <strong>Lowest S*</strong>: small island far away.</li>
  <li><strong>Simberloff & Wilson (1969)</strong>: defaunated Florida mangrove islets recovered to original species counts in months — equilibrium confirmed empirically.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Predictive theory in biogeography.</strong> Made falsifiable predictions about species counts; experimentally confirmed.</li>
  <li><strong>Equilibrium is DYNAMIC.</strong> At S*, species are constantly being lost and replaced — turnover continues even when totals stabilize.</li>
  <li><strong>Conservation foundation.</strong> Reserve design (size, connectivity) draws directly from MacArthur-Wilson logic.</li>
</ol>
`
    },
    "Wallace line — sharp biogeographic boundary": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> The sharpest land-based biogeographic boundary on Earth — Asian vs Australasian biota separated by a deep-water trench.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Discovered by <strong>Alfred Russel Wallace</strong> (1850s, during his ~8-year Malay Archipelago expedition).</li>
  <li>Boundary runs between <strong>Bali/Lombok</strong> and between <strong>Borneo/Sulawesi</strong>.</li>
  <li><strong>Lombok Strait &gt;250 m deep</strong> — never closed during Pleistocene sea-level lows (~120 m drop).</li>
  <li>Faunal switch in &lt;30 km: placental mammals + woodpeckers (west) vs marsupials + cockatoos (east).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Geological history beats geographic distance.</strong> Bali sat on the Sunda Shelf with Asia; Lombok sat on the Sahul Shelf with Australia. The strait between them stayed open even when seas dropped.</li>
  <li><strong>Tens of millions of years of isolation</strong> produced two completely different mammal faunas on islands ~30 km apart.</li>
  <li><strong>Robbins will hit you on this:</strong> the line is about deep-water barriers, not surface distance.</li>
</ol>
`
    },
    "Hawaiian Drosophila — peripatric explosion": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> ~1,000 endemic Drosophila species (>25% of world's Drosophila diversity) on a chain of islands &lt;2,000 km long — textbook peripatric radiation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>~800-1,000 endemic species</strong> in the Hawaiian Islands (more than 25% of all Drosophila species worldwide).</li>
  <li>All descend from a <strong>single colonizer ~25 MYA</strong>.</li>
  <li>Each new volcanic island colonized by a few founders → drift + new selection → rapid speciation.</li>
  <li>Phylogenies show <strong>"island progression"</strong>: flies on the youngest island (Big Island) are nested within Maui's, which are nested within O'ahu's, etc.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Textbook peripatric speciation.</strong> Each colonization is a small founder event → strong drift → rapid divergence.</li>
  <li><strong>Phylogeny matches geology.</strong> Older islands carry older lineages; this is a falsifiable prediction (and it's confirmed).</li>
  <li><strong>Robbins will hit you on this:</strong> when the question is "rapid speciation on a young island chain," Hawaiian Drosophila is the classic example.</li>
</ol>
`
    },
    "Latitudinal diversity gradient": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Species richness peaks at the tropics and declines toward the poles — for nearly every taxonomic group.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Pattern holds for <strong>terrestrial AND marine, vertebrates AND insects, plants AND animals</strong>.</li>
  <li>Hypotheses: (1) <strong>energy/productivity</strong>, (2) <strong>time since glaciation</strong>, (3) <strong>climate stability</strong>, (4) <strong>area effects</strong>.</li>
  <li>"One of biology's oldest unsolved problems" — debated for &gt;150 years.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The pattern is universal, the cause is contested.</strong> Multiple hypotheses predict the same gradient; the data alone can't distinguish them.</li>
  <li><strong>Likely a combination</strong> of factors weighted differently across clades and ecosystems.</li>
  <li><strong>Conservation implication:</strong> tropical regions hold disproportionate biodiversity; protecting them protects more species per unit area.</li>
</ol>
`
    },
    "Continental drift — biogeographic evidence": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Species distributions match Pangaean breakup timing — biology helped confirm continental drift before plate tectonics was accepted.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Pangaea</strong> breakup began ~200 MYA; <strong>Gondwana</strong> (southern half) split ~150-50 MYA.</li>
  <li><strong>Glossopteris</strong> seed-fern fossils on every Gondwanan continent — seeds couldn't disperse across modern oceans, so the continents must have been connected (~280 MYA).</li>
  <li><strong>Lystrosaurus</strong> fossils (~250 MYA) on South America, Africa, India, Australia.</li>
  <li><strong>Marsupials</strong> in Australia + South America (split via Antarctica ~50 MYA).</li>
  <li><strong>Lungfish</strong> in S. America, Africa, Australia (Gondwanan).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Biology confirmed geology.</strong> Wegener's drift was rejected for decades — biogeographic distributions (especially Glossopteris) provided independent evidence that the continents were once connected.</li>
  <li><strong>Plant evidence is strongest.</strong> Glossopteris seeds couldn't raft across oceans; mammals could in principle.</li>
  <li><strong>Robbins will hit you on this:</strong> Gondwanan distribution = vicariance from continental drift. Atlantic-spanning sister taxa = ~120 MYA split timing.</li>
</ol>
`
    }
  });

  window.addCardPatches('L18', {
    "Selective harvest": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Hunting and fishing that targets specific phenotypes (large size, big horns) drives directional evolution — humans are a selective force.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Bighorn sheep on Ram Mountain, Alberta</strong>: ~25% decline in mean horn size over 30 years of trophy hunting (Coltman et al. 2003). Heritability of horn size ~0.7.</li>
  <li><strong>Atlantic cod</strong>: maturation age dropped from ~6 years to ~5 years over decades of size-selective fishing.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same mechanism as natural selection</strong> — humans just play the selecting role.</li>
  <li><strong>Often REVERSES natural selection.</strong> Natural selection favored large body in cod; fishing now selects for small. Populations evolve away from natural-equilibrium phenotypes.</li>
  <li><strong>Trophy hunting irony:</strong> hunters select for the very phenotype they value — and remove it from the gene pool over generations.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Selective harvest is contemporary evolution in real time — observable within decades, not millennia.</li>
</ul>
`
    },
    "Fisheries-induced evolution": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Size-selective fishing causes fish populations to evolve toward earlier maturation and smaller size — within decades.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Atlantic cod</strong>: mean maturation age dropped substantially in 30-40 years under intense size-selective fishing.</li>
  <li><strong>Mechanism</strong>: minimum-size limits ("keep only fish &gt;50 cm") REMOVE large/late-maturing individuals. Fish that mature small and reproduce BEFORE reaching legal size escape the net.</li>
  <li>Heritable shift detectable in ~10-20 generations.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Well-intentioned regulations cause evolution.</strong> Minimum-size limits seem protective but select on the wrong trait.</li>
  <li><strong>Better alternatives:</strong> total catch quotas, slot limits (protect both small AND large fish), marine protected areas.</li>
  <li><strong>Recovery is slow or impossible.</strong> Even when fishing pressure stops, evolved early-maturation traits persist.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Fisheries-induced evolution is the textbook example of HUMAN AS SELECTIVE FORCE producing rapid contemporary evolution.</li>
</ul>
`
    },
    "Inbreeding depression": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Mating between close relatives raises homozygosity and exposes deleterious recessives — fitness drops in small populations.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Florida panthers</strong> by 1990s: ~20-30 individuals, severe inbreeding → heart defects, kinked tails, undescended testicles, sperm abnormalities.</li>
  <li><strong>Cheetahs</strong>: ancient bottleneck, very low genetic diversity, high cub mortality.</li>
  <li>Mechanism: deleterious recessives normally hidden in heterozygotes become exposed when homozygous.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Small populations are doubly vulnerable</strong> — demographic stochasticity AND genetic problems compound.</li>
  <li><strong>Counterintuitive twist:</strong> sustained extreme inbreeding can PURGE deleterious recessives over generations (homozygous aa individuals die, removing a alleles). Self-fertilizing plants have done this.</li>
  <li><strong>Conservation:</strong> genetic rescue (introducing unrelated individuals) can reverse inbreeding depression.</li>
</ol>
`
    },
    "Genetic rescue": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Introducing individuals from another population restores variation and fitness in inbred populations — Florida panthers are the textbook success.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Florida panthers (1995)</strong>: ~20-30 individuals remained, severely inbred. <strong>8 Texas pumas</strong> were introduced.</li>
  <li>Within 2 generations: kitten survival rose, defects (heart, sperm) dropped, population grew to <strong>~200 by 2010s</strong>.</li>
  <li>Texas pumas were chosen because they were the historic gene-flow source before Florida was isolated.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Conservation success story.</strong> Demonstrated that genetic rescue can save a population on the brink.</li>
  <li><strong>Risk: outbreeding depression.</strong> If the introduced population is too distantly related, hybrid offspring may be maladapted to local conditions.</li>
  <li><strong>Risk: loss of genetic identity.</strong> Some argue that introducing a related subspecies dilutes the original population's distinctness.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Florida panther + 8 Texas pumas (1995) is THE textbook genetic rescue example. Memorize the numbers.</li>
</ul>
`
    },
    "Fragmentation": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Habitat subdivision into small patches reduces gene flow and population sizes — drift gets stronger, inbreeding more likely.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Smaller patches → smaller populations → stronger genetic drift.</li>
  <li>Fewer corridors → less gene flow between patches → local divergence.</li>
  <li>Edge effects (microclimate, predation, invasive species) further reduce effective habitat.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Combines demographic and genetic problems.</strong> Small isolated populations face both stochastic extinction and inbreeding depression.</li>
  <li><strong>Non-flying species are most vulnerable.</strong> Without dispersal across roads/clearings, populations become genetically isolated within decades.</li>
  <li><strong>Conservation response:</strong> wildlife corridors, stepping-stone reserves, connectivity-focused reserve design.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Fragmentation is one of the H's in <strong>HIPPO</strong> (Habitat destruction, Invasive species, Pollution, Population/human, Overharvest) — the classic threat acronym.</li>
</ul>
`
    },
    "Phenological shift": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Seasonal events (flowering, breeding, migration) are shifting earlier under warming climate — and creating mismatches between interacting species.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Tree leaf-out advanced ~3 days per decade since 1980 in Europe.</strong></li>
  <li><strong>Pied flycatchers</strong>: migrate from Africa on photoperiod cues (FIXED). Caterpillar prey peak weeks earlier each year. Result: chicks miss the food peak → fitness loss.</li>
  <li>Phenological mismatch is a major modern extinction-risk mechanism.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Evidence climate change is biological, not just physical.</strong> Phenological shifts are observable in datasets going back centuries (cherry blossom records in Japan, ice-out dates).</li>
  <li><strong>Mismatch breaks ecological networks.</strong> When pollinators emerge before flowers, or predators after prey, food webs unravel.</li>
  <li><strong>Photoperiod can't shift.</strong> Day length doesn't change with climate — species using photoperiod cues can't track warming temperatures.</li>
</ol>
`
    },
    "Range shift": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> As climate warms, species shift ranges poleward and upslope — but mountain-top species and slow dispersers run out of room.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Average rate: <strong>~17 km poleward and ~11 m upslope per decade</strong> across many taxa (Chen et al. 2011 meta-analysis).</li>
  <li>Mountain-top species face "<strong>nowhere to go</strong>" — no higher elevation available.</li>
  <li>Trees and other slow dispersers can't keep pace; long-lived plants with poor seed dispersal are most at risk.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Range shift is one of four climate responses</strong>: shift, evolve, plastic, or extinct. The mix depends on dispersal ability, generation time, and severity.</li>
  <li><strong>Mountain-top extinctions are happening</strong> — alpine plants and animals are losing habitat as climate zones shift upslope.</li>
  <li><strong>Conservation response:</strong> assisted migration is controversial but increasingly considered.</li>
</ol>
`
    },
    "Conservation biology": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Applying evolutionary, ecological, and population-genetic principles to preserving biodiversity — both populations AND the genes within them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Founded as a discipline in the <strong>1980s</strong> (Soulé, Wilson) in response to escalating biodiversity loss.</li>
  <li>Recognizes <strong>HIPPO</strong> threats: <strong>H</strong>abitat destruction, <strong>I</strong>nvasive species, <strong>P</strong>ollution, <strong>P</strong>opulation (human), <strong>O</strong>verharvest.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Conservation is fundamentally evolutionary.</strong> Preserving biodiversity = preserving the variation that future evolution can act on.</li>
  <li><strong>Manages BOTH demographic AND genetic decline.</strong> A demographically large population with no genetic diversity is still vulnerable.</li>
  <li><strong>Robbins will hit you on this:</strong> conservation must address inbreeding, drift, and fragmentation — not just headcount.</li>
</ol>
<h4>Mnemonic</h4>
<ul>
  <li><strong>HIPPO</strong>: Habitat · Invasive · Pollution · Population · Overharvest.</li>
</ul>
`
    },
    "Captive breeding": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Maintain populations in human care to prevent extinction and supply individuals for reintroduction — California condor is the textbook case.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>California condor (1987)</strong>: only 22 wild birds remained — ALL captured (controversial), joining ~5 already in captivity. Total breeding population: 27.</li>
  <li>Reintroduced from <strong>1992</strong>; <strong>~500 alive today, ~half wild</strong>.</li>
  <li>Other examples: <strong>Arabian oryx</strong> (extinct in wild 1972, reintroduced 1980s), <strong>black-footed ferret</strong>.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Last-resort tool</strong> when wild populations are too small for in-situ recovery.</li>
  <li><strong>Risks:</strong> (1) <strong>adaptation to captivity</strong> reduces wild fitness on release, (2) <strong>genetic bottleneck</strong> from few founders, (3) underlying threat (lead poisoning for condors) often unsolved.</li>
  <li><strong>Pedigree management</strong> (each bird's lineage tracked) minimizes inbreeding in captive breeding programs.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>California condor: <strong>22 wild + 5 captive = 27 founders in 1987</strong>; <strong>~500 today</strong>. Memorize this success-and-cautionary tale.</li>
</ul>
`
    },
    "Fisheries-induced evolution — size selection": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Minimum-size fishing rules drive size and maturation evolution — Atlantic cod shrunk and matured younger over 30-40 years.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Atlantic cod under intense size-selective fishing: <strong>maturation age dropped substantially in 30-40 years</strong>.</li>
  <li>Heritable size-at-maturity drops in <strong>~10-20 generations</strong> under strong size selection.</li>
  <li>Mechanism: a "keep only &gt;50 cm" rule REMOVES late-maturing fish before they reproduce. Fish that mature small and breed BEFORE reaching legal size escape entirely.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Counterintuitive consequence of "protective" rules.</strong> Minimum-size limits seem to protect young fish but actually select for early-maturing genotypes.</li>
  <li><strong>Better policies:</strong> total catch quotas, <strong>slot limits</strong> (protect both small AND large fish), marine reserves.</li>
  <li><strong>Recovery is slow.</strong> Even after fishing stops, evolved traits persist — the population doesn't "bounce back."</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Cod = textbook contemporary evolution under human selection. Connect fisheries-induced evolution to "humans as selective force" framing.</li>
</ul>
`
    },
    "Bighorn sheep trophy hunting → smaller horns": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Trophy hunting selects for the largest horns — and removes them from the gene pool. Mean horn size on Ram Mountain dropped ~25% in 30 years.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>Ram Mountain, Alberta</strong>: 30-year study (Coltman et al. 2003).</li>
  <li>Mean horn size declined <strong>~25%</strong>.</li>
  <li>Heritability of horn size: <strong>~0.7</strong> (very high).</li>
  <li>Body size and age at first reproduction also shifted as correlated traits.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Selection on a heritable trait causes rapid evolution.</strong> ~0.7 heritability + strong directional selection = visible change in 30 years.</li>
  <li><strong>The irony of trophy hunting:</strong> hunters value large horns, kill the large-horned rams, remove the genes for large horns. Compare to natural sexual selection where peacock tails GROW because females PREFER large.</li>
  <li><strong>Management implication:</strong> trophy hunting is a powerful evolutionary force, not just a conservation harvest.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Ram Mountain bighorn = textbook case of contemporary evolution from human selection. Memorize the 25% decline over 30 years.</li>
</ul>
`
    },
    "Florida panther genetic rescue": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> By 1990s, ~30 inbred Florida panthers remained. In 1995, 8 Texas pumas were introduced. Within 2 generations, fitness restored. Population grew to ~200.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>~20-30 individuals</strong> remained by 1990s; severe inbreeding caused heart defects, kinked tails, undescended testicles, sperm abnormalities.</li>
  <li><strong>1995: 8 Texas pumas introduced</strong> as genetic rescue.</li>
  <li><strong>Within 2 generations</strong>: defects dropped, kitten survival rose.</li>
  <li><strong>Population grew to ~200</strong> within ~15 years.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Conservation success.</strong> Demonstrated genetic rescue can reverse severe inbreeding depression.</li>
  <li><strong>Texas pumas were chosen carefully</strong> — they were the historic gene-flow source before Florida was isolated. Donor selection matters.</li>
  <li><strong>Risks:</strong> outbreeding depression (if donors are too distant) and loss of genetic identity (some argue subspecies distinctness was diluted).</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Memorize: <strong>Florida panther + 8 Texas pumas in 1995</strong>. This is THE textbook genetic rescue example.</li>
</ul>
`
    },
    "Inbreeding depression mechanism": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Close-relative mating raises homozygosity → recessive deleterious alleles get exposed → fitness drops.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mechanism: heterozygotes mask recessive deleterious alleles. Inbreeding produces aa homozygotes that express the deleterious phenotype.</li>
  <li>Severity depends on <strong>genetic load</strong> (mutation accumulation) and how many recessive deleteriouss the population carries.</li>
  <li>Florida panthers, cheetahs, Mauritius kestrels — all classic inbreeding-depressed populations.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Small populations are doubly vulnerable.</strong> Less standing variation, more close-relative mating, more homozygous deleterious expression.</li>
  <li><strong>Counterintuitive twist: PURGING.</strong> Sustained extreme inbreeding can REMOVE deleterious recessives over generations (every aa homozygote that dies removes 2 a alleles). Self-fertilizing plants and eusocial Hymenoptera have purged.</li>
  <li><strong>Genetic rescue reverses it.</strong> Outcrossing restores heterozygosity and masks deleterious recessives.</li>
</ol>
`
    },
    "Climate change → range shifts and phenological mismatch": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> Species track climate by shifting ranges or timing — but interacting species track at different rates, breaking ecological networks.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Average shift: <strong>~17 km poleward and ~11 m upslope per decade</strong> (Chen et al. 2011 meta-analysis across taxa).</li>
  <li><strong>Pied flycatchers</strong>: migrate from Africa on FIXED photoperiod cues. Caterpillar prey peak weeks earlier each year → chicks miss the food peak → fitness loss.</li>
  <li>Tree leaf-out advanced <strong>~3 days per decade</strong> in Europe since 1980.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Four possible responses:</strong> shift range, evolve in place, plastic response, or extinct. Mix depends on dispersal ability, generation time, severity.</li>
  <li><strong>Photoperiod can't shift.</strong> Day length doesn't change with climate — species using photoperiod cues fall behind temperature shifts.</li>
  <li><strong>Mountain-top species face "nowhere to go."</strong> Already at max elevation when climate warms further.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Phenological mismatch = MAJOR modern extinction risk. Connect to "contemporary evolution" framing.</li>
</ul>
`
    },
    "Captive breeding + reintroduction (California condor)": {
      importance: `
<p class="big-deal"><strong>The big deal in one line:</strong> 1987: only 22 wild condors left — ALL captured. Today ~500 alive, ~half wild. Success — but lead poisoning still kills them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li><strong>April 1987</strong>: 22 wild California condors captured (controversial), joined ~5 already captive → 27 total breeding birds.</li>
  <li><strong>1992</strong>: reintroductions begin.</li>
  <li><strong>Today: ~500 alive, ~half wild</strong> — ~25-fold increase from 1987.</li>
  <li>Pedigree management tracked each bird's lineage to minimize inbreeding.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Success: extinction averted.</strong> ~25-fold population increase; reintroduction works.</li>
  <li><strong>Cautionary tale:</strong> the original threat (LEAD POISONING from bullet-shot carcasses) wasn't fully solved. Reintroduced condors still die from lead and trash. Without removing the underlying anthropogenic cause, reintroduction is just expensive maintenance.</li>
  <li><strong>Genetic bottleneck:</strong> 27 founders → reduced variation → future inbreeding risk.</li>
</ol>
<h4>Robbins will hit you on this</h4>
<ul>
  <li>Memorize: <strong>22 wild + 5 captive = 27 founders in 1987</strong>; <strong>~500 today</strong>. Both success and cautionary tale.</li>
</ul>
`
    }
  });
})();
