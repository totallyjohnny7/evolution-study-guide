/* Final gap-fill patch — exAnswer + mnem completion. Loaded last in the patch chain. */
(function () {
  if (!window.addCardPatches) return;

  // ===== L04 =====
  window.addCardPatches('L04', {
    "Wahlund effect": {
      exAnswer: "Wahlund effect: pooling subpopulations with different allele frequencies LOOKS like a deficit of heterozygotes (excess homozygotes) under HWE — even when each subpopulation is itself in HWE. Two ponds at q=0.2 and q=0.8 each show 2pq=0.32, but pooled (q=0.5) you'd EXPECT 2pq=0.5, while observed average is 0.32 — apparent inbreeding from population structure alone.",
      mnem: "Wahlund = Wrong assumption (one population) → looks inbred."
    }
  });

  // ===== L05 =====
  window.addCardPatches('L05', {
    "Reaction norm": {
      exAnswer: "A reaction norm plots one GENOTYPE's phenotype across an environmental gradient. FLAT line = canalized (insensitive to environment). SLOPED line = plastic (responds to environment). CROSSING lines for different genotypes = G×E interaction (rank order of genotypes flips between environments). Reaction norms are the diagnostic tool for separating genetic effects from plasticity from G×E.",
      mnem: "Reaction norm = phenotype's response curve to environment. Slope = plasticity, crossing = G×E."
    },
    "V_P = V_A + V_D + V_I + V_E": {
      exAnswer: "Total phenotypic variance partitions into FOUR sources: V_A (additive genetic — selection's grip), V_D (dominance interactions at one locus), V_I (epistatic interactions across loci), V_E (environment + measurement). Only V_A predictably transmits via gametes — V_D and V_I get scrambled by recombination each generation, V_E isn't inherited at all. h² = V_A/V_P; H² = (V_A+V_D+V_I)/V_P.",
      mnem: "VP = VA + VD + VI + VE — only VA gets shipped."
    },
    "Selection-type discrimination cheat": {
      exAnswer: "Three selection types differ by which part of the distribution shifts: DIRECTIONAL — mean shifts (most common: drug resistance, beak depth in drought). STABILIZING — variance shrinks, mean unchanged (human birth weight ~7 lbs survives best). DISRUPTIVE — variance grows bimodally, mean unchanged (Cameroon seedcrackers, large + small bills survive, intermediates lose).",
      mnem: "Directional = mean moves; Stabilizing = squeeze middle; Disruptive = split peaks."
    },
    "Breeder's equation R = h²·S": {
      exAnswer: "R = h²·S. Apply: S = (selected mean) − (population mean) = 30 − 25 = 5. R = 0.5 × 5 = 2.5 g. Next-generation predicted weight = 25 + 2.5 = 27.5 g. Half the selection differential is recovered because half the phenotypic variance is non-additive/environmental. If h²=1, full S converts; if h²=0, no response at all.",
      mnem: "R = h²·S — only the heritable share moves the next generation."
    },
    "Narrow vs broad heritability": {
      mnem: "Narrow (h²) = additive only, predicts selection response. Broad (H²) = all genetic, doesn't."
    },
    "Parent-offspring regression estimates h²": {
      mnem: "Slope = h². Steep parent-kid line → trait is heritable; flat → mostly environment."
    }
  });

  // ===== L07 =====
  window.addCardPatches('L07', {
    "Three requirements for measurable evolution in nature": {
      mnem: "VHS: Variation (heritable) + Heritability + Selection differential — all three required."
    },
    "Grants' Galápagos finches — predicted vs observed R": {
      mnem: "1977 drought: S=0.53mm, h²=0.78, predicted R=0.41mm — close to observed."
    },
    "Peppered moth industrial melanism — what was actually selected?": {
      mnem: "Cortex gene transposon insertion (Hof 2016) — the genetic basis was a single jumping-DNA event."
    },
    "Antibiotic resistance — speed and predictability": {
      mnem: "Antibiotic resistance = evolution in fast-forward — days, not millennia."
    },
    "Domestication = artificial selection (greyhound case)": {
      mnem: "Belyaev silver fox: tame in ~10 generations — human-driven directional selection on tameness."
    },
    "Why field selection studies need longitudinal data": {
      mnem: "One year ≠ evolution. Need multiple generations to confirm allele-frequency change."
    },
    "Influenza antigenic drift vs antigenic shift": {
      mnem: "Drift = small mutations (yearly flu). Shift = reassortment between strains (pandemic flu)."
    },
    "When does R = h²·S fail to predict the next generation?": {
      mnem: "R = h²·S fails when h² is overestimated, environment changes, or selection is non-linear."
    }
  });

  // ===== L08 =====
  window.addCardPatches('L08', {
    "Neofunctionalization vs subfunctionalization": {
      exAnswer: "After gene duplication, the redundant copy can take three fates. NEOFUNCTIONALIZATION: one copy acquires a NEW function not present in the ancestor (e.g., antifreeze glycoprotein in Antarctic notothenioid fish, evolved from a digestive trypsinogen). SUBFUNCTIONALIZATION: the ancestor's combined functions split between the two copies, each retaining a SUBSET (e.g., zebrafish eng1 gene partitioned into eng1a and eng1b expression domains). The third (commonest) fate is pseudogenization — silenced copy becomes a pseudogene.",
      mnem: "Neo = new function; Sub = split functions; Pseudo = silenced (most common fate)."
    },
    "Cis-regulatory mutations vs structural": {
      mnem: "Cis-regulatory = where/when gene runs (less pleiotropic). Structural = what protein is."
    },
    "Adaptation — noun vs verb (trait vs process)": {
      mnem: "Adaptation = the trait (noun) AND the selection process that built it (verb). Same word."
    },
    "Protein promiscuity → cooption": {
      mnem: "Cooption = old protein, new job. Crystallin = stress enzyme repurposed for lens."
    }
  });

  // ===== L09 =====
  window.addCardPatches('L09', {
    "Coevolution vs coexistence": {
      mnem: "Coexistence = sharing space; Coevolution = reciprocal selection. Different things."
    },
    "Newt-snake arms race (TTX example)": {
      mnem: "Newt TTX ↑ ↔ Snake Na-channel resistance ↑ — escalation locked in by reciprocal selection."
    },
    "Geographic Mosaic Theory of Coevolution (Thompson)": {
      mnem: "Coevolution varies by zip code: hotspots match, coldspots don't."
    },
    "Pollinator-flower mutualism (Darwin's orchid prediction)": {
      mnem: "Darwin predicted Xanthopan moth from Angraecum's 30cm spur — found 1903, 41 years later."
    },
    "Endosymbiosis: two distinct organelle origins": {
      mnem: "Mito = alphaproteobacterium ~2 Gya. Plastid = cyanobacterium ~1.5 Gya. Two events, both real."
    }
  });

  // ===== L11 =====
  window.addCardPatches('L11', {
    "Anisogamy = the basis of male/female": {
      mnem: "Anisogamy = unequal gametes. Big costly few = female; small cheap many = male."
    },
    "Fisher's runaway": {
      mnem: "Runaway = preference + trait genetically correlated → both escalate exponentially."
    },
    "Sexual conflict — when do interests diverge?": {
      mnem: "Sexual conflict: what's good for male fitness ≠ good for female fitness. Arms race within species."
    },
    "Sperm competition — male anatomical responses": {
      mnem: "Polyandry → bigger testes (chimps > gorillas). Sperm compete; biggest reservoir wins."
    },
    "Cryptic female choice — why it matters": {
      mnem: "Female chooses INSIDE her body — sperm storage, fertilization timing, ejaculate dumping."
    }
  });

  // ===== L12 =====
  window.addCardPatches('L12', {
    "Extrinsic mortality → life history": {
      mnem: "High extrinsic mortality → live fast, breed early, die young. Low → slow life, late breeding."
    },
    "Life-history trade-offs — what's the currency?": {
      mnem: "Energy + time = limited. Reproduce now ↔ survive to reproduce later. No free lunch."
    },
    "Offspring number vs size (bet-hedging vs provisioning)": {
      mnem: "Many small (r-strategists, dandelion) vs few large (K-strategists, oak). Trade-off."
    },
    "Seychelles warblers — why help, not disperse?": {
      mnem: "Seychelles warblers help when no territory open — kin-selected delayed dispersal."
    }
  });

  // ===== L13 =====
  window.addCardPatches('L13', {
    "Hamilton's rule: rB > C": {
      exAnswer: "rB > C: Apply r=0.75 (sister), B=5 (extra sisters helped), C=1 (own offspring lost). rB = 0.75 × 5 = 3.75 > 1 = C → kin selection FAVORS the helping. Worker loses 1 unit direct fitness, gains 3.75 indirect — net +2.75 inclusive fitness. This is the canonical haplodiploidy explanation for hymenopteran eusociality.",
      mnem: "rB > C — related-times-benefit beats cost. Hamilton's threshold."
    },
    "Coefficient of relatedness — common values": {
      exAnswer: "Common r values: PARENT-OFFSPRING = 0.5 (direct genetic transmission). FULL SIB = 0.5 (50% chance any allele copy is shared). HALF SIB = 0.25 (one shared parent). FIRST COUSIN = 0.125 (one shared grandparent, halved twice). HYMENOPTERAN SISTER = 0.75 (haplodiploidy: father's haploid sperm makes sisters share ALL his alleles plus 50% of mother's). NIECE/UNCLE = 0.25.",
      mnem: "Halve r at every meiosis between you and them. Hymenoptera sisters = 0.75 anomaly."
    },
    "Hawk-Dove game payoffs": {
      exAnswer: "Payoff matrix entries: HAWK vs HAWK = ½(V−C) (each wins half the time, loses half the time, paying injury cost C; if C>V, this is negative). HAWK vs DOVE = V (Hawk wins, no injury). DOVE vs HAWK = 0 (Dove flees, gets nothing). DOVE vs DOVE = V/2 (share). When C>V, mixed ESS at p_Hawk = V/C; pure-Hawk and pure-Dove are both invadable.",
      mnem: "HH=½(V-C), HD=V, DH=0, DD=V/2. Mixed ESS at p_Hawk = V/C when C>V."
    },
    "Direct vs indirect reciprocity": {
      mnem: "Direct = I scratch yours, you scratch mine. Indirect = reputation-based (your past tells me)."
    },
    "Group selection — why naive version fails": {
      mnem: "Within-group cheaters win FAST; between-group altruistic groups win SLOW. Cheaters arrive first."
    }
  });

  // ===== L14 =====
  window.addCardPatches('L14', {
    "Major life-history milestones (timeline)": {
      exAnswer: "Memorize: 4.5 Ga Earth forms. 3.8 Ga first life (LUCA). 3.5 Ga first fossils (stromatolites). 2.4 Ga GREAT OXYGENATION EVENT (cyanobacteria). 1.8 Ga eukaryotes. 720-635 Ma snowball Earth. 540 Ma CAMBRIAN EXPLOSION. 252 Ma END-PERMIAN (~95% marine extinct, Siberian Traps). 66 Ma K-Pg (Chicxulub iridium, dinos out). 6 Ma chimp-human split. 300 Ka Homo sapiens.",
      mnem: "4.5→3.8→2.4 GOE→540 Cambrian→252 P-Tr→66 K-Pg→6 chimp split→300 Ka us."
    },
    "Radiometric dating logic": {
      mnem: "Half-life = time for half to decay. Parent/daughter ratio → age. Carbon-14 for ~50 Ka; U-Pb for billions."
    },
    "Great Oxidation Event — cause and consequence": {
      mnem: "GOE 2.4 Ga: cyanobacteria pumped O₂. Killed anaerobes (= O₂ holocaust), enabled eukaryotes."
    },
    "Cambrian explosion — what drove the radiation?": {
      mnem: "Cambrian 540 Ma: Hox genes + oxygen + ecology = animal body plans diversify FAST."
    },
    "Endosymbiosis evidence (Margulis)": {
      mnem: "Double membrane + circular DNA + 70S ribosomes + binary fission = bacterial origin."
    }
  });

  // ===== L15 =====
  window.addCardPatches('L15', {
    "Synapomorphy vs symplesiomorphy vs homoplasy": {
      exAnswer: "SYNAPOMORPHY = shared DERIVED character (defines a clade — feathers in birds). SYMPLESIOMORPHY = shared ANCESTRAL character (doesn't define a clade — vertebral column shared by all vertebrates). HOMOPLASY = independently evolved similarity (convergence — wings in bats and birds). Only synapomorphies indicate close relationship; symplesiomorphies and homoplasies are misleading.",
      mnem: "Syn = SHARED derived (groups together). Sym = SHARED ancestral (uninformative). Homo = HOMOPLASTIC (convergent)."
    },
    "Monophyletic / paraphyletic / polyphyletic": {
      exAnswer: "MONOPHYLETIC = ancestor + ALL descendants (mammals: clade). PARAPHYLETIC = ancestor + SOME descendants (reptiles excluding birds — birds ARE descendants of dinosaurs, so 'reptiles' as commonly used is paraphyletic). POLYPHYLETIC = members from MULTIPLE ancestors with NO common ancestor in the group ('warm-blooded animals' = mammals + birds = polyphyletic, evolved warm-bloodedness independently).",
      mnem: "MONO = whole branch. PARA = branch minus a twig. POLY = no branch (multiple origins)."
    },
    "Outgroup": {
      mnem: "Outgroup = closest relative OUTSIDE your clade. Polarizes ancestral vs derived."
    },
    "Crown group vs stem group": {
      mnem: "Crown = living members + last common ancestor. Stem = extinct sisters branching off earlier."
    },
    "Maximum parsimony": {
      mnem: "Parsimony = fewest evolutionary changes wins. Occam's razor for trees."
    }
  });

  // ===== L16 =====
  window.addCardPatches('L16', {
    "Sympatric speciation (when it actually works)": {
      exAnswer: "Sympatric speciation requires INSTANT reproductive isolation in the same place. Three scenarios that work: (1) POLYPLOIDY (instant tetraploid × diploid hybrids are sterile triploids — common in plants, ~50% of plant species are polyploid). (2) HOST-RACE FORMATION (Rhagoletis flies on apple vs hawthorn — different host fruits select for different mating times). (3) DISRUPTIVE SELECTION on assortative mating (cichlid color morphs in Lake Apoyo). Without one of these, gene flow swamps divergence.",
      mnem: "Sympatric = same place. Works via: polyploidy / host shift / disruptive selection."
    }
  });

  // ===== L17 =====
  window.addCardPatches('L17', {
    "Equilibrium island biogeography (MacArthur-Wilson)": {
      mnem: "MacArthur-Wilson: species richness = balance of immigration (down with distance) vs extinction (down with area). Big islands close to mainland = max diversity."
    },
    "Wallace line — sharp biogeographic boundary": {
      mnem: "Wallace line: Bali (Asian fauna) vs Lombok (Australian fauna) — 35 km apart, totally different. Deep ocean trench prevented mixing."
    },
    "Hawaiian Drosophila — peripatric explosion": {
      mnem: "Hawaiian Drosophila: ~800 species from one founder, ~25 Mya — small founder + isolation = explosive radiation."
    },
    "Latitudinal diversity gradient": {
      mnem: "More species near equator. Reasons debated: more energy, more time, more stable climate."
    },
    "Continental drift — biogeographic evidence": {
      mnem: "Marsupials in Australia + South America (no placentals there in past) — Gondwana split."
    }
  });

  // ===== L18 =====
  window.addCardPatches('L18', {
    "Fisheries-induced evolution — size selection": {
      mnem: "Fish big → caught → small fish reproduce. Cod now mature smaller and earlier than 1950."
    },
    "Bighorn sheep trophy hunting → smaller horns": {
      mnem: "Hunters take big-horned rams → small-horned alleles increase. Coltman 2003: ~25% horn shrinkage in 30 yrs."
    },
    "Florida panther genetic rescue": {
      mnem: "1995: 8 Texas pumas added to ~25 Florida panthers. Genetic rescue tripled population, fixed sperm defects."
    },
    "Inbreeding depression mechanism": {
      mnem: "Inbreeding exposes deleterious recessives (homozygous more often) → lower fitness."
    },
    "Climate change → range shifts and phenological mismatch": {
      mnem: "Species moving poleward ~17 km/decade. Mismatch when prey/host doesn't shift in sync."
    },
    "Captive breeding + reintroduction (California condor)": {
      mnem: "California condor: 1987 down to 22 wild + 5 captive = 27 founders. Now ~500. Genetic bottleneck legacy."
    }
  });

  // ===== L20 =====
  window.addCardPatches('L20', {
    "Hygiene hypothesis": {
      exAnswer: "The hygiene hypothesis says modern environments are TOO CLEAN — without diverse early-life microbial exposure, the immune system mis-trains and over-reacts to harmless allergens (asthma, hay fever) or self (autoimmunity, T1D, Crohn's). Evidence: farm-raised children + kids with multiple older siblings (more microbial exposure) have lower asthma/allergy rates. Amish (high farm exposure) vs Hutterite (similar genetics, sterile) shows ~6× difference in asthma. The immune Treg/Th2 balance needs early diverse pathogen exposure to calibrate.",
      mnem: "Too clean = immune system over-reacts. Allergies are mismatch with ancestral microbe load."
    }
  });

  console.log('[gaps] final fill applied');
})();
