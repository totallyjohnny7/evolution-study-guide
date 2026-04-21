#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate enhanced Exam 3 flashcard HTML section with images + what/why/how/where."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

EXAM3 = Path(__file__).parent / "public" / "exam3_review.html"

# Image helper — use local path or Wikipedia thumbnail URL
L = lambda f: f"/img/fc/{f}"  # local
W = lambda u: u               # wikimedia

IMGS = {
    'geologic_clock': L('ch3_geologic_clock.jpg'),
    'miller_urey':    L('ch3_miller_urey.jpg'),
    'stromatolites':  L('ch3_stromatolites.jpg'),
    'tiktaalik':      L('ch3_tiktaalik.jpg'),
    'three_domains':  L('ch3_three_domains.png'),
    'mass_extinction':L('ch3_mass_extinction.png'),
    'archaeopteryx':  L('ch4_archaeopteryx.jpg'),
    'darwin_finches': L('ch14_darwin_finches.jpg'),
    'lucy':           L('ch17_lucy.jpg'),
    'human_evo':      L('ch17_human_evo.jpg'),
    'neanderthal':    L('ch17_neanderthal.jpg'),
    'sickle_cell':    L('ch18_sickle_cell.jpg'),
    'malaria_map':    L('ch18_malaria_map.jpg'),
    'burgess_shale':  W('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Burgess_Shale_Fossils.jpg/960px-Burgess_Shale_Fossils.jpg'),
    'feathered_dino': W('https://upload.wikimedia.org/wikipedia/commons/f/f9/Sinosauropteryx_prima.jpg'),
    'cladogram':      W('https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Monophyly%2C_paraphyly%2C_polyphyly.svg/960px-Monophyly%2C_paraphyly%2C_polyphyly.svg.png'),
    'mule':           W('https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Asino_Martina_Franca.jpg/960px-Asino_Martina_Franca.jpg'),
    'speciation':     W('https://upload.wikimedia.org/wikipedia/commons/1/17/Speciation.jpg'),
    'pangaea':        W('https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Pangaea_continents.svg/960px-Pangaea_continents.svg.png'),
    'bighorn':        W('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Bighorn_sheep_in_Yellowstone_National_Park.jpg/960px-Bighorn_sheep_in_Yellowstone_National_Park.jpg'),
    'antibiotic_res': W('https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Antibiotic_resistance_mechanisms.jpg/960px-Antibiotic_resistance_mechanisms.jpg'),
    'elephant':       W('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Elephant_Tusks.jpg/960px-Elephant_Tusks.jpg'),
    'peppered_moth':  W('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Biston_betularia.jpg/960px-Biston_betularia.jpg'),
    'out_africa':     W('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Early_migrations_mercator.svg/960px-Early_migrations_mercator.svg.png'),
    'chromosome2':    W('https://upload.wikimedia.org/wikipedia/commons/7/71/Chromosome2_merge.png'),
    'cancer_evo':     W('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Clonal_evolution_and_development_of_tumor_heterogeneity.png/960px-Clonal_evolution_and_development_of_tumor_heterogeneity.png'),
    'myxoma':         W('https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Rabbit_with_Myxomatosis_on_Flat_Holm_island%2C_Wales._September_2013.jpg/960px-Rabbit_with_Myxomatosis_on_Flat_Holm_island%2C_Wales._September_2013.jpg'),
}

IMG_STYLE = 'max-width:100%;max-height:160px;border-radius:8px;margin-top:10px;object-fit:cover;display:block;border:1px solid #2a2a2a'

def img(key, alt=''):
    src = IMGS.get(key,'')
    if not src: return ''
    return f'<img src="{src}" alt="{alt}" loading="lazy" style="{IMG_STYLE}">'

def card(ch, front, back, img_key='', img_alt=''):
    img_html = img(img_key, img_alt) if img_key else ''
    return (
        f'<div class="fc2" data-ch="{ch}" onclick="this.classList.toggle(\'flipped\')">\n'
        f'<div class="fi2">\n'
        f'<div class="ff2"><div class="chip">{ch.upper()}</div>{front}</div>\n'
        f'<div class="fb2"><div class="verdict">Answer</div>{back}{img_html}</div>\n'
        f'</div></div>'
    )

def chapter(ch, color, title_short, title_full, cards_html):
    return (
        f'<div class="fc-chapter" data-ch="{ch}">\n'
        f'<h3 style="color:{color}"><span style="background:{color}">{ch.upper()} • {title_short}</span> {title_full}</h3>\n'
        f'<div class="fc-grid">\n'
        + cards_html +
        f'\n</div></div>'
    )

# ── CH3 — History of Life ────────────────────────────────────────────────────
ch3_cards = [
    card('ch3', "Earth's age — what, how confirmed?",
         "<b>WHAT:</b> ~4.568 billion years. <b>HOW confirmed:</b> Radiometric dating of zircon crystals from Jack Hills, Australia (oldest known minerals on Earth). <b>WHY it matters:</b> Gives deep time for evolution to produce all modern diversity via gradual change.",
         'geologic_clock', 'Geologic time clock'),
    card('ch3', "Radiometric dating — mechanism",
         "<b>WHAT:</b> Measure parent:daughter isotope ratio in a rock. Apply known half-life to calculate elapsed time. <b>HOW:</b> Radioactive parent decays at constant rate into daughter isotope — temperature, pressure, chemistry cannot change this rate. <b>WHY reliable:</b> Decay constant = true clock."),
    card('ch3', "Half-life — definition",
         "<b>WHAT:</b> Time for 50% of parent isotope to decay into daughter. <b>KEY:</b> FIXED — unaffected by temperature, pressure, chemistry, or burial depth. Each isotope has a unique half-life. <b>WHY useful:</b> After N half-lives, (½)ᴺ of original parent remains — gives precise age."),
    card('ch3', "C-14 dating — half-life, range, what it dates",
         "<b>WHAT:</b> Carbon-14 → Nitrogen-14. Half-life = <b>5,730 years</b>. <b>RANGE:</b> Only works on organic (carbon-containing) material &lt;50,000 years old. <b>WHY limited:</b> After 10 half-lives (~57,000 yr) &lt;0.1% of C-14 remains — unmeasurable. <b>CANNOT date dinosaurs</b> (~66 mya). Used for: human remains, charcoal, wood, cloth."),
    card('ch3', "K-Ar dating — half-life + what it dates",
         "<b>WHAT:</b> Potassium-40 → Argon-40. Half-life = <b>1.3 billion years</b>. <b>HOW:</b> Used on VOLCANIC ROCKS (igneous). Argon gas trapped in crystals at solidification. <b>WHY ideal for hominins:</b> East African hominin fossils found between volcanic ash layers — K-Ar dates the ash, sandwiching the fossil in time."),
    card('ch3', "U-Pb dating — half-life + uses",
         "<b>WHAT:</b> Uranium-238 → Lead-206. Half-life = <b>4.5 billion years</b>. <b>USE:</b> Ancient rocks hundreds of millions to billions of years old. Used to date Earth's oldest zircons (4.4 bya). <b>WHY:</b> Long half-life = still measurable parent remaining in ancient rocks."),
    card('ch3', "Why Kelvin was wrong about Earth's age",
         "<b>WHAT:</b> Lord Kelvin calculated ~20–40 million years based on cooling rate. <b>WHY WRONG:</b> He assumed Earth was passively cooling. Didn't know about <b>radioactive decay</b> continuously generating heat from ²³⁸U, ²³²Th, ⁴⁰K in Earth's interior. True age ~4.568 bya — >100× longer than Kelvin estimated."),
    card('ch3', "Prebiotic soup hypothesis — what, where, when",
         "<b>WHAT:</b> Before life existed, Earth's shallow pools/oceans contained organic molecules formed abiotically. <b>WHERE:</b> Reducing atmosphere (CH₄, H₂, NH₃, H₂O; essentially NO O₂). <b>WHEN:</b> ~4.0–3.8 bya. <b>ENERGY:</b> Lightning, UV radiation, volcanic heat drove chemical reactions. <b>RESULT:</b> Formation of amino acids, nucleotides, simple organic molecules."),
    card('ch3', "Miller-Urey experiment (1953) — what it showed",
         "<b>WHO:</b> Stanley Miller + Harold Urey. <b>HOW:</b> Sealed flask with CH₄, H₂, NH₃, H₂O + electric sparks (simulated lightning). <b>RESULT:</b> Within 1 week → 20+ amino acids formed. <b>WHAT IT PROVED:</b> Building blocks of life CAN form abiotically from inorganic chemistry. <b>WHAT IT DID NOT PROVE:</b> Did NOT produce cells, DNA, or actual life — just monomers.",
         'miller_urey', 'Miller-Urey apparatus diagram'),
    card('ch3', "RNA World Hypothesis — what, why, how",
         "<b>WHAT:</b> Hypothesis that RNA was the first self-replicating functional molecule before DNA/protein system evolved. <b>WHY unique:</b> RNA is BIFUNCTIONAL — (1) stores genetic information like DNA, (2) catalyzes reactions like enzymes (ribozymes). <b>HOW it works:</b> Self-replicating RNA → natural selection among RNA variants → most efficient replicators survive. Evidence: ribosomes still use RNA as catalytic core."),
    card('ch3', "Biomarkers — what, when",
         "<b>WHAT:</b> Molecular chemical signatures of life preserved in ancient rocks. Includes: distinctive carbon isotope ratios (¹²C enrichment from photosynthesis), preserved lipids from cell membranes. <b>WHEN:</b> Earliest biomarkers ~3.8–3.5 bya. <b>SIGNIFICANCE:</b> Evidence for life even where fossil preservation failed — complements fossil record."),
    card('ch3', "Stromatolites — what, when, where",
         "<b>WHAT:</b> Layered laminated structures formed by microbial (cyanobacterial) mats trapping and binding sediment. <b>WHEN:</b> Fossil stromatolites date to ~3.45 bya (Pilbara, Western Australia) — oldest morphological evidence of life. <b>WHERE today:</b> Hamelin Pool, Shark Bay, Australia — one of few modern stromatolite communities. <b>SIGNIFICANCE:</b> Cyanobacteria in stromatolites produced the O₂ that changed Earth's atmosphere.",
         'stromatolites', 'Living stromatolites, Shark Bay Australia'),
    card('ch3', "LUCA — what, when, features",
         "<b>WHAT:</b> Last Universal Common Ancestor — the single population from which all life descended. <b>WHEN:</b> ~3.5–3.8 bya. <b>FEATURES inferred:</b> Single-celled, had DNA as genetic material, RNA, ribosomes (ribosomal proteins universally conserved), used ATP for energy, had a lipid membrane. <b>HOW inferred:</b> Comparative genomics finds universal genes shared by bacteria, archaea, and eukaryotes."),
    card('ch3', "Three domains of life — first appearances",
         "<b>BACTERIA:</b> ~3.5 bya (cyanobacteria — produced first O₂). <b>ARCHAEA:</b> Biologically produced methane signals in Australian rocks ~3.5 bya. <b>EUKARYOTES:</b> ~1.8–2.1 bya (fossil eukaryotes in shales). <b>WHY 3 domains:</b> rRNA phylogenetics (Woese 1977) revealed Archaea are as different from Bacteria as from Eukaryotes — not just 'weird bacteria.'",
         'three_domains', 'Three domain tree of life'),
    card('ch3', "Endosymbiotic Theory — what, evidence",
         "<b>WHAT:</b> Mitochondria + chloroplasts originated as free-living bacteria engulfed by a host cell. <b>PROPOSED by:</b> Lynn Margulis (1967). <b>EVIDENCE (4 key):</b> (1) Own circular DNA like bacteria; (2) Double membrane (inner = original bacterial membrane); (3) Reproduce by binary fission; (4) 70S ribosomes like prokaryotes (not 80S like eukaryotic cytoplasm). <b>WHEN:</b> Mitochondria ~1.8 bya, chloroplasts ~1.2 bya."),
    card('ch3', "Great Oxidation Event — what, when, consequence",
         "<b>WHAT:</b> Atmospheric oxygen rose from near-zero to ~2% beginning ~2.4 bya. <b>CAUSE:</b> Cyanobacteria (evolving ~2.6 bya) released O₂ as byproduct of oxygenic photosynthesis. <b>CONSEQUENCE:</b> (1) Killed most anaerobic life (O₂ = toxic to them); (2) Enabled aerobic respiration (~18× more ATP per glucose); (3) Built ozone layer → blocked UV → enabled land colonization billions of years later."),
    card('ch3', "Cambrian Explosion — when, what, why significant",
         "<b>WHEN:</b> ~541–488 mya. <b>WHAT:</b> Rapid appearance of most major animal body plans (arthropods, mollusks, echinoderms, chordates, annelids). <b>WHY rapid:</b> Possibly: rise in O₂ to ~10%, predator-prey arms race, evolution of eyes, ecological opportunity. <b>EVIDENCE:</b> Burgess Shale (505 mya, British Columbia) — 93 species preserved in soft tissue detail.",
         'burgess_shale', 'Burgess Shale fossils 505 million years old'),
    card('ch3', "Devonian Period — key highlights",
         "<b>WHEN:</b> 419–359 mya. <b>NICKNAME:</b> Age of Fishes. <b>KEY EVENTS:</b> (1) Dunkleosteus — 6m armored apex predator fish; (2) <b>Tiktaalik roseae</b> (375 mya) — fish-tetrapod transitional form with elbows, wrists, neck; (3) First tetrapods colonize land ~370 mya; (4) First forests ~385 mya (Archaeopteris). <b>ENDED:</b> Late Devonian extinction ~375 mya — ~75% marine species lost.",
         'tiktaalik', 'Tiktaalik roseae reconstruction — fish-tetrapod transition'),
    card('ch3', "Tiktaalik roseae — why it matters",
         "<b>WHAT:</b> 375 mya fish-tetrapod transitional form from Arctic Canada. <b>PREDICTED by:</b> Phylogenetic analysis — knew transitional form should exist in 375 mya freshwater deposits → searched and found. <b>TRANSITIONAL FEATURES:</b> Fish traits: scales, gills, fins. Tetrapod traits: weight-bearing elbows, bending wrist with wrist bones, neck (no operculum bone), ribs. <b>SIGNIFICANCE:</b> Shows fish-to-land transition in detail."),
    card('ch3', "Permian extinction — when, severity, cause",
         "<b>WHEN:</b> ~252 mya. <b>SEVERITY:</b> ~96% of all species lost — LARGEST mass extinction ('The Great Dying'). <b>CAUSE:</b> Siberian Traps volcanism → massive CO₂ + SO₂ release → global warming, ocean acidification, anoxic oceans. <b>AFTERMATH:</b> ~10 million years for ecosystems to recover; opened ecological space → Age of Reptiles (Mesozoic).",
         'mass_extinction', 'Extinction intensity through geologic time'),
    card('ch3', "K-Pg extinction — when, severity, cause",
         "<b>WHEN:</b> ~66 mya. <b>SEVERITY:</b> ~76% species lost including non-avian dinosaurs. <b>CAUSE:</b> Chicxulub asteroid (~10 km diameter, Yucatán Peninsula) + Deccan Traps volcanism. <b>EVIDENCE:</b> Global iridium layer (iridium rare on Earth, common in asteroids); Chicxulub crater (180 km); fern spore spike (pioneer plant after catastrophe). <b>SURVIVORS:</b> Small mammals, birds (avian dinosaurs), turtles."),
    card('ch3', "Lagerstätte — definition + example",
         "<b>WHAT:</b> Exceptionally preserved fossil deposit where soft tissues are preserved (German: 'storage place'). <b>HOW:</b> Rapid burial in anoxic conditions prevents decay by bacteria. <b>EXAMPLE:</b> Burgess Shale (505 mya, British Columbia) — soft tissues of ~93 species including gut contents, eyes, muscles. <b>WHY priceless:</b> Most fossils = hard parts only; Lagerstätten reveal morphology impossible to infer otherwise."),
    card('ch3', "Geologic period mnemonic",
         "<b>ORDER (oldest to youngest):</b> Cambrian, Ordovician, Silurian, Devonian, Carboniferous, Permian, Triassic, Jurassic, Cretaceous, Paleogene, Neogene, Quaternary.<br><b>MNEMONIC:</b> <i>'Camels Often Sit Down Carefully, Perhaps Their Joints Creak Painfully Near Quitting.'</i><br><b>ERA boundaries:</b> Paleozoic ends at Permian (~252 mya); Mesozoic ends at K-Pg (~66 mya)."),
]

# ── CH4 — Phylogenetics ──────────────────────────────────────────────────────
ch4_cards = [
    card('ch4', "Phylogenetic tree — 5 components defined",
         "<b>TIPS:</b> Living (or fossil) taxa being compared. <b>BRANCHES:</b> Lineages through time. <b>NODES:</b> Speciation events (common ancestors). <b>ROOT:</b> Most recent common ancestor of all taxa shown. <b>CLADE:</b> Node + ALL descendants. <b>WHY it matters:</b> Trees are hypotheses of evolutionary history, not observations — tested with more data."),
    card('ch4', "Sister taxa — definition",
         "<b>WHAT:</b> Two lineages that diverged from the SAME immediate ancestral node. <b>HOW to identify:</b> Share a node not shared with any other taxon in the analysis. <b>KEY:</b> Sister taxa are each other's CLOSEST relatives — most recently diverged. <b>EXAMPLE:</b> Humans and chimps are sister taxa within hominins."),
    card('ch4', "Synapomorphy — definition + why it defines clades",
         "<b>WHAT:</b> A SHARED DERIVED character state — evolved in the common ancestor of a clade and inherited by ALL descendants. <b>WHY it defines clades (not ancestral characters):</b> Ancestral characters (plesiomorphies) are shared by groups with different evolutionary histories → mislead. Only synapomorphies uniquely mark a lineage. <b>EXAMPLE:</b> Hair = synapomorphy of mammals; vertebrae = synapomorphy of vertebrates."),
    card('ch4', "Monophyletic vs. Paraphyletic vs. Polyphyletic",
         "<b>MONOPHYLETIC:</b> Common ancestor + ALL descendants = VALID clade. <b>PARAPHYLETIC:</b> Common ancestor + SOME descendants (some excluded) = INVALID. Example: 'Reptiles' without birds. <b>POLYPHYLETIC:</b> Does NOT include most recent common ancestor of all members = INVALID. Example: 'warm-blooded animals' (birds + mammals separately evolved endothermy).",
         'cladogram', 'Monophyly, paraphyly, polyphyly diagram'),
    card('ch4', "Are 'Reptiles' monophyletic? Why not?",
         "<b>NO — PARAPHYLETIC.</b> 'Reptiles' traditionally = lizards, snakes, turtles, crocs, but EXCLUDES birds. <b>WHY wrong:</b> Crocodilians are MORE closely related to birds than to lizards. Birds ARE avian theropod dinosaurs. <b>FIX:</b> Reptilia must include birds to be monophyletic. <b>Lesson:</b> Common names often reflect appearance, not evolutionary history."),
    card('ch4', "Principle of parsimony",
         "<b>WHAT:</b> Choose the phylogenetic tree requiring the FEWEST evolutionary changes (steps) as the preferred hypothesis. <b>WHY:</b> Extra steps = extra homoplasy assumed — we should minimize unparsimonious assumptions. <b>HOW applied:</b> Count total character state changes on each possible tree; tree with minimum steps is most parsimonious. <b>LIMITATION:</b> Rapid evolution or convergence can mislead parsimony (long-branch attraction)."),
    card('ch4', "Homoplasy — definition + 2 types",
         "<b>WHAT:</b> Similarity NOT due to shared ancestry. <b>TYPE 1 — Convergent evolution:</b> Same trait evolves independently via DIFFERENT developmental/genetic mechanisms (e.g., camera eye in vertebrates vs. octopus — same structure, different embryonic origin). <b>TYPE 2 — Evolutionary reversal:</b> Derived character reverts to ancestral state (e.g., limblessness in snakes — tetrapod ancestor lost limbs). <b>WHY problematic:</b> Can mislead phylogenetic analysis."),
    card('ch4', "Homology vs. homoplasy — examples",
         "<b>HOMOLOGY:</b> Similarity due to SHARED ANCESTRY. Human arm bones = whale flipper bones = bat wing bones — all modified from same tetrapod forelimb (different function, same bones). <b>HOMOPLASY:</b> Dolphin streamlined body vs. shark streamlined body — similar shape via DIFFERENT evolutionary paths (mammals vs. fish). <b>TEST:</b> Homologs have same embryonic origin; analogs do not."),
    card('ch4', "Convergent vs. parallel evolution",
         "<b>CONVERGENT:</b> Different genetic/developmental mechanisms in distantly related organisms produce similar phenotype. Example: camera eyes in vertebrates vs. octopus (different genes, different embryology). <b>PARALLEL:</b> SAME genetic pathway in closely related organisms. Example: loss of armor plates in multiple freshwater stickleback populations — same Pitx1 gene each time. <b>KEY distinction:</b> Mechanism, not just outcome."),
    card('ch4', "Exaptation — definition + feather example",
         "<b>WHAT:</b> Trait that evolved for function A later co-opted for function B. <b>FEATHERS:</b> Evolved in non-flying theropod dinosaurs (Velociraptor had feather quill nodes; arms too short for flight). Original functions: insulation, species recognition, display, egg incubation. Flight was a LATER exaptation. <b>OTHER example:</b> Fish swim bladder (ancestral lung) → buoyancy organ in bony fishes.",
         'feathered_dino', 'Sinosauropteryx — earliest known feathered dinosaur'),
    card('ch4', "Feathers — did they evolve FOR flight?",
         "<b>NO — classic exaptation.</b> Fossil evidence (Sinosauropteryx, Velociraptor, Anchiornis) shows feathers in non-flying theropods. Velociraptor's arms were too short to generate lift. Feathers predate flight by tens of millions of years. <b>Original functions:</b> Insulation (found on small body dinosaurs that lose heat fast), display, brooding eggs. <b>Archaeopteryx</b> (150 mya) = earliest known flying bird.",
         'archaeopteryx', 'Archaeopteryx lithographica — Berlin specimen, 150 mya'),
    card('ch4', "Cladistics — what, who, how",
         "<b>WHAT:</b> Phylogenetic classification method using ONLY shared derived characters (synapomorphies) to build trees. <b>WHO:</b> Developed by Willi Hennig (1966). <b>HOW:</b> (1) Identify character states; (2) Determine ancestral vs. derived states (using outgroup comparison); (3) Group by synapomorphies; (4) Apply parsimony. <b>WHY preferred:</b> Produces strictly monophyletic groupings."),
    card('ch4', "Outgroup comparison — what, why",
         "<b>WHAT:</b> Compare in-group taxa to an outgroup (a taxon outside the group of interest) to determine which character state is ancestral vs. derived. <b>HOW:</b> Character state shared with outgroup = ANCESTRAL (plesiomorphy). Character state unique to in-group = DERIVED (apomorphy). <b>WHY essential:</b> Cannot identify synapomorphies without knowing which state is ancestral."),
    card('ch4', "Molecular phylogenetics — what sequences used",
         "<b>WHAT:</b> Build phylogenies using DNA/RNA/protein sequences instead of morphology. <b>MOLECULES used:</b> rRNA genes (highly conserved — good for deep phylogeny, e.g., 3 domains); mitochondrial DNA (fast-evolving — good for recent divergences, population-level); nuclear protein-coding genes; whole genomes. <b>WHY powerful:</b> Overcomes morphological convergence; provides thousands of independent characters."),
    card('ch4', "Phylogeography — definition",
         "<b>WHAT:</b> Study of the geographic distributions of genealogical lineages within and among species. <b>HOW:</b> Integrates phylogenetics + biogeography. <b>QUESTIONS asked:</b> Did populations separate by vicariance (barrier formed) or dispersal (organisms moved)? Do phylogenetic patterns match geographic patterns? <b>EXAMPLE:</b> Hawaiian island chain phylogeny mirrors island age (youngest island = most recently colonized populations)."),
    card('ch4', "Bootstrap support — what it measures",
         "<b>WHAT:</b> Statistical measure of confidence in a node (clade) in a phylogenetic tree. <b>HOW:</b> Resample data randomly with replacement hundreds of times; rebuild tree each time; count what % of resampled trees contain the same node. <b>INTERPRETATION:</b> Bootstrap value ≥70% = moderately supported; ≥95% = strongly supported. <b>WHY:</b> Tells you how reproducible a node is — low bootstrap = node sensitive to data subset."),
]

# ── CH13 — Speciation ────────────────────────────────────────────────────────
ch13_cards = [
    card('ch13', "Biological Species Concept (BSC) — definition + 3 failures",
         "<b>WHAT (Mayr 1942):</b> Groups of interbreeding natural populations reproductively isolated from other such groups. <b>FAILS for:</b> (1) Fossils — can't test gene flow in extinct taxa; (2) Asexual species — bacteria, archaea, many plants reproduce without sex; (3) Hybridizing species — lions × tigers produce ligers; many plant species freely hybridize. <b>STRENGTH:</b> Gene flow = evolutionary unit — biologically meaningful."),
    card('ch13', "Morphospecies Concept — definition + failure",
         "<b>WHAT:</b> Species defined by measurable morphological differences from all other species. <b>STRENGTHS:</b> Works for fossils; fast field identification. <b>FAILS for:</b> (1) Cryptic species — look identical but genetically distinct (e.g., mosquitoes in Anopheles gambiae complex); (2) Phenotypically plastic species — same genotype produces very different morphologies in different environments. <b>USE:</b> Most museum taxonomy + fossil record."),
    card('ch13', "Phylogenetic Species Concept (PSC) — definition",
         "<b>WHAT (Cracraft):</b> Smallest monophyletic group sharing a unique combination of character states (synapomorphies). <b>STRENGTHS:</b> Works for asexual and sexual organisms; works for fossils; theoretically clean. <b>FAILS for:</b> (1) Requires established phylogeny (not always available); (2) Over-splits — defines many more 'species' than BSC → management/conservation complications. <b>IMPLICATION:</b> PSC species are often subspecies under BSC."),
    card('ch13', "General Lineage Species Concept",
         "<b>WHAT (de Queiroz):</b> Species = independently evolving metapopulation lineages. Unifying concept — all other species concepts detect different properties of the same underlying lineage separation. <b>KEY INSIGHT:</b> Speciation is a process (gradual), not an event — different criteria (gene flow, morphology, diagnosis) reach the same conclusion at different points in the process. <b>USE:</b> Academic synthesis; explains why species concepts disagree."),
    card('ch13', "3 steps of speciation (+ reinforcement)",
         "<b>STEP 1:</b> Barrier to gene flow forms (geographic, behavioral, ecological, temporal). <b>STEP 2:</b> Populations diverge genetically via mutation, drift, and/or natural selection. <b>STEP 3:</b> Reproductive isolation evolves as byproduct of divergence (Bateson-Dobzhansky-Muller incompatibilities). <b>STEP 4 (if secondary contact):</b> Reinforcement — natural selection strengthens prezygotic barriers if hybrids have low fitness.",
         'speciation', 'Modes of speciation diagram'),
    card('ch13', "Prezygotic barriers — pre-mating (3 types)",
         "<b>1. Habitat isolation:</b> Same region but different microhabitats — populations don't encounter each other. Example: Rhagoletis on hawthorn vs. apple. <b>2. Temporal isolation:</b> Different breeding/flowering times. Example: hummingbird plants staggering flowering phenology. <b>3. Behavioral isolation:</b> Different mate-recognition signals, courtship displays, mating calls. Example: firefly flash patterns species-specific."),
    card('ch13', "Prezygotic barriers — post-mating pre-fertilization (2 types)",
         "<b>4. Mechanical isolation:</b> Physical incompatibility of reproductive structures — flower shape + pollinator mismatch. <b>5. Gametic incompatibility:</b> Sperm/pollen physically fails to reach or penetrate egg — species-specific surface proteins prevent fertilization even after mating. Example: sea urchin bindin protein (Strongylocentrotus) — diverges rapidly between species."),
    card('ch13', "Postzygotic barriers — 2 types",
         "<b>6. Hybrid inviability:</b> Hybrid embryo forms but developmental incompatibilities cause death before reproductive age (Bateson-Dobzhansky-Muller incompatibilities). <b>7. Hybrid sterility:</b> Hybrids survive and are healthy BUT cannot reproduce. Example: MULE (horse 2n=64 × donkey 2n=62 = mule 2n=63). Odd chromosome number → meiosis fails → sterile. Horse + donkey gene pools cannot merge.",
         'mule', 'Mule — horse × donkey hybrid (sterile)'),
    card('ch13', "Bateson-Dobzhansky-Muller (BDM) incompatibilities",
         "<b>WHAT:</b> Two alleles that evolved independently in two isolated populations are INCOMPATIBLE when combined in a hybrid — cause inviability or sterility. <b>HOW:</b> Allele A₁B₂ works fine; A₂B₁ works fine in isolation. Hybrid A₁B₁ or A₂B₂ combination = developmental failure. <b>WHY happens:</b> Each allele is fine in its own genetic background but epistatic interactions go wrong in the hybrid's novel combination."),
    card('ch13', "Reinforcement — definition, mechanism, result",
         "<b>WHAT:</b> Natural selection STRENGTHENS prezygotic barriers when populations meet in secondary contact and produce low-fitness hybrids. <b>MECHANISM:</b> Individuals that avoid mating with the other species waste no gametes on failed offspring → higher fitness → alleles for stronger prezygotic barriers spread. <b>RESULT:</b> Prezygotic isolation increases over time. <b>EVIDENCE:</b> More pronounced mating signal differences between sympatric than allopatric populations (reproductive character displacement)."),
    card('ch13', "Allopatric speciation — steps, examples",
         "<b>WHAT:</b> Speciation with geographic isolation. <b>STEPS:</b> (1) Geographic barrier forms OR colonization of new area; (2) Gene flow stops; (3) Divergence via drift + selection; (4) Reproductive isolation evolves. <b>EXAMPLES:</b> Darwin's finches (dispersal to Galápagos); Snapping shrimp separated by Panama Isthmus 3.5 mya; Hawaiian Laupala crickets (island-hopping, matches island age sequence)."),
    card('ch13', "Sympatric speciation — definition, example",
         "<b>WHAT:</b> New species evolves WITHIN the same geographic area as ancestor WITHOUT geographic isolation. <b>EXAMPLE — Rhagoletis pomonella:</b> Apple maggot fly shifted from native hawthorn to introduced apple trees ~140 years ago. Host plant = (1) mating site (assortative mating by host), (2) different developmental timing (temporal isolation), (3) different selection pressures. <b>KEY:</b> Ecological divergence alone can produce reproductive isolation."),
    card('ch13', "Vicariance vs. dispersal — what, difference",
         "<b>VICARIANCE:</b> Organisms STAY PUT — a barrier FORMS and splits their range (e.g., Panama Isthmus rising 3.5 mya splits Atlantic/Pacific snapping shrimp populations). <b>DISPERSAL (founder event):</b> A SUBSET of organisms MOVES to a new area (e.g., a hawk flies to a new island and founds a population). <b>KEY distinction:</b> In vicariance, both daughter populations large; in dispersal, founder population small → strong genetic drift."),
    card('ch13', "Allopolyploidy — instant speciation, how",
         "<b>WHAT:</b> Hybridization between two species + genome duplication = new allopolyploid species instantly reproductively isolated from both parents. <b>HOW it isolates:</b> Allopolyploid has double the chromosomes → when it tries to cross back with either parent → odd ploidy → meiosis fails → sterile hybrids. <b>FREQUENCY:</b> ~70–80% of flowering plant species are polyploids. <b>EXAMPLE:</b> Bread wheat: hexaploid (6n=42) from 3 ancestral grasses.",
         ),
    card('ch13', "Allopolyploidy — real-time examples",
         "<b>Tragopogon:</b> Two allopolyploid species (T. mirus, T. miscellus) formed in Pacific Northwest within ~80 years after European grasses were introduced — observed speciation in real time. <b>Bread wheat (Triticum aestivum):</b> Emmer wheat (4n) × Aegilops (2n) → 6n hexaploid ~8,000 years ago. <b>WHY plants:</b> Animals rarely tolerate polyploidy because sex determination systems break down."),
    card('ch13', "Haldane's Rule",
         "<b>WHAT:</b> When one sex of hybrid offspring is inviable or sterile, it is almost always the HETEROGAMETIC sex (XY males in mammals; ZW females in birds/butterflies). <b>WHY:</b> Recessive BDM incompatibility alleles on the X (or Z) chromosome are EXPOSED in hemizygous XY males (no second X to mask them). XX females have a backup allele. <b>PREDICTION:</b> BDM incompatibility genes accumulate on sex chromosomes disproportionately."),
    card('ch13', "Parapatric speciation",
         "<b>WHAT:</b> Populations have PARTIAL geographic separation; gene flow occurs in a narrow contact zone. <b>HOW speciation occurs:</b> Selection gradients stronger than gene flow → divergence despite some hybridization. <b>EXAMPLE:</b> Anthoxanthum odoratum grass populations at mine boundary — populations separated by &lt;1 meter but heavy metal tolerance diverges; different flowering times evolve → temporal isolation."),
    card('ch13', "Peripatric speciation (founder effect speciation)",
         "<b>WHAT:</b> Subset of allopatric speciation — a tiny founder population colonizes a new, isolated habitat. <b>KEY:</b> Small founder size → strong genetic drift; new alleles can fix rapidly regardless of fitness in original environment. <b>EXAMPLE:</b> Hawaiian islands — each colonization event = new founder population. Hawaiian honeycreepers: 1 founder species → ~50+ species. <b>WHY rapid:</b> Drift + new selective environment accelerate divergence."),
    card('ch13', "Hawaiian Laupala crickets — what they demonstrate",
         "<b>37 endemic species</b> on Hawaiian archipelago. <b>PHYLOGENY mirrors island age:</b> Oldest populations on oldest island (Kauai ~5 mya), youngest on Big Island (&lt;1 mya). <b>DISPERSAL model confirmed:</b> Colonized sequentially from older to younger islands (not vicariance — islands formed independently). <b>MECHANISM:</b> Each island colonization = new founder population → peripatric speciation. <b>RATE:</b> ~4× faster than insular Drosophila."),
    card('ch13', "Ecological speciation — what, why important",
         "<b>WHAT:</b> Speciation driven directly by natural selection due to adaptation to different ecological environments — no geographic isolation required. <b>HOW:</b> Different ecological niches → different selective regimes → different traits → assortative mating by habitat/resource → reproductive isolation as byproduct. <b>RHAGOLETIS example:</b> Hawthorn vs. apple host plant = different timing, morphology, behavior → mating isolation within same range. <b>WHY important:</b> Shows ecology drives species formation."),
]

# ── CH14 — Biogeography ──────────────────────────────────────────────────────
ch14_cards = [
    card('ch14', "Biogeography — definition",
         "<b>WHAT:</b> Study of spatial and temporal distribution of biodiversity — WHERE organisms live and WHY. <b>INTEGRATES:</b> Biology, geology, geography, paleontology, evolution. <b>FOUNDED by:</b> Darwin and Wallace (independently, 1850s). <b>KEY TOOLS:</b> Vicariance analysis, dispersal modeling, phylogeography. <b>FUNDAMENTAL QUESTION:</b> Are distribution patterns explained by organisms moving (dispersal) or barriers forming around stationary organisms (vicariance)?"),
    card('ch14', "Continental drift — Pangaea timeline",
         "<b>WHAT:</b> Earth's continents move (plate tectonics). <b>PANGAEA:</b> Supercontinent assembled ~300 mya, began breaking up ~200 mya. <b>KEY SPLITS:</b> N. America / Eurasia separated ~80 mya; S. America isolated ~65 mya; India-Asia collision ~55 mya (formed Himalayas); Australia separated from Antarctica ~35 mya. <b>WHY matters:</b> Explains disjunct distributions — marsupials in Australia + S. America (both Gondwanan lineages).",
         'pangaea', 'Pangaea supercontinent ~250 million years ago'),
    card('ch14', "Vicariance biogeography — principle",
         "<b>WHAT:</b> Organisms in a continuous population are SEPARATED by a geological or climatic barrier forming BETWEEN them → two daughter populations. <b>PREDICTION:</b> Phylogeny of separated populations should MATCH the sequence of barrier formation. <b>EXAMPLE:</b> Snapping shrimp (Alpheus): 15+ species pairs separated by Panama Isthmus (formed 3.5 mya) — shrimp species diverged ~3.5 mya. Isthmus age = speciation age."),
    card('ch14', "Dispersal biogeography — principle",
         "<b>WHAT:</b> Organisms MOVE from their origin to a new area — usually rare 'sweepstakes' events across barriers. <b>EVIDENCE for:</b> Phylogeny shows dispersal direction (e.g., New World monkeys — closest relative in Africa, must have crossed Atlantic ~35 mya on floating vegetation mats). <b>HOW distinguished from vicariance:</b> In dispersal, only 1 lineage crosses; in vicariance, related populations on both sides of barrier."),
    card('ch14', "Island biogeography — MacArthur & Wilson equilibrium theory",
         "<b>THEORY (1967):</b> Species richness on islands is an EQUILIBRIUM between immigration rate and extinction rate. <b>IMMIGRATION:</b> Decreases as species richness increases (fewer new species available to colonize). <b>EXTINCTION:</b> Increases as species richness increases (more competition, smaller populations). <b>EQUILIBRIUM:</b> Where immigration rate = extinction rate. <b>PREDICTION:</b> Larger islands and closer-to-mainland islands have MORE species."),
    card('ch14', "Island biogeography — distance + area effects",
         "<b>DISTANCE effect:</b> Islands closer to mainland have HIGHER immigration rate → higher equilibrium species richness. Each km of ocean reduces probability of successful colonization. <b>AREA effect:</b> Larger islands support LARGER populations → lower extinction rate; also more habitat diversity → more niches. <b>SPECIES-AREA RELATIONSHIP:</b> S = cA^z (where z ≈ 0.20–0.35 for most taxa). Doubling island area increases species ~15%."),
    card('ch14', "Adaptive radiation — what, conditions, examples",
         "<b>WHAT:</b> Rapid diversification of one lineage into many ecologically different species — exploiting new resources or habitats. <b>CONDITIONS:</b> (1) Access to new ecological opportunity (after extinction, colonizing new island, key innovation); (2) Low competition from other lineages. <b>EXAMPLES:</b> Darwin's finches (Galápagos — 1 ancestor → 13+ species); Hawaiian honeycreepers (1 ancestor → 50+ species); mammals (post K-Pg — rapid diversification in 10 mya).",
         'darwin_finches', 'Darwin\'s finches by Gould — adaptive radiation example'),
    card('ch14', "Wallace Line — what, significance",
         "<b>WHAT:</b> Biogeographic boundary between Asian and Australasian fauna running between Bali/Lombok and Borneo/Sulawesi (discovered by Alfred Russel Wallace, 1859). <b>WHY persists:</b> Deep ocean trench between islands — persisted even when sea levels dropped 120m during ice ages → never a land bridge. <b>WEST:</b> Asian fauna (primates, deer, tigers, Asian birds). <b>EAST:</b> Australian fauna (marsupials, cockatoos, birds of paradise). <b>SIGNIFICANCE:</b> Demonstrates how water barriers maintain faunal boundaries."),
    card('ch14', "Species-area relationship (SAR)",
         "<b>EQUATION:</b> S = cA^z, where S = species richness, A = area, c = taxa-specific constant, z = slope (~0.20–0.35). <b>PRACTICAL USE:</b> Predict species loss from habitat destruction — if 90% of habitat is lost (A reduced to 10%), species richness drops to ~50% (using z=0.30: 0.1^0.3 = 0.5). <b>APPLICATION:</b> Conservation — minimum reserve size to maintain species richness; predicts extinction debt from fragmentation."),
    card('ch14', "Species-area relationship — habitat fragmentation consequences",
         "<b>WHAT:</b> Habitat fragmentation creates 'islands' of suitable habitat in a 'sea' of unsuitable matrix. <b>CONSEQUENCES:</b> (1) Smaller patches → fewer species (SAR); (2) Reduced immigration between patches → higher extinction; (3) Edge effects increase (altered microclimate at habitat edges); (4) Inbreeding depression in small isolated populations. <b>SOLUTION:</b> Wildlife corridors connect patches → restore immigration → slow extinction."),
    card('ch14', "Metapopulation dynamics",
         "<b>WHAT:</b> A population of populations — subpopulations in distinct patches connected by dispersal. <b>KEY DYNAMICS:</b> Local extinction and recolonization are normal. As long as recolonization rate &gt; extinction rate, metapopulation persists even if individual patches go extinct. <b>RESCUE EFFECT:</b> Immigration from other patches can prevent local extinction (genetic + demographic). <b>WHO:</b> Levins (1969). <b>EXAMPLE:</b> Bay checkerspot butterfly (Euphydryas editha bayensis)."),
    card('ch14', "Conservation genetics — 50/500 rule",
         "<b>WHAT:</b> Rule of thumb for minimum population sizes. <b>50 rule:</b> Ne ≥ 50 to avoid immediate inbreeding depression (lose ~1% heterozygosity per generation). <b>500 rule:</b> Ne ≥ 500 to maintain evolutionary potential long-term (mutation input ≈ drift loss). <b>NOTE:</b> Ne (effective) = usually 10–25% of census population N. <b>LIMITATION:</b> Some argue 5,000 needed for long-term viability in changing environments."),
    card('ch14', "Inbreeding depression — mechanism",
         "<b>WHAT:</b> Reduced fitness in offspring of closely related parents. <b>MECHANISM:</b> Inbreeding increases homozygosity → previously masked recessive deleterious alleles become homozygous → expressed as defects. <b>ALSO:</b> Overdominance (heterozygote advantage) lost when alleles become homozygous. <b>EXAMPLES:</b> Florida panther (skull defects, cryptorchidism from inbreeding). <b>FIX:</b> Gene flow from other populations — even one migrant per generation reduces inbreeding depression."),
    card('ch14', "Area phylogeny — what it is",
         "<b>WHAT:</b> A cladogram where tips are geographic AREAS (not taxa). Built by replacing taxon names with their geographic locations in a phylogenetic tree. <b>PURPOSE:</b> Detect shared historical biogeographic patterns across multiple lineages — if fish, insects, and plants in region A all show same vicariance pattern relative to region B, it implies a common historical barrier between A and B. <b>USE:</b> Distinguish vicariance (repeated pattern) from dispersal (idiosyncratic pattern)."),
    card('ch14', "Phylogeography — definition",
         "<b>WHAT (Avise 1987):</b> Study of principles and processes governing geographic distributions of genealogical lineages within and among closely related species. <b>HOW:</b> Build gene tree from DNA sequences of individuals across their range; map on geography. <b>QUESTIONS:</b> Do different parts of range have different lineages? Did populations expand post-ice age? Where did glacial refugia exist? <b>EXAMPLE:</b> North American trees have S. Appalachian refugia lineages — survived ice ages there."),
    card('ch14', "Gondwana vs. Laurasia — what each contained",
         "<b>GONDWANA (southern Pangaea):</b> South America, Africa, Antarctica, Australia, India, Madagascar. After breakup: explains why marsupials in S. America + Australia (both Gondwanan); why ratites (ostrich, emu, rhea) on separate southern continents. <b>LAURASIA (northern Pangaea):</b> North America, Europe, Asia. After breakup: explains why N. American + Eurasian mammals closely related (land bridges persisted longer). <b>SPLIT:</b> ~200 mya."),
]

# ── CH8 — Humans as Selective Force ─────────────────────────────────────────
ch8_cards = [
    card('ch8', "Humans as selective force — 4 key examples",
         "<b>1. Trophy hunting</b> (bighorn sheep, African elephants) — selects AGAINST large traits. <b>2. Fishing</b> (Atlantic cod) — selects for smaller, younger maturation. <b>3. Antibiotic/pesticide use</b> — selects for resistance. <b>4. Habitat change</b> (peppered moth industrial melanism) — changes cryptic coloration selection. <b>WHY matters:</b> Humans are the dominant selective force on Earth — evolutionary consequences have practical implications for conservation and medicine."),
    card('ch8', "Trophy hunting evolution — bighorn sheep example",
         "<b>WHAT:</b> Trophy hunters selectively kill LARGE-horned rams (most desirable trophies). <b>EVOLUTIONARY RESULT:</b> This is artificial selection IN REVERSE — removes genes for large horns from population. <b>DATA:</b> Ram horn size in Ram Mountain, Alberta DECLINED ~20% in 30 years (Coltman et al. 2003). Heritable horn size selected AGAINST by hunting. <b>KEY:</b> Demonstrates evolution is occurring RIGHT NOW under human pressure.",
         'bighorn', 'Bighorn sheep — trophy hunting drives horn size reduction'),
    card('ch8', "Tusklessness in African elephants",
         "<b>WHAT:</b> In heavily poached populations, proportion of tuskless female elephants has increased dramatically. <b>MECHANISM:</b> Poachers target elephants WITH tusks → tuskless individuals survive and reproduce → tuskless allele increases in frequency. <b>DATA:</b> Gorongosa NP (Mozambique) — proportion of tuskless females rose from ~18% pre-war to ~51% post-civil war (heavy poaching). <b>GENETIC:</b> Tusklessness linked to X chromosome — heterozygous females tuskless; hemizygous males lethal.",
         'elephant', 'Elephant tusks — poaching selects for tusklessness'),
    card('ch8', "Antibiotic resistance — how it evolves",
         "<b>MECHANISM:</b> (1) Random mutations create resistance alleles in bacterial population (pre-exist before antibiotic exposure). (2) Antibiotic kills susceptible cells — resistant cells survive and reproduce. (3) Resistance alleles increase in frequency via selection. (4) Resistant cells may transfer R-plasmids to other cells (horizontal gene transfer). <b>KEY:</b> Antibiotics do NOT cause mutations — they SELECT for pre-existing resistance."),
    card('ch8', "4 mechanisms of antibiotic resistance",
         "<b>1. Efflux pumps:</b> Protein pumps in cell membrane actively expel antibiotic out of cell. <b>2. Enzymatic degradation:</b> Enzyme breaks down antibiotic (e.g., β-lactamase destroys penicillin). <b>3. Target modification:</b> Change the target protein so antibiotic no longer binds (e.g., modified ribosome). <b>4. Reduced permeability:</b> Alter cell membrane porins to block antibiotic entry.",
         'antibiotic_res', 'Four mechanisms of antibiotic resistance'),
    card('ch8', "Atlantic cod — fishing-driven evolution",
         "<b>WHAT:</b> Industrial fishing removes largest, oldest cod. <b>EVOLUTIONARY CONSEQUENCE:</b> Selection for SMALLER body size and YOUNGER age at maturity over 30+ years. <b>DATA:</b> Average age at maturation in Atlantic cod declined from ~6 years (1970s) to ~4 years (2000s). Body size declined ~30%. <b>WHY dangerous:</b> Smaller, younger fish = less reproductive output per individual. Even if fishing stopped, evolutionary change persists. <b>EVIDENCE it's evolution:</b> Changes maintained across generations + heritable."),
    card('ch8', "Industrial melanism — peppered moth",
         "<b>WHAT:</b> Biston betularia (peppered moth) exists in light-speckled and dark melanic forms. <b>PRE-INDUSTRIAL:</b> Light form cryptic on lichen-covered trees; dark form rare (conspicuous to birds). <b>INDUSTRIAL REVOLUTION:</b> Pollution killed lichens; soot blackened tree bark → dark form now cryptic. Dark form rose to 90%+ in industrial areas by 1900. <b>AFTER CLEAN AIR ACTS:</b> Dark form declined as pollution reduced, lichens returned. <b>GENETICS:</b> Single gene (cortex) controls morph.",
         'peppered_moth', 'Peppered moth — industrial melanism on tree bark'),
    card('ch8', "Habitat fragmentation + genetic consequences",
         "<b>WHAT:</b> Human land use fragments continuous habitat into isolated patches. <b>GENETIC EFFECTS:</b> (1) Reduced effective population size → more genetic drift → loss of heterozygosity; (2) Reduced gene flow between patches → inbreeding depression; (3) Loss of evolutionary potential (fewer alleles). <b>REAL EXAMPLE:</b> Florida panther: severe inbreeding depression (heart defects, cryptorchidism, kinked tail). FIXED by importing Texas pumas — rescued genetic diversity."),
    card('ch8', "Selective breeding vs. natural selection",
         "<b>SELECTIVE BREEDING:</b> Humans choose which individuals reproduce based on desired traits → same mechanism as natural selection but humans control who reproduces. <b>RATE:</b> Much faster than natural selection (can select one trait intensely each generation). <b>CONSEQUENCES:</b> Extreme phenotypes with fitness costs (bulldogs: breathing problems; dairy cows: mastitis). <b>KEY:</b> Artificial selection demonstrates evolution is real and fast when selection is strong — same mechanism Darwin used as evidence for natural selection."),
    card('ch8', "Why fishing-driven evolution is real evolution, not plasticity",
         "<b>QUESTION:</b> Maybe fish just grow slower because of overfishing (less food = smaller fish = phenotypic plasticity)? <b>EVIDENCE it's GENETIC:</b> (1) Common garden experiments — raised fish from fished vs. unfished populations under IDENTICAL conditions; fished populations still maturate younger and smaller. (2) Changes maintained in captive populations across generations. (3) Heritability studies confirm traits are heritable. <b>LESSON:</b> Must distinguish phenotypic plasticity from genetic evolution."),
]

# ── CH17 — Human Evolution ───────────────────────────────────────────────────
ch17_cards = [
    card('ch17', "Why Linnaeus classified humans as primates",
         "<b>WHAT:</b> Carolus Linnaeus (1758) placed Homo sapiens in Order Primates in Systema Naturae. <b>CRITERIA used (morphology):</b> Forward-facing eyes, fingernails (not claws), five digits, complex brain, social behavior. <b>SIGNIFICANCE:</b> First formal scientific classification acknowledging human kinship with apes. <b>NOW confirmed by:</b> Molecular data — humans share ~98.8% DNA identity with chimpanzees, ~98.4% with bonobos."),
    card('ch17', "Molecular evidence of human-chimp kinship",
         "<b>DNA similarity:</b> 98.8% sequence identity (coding regions). <b>Shared ERVs:</b> Identical endogenous retrovirus insertions at same genomic locations (ERVs = retroviruses that integrated into germline — must share ancestor that was infected). <b>Chromosome 2 fusion:</b> Human chr 2 = fusion of two ancestral chromosomes (still separate in chimps). <b>Protein similarity:</b> Cytochrome c: 100% identical; hemoglobin: 99% identical. <b>CONCLUSION:</b> Shared ancestry is overwhelming.",
         'chromosome2', 'Human chromosome 2 = fusion of two ancestral primate chromosomes'),
    card('ch17', "Did humans evolve FROM chimpanzees? Why not?",
         "<b>NO — common MISCONCEPTION.</b> Humans and chimps share a COMMON ANCESTOR that was NEITHER modern human NOR modern chimp. Chimps have been evolving just as long as humans have. Saying 'humans evolved from chimps' is like saying you descended from your cousin rather than from your shared grandparent. <b>ANALOGY:</b> Humans and chimps are sister lineages — both descended from an unknown ancestral ape ~6–7 mya."),
    card('ch17', "Sahelanthropus tchadensis — key features",
         "<b>WHEN:</b> ~7 mya (Chad, Central Africa). <b>WHY important:</b> Possibly EARLIEST known hominin. <b>KEY features:</b> Small canine teeth (reduced like hominins); foramen magnum positioned anteriorly (suggests upright posture); small brain (~360 cc). <b>CONTROVERSY:</b> Some scientists argue it was quadrupedal and not a hominin based on femur morphology. <b>SIGNIFICANCE:</b> If correctly classified = pushes human-chimp split toward 7 mya."),
    card('ch17', "Ardipithecus ramidus — key features",
         "<b>WHEN:</b> ~4.4 mya (Ethiopia). <b>KEY features:</b> Walked upright (bipedal pelvis + femur) BUT retained grasping big toe (could climb trees). Brain ~300–350 cc. Small, ape-like canines. <b>SIGNIFICANCE:</b> Before Lucy — shows early hominins were bipedal BEFORE large brains evolved. Bipedalism preceded encephalization. Overturns 'knuckle-walking ancestor' model."),
    card('ch17', "Australopithecus — key facts",
         "<b>WHEN:</b> ~4.2–1.9 mya (Africa). <b>BRAIN:</b> 420–550 cc (larger than apes, smaller than Homo). <b>BIPEDAL:</b> Yes — Laetoli footprints (3.6 mya, Tanzania) show bipedal gait. <b>ARMS:</b> Long arms + curved fingers — still climbed trees. <b>MOST FAMOUS:</b> 'Lucy' (A. afarensis, 3.2 mya, Ethiopia) — 40% complete skeleton. <b>TEETH:</b> Large molars (herbivorous diet). <b>KEY:</b> BIPEDAL BEFORE LARGE BRAIN — overturns earlier expectation.",
         'lucy', 'Lucy — Australopithecus afarensis skeleton (3.2 mya)'),
    card('ch17', "Homo erectus — key facts",
         "<b>WHEN:</b> ~1.9 mya–100,000 ya. <b>BRAIN:</b> 850–1,100 cc. <b>DISTRIBUTION:</b> Africa, Asia (Peking Man, Java Man), possibly Europe — first hominin to leave Africa. <b>TOOLS:</b> Acheulean hand axes. <b>FIRE:</b> Evidence of fire control (Zhoukoudian, China ~400,000 ya). <b>BODY:</b> Fully modern human proportions (long legs adapted for long-distance running). <b>SIGNIFICANCE:</b> Long geographic range; modern locomotion; increasing cognitive capacity."),
    card('ch17', "Homo neanderthalensis — key facts",
         "<b>WHEN:</b> ~400,000–40,000 ya. <b>RANGE:</b> Europe + western Asia. <b>BRAIN:</b> ~1,500 cc — EQUAL TO or larger than modern humans. <b>ADAPTATIONS:</b> Cold climate (compact body, large nasal passages). <b>TOOLS:</b> Mousterian stone tools. <b>CULTURE:</b> Buried dead, used ochre, made jewelry, cared for injured. <b>INTERBREEDING:</b> Had sex with H. sapiens — all non-African modern humans carry ~1–4% Neanderthal DNA. <b>EXTINCTION:</b> ~40 kya.",
         'neanderthal', 'Neanderthal vs. modern human skull comparison'),
    card('ch17', "Homo sapiens — origin + timeline",
         "<b>WHEN:</b> ~300,000 ya (anatomically modern). <b>WHERE:</b> Multiple locations in Africa (Jebel Irhoud, Morocco ~315 kya; Florisbad, S. Africa ~259 kya). <b>BEHAVIORALLY MODERN:</b> ~100,000–50,000 ya (symbolic art, complex tools, language). <b>OUT OF AFRICA:</b> ~60,000–70,000 ya major migration wave out of Africa → colonized entire world. <b>BRAIN:</b> ~1,350 cc. <b>KEY:</b> Anatomically modern ≠ behaviorally modern — ~200,000 year gap."),
    card('ch17', "Bipedalism — when did it evolve?",
         "<b>WHEN:</b> Before large brains — ~7 mya (Sahelanthropus) suggests upright posture; Ardipithecus (~4.4 mya) was bipedal with small brain (~300 cc); Laetoli footprints (3.6 mya) = modern bipedal gait. <b>KEY POINT:</b> Bipedalism preceded encephalization by millions of years. Old hypothesis ('brain first, then stand up') was WRONG."),
    card('ch17', "4 anatomical markers of bipedalism",
         "<b>1. Foramen magnum position:</b> Shifted anterior (bottom of skull → head balanced atop spine, not hanging in front). <b>2. Pelvis shape:</b> Broad, bowl-shaped ileum (supports organs; provides gluteal muscle attachment for stability). <b>3. Femur angle:</b> Femur angled inward (knock-kneed) → keeps center of gravity over feet while walking. <b>4. Foot arch + big toe:</b> Non-opposable big toe; longitudinal arch acts as spring for efficient locomotion."),
    card('ch17', "Why did bipedalism evolve? 2 main hypotheses",
         "<b>1. Thermoregulation hypothesis:</b> Upright posture exposes less body surface to direct overhead sun at noon; raised height catches cooling breezes on open savanna. <b>2. Energetic efficiency hypothesis:</b> Bipedal walking is MORE energetically efficient than chimpanzee knuckle-walking for the same distance — frees hands for carrying food. <b>ADDITIONAL:</b> Freed hands for tool use, throwing, carrying infants. <b>EVIDENCE:</b> Treadmill studies — human walking significantly more efficient than chimp walking."),
    card('ch17', "Bipedalism costs — maladaptations",
         "<b>WHY costs exist:</b> Bipedal pelvis evolved under conflicting selection: wide enough to birth large-brained babies vs. narrow enough for efficient locomotion. <b>COSTS:</b> (1) Back pain — lumbar lordosis + intervertebral discs poorly designed for vertical load; (2) Difficult childbirth — neonatal head barely fits birth canal → obstetric dilemma; (3) Knee + hip problems — joints bearing full body weight; (4) Varicose veins — blood pumped uphill against gravity."),
    card('ch17', "Hominin tool traditions in chronological order",
         "<b>1. Oldowan (~2.6 mya):</b> Simple choppers and flakes — Homo habilis. <b>2. Acheulean (~1.7 mya):</b> Bifacial hand axes — Homo erectus. Required planning: hold 3D shape in mind while knapping. <b>3. Mousterian (~300–40 kya):</b> Prepared core technique — Neanderthals + archaic H. sapiens. More standardized flakes. <b>4. Upper Paleolithic (~45–10 kya):</b> Blade tools, needles, art, projectiles — behaviorally modern H. sapiens. <b>TREND:</b> Increasing sophistication + planning depth."),
    card('ch17', "FOXP2 gene — what it is, why it matters",
         "<b>WHAT:</b> Transcription factor gene on chromosome 7, regulates ~100+ downstream genes. <b>HUMAN VERSION:</b> 2 amino acid differences vs. chimp; human version under positive selection. <b>FUNCTION:</b> Required for orofacial motor control and language — mutations cause severe speech/language disorders. <b>MYTH:</b> NOT 'the language gene' — it doesn't encode language itself; it encodes fine motor control circuits needed for speech. Found in songbirds, crocodiles too. <b>SIGNIFICANCE:</b> Hints at genetic basis of human speech evolution."),
    card('ch17', "Out of Africa hypothesis — evidence",
         "<b>WHAT:</b> All modern humans derive from an African ancestral population that migrated out of Africa ~60–70 kya. <b>EVIDENCE:</b> (1) Genetic diversity HIGHEST in Africa (more time for mutations to accumulate); (2) All major human haplogroups root in Africa; (3) Fossil anatomically modern H. sapiens earliest in Africa; (4) Population structure: African populations basal to all others in phylogeny. <b>COMPETING:</b> Multiregional hypothesis (largely rejected by genetics).",
         'out_africa', 'Out of Africa migration routes of early modern humans'),
    card('ch17', "Neanderthal DNA in modern humans",
         "<b>HOW MUCH:</b> ~1–4% of the genome in ALL non-African modern humans. <b>PATTERN:</b> Sub-Saharan Africans: essentially 0% Neanderthal DNA. East Asians: slightly more than Europeans. <b>WHERE in genome:</b> Neanderthal DNA absent from X chromosome + gene desert regions (negative selection — BDM incompatibilities). Present in immune genes, skin/hair genes. <b>WHEN interbreeding:</b> Primarily in Middle East ~60 kya as H. sapiens exited Africa and encountered Neanderthals."),
    card('ch17', "Denisovans — who, where, legacy",
         "<b>WHAT:</b> Archaic hominin known primarily from DNA extracted from Denisova Cave, Siberia. <b>WHO THEY ARE:</b> Sister group to Neanderthals; diverged ~400 kya. <b>INTERBREEDING:</b> Denisovan DNA in Melanesians/Pacific Islanders (~3–6%), some mainland Asians. Sub-Saharan Africans and Europeans: essentially 0%. <b>ADAPTIVE GIFT:</b> EPAS1 gene (high-altitude oxygen adaptation in Tibetans) came from Denisovans via introgression."),
    card('ch17', "Adaptive introgression — definition + examples",
         "<b>WHAT:</b> Gene flow that transfers BENEFICIAL alleles from one species/population to another — alleles spread because they increase fitness. <b>EXAMPLE 1:</b> EPAS1 from Denisovans → Tibetans (oxygen regulation at high altitude). <b>EXAMPLE 2:</b> Neanderthal immune genes (HLA alleles) in non-African humans — beneficial because Neanderthals were already adapted to Eurasian pathogens. <b>WHY important:</b> Interbreeding was not just 'noise' — it transferred locally adapted alleles."),
    card('ch17', "Anatomically vs. behaviorally modern H. sapiens",
         "<b>ANATOMICALLY MODERN:</b> Modern skeleton — rounded skull, small brow ridges, chin, gracile frame. ~300 kya. <b>BEHAVIORALLY MODERN:</b> Symbolic art, beads, long-distance trade networks, complex tools, hafted projectiles, musical instruments. ~100–50 kya (Upper Paleolithic 'revolution'). <b>GAP:</b> ~150,000–200,000 years between anatomical and behavioral modernity. <b>WHY gap?</b> Unknown — possibly language, larger population size enabling cumulative culture, or genetic change."),
    card('ch17', "Cooking hypothesis (Wrangham)",
         "<b>WHAT:</b> Cooking food was the KEY innovation enabling the reduction of jaw muscles and expansion of brain in Homo. <b>HOW:</b> Cooking breaks down fibers, denatures proteins, gelatinizes starch → MUCH easier to digest → more caloric yield per gram. Less time chewing (chimps chew ~6 h/day; humans ~1 h/day). <b>RESULT:</b> Smaller gut needed (expensive tissue); energy freed for brain. <b>WHEN:</b> Controlled fire evidence ~400 kya; possibly earlier uncontrolled fire use by H. erectus."),
    card('ch17', "MHC and human mate choice",
         "<b>WHAT:</b> Major Histocompatibility Complex — immune system genes on chromosome 6; highly polymorphic. <b>SWEATY T-SHIRT EXPERIMENT (Wedekind 1995):</b> Women rated men's T-shirts by smell — preferred MHC-DISSIMILAR men. <b>WHY:</b> Offspring of MHC-dissimilar parents have more diverse immune repertoire (heterozygote advantage for immunity). <b>SIGNIFICANCE:</b> Humans detect MHC-related mate quality via body odor — evidence for mate quality assessment based on genetic compatibility."),
]

# ── CH18 — Evolutionary Medicine ─────────────────────────────────────────────
ch18_cards = [
    card('ch18', "Evolutionary medicine — definition + why it matters",
         "<b>WHAT:</b> Application of evolutionary principles to understand disease, health, aging, and the human body's design. <b>KEY INSIGHT:</b> The body wasn't designed perfectly — it was shaped by evolution to maximize reproductive success in ancestral environments, often at the cost of health in modern environments. <b>FOUNDERS:</b> Nesse &amp; Williams (1994). <b>POWER:</b> Explains WHY disease exists rather than just HOW — leads to novel therapeutic strategies."),
    card('ch18', "Nesse's 6 reasons we get sick",
         "<b>1.</b> Pathogens evolve faster than we do. <b>2.</b> Evolutionary mismatch (modern body in unnatural environment). <b>3.</b> Trade-offs (adaptations for one trait create vulnerabilities elsewhere). <b>4.</b> Evolutionary constraints (body can't be redesigned from scratch). <b>5.</b> Antagonistic pleiotropy (genes beneficial early are harmful late). <b>6.</b> Apparent disease IS an adaptation (fever, vomiting, pain = defenses, not failures)."),
    card('ch18', "Reason 1: Pathogens evolve faster",
         "<b>WHY:</b> Bacteria generation time = ~20 min vs. human ~25 years. Bacteria can evolve 1 million generations in 40 years. Mutation rate per generation also higher. <b>RESULT:</b> Coevolutionary arms race — bacteria can always evolve resistance faster than we can deploy new drugs. <b>EXAMPLE:</b> Antibiotic resistance arises within years of introducing new antibiotic. <b>IMPLICATION:</b> We can never 'win' permanently — must keep developing new antibiotics OR manage resistance strategically."),
    card('ch18', "Reason 2: Evolutionary mismatch",
         "<b>WHAT:</b> Human body evolved in ancestral (Pleistocene) environment; modern environment is RADICALLY different. <b>EXAMPLES:</b> (1) Salt preference evolved when salt was scarce → hypertension in salt-rich modern diet. (2) Fat preference evolved when calories were scarce → obesity epidemic. (3) Sedentary lifestyle → cardiovascular disease, type 2 diabetes. (4) Vitamin D deficiency in northern latitudes (evolved in Africa). <b>KEY:</b> Body is fit for ancestral environment, not modern one."),
    card('ch18', "Reason 3: Trade-offs",
         "<b>WHAT:</b> Natural selection cannot simultaneously maximize ALL traits — improving one character often worsens another. <b>EXAMPLES:</b> (1) Upright bipedalism → back pain + difficult childbirth; (2) Large brain + narrow pelvis → obstetric dilemma (human birth extremely difficult vs. other primates); (3) Sickle cell: HbS/HbA heterozygote resistant to malaria but HbS/HbS has severe anemia. <b>WHY important:</b> There may be NO perfect solution — only trade-off optima."),
    card('ch18', "Reason 4: Evolutionary constraints",
         "<b>WHAT:</b> Evolution cannot redesign the body from scratch — it modifies existing structures. New adaptations must build on existing architecture. <b>EXAMPLES:</b> (1) Human back pain — lumbar spine repurposed from horizontal to vertical orientation; (2) Blind spot in vertebrate eye — retinal nerve fibers exit in front of photoreceptors (cephalopod eyes have no blind spot — evolved independently, correct 'wiring'); (3) Recurrent laryngeal nerve takes ridiculous detour around aorta."),
    card('ch18', "Reason 5: Antagonistic pleiotropy (aging)",
         "<b>WHAT:</b> Single gene has BENEFICIAL effects early in life (high reproductive value) and HARMFUL effects late in life (low reproductive value). <b>MECHANISM:</b> Selection removes alleles harmful early, but late-acting harmful effects 'invisible' to selection (most individuals already reproduced). <b>EXAMPLE 1:</b> p53 — suppresses cancer growth early BUT high p53 activity accelerates tissue aging. <b>EXAMPLE 2:</b> Testosterone — promotes reproduction early; may promote prostate cancer + cardiovascular risk late. <b>RESULT:</b> Senescence (aging) is inevitable."),
    card('ch18', "Reason 6: Apparent disease = adaptation",
         "<b>KEY INSIGHT:</b> Some 'symptoms' are ADAPTATIONS — defenses that increase fitness, NOT failures of the body. <b>FEVER:</b> Elevated temperature inhibits pathogen growth + speeds immune cell activity. Taking fever reducers may prolong infection. <b>VOMITING:</b> Expels toxins/pathogens rapidly. <b>DIARRHEA:</b> Flushes gut pathogens. <b>MORNING SICKNESS:</b> Avoids teratogenic foods during organogenesis. <b>PAIN:</b> Signals tissue damage — necessary for behavior modification. <b>LESSON:</b> Don't suppress symptoms without understanding their function."),
    card('ch18', "Antagonistic pleiotropy vs. mutation accumulation (aging theories)",
         "<b>ANTAGONISTIC PLEIOTROPY (Williams 1957):</b> Genes with beneficial early effects and harmful late effects — selected positively early, harmful late effects 'ride along.' Predicts some late-acting deleterious alleles should be under POSITIVE selection early. <b>MUTATION ACCUMULATION (Medawar 1952):</b> Deleterious mutations that act late in life escape purifying selection (few individuals survive to old age in nature) → accumulate in population. <b>BOTH operate simultaneously.</b> <b>PREDICTION:</b> Aging is not programmed — it's the cost of early fitness."),
    card('ch18', "p53 — antagonistic pleiotropy example",
         "<b>WHAT:</b> Tumor suppressor protein; triggers apoptosis or cell cycle arrest when DNA damage detected. <b>EARLY BENEFIT:</b> High p53 activity = low cancer risk (kills pre-cancerous cells). <b>LATE COST:</b> High p53 also triggers cell senescence — aging of tissues (stem cells retire permanently). Mice engineered for extra p53 had LOWER cancer but aged FASTER. <b>TRADE-OFF:</b> Cancer suppression vs. tissue aging. Classic antagonistic pleiotropy at the molecular level."),
    card('ch18', "Virulence — definition + trade-off",
         "<b>WHAT:</b> The harm a pathogen causes to its host. <b>TRADE-OFF:</b> Virulence vs. transmission. Extremely virulent pathogen kills host too fast → no time to transmit. Extremely benign pathogen → doesn't exploit host enough → outcompeted by more virulent strains. <b>EVOLUTIONARY STABLE VIRULENCE:</b> At intermediate virulence level where transmission rate is maximized. <b>KEY:</b> Virulence is NOT just an accident — it's the evolved optimum of this trade-off."),
    card('ch18', "Why cholera maintains high virulence",
         "<b>BIOLOGY:</b> Vibrio cholerae causes massive diarrhea (10–20L/day) → kills rapidly. <b>WHY STILL VIRULENT?</b> Transmission DOES NOT require mobile host (unlike flu — you need to walk around to spread it). Cholera spreads via contaminated water — host can be incapacitated or dead and bacteria still spread into water supply. <b>PREDICTION:</b> Improve water sanitation → select for less virulent strains (mobile host needed). <b>CONFIRMED:</b> Cholera strains less virulent in clean-water environments."),
    card('ch18', "Antibiotic resistance — evolutionary medicine angle",
         "<b>CLINICAL INSIGHT:</b> Every antibiotic use = a selection event. Incomplete courses leave intermediate-resistance survivors (more dangerous than full survivors or full kills). <b>STRATEGIES from evo medicine:</b> (1) Antibiotic stewardship — don't use unless necessary; (2) Combination therapy — multiple drugs simultaneously (probability of simultaneous resistance to all = very low); (3) Phage therapy; (4) 'Collateral sensitivity' — resistance to drug A makes bacteria MORE susceptible to drug B."),
    card('ch18', "Cancer as somatic evolution",
         "<b>WHAT:</b> Cancer is evolution happening in somatic (body) cells. <b>MECHANISM:</b> Mutations accumulate in somatic cells → mutant cells with growth advantage outcompete normal cells → natural selection within body → clonal expansion → metastasis. <b>DARWINIAN PROPERTIES:</b> Heritable variation (somatic mutations), differential reproduction (faster-dividing cells leave more offspring), natural selection. <b>IMPLICATION:</b> Using cytotoxic chemo = strong selection for resistant cells. Need evolutionary-aware treatment strategies.",
         'cancer_evo', 'Clonal evolution of cancer — somatic natural selection'),
    card('ch18', "Sickle cell — fitness ranking in malaria-endemic Africa",
         "<b>HbS/HbS (homozygous sickle):</b> LOWEST fitness — severe sickle cell disease, often fatal before reproduction. <b>HbA/HbA (normal homozygote):</b> INTERMEDIATE — susceptible to Plasmodium falciparum malaria. <b>HbA/HbS (heterozygote):</b> HIGHEST fitness — protected from malaria (parasites can't thrive in sickled cells at low O₂) + no severe anemia. <b>TYPE:</b> Heterozygote advantage → balancing selection → both alleles maintained at equilibrium.",
         'sickle_cell', 'Sickle cell anemia — red blood cell morphology'),
    card('ch18', "Sickle cell — fitness ranking in NON-malarial regions",
         "<b>HbA/HbA:</b> HIGHEST fitness — no malaria to worry about, normal blood function. <b>HbA/HbS:</b> INTERMEDIATE — mild sickling episodes under extreme conditions, but no malaria protection benefit. <b>HbS/HbS:</b> LOWEST — severe sickle cell disease without any compensating benefit. <b>RESULT:</b> HbS allele frequency DECLINES over generations in non-malarial populations — natural selection removes it. Currently declining in African-American populations relative to West African origin populations.",
         'malaria_map', 'Sickle cell allele frequency mirrors malaria distribution globally'),
    card('ch18', "Hygiene hypothesis",
         "<b>WHAT:</b> Reduced exposure to parasites, bacteria, and pathogens in early childhood increases risk of allergies and autoimmune disease. <b>MECHANISM:</b> Immune system evolved to combat helminths, bacteria, protozoa. In their absence, immune system 'misdirects' inflammatory response toward harmless antigens (pollen, peanuts, own tissues). <b>EVIDENCE:</b> Inverse correlation between parasitic worm prevalence and autoimmune disease prevalence globally. <b>MISMATCH:</b> Over-clean modern environments lack immune-calibrating signals."),
    card('ch18', "Myxoma virus — evolutionary case study",
         "<b>WHAT:</b> Deliberately introduced to Australia (1950) to control European rabbits. Initially: 99.8% mortality. <b>WHAT HAPPENED:</b> Within years, both virus AND rabbits evolved. Virus: less virulent strains spread better (rabbit lived longer → more mosquito bites → more transmission). Rabbits: evolved partial resistance. <b>CURRENT:</b> ~50% mortality (vs. 99.8% originally). <b>LESSON:</b> Virulence evolves to transmission-optimizing intermediate. Cannot deploy biocontrol without expecting evolutionary response.",
         'myxoma', 'Rabbit with myxomatosis — Australian biocontrol case study'),
    card('ch18', "Mismatch disease examples",
         "<b>DEFINITION:</b> Diseases caused by a mismatch between the environment humans evolved in (Pleistocene Africa) and the modern environment. <b>EXAMPLES:</b> (1) Type 2 diabetes — fat/sugar storage genes optimal in feast-famine cycle; (2) Cardiovascular disease — salt preference + sedentary lifestyle; (3) Myopia — eyes adapted for distance, not reading 30 cm away; (4) Vitamin D deficiency in high latitudes; (5) Anxiety disorders — stress response evolved for acute threats, not chronic modern stress. <b>TREATMENT:</b> Understand ancestral environment."),
    card('ch18', "Evolutionary mismatch — back pain",
         "<b>WHY SO COMMON:</b> Human lumbar spine derived from horizontal ancestral mammal spine. Evolution co-opted a horizontal support structure for vertical load-bearing. <b>DESIGN PROBLEMS:</b> Intervertebral discs bulge under compression (herniation); lumbar lordosis curve puts uneven pressure on vertebrae; gluteal muscles and hip flexors poorly balanced for prolonged sitting. <b>EPIDEMIOLOGY:</b> ~80% of people experience significant back pain — #1 cause of disability globally. <b>LESSON:</b> Evolutionary constraint + mismatch = imperfect design."),
    card('ch18', "Peto's paradox — cancer resistance in large animals",
         "<b>WHAT:</b> Large, long-lived animals (whales, elephants) should get more cancer — more cells = more mutations = more cancer. But they DON'T. <b>PARADOX:</b> Cancer rates similar or lower in large animals than small ones. <b>SOLUTION:</b> Large/long-lived lineages evolved BETTER cancer suppression mechanisms. Elephants: 20 copies of p53 gene (humans have 2). Whales: more efficient DNA repair, alternative tumor suppression pathways. <b>SIGNIFICANCE:</b> Evolution solved cancer suppression repeatedly — understand HOW for cancer therapy."),
    card('ch18', "Conserved gene networks in evolutionary medicine",
         "<b>INSIGHT:</b> Many disease-causing genes are evolutionarily ancient and conserved — same pathway exists in model organisms. <b>PRACTICAL:</b> Model organisms (C. elegans, Drosophila, mouse) reveal disease mechanism because gene function conserved. <b>EXAMPLES:</b> BRCA1 breast cancer gene homologs in yeast; Huntington's gene (huntingtin) in flies; p53 family in Hydra (1 billion years old). <b>LESSON:</b> Cancer genes are often ancient growth/cell cycle regulators re-purposed; their ancient function matters for therapy design."),
]

# ── TRAP CARDS ───────────────────────────────────────────────────────────────
trap_cards = [
    card('trap', "TRAP: Using C-14 to date dinosaur fossils",
         "WRONG. C-14 has a half-life of only 5,730 years — after ~50,000 years virtually ALL C-14 has decayed. Dinosaurs = ~66+ million years old. Must use U-Pb or K-Ar for such ancient material. Students confuse 'radioactive dating' with C-14 specifically."),
    card('trap', "TRAP: 'Reptiles' are a valid taxonomic group",
         "NO — 'Reptiles' (lizards + snakes + turtles + crocs, excluding birds) = PARAPHYLETIC. Excludes birds, which ARE avian theropod dinosaurs. Crocodilians are more closely related to birds than to lizards. Correct monophyletic group = Reptilia INCLUDING birds."),
    card('trap', "TRAP: K-Pg was the largest mass extinction",
         "NO. The PERMIAN extinction (~252 mya) was the largest = ~96% of species lost ('The Great Dying'). K-Pg (~66 mya) killed ~76% of species — catastrophic but smaller. Permian = #1, K-Pg = #3. Students confuse fame (K-Pg killed dinosaurs) with severity."),
    card('trap', "TRAP: Antibiotics cause bacteria to mutate",
         "NO — antibiotics SELECT for pre-existing resistance mutations; they do NOT cause mutations. Mutations occur randomly due to replication errors — they pre-exist antibiotic exposure. Antibiotics simply kill susceptible cells, leaving resistant ones to reproduce. Directed mutation = Lamarckism (wrong)."),
    card('trap', "TRAP: Humans evolved from chimpanzees",
         "NO — humans and chimps share a COMMON ANCESTOR ~6–7 mya that was neither modern human nor modern chimp. Both lineages have been evolving since the split. Saying 'humans evolved from chimps' = saying you descended from your cousin. Chimps have evolved just as long as we have."),
    card('trap', "TRAP: Bipedalism evolved AFTER large brains",
         "WRONG. BIPEDALISM FIRST (~7 mya Sahelanthropus, ~4.4 mya Ardipithecus). Large brains came MUCH LATER (~2 mya with Homo). Australopithecus: fully bipedal with only 420–550 cc brain (barely larger than chimp). The old 'brain first' hypothesis was disproven by fossil evidence."),
    card('trap', "TRAP: BSC works for all organisms",
         "BSC (Mayr) FAILS for: (1) Fossils — cannot test gene flow in extinct taxa; (2) Asexual species — bacteria/archaea/many plants/fungi don't interbreed sexually; (3) Hybridizing species — many plant species produce fertile hybrids across species boundaries. BSC applies only to sexual species with living representatives."),
    card('trap', "TRAP: Mule is an example of hybrid inviability",
         "NO — mule is HYBRID STERILITY. Mule is a healthy, long-lived, strong animal (survives into 30s). It is STERILE because 63 chromosomes cannot pair in meiosis. Hybrid inviability = hybrid dies before reproductive age. Mule = survives but cannot reproduce = sterility, not inviability."),
    card('trap', "TRAP: Island biogeography equilibrium never changes",
         "WRONG. The equilibrium SPECIES RICHNESS changes dynamically — it is an equilibrium of RATES not a fixed value. As island size or distance from mainland changes, equilibrium shifts. Turnover continues at equilibrium — species going extinct are replaced by immigrants. Total number stable, but COMPOSITION changes constantly."),
    card('trap', "TRAP: Virulence always evolves lower over time",
         "WRONG. Virulence evolves to the level that MAXIMIZES pathogen transmission, not the lowest possible level. If high virulence increases transmission (e.g., cholera — host doesn't need to move), virulence stays high. Only when transmission REQUIRES a healthy/mobile host does selection favor lower virulence. Example: Myxoma virus — intermediate virulence evolved, not zero."),
    card('trap', "TRAP: FOXP2 is 'the language gene'",
         "OVERSIMPLIFICATION. FOXP2 is a transcription factor required for fine OROFACIAL MOTOR CONTROL needed for articulate speech. It regulates ~100+ downstream genes. Mutations cause severe speech/language disorders. But FOXP2 is found in crocodiles, mice, and songbirds — it didn't 'create' language. Language involves thousands of genes. FOXP2 = one piece of a very complex puzzle."),
    card('trap', "TRAP: Global species diversity = immigration + extinction",
         "NO. Global diversity ≠ island diversity. Island biogeography: diversity = balance of IMMIGRATION from mainland minus local EXTINCTION. But GLOBAL diversity = speciation rate minus global extinction rate. No 'mainland' exists globally — new species can only come from speciation. Immigration applies at local/regional scale."),
    card('trap', "TRAP: In vicariance, organisms MOVE; in dispersal, barriers FORM",
         "REVERSED. VICARIANCE: organisms STAY PUT, a BARRIER forms between them (e.g., Isthmus of Panama separates Atlantic/Pacific populations). DISPERSAL: organisms MOVE across an existing barrier to colonize new territory. Easy memory: Vicariance = 'Victimized by geography' (barrier forms around them); Dispersal = 'organisms Do the Dispersing.'"),
    card('trap', "TRAP: Neanderthal brain was smaller than modern human brain",
         "WRONG. Neanderthal average brain volume (~1,500 cc) was EQUAL TO or SLIGHTLY LARGER than modern human average (~1,350 cc). Neanderthals had culture, tools, buried dead, used ochre. Modern human cognitive advantage is NOT simply brain SIZE — likely due to different internal organization, connectivity, and specific region development."),
    card('trap', "TRAP: Miller-Urey experiment produced living cells",
         "NO. Miller-Urey (1953) produced AMINO ACIDS (the monomers of proteins) — NOT cells, NOT DNA, NOT RNA, NOT functional proteins. It showed building blocks can form abiotically. The gap between amino acids and a living cell is enormous — that gap is the 'origin of life' problem, not solved by Miller-Urey."),
    card('trap', "TRAP: Feathers evolved for flight",
         "NO — classic exaptation. Feathers evolved in NON-FLYING theropod dinosaurs (Velociraptor, Sinosauropteryx, Anchiornis) for insulation, display, and species recognition. Velociraptor arms were far too short to generate lift. Feathers predate flight by tens of millions of years. Flight was a LATER co-option (exaptation) of feathers."),
    card('trap', "TRAP: Antagonistic pleiotropy = one gene with two pleiotropic effects",
         "REQUIRES SPECIFIC TIMING. Antagonistic pleiotropy specifically means a gene is BENEFICIAL early in life (during peak reproduction) and HARMFUL late in life (post-reproduction). This is why selection doesn't remove it — early benefit outweighs late cost. Simply having two pleiotropic effects (both bad, or both good, or both at same age) is NOT antagonistic pleiotropy."),
    card('trap', "TRAP: Synapomorphies = any shared character",
         "NO — synapomorphies = SHARED DERIVED characters. There are 4 types: (1) Synapomorphy: shared derived (defines clades); (2) Symplesiomorphy: shared ANCESTRAL (doesn't define clades — e.g., 'has bones' = ancestral for all vertebrates); (3) Autapomorphy: unique derived character of one taxon only; (4) Homoplasy: similar character in unrelated groups (NOT synapomorphy). Only synapomorphies are phylogenetically informative."),
    card('trap', "TRAP: Allopolyploidy requires geographic isolation",
         "NO — allopolyploidy produces INSTANT reproductive isolation within one generation WITHOUT any geographic isolation. The new allopolyploid is immediately reproductively isolated from both parent species (different ploidy → meiosis failure when crossed back). This is WHY it's classified as a form of sympatric speciation. No geographic isolation step needed."),
    card('trap', "TRAP: Sickle cell heterozygote fitness in malaria regions",
         "HbA/HbS (sickle cell CARRIER) has the HIGHEST fitness in malaria-endemic regions — NOT HbA/HbA. This is HETEROZYGOTE ADVANTAGE (overdominance). HbA/HbA: susceptible to malaria. HbS/HbS: severe sickle cell disease. HbA/HbS: protected from malaria AND no severe anemia. This balancing selection maintains BOTH alleles in the population."),
    card('trap', "TRAP: Cancer is not evolution",
         "Cancer IS evolution — Darwinian evolution in somatic cells. Cancer cells have: heritable variation (somatic mutations), differential reproduction (some cells divide faster), natural selection (fastest-growing clones dominate). This is WHY cancer is so hard to cure — applying one drug = strong selection for resistant cells. Evolutionary-aware treatment strategies (e.g., 'adaptive therapy') use this insight."),
    card('trap', "TRAP: Anatomically modern = behaviorally modern",
         "NO — there is a ~150,000–200,000 year gap. Anatomically modern H. sapiens: ~300 kya (rounded skull, small brow ridges, chin). Behaviorally modern: ~50–100 kya (Upper Paleolithic — art, beads, complex tools, long-distance trade). The 'creative revolution' or 'human revolution' came long after anatomical modernization. Cause of gap is debated — possible language, population density, or genetic change."),
    card('trap', "TRAP: Denisovan DNA = same distribution as Neanderthal DNA",
         "DIFFERENT distributions. NEANDERTHAL DNA: found in ALL non-African modern humans (~1–4%) — Eurasians, Asians, Pacific Islanders, Native Americans. DENISOVAN DNA: mainly MELANESIANS and Pacific Islanders (~3–6%) + some mainland Asians. Notably ABSENT in sub-Saharan Africans AND in most Europeans. Different geographic interbreeding zones — Denisovans were in eastern Asia/Southeast Asia when H. sapiens arrived."),
]

# ── Assemble all chapters ────────────────────────────────────────────────────
fc_html = ''
fc_html += chapter('ch3', '#4ade80', 'History of Life', 'Ch 3 • History of Life on Earth',
                   '\n'.join(ch3_cards))
fc_html += '\n'
fc_html += chapter('ch4', '#60a5fa', 'Phylogenetics', 'Ch 4 • Phylogenetics & Macroevolution',
                   '\n'.join(ch4_cards))
fc_html += '\n'
fc_html += chapter('ch13', '#a78bfa', 'Speciation', 'Ch 13 • The Origin of Species',
                   '\n'.join(ch13_cards))
fc_html += '\n'
fc_html += chapter('ch14', '#f472b6', 'Biogeography', 'Ch 14 • Macroevolution & Biogeography',
                   '\n'.join(ch14_cards))
fc_html += '\n'
fc_html += chapter('ch8', '#fbbf24', 'Humans & Selection', 'Ch 8 • Natural Selection: Empirical Studies',
                   '\n'.join(ch8_cards))
fc_html += '\n'
fc_html += chapter('ch17', '#34d399', 'Human Evolution', 'Ch 17 • Human Evolution: A New Kind of Ape',
                   '\n'.join(ch17_cards))
fc_html += '\n'
fc_html += chapter('ch18', '#f87171', 'Evolutionary Medicine', 'Ch 18 • Evolutionary Medicine',
                   '\n'.join(ch18_cards))
fc_html += '\n'
fc_html += chapter('trap', '#fb923c', 'Trap Cards', '⚠ Common Exam Traps',
                   '\n'.join(trap_cards))

# ── Inject into exam3 ────────────────────────────────────────────────────────
html = EXAM3.read_text(encoding='utf-8')
# Find start: <div class="fc-chapter" data-ch="ch3">
start_marker = '<div class="fc-chapter" data-ch="ch3">'
# Find end: the closing </div></div> after the last trap chapter
end_marker = '</div></div>\n\n</section>'

start_idx = html.index(start_marker)
# Find the closing after trap chapter
end_search = html[start_idx:]
end_idx = start_idx + end_search.index('</section>')

new_html = html[:start_idx] + fc_html + '\n\n</section>' + html[end_idx + len('</section>'):]
EXAM3.write_text(new_html, encoding='utf-8')

# Count cards
total = new_html.count('<div class="fc2"')
imgs_added = new_html.count('<img src=') - html.count('<img src=') + new_html.count('<img src=')
print(f"Done. {total} flashcards written, {new_html.count('<img src=')} images embedded, {len(new_html)//1024} KB total")
