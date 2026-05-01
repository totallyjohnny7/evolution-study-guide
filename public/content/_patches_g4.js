/* Patches group 4: L13, L14, L15 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L13: {
      "Group selection": {
        exAnswer: "The naive 'good of the species' story breaks under within-group cheater dynamics. Inside any group, an individual that withholds the costly altruistic act (e.g., does NOT call out an alarm) keeps fitness C while still receiving the benefit B from groupmates' calls — selfish individuals out-reproduce altruists every generation, so altruism is invaded and lost long before slower among-group selection (groups with more altruists outproducing groups with fewer) can act. Modern evolutionary biology accepts group/multilevel selection only under strict conditions (small groups, frequent extinction, low gene flow) and prefers kin selection or reciprocity to explain most apparent 'good of the species' traits.",
        mnem: "Cheaters win the WITHIN race before altruistic GROUPS win the among-group race."
      },
      "Selfish gene perspective": {
        exAnswer: "From the gene's-eye view, the worker ant's 'self-sacrifice' isn't sacrifice at all — the genes she carries are propagating efficiently through the queen's offspring, who share her alleles at relatedness r. In Hymenoptera, sisters share r=0.75 (haplodiploidy), so helping the queen produce more sisters spreads worker alleles FASTER than producing daughters herself (r=0.5). The 'individual' lost reproduction; the 'gene' won. Dawkins's reframing: ask which alleles increase, not which bodies reproduce.",
        mnem: "Bodies are vehicles; genes are the passengers calling the shots."
      },
      "Hamilton's rule": {
        exAnswer: "Apply rB > C: r=0.75, B=5, C=1, so rB = 0.75 × 5 = 3.75. Since 3.75 > 1, Hamilton's rule is satisfied and the helping behavior is favored by kin selection. The worker loses 1 unit of direct fitness but gains 3.75 units of indirect fitness through the extra sisters — net inclusive-fitness gain of +2.75. This is the canonical haplodiploidy explanation for hymenopteran eusociality: high r makes even modest B easily clear the cost C.",
        mnem: "rB > C: 'related-times-benefit beats cost.'"
      },
      "Coefficient of relatedness (r)": {
        exAnswer: "(a) Full sibs r=0.5 (share both parents, ½ chance any allele copies). (b) Half-sibs r=0.25 (share one parent). (c) First cousins r=0.125 (one shared grandparent, halve twice). (d) Parent-offspring r=0.5. r is the relevant quantity because Hamilton's rule asks: what is the probability the SPECIFIC allele driving the altruistic behavior is also in the recipient by RECENT common descent? Two unrelated humans share ~99.9% of their genome by overall sequence similarity, but their r is ~0 — that ancient shared sequence cannot be selected on by present-day kin-directed altruism.",
        mnem: "Halve r at every meiosis between you and them."
      },
      "Inclusive fitness": {
        exAnswer: "Inclusive fitness counts: (1) direct fitness — own offspring she produces — and (2) indirect fitness — the EXTRA offspring her relatives produce because of her help, weighted by r. Workers have direct fitness = 0 (sterile) but enormous indirect fitness through the queen's offspring (sisters, r=0.75 in Hymenoptera). From the workers' allelic perspective, evolution doesn't care which body reproduces — it cares whether the worker's alleles increase in the next generation, and they do, faster than if she'd bred herself.",
        mnem: "Inclusive = own kids + relatives' EXTRA kids × r."
      },
      "Eusociality": {
        exAnswer: "Naked mole-rats are the textbook 'most extreme' kin-selection case because (1) workers are STERILE — zero direct fitness, all reproductive output is indirect — and (2) colony members are extraordinarily inbred (effective r ≈ 0.8 between colony-mates), so helping the queen is helping near-clones. With C=lifetime reproduction lost but B=many siblings raised at r near 1, Hamilton's rule rB>C is satisfied with massive margin. Eusociality is the predicted endpoint when relatedness is maximal AND breeding opportunities for non-queens are minimal.",
        mnem: "Eu-social = TRUE social: sterile workers + queen + overlapping generations."
      },
      "Evolutionarily Stable Strategy (ESS)": {
        exAnswer: "Pure-Hawk is unstable because Hawks injure each other (½(V−C) < 0 when C>V), so a rare Dove invader avoids costly fights and out-reproduces resident Hawks. Pure-Dove is unstable because a rare Hawk faces only Doves and takes V every time. The stable equilibrium is a MIXED ESS at frequency p* = V/C of Hawks (or equivalently a polymorphic population, or every individual playing Hawk with probability p*). It is stable because at p*, expected payoff to Hawk = expected payoff to Dove, so neither rare alternative can invade — the defining ESS condition."
        // mnem provided in extras card
      },
      "Frequency-dependent selection": {
        exAnswer: "This is NEGATIVE frequency-dependent selection: each morph's fitness is HIGH when rare and LOW when common. Because no morph is unconditionally best, none can fix — the system instead produces stable cyclical dynamics (rock-paper-scissors), with morph frequencies oscillating on a ~5–6 year cycle in side-blotched lizards. The result is maintained polymorphism rather than equilibrium, contrasting with positive frequency-dependent selection (e.g., warning coloration), which drives one morph to fixation.",
        mnem: "Rare-is-fit = NEGATIVE freq-dep = polymorphism."
      },
      "Hawk-Dove game": {
        exAnswer: "Pure-Hawk fails because two Hawks meeting pay ½(V−C) each — when injury cost C > resource value V, this is negative, so Hawks lose fitness fighting each other. Once Hawks are common, a rare Dove invader avoids fights, scores 0 against Hawks (better than negative payoff), and earns V/2 against the few other Doves — Doves out-reproduce Hawks. The system settles at the mixed ESS where p_Hawk = V/C, the only frequency at which Hawk and Dove have equal expected payoffs and neither can invade.",
        mnem: "Hawk fights, Dove flees: mixed ESS at p* = V/C when V<C."
      },
      "Side-blotched lizard (Uta stansburiana)": {
        exAnswer: "All three persist because of NEGATIVE frequency-dependent selection in a rock-paper-scissors structure. When ORANGE (aggressive territory holders) is common, YELLOW sneakers (mimic females, slip past oranges) gain. When YELLOW rises, BLUE (mate-guarders) detect sneakers and spread. When BLUE is common, ORANGE overpowers them. No morph is best at all frequencies, so none fixes; instead, frequencies cycle on a ~5–6 year period. This was Sinervo & Lively's classic field demonstration that ESS theory can yield stable cycles, not just equilibria.",
        mnem: "Orange beats Blue beats Yellow beats Orange — like the game."
      },
      "Direct reciprocity": {
        exAnswer: "It's called 'tit-for-tat' because the simple rule — cooperate first, then copy what your partner did last round — wins repeated Prisoner's Dilemma tournaments (Axelrod). Conditions for evolution: (1) repeated encounters with the SAME individual (low partner turnover), (2) recognition/memory of past behavior, and (3) sufficient probability of future interaction (the 'shadow of the future' must be long enough that w > C/B, where w = continuation probability). Vampire bats meet all three: stable roost membership, individual recognition, nightly survival risk that makes future help valuable.",
        mnem: "Tit-for-tat: be nice first, copy opponent thereafter."
      },
      "Indirect reciprocity": {
        exAnswer: "Conditions: (1) BEHAVIOR IS OBSERVED by third parties (transparency, gossip, public scoring), (2) reputations are tracked accurately and shared across the group, and (3) potential helpers DISCRIMINATE — they preferentially aid those with good reputations and refuse defectors. Unlike direct reciprocity, the donor and the eventual repayer need NEVER meet; the social information network does the bookkeeping. Language and norms massively amplify indirect reciprocity, which is why it scales to large human groups where direct tit-for-tat would fail.",
        mnem: "Help to be SEEN helping; reputation pays you back later."
      }
    },
    L14: {
      "Radiometric dating": {
        exAnswer: "The ash bed must be EXACTLY 65.0 ± 0.2 Mya old (volcanic ash is dated directly because it crystallizes minerals like zircon at eruption, locking in the parent/daughter ratio). Fossils ABOVE the ash are younger than 65.0 Mya; fossils BELOW are older. This is the 'bracketing' logic of geology: most fossils can't be dated directly (sedimentary rock isn't datable), so we date interbedded volcanic layers and constrain fossils to lie between two known dates. The U-Pb system in zircons is the gold standard for this timescale.",
        mnem: "Date the ash, bracket the fossil."
      },
      "Half-life": {
        exAnswer: "28,650 / 5,730 = 5 half-lives. Fraction remaining = (½)^5 = 1/32 ≈ 3.1%. ¹⁴C dating is useless for dinosaurs (extinct ~66 Mya) because that's >11,500 half-lives — the parent isotope is far below detection limits (~50,000 yr practical maximum). Dating dinosaurs requires longer-half-life systems like K-Ar (1.25 Gyr) or U-Pb in zircons (4.5 Gyr) applied to interbedded volcanic ashes.",
        mnem: "Each half-life: halve what's left. After n half-lives: (½)^n remains."
      },
      "Biomarker": {
        exAnswer: "Steranes are stable lipid molecules derived ONLY from sterols, which require eukaryotic membrane biochemistry (sterol synthesis needs O₂ and a complex enzymatic pathway absent in most prokaryotes). Finding steranes in 1.6-Gyr-old rocks is strong CHEMICAL evidence for eukaryotes, weaker than actual fossils (which show cells and morphology) but valuable when fossils are absent or ambiguous. Caveat: contamination by younger biological material is a perennial concern, so biomarker dates are sometimes revised downward upon re-analysis.",
        mnem: "Biomarker = chemical fingerprint of a vanished organism."
      },
      "Great Oxidation Event": {
        exAnswer: "It was a 'mass extinction' for OBLIGATE ANAEROBES because O₂ is corrosive to their reduced-iron-and-sulfur biochemistry — they survived only by retreating to anoxic refugia (deep sediment, gut, hydrothermal vents), where they remain today. Evolutionary opportunities created: (1) AEROBIC RESPIRATION yields ~18× more ATP per glucose than fermentation, fueling larger cells and active lifestyles; (2) the OZONE LAYER formed from O₂, shielding land surfaces from UV; (3) eukaryogenesis via mitochondrial endosymbiosis (~2 Gya) and eventual multicellularity required oxygen for sterol synthesis and energetic budgets.",
        mnem: "GOE ~2.4 Gya: oxygen poisons anaerobes, powers aerobes."
      },
      "Cambrian explosion": {
        exAnswer: "It's called an 'explosion' because most modern animal phyla appear in the fossil record over ~20 Myr, geologically rapid. But in evolutionary terms, 20 Myr is plenty — molecular clocks place most phylum-splits at 700+ Mya, suggesting soft-bodied ancestors had been diversifying through the Cryogenian/Ediacaran for 100s of Myr. The 'explosion' is partly a fossilization artifact: hard parts (shells, exoskeletons) evolved during this window and PRESERVE, while soft-bodied predecessors largely don't. Drivers proposed: rising O₂ crossing a metabolic threshold, Hox/Pax regulatory toolkits enabling body-plan experimentation, and ecological arms races (predators select for armor, vision, burrowing).",
        mnem: "Cambrian 'explosion' = sudden FOSSILS, not sudden lineages."
      },
      "Devonian": {
        exAnswer: "The Devonian (~419–359 Mya) is the 'Age of Fishes' — jawed vertebrates (placoderms, sharks, bony fish) radiate dramatically and dominate marine ecosystems. The most consequential innovation: the TETRAPOD TRANSITION — sarcopterygian (lobe-finned) fish like Tiktaalik (~375 Mya) acquire weight-bearing limbs, mobile necks, and air-breathing lungs, giving rise to the first land vertebrates by the late Devonian. Forests of early vascular plants and seed plants also emerge, transforming continental ecosystems. The period ends with the Late Devonian mass extinction (one of the Big Five).",
        mnem: "Devonian = fish out of water (tetrapod origins)."
      },
      "Permian": {
        exAnswer: "The end-Permian (~252 Mya) lost ~95% of marine species and ~70% of terrestrial vertebrate species — the LARGEST mass extinction in Earth history, often called 'the Great Dying.' Implicated causes: massive Siberian Traps flood-basalt volcanism releasing CO₂ and SO₂ → rapid warming, ocean acidification, anoxia, and possibly clathrate destabilization; together these collapse marine and terrestrial food webs over <100 Kyr. The event reset evolutionary trajectories: surviving therapsids and archosaurs gave rise to the Mesozoic dinosaur-and-mammal world.",
        mnem: "Permian = 'Great Dying' — 95% marine extinct ~252 Mya."
      },
      "Mass extinction": {
        exAnswer: "End-PERMIAN was most severe (~95% marine species lost, ~252 Mya — Siberian Traps + acidification). End-CRETACEOUS (K-Pg, ~66 Mya, asteroid) most shaped vertebrate evolution because it ended the dinosaur reign and emptied terrestrial niches that mammals — previously small and nocturnal for ~150 Myr — radiated into within ~10 Myr (large body sizes, arboreal/aquatic forms, eventual primates). Mass extinctions don't just kill — they CREATE adaptive opportunity by clearing competitive landscapes non-randomly.",
        mnem: "Big Five: Ord-Dev-Perm-Tri-Cret. Permian biggest, K-Pg most famous."
      },
      "K-T (K-Pg) boundary": {
        exAnswer: "The iridium-rich clay layer dated to ~66 Mya is the global geochemical signature of the CHICXULUB ASTEROID IMPACT off the Yucatán Peninsula. Iridium is rare in Earth's crust but abundant in chondritic asteroids/comets, so a worldwide spike points to extraterrestrial deposition (Alvarez et al. 1980). It marks the END-CRETACEOUS / K-Pg MASS EXTINCTION, which ended the non-avian dinosaurs (and ammonites, mosasaurs, plesiosaurs) and triggered the Cenozoic mammalian radiation. Confirmed by impact-shocked quartz and the buried Chicxulub crater.",
        mnem: "K-Pg = K (Cretaceous) ends, Pg (Paleogene) begins, dinos out, mammals in."
      },
      "Iridium layer": {
        exAnswer: "It's the 'smoking gun' because (1) iridium is depleted in Earth's crust (sank into the core during planetary differentiation) but enriched in undifferentiated extraterrestrial material; (2) the spike is GLOBAL — found at K-Pg-age sediments on every continent and ocean floor — ruling out a localized terrestrial source; (3) it co-occurs with shocked-quartz grains and microspherules diagnostic of hypervelocity impact; (4) it's consistent with the size and composition of the buried Chicxulub crater. No volcanic mechanism produces this combination of signatures globally and instantaneously.",
        mnem: "Iridium = asteroid fingerprint sprinkled worldwide at 66 Mya."
      }
    },
    L15: {
      "Tip / Terminal taxon": {
        exAnswer: "Humans are at a TIP — terminal taxa are the labeled organisms (extant or extinct) at the END of branches, representing what's being classified. Internal points are NODES (common ancestors), and the lines connecting them are BRANCHES (lineages through time). Every extant species in a tree is necessarily a tip; reading a tree backwards from a tip toward the root traces that lineage's evolutionary history.",
        mnem: "Tips = the leaves of the tree (the species labels)."
      },
      "Node": {
        exAnswer: "The node represents the MOST RECENT COMMON ANCESTOR (MRCA) of all descendant lineages — a single ancestral species/population that lived ~5 Mya and from which both of these species descend. Nodes do NOT represent 'speciation events' as instantaneous moments — they mark the population from which two daughter lineages later diverged. The node's date is estimated by molecular clocks or fossil calibration, not directly observed.",
        mnem: "Node = the ancestor at the fork."
      },
      "Branch": {
        exAnswer: "It matters because the BIOLOGICAL CLAIM differs by length convention: (a) time-scaled trees (chronograms) — branch length = millions of years, so vertical position = age; (b) change-scaled trees (phylograms) — branch length = number of substitutions or character changes; (c) cladograms — branches are uninformative, only TOPOLOGY (who is sister to whom) matters. Mistaking a cladogram for a chronogram leads readers to infer speed of evolution where the diagram makes no such claim. Always check the scale bar.",
        mnem: "Same topology, different branch lengths = different stories."
      },
      "Sister groups": {
        exAnswer: "Sister groups are two clades that share their MRCA at a SINGLE NODE — i.e., each is the closest relative of the other, with no other lineage branching between them. Chimps and humans share an MRCA ~6–7 Mya that has no other living descendants in between. Gorillas branched off EARLIER (~8–9 Mya), so the gorilla lineage is sister to the chimp+human clade as a whole, not to chimps or humans individually. Sister-group relationships are reciprocal: A is sister to B iff B is sister to A.",
        mnem: "Sisters = closest cousins at one shared fork."
      },
      "Synapomorphy": {
        exAnswer: "AT THE LEVEL OF MAMMALIA, lactation/mammary glands are SYNAPOMORPHIES — they are derived novelties that appeared in the mammalian ancestor and are uniquely shared by all descendants. AT THE LEVEL OF, say, PRIMATES (a sub-clade within Mammalia), the same trait is a SYMPLESIOMORPHY — it's ancestral to primates (inherited, not novel) and shared with all other mammals, so it can't be used to define the primate clade. The same character can be 'derived' or 'ancestral' depending on which node you're trying to diagnose.",
        mnem: "Syn-APO = APart-from-the-rest = derived. Defines a clade."
      },
      "Symplesiomorphy": {
        exAnswer: "The vertebral column is a SYNAPOMORPHY OF VERTEBRATES (it arose in the vertebrate ancestor, defines the clade), but a SYMPLESIOMORPHY OF MAMMALS (mammals inherited it; it's shared with fish, reptiles, etc., so it doesn't tell us mammals are mammals). The difference matters for cladistics: only synapomorphies at a given level are EVIDENCE that a group is a clade. Using symplesiomorphies to group taxa creates paraphyletic 'wastebasket' categories (the classic mistake: grouping fish + amphibians + reptiles as 'lower vertebrates' based on shared ancestral traits).",
        mnem: "Sym-PLESIO = Plenty-old = ancestral. Useless for grouping."
      },
      "Homoplasy": {
        exAnswer: "Bat wings and bird wings are HOMOPLASIES (analogous, convergent) — they evolved independently from non-winged ancestors and the WING is not present in their MRCA. Distinguishing evidence: (1) underlying anatomy differs — bat wings stretch skin between elongated FINGERS, bird wings are FEATHERED forelimbs without independent fingers; (2) developmental origins differ — different genetic and embryonic programs; (3) the phylogenetic placement of non-winged outgroups (most mammals, most reptiles) tells us the wing-less state is ancestral. Homologous structures (true synapomorphies) share deep developmental and structural identity even when superficially modified.",
        mnem: "Homoplasy = looks alike, evolved alike INDEPENDENTLY."
      },
      "Clade / Monophyletic group": {
        exAnswer: "Mammals are MONOPHYLETIC because the group includes the mammalian MRCA AND every descendant species (mice, whales, humans, platypuses — all living and extinct mammals). It would FAIL to be monophyletic if we excluded any descendants — for example, removing whales from 'mammals' would make it paraphyletic, because whales are deeply nested within mammals (descended from artiodactyl-like ancestors). A clade is the only group that corresponds to a real evolutionary unit; all valid taxa in modern systematics must be monophyletic.",
        mnem: "Clade = ancestor + EVERY descendant. No exceptions."
      },
      "Paraphyletic group": {
        exAnswer: "'Reptiles' (traditional) is paraphyletic because birds are descended from theropod dinosaurs — i.e., birds are nested INSIDE the reptile clade — yet the traditional grouping excludes them. The group thus contains a common ancestor + SOME but not ALL of its descendants (the bird descendants are missing). Modern systematists fix it by either (a) expanding to SAUROPSIDA / REPTILIA-INCLUDING-BIRDS (a clade), or (b) abandoning 'reptile' as a taxon and using only the natural sub-clades (Lepidosauria, Testudines, Archosauria-with-birds-and-crocs). The principle: every taxon must be a clade.",
        mnem: "Para = ancestor + Part of descendants (some left out)."
      },
      "Polyphyletic group": {
        exAnswer: "'Warm-blooded animals' is polyphyletic because endothermy evolved INDEPENDENTLY in mammals (one origin, in synapsids) and in birds (separate origin, in theropod dinosaurs) — there is no exclusive common ancestor that was warm-blooded and is shared only by these two groups. The grouping was defined on a HOMOPLASY (convergent trait) rather than a synapomorphy. This is problematic because polyphyletic groups don't reflect shared ancestry — they hide the fact that the trait evolved twice and obscure the actual evolutionary structure. Modern systematics rejects polyphyletic taxa entirely.",
        mnem: "Poly = Pick-and-mix from multiple ancestors (no shared origin)."
      },
      "Biological Species Concept (BSC)": {
        exAnswer: "Under the strict BSC, horses and donkeys ARE 'good' species — they meet successfully and mate, but their offspring (mules) are STERILE, which constitutes POSTZYGOTIC reproductive isolation. The BSC's threshold is reproductive isolation, not zero mating: occasional hybridization that fails to produce reproducing offspring (sterile or inviable) preserves the species as separate gene pools. Mules cannot pass alleles between the parental species, so horse and donkey gene pools remain distinct over evolutionary time — exactly what the BSC requires.",
        mnem: "BSC = can-they-make-FERTILE-babies? Mules don't count."
      },
      "Morphological species concept": {
        exAnswer: "The MORPHOLOGICAL species concept FAILS on cryptic species because it relies on visible/diagnosable physical differences — and cryptic species look nearly identical despite being reproductively isolated lineages. The BIOLOGICAL or PHYLOGENETIC species concepts work better: BSC catches the reproductive barrier (mating tests, hybrid sterility), and PSC catches the genetic distinctness (DNA barcoding reveals deep splits in mitochondrial or nuclear loci). Cryptic skipper butterflies were resolved into multiple species via DNA barcoding when morphology had failed to distinguish them for centuries.",
        mnem: "Morph concept = if it LOOKS different. Fails on cryptics and ring species."
      },
      "Phylogenetic species concept": {
        exAnswer: "The PSC handles asexual / horizontally-transferring bacteria because it doesn't require interbreeding — it defines a species as the SMALLEST monophyletic cluster diagnosable by shared derived characters (typically genetic markers like 16S rRNA or core-genome SNPs). Bacterial 'species' under the PSC are tight monophyletic clades within rRNA trees, even though gene flow within them is asexual and occasional HGT crosses species boundaries. The BSC is inapplicable (no interbreeding to test); the PSC sidesteps the issue by anchoring species in shared evolutionary history rather than reproductive compatibility.",
        mnem: "PSC = smallest CLADE you can diagnose by shared derived traits."
      }
    }
  });
})();
