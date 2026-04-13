#!/usr/bin/env node
/**
 * Build script: transforms evolution data.json → single-file study.html
 * using the monochrome design system template.
 */
const fs = require('fs');
const data = require('./data.json');

// ── Lecture → Chapter mapping ────────────────────────────────────
function getChapter(id) {
  if (id.startsWith('lec1')) return 'Lec 1-2';
  if (id.startsWith('lec2')) return 'Lec 1-2';
  if (id.startsWith('lec3')) return 'Lec 3';
  if (id.startsWith('lec4')) return 'Lec 4';
  if (id.startsWith('lec56')) return 'Lec 5-6';
  if (id.startsWith('lec7')) return 'Lec 7';
  if (id.startsWith('lec8')) return 'Lec 8';
  if (id.startsWith('lec9')) return 'Lec 9';
  if (id.startsWith('lec1011')) return 'Lec 10-11';
  if (id.startsWith('lec12')) return 'Lec 12';
  if (id.startsWith('lec13')) return 'Lec 13';
  if (id.startsWith('lec14')) return 'Lec 14';
  if (id.startsWith('lec15')) return 'Lec 15';
  if (id.startsWith('ch13')) return 'Speciation';
  return 'Applied';
}

// ── Parse v2 flashcard back into technical + ELI5 ────────────────
function parseBack(back) {
  if (!back) return { technical: '', eli5: '' };
  const eli5Match = back.match(/\*\*ELI5:\*\*\s*([\s\S]*)/i);
  const techMatch = back.match(/\*\*TECHNICAL:\*\*\s*([\s\S]*?)(?=\*\*ELI5:|$)/i);
  let technical = techMatch ? techMatch[1].trim() : back.split('\n\n')[0].replace(/\*\*/g, '').trim();
  let eli5 = eli5Match ? eli5Match[1].trim() : '';
  // Strip markdown bold
  technical = technical.replace(/\*\*/g, '');
  eli5 = eli5.replace(/\*\*/g, '');
  return { technical, eli5 };
}

// ── 1. FLASHCARDS ────────────────────────────────────────────────
const FLASHCARDS = [];
data.nodes.forEach(node => {
  const ch = getChapter(node.id);
  (node.v2?.flashcards || []).forEach(fc => {
    const { technical, eli5 } = parseBack(fc.back);
    if (fc.front && technical) {
      FLASHCARDS.push({ q: fc.front, a: technical, ch, eli5: eli5 || 'Think of it as a key concept you need to connect to the bigger picture.' });
    }
  });
});
console.log(`Flashcards: ${FLASHCARDS.length}`);

// ── 2. QUIZ ──────────────────────────────────────────────────────
const QUIZ = [];
data.nodes.forEach(node => {
  const coreSection = node.popup?.sections?.find(s => s.label === 'CORE CONCEPT');
  const coreBrief = coreSection ? coreSection.body.split('.').slice(0, 2).join('.') + '.' : '';
  (node.quiz || []).forEach(q => {
    // Shuffle correct answer into distractors
    const allOpts = [...q.distractors];
    const insertIdx = Math.floor(Math.random() * 4);
    allOpts.splice(insertIdx, 0, q.correct);
    const explain = `Correct: ${q.correct}. ${coreBrief}`.substring(0, 400);
    QUIZ.push({ q: q.question, opts: allOpts.slice(0, 4), ans: insertIdx, explain });
  });
});
console.log(`Quiz: ${QUIZ.length}`);

// ── 3. COMPARES ──────────────────────────────────────────────────
const COMPARES = [
  {
    title: "Natural Selection vs Genetic Drift",
    left: "Natural Selection", right: "Genetic Drift",
    rows: [
      ["Mechanism", "Differential survival/reproduction based on fitness", "Random sampling of alleles each generation"],
      ["Direction", "Non-random — favors adaptive alleles", "Random — no consistent direction"],
      ["Population size effect", "Works in any population size", "Strongest in small populations"],
      ["Outcome", "Adaptation — improved fit to environment", "Fixation/loss of alleles by chance"],
      ["Genetic variation", "Reduces variation at selected locus", "Reduces variation randomly"],
      ["Predictability", "Somewhat predictable if environment known", "Unpredictable — stochastic process"]
    ]
  },
  {
    title: "Allopatric vs Sympatric Speciation",
    left: "Allopatric", right: "Sympatric",
    rows: [
      ["Geographic barrier", "Yes — physical separation required", "No — occurs within same range"],
      ["Frequency in nature", "Most common mode of speciation", "Rarer, more controversial"],
      ["Key driver", "Geographic isolation → independent evolution", "Disruptive selection or polyploidy"],
      ["Gene flow", "Completely interrupted by barrier", "Must be overcome despite proximity"],
      ["Classic example", "Grand Canyon squirrels (Kaibab vs Abert)", "Cichlid fishes in African rift lakes"],
      ["Evidence required", "Show barrier preceded divergence", "Show reproductive isolation without barrier"]
    ]
  },
  {
    title: "Müllerian vs Batesian Mimicry",
    left: "Müllerian", right: "Batesian",
    rows: [
      ["Model", "Both species are toxic/harmful", "Only model is toxic; mimic is harmless"],
      ["Benefit", "Shared warning signal — predators learn faster", "Mimic gains protection without cost"],
      ["Relationship", "Mutualistic — both benefit", "Parasitic — mimic exploits model's signal"],
      ["Frequency dependence", "Positive — more mimics = better for all", "Negative — too many mimics dilute signal"],
      ["Example", "Monarch + Viceroy (both toxic)", "Harmless hoverflies mimicking wasps"],
      ["Selection pressure", "Convergence toward shared pattern", "Mimic evolves toward model appearance"]
    ]
  },
  {
    title: "Directional vs Stabilizing vs Disruptive Selection",
    left: "Directional", right: "Stabilizing / Disruptive",
    rows: [
      ["Favored phenotype", "One extreme end of distribution", "Stabilizing: average / Disruptive: both extremes"],
      ["Effect on mean", "Shifts mean toward favored extreme", "Stabilizing: no shift / Disruptive: no shift or split"],
      ["Effect on variance", "Reduces variance, shifts distribution", "Stabilizing: reduces / Disruptive: increases variance"],
      ["When it occurs", "Environmental change, new selection pressure", "Stabilizing: consistent env / Disruptive: multiple niches"],
      ["Example", "Antibiotic resistance increasing in bacteria", "Stabilizing: human birth weight / Disruptive: finch beaks"],
      ["Long-term outcome", "Trait fixation at one extreme", "Stabilizing: optimum / Disruptive: possible speciation"]
    ]
  },
  {
    title: "Homologous vs Analogous Structures",
    left: "Homologous", right: "Analogous",
    rows: [
      ["Origin", "Shared common ancestor", "Independent evolution (convergence)"],
      ["Structural similarity", "Same underlying structure, different function", "Different structure, similar function"],
      ["DNA evidence", "Shared genetic sequences", "Different genetic basis"],
      ["Phylogenetic signal", "Indicates shared ancestry (synapomorphy)", "Does NOT indicate close relatedness"],
      ["Example", "Bat wing, whale flipper, human arm", "Bird wing vs insect wing"],
      ["Term in cladistics", "Synapomorphy (shared derived character)", "Homoplasy"]
    ]
  },
  {
    title: "Prezygotic vs Postzygotic Barriers",
    left: "Prezygotic", right: "Postzygotic",
    rows: [
      ["When they act", "BEFORE fertilization", "AFTER fertilization"],
      ["Energy cost", "Low — prevents wasted reproductive effort", "High — gametes/energy already invested"],
      ["Types", "Habitat, temporal, behavioral, mechanical, gametic", "Hybrid inviability, infertility, breakdown"],
      ["Reinforcement", "Strengthened by natural selection", "Less directly reinforced"],
      ["Example", "Firefly flash pattern differences", "Mule (horse × donkey) — sterile hybrid"],
      ["Evolution", "Evolve faster — selected against wasted mating", "Evolve as byproduct of genetic divergence"]
    ]
  },
  {
    title: "Biological vs Phylogenetic Species Concept",
    left: "Biological (Mayr)", right: "Phylogenetic (Cracraft)",
    rows: [
      ["Definition", "Reproductively isolated group", "Smallest diagnosable monophyletic group"],
      ["Criterion", "Can interbreed, produce fertile offspring", "Share unique synapomorphies"],
      ["Strengths", "Directly tests gene flow", "Works for fossils, asexuals, any organism"],
      ["Weaknesses", "Fails for asexuals, fossils, ring species", "May over-split (every population = species)"],
      ["Hybridization", "Hybridizers = same species (problematic)", "Irrelevant if monophyly maintained"],
      ["Most useful for", "Sexually reproducing, living populations", "All organisms including fossils"]
    ]
  },
  {
    title: "r-Selected vs K-Selected Life Histories",
    left: "r-Selected", right: "K-Selected",
    rows: [
      ["Offspring number", "Many offspring per event", "Few offspring per event"],
      ["Parental care", "Little to none", "Extensive parental investment"],
      ["Body size", "Typically small", "Typically large"],
      ["Lifespan", "Short-lived", "Long-lived"],
      ["Development speed", "Fast maturation", "Slow maturation"],
      ["Environment", "Unpredictable, high mortality", "Stable, competitive environments"],
      ["Example", "Insects, bacteria, dandelions", "Elephants, whales, humans"]
    ]
  },
  {
    title: "Adaptation vs Exaptation",
    left: "Adaptation", right: "Exaptation",
    rows: [
      ["Definition", "Trait shaped BY natural selection FOR current function", "Trait co-opted for NEW function different from original"],
      ["Selection history", "Selected for current use", "Originally selected for something else (or neutral)"],
      ["Example", "Shark streamlining for swimming", "Feathers: evolved for insulation, co-opted for flight"],
      ["Identifying it", "Function matches apparent design", "Function differs from ancestral use"],
      ["Importance", "Shows how selection sculpts traits", "Shows evolution tinkers with existing parts"],
      ["Gould's term", "—", "Coined 'exaptation' (Gould & Vrba 1982)"]
    ]
  },
  {
    title: "Sexual Selection vs Natural Selection",
    left: "Sexual Selection", right: "Natural Selection (Survival)",
    rows: [
      ["Selective agent", "Mate choice or mating competition", "Environment, predators, resources"],
      ["What is maximized", "Mating success", "Survival to reproduction"],
      ["Can oppose viability?", "Yes — costly ornaments reduce survival", "No — by definition improves survival"],
      ["Sexual dimorphism", "Often creates dramatic sex differences", "Usually affects both sexes similarly"],
      ["Types", "Intersexual (mate choice) + intrasexual (combat)", "Directional, stabilizing, disruptive"],
      ["Example", "Peacock tail, deer antlers", "Camouflage, antibiotic resistance"]
    ]
  },
  {
    title: "Gene Flow vs Genetic Drift",
    left: "Gene Flow", right: "Genetic Drift",
    rows: [
      ["Mechanism", "Migration of alleles between populations", "Random sampling error in allele transmission"],
      ["Effect on variation", "Homogenizes populations (reduces between-pop differences)", "Reduces within-population variation"],
      ["Population size", "Independent of size", "Strongest in small populations"],
      ["Direction", "Moves alleles from source to recipient", "Random — no consistent direction"],
      ["Can oppose selection?", "Yes — swamps local adaptation", "Yes — can fix maladaptive alleles"],
      ["Result", "Populations become more similar", "Populations diverge randomly"]
    ]
  },
  {
    title: "Gradualism vs Punctuated Equilibrium",
    left: "Gradualism", right: "Punctuated Equilibrium",
    rows: [
      ["Rate of change", "Slow, constant accumulation", "Long stasis punctuated by rapid bursts"],
      ["Proposed by", "Darwin (implicit in Origin)", "Eldredge & Gould (1972)"],
      ["Fossil prediction", "Continuous transitional forms", "Gaps are real — stasis + rapid change"],
      ["Mechanism", "Same neo-Darwinian processes, slow pace", "Speciation events drive morphological change"],
      ["Stasis explained", "Stabilizing selection", "Developmental/genetic constraints"],
      ["Current view", "Both patterns observed — not mutually exclusive", "Both patterns observed — not mutually exclusive"]
    ]
  },
  {
    title: "Parasitism vs Mutualism (Coevolution)",
    left: "Parasitic Coevolution", right: "Mutualistic Coevolution",
    rows: [
      ["Relationship", "One benefits, one harmed (+/−)", "Both benefit (+/+)"],
      ["Selection dynamic", "Antagonistic arms race", "Cooperative escalation"],
      ["Red Queen applies?", "Yes — constant adaptation to keep up", "Less directly, but co-dependence can evolve"],
      ["Specificity", "Often highly host-specific", "Can be specific or diffuse"],
      ["Example", "Newt-snake toxin arms race", "Fig wasps + fig trees"],
      ["Evolutionary outcome", "Escalating offense/defense traits", "Increasing interdependence"]
    ]
  },
  {
    title: "Kin Selection vs Reciprocal Altruism",
    left: "Kin Selection", right: "Reciprocal Altruism",
    rows: [
      ["Basis", "Shared genes (relatedness r)", "Repeated interactions, not relatedness"],
      ["Hamilton's Rule", "rB > C must hold", "Not applicable — uses game theory"],
      ["Requires relatedness?", "Yes — higher r = more altruism", "No — unrelated individuals can cooperate"],
      ["Cognitive requirement", "None — can be instinctual", "Requires memory, cheater detection"],
      ["Example", "Worker bees sacrificing for queen", "Vampire bat blood sharing"],
      ["Taxonomic scope", "Universal — bacteria to humans", "Mainly cognitively complex species"]
    ]
  },
  {
    title: "Bottleneck vs Founder Effect",
    left: "Bottleneck", right: "Founder Effect",
    rows: [
      ["Cause", "Population crash (disaster, disease)", "Small group colonizes new area"],
      ["Population before", "Large → drastically reduced → recovers", "Small subset leaves parent population"],
      ["Genetic outcome", "Reduced diversity, random allele loss", "Reduced diversity, different frequencies than source"],
      ["Location", "Same geographic area", "New geographic area (migration)"],
      ["Example", "Northern elephant seals (hunted to ~30)", "Amish population (Ellis-van Creveld syndrome)"],
      ["Type of drift", "Both are special cases of genetic drift", "Both are special cases of genetic drift"]
    ]
  }
];
console.log(`Compares: ${COMPARES.length}`);

// ── 4. SEQUENCES ─────────────────────────────────────────────────
const SEQUENCES = [
  {
    title: "Natural Selection — The Four Ingredients",
    steps: [
      { n: 1, text: "<strong>Variation</strong> — Individuals in a population differ in phenotypic traits." },
      { n: 2, text: "<strong>Heritability</strong> — Some of that variation is heritable (passed from parent to offspring via genes)." },
      { n: 3, text: "<strong>Differential survival/reproduction</strong> — Some variants survive or reproduce better than others in the current environment." },
      { n: 4, text: "<strong>Non-random outcome</strong> — Advantageous alleles increase in frequency across generations → population evolves." }
    ]
  },
  {
    title: "Hardy-Weinberg Equilibrium — Conditions & Logic",
    steps: [
      { n: 1, text: "Start with a <strong>large population</strong> (no drift)." },
      { n: 2, text: "Require <strong>no mutation</strong> (alleles don't change)." },
      { n: 3, text: "Require <strong>no migration</strong> (no gene flow in or out)." },
      { n: 4, text: "Require <strong>random mating</strong> (no sexual selection or assortative mating)." },
      { n: 5, text: "Require <strong>no selection</strong> (all genotypes equally fit)." },
      { n: 6, text: "If ALL five hold → allele frequencies stay at p² + 2pq + q² = 1 forever. Violation of any = <strong>evolution is occurring</strong>." }
    ]
  },
  {
    title: "Genetic Drift → Fixation in Small Populations",
    steps: [
      { n: 1, text: "Small population has limited allele copies each generation." },
      { n: 2, text: "<strong>Random sampling</strong> — not all parents contribute equally to the next generation by chance." },
      { n: 3, text: "Allele frequencies <strong>fluctuate unpredictably</strong> each generation." },
      { n: 4, text: "Over many generations, one allele randomly reaches <strong>fixation (100%)</strong> or <strong>loss (0%)</strong>." },
      { n: 5, text: "Result: <strong>reduced genetic diversity</strong> — the population becomes more homogeneous." }
    ]
  },
  {
    title: "Speciation — Allopatric Model",
    steps: [
      { n: 1, text: "Ancestral population occupies a continuous range." },
      { n: 2, text: "<strong>Geographic barrier</strong> forms (mountain, river, glacier) splitting the population." },
      { n: 3, text: "Gene flow is <strong>completely interrupted</strong> between the two groups." },
      { n: 4, text: "Each group experiences <strong>independent selection, drift, and mutation</strong>." },
      { n: 5, text: "Genetic divergence accumulates over time." },
      { n: 6, text: "If barrier removed, populations can no longer interbreed → <strong>reproductive isolation = new species</strong>." }
    ]
  },
  {
    title: "Evolution of the Eye — From Photoreceptor to Camera",
    steps: [
      { n: 1, text: "<strong>Flat photoreceptor patch</strong> — light-sensitive cells on surface. Detects light vs dark." },
      { n: 2, text: "<strong>Cupped eye</strong> — patch folds inward. Gain crude directional sensing." },
      { n: 3, text: "<strong>Pinhole eye</strong> — cup narrows to small aperture. Produces dim but focused image (nautilus)." },
      { n: 4, text: "<strong>Lens added</strong> — transparent tissue fills aperture. Focuses light, brightens image." },
      { n: 5, text: "<strong>Camera eye</strong> — adjustable lens + iris + retina. High-resolution vision (vertebrates, cephalopods)." },
      { n: 6, text: "Each stage is <strong>functional and adaptive</strong> — no \"half an eye\" problem. ~1,800 intermediate steps modeled (Nilsson & Pelger)." }
    ]
  },
  {
    title: "Red Queen Hypothesis — Coevolutionary Arms Race",
    steps: [
      { n: 1, text: "<strong>Parasite adapts</strong> — evolves to exploit most common host genotype." },
      { n: 2, text: "Common host genotype suffers <strong>increased infection</strong> → fitness drops." },
      { n: 3, text: "<strong>Rare host genotypes</strong> gain advantage (frequency-dependent selection)." },
      { n: 4, text: "Rare genotypes <strong>increase in frequency</strong>, becoming the new common type." },
      { n: 5, text: "Parasite <strong>tracks the new common host</strong> → cycle repeats indefinitely." },
      { n: 6, text: "Result: <strong>constant cycling</strong> of genotype frequencies — \"running just to stay in place.\"" }
    ]
  },
  {
    title: "Origin of Life — Major Transitions",
    steps: [
      { n: 1, text: "<strong>Prebiotic chemistry</strong> — Miller-Urey experiment shows amino acids form in early atmosphere." },
      { n: 2, text: "<strong>RNA World</strong> — self-replicating RNA molecules arise (ribozymes = catalytic + informational)." },
      { n: 3, text: "<strong>Protocells</strong> — lipid bilayer membranes encapsulate replicators → first cell-like units." },
      { n: 4, text: "<strong>DNA takes over</strong> — more stable than RNA → becomes primary genetic material." },
      { n: 5, text: "<strong>Prokaryotes</strong> — first true cells (bacteria/archaea), ~3.5 bya stromatolites." },
      { n: 6, text: "<strong>Eukaryotes via endosymbiosis</strong> — mitochondria (+ chloroplasts) were once free-living bacteria." },
      { n: 7, text: "<strong>Multicellularity</strong> — cells cooperate → division of labor → complex organisms." }
    ]
  },
  {
    title: "Phylogeny Construction — Building a Cladogram",
    steps: [
      { n: 1, text: "Identify a set of <strong>taxa</strong> (species or groups) to classify." },
      { n: 2, text: "Collect <strong>character data</strong> — morphological traits or DNA sequences." },
      { n: 3, text: "Distinguish <strong>ancestral (plesiomorphic)</strong> vs <strong>derived (apomorphic)</strong> character states." },
      { n: 4, text: "Group taxa by <strong>shared derived characters (synapomorphies)</strong> — NOT shared ancestral traits." },
      { n: 5, text: "Apply <strong>parsimony</strong> — choose the tree requiring the fewest evolutionary changes." },
      { n: 6, text: "Add an <strong>outgroup</strong> to root the tree and determine character polarity." },
      { n: 7, text: "Result: a <strong>cladogram</strong> showing nested monophyletic groups (clades)." }
    ]
  },
  {
    title: "Fisher's Runaway Sexual Selection",
    steps: [
      { n: 1, text: "Some females happen to <strong>prefer a male trait</strong> (e.g., longer tail)." },
      { n: 2, text: "Males with the trait <strong>get more matings</strong> → more offspring." },
      { n: 3, text: "Sons inherit the <strong>exaggerated trait</strong>; daughters inherit the <strong>preference</strong>." },
      { n: 4, text: "Positive feedback loop: <strong>preference and trait genes become linked</strong>." },
      { n: 5, text: "Trait escalates beyond survival optimum — <strong>runaway process</strong>." },
      { n: 6, text: "Stopped only when <strong>survival costs</strong> of the trait balance mating advantage." }
    ]
  },
  {
    title: "BDM (Bateson-Dobzhansky-Muller) Incompatibility",
    steps: [
      { n: 1, text: "Ancestral population has genotype <strong>aabb</strong> at two loci." },
      { n: 2, text: "Population splits into two <strong>isolated groups</strong>." },
      { n: 3, text: "Group 1: allele <strong>A</strong> arises and fixes (Aabb). Works fine with b background." },
      { n: 4, text: "Group 2: allele <strong>B</strong> arises and fixes (aaBb). Works fine with a background." },
      { n: 5, text: "Groups reunite → hybrid is <strong>AaBb</strong>. A and B have <strong>never been tested together</strong>." },
      { n: 6, text: "A-B interaction causes <strong>hybrid inviability or sterility</strong> → postzygotic isolation → speciation complete." }
    ]
  },
  {
    title: "Adaptive Radiation — Process",
    steps: [
      { n: 1, text: "A lineage gains access to <strong>new ecological opportunity</strong> (new habitat, key innovation, competitors gone)." },
      { n: 2, text: "<strong>Ecological release</strong> — reduced competition allows exploitation of diverse niches." },
      { n: 3, text: "<strong>Rapid diversification</strong> — lineage splits into many species filling different niches." },
      { n: 4, text: "Each new species evolves <strong>specialized adaptations</strong> for its niche." },
      { n: 5, text: "Result: a <strong>species flock</strong> of closely related but ecologically distinct species." },
      { n: 6, text: "Classic examples: Darwin's finches, Hawaiian honeycreepers, cichlid fishes." }
    ]
  },
  {
    title: "Mass Extinction → Recovery Cycle",
    steps: [
      { n: 1, text: "<strong>Catastrophic event</strong> (asteroid, volcanism, ocean anoxia) causes rapid environmental change." },
      { n: 2, text: "<strong>Mass die-off</strong> — large fraction of species go extinct (>75% in Big Five events)." },
      { n: 3, text: "<strong>Survival lottery</strong> — survival partly random (not just fitness), altering global diversity." },
      { n: 4, text: "<strong>Ecological vacuums</strong> — niches left empty by extinct taxa." },
      { n: 5, text: "<strong>Adaptive radiation</strong> — surviving lineages diversify rapidly into open niches." },
      { n: 6, text: "<strong>Recovery</strong> — biodiversity rebuilds over 5-10 million years, often with entirely new dominant groups." }
    ]
  },
  {
    title: "Endosymbiosis — Origin of Mitochondria",
    steps: [
      { n: 1, text: "An <strong>ancestral archaean</strong> cell (host) engulfs an <strong>alpha-proteobacterium</strong>." },
      { n: 2, text: "Instead of digesting it, the bacterium <strong>survives inside</strong> the host." },
      { n: 3, text: "Bacterium provides <strong>aerobic respiration</strong> (ATP) → host gains energy advantage." },
      { n: 4, text: "Host provides <strong>nutrients and protection</strong> → mutualistic relationship." },
      { n: 5, text: "Over time, <strong>gene transfer</strong> from endosymbiont to host nucleus." },
      { n: 6, text: "Endosymbiont becomes <strong>obligate organelle = mitochondrion</strong>. Evidence: double membrane, own DNA, bacterial ribosomes." }
    ]
  },
  {
    title: "Reinforcement — Strengthening Prezygotic Barriers",
    steps: [
      { n: 1, text: "Two populations come into <strong>secondary contact</strong> after partial divergence." },
      { n: 2, text: "Hybridization occurs, but <strong>hybrids have reduced fitness</strong> (postzygotic cost)." },
      { n: 3, text: "Individuals who <strong>avoid mating with the other population</strong> produce fitter offspring." },
      { n: 4, text: "<strong>Selection strengthens prezygotic barriers</strong> (mate choice, timing, habitat) in the contact zone." },
      { n: 5, text: "Pattern: <strong>reproductive character displacement</strong> — traits more different in sympatry than allopatry." },
      { n: 6, text: "Result: speciation is <strong>completed by natural selection</strong> acting against hybridization." }
    ]
  },
  {
    title: "Breeder's Equation — Predicting Evolutionary Response",
    steps: [
      { n: 1, text: "Measure <strong>trait variation</strong> in the population (phenotypic variance)." },
      { n: 2, text: "Determine <strong>heritability (h²)</strong> — the fraction of phenotypic variance due to additive genetics." },
      { n: 3, text: "Apply <strong>selection</strong> — choose individuals above a threshold to reproduce (<strong>selection differential S</strong>)." },
      { n: 4, text: "Calculate <strong>response to selection: R = h² × S</strong>." },
      { n: 5, text: "Next generation's mean shifts by <strong>R</strong> in the direction of selection." },
      { n: 6, text: "Key insight: if h² = 0 (all variation environmental), <strong>R = 0 — no evolutionary response</strong> no matter how strong selection is." }
    ]
  }
];
console.log(`Sequences: ${SEQUENCES.length}`);

// ── 5. MATCH SETS ────────────────────────────────────────────────
// Group flashcards by chapter, pick key terms for matching
const MATCH_SETS = [];
const chapterGroups = {};
FLASHCARDS.forEach((fc, i) => {
  if (!chapterGroups[fc.ch]) chapterGroups[fc.ch] = [];
  chapterGroups[fc.ch].push(fc);
});

Object.entries(chapterGroups).forEach(([ch, cards]) => {
  // Pick up to 7 cards with short questions for matching
  const good = cards.filter(c => c.q.length < 80 && c.a.length > 20).slice(0, 7);
  if (good.length >= 4) {
    MATCH_SETS.push({
      title: `Key Terms — ${ch}`,
      pairs: good.map(c => ({
        a: c.q.replace(/\?$/, ''),
        b: c.a.split('.')[0].substring(0, 120)
      }))
    });
  }
});
console.log(`Match Sets: ${MATCH_SETS.length}`);

// ── 6. TRAPS ─────────────────────────────────────────────────────
const TRAPS = [];
data.nodes.forEach(node => {
  // From warnings
  (node.popup?.warnings || []).forEach(w => {
    const clean = w.replace(/^WATCH OUT:\s*/i, '').trim();
    // Make it a statement (often already is)
    TRAPS.push({
      stmt: clean.split('—')[0].trim().replace(/\.$/, ''),
      verdict: false,
      explain: clean
    });
  });
  // From visual traps
  if (node.visual?.trap) {
    const t = node.visual.trap;
    TRAPS.push({
      stmt: t.replace(/^Common misconception:\s*/i, '').split('.')[0].trim(),
      verdict: false,
      explain: t
    });
  }
});
// Add some true statements for balance
const trueTraps = [
  { stmt: "Evolution can occur without natural selection (e.g., genetic drift alone)", verdict: true, explain: "TRUE. Genetic drift is a random, non-selective mechanism that changes allele frequencies. Drift alone constitutes evolution by the population-genetics definition." },
  { stmt: "Natural selection acts on phenotypes, not directly on genotypes", verdict: true, explain: "TRUE. Selection 'sees' the phenotype — the organism's appearance, behavior, physiology. Genes are selected indirectly through their phenotypic effects." },
  { stmt: "Mitochondria have their own DNA because they were once free-living bacteria", verdict: true, explain: "TRUE. Endosymbiosis theory (Lynn Margulis): mitochondria descend from alpha-proteobacteria engulfed by an ancestral archaean cell. Their double membrane, bacterial ribosomes, and circular DNA are evidence." },
  { stmt: "The Hardy-Weinberg model assumes an infinitely large population", verdict: true, explain: "TRUE. One of the five HW assumptions is infinite population size (= no drift). Violating this assumption means drift can change allele frequencies." },
  { stmt: "Extinction is the ultimate fate of all species", verdict: true, explain: "TRUE. Over 99% of all species that ever lived are extinct. Extinction is the norm, not the exception, in evolutionary history." },
  { stmt: "Sexual selection can favor traits that DECREASE survival", verdict: true, explain: "TRUE. The peacock's tail is the classic example — it reduces flight ability and increases predation risk but increases mating success. Sexual and natural selection can oppose each other." },
  { stmt: "Ring species demonstrate speciation as a gradual geographic continuum", verdict: true, explain: "TRUE. In ring species (e.g., Ensatina salamanders), adjacent populations can interbreed, but the endpoints of the ring cannot — showing speciation as a continuous process." },
  { stmt: "Heritability of zero means selection cannot change the trait across generations", verdict: true, explain: "TRUE. From the breeder's equation R = h²S: if h² = 0, then R = 0 regardless of selection intensity. All variation is environmental, so nothing is passed to offspring." },
  { stmt: "Convergent evolution produces analogous structures, not homologous ones", verdict: true, explain: "TRUE. Convergent evolution = independent lineages evolving similar solutions to similar problems. These structures are analogous (similar function, different origin), not homologous (same origin)." },
  { stmt: "Inclusive fitness counts an individual's own reproduction PLUS the reproduction of relatives it helps", verdict: true, explain: "TRUE. Hamilton's inclusive fitness = direct fitness (own offspring) + indirect fitness (relatives' offspring weighted by relatedness r). This is the basis of kin selection theory." }
];
TRAPS.push(...trueTraps);
console.log(`Traps: ${TRAPS.length}`);

// ── 7. BOSS MODE ─────────────────────────────────────────────────
const BOSS = [
  {
    q: "A new antibiotic is developed. Within 5 years, resistant bacteria dominate hospitals. Trace this outcome through mutation, natural selection, genetic drift, and gene flow — explaining how each mechanism contributes to the spread of resistance.",
    a: "This integrates Lectures 3 (mutation), 4 (all four mechanisms), and 9 (arms races). <strong>Mutation</strong> provides the raw material — a random change in a bacterial gene (e.g., beta-lactamase) that happens to break down the antibiotic. This mutation exists at low frequency. <strong>Natural selection</strong> then acts: in hospitals saturated with the antibiotic, resistant bacteria survive while susceptible ones die. The resistant allele rapidly increases in frequency — classic directional selection. <strong>Gene flow</strong> spreads resistance between populations via horizontal gene transfer (plasmids carrying resistance genes move between bacterial species) and physical transfer (patients, healthcare workers moving between hospitals). <strong>Genetic drift</strong> can accelerate fixation in small bacterial colonies (e.g., on a catheter surface). The combination makes resistance nearly inevitable — it's not a matter of IF but WHEN. This is evolution by natural selection observed in real time, on the timescale of years rather than millennia."
  },
  {
    q: "Why does sex exist, given its enormous costs? Synthesize the Red Queen hypothesis, Muller's Ratchet, and the two-fold cost of sex into a coherent argument.",
    a: "This integrates Lectures 9 (coevolution/Red Queen), 10-11 (sexual selection), and 3 (genetic variation). The <strong>two-fold cost</strong>: sexual females pass only 50% of their genes per offspring (males contribute nothing to population growth in many species). An asexual female passes 100%. So sex must provide a >2x fitness advantage to persist. <strong>Muller's Ratchet</strong>: asexual lineages accumulate deleterious mutations irreversibly (no recombination to purge them). Sex recombines genomes, creating offspring with fewer harmful mutations. <strong>Red Queen</strong>: parasites adapt to the most common host genotype. Sexual reproduction shuffles genotypes each generation, producing rare combinations that parasites haven't yet adapted to. Asexual clones are sitting ducks — all genetically identical, all equally vulnerable. The synthesis: sex is maintained because it generates genetic diversity that (1) purges harmful mutations (Muller's Ratchet) and (2) outruns parasites (Red Queen). The cost of sex is real but the cost of NOT having sex — clonal vulnerability to parasites and mutational meltdown — is even greater."
  },
  {
    q: "Explain how fitness landscapes connect to speciation. How can a single population on one adaptive peak end up as two species on different peaks?",
    a: "This integrates Lectures 7 (fitness landscapes), 4 (drift), and Ch 13 (speciation). A <strong>fitness landscape</strong> maps genotypes to fitness — peaks are adaptive optima, valleys are maladaptive combinations. A population clusters around one peak. <strong>Allopatric speciation</strong>: a barrier splits the population. Each subpopulation independently explores the landscape via mutation and drift. In small populations, <strong>drift can push a population through a fitness valley</strong> to reach a new peak that selection alone couldn't reach (Wright's shifting balance). The two populations end up on different adaptive peaks with different genotypes. When they meet again, hybrids fall in the valley (low fitness) = <strong>postzygotic isolation</strong>. <strong>Disruptive selection</strong> can also split a population: if the landscape has two peaks with a valley between, individuals near the extremes outperform intermediates, potentially driving sympatric divergence. <strong>BDM incompatibilities</strong> are the molecular mechanism: different substitutions fixed in each population are individually fine but interact badly in hybrids — the valley on the landscape."
  },
  {
    q: "The peacock's tail is a textbook example of sexual selection. But it's also an imperfect adaptation. Explain this apparent contradiction using runaway selection, honest signaling, and antagonistic pleiotropy.",
    a: "This integrates Lectures 8 (adaptation/pleiotropy), 10-11 (sexual selection), and 7 (empirical selection). <strong>Fisher's runaway</strong>: female preference for long tails co-evolves with the tail itself. Sons get long tails; daughters get the preference. Positive feedback escalates the trait far beyond the survival optimum. <strong>Honest signaling (Zahavi's handicap)</strong>: the tail is costly to produce and maintain. Only genuinely healthy, well-fed males can afford an extravagant tail. The cost IS the signal — it honestly advertises male quality because weak males can't fake it. <strong>Antagonistic pleiotropy</strong>: genes for tail length affect multiple traits. The same genes that produce a magnificent display also increase predation risk, energy expenditure, and flight impairment. There's no 'tail gene' that only affects the tail — pleiotropy means every adaptation comes with trade-offs. The tail IS an adaptation (for mating success) AND an imperfection (for survival). This isn't a contradiction — it's the fundamental insight that evolution optimizes inclusive fitness, not any single trait. The peacock's tail represents a compromise between sexual and natural selection, mediated by pleiotropic genetic architecture."
  },
  {
    q: "How does the evolution of feathers illustrate exaptation, evo-devo, and the relationship between micro- and macroevolution?",
    a: "This integrates Lectures 8 (evo-devo, exaptation), 14 (macroevolution), and 15 (phylogeny). <strong>Exaptation</strong>: feathers did NOT evolve for flight. Fossil evidence (e.g., Sinosauropteryx) shows feathered dinosaurs that couldn't fly. Original function was likely <strong>thermoregulation</strong> (insulation) or display. Flight was a later co-option — an exaptation. <strong>Evo-devo</strong>: feather development uses the same signaling pathways (Shh, BMP, Wnt) as reptilian scales. A small regulatory change — tweaking when and where these genes are expressed — transforms a flat scale into a branching feather. This shows how major morphological innovations can arise from <strong>regulatory mutations</strong>, not new genes. <strong>Micro → Macro connection</strong>: each step (scale → filament → branched feather → asymmetric flight feather) is a small, selectable modification. No single macro-mutation was needed. Phylogenetic analysis of theropod dinosaurs shows the feather stages mapped onto the cladogram — documenting the gradual assembly of the flight apparatus over millions of years. The lesson: macroevolutionary novelty emerges from accumulated microevolutionary changes, often with function shifts (exaptation) along the way."
  },
  {
    q: "A species of snail shows a ring distribution around a mountain range. Adjacent populations interbreed, but the two ends of the ring cannot. Explain this using gene flow, genetic drift, reproductive isolation, and the biological species concept.",
    a: "This integrates Lectures 4 (gene flow, drift), Ch 13 (species concepts, speciation), and 7 (empirical selection). <strong>Gene flow</strong> connects adjacent populations — alleles move stepwise around the ring, maintaining partial genetic cohesion between neighbors. But gene flow attenuates with distance: populations far apart along the ring exchange very few alleles. <strong>Genetic drift + local selection</strong>: each population independently adapts to its local environment and accumulates random genetic changes. These changes compound across the ring. <strong>The endpoints</strong>: by the time the ring closes, the two terminal populations have diverged so much that they're reproductively isolated — they can't interbreed even in sympatry. <strong>BSC paradox</strong>: the biological species concept says reproductively isolated populations are different species. But there's a continuous chain of interbreeding populations connecting them! Where do you draw the species boundary? Ring species demonstrate that speciation is a <strong>continuous process</strong>, not a discrete event — and they expose the limitations of the BSC. They're among the most powerful natural demonstrations that speciation is gradual geographic divergence."
  },
  {
    q: "Explain how Hamilton's Rule (rB > C), the concept of inclusive fitness, and the evolution of eusociality in Hymenoptera all connect. Why are bees and ants more likely to evolve eusociality than mammals?",
    a: "This integrates Lectures 13 (kin selection, altruism), 10-11 (anisogamy, relatedness), and 3 (genetics/meiosis). <strong>Hamilton's Rule</strong>: altruism evolves when rB > C — the benefit (B) to the recipient, weighted by relatedness (r), exceeds the cost (C) to the altruist. <strong>Inclusive fitness</strong>: an organism's genetic success includes not just its own offspring (direct fitness) but the offspring of relatives it helps, weighted by r (indirect fitness). <strong>Hymenopteran haplodiploidy</strong>: females are diploid (from fertilized eggs), males are haploid (from unfertilized eggs). This creates asymmetric relatedness: sisters share 75% of genes (r = 0.75), but a mother shares only 50% with her daughters (r = 0.5). A female worker is <strong>more related to her sisters than to her own potential daughters</strong>. So helping her mother produce more sisters (B × 0.75) can exceed the cost of foregoing her own reproduction (C × 0.5). This makes the rB > C condition easier to satisfy. <strong>Mammals</strong>: with standard diploid genetics, siblings share r = 0.5, same as parent-offspring. The asymmetry that makes eusociality 'easy' in Hymenoptera doesn't exist. Eusociality in mammals (naked mole-rats) is much rarer and requires additional ecological factors (high predation, cooperative burrow defense)."
  },
  {
    q: "Mass extinctions have repeatedly reset the evolutionary playing field. Using the K-T extinction as a case study, explain how extinction, adaptive radiation, and contingency interact to shape biodiversity.",
    a: "This integrates Lectures 14 (deep time, mass extinctions), 8 (adaptation), and the concept of historical contingency. <strong>The K-T extinction</strong> (66 mya): an asteroid impact + Deccan Traps volcanism eliminated ~75% of species, including all non-avian dinosaurs. <strong>Contingency</strong>: which lineages survived was partly random — not just about fitness. Small, nocturnal, burrowing mammals survived not because they were 'better' but because their traits happened to match the post-impact conditions (cold, dark, food scarcity). Dinosaurs' traits (large body size, high metabolic needs) that were highly adaptive before the impact became lethal liabilities. <strong>Ecological release</strong>: with dinosaurs gone, mammals faced vastly reduced competition and empty niches — terrestrial herbivore, large predator, marine mammal niches all open. <strong>Adaptive radiation</strong>: mammals explosively diversified in the Paleocene/Eocene, filling niches dinosaurs once occupied. Bats, whales, primates, ungulates all radiated from small insectivore-like ancestors. <strong>The lesson</strong>: evolution is not progressive. The 'best-adapted' lineage can be wiped out by an unpredictable catastrophe, and the survivors radiate into a world shaped by accident as much as selection. History matters — rewind the tape and you'd get a completely different biosphere."
  },
  {
    q: "Reaction norms and phenotypic plasticity challenge the simple 'genotype determines phenotype' model. How do they connect to heritability, the breeder's equation, and the limits of natural selection?",
    a: "This integrates Lectures 5-6 (quantitative genetics, heritability, plasticity) and 4 (selection as mechanism). <strong>Reaction norms</strong>: a genotype doesn't produce one phenotype — it produces a RANGE of phenotypes depending on the environment. The reaction norm is the function mapping environment → phenotype for a given genotype. <strong>Phenotypic plasticity</strong>: the ability of a genotype to produce different phenotypes in different environments. Flat reaction norms = low plasticity; steep = high plasticity. <strong>Impact on heritability</strong>: heritability (h²) measures the fraction of phenotypic variance due to additive genetic variance. In a uniform environment, most variation is genetic → h² is high. In a variable environment, environmental variation dominates → h² drops. <strong>Breeder's equation R = h²S</strong>: if plasticity adds environmental variance, h² decreases, and selection response (R) decreases even with strong selection (S). <strong>The limit</strong>: natural selection can only act on heritable variation. If a trait's variation is mostly plastic (environmental), selection cannot change it genetically. This is why heritability must be measured in the specific environment where selection occurs — h² is not a property of the trait alone but of the trait-in-environment."
  },
  {
    q: "Compare how evolutionary medicine explains antibiotic resistance, autoimmune diseases, and aging — three seemingly unrelated health issues — through a unified evolutionary lens.",
    a: "This integrates the Evolutionary Medicine lecture, Lectures 3-4 (mutation, selection), 12 (aging/life history), and 9 (coevolution). <strong>Antibiotic resistance</strong>: bacteria evolve resistance by natural selection — antibiotics create a strong selective environment, resistant mutants survive and proliferate. This is evolution by natural selection observed in real time. The evolutionary insight: we need to manage antibiotic use to slow selection for resistance (rotation, combination therapy). <strong>Autoimmune diseases</strong>: the immune system evolved under constant pathogen pressure (Red Queen). In modern hygienic environments, the immune system may be 'over-tuned' — it evolved to fight parasites we no longer encounter. The hygiene hypothesis suggests that without these calibrating infections, the immune system attacks self-tissues. Evolutionary mismatch: our immune genes are adapted to ancestral, not modern, environments. <strong>Aging</strong>: explained by antagonistic pleiotropy (Williams 1957) and mutation accumulation (Medawar 1952). Genes that boost early reproduction but cause late-life damage are favored by selection because most individuals in ancestral environments died young from extrinsic causes (predation, disease). Selection is strong on early traits, weak on late traits. <strong>Unified lens</strong>: all three arise from the fact that evolution optimizes reproductive fitness, not health or longevity, and that adaptation to past environments can cause problems in present ones."
  }
];
console.log(`Boss: ${BOSS.length}`);

// ── 8. CHAPTERS ──────────────────────────────────────────────────
const CHAPTER_MAP = {
  'Lec 1-2': { title: 'Lectures 1-2: Evolution & Darwin', nodes: [] },
  'Lec 3': { title: 'Lecture 3: Genetics & Mutation', nodes: [] },
  'Lec 4': { title: 'Lecture 4: Mechanisms of Evolution', nodes: [] },
  'Lec 5-6': { title: 'Lectures 5-6: Quantitative Genetics', nodes: [] },
  'Lec 7': { title: 'Lecture 7: Empirical Natural Selection', nodes: [] },
  'Lec 8': { title: 'Lecture 8: Adaptation & Evo-Devo', nodes: [] },
  'Lec 9': { title: 'Lecture 9: Coevolution', nodes: [] },
  'Lec 10-11': { title: 'Lectures 10-11: Sexual Selection', nodes: [] },
  'Lec 12': { title: 'Lecture 12: Life History & Aging', nodes: [] },
  'Lec 13': { title: 'Lecture 13: Social Evolution', nodes: [] },
  'Lec 14': { title: 'Lecture 14: Deep Time & Macroevolution', nodes: [] },
  'Lec 15': { title: 'Lecture 15: Phylogenetics', nodes: [] },
  'Speciation': { title: 'Speciation (Ch 13)', nodes: [] },
  'Applied': { title: 'Applied Evolution', nodes: [] },
};
data.nodes.forEach(node => {
  const ch = getChapter(node.id);
  if (CHAPTER_MAP[ch]) {
    CHAPTER_MAP[ch].nodes.push({
      id: node.id,
      title: node.title,
      subtitle: node.subtitle || '',
      core: node.popup?.sections?.find(s => s.label === 'CORE CONCEPT')?.body || '',
      sections: (node.popup?.sections || []).filter(s => s.label !== 'CORE CONCEPT').map(s => ({
        label: s.label,
        body: s.body
      })),
      warnings: node.popup?.warnings || [],
      mnemonic: node.visual?.mnemonic || '',
    });
  }
});

// ── Escape for embedding in JS ───────────────────────────────────
function jsStr(obj) {
  return JSON.stringify(obj)
    .replace(/<\/script/gi, '<\\/script')
    .replace(/<!--/g, '<\\!--');
}

// ── BUILD HTML ───────────────────────────────────────────────────
const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evolution Full Course — Study Command Center</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
/* ── Reset ─────────────────────────────────────────── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0a0a;--surface:#141414;--surface2:#1a1a1a;--surface3:#1e1e1e;--surface4:#252525;
  --text:#e5e5e5;--text2:#888;--text3:#666;
  --accent:#e5e5e5;--accent2:#ccc;--accent-dim:rgba(255,255,255,0.08);
  --green:#ccc;--green-dim:rgba(255,255,255,0.06);
  --red:#999;--red-dim:rgba(255,255,255,0.05);
  --blue:#bbb;--blue-dim:rgba(255,255,255,0.06);
  --teal:#aaa;--teal-dim:rgba(255,255,255,0.06);
  --amber:#ddd;--amber-dim:rgba(255,255,255,0.07);
  --purple:#bbb;--purple-dim:rgba(255,255,255,0.06);
  --rose:#999;--rose-dim:rgba(255,255,255,0.05);
  --font:'Inter',system-ui,-apple-system,sans-serif;
  --font-heading:'Cormorant Garamond',Georgia,serif;
  --font-mono:'JetBrains Mono','Fira Code',monospace;
  --radius:10px;--radius-sm:6px;--radius-md:8px;--radius-lg:12px;--radius-xl:12px;
  --trans:all .25s cubic-bezier(.4,0,.2,1);
  --glow-accent:0 0 0 1px rgba(255,255,255,0.15),0 4px 12px rgba(0,0,0,0.3);
}
body{background:var(--bg);color:var(--text);font-family:var(--font);font-size:14px;line-height:1.6;overflow-x:hidden}
a{color:var(--accent);text-decoration:none}
h1,h2,h3{font-family:var(--font-heading);font-weight:600;line-height:1.2}

/* ── Animations ────────────────────────────────────── */
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes cardEnter{from{opacity:0;transform:scale(.97) translateY(16px)}to{opacity:1;transform:none}}
@keyframes glowPulse{0%,100%{box-shadow:0 0 0 0 rgba(255,255,255,0.1)}50%{box-shadow:0 0 0 6px rgba(255,255,255,0)}}
@keyframes wrongShake{0%,100%{transform:none}25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
@keyframes correctFlash{0%{background:rgba(255,255,255,0.15)}100%{background:inherit}}
@keyframes badgePop{0%{transform:scale(.7)}70%{transform:scale(1.12)}100%{transform:scale(1)}}
@keyframes ripple{to{transform:scale(4);opacity:0}}
@keyframes revealDown{from{max-height:0;opacity:0}to{max-height:600px;opacity:1}}
@keyframes shimmer{from{background-position:-200% 0}to{background-position:200% 0}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.6}}

/* ── Topbar ────────────────────────────────────────── */
#topbar{position:sticky;top:0;z-index:100;background:rgba(10,10,10,0.95);backdrop-filter:blur(12px);
  border-bottom:1px solid rgba(255,255,255,0.06);padding:0 20px;display:flex;align-items:center;gap:12px;height:52px}
#topbar h1{font-size:1.1rem;font-weight:600;white-space:nowrap;color:var(--text)}
#nav{display:flex;overflow-x:auto;gap:4px;flex:1;scrollbar-width:none;-ms-overflow-style:none}
#nav::-webkit-scrollbar{display:none}
.tab-btn{padding:7px 16px;border-radius:var(--radius-sm);border:none;background:transparent;
  color:var(--text2);font-size:13px;font-weight:500;font-family:var(--font);cursor:pointer;
  white-space:nowrap;transition:var(--trans)}
.tab-btn:hover{color:var(--text);background:var(--surface2)}
.tab-btn.active{color:var(--text);background:var(--accent-dim)}
#gs-trigger{background:none;border:none;color:var(--text2);cursor:pointer;padding:6px;border-radius:4px;flex-shrink:0}
#gs-trigger:hover{color:var(--text);background:var(--surface2)}

/* ── Main ──────────────────────────────────────────── */
#main{max-width:960px;margin:0 auto;padding:24px 20px 100px}
.view{display:none}.view.active{display:block;animation:fadeUp .3s ease}

/* ── Card ──────────────────────────────────────────── */
.card{background:var(--surface);border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius);
  padding:1.25rem 1.5rem;transition:var(--trans);margin-bottom:16px}
.card:hover{border-color:rgba(255,255,255,0.12);transform:translateY(-1px)}

/* ── Flashcard ─────────────────────────────────────── */
#fc-area{perspective:1000px;min-height:300px;cursor:pointer;margin-bottom:16px}
#fc-inner{position:relative;width:100%;min-height:300px;transform-style:preserve-3d;transition:transform .6s cubic-bezier(.4,0,.2,1)}
#fc-inner.flipped{transform:rotateY(180deg)}
.fc-front,.fc-back{position:absolute;width:100%;min-height:300px;backface-visibility:hidden;
  background:var(--surface);border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius);
  padding:2rem;display:flex;flex-direction:column;justify-content:center}
.fc-back{transform:rotateY(180deg)}
.fc-front-label{font-size:12px;color:var(--text3);margin-bottom:12px;text-transform:uppercase;letter-spacing:.05em}
.fc-question{font-size:1.3rem;font-weight:600;font-family:var(--font-heading);line-height:1.3}
.fc-answer{font-size:.95rem;line-height:1.7;color:var(--text)}
.fc-controls{display:flex;gap:12px;justify-content:center;margin-top:16px}
.fc-controls button{padding:10px 28px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface);color:var(--text);cursor:pointer;font-family:var(--font);font-size:14px;transition:var(--trans)}
.fc-controls button:hover{background:var(--surface2);border-color:rgba(255,255,255,0.2)}
.fc-progress{text-align:center;color:var(--text2);font-size:13px;margin-top:8px}
#fc-inner.swipe-left{transition:transform .3s ease,opacity .3s ease;transform:translateX(-120%) rotateZ(-8deg);opacity:0}
#fc-inner.swipe-right{transition:transform .3s ease,opacity .3s ease;transform:translateX(120%) rotateZ(8deg);opacity:0}

/* ── Quiz ──────────────────────────────────────────── */
#quiz-results-bar{display:flex;align-items:center;justify-content:space-between;position:sticky;top:52px;z-index:50;
  background:var(--surface);padding:8px 16px;border-bottom:1px solid rgba(255,255,255,0.06);
  border-radius:var(--radius-sm);margin-bottom:16px}
#quiz-score{font-size:14px;font-weight:600;color:var(--text)}
#quiz-reset{padding:6px 14px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface2);color:var(--text2);cursor:pointer;font-size:12px;font-family:var(--font)}
.quiz-q{border-left:3px solid var(--accent);padding-left:16px;margin-bottom:24px}
.quiz-question{font-size:1rem;font-weight:500;margin-bottom:12px;line-height:1.5}
.quiz-opts{display:flex;flex-direction:column;gap:8px}
.quiz-opt{border:1px solid rgba(255,255,255,0.08);border-radius:var(--radius-sm);padding:10px 14px;
  cursor:pointer;transition:background .15s,border-color .15s;font-size:14px;background:var(--surface);color:var(--text)}
.quiz-opt:hover{background:var(--surface2)}
.quiz-opt.selected{background:var(--accent-dim);border-color:rgba(255,255,255,0.2)}
.quiz-opt.correct{background:rgba(46,160,67,0.18);color:var(--green);animation:correctFlash .5s ease}
.quiz-opt.wrong{text-decoration:line-through;color:var(--text3);animation:wrongShake .4s ease}
.quiz-explain{display:none;border-left:3px solid var(--teal);background:var(--teal-dim);
  padding:10px 14px;margin-top:8px;border-radius:0 var(--radius-sm) var(--radius-sm) 0;font-size:13px;line-height:1.6}
.quiz-explain.show{display:block;animation:revealDown .3s ease}

/* ── Compare ───────────────────────────────────────── */
.cmp-card h3{font-size:1.3rem;margin-bottom:12px}
.cmp-grid{display:grid;grid-template-columns:auto 1fr 1fr;gap:1px;background:rgba(255,255,255,0.06);border-radius:var(--radius-sm);overflow:hidden}
.cmp-header{padding:10px 14px;font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.03em}
.cmp-header.feat{background:var(--surface3);color:var(--text2)}
.cmp-header.left{background:rgba(170,170,170,0.08);color:var(--teal)}
.cmp-header.right{background:rgba(187,187,187,0.08);color:var(--purple)}
.cmp-cell{padding:10px 14px;background:var(--surface);font-size:13px;line-height:1.5}
.cmp-cell.feat{font-weight:500;color:var(--text2);background:var(--surface2)}

/* ── Sequence ──────────────────────────────────────── */
.seq-card h3{font-size:1.3rem;margin-bottom:12px}
.seq-item{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.05)}
.seq-item:last-child{border-bottom:none}
.seq-num{width:28px;height:28px;border-radius:50%;background:var(--accent-dim);
  display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0;color:var(--text)}
.seq-text{font-size:14px;line-height:1.6}

/* ── Match ─────────────────────────────────────────── */
#match-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
#match-header h3{font-size:1.3rem}
#match-score{font-size:14px;color:var(--text2)}
#match-next{padding:6px 14px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface2);color:var(--text2);cursor:pointer;font-size:12px;font-family:var(--font)}
.match-wrap{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.match-col{display:flex;flex-direction:column;gap:8px}
.match-btn{padding:10px 14px;border:1px solid rgba(255,255,255,0.08);border-radius:var(--radius-sm);
  cursor:pointer;transition:var(--trans);text-align:left;background:var(--surface);color:var(--text);font-size:13px;font-family:var(--font)}
.match-btn:hover{background:var(--surface2)}
.match-btn.selected{background:var(--accent-dim);animation:glowPulse 1.5s infinite}
.match-btn.matched{background:var(--green-dim);pointer-events:none;opacity:.7}
.match-btn.wrong{animation:wrongShake .4s ease}

/* ── Trap ──────────────────────────────────────────── */
.trap-card{margin-bottom:16px}
.trap-stmt{font-size:1rem;font-weight:500;line-height:1.5;margin-bottom:10px}
.trap-controls{display:flex;gap:8px;margin-bottom:8px}
.trap-controls button{padding:6px 16px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface2);color:var(--text2);cursor:pointer;font-size:13px;font-family:var(--font);transition:var(--trans)}
.trap-controls button:hover{background:var(--surface3);color:var(--text)}
.trap-reveal{display:none;animation:revealDown .3s ease}
.trap-reveal.show{display:block}
.trap-verdict{display:inline-block;padding:3px 12px;border-radius:99px;font-size:12px;font-weight:600;margin-bottom:8px}
.trap-verdict.true{background:var(--green-dim);color:var(--green)}
.trap-verdict.false{background:var(--red-dim);color:var(--red)}
.trap-explain{font-size:13px;line-height:1.6;color:var(--text2);border-left:3px solid var(--rose);
  background:var(--rose-dim);padding:10px 14px;border-radius:0 var(--radius-sm) var(--radius-sm) 0}

/* ── Boss ──────────────────────────────────────────── */
.boss-q{border-left:3px solid var(--red);padding-left:16px;margin-bottom:24px}
.boss-question{font-size:1rem;font-weight:500;line-height:1.5;margin-bottom:12px}
.boss-toggle{padding:6px 16px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface2);color:var(--text2);cursor:pointer;font-size:13px;font-family:var(--font)}
.boss-answer{display:none;margin-top:12px;font-size:14px;line-height:1.7;color:var(--text);
  border-left:3px solid var(--teal);background:var(--teal-dim);padding:14px;border-radius:0 var(--radius-sm) var(--radius-sm) 0}
.boss-answer.show{display:block;animation:revealDown .3s ease}

/* ── Chapters ──────────────────────────────────────── */
#chapters-layout{display:grid;grid-template-columns:240px 1fr;gap:24px;align-items:start}
#chapters-toc{position:sticky;top:52px;max-height:calc(100vh - 80px);overflow-y:auto;
  scrollbar-width:thin;scrollbar-color:var(--surface3) transparent}
.toc-item{padding:8px 12px;border-radius:var(--radius-sm);cursor:pointer;font-size:13px;
  color:var(--text2);transition:var(--trans);display:flex;justify-content:space-between;align-items:center}
.toc-item:hover{background:var(--surface2);color:var(--text)}
.toc-item.active{background:var(--accent-dim);color:var(--text)}
.toc-qcount{font-size:11px;color:var(--text3);background:var(--surface3);padding:1px 6px;border-radius:99px}
#toc-toggle{display:none;padding:8px 16px;border-radius:var(--radius-sm);border:1px solid rgba(255,255,255,0.1);
  background:var(--surface);color:var(--text2);cursor:pointer;font-size:13px;font-family:var(--font);margin-bottom:12px}
.concept-block{margin-bottom:16px}
.concept-header{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.concept-body{font-size:14px;line-height:1.7;color:var(--text)}
.concept-body p{margin-bottom:8px}
.concept-sections{margin-top:12px}
.concept-section{margin-bottom:10px}
.concept-section-label{font-size:11px;font-weight:600;letter-spacing:.05em;color:var(--text2);text-transform:uppercase;margin-bottom:4px}

/* ── Callouts ──────────────────────────────────────── */
.eli5{border-left:3px solid var(--teal);background:var(--teal-dim);padding:10px 14px;border-radius:0 6px 6px 0;margin-top:12px}
.mnemonic{border-left:3px solid var(--amber);background:var(--amber-dim);padding:10px 14px;border-radius:0 6px 6px 0;margin-top:8px}
.trap-note{border-left:3px solid var(--rose);background:var(--rose-dim);padding:10px 14px;border-radius:0 6px 6px 0;margin-top:8px}
.callout-label{display:block;font-size:11px;font-weight:600;letter-spacing:.05em;color:var(--text2);margin-bottom:4px;text-transform:uppercase}

/* ── Shared ────────────────────────────────────────── */
.term{background:var(--accent-dim);padding:1px 6px;border-radius:4px;font-weight:500}
.pill{display:inline-block;padding:3px 10px;border-radius:99px;font-size:11px;font-weight:500;background:var(--accent-dim);color:var(--text)}
.progress-bar-track{background:var(--surface3);border-radius:99px;height:4px;overflow:hidden}
.progress-bar-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .3s}

/* ── Timer ─────────────────────────────────────────── */
#timer-bar{position:fixed;bottom:0;width:100%;z-index:200;background:var(--surface);
  border-top:1px solid rgba(255,255,255,0.08);backdrop-filter:blur(12px);
  padding:8px 16px;display:flex;align-items:center;gap:12px}
#timer-bar.hidden{transform:translateY(100%);pointer-events:none}
.timer-btn{background:none;border:1px solid rgba(255,255,255,0.1);border-radius:4px;
  color:var(--text2);padding:4px 8px;cursor:pointer;font-family:var(--font);font-size:13px}
.timer-btn:hover{color:var(--text);border-color:rgba(255,255,255,0.2)}
#timer-speed{flex:0 0 100px;accent-color:var(--accent)}
#timer-label{font-size:12px;color:var(--text2);min-width:30px}
#timer-progress{flex:1;height:3px;background:var(--surface3);border-radius:99px;overflow:hidden}
#timer-progress-fill{height:100%;width:0%;background:var(--accent);transition:width .1s linear}

/* ── Settings ──────────────────────────────────────── */
#settings-toggle{position:fixed;bottom:70px;right:20px;width:40px;height:40px;border-radius:50%;
  background:var(--surface2);border:1px solid rgba(255,255,255,0.1);cursor:pointer;
  transition:var(--trans);z-index:150;display:flex;align-items:center;justify-content:center}
#settings-toggle:hover{border-color:rgba(255,255,255,0.2)}
#settings-toggle.open{transform:rotate(90deg)}
#settings-toggle svg{width:18px;height:18px;fill:var(--text2)}
#settings-panel{position:fixed;bottom:120px;right:20px;width:260px;padding:16px;
  background:var(--surface);border:1px solid rgba(255,255,255,0.08);border-radius:var(--radius-lg);
  z-index:149;opacity:0;pointer-events:none;transition:opacity .2s}
#settings-panel.open{opacity:1;pointer-events:auto}
.setting-group{margin-bottom:12px}
.setting-group label{font-size:12px;color:var(--text2);display:block;margin-bottom:6px}
.hotkey-grid{display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:12px}
.hotkey-grid span{padding:4px 8px;background:var(--surface2);border-radius:4px;text-align:center}

/* ── Search Modal ──────────────────────────────────── */
#gs-modal{display:none;position:fixed;inset:0;z-index:300;background:rgba(0,0,0,0.7);backdrop-filter:blur(4px);
  align-items:flex-start;justify-content:center;padding-top:80px}
#gs-modal.open{display:flex}
#gs-box{width:90%;max-width:560px;background:var(--surface);border:1px solid rgba(255,255,255,0.1);
  border-radius:var(--radius-lg);padding:16px;max-height:70vh;overflow-y:auto}
#gs-input{width:100%;padding:10px 14px;background:var(--surface2);border:1px solid rgba(255,255,255,0.08);
  border-radius:var(--radius-sm);color:var(--text);font-family:var(--font);font-size:14px;outline:none}
#gs-input:focus{border-color:rgba(255,255,255,0.2)}
#gs-results{margin-top:12px}
.gs-result{padding:10px;border-radius:var(--radius-sm);cursor:pointer;transition:var(--trans);margin-bottom:4px}
.gs-result:hover{background:var(--surface2)}
.gs-result-type{font-size:11px;color:var(--text3);text-transform:uppercase;letter-spacing:.03em}
.gs-result-text{font-size:13px;color:var(--text);margin-top:2px}

/* ── Responsive ────────────────────────────────────── */
@media(max-width:768px){
  #chapters-layout{grid-template-columns:1fr}
  #chapters-toc{display:none}
  #chapters-toc.mobile-show{display:block;position:fixed;top:52px;left:0;width:240px;height:100%;
    z-index:90;background:var(--surface);padding:16px;overflow-y:auto;border-right:1px solid rgba(255,255,255,0.06)}
  #toc-toggle{display:block}
  .cmp-grid{grid-template-columns:auto 1fr;gap:1px}
  .cmp-header.right,.cmp-cell:nth-child(3n){display:none}
  .match-wrap{grid-template-columns:1fr}
}
@media(max-width:480px){
  #main{padding:16px 12px 100px}
  .card{padding:1rem 1.1rem}
  #topbar h1{font-size:.9rem}
}
@media print{
  #topbar,#timer-bar,#settings-toggle,#settings-panel,#gs-modal{display:none!important}
  body{background:#fff!important;color:#000!important}
  .card{break-inside:avoid;border:1px solid #ddd!important}
}
</style>
</head>
<body>

<!-- ── Topbar ──────────────────────────────────────── -->
<div id="topbar">
  <h1>Evolution — Study Hub</h1>
  <div id="nav">
    <button class="tab-btn active" data-tab="flashcards">Flashcards</button>
    <button class="tab-btn" data-tab="quiz">Quiz</button>
    <button class="tab-btn" data-tab="compare">Compare</button>
    <button class="tab-btn" data-tab="sequence">Sequence</button>
    <button class="tab-btn" data-tab="match">Match</button>
    <button class="tab-btn" data-tab="trapdrill">Trap Drill</button>
    <button class="tab-btn" data-tab="bossmode">Boss Mode</button>
    <button class="tab-btn" data-tab="chapters">Chapters</button>
  </div>
  <button id="gs-trigger" aria-label="Search" onclick="document.getElementById('gs-modal').classList.add('open');document.getElementById('gs-input').focus()">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
  </button>
</div>

<!-- ── Main ────────────────────────────────────────── -->
<div id="main">

  <!-- Flashcards -->
  <div id="tab-flashcards" class="view active">
    <div id="fc-area" onclick="flipCard()">
      <div id="fc-inner">
        <div class="fc-front"><div class="fc-front-label" id="fc-label"></div><div class="fc-question" id="fc-q"></div></div>
        <div class="fc-back"><div class="fc-answer" id="fc-a"></div><div class="eli5" id="fc-eli5"><span class="callout-label">ELI5</span><span id="fc-eli5-text"></span></div></div>
      </div>
    </div>
    <div class="fc-controls">
      <button id="fc-no" onclick="event.stopPropagation();fcWrong()">✗ Review again</button>
      <button id="fc-yes" onclick="event.stopPropagation();fcRight()">✓ Got it</button>
    </div>
    <div class="fc-progress" id="fc-progress"></div>
  </div>

  <!-- Quiz -->
  <div id="tab-quiz" class="view">
    <div id="quiz-results-bar">
      <span id="quiz-score">0 / 0</span>
      <button id="quiz-reset" onclick="resetQuiz()">Reset</button>
    </div>
    <div id="quiz-container"></div>
    <div id="quiz-sentinel"></div>
  </div>

  <!-- Compare -->
  <div id="tab-compare" class="view">
    <h2 style="font-size:1.6rem;margin-bottom:16px">Side-by-Side Comparisons</h2>
    <div id="compare-container"></div>
  </div>

  <!-- Sequence -->
  <div id="tab-sequence" class="view">
    <h2 style="font-size:1.6rem;margin-bottom:16px">Step-by-Step Processes</h2>
    <div id="sequence-container"></div>
  </div>

  <!-- Match -->
  <div id="tab-match" class="view">
    <div id="match-header"><h3 id="match-title"></h3><span id="match-score"></span><button id="match-next" onclick="nextMatchSet()">Next Set →</button></div>
    <div class="match-wrap" id="match-wrap"></div>
  </div>

  <!-- Trap Drill -->
  <div id="tab-trapdrill" class="view">
    <h2 style="font-size:1.6rem;margin-bottom:16px">Trap Drill — True / False / Tricky</h2>
    <div id="trap-container"></div>
  </div>

  <!-- Boss Mode -->
  <div id="tab-bossmode" class="view">
    <h2 style="font-size:1.6rem;margin-bottom:16px">Boss Mode — Hard Integration Questions</h2>
    <div id="boss-container"></div>
  </div>

  <!-- Chapters -->
  <div id="tab-chapters" class="view">
    <button id="toc-toggle" onclick="document.getElementById('chapters-toc').classList.toggle('mobile-show')">☰ Table of Contents</button>
    <div id="chapters-layout">
      <div id="chapters-toc"></div>
      <div id="chapters-body"></div>
    </div>
  </div>

</div>

<!-- ── Timer Bar ───────────────────────────────────── -->
<div id="timer-bar" class="hidden">
  <button class="timer-btn" id="timer-play" onclick="toggleTimer()">▶</button>
  <button class="timer-btn" id="timer-slower" onclick="adjustTimer(-0.5)">−</button>
  <input type="range" id="timer-speed" min="0.5" max="30" step="0.5" value="5" oninput="updateTimerLabel()">
  <button class="timer-btn" id="timer-faster" onclick="adjustTimer(0.5)">+</button>
  <span id="timer-label">5s</span>
  <div id="timer-progress"><div id="timer-progress-fill"></div></div>
  <button class="timer-btn" id="timer-close" onclick="document.getElementById('timer-bar').classList.add('hidden');stopTimer()">✕</button>
</div>

<!-- ── Settings ────────────────────────────────────── -->
<button id="settings-toggle" onclick="this.classList.toggle('open');document.getElementById('settings-panel').classList.toggle('open')">
  <svg viewBox="0 0 24 24"><path d="M12 15.5A3.5 3.5 0 1 0 12 8.5a3.5 3.5 0 0 0 0 7zm7.43-2.53l1.11-.64a1 1 0 0 0 .37-1.37l-2-3.46a1 1 0 0 0-1.37-.37l-1.11.64A8 8 0 0 0 15 6.57V5.43a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v1.14a8 8 0 0 0-1.43.83l-1.11-.64a1 1 0 0 0-1.37.37l-2 3.46a1 1 0 0 0 .37 1.37l1.11.64A8 8 0 0 0 4.57 14H3.43a1 1 0 0 0-1 1v4a1 1 0 0 0 1 1h1.14c.18.5.42.97.72 1.4l-.8.8a1 1 0 0 0 0 1.42l2.83 2.83a1 1 0 0 0 1.42 0l.8-.8z"/></svg>
</button>
<div id="settings-panel">
  <div class="setting-group">
    <label>Timer</label>
    <button class="timer-btn" onclick="document.getElementById('timer-bar').classList.remove('hidden')" style="width:100%">Show Timer Bar</button>
  </div>
  <div class="setting-group">
    <label>Keyboard Shortcuts</label>
    <div class="hotkey-grid">
      <span>F → Flash</span><span>Q → Quiz</span>
      <span>X → Compare</span><span>S → Sequence</span>
      <span>M → Match</span><span>T → Traps</span>
      <span>B → Boss</span><span>C → Chapters</span>
      <span>Space → Flip</span><span>← → → Nav</span>
      <span>P → Timer</span><span>+/- Speed</span>
    </div>
  </div>
</div>

<!-- ── Search Modal ────────────────────────────────── -->
<div id="gs-modal">
  <div id="gs-box">
    <input id="gs-input" placeholder="Search flashcards, quiz, traps..." oninput="doSearch(this.value)">
    <div id="gs-results"></div>
  </div>
</div>

<script>
// ══════════════════════════════════════════════════════
// DATA
// ══════════════════════════════════════════════════════
const FLASHCARDS=${jsStr(FLASHCARDS)};
const QUIZ=${jsStr(QUIZ)};
const COMPARES=${jsStr(COMPARES)};
const SEQUENCES=${jsStr(SEQUENCES)};
const MATCH_SETS=${jsStr(MATCH_SETS)};
const TRAPS=${jsStr(TRAPS)};
const BOSS=${jsStr(BOSS)};
const CHAPTERS=${jsStr(CHAPTER_MAP)};

// ══════════════════════════════════════════════════════
// TAB NAVIGATION
// ══════════════════════════════════════════════════════
const inited={};
function showTab(id){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  const el=document.getElementById('tab-'+id);
  if(el){el.classList.add('active')}
  const btn=document.querySelector('.tab-btn[data-tab="'+id+'"]');
  if(btn){btn.classList.add('active')}
  window.scrollTo(0,0);
  if(!inited[id]){inited[id]=true;initTab(id)}
}
document.querySelectorAll('.tab-btn[data-tab]').forEach(b=>{
  b.addEventListener('click',()=>showTab(b.dataset.tab));
});

function initTab(id){
  if(id==='compare')renderCompares();
  if(id==='sequence')renderSequences();
  if(id==='match')renderMatch();
  if(id==='trapdrill')renderTraps();
  if(id==='bossmode')renderBoss();
  if(id==='chapters')renderChapters();
  if(id==='quiz')renderQuizBatch();
}

// ══════════════════════════════════════════════════════
// FLASHCARD ENGINE
// ══════════════════════════════════════════════════════
let fcDeck=[...Array(FLASHCARDS.length).keys()];
for(let i=fcDeck.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[fcDeck[i],fcDeck[j]]=[fcDeck[j],fcDeck[i]]}
let fcIdx=0,fcCorrect=0;

function renderFC(){
  if(fcIdx>=fcDeck.length){
    document.getElementById('fc-inner').innerHTML='<div class="fc-front" style="position:relative;backface-visibility:visible"><div class="fc-question">All done! Score: '+fcCorrect+' / '+FLASHCARDS.length+'</div><button onclick="resetFC()" style="margin-top:16px;padding:10px 24px;border:1px solid rgba(255,255,255,0.1);background:var(--surface2);color:var(--text);border-radius:var(--radius-sm);cursor:pointer;font-family:var(--font)">Restart</button></div>';
    return;
  }
  const c=FLASHCARDS[fcDeck[fcIdx]];
  document.getElementById('fc-label').textContent=c.ch+' — Click to reveal';
  document.getElementById('fc-q').textContent=c.q;
  document.getElementById('fc-a').textContent=c.a;
  document.getElementById('fc-eli5-text').textContent=c.eli5;
  document.getElementById('fc-inner').classList.remove('flipped','swipe-left','swipe-right');
  document.getElementById('fc-inner').style.transform='';
  document.getElementById('fc-progress').textContent=(fcIdx+1)+' / '+fcDeck.length;
}
function flipCard(){document.getElementById('fc-inner').classList.toggle('flipped')}
function fcRight(){
  fcCorrect++;
  const el=document.getElementById('fc-inner');
  el.classList.add('swipe-right');
  setTimeout(()=>{fcIdx++;renderFC()},300);
}
function fcWrong(){
  fcDeck.push(fcDeck[fcIdx]);
  const el=document.getElementById('fc-inner');
  el.classList.add('swipe-left');
  setTimeout(()=>{fcIdx++;renderFC()},300);
}
function resetFC(){
  fcDeck=[...Array(FLASHCARDS.length).keys()];
  for(let i=fcDeck.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[fcDeck[i],fcDeck[j]]=[fcDeck[j],fcDeck[i]]}
  fcIdx=0;fcCorrect=0;
  document.getElementById('fc-inner').innerHTML='<div class="fc-front"><div class="fc-front-label" id="fc-label"></div><div class="fc-question" id="fc-q"></div></div><div class="fc-back"><div class="fc-answer" id="fc-a"></div><div class="eli5" id="fc-eli5"><span class="callout-label">ELI5</span><span id="fc-eli5-text"></span></div></div>';
  renderFC();
}
renderFC();

// ══════════════════════════════════════════════════════
// QUIZ ENGINE (lazy)
// ══════════════════════════════════════════════════════
let quizRendered=0,quizCorrect=0,quizAnswered=0;
const QUIZ_BATCH=30;
function renderQuizBatch(){
  const container=document.getElementById('quiz-container');
  const end=Math.min(quizRendered+QUIZ_BATCH,QUIZ.length);
  for(let i=quizRendered;i<end;i++){
    const q=QUIZ[i];
    const div=document.createElement('div');div.className='quiz-q';
    div.innerHTML='<div class="quiz-question">'+(i+1)+'. '+esc(q.q)+'</div><div class="quiz-opts">'+
      q.opts.map((o,oi)=>'<div class="quiz-opt" data-qi="'+i+'" data-oi="'+oi+'" onclick="answerQuiz(this,'+i+','+oi+')">'+esc(o)+'</div>').join('')+
      '</div><div class="quiz-explain" data-qi="'+i+'">'+esc(q.explain)+'</div>';
    container.appendChild(div);
  }
  quizRendered=end;
  if(quizRendered<QUIZ.length){
    const sent=document.getElementById('quiz-sentinel');
    const obs=new IntersectionObserver((entries)=>{
      if(entries[0].isIntersecting){obs.disconnect();renderQuizBatch()}
    },{rootMargin:'200px'});
    obs.observe(sent);
  }
}
function answerQuiz(el,qi,oi){
  const opts=document.querySelectorAll('.quiz-opt[data-qi="'+qi+'"]');
  if(el.classList.contains('correct')||el.classList.contains('wrong'))return;
  opts.forEach(o=>o.style.pointerEvents='none');
  const q=QUIZ[qi];
  if(oi===q.ans){el.classList.add('correct');quizCorrect++}
  else{el.classList.add('wrong');opts[q.ans].classList.add('correct')}
  quizAnswered++;
  document.getElementById('quiz-score').textContent=quizCorrect+' / '+quizAnswered;
  const exp=document.querySelector('.quiz-explain[data-qi="'+qi+'"]');
  if(exp)exp.classList.add('show');
}
function resetQuiz(){
  document.getElementById('quiz-container').innerHTML='';
  quizRendered=0;quizCorrect=0;quizAnswered=0;
  document.getElementById('quiz-score').textContent='0 / 0';
  renderQuizBatch();window.scrollTo(0,0);
}

// ══════════════════════════════════════════════════════
// COMPARE ENGINE
// ══════════════════════════════════════════════════════
function renderCompares(){
  const c=document.getElementById('compare-container');
  COMPARES.forEach(cmp=>{
    const div=document.createElement('div');div.className='card cmp-card';
    let grid='<div class="cmp-header feat">Feature</div><div class="cmp-header left">'+esc(cmp.left)+'</div><div class="cmp-header right">'+esc(cmp.right)+'</div>';
    cmp.rows.forEach(r=>{
      grid+='<div class="cmp-cell feat">'+esc(r[0])+'</div><div class="cmp-cell">'+esc(r[1])+'</div><div class="cmp-cell">'+esc(r[2])+'</div>';
    });
    div.innerHTML='<h3>'+esc(cmp.title)+'</h3><div class="cmp-grid">'+grid+'</div>';
    c.appendChild(div);
  });
}

// ══════════════════════════════════════════════════════
// SEQUENCE ENGINE
// ══════════════════════════════════════════════════════
function renderSequences(){
  const c=document.getElementById('sequence-container');
  SEQUENCES.forEach(seq=>{
    const div=document.createElement('div');div.className='card seq-card';
    div.innerHTML='<h3>'+esc(seq.title)+'</h3><div class="seq-steps">'+
      seq.steps.map(s=>'<div class="seq-item"><div class="seq-num">'+s.n+'</div><div class="seq-text">'+s.text+'</div></div>').join('')+'</div>';
    c.appendChild(div);
  });
}

// ══════════════════════════════════════════════════════
// MATCH ENGINE
// ══════════════════════════════════════════════════════
let matchSetIdx=0,matchSelected=null,matchedCount=0;
function renderMatch(){
  if(matchSetIdx>=MATCH_SETS.length)matchSetIdx=0;
  const set=MATCH_SETS[matchSetIdx];
  document.getElementById('match-title').textContent=set.title;
  document.getElementById('match-score').textContent='0 / '+set.pairs.length;
  matchSelected=null;matchedCount=0;
  const wrap=document.getElementById('match-wrap');wrap.innerHTML='';
  const leftCol=document.createElement('div');leftCol.className='match-col';
  const rightCol=document.createElement('div');rightCol.className='match-col';
  // Shuffle right side
  const shuffled=[...set.pairs];
  for(let i=shuffled.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[shuffled[i],shuffled[j]]=[shuffled[j],shuffled[i]]}
  set.pairs.forEach((p,i)=>{
    const btn=document.createElement('button');btn.className='match-btn';btn.textContent=p.a;
    btn.dataset.side='left';btn.dataset.idx=String(i);btn.dataset.key=p.a;
    btn.onclick=()=>matchClick(btn);
    leftCol.appendChild(btn);
  });
  shuffled.forEach((p,i)=>{
    const btn=document.createElement('button');btn.className='match-btn';btn.textContent=p.b;
    btn.dataset.side='right';btn.dataset.idx=String(i);btn.dataset.key=p.a;
    btn.onclick=()=>matchClick(btn);
    rightCol.appendChild(btn);
  });
  wrap.appendChild(leftCol);wrap.appendChild(rightCol);
}
function matchClick(btn){
  if(btn.classList.contains('matched'))return;
  if(!matchSelected){
    matchSelected=btn;btn.classList.add('selected');return;
  }
  if(matchSelected.dataset.side===btn.dataset.side){
    matchSelected.classList.remove('selected');matchSelected=btn;btn.classList.add('selected');return;
  }
  const set=MATCH_SETS[matchSetIdx];
  // Check match
  const leftBtn=matchSelected.dataset.side==='left'?matchSelected:btn;
  const rightBtn=matchSelected.dataset.side==='right'?matchSelected:btn;
  const leftKey=leftBtn.dataset.key;
  const pair=set.pairs.find(p=>p.a===leftKey);
  if(pair&&rightBtn.textContent===pair.b){
    leftBtn.classList.remove('selected');leftBtn.classList.add('matched');
    rightBtn.classList.add('matched');
    matchedCount++;
    document.getElementById('match-score').textContent=matchedCount+' / '+set.pairs.length;
  }else{
    leftBtn.classList.add('wrong');rightBtn.classList.add('wrong');
    setTimeout(()=>{leftBtn.classList.remove('wrong','selected');rightBtn.classList.remove('wrong')},400);
  }
  matchSelected.classList.remove('selected');matchSelected=null;
}
function nextMatchSet(){matchSetIdx++;renderMatch()}

// ══════════════════════════════════════════════════════
// TRAP ENGINE
// ══════════════════════════════════════════════════════
function renderTraps(){
  const c=document.getElementById('trap-container');
  TRAPS.forEach((t,i)=>{
    const div=document.createElement('div');div.className='card trap-card';
    div.innerHTML='<div class="trap-stmt">'+esc(t.stmt)+'</div>'+
      '<div class="trap-controls"><button onclick="revealTrap('+i+')">Reveal</button></div>'+
      '<div class="trap-reveal" id="trap-r-'+i+'"><span class="trap-verdict '+(t.verdict?'true':'false')+'">'+(t.verdict?'TRUE':'FALSE')+'</span>'+
      '<div class="trap-explain">'+esc(t.explain)+'</div></div>';
    c.appendChild(div);
  });
}
function revealTrap(i){document.getElementById('trap-r-'+i).classList.add('show')}

// ══════════════════════════════════════════════════════
// BOSS ENGINE
// ══════════════════════════════════════════════════════
function renderBoss(){
  const c=document.getElementById('boss-container');
  BOSS.forEach((b,i)=>{
    const div=document.createElement('div');div.className='boss-q';
    div.innerHTML='<div class="boss-question">'+(i+1)+'. '+esc(b.q)+'</div>'+
      '<button class="boss-toggle" onclick="bossReveal('+i+')">Reveal Answer</button>'+
      '<div class="boss-answer">'+b.a+'</div>';
    c.appendChild(div);
  });
}
function bossReveal(i){const els=document.querySelectorAll('.boss-answer');if(els[i])els[i].classList.toggle('show')}

// ══════════════════════════════════════════════════════
// CHAPTERS ENGINE
// ══════════════════════════════════════════════════════
function renderChapters(){
  const toc=document.getElementById('chapters-toc');
  const body=document.getElementById('chapters-body');
  Object.entries(CHAPTERS).forEach(([key,ch])=>{
    if(!ch.nodes||ch.nodes.length===0)return;
    // TOC item
    const ti=document.createElement('div');ti.className='toc-item';
    ti.innerHTML=esc(ch.title)+'<span class="toc-qcount">'+ch.nodes.length+'</span>';
    ti.onclick=()=>{
      document.querySelectorAll('.toc-item').forEach(t=>t.classList.remove('active'));
      ti.classList.add('active');
      document.getElementById('ch-'+key).scrollIntoView({behavior:'smooth',block:'start'});
    };
    toc.appendChild(ti);
    // Section
    const sec=document.createElement('div');sec.id='ch-'+key;sec.style.marginBottom='32px';
    let html='<h2 style="font-size:1.4rem;margin-bottom:16px;padding-top:8px">'+esc(ch.title)+'</h2>';
    ch.nodes.forEach(n=>{
      html+='<div class="concept-block card"><div class="concept-header"><span class="pill">'+esc(key)+'</span><h3 style="font-size:1.1rem">'+esc(n.title)+'</h3></div>';
      if(n.subtitle)html+='<div style="font-size:12px;color:var(--text3);margin-bottom:8px">'+esc(n.subtitle)+'</div>';
      if(n.core)html+='<div class="concept-body"><p>'+esc(n.core)+'</p></div>';
      if(n.sections.length>0){
        html+='<div class="concept-sections">';
        n.sections.forEach(s=>{
          html+='<div class="concept-section"><div class="concept-section-label">'+esc(s.label)+'</div><div style="font-size:13px;line-height:1.6;color:var(--text2)">'+esc(s.body)+'</div></div>';
        });
        html+='</div>';
      }
      if(n.warnings.length>0){
        n.warnings.forEach(w=>{
          html+='<div class="trap-note"><span class="callout-label">Exam Trap</span>'+esc(w)+'</div>';
        });
      }
      if(n.mnemonic){
        html+='<div class="mnemonic"><span class="callout-label">Mnemonic</span>'+esc(n.mnemonic)+'</div>';
      }
      html+='</div>';
    });
    sec.innerHTML=html;
    body.appendChild(sec);
  });
}

// ══════════════════════════════════════════════════════
// TIMER ENGINE
// ══════════════════════════════════════════════════════
let timerInterval=null,timerRunning=false,timerStart=0;
function getTimerSpeed(){return parseFloat(document.getElementById('timer-speed').value)}
function updateTimerLabel(){document.getElementById('timer-label').textContent=getTimerSpeed()+'s'}
function toggleTimer(){
  timerRunning=!timerRunning;
  document.getElementById('timer-play').textContent=timerRunning?'⏸':'▶';
  if(timerRunning)startTimer();else stopTimer();
}
function startTimer(){
  stopTimer();timerRunning=true;timerStart=Date.now();
  const fill=document.getElementById('timer-progress-fill');
  timerInterval=setInterval(()=>{
    const elapsed=(Date.now()-timerStart)/1000;
    const pct=Math.min(100,(elapsed/getTimerSpeed())*100);
    fill.style.width=pct+'%';
    if(pct>=100){fill.style.width='0%';timerStart=Date.now();advanceActive()}
  },50);
}
function stopTimer(){clearInterval(timerInterval);timerInterval=null;document.getElementById('timer-progress-fill').style.width='0%'}
function adjustTimer(d){
  const el=document.getElementById('timer-speed');
  el.value=String(Math.max(0.5,Math.min(30,parseFloat(el.value)+d)));
  updateTimerLabel();if(timerRunning){timerStart=Date.now()}
}
function advanceActive(){
  const active=document.querySelector('.view.active')?.id?.replace('tab-','');
  if(active==='flashcards'){fcRight()}
}

// ══════════════════════════════════════════════════════
// KEYBOARD SHORTCUTS
// ══════════════════════════════════════════════════════
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
  const map={f:'flashcards',q:'quiz',x:'compare',s:'sequence',m:'match',t:'trapdrill',b:'bossmode',c:'chapters'};
  if(map[e.key]){showTab(map[e.key]);return}
  if(e.key===' '){flipCard();e.preventDefault()}
  if(e.key==='ArrowRight'){fcRight()}
  if(e.key==='ArrowLeft'){fcWrong()}
  if(e.key==='p'||e.key==='P'){toggleTimer()}
  if(e.key==='+'){adjustTimer(0.5)}
  if(e.key==='-'){adjustTimer(-0.5)}
  if(e.key==='Escape'){document.getElementById('gs-modal').classList.remove('open')}
});
document.getElementById('gs-modal').addEventListener('click',e=>{if(e.target.id==='gs-modal')e.target.classList.remove('open')});

// ══════════════════════════════════════════════════════
// GLOBAL SEARCH
// ══════════════════════════════════════════════════════
let searchIdx=[];
function buildSearchIndex(){
  FLASHCARDS.forEach((f,i)=>searchIdx.push({type:'Flashcard',text:f.q,tab:'flashcards',idx:i}));
  QUIZ.forEach((q,i)=>searchIdx.push({type:'Quiz',text:q.q,tab:'quiz',idx:i}));
  TRAPS.forEach((t,i)=>searchIdx.push({type:'Trap',text:t.stmt,tab:'trapdrill',idx:i}));
}
buildSearchIndex();
function doSearch(query){
  const r=document.getElementById('gs-results');
  if(!query||query.length<2){r.innerHTML='';return}
  const q=query.toLowerCase();
  const results=searchIdx.filter(s=>s.text.toLowerCase().includes(q)).slice(0,20);
  r.innerHTML=results.map(s=>'<div class="gs-result" data-tab="'+s.tab+'"><div class="gs-result-type">'+s.type+'</div><div class="gs-result-text">'+esc(s.text.substring(0,120))+'</div></div>').join('');
  r.querySelectorAll('.gs-result').forEach(function(el){el.onclick=function(){showTab(this.dataset.tab);document.getElementById('gs-modal').classList.remove('open')}});
}

// ── Utility ───────────────────────────────────────────
function esc(s){if(!s)return'';return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
</script>
</body>
</html>`;

// ── Write output ─────────────────────────────────────
fs.writeFileSync('public/index.html', html, 'utf8');
const size = (Buffer.byteLength(html) / 1024).toFixed(0);
console.log(`\\n=== STUDY HUB BUILD COMPLETE ===`);
console.log(`File: public/index.html`);
console.log(`Size: ${size} KB`);
console.log(`─────────────────────────────────`);
console.log(`Content:`);
console.log(`  Flashcards:   ${FLASHCARDS.length}`);
console.log(`  Quiz Qs:      ${QUIZ.length}`);
console.log(`  Comparisons:  ${COMPARES.length}`);
console.log(`  Sequences:    ${SEQUENCES.length}`);
console.log(`  Match Sets:   ${MATCH_SETS.length} (${MATCH_SETS.reduce((a,s)=>a+s.pairs.length,0)} pairs)`);
console.log(`  Trap Drills:  ${TRAPS.length}`);
console.log(`  Boss Mode Qs: ${BOSS.length}`);
console.log(`  Chapters:     ${Object.keys(CHAPTER_MAP).length}`);
console.log(`─────────────────────────────────`);
console.log(`Checks passed: Build complete`);
console.log(`================================`);
