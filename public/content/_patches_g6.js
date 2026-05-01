/* Patches group 6: L19, L20 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L19: {
      "Hominin": {
        exAnswer: "Hominins are all species on the human side of the chimpanzee–human split — modern Homo sapiens plus all extinct relatives (australopithecines, Homo habilis, erectus, neanderthalensis, Denisovans, etc.). Molecular clock and fossil evidence date the divergence to ~6–7 Mya in Africa. The first major distinguishing trait is BIPEDALISM (habitual two-legged walking), evident in Sahelanthropus (~7 Mya) — brain expansion came millions of years later. So the lineage is defined first by posture, not intelligence.",
        mnem: "Hominin = Human-team-only (chimps not invited). Bipedal first, big brain later."
      },
      "Bipedalism": {
        exAnswer: "Because the fossil record reverses the popular 'big brain → standing up' story. Sahelanthropus (~7 Mya) shows bipedal traits with a chimp-sized ~350 cc brain; brain expansion in genus Homo doesn't begin until ~2 Mya — five million years later. So bipedalism was selected on its own merits, likely for thermoregulation on hot savannas, energy-efficient long-distance walking, or freed hands for carrying food, infants, or tools. Brain growth then rode on different selective pressures (tools, meat-eating, social cognition).",
        mnem: "Walk first, think later — feet beat the brain by 5 million years."
      },
      "Foramen magnum": {
        exAnswer: "The position of the foramen magnum (the hole where the spinal cord exits the skull) is the smoking gun. In quadrupedal apes (chimps, gorillas), it sits at the BACK of the skull, so the spine projects horizontally. In bipedal hominins, it shifts to the BOTTOM-CENTER, so the skull balances atop a vertical spine. This single feature alone diagnosed Sahelanthropus (~7 Mya) and Ardipithecus (~4.4 Mya) as upright walkers from skull fragments, even before postcranial bones were found.",
        mnem: "Magnum on the bottom = body upright; magnum on the back = body horizontal."
      },
      "Australopithecus": {
        exAnswer: "Australopithecus is the bridge genus between ape-like ancestors and Homo. From ~4–2 Mya in Africa, species like A. afarensis (Lucy) and A. africanus had a fully bipedal pelvis, valgus knee, and longitudinal foot arch — but retained chimp-sized ~400 cc brains, curved fingers, and long arms (mosaic anatomy). They're significant because they prove bipedalism was firmly established BEFORE brain enlargement, and they're the likely ancestors (or sister group) of genus Homo. Lucy's skeleton is ~40% complete, providing the clearest single-individual snapshot of an early hominin.",
        mnem: "Australo = 'southern' ape (south Africa) — bipedal body, chimp brain. Lucy's the cover girl."
      },
      "Homo habilis": {
        exAnswer: "H. habilis (~2.4–1.5 Mya) is significant as the earliest member of genus Homo, with a brain ~600 cc (50% larger than Australopithecus) and stable association with Oldowan stone tools (sharp flakes for butchering). The toolkit evolutionary signal matters more than its crude form: STANDARDIZED designs across regions, deliberate raw-material selection, and persistence across generations imply social learning and cumulative culture — the foundation of the Homo niche. Tool-use opened new dietary niches (scavenging meat), which fed back into the brain expansion seen in H. erectus.",
        mnem: "Habilis = 'handy man' — first to make and pass on stone tools."
      },
      "Out of Africa": {
        exAnswer: "Modern Homo sapiens originated in Africa ~300 Kya and spread out in a major wave ~70 Kya, displacing or absorbing Neanderthals (Europe/W. Asia) and Denisovans (Asia) by ~40 Kya. Likely advantages include more efficient projectile weapons, complex symbolic culture (art, language), broader social networks for resource sharing, and possibly cognitive/behavioral flexibility allowing rapid adaptation to new environments. Genetic evidence (low Neanderthal/Denisovan DNA in non-Africans, ~0% in sub-Saharan Africans) confirms the African origin and limited interbreeding outside Africa.",
        mnem: "OOA = One Origin in Africa, then a single big walk-out ~70 Kya."
      },
      "Introgression": {
        exAnswer: "Introgression is gene flow between populations or species via interbreeding followed by repeated backcrossing — alleles from one lineage end up in the genome of another. The ~1–4% Neanderthal DNA in non-Africans is direct evidence that modern humans interbred with Neanderthals after leaving Africa (~50–60 Kya in the Middle East/Europe). This doesn't break the Out-of-Africa model — it refines it: the model isn't 'pure replacement' but 'replacement with limited admixture.' Some introgressed alleles (immune HLA, EPAS1 from Denisovans) were adaptively selected.",
        mnem: "Introgression = INTRO + Gression — one species CRASHES INTO another's genome."
      },
      "Neanderthal": {
        exAnswer: "Neanderthals (~400–40 Kya) went extinct ~40 Kya, soon after modern humans arrived in Europe. Likely causes include direct competition for resources, climate fluctuations stressing their small populations, and demographic absorption via interbreeding with the larger H. sapiens population. Their genome (sequenced 2010) shows they were a sister group to modern humans diverging ~600 Kya, and that ~1–4% of Neanderthal DNA persists in non-African modern humans — so they didn't fully disappear; they were partially absorbed. Larger brains than ours, but not the same cognitive package.",
        mnem: "Neander = 'Neander Valley' Germany. Big brains, big brows, partly inside us."
      },
      "Evolutionary medicine": {
        exAnswer: "This is the MISMATCH HYPOTHESIS — modern environments differ radically from the ancestral conditions our genomes were tuned to. Ancestral foragers ate diverse plants, lean meat, fiber, and were calorie-limited. Industrial diets are calorie-dense, processed, low-fiber, and laden with refined sugars/seed oils. Diseases linked to this mismatch include type 2 diabetes, obesity, atherosclerosis, dental caries, and certain cancers — all rare in traditional populations and epidemic in industrialized ones. Our metabolic and digestive adaptations are 'expecting' a Pleistocene environment we no longer inhabit.",
        mnem: "Stone-Age genome × Space-Age diet = mismatch disease."
      },
      "Virulence": {
        exAnswer: "The driver is TRANSMISSION MODE (Ewald). Respiratory pathogens like the common cold need a MOBILE host coughing on others — kill or bedrid the host and you lose transmission, so selection favors LOWER virulence. Waterborne pathogens like cholera transmit via contaminated water — host doesn't need to walk; in fact, more diarrhea = more pathogen excreted into the water supply = more transmission, so HIGH virulence is rewarded. Vector-borne (mosquito) pathogens are similar to waterborne: host immobility doesn't hurt transmission, so virulence can climb. Mode of transmission shapes the optimum.",
        mnem: "Mobile-host pathogens stay nice; water/vector pathogens go nasty."
      },
      "Mismatch hypothesis": {
        exAnswer: "Genes for efficient fat/glucose storage ('thrifty' physiology) were adaptive in ancestral environments where calories were scarce and unpredictable. Indigenous populations on traditional diets (low-glycemic, high-fiber) don't trigger pathological insulin/glucose responses. Switching to Western processed foods (refined sugars, refined grains, high glycemic load) overwhelms the thrifty machinery — chronic hyperglycemia → insulin resistance → type 2 diabetes. The genes haven't changed in 1–2 generations; the environment has. Classic environmental mismatch with an evolved physiology.",
        mnem: "Thrifty genes meet abundant calories = the body breaks. Genome can't catch up to the grocery store."
      },
      "Hominin bipedality timing": {
        mnem: "Feet first, brains later — bipedalism leads brain expansion by ~5 Myr."
      },
      "Australopithecus afarensis (Lucy) — anatomy": {
        mnem: "Lucy = ground feet + tree fingers. Walking and climbing both."
      },
      "Out-of-Africa + Neanderthal introgression": {
        mnem: "If you left Africa, you met Neanderthals. Stayed home? You didn't."
      },
      "EPAS1 — Tibetan high-altitude adaptation via Denisovan introgression": {
        mnem: "Tibetans breathe thin air on a Denisovan gene — borrowed altitude."
      },
      "Homo habilis — first stone tools (Oldowan)": {
        mnem: "Oldowan = the oldest 'wow' — first culture you can carbon-date."
      }
    },
    L20: {
      "Evolutionary medicine": {
        exAnswer: "PROXIMATE answer: immune systems involve cytokines, T cells, MHC presentation — current mechanism. ULTIMATE answer: evolution doesn't optimize, it satisficies under TRADE-OFFS. A stronger immune system costs energy, risks autoimmunity, and creates collateral damage (sepsis, allergies). The genome is also stuck with deep-time constraints (vertebrate body plan, mammalian thermoregulation) and is in an arms race with rapidly-evolving pathogens — pathogens evolve generations faster than we do. So 'better' isn't an option: every immune trait is a compromise between defense, autoimmunity, energy cost, and reproductive timing.",
        mnem: "Proximate = how it works; Ultimate = why it works that way. Mechanism vs. evolution."
      },
      "Proximate vs ultimate explanation": {
        exAnswer: "The ULTIMATE (evolutionary) explanation: fever is an evolved DEFENSE, not a malfunction. Elevated body temperature inhibits replication of many pathogens, boosts immune-cell activity (lymphocyte proliferation, neutrophil chemotaxis), and may sequester iron from invaders. Cross-species evidence: lizards bask to elevate body temperature when infected and survive better than those prevented from doing so. Implication for medicine: aggressively suppressing moderate fever may be counterproductive — a Darwinian view says the fever is the body fighting back, not the disease itself.",
        mnem: "Proximate = mechanism (HOW, the molecular wiring). Ultimate = evolution (WHY, the fitness payoff)."
      },
      "Antibiotic resistance": {
        exAnswer: "Random MUTATION created the resistance allele(s) before antibiotic exposure — every large bacterial population already carries rare resistant variants by chance. Antibiotic exposure didn't 'cause' the mutation; it imposed strong NATURAL SELECTION that killed susceptible cells, leaving resistant ones to multiply unimpeded. Once resistant cells dominate locally, HORIZONTAL GENE TRANSFER (plasmids, transformation) spreads resistance genes to other species. MRSA's β-lactam resistance is encoded by mecA, imported to Staphylococcus on a mobile genetic element from another bacterium — selection × HGT, classic Darwinian evolution on a hospital timescale.",
        mnem: "Mutation makes it; antibiotics select it; plasmids spread it."
      },
      "Horizontal gene transfer (HGT)": {
        exAnswer: "Conjugation transferred the plasmid — the donor (Klebsiella) extends a pilus to the recipient (E. coli) and copies the plasmid across. HGT also occurs by transformation (uptake of free DNA) and transduction (phage-mediated transfer). HGT is critical for resistance because it lets resistance genes JUMP species barriers in single events — bypassing the slow accumulation that vertical descent requires. A new resistance gene can spread across a hospital's bacterial flora in days, not generations. This is why resistance evolution is much faster than evolution by mutation alone.",
        mnem: "HGT = bacteria do XEROX, not just sex. Resistance genes ride plasmid taxis."
      },
      "Combination therapy": {
        exAnswer: "Resistance to a single drug typically requires one mutation, present in any large population at frequency ~10⁻⁹. With THREE drugs hitting different targets, a virus must acquire ALL THREE resistance mutations IN THE SAME GENOME to escape — joint frequency ~10⁻²⁷, vanishingly small. Sequential resistance is also blocked because any partial-resistance mutant is killed by the other two drugs before it can fix or evolve further. HIV's high mutation rate (RT lacks proofreading) means single-drug therapy fails in weeks; cART (combination) maintains viral suppression for decades.",
        mnem: "One drug = one mutation away. Three drugs = cubed away. Resistance has nowhere to go."
      },
      "Vaccine escape / antigenic drift": {
        exAnswer: "Influenza A's surface proteins (hemagglutinin, neuraminidase) accumulate point mutations under immune selection — antibodies that bound last year's strain don't bind this year's. The virus's segmented RNA genome and lack of proofreading drive a high mutation rate, and global circulation provides huge population sizes for selection to act on. Public health responds with annual surveillance (WHO Global Influenza Surveillance Network) tracking circulating strains, and yearly REFORMULATED VACCINES targeting the strains predicted to dominate the upcoming season — Red Queen pace, by design.",
        mnem: "Drift = slow point-mutation creep on flu's coat. Shift = full coat swap (reassortment, pandemics)."
      },
      "Virulence": {
        exAnswer: "Virulence is the degree of damage (morbidity/mortality) a pathogen causes its host per infection. The current value isn't fixed — it's the EQUILIBRIUM of an ongoing evolutionary process. Predicting future virulence requires knowing the selective pressures: transmission mode, host immunity, host density, vaccine pressure, treatment regime. A pathogen that's mild today can evolve to be virulent if conditions favor it (and vice versa). So predicting outcomes — for emerging viruses, vaccines, or treatments — requires evolutionary thinking, not just current epidemiology.",
        mnem: "Virulence is a moving target — selection sets the dial, not the pathogen's nature."
      },
      "Virulence-transmission trade-off": {
        exAnswer: "At an INTERMEDIATE virulence — high enough to produce enough pathogen for transmission, low enough to keep the host alive long enough to spread it. Mathematically, the optimum maximizes R₀ = (transmission rate × infectious period). Virulence boosts transmission rate but shortens the infectious period (kills the host). The optimum depends on transmission mode: respiratory pathogens (host must be mobile) → low virulence; waterborne or vector-borne (host mobility irrelevant) → higher virulence tolerated. So 'pathogens always evolve to be benign' is wrong — they evolve to MAXIMIZE SPREAD, which is sometimes nasty.",
        mnem: "Too nice = no spread. Too nasty = host dead. Sweet spot wins."
      },
      "Vector-borne": {
        exAnswer: "Malaria (mosquito vector) → HIGH virulence tolerated: bedridden host is fine for mosquitoes that bite anyway. Cholera (waterborne) → HIGH virulence: more diarrhea = more contaminated water = more transmission, host doesn't need to walk. HIV (direct sexual contact) → LOW virulence early in infection: needs a mobile, sexually active host for transmission, then virulence is delayed years. The general rule: when the host's mobility/health doesn't gate transmission, selection permits or favors high virulence; when transmission requires a healthy mobile host, low virulence wins.",
        mnem: "If the bug doesn't ride your legs, your legs don't matter — high virulence allowed."
      },
      "Ewald's hypothesis": {
        exAnswer: "Ewald's logic: with poor sanitation, contaminated water transmits cholera regardless of host mobility — so high-toxin (high-virulence) strains win because they produce more diarrhea, more water contamination, more spread. With clean water, the contaminated-water route is broken — the only way for the pathogen to spread now is via a mobile host who travels to new water sources. A bedridden host can't do that, so low-virulence strains gain. Empirical data confirm: Vibrio cholerae strains in Bangladesh (high contamination) have higher cholera-toxin output than those in Latin America (better sanitation).",
        mnem: "Clean the water = clean up the pathogen. Sanitation evolves virulence DOWN."
      },
      "MHC (Major Histocompatibility Complex)": {
        exAnswer: "Two flavors of BALANCING SELECTION compound to maintain MHC variation. (1) HETEROZYGOTE ADVANTAGE: a heterozygote presents twice as many distinct peptides to T cells, recognizing more pathogens. (2) NEGATIVE FREQUENCY-DEPENDENT SELECTION: rare alleles are favored because pathogens evolve to evade COMMON ones first; rare alleles regain advantage and rotate up. Result: MHC alleles persist for tens of millions of years (humans share alleles with chimps — trans-species polymorphism). MHC and dating: humans show subtle preferences for partners with DISSIMILAR MHC (T-shirt smell studies), maximizing offspring heterozygosity.",
        mnem: "MHC = Most Hyper-variable Code. Balancing selection keeps the allele bank stocked."
      },
      "Sickle-cell heterozygote advantage": {
        exAnswer: "Three genotypes have different fitness in malaria-endemic regions: HbA/HbA (susceptible to severe malaria — fitness penalty), HbS/HbS (severe sickle-cell anemia — fitness penalty), HbA/HbS (mild anemia, RESISTANT to severe malaria — HIGHEST fitness). Selection favors the heterozygote, but heterozygotes can't 'breed true' — they keep producing 25% HbA/HbA and 25% HbS/HbS each generation. Equilibrium allele frequency q* ≈ s_AA / (s_AA + s_SS), giving HbS ~10% in malaria-endemic regions. Where malaria is absent (Europe, North America), HbA/HbA loses no fitness, so HbS is selected OUT — explaining the geographic gradient.",
        mnem: "AS beats AA beats SS in malaria-land. Heterozygote wins, polymorphism stays."
      },
      "Antigenic variation": {
        exAnswer: "Antigenic variation lets pathogens stay one step ahead of host immunity — even within a single infection, the pathogen swaps surface proteins so antibodies built against the previous variant become useless. Trypanosomes have ~1,000 VSG (variant surface glycoprotein) genes and switch every few weeks; HIV mutates env at high rate every replication; influenza drifts seasonally and shifts via reassortment. Vaccine design is hard because there's no SINGLE conserved target — by the time immunity builds, the antigen has changed. This is why we don't have universal flu, HIV, or sleeping-sickness vaccines despite decades of effort.",
        mnem: "Antigenic variation = pathogen wears a new disguise every act."
      },
      "Mismatch hypothesis": {
        exAnswer: "Hunter-gatherer diets were low-sugar, fibrous, and required heavy chewing — teeth experienced little cariogenic acid. Modern diets (refined sugars, soft processed foods) feed Streptococcus mutans, which ferments sugar to acid and demineralizes enamel. Other dental mismatches: malocclusion (crowded teeth) from soft modern foods that don't stimulate jaw growth, and wisdom-tooth impaction from shrinking jaw size while tooth count stayed the same. Our oral microbiome and jaws evolved for tougher diets; modern foods overwhelm their ancestral defenses.",
        mnem: "Dentist visits = the bill for inventing sugar after the genome stopped paying attention."
      },
      "Hygiene hypothesis": {
        exAnswer: "Our immune systems EVOLVED to develop in the presence of diverse microbes (helminths, soil bacteria, gut commensals) — these prime regulatory T cells (Tregs) and balance Th1/Th2 arms. Modern sterile environments (urban, indoor, sanitized, antibiotics, formula-fed) deprive children of this microbial 'training,' leaving the immune system uncalibrated. The result is mis-targeting: over-active Th2 responses (asthma, hay fever, eczema), failed self-tolerance (type 1 diabetes, Crohn's, MS). Confirmed by: Amish vs Hutterite (same genome, different microbes, vastly different asthma rates) and the helminth-treatment trials reducing autoimmune symptoms.",
        mnem: "Too clean = immune system never finishes school — graduates picking fights with pollen and self."
      },
      "Diseases of civilization": {
        exAnswer: "These are chronic non-infectious diseases nearly absent in traditional foragers/horticulturalists but epidemic in industrialized populations: type 2 diabetes (refined-sugar mismatch with thrifty genes), atherosclerosis (sedentary life + processed-fat diet vs. active lifestyle the cardiovascular system was tuned for), some cancers (delayed/few pregnancies → high lifetime estrogen exposure → breast cancer; sun-deprived skin pigmentation; processed food carcinogens), mental health disorders (social isolation, light cycles disrupted, novel stressors). Each is a specific MISMATCH between an evolved physiology and a novel environment — evolution can't track the change in 1–3 generations.",
        mnem: "Diseases of civilization = bills civilization pays the genome for cheating."
      },
      "Somatic evolution": {
        exAnswer: "Cancer satisfies all Darwinian requirements for evolution within an organism. (1) HERITABLE VARIATION: somatic mutations during cell division create genetic differences among descendant cells. (2) DIFFERENTIAL FITNESS: cells with mutations disabling apoptosis, escaping growth control, or evading immunity proliferate faster. (3) DESCENT WITH MODIFICATION: each new mutation is preserved and combined with later mutations through clonal expansion. The whole tumor is a population of competing clones, with selection favoring those that grow fastest, evade immunity, and metastasize. Cancer IS Darwinian evolution on a 30-year timescale, inside one body.",
        mnem: "Cancer = a private microevolution party — each cell line a competing clone."
      },
      "Tumor heterogeneity": {
        exAnswer: "Heterogeneity matters because a single drug typically targets a specific molecular feature — and the tumor likely contains a clone LACKING that feature, which then escapes treatment and rebounds. The evolutionary process at work is CLONAL DIVERSIFICATION: ongoing somatic mutation generates variation; cellular competition (for oxygen, nutrients, space, immune evasion) selects fitter clones; the result is a heterogeneous population shaped by within-tumor selection pressures. This is why aggressive single-agent therapy often produces transient response followed by relapse with a resistant subclone — a tumor is an evolving ecosystem, not a static lump.",
        mnem: "One tumor, many clones — kill the visible ones, the hidden ones inherit the body."
      },
      "Adaptive therapy": {
        exAnswer: "Maximum-dose chemo eliminates susceptible clones entirely — but resistant clones (always present in heterogeneous tumors) are released from competition and proliferate unimpeded → relapse. Adaptive therapy uses LOWER doses that keep some susceptible cells alive, which COMPETE with resistant cells for resources (glucose, oxygen) and suppress their growth ecologically. The goal shifts from 'cure by elimination' to 'long-term control by competition.' Trials in metastatic prostate cancer (Gatenby et al., Moffitt) show adaptive therapy doubles time to progression vs. standard MTD. It's evolutionary game theory applied to oncology.",
        mnem: "Don't kill all your enemies — keep some weak ones around to crowd out the strong ones."
      },
      "Antibiotic resistance — evolution by selection": {
        exAnswer: "Resistant variants pre-exist at low frequency in any large bacterial population (random mutation). A FULL course suppresses ALL bacteria — including partially-resistant survivors — long enough to clear them. STOPPING EARLY removes the selection pressure while resistant survivors are still around: they regrow, and now the population is enriched for resistance. Each successive course selects for higher resistance. Plus, resistance genes spread by horizontal transfer to other species in the gut/environment. So 'finish the course' isn't arbitrary medical paternalism — it's an evolutionary strategy to prevent enrichment of resistant lineages.",
        mnem: "Half a course = half-killed bacteria = full-strength resistance evolution."
      },
      "Virulence-transmission trade-off (Ewald)": {
        mnem: "Mobile-host bugs play nice; water/vector bugs play dirty. Transmission mode tunes the dial."
      },
      "MHC and balancing selection": {
        mnem: "MHC = the body's most-collected stamp set. Heterozygote advantage + frequency-dependence keeps it growing."
      },
      "Sickle-cell heterozygote advantage (HbA/HbS) vs malaria": {
        mnem: "AS > AA > SS where mosquitoes bite. Polymorphism is selection's compromise."
      },
      "Cancer as somatic evolution + adaptive therapy": {
        mnem: "Tumors evolve like any population — fight them with ecology, not annihilation."
      },
      "Hygiene hypothesis": {
        mnem: "Dirty kids = trained immune system. Sterile kids = confused immune system."
      }
    }
  });
})();
