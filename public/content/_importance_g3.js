/* Importance content (group 3: L09, L11, L12) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  window.addCardPatches('L09', {
    "Coevolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Coevolution is RECIPROCAL — adaptation must run both ways, or it isn't coevolution. Robbins will hit you on this distinction in a definition or matching question.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Two (or more) lineages — coevolution requires at least a pair imposing reciprocal selection on each other.</li><li>Three flavors: antagonistic (predator-prey, host-parasite), mutualistic (pollinator-plant), and within-species (sexual conflict).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Foundational concept for L09.</strong> Every later card (TTX arms race, mimicry, geographic mosaic) is a special case of coevolution.</li><li><strong>Common exam-trap.</strong> Robbins likes to give you two species in the same forest and ask "is this coevolution?" The answer is "not necessarily" — you need evidence of reciprocal trait change.</li><li><strong>Distinguishes coevolution from convergent evolution.</strong> Convergence = similar traits in unrelated lineages with no reciprocal feedback. Coevolution = feedback loop.</li></ol>
<h4>Coevolution vs coexistence vs convergence</h4>
<ul><li>Coexistence: two species share habitat. Not enough for coevolution.</li><li>Convergence: similar solutions to similar problems, no feedback. Not coevolution.</li><li>Coevolution: trait change in A drives trait change in B drives further change in A.</li></ul>`
    },
    "Reciprocal selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Reciprocal selection is the MECHANISM that makes coevolution real — A imposes selection on B, B imposes selection back on A. Without reciprocity, it's just parallel adaptation.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Two-way feedback — required for the term to apply.</li><li>Diagnostic signature: geographic correlation (where A is strong, B is strong; where A is weak, B is weak).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Distinguishes coevolution from one-sided adaptation.</strong> A plant adapting to a static abiotic stressor is not coevolution — there's no reciprocal feedback.</li><li><strong>Robbins exam-trap:</strong> "Wild ginger evolved scent that mimics rotting meat to attract carrion flies." This is one-sided unless flies have changed in response. Look for reciprocal evidence.</li><li><strong>Evidence for reciprocity</strong> = matched geographic variation in interacting traits across the range. Static co-adaptation alone is suggestive but not definitive.</li></ol>`
    },
    "Coevolutionary arms race": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Antagonistic coevolution escalates offense and defense in lockstep — the textbook newt/snake TTX system is THE go-to example, and Robbins will likely use it on the exam.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Rough-skinned newt <em>Taricha granulosa</em> can carry enough TTX to kill ~17 adult humans (most toxic terrestrial vertebrate).</li><li>Garter snake <em>Thamnophis sirtalis</em> resistance comes from amino acid substitutions in the Nav1.4 sodium channel.</li><li>Resistant snakes pay a SPEED cost — slower locomotion = more vulnerable to bird predation. This caps the escalation.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classic case study Robbins will reference.</strong> Brodie's lab work is the textbook arms race example — know it cold.</li><li><strong>Demonstrates trade-off limits.</strong> Arms races don't escalate forever; resistance has a fitness cost.</li><li><strong>Geographic variation = key signature.</strong> Where snakes are resistant, newts are toxic; where snakes are sensitive, newts are weakly toxic. Co-variation is the smoking gun.</li></ol>
<h4>Exam-trap</h4>
<ul><li>Don't say arms races escalate forever — fitness costs cap the escalation.</li><li>Uniform "one-size-fits-all" adaptations argue AGAINST ongoing coevolution. Look for variation.</li></ul>`
    },
    "Tetrodotoxin (TTX)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> TTX is the molecular weapon at the heart of the most famous arms race in evolutionary biology — Robbins will expect you to name the toxin, the mechanism (Na channel block), and the trade-off in resistance.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>TTX blocks voltage-gated sodium channels (Nav) — the same channels that fire neurons in mammals.</li><li>Resistance evolved via point mutations in the Nav1.4 channel pore region.</li><li>Resistant snakes are ~30-50% slower than sensitive snakes — a real survival cost.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Mechanism specificity.</strong> Robbins may ask WHY TTX is so dangerous — answer: it blocks ion channels essential to all neuronal firing.</li><li><strong>Resistance evolved repeatedly.</strong> Convergent point mutations in the Nav channel across snake populations — a clean demo of parallel molecular evolution.</li><li><strong>Trade-off keeps the system from running away.</strong> Slower snakes get eaten by birds; cost prevents universal resistance.</li></ol>`
    },
    "Mutualism": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mutualism is coevolution where BOTH partners win — but cheating is always a threat, and stable mutualisms have enforcement. Robbins will hit you on the "cheater problem".</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Acacia-ant mutualism: ants get hollow thorns (domatia) + Beltian bodies (food); tree gets herbivore protection.</li><li>Yucca-yucca moth: moth pollinates yucca flowers and lays eggs in ovary; tree aborts overstuffed fruits to limit moth larvae (enforcement).</li><li>Fig-fig wasp: ~750 fig species, each with ~1 specialist wasp pollinator.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Mutualism is NOT cooperation for the good of the species.</strong> Each partner is selected for individual fitness — mutual benefit is a coincidence of interests. Key Robbins point.</li><li><strong>Cheating is always favored if unenforced.</strong> Selection on each partner favors taking benefits without paying costs.</li><li><strong>Stable mutualisms require enforcement</strong> — partner choice, sanctions, or shared interests preventing cheaters from invading.</li></ol>
<h4>Acacia-ant example</h4>
<ul><li>Tree provides: hollow thorns (housing), nectar from extrafloral nectaries, Beltian bodies (protein-rich food).</li><li>Ants provide: aggressive defense against herbivores AND clearing of competing vegetation.</li><li>Cheating: some ant species occupy thorns but don't defend — selected against by tree's nectar control.</li></ul>`
    },
    "Endosymbiosis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Endosymbiosis is the deepest and most consequential mutualism in life's history — mitochondria from an alphaproteobacterium ~2 billion years ago. Robbins will quiz the FOUR LINES of evidence.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Mitochondrial origin: ~1.5–2.0 billion years ago (Gya), from an alphaproteobacterium ancestor.</li><li>Chloroplast origin: ~1.5 Gya, from a cyanobacterium ancestor (Archaeplastida lineage only).</li><li>FOUR lines of evidence: (1) double membrane, (2) circular DNA, (3) bacterial-style 70S ribosomes, (4) binary fission for replication.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Memorize the four lines of evidence.</strong> Robbins will want them in any test of endosymbiosis. Double membrane (inner = bacterial, outer = host vesicle), circular DNA, 70S ribosomes, fission.</li><li><strong>Two distinct events nested in the eukaryotic tree.</strong> Mitochondrion came FIRST (universal); chloroplast came LATER, only in plants/algae.</li><li><strong>Shows mutualism can become OBLIGATE</strong> — neither partner can live without the other today. The deepest possible coevolutionary lock-in.</li></ol>
<h4>Why the order matters</h4>
<ul><li>Animals have mitochondria but no chloroplasts → animals branched off before chloroplast event.</li><li>Plants have both → chloroplast event happened in a lineage that already had mitochondria.</li><li>Lynn Margulis's serial endosymbiosis theory — vindicated decades later by molecular phylogenetics.</li></ul>`
    },
    "Batesian mimicry": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Batesian = HARMLESS mimic resembles HARMFUL model — a BLUFF that only works if mimics stay rare. Frequency-dependence is the testable feature Robbins loves.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Mimic must be RARER than the model — high mimic-to-model ratios collapse the bluff (predators stop avoiding the signal).</li><li>Classic example: hoverflies (harmless) mimicking wasps (stinging).</li><li>The model PAYS the cost (being toxic); the mimic FREE-RIDES on the warning signal.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Frequency-dependent selection — a key exam concept.</strong> The mimic's advantage decreases as it becomes common. This is unlike most directional selection.</li><li><strong>Robbins will contrast Batesian with Müllerian.</strong> Be ready to identify which is which from a scenario.</li><li><strong>The "cheater" of mimicry.</strong> The mimic is essentially parasitizing the model's reputation.</li></ol>
<h4>Batesian vs Müllerian (memorize this contrast)</h4>
<ul><li>Batesian: ONE harmful model + harmless mimic. Mimic is the cheater. Must stay rare.</li><li>Müllerian: TWO+ harmful species converge. Both pay the toxin cost. Frequency doesn't matter; both can be common.</li></ul>`
    },
    "Müllerian mimicry": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Müllerian = MULTIPLE harmful species converge on one warning signal — both partners share the cost of educating predators. Robbins's trick question is whether this counts as coevolution AND convergence (yes to both).</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Classic system: <em>Heliconius</em> butterflies — co-mimics with shared warning patterns across rainforest "rings".</li><li>Each <em>Heliconius</em> "mimicry ring" can include 2-10+ species converging on one wing pattern.</li><li>Both species are unpalatable — predators learn the lesson once, all members benefit.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Both species pay the toxin cost.</strong> No cheaters — every encounter teaches the SAME lesson, reinforcing the signal.</li><li><strong>Counts as convergent evolution AND coevolution simultaneously.</strong> A favorite Robbins exam-trap.</li><li><strong>Frequency-INDEPENDENT.</strong> Unlike Batesian, no problem if both species are common — that's actually better.</li></ol>
<h4>Bates vs Müller mnemonic</h4>
<ul><li><strong>Bates = Bluff</strong> (one liar, one truth-teller).</li><li><strong>Müller = Mutual</strong> (both honest, sharing the cost).</li></ul>`
    },
    "Aposematism": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Aposematism = "I am dangerous, see me coming" — conspicuous warning coloration. Robbins will ask why obvious coloration is favored over camouflage when you're toxic.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Classic examples: poison dart frogs (Dendrobatidae), monarch butterflies, coral snakes, skunks.</li><li>Aposematism only works AFTER predators learn — initial mortality must be paid by some "teacher" individuals.</li><li>Often accompanied by neophobia in predators (innate caution toward bright colors).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Counterintuitive payoff.</strong> Why be conspicuous when you're toxic? Because PREDATORS NEED TO LEARN — and unmemorable prey teach nothing.</li><li><strong>Necessary precondition for mimicry.</strong> No aposematic model = no Batesian mimic. No co-aposematic species = no Müllerian rings.</li><li><strong>Frequency-dependent at startup.</strong> Aposematism evolves more easily when prey are clumped (kin survive after one is sampled).</li></ol>`
    },
    "Geographic Mosaic Theory of Coevolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Thompson's MOSAIC theory: coevolution happens in HOTSPOTS and COLDSPOTS across geography — and trait MISMATCH is evidence FOR ongoing coevolution, not against it. Robbins will absolutely test the mismatch logic.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Three mechanisms: (1) selection mosaic (different sites favor different outcomes), (2) coevolutionary hotspots (intense reciprocal selection) and coldspots (weak/none), (3) trait remixing via gene flow.</li><li>Predicts spatially variable trait combinations across a species' range.</li><li>Best documented in: newt-snake (Brodies), crossbill-pine (Benkman), Greya moth-Lithophragma plant (Thompson).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins exam-trap (high confidence).</strong> If asked "does trait mismatch refute coevolution?" the answer is NO — mosaic theory predicts mismatch in coldspots.</li><li><strong>Reframes coevolution as a dynamic landscape.</strong> Not a single endpoint but a patchwork that changes over space and time.</li><li><strong>Combines local adaptation + gene flow + reciprocal selection.</strong> Three forces interacting across a heterogeneous landscape.</li></ol>
<h4>Hotspot vs coldspot</h4>
<ul><li>Hotspot: intense reciprocal selection, tightly co-adapted traits.</li><li>Coldspot: weak or no reciprocal selection — traits drift, mismatch from immigrant alleles, no selection to fix the match.</li></ul>`
    },
    "Coevolution vs coexistence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Coexistence ≠ coevolution. The diagnostic for coevolution is RECIPROCAL trait change tracked across populations or time, not just sharing space. Robbins's favorite definitional trap.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Two species + same forest = coexistence (necessary but not sufficient).</li><li>Two species + matched trait variation across populations = coevolution (necessary AND sufficient).</li><li>Geographic correlation in interacting traits is the gold-standard evidence.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>This is THE most likely L09 multiple-choice trap.</strong> Robbins will give you two species coexisting and ask whether that's coevolution.</li><li><strong>Static co-adaptation could be coincidence.</strong> Only matched DYNAMIC variation across populations rules out alternatives.</li><li><strong>Diagnostic example: TTX.</strong> Newt toxicity correlates with snake resistance across the West Coast — that's diagnostic, not coincidence.</li></ol>
<h4>What to look for as evidence</h4>
<ul><li>Geographic correlation in interacting traits.</li><li>Heritable trait change in BOTH species.</li><li>Selection pressure imposed by one on the other (and vice versa).</li><li>Mismatched populations with neither extreme phenotype.</li></ul>`
    },
    "Newt-snake arms race (TTX example)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Brodie's newt-snake system is THE textbook arms race — Robbins will hit you on the geographic correlation, the molecular mechanism (Nav1.4), and the trade-off (resistance costs speed).</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Newt: <em>Taricha granulosa</em>; toxin: TTX (tetrodotoxin); enough in one newt to kill ~17 humans.</li><li>Snake: <em>Thamnophis sirtalis</em>; resistance via amino-acid substitutions in Nav1.4 sodium channel pore.</li><li>Resistant snakes are ~30-50% slower; cost caps escalation.</li><li>Geographic match: high TTX where high resistance; low TTX where low resistance.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classic study system — know names cold.</strong> "Brodie newts and Brodie snakes" (Edmund Brodie Sr. and Jr.).</li><li><strong>Demonstrates molecular evolution.</strong> Specific point mutations in Nav1.4 channel pore confer resistance — beautiful gene-to-phenotype story.</li><li><strong>Trade-off logic.</strong> Resistance ISN'T free — slower snakes = more bird predation. This caps the arms race.</li></ol>
<h4>Why this is the canonical case</h4>
<ul><li>Geographic correlation across the West Coast (CA to OR).</li><li>Molecular mechanism worked out at the amino acid level.</li><li>Reciprocal selection demonstrated experimentally.</li><li>Trade-off measured (locomotion cost of resistance).</li></ul>`
    },
    "Batesian vs Müllerian mimicry": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Bates = ONE liar (frequency-dependent, must stay rare); Müller = MUTUAL honest (both noxious, both reinforce signal, frequency-independent). Robbins will absolutely give you a scenario and ask which.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>BATESIAN: 1 model (toxic) + 1 mimic (harmless) — mimic must be rarer than model.</li><li>MÜLLERIAN: 2+ species, all toxic — converging on one shared warning signal.</li><li>Heliconius mimicry rings: 2-10 species converging on one wing pattern.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The most testable comparison in L09.</strong> Robbins's go-to short-answer setup.</li><li><strong>Frequency-dependence is the killer feature.</strong> Bates collapses if mimic is too common; Müller doesn't care.</li><li><strong>Cost-sharing logic.</strong> Müller is mutualistic (both pay toxin cost); Bates is parasitic (mimic free-rides).</li></ol>
<h4>The Bates-Müller cheat sheet</h4>
<ul><li><strong>Bates = Bluff</strong> (one liar). Frequency-dependent. Mimic must stay rare.</li><li><strong>Müller = Mutual</strong> (both honest). Frequency-independent. Both can be common.</li><li>Viceroy + Monarch: actually Müllerian (both noxious) — overturned old textbook claim.</li><li>Hoverfly + wasp: Batesian (hoverfly is harmless).</li></ul>`
    },
    "Geographic Mosaic Theory of Coevolution (Thompson)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mismatch is evidence FOR mosaic coevolution, not against it. This is THE counterintuitive logic Robbins loves to test.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Three mechanisms: selection mosaic + hotspots/coldspots + trait remixing via gene flow.</li><li>Hotspot = intense reciprocal selection; Coldspot = weak/no reciprocal selection.</li><li>Best examples: crossbill-pine (Benkman), Greya moth-Lithophragma (Thompson), newt-snake (Brodies).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins's favorite mosaic exam-trap:</strong> "Crossbill beaks match local pine cones in some valleys but not others. Does this disprove coevolution?" Answer: NO. Mosaic predicts mismatch in coldspots.</li><li><strong>Distinguishes mosaic theory from naïve local adaptation.</strong> Mosaic specifically requires reciprocal feedback between species — both parties evolve.</li><li><strong>Solves the "imperfect adaptation" puzzle.</strong> Why don't all populations show tight matching? Because gene flow + variable selection prevents universal optimization.</li></ol>
<h4>Hotspot vs coldspot reasoning</h4>
<ul><li>Hotspot: high abundance of both species + ecological conditions that intensify the interaction → reciprocal selection.</li><li>Coldspot: low abundance, alternative resources, or different selective regime → weak reciprocal selection.</li><li>Gene flow between zones blurs trait matching.</li></ul>`
    },
    "Pollinator-flower mutualism (Darwin's orchid prediction)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Darwin saw a 25-cm-spurred orchid and PREDICTED a 25-cm-tongued moth must exist — and was right. Robbins loves this story because it shows coevolutionary prediction works.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Plant: Madagascar star orchid (<em>Angraecum sesquipedale</em>); spur length ~25-30 cm.</li><li>Moth: <em>Xanthopan morganii praedicta</em>; tongue ~25 cm.</li><li>Darwin made prediction in 1862; moth discovered in 1903 — 21 years after Darwin's death; subspecies named "praedicta" in his honor.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classic coevolutionary prediction story.</strong> Robbins will likely use this as the canonical mutualism example.</li><li><strong>Reciprocal selection mechanism.</strong> Longer spurs force moths to push deeper → more pollen contact → flower fitness up. Longer tongues reach more nectar → moth fitness up.</li><li><strong>Tight trait matching → past coevolution.</strong> Steady-state evidence of mutual escalation.</li></ol>
<h4>Why this exemplifies mutualistic coevolution</h4>
<ul><li>Both partners gain fitness from the interaction.</li><li>Each partner's traits create selection on the other.</li><li>Match isn't coincidence — it's the result of feedback.</li><li>Predictive: Darwin used the logic to forecast unseen species.</li></ul>`
    },
    "Endosymbiosis: two distinct organelle origins": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mitochondria came FIRST (~2 Gya, alphaproteobacterium, universal in eukaryotes); chloroplasts came LATER (~1.5 Gya, cyanobacterium, only Archaeplastida). Order and exclusivity matter on the exam.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Mitochondrion: ~1.5-2.0 Gya, alphaproteobacterium, ALL eukaryotes inherit it (or did originally).</li><li>Chloroplast: ~1.5 Gya, cyanobacterium, only Archaeplastida (plants + green/red algae).</li><li>Four lines of evidence (apply to both): double membrane, circular DNA, 70S bacterial ribosomes, binary fission.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Two events nested in the tree.</strong> Mitochondrion in stem; chloroplast in one daughter lineage. Animals branched off before chloroplast event — that's why we don't have them.</li><li><strong>Distribution of organelles tells you the order.</strong> Animals: mito only. Plants: both. Some "primitive" protists: appear to lack functional mito (have remnant organelles).</li><li><strong>Tertiary endosymbiosis</strong> — chloroplasts later spread to other eukaryotes by engulfing whole algal cells. Adds nuance Robbins might mention.</li></ol>
<h4>The four lines of evidence (cold)</h4>
<ul><li>Double membrane — inner is bacterial-style, outer is host vesicle.</li><li>Circular DNA — like bacteria, unlike nuclear DNA.</li><li>70S ribosomes — bacterial-style, sensitive to bacterial antibiotics (chloramphenicol).</li><li>Binary fission — replicates independently of nucleus.</li></ul>`
    }
  });

  window.addCardPatches('L11', {
    "Anisogamy = the basis of male/female": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Anisogamy (unequal gamete sizes) is THE asymmetry that creates "male" and "female" — and from it everything else (Bateman, parental investment, sexual selection, conflict) follows.</p>
<h4>The numbers (memorize these)</h4>
<ul><li><strong>Female gamete</strong> = large, costly, few (mammalian egg ~120 µm, ~10⁵× volume of sperm).</li><li><strong>Male gamete</strong> = small, cheap, many (sperm ~5 µm head; humans produce ~10⁸/day).</li><li>Isogamy (equal gametes) is ancestral — anisogamy evolved independently many times.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>"Male" and "female" are operational definitions tied to gamete size, not chromosomes.</strong> Don't define sex by XY — define it by who makes the small gametes.</li><li><strong>Anisogamy → Bateman's principle.</strong> Few costly eggs → female fitness limited by resources. Many cheap sperm → male fitness limited by mate access. This is the foundation of all sexual selection theory.</li><li><strong>Anisogamy → unequal parental investment → mate choice asymmetry.</strong> The sex investing more (usually female) is choosier; the sex investing less (usually male) competes.</li><li><strong>Robbins-bait:</strong> sex-role reversal cases (pipefish, jacanas) where MALES invest more — there, females compete and males choose. The pattern follows investment, not anatomy.</li></ol>
<h4>How to spot the female</h4>
<ul><li>Bigger, fewer, costlier gametes → that sex is "female" by definition.</li><li>This is independent of chromosome system (XY in mammals, ZW in birds, haplodiploid in bees, environmental in turtles).</li></ul>`
    },
    "Twofold cost of sex": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sexual mothers pass only HALF as many gene copies per offspring as asexual mothers — yet sex is everywhere. Why? Robbins will absolutely test this paradox.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Cost = 2× — asexual mom transmits 100% of her genes per offspring; sexual mom transmits 50% (other half from male).</li><li>Maynard Smith (1971) formalized the calculation.</li><li>Sex must produce ≥2× the benefit to break even.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The central paradox of sex.</strong> Sex is widespread despite the 2× cost — the benefits must be huge.</li><li><strong>Memorize the four benefits</strong> that propose to outweigh: (1) recombination genetic novelty, (2) Muller's ratchet relief, (3) Red Queen against parasites, (4) sib-competition reduction.</li><li><strong>Robbins exam-trap:</strong> the cost is sometimes phrased as "cost of MALES" or "cost of SEX" — both refer to the same thing. Don't get tripped up by terminology.</li></ol>
<h4>The four proposed benefits</h4>
<ul><li>Genetic diversity from recombination → new allele combinations selection can act on.</li><li>Muller's ratchet relief → recombination purges accumulated deleterious mutations.</li><li>Red Queen → genetic novelty keeps hosts ahead of parasites.</li><li>Sib competition → genetically diverse offspring don't all compete for the same niche.</li></ul>`
    },
    "Muller's ratchet": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> In asexual lineages, deleterious mutations accumulate IRREVERSIBLY — the ratchet "clicks" but never unclicks. Robbins will test this as a major reason sex evolved.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Named after H. J. Muller — proposed in 1964.</li><li>Each "click" = the loss of the lowest-mutation class via drift; once gone, can't be regenerated without recombination.</li><li>Predicts asexual lineages should be evolutionarily young (most go extinct) — borne out: ~99% of asexual lineages are recent splits from sexual ancestors.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Mechanistic explanation for sex's persistence.</strong> Recombination can produce offspring with FEWER mutations than either parent — sex restores the mutation-free class.</li><li><strong>Predicts asexual extinction.</strong> Pure clones should accumulate mutational load and crash. This is observed in lab Drosophila clones and in the fossil record.</li><li><strong>Robbins exam-trap:</strong> bacteria can recombine via horizontal gene transfer, so they aren't fully subject to the ratchet. The ratchet specifically requires NO recombination at all.</li></ol>
<h4>Why irreversible</h4>
<ul><li>Drift can stochastically eliminate the mutation-free class even when fitness favors it.</li><li>Without recombination, you can't combine partial backups into a clean genome.</li><li>Reverse mutation rates are too low to restore the clean class.</li></ul>`
    },
    "Red Queen hypothesis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sex helps hosts STAY AHEAD of rapidly coevolving parasites — like the Queen in <em>Through the Looking-Glass</em>, you must keep running to stay in place. Robbins's favorite "why sex" hypothesis.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Named after Lewis Carroll's Red Queen: "It takes all the running you can do, to keep in the same place."</li><li>Best test system: New Zealand snail <em>Potamopyrgus antipodarum</em> — sexual forms in deep parasite-rich lakes; asexual forms in shallow parasite-poor ones.</li><li>Hamilton et al. proposed parasites as the sex-maintenance force.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Solves the "why sex" puzzle.</strong> Recombination produces novel allele combinations parasites haven't adapted to yet → frequency-dependent selection in hosts.</li><li><strong>Empirically tested in Lively's snails.</strong> Sex-asex distribution tracks parasite pressure — clean prediction confirmed.</li><li><strong>Predicts asexual lineages lose to parasites.</strong> Asexuals can't escape the parasite arms race fast enough — Red Queen extinction filter.</li></ol>
<h4>Why parasites uniquely drive this</h4>
<ul><li>Parasites have shorter generation times → can adapt faster than hosts.</li><li>Hosts need genetic novelty just to keep up — recombination provides it.</li><li>Without sex, common host genotypes get hammered by adapted parasites.</li></ul>`
    },
    "Anisogamy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Anisogamy = unequal gamete sizes — and IT defines male and female, not behavior or chromosomes. The female makes the costly egg; the male makes the cheap sperm. EVERYTHING downstream (mate choice, dimorphism, conflict) follows.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Sea urchins: ~10⁶ sperm per spawn vs ~10³ much larger eggs.</li><li>Definition: female = sex with larger gamete; male = sex with smaller gamete.</li><li>Evolved as a stable evolutionary endpoint of disruptive selection from isogamy.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Foundation of all sex differences.</strong> Robbins will hit you on this. Female "choosiness" and male "competition" both derive from gamete asymmetry.</li><li><strong>Definitional trap:</strong> "Female" is NOT defined by nurturing, chromosomes, or anatomy — it's defined by GAMETE SIZE. Get this right.</li><li><strong>Bateman's principle follows directly.</strong> Females limited by resources (large eggs); males limited by mates (cheap sperm).</li></ol>
<h4>Why anisogamy is stable</h4>
<ul><li>Disruptive selection on gamete size — middle-sized gametes are the worst (too costly to make many, too small to provision).</li><li>Bigger gametes survive better; smaller gametes find more mates. Stable extremes.</li><li>Once anisogamy locks in, asymmetric strategies (choosy female, competitive male) become evolutionarily stable.</li></ul>`
    },
    "Isogamy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Isogamy = equal-sized gametes; the ANCESTRAL state from which anisogamy evolved. Robbins might ask why anisogamy is favored and what came before.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Found in some algae (e.g., <em>Chlamydomonas</em>) and fungi.</li><li>Two mating types but no size difference between gametes — "+" and "-" not male and female.</li><li>The starting point for the evolution of anisogamy via disruptive selection.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Shows anisogamy isn't inevitable.</strong> Some lineages still have isogamy. Anisogamy evolved when conditions favored disruptive selection on gamete size.</li><li><strong>No "male" or "female" without anisogamy.</strong> Mating types in isogamous species are not sexes in the conventional sense.</li><li><strong>Robbins may use it as a contrast</strong> — anisogamy as derived; isogamy as ancestral.</li></ol>`
    },
    "Sexual selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Darwin's SECOND mechanism — selection for MATING success, not survival. Explains traits like peacock tails that REDUCE survival but boost mating.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Peacock train (<em>Pavo cristatus</em>): ~150 cm long when fanned; comprises ~150 elongated tail-coverts (eyespotted feathers).</li><li>Darwin developed sexual selection in <em>The Descent of Man</em> (1871).</li><li>Two flavors: INTRA (male-male combat) and INTER (mate choice, usually female).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Resolves Darwin's "peacock tail" puzzle.</strong> Why do showy ornaments evolve when they reduce survival? Because mating gain > survival loss.</li><li><strong>Sexual selection IS natural selection.</strong> Robbins exam-trap: don't say they're separate. They're related — same logic of differential reproduction.</li><li><strong>Net fitness = mating gain − survival cost.</strong> Sexually selected traits balance these forces.</li></ol>
<h4>The four hypotheses for female choice</h4>
<ul><li><strong>Direct benefits:</strong> female gets resources/territory/parental care from chosen male.</li><li><strong>Good genes:</strong> female chooses males whose ornaments signal heritable viability (handicap principle).</li><li><strong>Runaway (Fisher):</strong> arbitrary preference + heritable trait = self-amplifying loop.</li><li><strong>Sexy son:</strong> female gains by producing attractive sons that mate well next generation.</li></ul>`
    },
    "Intrasexual selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> INTRA = within-sex combat (usually male-male) → produces WEAPONS and large body size. Elk antlers, elephant seal bulks, dung beetle horns. Robbins will ask intra vs inter.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Elephant seal males weigh ~3-4× more than females; harem-holders monopolize ~50+ females.</li><li>Elk antlers can weigh ~18 kg, regrown every year.</li><li>Pattern: extreme dimorphism + weapons + winner monopolizes mating.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>One of the two sexual selection modes.</strong> Robbins will test the intra/inter distinction with example scenarios.</li><li><strong>Produces weapons.</strong> Antlers, horns, tusks, large body size — all intrasexual outcomes.</li><li><strong>Skewed mating success</strong> → strong selection on combat-related traits.</li></ol>
<h4>Intra vs inter mnemonic</h4>
<ul><li><strong>Intra = Inside-the-sex</strong> contest (male-male combat).</li><li><strong>Inter = Inter-sex</strong> choice (female chooses).</li><li>Intra → weapons; Inter → ornaments.</li></ul>`
    },
    "Intersexual selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> INTER = mate CHOICE by the other sex (typically female choice) → produces ORNAMENTS and elaborate displays. Peacock tails, bowerbird bowers, frog calls.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Bowerbird males build decorated structures (bowers) → no parental care, just bachelor pads.</li><li>Frog choruses: females discriminate calls within milliseconds of timing variation.</li><li>Pattern: ornament + display + female choice + male provides only sperm (in many species).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The other half of sexual selection.</strong> Robbins's standard intra/inter scenario question.</li><li><strong>Produces ornaments and signals.</strong> Showy color, songs, complex displays — intersexual outcomes.</li><li><strong>Honest signaling logic.</strong> Costly ornaments signal heritable quality (Zahavi handicap).</li></ol>`
    },
    "Sexual dimorphism": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sexual dimorphism = trait differences between males and females — usually a SIGNATURE of sexual selection. Bigger asymmetry = stronger sexual selection.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Lions: males ~50% heavier than females; have manes (intersexual ornament + intrasexual armor).</li><li>Elephant seals: males 3-4× heavier than females (extreme intrasexual selection).</li><li>Peacock train: males have it; females (peahens) don't (intersexual ornament).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins will use dimorphism as evidence of sexual selection.</strong> Identify whether the dimorphism is a weapon (intrasexual) or ornament (intersexual).</li><li><strong>Predicts mating system.</strong> High dimorphism → polygynous mating (one male monopolizes many females).</li><li><strong>Quantifies sexual selection intensity.</strong> Bigger sex difference = stronger selection on the dimorphic sex.</li></ol>`
    },
    "Sexual conflict": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Males and females have DIFFERENT optima — what helps a male's fitness can hurt a female's, and vice versa. Robbins likes the ducks-bedbugs examples.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Bedbugs: traumatic insemination (males stab females through abdomen) → females evolve thickened spermalege.</li><li>Ducks: corkscrew penis in drakes; counter-coiled vagina in females (rejection structure).</li><li>Drosophila: seminal fluid proteins shorten female lifespan but increase male paternity assurance.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Intra-species coevolution.</strong> Males and females are evolutionary antagonists despite being the same species. Key Robbins concept.</li><li><strong>Drives RAPID divergence in genitalia.</strong> Closely related species often have wildly different reproductive structures — sexual conflict explains why.</li><li><strong>Common signature:</strong> male coercion structures + female resistance morphology.</li></ol>
<h4>Classic examples</h4>
<ul><li>Bedbugs: traumatic insemination + spermalege resistance.</li><li>Ducks: spiral penises + counter-spiral vaginas.</li><li>Fruit flies: seminal fluid harms but boosts paternity.</li><li>Water striders: male anti-grasping structures + female resistance.</li></ul>`
    },
    "Sperm competition": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> When females mate with multiple males, sperm of different males COMPETE to fertilize — produces big testes, mating plugs, sperm removal. Testis size scales with mating system.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Chimpanzees (promiscuous): testes ~3% of body weight; many ejaculate matings per cycle.</li><li>Gorillas (single-male harems): testes ~0.05% of body weight; one male monopolizes.</li><li>Humans (intermediate): suggests moderate ancestral sperm competition.</li><li>Damselflies: penis has scoop to remove rival sperm before depositing own.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Comparative anatomy as evolutionary test.</strong> Testis size is a clean prediction of mating system. Robbins will use the chimp/gorilla contrast.</li><li><strong>Adaptations are diverse:</strong> big testes, long sperm, mating plugs, sperm-removal devices, copulation extension.</li><li><strong>Requires polyandry.</strong> Monogamous species have weak sperm competition.</li></ol>
<h4>Adaptations to sperm competition</h4>
<ul><li>Larger testes (more sperm = more lottery tickets).</li><li>Longer/faster sperm.</li><li>Mating plugs (block subsequent males).</li><li>Sperm-removal devices (damselfly scoop).</li><li>Extended copulation / mate-guarding behaviors.</li></ul>`
    },
    "Cryptic female choice": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Females bias paternity AFTER copulation through internal mechanisms — sperm storage, ejection, differential transport. "Cryptic" = invisible to outside observers. Major component of sexual selection in many taxa.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Some insects have multiple sperm-storage organs (spermathecae) — females selectively use sperm from one organ.</li><li>Female chickens can eject sperm from low-status males after copulation.</li><li>Detected via DNA paternity testing — pre- vs post-copulatory choice differ.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Female choice continues after mating.</strong> Pre-copulatory choice (mate selection) is visible; cryptic choice extends preference internally.</li><li><strong>Critical when females can't fully avoid mating with all males.</strong> Coercion, random encounters, sperm storage — cryptic choice is the post-hoc filter.</li><li><strong>Complicates measurement of male reproductive success.</strong> Mating ≠ paternity. Robbins may push you on this nuance.</li></ol>`
    },
    "Antagonistic coevolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Reciprocal evolutionary change driven by CONFLICTING interests — between species (predator-prey) OR within species (sexual conflict). Robbins will use this for both.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Bedbugs: traumatic insemination by males → thickened spermalege in females.</li><li>Ducks: corkscrew penises in males → counter-coiled vaginas in females.</li><li>Drives RAPID genital divergence even between closely-related species.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Same logic as inter-species arms race.</strong> Each side's adaptation imposes new selection on the other.</li><li><strong>Explains why genitalia diverge fastest.</strong> Sexual conflict accelerates evolutionary change in reproductive structures.</li><li><strong>Robbins may ask if antagonistic coevolution is "good" or "bad" for the species.</strong> Trick: it's neither — selection works on individuals, not species.</li></ol>`
    },
    "Twofold cost of sex (Maynard Smith)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Maynard Smith (1971) formalized the cost: a sexual female passes ½ her genes per offspring; an asexual female passes 100%. Sex must produce ≥2× the benefit to break even. Critical exam concept.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Cost = 2× — gene transmission per offspring is halved by sex.</li><li>Sex must overcome this with at least 2× the benefit.</li><li>Sometimes called "cost of males" — equivalent calculation.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The fundamental paradox of sex.</strong> Why is sex everywhere despite the cost? Robbins will absolutely test this.</li><li><strong>Memorize the four candidate benefits</strong>: recombination, Muller's ratchet, Red Queen, sib-competition.</li><li><strong>Maynard Smith's calculation</strong> — count gene copies in next generation, asexual vs sexual mom.</li></ol>
<h4>The math</h4>
<ul><li>Asexual mom: 2 daughters, each carries 100% of mom's genes → 2 × 1.0 = 2.0 gene-equivalents transmitted.</li><li>Sexual mom: 1 son + 1 daughter, each carries 50% of mom's genes → 2 × 0.5 = 1.0 gene-equivalents transmitted.</li><li>Asexual transmits 2× as many copies of mom's genes per offspring.</li></ul>`
    },
    "Fisher's runaway": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Arbitrary female preference + heritable male trait → sons inherit BOTH → preference and trait amplify together in a self-reinforcing positive-feedback loop. Even costly traits run away.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Proposed by R.A. Fisher (1930).</li><li>Classic example: peacock train (~150 cm long, very costly).</li><li>Loop ends when natural-selection cost balances sexual-selection benefit.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Self-reinforcing positive feedback.</strong> Once started (perhaps by drift or sensory bias), the loop accelerates exponentially.</li><li><strong>Doesn't require honest signaling.</strong> Unlike "good genes," runaway works for ARBITRARY preferences. Key Robbins distinction.</li><li><strong>Predicts trait values that REDUCE survival</strong> — peacock tails, exaggerated bird songs.</li></ol>
<h4>The four female-choice hypotheses</h4>
<ul><li><strong>Direct benefits:</strong> female gets resources from male.</li><li><strong>Good genes:</strong> ornament signals heritable quality (handicap principle, Zahavi).</li><li><strong>Runaway (Fisher):</strong> arbitrary self-amplifying loop.</li><li><strong>Sexy son:</strong> female gains by producing attractive sons.</li></ul>`
    },
    "Intrasexual vs intersexual selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> INTRA = combat within one sex (weapons); INTER = mate choice between sexes (ornaments). Robbins's standard exam scenario question.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Intrasexual: elephant seals (males 3-4× heavier), elk antlers (~18 kg), dung beetle horns.</li><li>Intersexual: peacock train (~150 cm), bowerbird bowers, frog choruses.</li><li>Both impose survival costs but in different ways.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The most likely L11 short-answer setup.</strong> Robbins will give you a scenario; you must identify intra or inter.</li><li><strong>Intra = weapons; Inter = ornaments.</strong> Memorize the asymmetric outcomes.</li><li><strong>Both reduce survival</strong> — intrasexual through injury risk and energy diversion; intersexual through predation and metabolic cost.</li></ol>
<h4>Mnemonic</h4>
<ul><li><strong>Intra = Inside-the-sex</strong> contest.</li><li><strong>Inter = Inter-sex</strong> choice.</li><li>Intra → weapons (antlers, horns, body size).</li><li>Inter → ornaments (color, song, displays).</li></ul>
<h4>Honest signaling (handicap principle)</h4>
<ul><li>Zahavi (1975): costly ornaments are honest precisely BECAUSE they reduce survival.</li><li>Only high-quality males can afford the cost — handicap = honest signal.</li><li>Intersexual ornaments often act as handicap signals.</li></ul>`
    },
    "Sexual conflict — when do interests diverge?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sexual conflict = males and females have OPPOSING optima. Male's optimum (more matings, paternity assurance) reduces female fitness (cost of remating, harassment).</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Bedbugs: traumatic insemination + spermalege resistance.</li><li>Ducks: corkscrew penises + counter-coiled vaginas.</li><li>Fruit flies: seminal fluid proteins shorten female lifespan.</li><li>Water striders: anti-grasping male structures + female resistance.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Antagonistic coevolution WITHIN species.</strong> Males and females are evolutionary opponents despite sharing a species.</li><li><strong>Drives rapid genital divergence.</strong> Closely related species often have wildly different reproductive morphologies.</li><li><strong>Common signature:</strong> male coercion structure + female counter-structure.</li></ol>
<h4>Why interests diverge</h4>
<ul><li>Anisogamy → asymmetric reproductive investment.</li><li>Males benefit from MORE matings; females typically benefit from fewer with high-quality partners.</li><li>Each sex's optimum hurts the other's fitness → arms race within species.</li></ul>`
    },
    "Sperm competition — male anatomical responses": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Testis size scales with sperm-competition intensity — chimps (promiscuous) have huge testes; gorillas (harem) have tiny ones; humans are intermediate. Comparative anatomy is the test.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Chimpanzees: testes ~3% of body weight (extreme sperm competition).</li><li>Gorillas: testes ~0.05% of body weight (single-male harems, no competition).</li><li>Humans: intermediate (~0.08%) → moderate ancestral sperm competition.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Beautiful test of evolutionary prediction.</strong> Mating system → testis size — predicts and explains.</li><li><strong>Multiple anatomical adaptations</strong>: big testes, long sperm, mating plugs, removal devices, copulation extension.</li><li><strong>Robbins will use the chimp/gorilla contrast.</strong> Memorize the numbers.</li></ol>
<h4>Adaptations beyond testis size</h4>
<ul><li>Sperm length and speed (faster sperm win).</li><li>Mating plugs (block subsequent males).</li><li>Sperm-removal scoops (damselflies).</li><li>Extended copulation / mate-guarding behaviors.</li></ul>`
    },
    "Cryptic female choice — why it matters": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Cryptic female choice = post-copulatory paternity bias by females through reproductive-tract physiology. Extends preference INTERNALLY when external choice is incomplete.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Multiple spermathecae in some insects → female can selectively fertilize from preferred organ.</li><li>Female chickens can eject sperm from low-status males after copulation.</li><li>DNA paternity testing reveals the discrepancy between mating and fertilization.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Female choice extends past mating.</strong> Pre-copulatory choice = visible; cryptic choice = internal post-hoc filter.</li><li><strong>Critical when females can't fully avoid all matings.</strong> Coercion, random encounters, stored sperm — cryptic choice handles what pre-copulatory choice can't.</li><li><strong>Robbins may push on the consequence:</strong> male reproductive success ≠ male mating success in many taxa.</li></ol>`
    }
  });

  window.addCardPatches('L12', {
    "Life history": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Life history = the SCHEDULE of birth, growth, reproduction, and death — selection can't optimize all at once, so trade-offs force compromises. Foundation of L12.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Key axes: age at maturity, fecundity, longevity, reproductive timing.</li><li>Selection maximizes LIFETIME reproductive success, not any single component.</li><li>Continuous variables, not strict r/K dichotomy.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins exam-trap:</strong> "What does selection maximize?" Answer is LIFETIME reproductive success — NOT longevity, NOT fecundity alone.</li><li><strong>Trade-offs constrain everything.</strong> Selection works WITHIN trade-offs, not to escape them.</li><li><strong>All later L12 cards are special cases.</strong> Senescence, r/K, age at maturity — all life-history phenomena.</li></ol>`
    },
    "Trade-off": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Trade-offs are PHYSIOLOGICAL — they're not optional. Selection navigates them, never escapes them. Robbins will hit you on this.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Currencies: ENERGY (calories), TIME (development vs reproduction), MORTALITY RISK (current vs future).</li><li>Classic examples: growth vs reproduction, current vs future reproduction, offspring number vs size.</li><li>Trade-offs arise from SHARED LIMITED RESOURCES — one pool can't fund two demands.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Trade-offs are the engine of life-history evolution.</strong> Without them, every trait would maximize independently.</li><li><strong>Robbins exam-trap:</strong> "Why don't organisms maximize lifespan?" Because doing so would reduce reproduction. Trade-off is mandatory.</li><li><strong>Selection optimizes WITHIN trade-offs.</strong> Cannot escape the constraint, only navigate it.</li></ol>
<h4>Major trade-off currencies</h4>
<ul><li>Energy: calories spent on growth vs reproduction vs maintenance.</li><li>Time: time to maturity vs reproductive lifespan.</li><li>Mortality risk: high current effort → less future survival.</li></ul>`
    },
    "Reproductive effort": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Reproductive effort = fraction of resources allocated to current reproduction vs survival/future reproduction. Semelparity (one shot, then die) vs iteroparity (repeated breeding).</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Semelparous: Pacific salmon (5 species, all die after spawning), agave (lives 10-30 yrs, blooms once, dies), some bamboos, octopus.</li><li>Iteroparous: humans, perch, most mammals, perennial plants.</li><li>Salmon expend ~60-70% of body mass during spawning migration.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins will contrast salmon vs perch.</strong> Why does each work? Different extrinsic mortality regimes favor different optima.</li><li><strong>Context-dependent strategy.</strong> Semelparity wins when future survival is unlikely (high adult mortality, costly migration). Iteroparity wins when adult survival is high.</li><li><strong>Big-bang vs steady-state reproduction.</strong> Both are stable evolved strategies — neither is "better".</li></ol>
<h4>Semelparity vs iteroparity examples</h4>
<ul><li>Semelparous: Pacific salmon, agave, octopus, mayflies.</li><li>Iteroparous: most fish (perch, trout), birds, mammals, perennial plants, oaks.</li><li>Salmon strategy: massive reproduction → don't bank on second chance (high mortality on return migration).</li></ul>`
    },
    "Extrinsic mortality": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Extrinsic mortality (predation, disease, accident) is the SINGLE most important determinant of life-history strategy. High predation → fast life; low predation → slow life. Robbins will hit you on this principle.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>HIGH extrinsic mortality → early maturity, many offspring, short lifespan ("live fast, die young").</li><li>LOW extrinsic mortality → delayed maturity, fewer/larger offspring, longer lifespan.</li><li>Mainland opossums (predator-rich) mature ~2 years earlier than island opossums (predator-free).</li><li>Reznick's guppy experiments: life-history shifts evolve in tens of generations.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The master variable in life-history evolution.</strong> Robbins will use it to explain everything from salmon to elephants.</li><li><strong>Predicts island vulnerability.</strong> Slow island species (Galápagos tortoises, dodos) collapse when predators arrive — selection can't reverse fast enough.</li><li><strong>Affects optimal age at maturity</strong> even if intrinsic survival is high.</li></ol>
<h4>Classic comparisons</h4>
<ul><li>Mainland vs island opossums: predators → faster life history.</li><li>Trinidadian guppies (high vs low predation pools): high-pred = early maturity, many offspring; low-pred = late maturity, few offspring.</li><li>Mice (r-selected) vs elephants (K-selected): high vs low predation/mortality regimes.</li></ul>`
    },
    "Intrinsic mortality / senescence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Intrinsic mortality = aging from internal causes — physiological decline. Why we age even when external dangers are eliminated. Robbins will pair this with extrinsic mortality.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Hayflick limit: human cells divide ~50-60 times before senescing in culture.</li><li>Telomere shortening: cells lose ~50-200 base pairs per division.</li><li>Naked mole rats: live ~30+ years (most rodents live 2-3) — exhibit "negligible senescence".</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Even in zero-extrinsic-mortality conditions, organisms age.</strong> Why? Because selection is weaker at older ages — three theories of senescence explain it.</li><li><strong>Distinguishes "death from outside" vs "death from inside".</strong> Both contribute to total mortality.</li><li><strong>Naked mole rats are the exception</strong> — Robbins's favorite "weird" example.</li></ol>`
    },
    "Senescence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Senescence = age-related decline in survival and reproduction. Selection can't prevent it because selection's STRENGTH DECLINES with age. Three theories (MAD: Mutation accumulation, Antagonistic pleiotropy, Disposable soma).</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Hayflick limit: ~50-60 divisions for human fibroblasts in culture.</li><li>Telomeres shorten ~50-200 bp per division.</li><li>Naked mole rats: ~30 yr lifespan (most rodents 2-3 yrs) — negligible senescence.</li><li>Three theories: Mutation accumulation (Medawar), Antagonistic pleiotropy (Williams), Disposable soma (Kirkwood).</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Why we age — central evolutionary question.</strong> Robbins will absolutely test the three theories.</li><li><strong>Selection strength declines with age</strong> because few individuals reach old age (extrinsic mortality reduces the population at older ages).</li><li><strong>All three theories follow from the same logic:</strong> selection can't see what happens after most individuals are dead.</li></ol>
<h4>The three theories (MAD)</h4>
<ul><li><strong>M</strong>utation accumulation (Medawar): late-acting deleterious mutations escape selection.</li><li><strong>A</strong>ntagonistic pleiotropy (Williams): one gene benefits early, harms late — selection net-favors early benefit.</li><li><strong>D</strong>isposable soma (Kirkwood): trade-off between reproduction and somatic maintenance.</li></ul>`
    },
    "Mutation accumulation theory": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Medawar's theory: late-acting deleterious mutations ESCAPE selection because they affect post-reproductive individuals. Mutations accumulate → senescence. Many-gene story.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Proposed by Peter Medawar (1952).</li><li>Selection strength on mutations declines to ~0 after reproductive years.</li><li>Classic example: Huntington's disease — late onset (typically 30-50), so dominant lethal allele isn't purged.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>One of three senescence theories.</strong> Robbins will test all three; this is the "many late-acting mutations" version.</li><li><strong>Predicts late-onset diseases that should never have evolved</strong> if selection saw them. They evolved because selection didn't.</li><li><strong>Distinct from antagonistic pleiotropy:</strong> mutation accumulation = MANY genes, each only late-acting; AP = ONE gene with two effects.</li></ol>
<h4>Mutation accumulation vs antagonistic pleiotropy</h4>
<ul><li><strong>Mutation accumulation:</strong> many genes, each has late-life cost only. Selection blind to late effects.</li><li><strong>Antagonistic pleiotropy:</strong> one gene, two effects (early benefit + late cost). Selection net-favors early benefit.</li></ul>`
    },
    "Antagonistic pleiotropy": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Williams's theory: ONE gene with TWO effects — early beneficial, late harmful. Selection favors it on net because early-life effects on reproduction outweigh late-life costs. Single-gene story.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Proposed by George C. Williams (1957).</li><li>Classic example: testosterone-related genes (boost early reproduction; later prostate/cardiovascular costs).</li><li>BRCA1/2 hypothesized similarly (early reproductive benefit; later cancer risk) — though this is debated.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The "one-gene-two-effects" version of senescence.</strong> Robbins will test this vs mutation accumulation.</li><li><strong>Selection actively FAVORS the gene</strong> — not blind to it (unlike mutation accumulation).</li><li><strong>Predicts cellular trade-offs</strong> like the link between cancer suppression (TP53) and aging.</li></ol>
<h4>Single gene vs many genes (key Robbins distinction)</h4>
<ul><li><strong>Antagonistic pleiotropy:</strong> ONE gene, beneficial early + harmful late. Selection ACTIVELY favors.</li><li><strong>Mutation accumulation:</strong> MANY genes, late-acting only. Selection BLIND.</li></ul>`
    },
    "Disposable soma theory": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Kirkwood's theory: organisms allocate finite resources between SOMA (body upkeep, longevity) and REPRODUCTION (offspring). Investment in soma reduces fecundity. Resource trade-off explanation.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Proposed by Tom Kirkwood (1977).</li><li>Daphnia under caloric restriction live ~30% longer but produce fewer offspring.</li><li>Hayflick limit: cells stop dividing after ~50-60 divisions — disposable cellular machinery.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The "resource trade-off" version of senescence.</strong> Different framing from mutation accumulation and pleiotropy.</li><li><strong>Predicts caloric restriction effects.</strong> Less reproduction → more soma maintenance → longer life. Tested in worms, flies, mice.</li><li><strong>Soma is "disposable"</strong> — body is not built to last forever, only long enough to reproduce.</li></ol>
<h4>The three senescence theories — non-exclusive</h4>
<ul><li>All can operate simultaneously.</li><li>Mutation accumulation: late-life mutations escape selection.</li><li>Antagonistic pleiotropy: early benefit / late cost trade-off in single genes.</li><li>Disposable soma: resource allocation between maintenance and reproduction.</li></ul>`
    },
    "Age at maturity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Age at maturity = when reproduction starts. Earlier = reproduce sooner but at smaller size; later = bigger and better-provisioned but more risk of dying first. Robbins will test the trade-off.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Female elephants mature at 12-15 years; one calf every 4-5 years.</li><li>Mice mature at ~6 weeks; produce litters every ~3 weeks.</li><li>Optimal age at maturity depends on growth rate, mortality risk, and reproductive payoff.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Central life-history decision.</strong> Robbins's classic short answer: predict age at maturity given mortality regime.</li><li><strong>High extrinsic mortality favors early maturity.</strong> Don't wait — you might die.</li><li><strong>Low extrinsic mortality favors delayed maturity.</strong> Wait, grow bigger, invest more per offspring.</li></ol>`
    },
    "r/K selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> r-selected = many small offspring, fast life; K-selected = few large offspring, slow life. Useful HEURISTIC but not strict — Robbins will mention it's somewhat dated.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>r-selected: mice, weeds, most insects, dandelions.</li><li>K-selected: elephants, oaks, humans, whales.</li><li>r refers to intrinsic growth rate; K refers to carrying capacity.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classic framework Robbins will reference.</strong> Even though dated, it's still on every exam.</li><li><strong>Predicts associated traits.</strong> r → many small offspring + early maturity + short life. K → few large offspring + delayed maturity + long life + parental care.</li><li><strong>Modern theory uses continuous variables.</strong> Many species are intermediate.</li></ol>
<h4>r vs K mnemonic</h4>
<ul><li><strong>r = Rapid</strong> (many small, fast life).</li><li><strong>K = Carrying-capacity</strong> (few big, slow life).</li><li>Robbins exam-trap: don't say it's a strict dichotomy. It's a continuum.</li></ul>`
    },
    "Cooperative breeding": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Cooperative breeding = adult helpers (often offspring from previous broods) assist parents in raising young. Florida scrub jays, Seychelles warblers, naked mole rats. Robbins's classic kin-selection example.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Naked mole rats: colonies up to ~300 individuals; one breeding queen + sterile workers.</li><li>Seychelles warblers: ~250-360 territorial pairs on Cousin Island.</li><li>Florida scrub jays: helpers stay 1-3 years before dispersing.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Helping isn't pure altruism.</strong> Helpers gain inclusive fitness through kin AND may inherit territories. Hamilton's rule applies.</li><li><strong>Robbins's standard kin-selection scenario.</strong> "Why help instead of disperse?" Answer: when ecological constraints + relatedness make helping rB > C.</li><li><strong>Naked mole rats = eusocial mammal exception.</strong> Like ants/bees, but in a vertebrate.</li></ol>
<h4>Why help instead of disperse?</h4>
<ul><li>Ecological constraint: high-quality territories saturated; dispersal options poor.</li><li>Kin selection: helping siblings (r=0.5) raises indirect fitness.</li><li>Future direct fitness: helpers may inherit the territory.</li><li>All three forces can operate simultaneously.</li></ul>`
    },
    "Sex-biased dispersal": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Sex-biased dispersal = one sex leaves natal site more than the other. Birds: typically female-biased dispersal. Mammals: typically male-biased. Seychelles warblers are female-philopatric.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Seychelles warblers: FEMALES STAY (philopatric) on high-quality territories as helpers; MALES DISPERSE.</li><li>Most birds: females disperse more than males (reverse of mammal pattern).</li><li>Most mammals: males disperse more than females.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins exam-trap:</strong> Direction of bias in Seychelles warblers is FEMALE-PHILOPATRIC (females stay). Don't get this backwards.</li><li><strong>Driven by territory value + kin structure.</strong> Whichever sex gains more from staying, stays.</li><li><strong>Reduces inbreeding</strong> — sex-biased dispersal is one mechanism for outbreeding.</li></ol>
<h4>Seychelles warblers — direction of bias</h4>
<ul><li>FEMALES: stay on natal territory, often as helpers (especially on high-quality territories).</li><li>MALES: disperse to seek breeding opportunities elsewhere.</li><li>Direction follows territory value: high-quality territories → females stay (inheritance + kin selection).</li></ul>`
    },
    "Three theories of senescence": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> MAD = Mutation accumulation + Antagonistic pleiotropy + Disposable soma. All three explain why we age, none mutually exclusive. Robbins will hit all three.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Mutation accumulation (Medawar 1952): MANY genes, late-acting, escape selection.</li><li>Antagonistic pleiotropy (Williams 1957): ONE gene, beneficial early + harmful late.</li><li>Disposable soma (Kirkwood 1977): resource trade-off between maintenance and reproduction.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>The big senescence question.</strong> Robbins will absolutely ask "name and distinguish at least two theories of senescence".</li><li><strong>All three are non-exclusive.</strong> Probably all contribute. Don't pick one as "the" answer.</li><li><strong>Single-gene vs many-gene distinction</strong> separates AP from MA. Resource trade-off separates DS from both.</li></ol>
<h4>The MAD mnemonic</h4>
<ul><li><strong>M</strong>utation accumulation: late-life mutations escape selection (many genes).</li><li><strong>A</strong>ntagonistic pleiotropy: one gene, two effects at different ages.</li><li><strong>D</strong>isposable soma: trade-off between body maintenance and reproduction.</li></ul>
<h4>Classic examples</h4>
<ul><li>Huntington's: mutation accumulation (late-life dominant lethal escapes selection).</li><li>Testosterone effects: antagonistic pleiotropy (early reproduction boost, late cancer risk).</li><li>Caloric restriction extending lifespan: disposable soma (less reproduction → more maintenance).</li></ul>`
    },
    "Extrinsic mortality → life history": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> HIGH extrinsic mortality → FAST life (early maturity, many offspring, short lifespan). LOW extrinsic mortality → SLOW life. Robbins's master variable for predicting life history.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Galápagos tortoises: ~100 yr lifespan (no native predators).</li><li>Mainland opossums mature ~2 years earlier than island opossums (predator effect).</li><li>Reznick's guppy experiments: life-history shifts evolved in 4-11 generations.</li><li>Kakapo (heaviest parrot, flightless, predator-free island): nearly extinct after rats and cats arrived.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Predicts island vulnerability to introduced predators.</strong> Slow island species (kakapo, dodo, Galápagos tortoise) collapse when predators arrive.</li><li><strong>Selection can't reverse fast enough.</strong> Slow life histories evolve over many generations; introduced predators arrive in days.</li><li><strong>Robbins's signature life-history exam question.</strong> Given mortality regime, predict life history.</li></ol>
<h4>Predator-free islands → slow life history</h4>
<ul><li>Galápagos tortoises: ~100 yr lifespan.</li><li>Kakapo: heaviest parrot, flightless, slow-breeding.</li><li>Dodo: extinct shortly after humans + rats arrived in Mauritius.</li><li>All vulnerable to introduced predators because slow strategy can't reverse fast.</li></ul>`
    },
    "r vs K selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> r-selected = unstable/empty environments (many small offspring, fast life); K-selected = saturated/competitive environments (few big offspring, slow life). Robbins's classic life-history dichotomy.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>r-selected: mice, weeds, most insects.</li><li>K-selected: elephants, oaks, humans, whales.</li><li>r = intrinsic rate of increase (Malthusian growth).</li><li>K = environmental carrying capacity.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classical life-history framework.</strong> Robbins will reference even if it's somewhat dated.</li><li><strong>Predicts trait suite.</strong> r → high fecundity + early maturity + short life. K → low fecundity + delayed maturity + long life + parental care.</li><li><strong>Density and stability of resources predict position on continuum.</strong> Variable environment → r; stable, saturated → K.</li></ol>
<h4>r vs K mnemonic</h4>
<ul><li><strong>r = Rapid</strong> (many small offspring).</li><li><strong>K = Carrying-capacity</strong> (few big offspring).</li><li>Robbins exam-trap: it's a CONTINUUM, not a strict dichotomy. Many species are intermediate.</li></ul>`
    },
    "Life-history trade-offs — what's the currency?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Trade-offs are inverse fitness relationships mediated by SHARED LIMITED RESOURCES. Currencies: ENERGY, TIME, MORTALITY RISK. One pool can't fund two demands. Robbins's key conceptual frame.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Three currencies: energy (calories), time (development vs reproduction), mortality risk (current vs future).</li><li>Salmon expend ~60-70% of body mass during spawning → semelparity is forced by energy depletion.</li><li>Selection maximizes lifetime reproductive success across all trade-offs.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Currency is the key concept.</strong> Robbins exam-trap: don't just say "trade-off" — name the currency (energy/time/risk).</li><li><strong>Selection navigates, doesn't escape.</strong> Trade-offs are physiological constraints.</li><li><strong>Salmon vs albatross both work</strong> because they balance the SAME currency differently for different mortality regimes.</li></ol>
<h4>Salmon vs albatross — same trade-off, different optima</h4>
<ul><li>Salmon: high mortality during return migration → don't bank on second chance → semelparity (big-bang reproduction).</li><li>Albatross: low adult mortality at sea → slow steady reproduction across decades pays off.</li><li>Both maximize lifetime reproduction given their mortality regime.</li></ul>`
    },
    "Offspring number vs size (bet-hedging vs provisioning)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Fixed reproductive budget can be split MANY-SMALL (bet-hedging) or FEW-LARGE (provisioning). Optimum depends on offspring survival curve as a function of size. Robbins exam classic.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Trout: thousands of small unprotected eggs — bet-hedging in unpredictable environment.</li><li>Sharks: few large eggs (some live-born after gestation) — heavy per-offspring investment.</li><li>The trade-off: fixed total resources, choose between many small or few large.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Classical life-history trade-off.</strong> Robbins will use it as a short-answer.</li><li><strong>Bet-hedging vs provisioning logic.</strong> Variance vs mean optimization in offspring fitness.</li><li><strong>Predicts optimal strategy from environment.</strong> Unpredictable / high juvenile mortality → many small. Stable / competitive → few large.</li></ol>
<h4>When does each pay off?</h4>
<ul><li>MANY-SMALL pays off when: juvenile mortality is high and unpredictable; survival curve is FLAT with size; environment is variable.</li><li>FEW-LARGE pays off when: juvenile competition is intense; survival curve is STEEP with size; environment is stable.</li><li>Robbins: predict from a species's environment.</li></ul>`
    },
    "Seychelles warblers — why help, not disperse?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Seychelles warblers = COOPERATIVE breeders on Cousin Island; offspring (especially daughters on high-quality territories) STAY and help instead of dispersing. Two forces: kin selection + ecological constraint.</p>
<h4>The numbers (memorize these)</h4>
<ul><li>Cousin Island: ~250-360 territorial pairs.</li><li>Female-biased philopatry (especially on high-quality territories).</li><li>Helpers raise siblings (r = 0.5) AND may inherit the territory.</li></ul>
<h4>Why it's important</h4>
<ol><li><strong>Robbins's classic cooperative breeding case.</strong> Why help when you could breed independently?</li><li><strong>Two forces operate together:</strong> KIN SELECTION (siblings r=0.5) + ECOLOGICAL CONSTRAINT (saturated good territories make dispersal worse than waiting).</li><li><strong>Direction of bias = FEMALE-PHILOPATRIC.</strong> Robbins exam-trap: don't reverse it.</li></ol>
<h4>Why female-philopatric (not male)?</h4>
<ul><li>High-quality territories saturate; dispersal options for daughters are poor.</li><li>Hamilton's rule: rB > C — staying gives high inclusive fitness, low cost.</li><li>Helpers may inherit the territory later (direct fitness payoff too).</li><li>Two forces same direction → robust female philopatry.</li></ul>`
    }
  });
})();
