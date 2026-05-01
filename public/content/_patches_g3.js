/* Patches group 3: L09, L11, L12 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L09: {
      "Coevolution": {
        exAnswer: "No — coexistence alone doesn't prove coevolution. The diagnostic is RECIPROCAL trait change: species A's traits must impose selection on B, and B's traits must impose selection back on A. Look for matched geographic variation (where A's defense is strong, B's offense is also strong; where A is weak, B is weak) or for phylogenetic congruence between partner clades. Static co-adaptation could just be each lineage adapting separately to a shared environment.",
        mnem: "Co-evolution = Co-pressure: each side selects the other, both sides change."
      },
      "Reciprocal selection": {
        exAnswer: "Reciprocal evidence is essential because one-way adaptation isn't coevolution — it's just exploitation or co-option. To claim Asarum-fly coevolution, you'd need to show that fly olfactory preferences have shifted in response to ginger scent (e.g., flies in ginger-rich populations are MORE attracted to rotting-meat smells than naïve flies). Without that, the ginger evolved to mimic rotting meat for ALREADY-existing fly preferences — adaptation without reciprocity.",
        mnem: "Reciprocal = Round-trip selection: A→B, B→A — both arrows required."
      },
      "Coevolutionary arms race": {
        exAnswer: "Reciprocal escalation driven by antagonistic coevolution. Newts with more TTX survive snake predation → toxic newt alleles increase. Snakes with more resistant Na channels survive eating toxic newts → resistance alleles increase. Each step ratchets selection on the other species, producing the geographic correlation: high-TTX newts coexist with high-resistance snakes; low-TTX newts with low-resistance snakes. Mismatch in either direction collapses the correlation.",
        mnem: "Arms race = Escalation: bigger toxin → tougher channel → bigger toxin."
      },
      "Tetrodotoxin (TTX)": {
        exAnswer: "Voltage-gated sodium channels are HIGHLY conserved across animals because they underlie nerve and muscle function — mutating them usually breaks the organism. So TTX-resistance evolution required substitutions in a gene where most mutations are lethal. The fact that garter snakes evolved Na channel variants that block TTX binding without losing channel function shows the strength of antagonistic selection: only the rare mutations that preserve function AND resist toxin survived, and they spread despite a measurable cost (slower locomotion in resistant snakes).",
        mnem: "TTX = Targets The eXcitable membrane (Na channels) — newts' chemical weapon."
      },
      "Mutualism": {
        exAnswer: "Cheating — partners that take benefits without paying costs. An ant lineage that eats Acacia rewards but doesn't defend the tree gets a free lunch and would invade unless punished. Acacia trees enforce reciprocity by reducing reward production when ants slack off (conditional rewards) and by hosting ants that aggressively defend territory from competitor colonies. Without sanctions or partner choice, mutualisms collapse into parasitism. This is why most stable mutualisms have monitoring/punishment mechanisms.",
        mnem: "Mutualism = Mutual win: both gain, but cheaters lurk — partners must police."
      },
      "Endosymbiosis": {
        exAnswer: "Strong evidence that mitochondria are descended from a free-living alphaproteobacterium engulfed by an ancestral eukaryotic cell ~2 billion years ago. Circular DNA = bacterial-style genome; bacterial ribosomes = bacterial translation machinery; double membranes = the inner is the original bacterial membrane, the outer is the host's vacuole membrane from engulfment. The mitochondrion never left — it became permanently incorporated. Same story for chloroplasts (cyanobacterial origin, only in plants/algae).",
        mnem: "Endosymbiosis = Engulfed but Employed — bacterium became the powerhouse."
      },
      "Batesian mimicry": {
        exAnswer: "The mimic's protection collapses. Batesian mimicry is frequency-dependent: predators learn from costly experiences, but if mimics outnumber models, most attacks on the warning pattern are REWARDED with edible prey. Predators stop avoiding the signal, and the bluff fails. Mimics must remain rare relative to the toxic model for the system to work. This caps mimic population size and creates negative frequency-dependent selection.",
        mnem: "Batesian = Bluff: harmless liar must stay rare or predators call the bluff."
      },
      "Müllerian mimicry": {
        exAnswer: "Müllerian mimicry is COOPERATIVE: both species are toxic, so every predator attack reinforces the same warning lesson. Each species shares the cost of educating naïve predators, and convergence on a shared signal halves (or thirds, etc.) the per-species educational mortality. Unlike Batesian, there's no frequency limit — both species can be common. It's coadaptive because each species' fitness IMPROVES when the other becomes more abundant or signals more clearly. Same selection pressure pulls both toward the shared phenotype.",
        mnem: "Müllerian = Mutual honesty: both bite back, both gain by looking alike."
      },
      "Aposematism": {
        exAnswer: "Camouflage works ONCE per predator — but if a predator does spot you, you die. Aposematism trades cryptic safety for advertised unprofitability: the predator only needs to learn ONCE (via a bad experience with a conspecific or via innate avoidance) and then leaves all aposematic individuals alone. Net survival across the population is higher if the toxin is potent enough that predators learn to avoid the signal. Bright colors also help kin learning (offspring of nearby toxic frogs share the same warning).",
        mnem: "Aposematic = Advertised poison: 'Look at me, I'll make you regret it.'"
      },
      "Geographic Mosaic Theory of Coevolution": {
        exAnswer: "It's called a coevolutionary mosaic, with HOTSPOTS (sites of intense reciprocal selection and tight matching) and COLDSPOTS (sites with weak or absent selection, no matching). Gene flow among populations + locally varying selection produces a patchwork. Crucially, the Mosaic theory PREDICTS some sites will show mismatch — that's not evidence against coevolution but rather a signature of dynamic, geographically-varying coevolutionary process.",
        mnem: "Mosaic = Map of hotspots and coldspots: coevolution varies by zip code."
      }
    },
    L11: {
      "Twofold cost of sex": {
        exAnswer: "Per generation, sexual mothers transmit only 50% of their genome to each offspring (the other 50% comes from the male), while asexual mothers transmit 100%. So a sexual female effectively passes HALF the gene-copies an asexual female does — a 2× reproductive disadvantage. For sex to persist, recombination's benefits (Red Queen, Muller's ratchet escape, novel allele combinations) must outweigh this 2× per-generation cost. The fact that sex IS nearly universal in eukaryotes shows those benefits are real and substantial.",
        mnem: "2× cost = Sex shares the seat: only ½ your genes ride along per offspring."
      },
      "Muller's ratchet": {
        exAnswer: "Without recombination, a 'clean' (mutation-free) genome can't be reconstructed from two parents who each have different mutations. Once the zero-mutation class is lost to drift, it's gone forever — every descendant inherits at least one deleterious mutation. The ratchet clicks but never unclicks. Predicts asexual lineages should accumulate mutational load over time → mutational meltdown → eventual extinction. Explains why most asexual lineages are evolutionarily young (they don't last).",
        mnem: "Ratchet = one-way clicks: mutations stack up, no way to wind back."
      },
      "Red Queen hypothesis": {
        exAnswer: "Parasites adapt fastest to LOCALLY COMMON host genotypes. In parasite-rich deep lakes, common asexual clones are quickly exploited and crash; sex generates novel allele combinations each generation, so sexual hosts stay one step ahead. In shallow parasite-poor lakes, no such race exists, so the twofold cost of sex dominates and asexuals win. The geographic split between sexual and asexual forms tracks PARASITE PRESSURE — direct support for the Red Queen.",
        mnem: "Red Queen = Run to stay still: sex outpaces coevolving parasites."
      },
      "Anisogamy": {
        exAnswer: "Because anisogamy creates the asymmetric resource investment that drives all downstream sex differences. The sex producing big costly gametes (eggs) is RESOURCE-LIMITED in reproduction → choosy. The sex producing tiny cheap gametes (sperm) is ACCESS-LIMITED to eggs → competitive. From this single asymmetry follow: female mate choice, male-male competition, sperm competition, parental investment differences, and ultimately most sexual dimorphism. Behavior follows from gamete economics, not the reverse.",
        mnem: "Anisogamy = Aniso (unequal) gametes: big egg, small sperm — origin of male/female."
      },
      "Isogamy": {
        exAnswer: "Phylogenetic and theoretical evidence both support isogamy → anisogamy as the direction of evolution. Phylogenetically, isogamous taxa (some algae, fungi) sit at deeper branches of the tree, with anisogamy appearing in derived lineages. Theoretically, disruptive selection on gamete size (small gametes = many produced; large gametes = better-provisioned zygotes) favors the splitting of one gamete type into two specialized classes. Once anisogamy emerges, it tends to be evolutionarily stable, so reverting is rare.",
        mnem: "Isogamy = Identical gametes — the egalitarian ancestor of male-vs-female."
      },
      "Sexual selection": {
        exAnswer: "Because the peacock's tail decreases survival (drag, predator visibility, energy cost) yet persists — natural selection alone would prune it. The tail evolved because it INCREASES MATING SUCCESS (peahens prefer long, eyespotted tails). Sexual selection is selection acting on traits that improve reproduction at the cost of survival. Darwin proposed it explicitly to explain ornaments that natural selection couldn't account for. The trait persists when the mating-success benefit > survival cost.",
        mnem: "Sexual selection = Sex over Survival: traits that win mates even if they shorten life."
      },
      "Intrasexual selection": {
        exAnswer: "Intrasexual selection. Male elephant seals are competing AMONG MALES (within the same sex) for access to females; the females aren't choosing based on male displays but rather mating with whichever male holds the harem. The selection pressure is male-vs-male combat, which favors body size, weapons, and aggression in males — classic intrasexual signatures.",
        mnem: "Intra = Inside one sex: male-vs-male brawl for access."
      },
      "Intersexual selection": {
        exAnswer: "Intersexual selection. Female bowerbirds are CHOOSING among males based on a signal trait (bower elaborateness); males don't physically fight but display, and females discriminate. The selection pressure comes from the OPPOSITE sex's preferences. Classic intersexual signatures: ornaments, courtship displays, song, color — extravagant signals built to be evaluated by the choosing sex.",
        mnem: "Inter = Inter-sex choice: she picks, he displays."
      },
      "Sexual dimorphism": {
        exAnswer: "Mostly INTRASEXUAL. Lion male body size (and manes) function in male-male combat for control of prides — bigger males win fights and hold harems. Females don't choose based on size; they're herded by whichever male has won. The mane is partly a damage shield in fights and partly a signal of fighting ability to other males. Ornaments evaluated by females (intersexual) tend to be more extravagant and more costly; weapons evaluated by rivals (intrasexual) tend to be more functional.",
        mnem: "Dimorphism = Dual morphs: usually built for combat or for courtship."
      },
      "Sexual conflict": {
        exAnswer: "Conflict because the male's optimum (mate, transfer harmful seminal proteins that boost his paternity by suppressing female remating) reduces female fitness (she lays fewer total eggs, dies sooner). What's good for his genes is bad for hers. Females evolve counter-adaptations: detoxifying seminal proteins, evolving immune resistance to the harm, or behavioral resistance to remating. This is antagonistic coevolution WITHIN a species, generating rapid genital and behavioral divergence between species.",
        mnem: "Sexual conflict = Sexes' interests collide: his win can be her loss."
      },
      "Sperm competition": {
        exAnswer: "Chimps: high sperm competition → promiscuous (multi-male-multi-female) mating, where multiple males inseminate the same female and sperm compete inside her. Big testes win the lottery (more sperm = more eggs fertilized). Gorillas: low sperm competition → single-male-harem mating, where one silverback monopolizes females and rivals don't get access. Small testes are sufficient because there's no rival sperm to compete with. Testis size is a near-universal predictor of mating system across primates and many other taxa.",
        mnem: "Sperm competition = Sperm race: bigger testes for promiscuous, smaller for monogamous."
      },
      "Cryptic female choice": {
        exAnswer: "'Cryptic' because the choice happens INTERNALLY after copulation — invisible from outside, unlike pre-mating mate choice. Females may store sperm from multiple males, eject sperm of unwanted mates, kill sperm with reproductive-tract chemistry, or differentially transport sperm to eggs. This means observed copulation frequency doesn't equal paternity: a male may mate often but sire few offspring. Researchers must use genetic paternity assignment, not copulation counts, to measure male reproductive success.",
        mnem: "Cryptic = Concealed inside: female filters sperm AFTER mating."
      },
      "Antagonistic coevolution": {
        exAnswer: "Sexually antagonistic coevolution (also called intersexual arms race). Male traits evolve to maximize male fitness even at female cost; female counter-traits evolve to neutralize the male trait; each step generates new selection on the other → rapid coevolutionary cycling within a species. Signatures: harmful male coercion structures, female resistance morphology, very rapid divergence of genitalia and reproductive proteins among closely-related species. Same logic as Red Queen, but inside a species rather than between.",
        mnem: "Antagonistic coevolution = Adversarial arms race — between species OR between sexes."
      }
    },
    L12: {
      "Life history": {
        exAnswer: "A life history is the EVOLVED SCHEDULE of reproduction and survival across the lifespan — when an organism matures, how often it breeds, how many offspring it produces per attempt, how long it lives. It's a coherent strategy shaped by selection, not a list of independent traits. The fast (early/many/short) and slow (delayed/few/long) extremes both maximize fitness in their respective environments. Selection chooses among schedules given the trade-offs available.",
        mnem: "Life history = Life schedule: when to mature, breed, age, die."
      },
      "Trade-off": {
        exAnswer: "Trade-off: current reproduction vs. future reproduction. Constraint: ENERGY (the octopus's finite caloric budget). Pouring all reserves into one giant brood — guarding eggs without eating — leaves nothing for survival, so semelparity is enforced by physiological exhaustion. The energy currency literally can't fund both this brood and future broods. Whenever a fitness component competes with another for a limited shared pool (energy, time, mortality risk), a trade-off arises.",
        mnem: "Trade-off = This OR that: shared budget, can't fund both."
      },
      "Reproductive effort": {
        exAnswer: "Because optimal effort depends on extrinsic mortality. Salmon face high return-migration mortality → 'big-bang' semelparity is optimal (don't bank on a second chance you probably won't get). Perch face lower adult mortality → spread reproduction over years (iteroparity), since hedging across multiple seasons beats betting it all on one. Same selective logic (maximize lifetime reproduction), different optima because the survival landscape differs. Reproductive effort is shaped by the probability of surviving to breed again.",
        mnem: "Reproductive effort = how much you spend NOW vs. save for LATER."
      },
      "Extrinsic mortality": {
        exAnswer: "With predators: FAST life history — earlier maturity, more (smaller) offspring, shorter life. Without predators: SLOW life history — delayed maturity, fewer (larger) offspring, longer life. Reznick's classic guppy experiments confirmed this: predator-pond guppies mature faster and reproduce more in ~30 generations. Selection is direct: under high extrinsic mortality, individuals who delay reproduction are likely to die before breeding, so early reproducers leave more descendants.",
        mnem: "Extrinsic = External killers (predators, weather): more risk → live fast, die young."
      },
      "Intrinsic mortality / senescence": {
        exAnswer: "Senescence (intrinsic mortality from aging). Even without external causes, internal failure accumulates: cellular damage, mutation buildup, cumulative wear on organs. Selection cannot eliminate this because its strength declines with age — natural selection has little leverage on traits expressed AFTER reproduction is largely complete. So aging genes/effects accumulate as side-effects (mutation accumulation), or are actively favored when they trade late-life cost for early-life benefit (antagonistic pleiotropy).",
        mnem: "Intrinsic = Inside-out failure: aging happens even with zero external threats."
      },
      "Senescence": {
        exAnswer: "Selection's strength is proportional to how many future offspring a trait affects. A mutation hurting a 5-year-old reduces lifetime fitness sharply (lots of reproduction left to lose). A mutation hurting a 50-year-old reduces fitness barely at all (most reproduction is already done). So late-acting deleterious effects are nearly invisible to selection and accumulate as mutational byproducts, while early-acting good effects with late costs (antagonistic pleiotropy) are favored. Aging is the inevitable side-effect, not a programmed end.",
        mnem: "Senescence = Selection sees less of you with age — so damage accumulates."
      },
      "Mutation accumulation theory": {
        exAnswer: "Predicts that mortality should RISE STEEPLY with age past the age of last reproduction, because late-acting deleterious mutations are invisible to selection and pile up randomly across the genome. Different individuals carry different late-acting mutations, so causes of death diverge in old age. Predicts heritable variation in late-life traits (because no selection erases it) and supports observation that aging-related diseases are heterogeneous (cancer, heart disease, dementia — many independent failure modes).",
        mnem: "Mutation accumulation = Mutations hide in old age — selection blind, damage piles up."
      },
      "Antagonistic pleiotropy": {
        exAnswer: "Because selection's strength is much greater on early-life traits (early reproduction matters more for fitness), so an allele giving big early-life benefits + late-life costs has a NET POSITIVE effect on lifetime reproduction. The young organism gets boosted reproductive output during its prime; the late-life cost (prostate cancer at 60+) is largely after reproduction is mostly complete, so selection barely sees it. Even if the late-life cost is severe, it can't outweigh the early-life gain in evolutionary terms.",
        mnem: "Antagonistic pleiotropy = One gene, two ages, two effects: helps young, hurts old."
      },
      "Disposable soma theory": {
        exAnswer: "The body (soma) and germline compete for limited energy. Caloric restriction shifts allocation AWAY from reproduction (fewer offspring) and TOWARD somatic maintenance (DNA repair, antioxidants, autophagy) → longer life. Under normal conditions, selection favors investing in reproduction over body upkeep, since the soma is 'disposable' — it just needs to last long enough to reproduce. This is why aging is universal in organisms with germ-soma distinction: the body was never built to last.",
        mnem: "Disposable soma = Body is a disposable shell — repair just enough to reproduce."
      },
      "Age at maturity": {
        exAnswer: "Because in elephants, adult survival is high and parental investment per calf is enormous (~22-month gestation, ~5 years lactation). Maturing early at small body size would mean inadequate maternal resources to raise a calf, lower offspring survival, and few total grandchildren. Delaying maturity until full body size and social rank is reached pays off: a few well-provisioned calves over 50+ years far exceed many under-provisioned calves. Slow life histories are favored when extrinsic mortality is low and per-offspring investment matters.",
        mnem: "Age at maturity = First-breeding age — delay pays when adults survive long."
      },
      "r/K selection": {
        exAnswer: "Mice (r): ~6-12 offspring per litter, multiple litters per year, no parental care beyond weaning, mature at ~6 weeks, lifespan ~1-2 years. Elephants (K): 1 calf every 4-5 years, intense maternal care for years, mature at 12-15 years, lifespan ~60-70 years. r-selection wins in unstable, low-density environments where rapid colonization is rewarded; K-selection wins in stable, saturated environments where competition for resources rewards higher per-offspring investment.",
        mnem: "r = Rapid (mice many small) · K = Carrying capacity (elephants few big)."
      },
      "Cooperative breeding": {
        exAnswer: "In Hamilton's inclusive-fitness terms: a helper raising siblings (r=0.5) gains INDIRECT fitness equal to a parent raising offspring (also r=0.5). When ecological constraints make independent breeding hard (saturated territories, scarce mates), the COST of staying-and-helping is low (not much breeding opportunity available anyway), and indirect fitness through siblings outweighs the marginal direct fitness gain of dispersing. Hamilton's rule rB > C is satisfied because B is positive (siblings really do benefit), r is high, and C is low.",
        mnem: "Cooperative breeding = Common breeding family: helpers stay, kin gain."
      },
      "Sex-biased dispersal": {
        exAnswer: "It says philopatric females gain more from STAYING (helping kin, inheriting territory, sharing local knowledge) than they would from dispersing, while males gain more from DISPERSING (avoiding inbreeding, finding their own territory). This pattern is common when one sex's reproductive success depends heavily on territory quality (favored to stay) and the other's depends on access to mates (favored to disperse). It also reduces inbreeding by ensuring the sexes don't both stay in the natal site.",
        mnem: "Sex-biased dispersal = One sex stays, one sex strays — usually anti-inbreeding."
      }
    }
  });
})();
