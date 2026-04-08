"""Node generators for Lectures 14-15 (Exam 3 coverage) with LECTURE AUDIO from recordings.

Lec 14 (History of Life, Ch 3) lecture recorded 2026-04-01.
Lec 15 (Phylogenetics, Ch 4) lecture recorded 2026-04-06.

Recording text is pulled verbatim from _work/recordings.json and attached
to the slide clusters the professor was actively discussing.
"""
import json, os
from helpers import load_lec, slides_to_sections, audio_section, build_node

REC_PATH = os.path.join(os.path.dirname(__file__), '..', 'recordings.json')

def _load_recordings():
    with open(REC_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

_REC = _load_recordings()
APR1 = _REC['2026-04-01']['text']
APR6 = _REC['2026-04-06']['text']


# --------------------------------------------------------------------------
# April 1 recording segments (Lec 14 - History of Life)
# Segments are sliced by character range from the 25,221-char transcript.
# These ranges were identified by reading the transcript in 5 ~5k parts.
# --------------------------------------------------------------------------

# Segment A: deep time intro + age-of-Earth debate + radiometric dating
# (covers slides 1-5: lecture goals, 6000 years vs Kelvin 20 My vs 4.568 bya,
#  isotopes and half-life video)
APR1_AGE_EARTH = APR1[0:7500]

# Segment B: Earth formation + "come over someday" mnemonic entry
# (covers slides 6-11 origin-of-life overlap — minimal direct coverage in audio,
#  so we attach the brief formation-of-Earth passage)
APR1_ORIGIN = APR1[7500:9200]

# Segment C: Paleozoic periods walk-through (Ordovician → Permian)
# (covers slides 20-30)
APR1_PALEOZOIC = APR1[9200:15200]

# Segment D: Mesozoic + KT boundary
# (covers slides 31-34)
APR1_MESOZOIC = APR1[15200:20400]

# Segment E: Cenozoic + take-home points
# (covers slides 35-36)
APR1_CENOZOIC = APR1[20400:]


def lec14_nodes():
    d = load_lec('lec14')
    nodes = []

    # ---- Node 1: Age of Earth & Deep Time (slides 1-5) ----
    sections = slides_to_sections(d, (1, 5))
    sections.append(audio_section(
        'Age of Earth, Deep Time, Radiometric Dating (recorded 2026-04-01)',
        APR1_AGE_EARTH,
    ))
    nodes.append(build_node(
        id='lec14-age-earth',
        title='Age of the Earth & Deep Time',
        subtitle='4.568 billion years via radiometric dating (Lec 14 slides 1-5)',
        color='blue', row=12,
        heading='Lecture 14 — History of Life: Age of the Earth',
        sections=sections,
        examples=[
            'Special Creation: ~6,000 years (incorrect — contradicted by all physical evidence).',
            'Darwin\'s estimate: several billion years based on sediment accumulation rates. Remarkably close for the 1800s.',
            'Lord Kelvin: ~20 million years based on rock cooling rates. WRONG because Kelvin didn\'t know Earth\'s interior generates heat via radioactive decay.',
            'Modern answer: 4.568 billion years via radiometric dating of the oldest zircon crystals (4.4 By old, Western Australia).',
            'Counting to 1 million seconds = 11 days. Counting to 1 billion seconds = 31 years.',
        ],
        warnings=[
            'Kelvin\'s math was not wrong — his ASSUMPTION (that Earth was a homogeneous cooling rock) was wrong. Always check assumptions.',
            'A half-life is a STATISTICAL property, not a deterministic one. You cannot predict when a single atom will decay, only the population rate.',
        ],
        mnemonic='4.568 billion years — Earth is old beyond human intuition. Deep time.',
        flashcard={
            'front': 'How does radiometric dating work, and why is it trusted?',
            'back': 'Radiometric dating relies on radioactive isotopes decaying at a CONSTANT rate into daughter isotopes. The half-life (time for 50% of parent to decay) is fixed for each isotope — unaffected by temperature, pressure, or chemistry. To date a rock: (1) measure the ratio of parent to daughter isotope, (2) know the half-life, (3) calculate elapsed time. Multiple isotope systems (U-Pb, K-Ar, Rb-Sr, C-14) with different half-lives can be applied to the same sample as independent cross-checks. Zircon crystals trap uranium but exclude lead, making them excellent time capsules — the oldest known zircon (4.4 Bya, Western Australia) was dated using both U-235 and U-238 systems and gave the same age. Results also match tree rings and ice cores for recent dates.',
        },
        quiz={
            'question': 'Why was Lord Kelvin\'s estimate of Earth\'s age (20 million years) so far off?',
            'correct': 'He didn\'t know that Earth\'s interior generates heat via radioactive decay',
            'distractors': [
                'His math was wrong',
                'He used the wrong isotopes',
                'He assumed Earth was older than it is',
            ],
        },
        visual={
            'type': 'timeline',
            'description': 'Competing estimates of Earth\'s age',
            'regions': [
                {'label': 'Special Creation (~6 kya)', 'color': '#e63946', 'items': ['Young Earth', 'No evidence']},
                {'label': 'Kelvin (20 Mya)', 'color': '#f77f00', 'items': ['Based on cooling', 'Ignored radioactive heat']},
                {'label': 'Darwin (~300 Mya)', 'color': '#ffc857', 'items': ['Sediment rates', 'Close for 1800s']},
                {'label': 'Modern (4.568 Bya)', 'color': '#4ea8de', 'items': ['Radiometric', 'Zircons, U-Pb']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': '4.568 billion. Remember the decimal.',
            'trap': 'Carbon-14 dating only works for organic material up to ~50,000 years. For geology, use U-Pb, K-Ar, or Rb-Sr.',
        },
    ))

    # ---- Node 2: Origin of Life & Prebiotic Chemistry (slides 6-11) ----
    sections = slides_to_sections(d, (6, 11))
    sections.append(audio_section(
        'Early Earth formation (brief mention, recorded 2026-04-01)',
        APR1_ORIGIN,
    ))
    nodes.append(build_node(
        id='lec14-origin-life',
        title='Origin of Life & Prebiotic Soup',
        subtitle='Miller-Urey, RNA world, abiogenesis (Lec 14 slides 6-11)',
        color='teal', row=12,
        heading='Lecture 14 — Origin of Life from Non-Life',
        sections=sections,
        examples=[
            'Early Earth: no free oxygen, atmosphere of methane/hydrogen/ammonia/water/CO₂. Energy from lightning, UV, volcanoes, cosmic rays.',
            'Murchison meteorite (1989, Australia): contained carbon, purines, pyrimidines — extraterrestrial inputs may have enriched the prebiotic soup.',
            'Miller-Urey (1953): spark-discharge experiment produced 20+ amino acids including glycine, alanine, valine.',
            'Sydney Fox (1977): heated amino acids → weak peptide bonds when added to water. Claudia Huber (1997): CO made stable peptide bonds.',
            'RNA world hypothesis: RNA can BOTH store info AND catalyze reactions — likely predates DNA/protein life.',
        ],
        warnings=[
            'Abiogenesis is still an active research area — we know the building blocks can form, but the complete pathway from molecules → self-replicating cell is not fully solved.',
            'Darwin 1871 letter: "a warm little pond with all sorts of ammonia and phosphoric salts, light, heat, electricity" — Darwin imagined it 80+ years before Miller-Urey tested it.',
        ],
        mnemonic='Prebiotic soup: methane + ammonia + lightning = amino acids (Miller-Urey).',
        flashcard={
            'front': 'What did the Miller-Urey experiment demonstrate, and why does it matter for origin-of-life theory?',
            'back': 'In 1953, Stanley Miller and Harold Urey built a closed apparatus simulating early Earth conditions: a flask of water (ocean), gases representing the early atmosphere (methane, ammonia, hydrogen, water vapor), and electric sparks (lightning). After running the experiment for a week, they analyzed the water and found 20+ amino acids — including glycine, alanine, and valine — the building blocks of proteins. This proved that ORGANIC molecules essential for life can form spontaneously from INORGANIC precursors under plausible early-Earth conditions. It didn\'t prove life originated this way, but it showed abiogenesis is chemically plausible. Later experiments by Sydney Fox and Claudia Huber showed those amino acids could also be strung into peptide chains.',
        },
        quiz={
            'question': 'What did the Miller-Urey experiment produce?',
            'correct': 'Over 20 amino acids from inorganic precursors',
            'distractors': [
                'A complete living cell',
                'DNA from RNA',
                'Proteins with catalytic activity',
            ],
        },
        visual={
            'type': 'process',
            'description': 'Prebiotic chemistry pathway',
            'regions': [
                {'label': 'Early Earth', 'color': '#6e6a80', 'items': ['No O₂', 'CH₄, NH₃, H₂', 'Lightning, UV']},
                {'label': 'Miller-Urey', 'color': '#4ea8de', 'items': ['Spark discharge', '20+ amino acids']},
                {'label': 'Polymerization', 'color': '#7de2d1', 'items': ['Fox 1977', 'Huber 1997 (CO)']},
                {'label': 'RNA world', 'color': '#ffc857', 'items': ['Self-replicating', 'Ribozymes']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Gas + spark → amino acids → peptides → RNA → life.',
            'trap': 'The early atmosphere composition is debated. Modern estimates include more CO₂ and N₂ than the original Miller-Urey mix — but amino acid production still occurs.',
        },
    ))

    # ---- Node 3: Early Life & Multicellularity (slides 12-20) ----
    # Recording doesn't densely cover this range, so we skip audio here.
    sections = slides_to_sections(d, (12, 20))
    nodes.append(build_node(
        id='lec14-early-life',
        title='Early Life, Stromatolites & Multicellularity',
        subtitle='Biomarkers, LUCA, eukaryotes, first animals (Lec 14 slides 12-20)',
        color='green', row=12,
        heading='Lecture 14 — Earliest Life Forms',
        sections=sections,
        examples=[
            'Biomarkers (3.8 Bya): DNA fragments, isotopic ratios (organic carbon has different ratios than volcanic carbon), molecules like okenane (lipid pigment).',
            'Stromatolites (3.45 Bya): layered mounds formed when biofilm bacteria trap sediment. Still alive today in Shark Bay, Australia.',
            'LUCA (Last Universal Common Ancestor): ~3.5-3.8 Bya. All extant life descends from this.',
            'Archaea (3.5 By): single-celled, biochemically distinct from bacteria and eukaryotes.',
            'Cyanobacteria (2.6 By): first photosynthesis with O₂ as byproduct. First atmospheric oxygen.',
            'Eukaryotes (1.8 By): 100× bigger than bacteria. Endosymbiosis: archaeal cell engulfed a bacterium → mitochondrion. Second event → chloroplast.',
            'Multicellularity evolved INDEPENDENTLY multiple times: animals, plants, fungi, red algae, slime molds.',
            'First animals: sponges, 650-635 Mya.',
        ],
        warnings=[
            'The fossil record for microbial life is fragmentary. Biomarker evidence (isotope ratios in rocks) is often how we detect life before 2 Bya.',
            'Endosymbiosis was proposed by Lynn Margulis in the 1960s and was initially rejected. Now it is textbook-established (mitochondria have their own DNA, reproduce by fission, have double membranes).',
        ],
        mnemonic='LUCA → Archaea → Bacteria → Eukaryotes (via endosymbiosis). Multicellularity: many independent origins.',
        flashcard={
            'front': 'How did eukaryotic cells arise, and what evidence supports endosymbiotic theory?',
            'back': 'Lynn Margulis\'s endosymbiotic theory proposes that eukaryotic cells formed when a larger archaeal cell engulfed (but did not digest) a free-living bacterium, which persisted inside as a mitochondrion. A later endosymbiosis brought in a cyanobacterium that became the chloroplast. Evidence: (1) Mitochondria and chloroplasts have their OWN circular DNA (like bacteria) separate from the nucleus. (2) They reproduce by binary fission, not with the cell cycle. (3) They have double membranes — the outer membrane from the host, the inner from the original bacterium. (4) Their ribosomes are bacterial (70S), not eukaryotic (80S). (5) Antibiotics targeting bacterial ribosomes also affect mitochondria. This was once radical; now it is textbook.',
        },
        quiz={
            'question': 'Which piece of evidence most strongly supports endosymbiotic theory?',
            'correct': 'Mitochondria and chloroplasts have their own DNA and double membranes',
            'distractors': [
                'All eukaryotes have mitochondria',
                'Bacteria are smaller than eukaryotic cells',
                'Mitochondria generate ATP',
            ],
        },
        visual={
            'type': 'timeline',
            'description': 'Life origins timeline',
            'regions': [
                {'label': '3.8 Bya', 'color': '#6e6a80', 'items': ['Biomarkers', 'LUCA era']},
                {'label': '3.5 Bya', 'color': '#4ea8de', 'items': ['Stromatolites', 'Archaea']},
                {'label': '2.6 Bya', 'color': '#7de2d1', 'items': ['Cyanobacteria', 'First O₂']},
                {'label': '1.8 Bya', 'color': '#ffc857', 'items': ['Eukaryotes', 'Endosymbiosis']},
                {'label': '650 Mya', 'color': '#f77f00', 'items': ['First sponges', 'First animals']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': '3.8 → 3.5 → 2.6 → 1.8 → 0.65 (Bya): life, oxygen, complexity, animals.',
            'trap': 'Oxygen almost killed early life — the Great Oxidation Event (~2.4 Bya) was a mass extinction for anaerobes. Obligate anaerobes retreated to oxygen-free niches.',
        },
    ))

    # ---- Node 4: Cambrian Explosion & Paleozoic (slides 21-30) ----
    sections = slides_to_sections(d, (21, 30))
    sections.append(audio_section(
        'Paleozoic walk-through: Ordovician → Permian (recorded 2026-04-01)',
        APR1_PALEOZOIC,
    ))
    nodes.append(build_node(
        id='lec14-cambrian-paleozoic',
        title='Cambrian Explosion & Paleozoic Periods',
        subtitle='Burgess Shale to first reptiles (Lec 14 slides 21-30)',
        color='amber', row=12,
        heading='Lecture 14 — Paleozoic: Cambrian through Permian',
        sections=sections,
        examples=[
            'Ediacaran (575-535 Mya): earliest definitive multicellular animals. Many body plans disappeared before the Cambrian.',
            'Cambrian explosion (542-488 Mya): trilobites, early arthropods, first chordates (Haikouichthys, amphioxus-like). Huge burst of body plan diversity.',
            'Burgess Shale (505 Mya, Canadian Rockies): 65,000+ specimens, 93 species. Anoxic mudslides preserved soft tissues. A "Lagerstätte" — exceptional fossil site.',
            'Ordovician (488-444 Mya): early bony fish, first land plants (~475 Mya, moss/liverwort-like).',
            'Silurian (444-416 Mya): first land animals (millipede ~428 Mya). Invertebrates came out of water before vertebrates.',
            'Devonian (416-359 Mya): AGE OF FISHES. Earliest tetrapods (~370 Mya). Dunkleosteus — giant predatory fish up to 6 m long.',
            'Carboniferous (359-299 Mya): AGE OF AMPHIBIANS. Massive coal deposits from the lush land plants. Synapsid/sauropsid split (~300-280 Mya).',
            'Permian (299-251 Mya): first reptiles. Synapsids (→ mammals) vs sauropsids (→ reptiles, dinosaurs, birds). Skull window counts: anapsid, synapsid, diapsid.',
        ],
        warnings=[
            '"Age of X" means the period when X DOMINATES, not when X first appeared. E.g., Age of Fishes = Devonian, but fish originated in the Ordovician.',
            'Synapsid ≠ reptile, even though "mammal-like reptiles" is sometimes used casually. Synapsids are a separate lineage from the reptile lineage (sauropsids).',
        ],
        mnemonic='Robbins\' mnemonic: "COME OVER SOME DAY MAYBE PICKING UP HARD CASH" = Cambrian, Ordovician, Silurian, Devonian, Mississippian, Pennsylvanian, Permian, Triassic, Jurassic, Cretaceous. Or just: "Camels Often Sit Down Carefully, Perhaps Their Joints Creak." The Paleozoic 6: Cambrian → Ordovician → Silurian → Devonian → Carboniferous → Permian.',
        flashcard={
            'front': 'What was the Cambrian explosion, and why is the Burgess Shale so important?',
            'back': 'The Cambrian explosion (~542-488 Mya) was a relatively brief geological interval when most major animal PHYLA first appear in the fossil record. It represents a rapid burst of body-plan diversification: trilobites, early arthropods, brachiopods, mollusks, chordates, echinoderms all show up in the Cambrian. The Burgess Shale (Canadian Rockies, 505 Mya) is one of the most important fossil sites on Earth because (1) it captures a snapshot of an entire Cambrian ecosystem, (2) the anoxic conditions from underwater mudslides preserved SOFT tissues — normally fossils only preserve hard parts, (3) it contains 65,000+ specimens representing 93 species, including bizarre forms like Hallucigenia, Opabinia, and Anomalocaris that have no close modern relatives. Because of its exceptional preservation, Burgess Shale is called a "Lagerstätte" (German: storage place).',
        },
        quiz={
            'question': 'The Devonian is called the "Age of Fishes," but which ADDITIONAL major vertebrate transition also occurred during the Devonian?',
            'correct': 'The first tetrapods appeared (~370 Mya), transitioning from lobe-finned fish to early limbed vertebrates capable of weight-bearing locomotion',
            'distractors': [
                'The first birds evolved from theropod dinosaurs, marking the origin of powered flight in vertebrates',
                'The first reptiles diverged into synapsids and sauropsids, establishing the lineages leading to mammals and modern reptiles',
                'The first bony fish (Osteichthyes) appeared, eventually displacing cartilaginous fish as the dominant vertebrate group',
            ],
        },
        visual={
            'type': 'timeline',
            'description': 'Paleozoic periods',
            'regions': [
                {'label': 'Cambrian (542-488)', 'color': '#e63946', 'items': ['Explosion', 'Burgess Shale', 'Trilobites']},
                {'label': 'Ordovician (488-444)', 'color': '#f77f00', 'items': ['Early bony fish', 'First land plants']},
                {'label': 'Silurian (444-416)', 'color': '#ffc857', 'items': ['First land animals', 'Millipedes']},
                {'label': 'Devonian (416-359)', 'color': '#7de2d1', 'items': ['Age of fishes', 'First tetrapods']},
                {'label': 'Carbon. (359-299)', 'color': '#4ea8de', 'items': ['Coal deposits', 'Amphibians dominate']},
                {'label': 'Permian (299-251)', 'color': '#8a5cf6', 'items': ['First reptiles', 'Synapsid/sauropsid split']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Cambrian Ordovician Silurian Devonian Carboniferous Permian.',
            'trap': 'The Permian ended with the LARGEST mass extinction in Earth\'s history (~251 Mya, ~96% of marine species lost) — even bigger than the K-T dinosaur extinction.',
        },
    ))

    # ---- Node 5: Mesozoic, K-T & Cenozoic (slides 31-36) ----
    sections = slides_to_sections(d, (31, 36))
    sections.append(audio_section(
        'Mesozoic + K-T boundary (recorded 2026-04-01)',
        APR1_MESOZOIC,
    ))
    sections.append(audio_section(
        'Cenozoic + take-home points (recorded 2026-04-01)',
        APR1_CENOZOIC,
    ))
    nodes.append(build_node(
        id='lec14-mesozoic-cenozoic',
        title='Mesozoic, K-T Extinction & Cenozoic',
        subtitle='Dinosaurs, asteroid, mammals, humans (Lec 14 slides 31-36)',
        color='red', row=12,
        heading='Lecture 14 — Mesozoic Era through the Present',
        sections=sections,
        examples=[
            'Triassic (250-202 Mya): first dinosaurs appear ~230 Mya. Dinosaurs dominate land up to ~65 Mya.',
            'Jurassic (202-145 Mya): dinosaur diversification. First mammals (~200-180 Mya, small, nocturnal). Birds arise within Dinosauria (~150 Mya, Archaeopteryx).',
            'Cretaceous (145-65 Mya): rise of flowering plants (~132 Mya). Coevolution of flowers and pollinators → massive insect diversification.',
            'K-T boundary (65 Mya): asteroid impact at Chicxulub, Yucatán. ~10-mile diameter asteroid, ~100 trillion tons TNT equivalent. Iridium-rich layer in rocks worldwide. Global climate change → extinction of non-avian dinosaurs and ~2/3 of all species.',
            'Cenozoic (65 Mya–now): mammals radiate into vacated niches. Primates (~50 Mya, squirrel-sized arboreal). Apes (~20 Mya) as climate cooled and grasslands spread.',
            'Hominins ~7 Mya (bipedal primates). Homo sapiens ~195,000 years ago (oldest known fossils).',
        ],
        warnings=[
            'Birds ARE dinosaurs. They are the only surviving dinosaur lineage. The phrase "dinosaurs went extinct" is only true for non-avian dinosaurs.',
            'The K-T boundary is now often called the K-Pg boundary (Cretaceous-Paleogene). "K" comes from German "Kreide" (chalk) because "C" was already taken by Cambrian.',
            'Mammals existed ALONGSIDE dinosaurs for ~150 million years — they just stayed small and nocturnal while dinosaurs dominated day and large-body niches.',
        ],
        mnemonic='K-T boundary: asteroid → iridium → Chicxulub crater → 2/3 extinction → mammalian radiation → us.',
        flashcard={
            'front': 'What is the evidence that the K-T extinction was caused by an asteroid impact?',
            'back': 'Multiple lines of evidence converge: (1) A thin global layer of IRIDIUM — an element rare on Earth but common in asteroids — is found in rocks worldwide at exactly 65 Mya, proposed by Walter and Luis Alvarez in 1980. (2) The Chicxulub crater (Yucatán, Mexico), ~180 km across, was identified in the 1990s and dates to precisely 65 Mya. (3) Shocked quartz and microtektites (glass spherules) from the impact are found in the boundary layer. (4) The impact size (~10 mile diameter asteroid) releases energy equivalent to ~100 trillion tons of TNT — enough to throw debris globally, trigger massive fires, and block sunlight for years. (5) The global extinction pattern matches an impact-driven climate collapse: 2/3 of all species lost, preferentially large-bodied animals and anything dependent on photosynthesis. The non-avian dinosaurs went extinct; birds (a dinosaur lineage) survived.',
        },
        quiz={
            'question': 'Why is iridium the "smoking gun" for the K-T extinction being caused by an asteroid?',
            'correct': 'Iridium is rare in Earth\'s crust but abundant in asteroids, and a global iridium layer dates to exactly 65 Mya',
            'distractors': [
                'Iridium is toxic to dinosaurs specifically',
                'Iridium only forms from impacts',
                'Iridium was used by dinosaurs for camouflage',
            ],
        },
        visual={
            'type': 'event',
            'description': 'K-T extinction mechanism',
            'regions': [
                {'label': 'Impact', 'color': '#e63946', 'items': ['~10 mi asteroid', 'Chicxulub crater', '100 T tons TNT']},
                {'label': 'Global effects', 'color': '#f77f00', 'items': ['Iridium layer', 'Wildfires', 'Cooling/darkness']},
                {'label': 'Extinction', 'color': '#6e6a80', 'items': ['Non-avian dinos', '2/3 of species', 'Large bodies first']},
                {'label': 'Cenozoic radiation', 'color': '#7de2d1', 'items': ['Mammals expand', 'Primates emerge', 'Us, eventually']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Asteroid → iridium → climate collapse → mammalian radiation.',
            'trap': 'The K-T event is only one of 5 MAJOR mass extinctions. The biggest was the end-Permian (~251 Mya), wiping ~96% of marine species. We may be entering a 6th (anthropogenic).',
        },
    ))

    return nodes


# --------------------------------------------------------------------------
# April 6 recording segments (Lec 15 - Phylogenetics)
# The 45,182-char transcript was split into 5 ~9k parts.
# --------------------------------------------------------------------------

# Segment A: phylogeny intro, tree components, snail island example
# (covers slides 1-12)
APR6_TREE_THINKING = APR6[0:12000]

# Segment B: synapomorphy, monophyletic vs paraphyletic, birds-as-reptiles
# (covers slides 13-22)
APR6_CLADISTICS = APR6[12000:22000]

# Segment C: parsimony, homoplasy, convergence, reversals, mammal/whale
# (covers slides 23-29)
APR6_HOMOPLASY = APR6[22000:30000]

# Segment D: fins-to-limbs, Coelacanth, Tiktaalik, Shubin prediction
# (covers slides 30-37)
APR6_FINS_LIMBS = APR6[30000:37000]

# Segment E: feathers, Archaeopteryx, velociraptor quill nodes, exaptation
# (covers slides 38-44)
APR6_FEATHERS = APR6[37000:]


def lec15_nodes():
    d = load_lec('lec15')
    nodes = []

    # ---- Node 1: Tree Thinking & Tree Components (slides 1-12) ----
    sections = slides_to_sections(d, (1, 12))
    sections.append(audio_section(
        'Tree thinking, snail island example (recorded 2026-04-06)',
        APR6_TREE_THINKING,
    ))
    nodes.append(build_node(
        id='lec15-tree-thinking',
        title='Tree Thinking: Phylogeny Basics',
        subtitle='Tips, nodes, clades, root (Lec 15 slides 1-12)',
        color='teal', row=13,
        heading='Lecture 15 — Phylogenetics: Reading Evolutionary Trees',
        sections=sections,
        examples=[
            'Tip: terminal ends of a tree — species, populations, or molecules being compared.',
            'Branch: lineage evolving through time between divergence events (speciation).',
            'Node: point where a lineage splits. Internal nodes = inferred common ancestors.',
            'Root: ancestor from which all other nodes descend. Usually chosen with an outgroup.',
            'Clade: an ancestor plus ALL of its descendants. A monophyletic group.',
            'Sister taxa: two lineages that share one immediate common ancestor (one node apart).',
            'Snail island example: populations can evolve in place (in situ) OR move to new islands. Current island 1 snails are NOT the direct ancestors of island 3 & 4 snails — evolution did not stop.',
        ],
        warnings=[
            'Trees can be drawn in MANY visual styles without changing the phylogeny. Rotations at any node are free — the topology is what matters.',
            'NEVER read trees left-to-right as "progress." Humans are NOT at the "tip" of evolution — every living species is equally "evolved."',
            'Tree orientation (horizontal, vertical, radial, circular) is a display choice, not a biological statement.',
        ],
        mnemonic='Tip, Branch, Node, Root, Clade — the five words that describe any tree.',
        flashcard={
            'front': 'Why is reading a phylogenetic tree left-to-right as "progress toward humans" (or any tip) a fundamental misconception?',
            'back': 'Phylogenetic trees show BRANCHING patterns of descent, not linear progress. Every species at the tips is equally "evolved" — they have all been evolving for the same amount of time since their last common ancestor. A tree can be rotated at ANY node without changing its biological meaning, which proves that the left-to-right order of tips has no biological significance. The "ladder of progress" or "scala naturae" view — where amoebae are "primitive" and humans are "advanced" — was explicitly rejected by Darwin, who famously wrote "never use the words higher and lower" in the margin of an early manuscript. Modern tree thinking requires reading from ROOT to TIPS, following actual ancestry, not left-to-right along the tips.',
        },
        quiz={
            'question': 'In a phylogenetic tree, what does a "node" represent?',
            'correct': 'A point where a lineage splits (a common ancestor and a speciation event)',
            'distractors': [
                'A living species',
                'A fossil specimen',
                'The root of the entire tree',
            ],
        },
        visual={
            'type': 'anatomy',
            'description': 'Parts of a phylogenetic tree',
            'regions': [
                {'label': 'Root', 'color': '#6e6a80', 'items': ['Common ancestor of everything shown']},
                {'label': 'Branch', 'color': '#4ea8de', 'items': ['Lineage through time']},
                {'label': 'Node', 'color': '#ffc857', 'items': ['Speciation', 'Common ancestor']},
                {'label': 'Tip', 'color': '#7de2d1', 'items': ['Species/population', 'Today']},
                {'label': 'Clade', 'color': '#8a5cf6', 'items': ['Ancestor + ALL descendants', 'Monophyletic']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Root → Branches → Nodes → Tips.',
            'trap': 'A "clade" must include ALL descendants. If you exclude some descendants (e.g., "reptiles minus birds"), it is PARAPHYLETIC — not a valid clade.',
        },
    ))

    # ---- Node 2: Cladistics & Synapomorphies (slides 13-22) ----
    sections = slides_to_sections(d, (13, 22))
    sections.append(audio_section(
        'Synapomorphy, mono- vs paraphyletic, character tables (recorded 2026-04-06)',
        APR6_CLADISTICS,
    ))
    nodes.append(build_node(
        id='lec15-cladistics-synapomorphy',
        title='Cladistics, Synapomorphies & Monophyletic Groups',
        subtitle='Shared derived characters build valid clades (Lec 15 slides 13-22)',
        color='blue', row=13,
        heading='Lecture 15 — Cladistics: Building Trees from Characters',
        sections=sections,
        examples=[
            'Systematics: the scientific field of classification.',
            'Synapomorphy: a shared derived character — inherited from a common ancestor by all descendants. The KEY tool for building clades.',
            'Ancestral characters (symplesiomorphies) are NOT informative for defining relationships within a group because EVERY member has them.',
            'Monophyletic group: an ancestor + ALL of its descendants. A valid clade.',
            'Paraphyletic group: an ancestor + SOME descendants. NOT a valid clade.',
            'Classic example: "reptiles" (excluding birds) is PARAPHYLETIC. To make it monophyletic, you must INCLUDE birds as reptiles — which is what modern taxonomy does (Aves is a lineage within Sauropsida).',
            'Character matrix: rows = taxa, columns = characters (wings, antennae, elytra, mandibles). Identical rows group together, with an outgroup to root the tree.',
            'With 5 taxa, there are 105 possible tree topologies. With 9 taxa, 2 million. With more, it becomes astronomical — requiring computers.',
        ],
        warnings=[
            '"Fish" as commonly used is paraphyletic — it excludes tetrapods (which descend from lobe-finned fish). A monophyletic "fish" group would include us.',
            'Morphological characters can mislead if based on ancestral features. Always use DERIVED characters for clade-building.',
            'Synapomorphy / homology / homoplasy — keep these terms straight. Homology = same due to common ancestry. Homoplasy = same NOT due to common ancestry.',
        ],
        mnemonic='Synapomorphy = Shared + Derived. Ancestral doesn\'t count, derived does.',
        flashcard={
            'front': 'Explain why "reptiles" (excluding birds) is a paraphyletic group, and how this violates cladistic principles.',
            'back': 'A MONOPHYLETIC group (clade) must include a common ancestor AND ALL of its descendants. "Reptiles" as traditionally defined (lizards, snakes, crocodiles, turtles, tuataras — but not birds) is PARAPHYLETIC because birds ARE direct descendants of the same reptilian ancestor that gave rise to crocodiles and dinosaurs. Phylogenetically, crocodiles are MORE closely related to birds than to lizards. To make "reptiles" monophyletic, birds MUST be included — hence modern taxonomy calls birds "avian reptiles" and places Aves within the clade Sauropsida/Archosauria. This is why cladists emphasize: definitions must reflect ACTUAL ancestry, not superficial similarity or traditional categories. "Fish" has the same problem — it excludes tetrapods, but tetrapods are descended from lobe-finned fish.',
        },
        quiz={
            'question': 'Why is "reptiles" (excluding birds) considered a paraphyletic group?',
            'correct': 'It excludes birds, which are direct descendants of the reptilian common ancestor',
            'distractors': [
                'Reptiles and birds evolved independently',
                'Reptiles are a monophyletic group by definition',
                'Birds diverged from mammals, not reptiles',
            ],
        },
        visual={
            'type': 'classification',
            'description': 'Monophyletic vs paraphyletic vs polyphyletic',
            'regions': [
                {'label': 'Monophyletic ✓', 'color': '#7de2d1', 'items': ['Ancestor + ALL descendants', 'Valid clade']},
                {'label': 'Paraphyletic ✗', 'color': '#ffc857', 'items': ['Ancestor + SOME descendants', 'e.g., "reptiles" (no birds)']},
                {'label': 'Polyphyletic ✗', 'color': '#e63946', 'items': ['Convergent lookalikes', 'Not descended from same ancestor']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Mono = all. Para = some. Poly = random.',
            'trap': 'Linnaean groupings (Class Reptilia, etc.) were often paraphyletic. Modern cladistics has forced many revisions.',
        },
    ))

    # ---- Node 3: Parsimony, Homoplasy & Convergence (slides 23-29) ----
    sections = slides_to_sections(d, (23, 29))
    sections.append(audio_section(
        'Parsimony, homoplasy, reversals, convergence, whale/squamate cases (recorded 2026-04-06)',
        APR6_HOMOPLASY,
    ))
    nodes.append(build_node(
        id='lec15-homoplasy-convergence',
        title='Parsimony, Homoplasy & Convergence',
        subtitle='When similarity LIES: reversals and convergent evolution (Lec 15 slides 23-29)',
        color='purple', row=13,
        heading='Lecture 15 — Testing Phylogenetic Hypotheses',
        sections=sections,
        examples=[
            'Principle of parsimony (Occam\'s razor): the tree requiring the FEWEST evolutionary steps is the best hypothesis (starting point).',
            'Phylogenetic trees are HYPOTHESES. New evidence can revise them — e.g., molecular data has reshuffled many morphological trees.',
            'Homoplasy: similarity NOT due to common ancestry. Two types: evolutionary reversal (return to ancestral state) and convergent evolution (independent origin of similar trait).',
            'Camera-eye convergence: vertebrate eyes and octopus eyes both have lens, retina, iris — but evolved INDEPENDENTLY (the tree shows separate origins requires fewer steps than "ancestral loss by all other groups").',
            'Mammal aquatic reversal: whales, dolphins, and dugongs are mammals that returned to water. Their closest living relatives are hippopotamuses (molecular and fossil evidence).',
            'Shark vs killer whale body shape: convergent, not related. Similar selective pressure (fast swimming) → similar form.',
            'Limblessness in squamates: EVOLVED INDEPENDENTLY in snakes, glass lizards, legless skinks, amphisbaenians. Some snakes still retain vestigial hind-limb spurs (boas, pythons).',
        ],
        warnings=[
            'Parsimony is a starting assumption, NOT a guarantee. Real evolution can take non-parsimonious routes (e.g., when selection pressure is strong or ancestral states are truly rare).',
            'Homoplasy is RAMPANT. Do not mistake convergent similarity for homology. Always test with independent character sets (morphology + molecules).',
            'Molecular data has overturned many morphology-based groupings. When molecular and morphological trees conflict, molecular trees are usually (but not always) more reliable.',
        ],
        mnemonic='Parsimony = fewest steps. Homoplasy = similarity that LIES (reversal or convergence).',
        flashcard={
            'front': 'How does the camera eye of vertebrates and octopuses illustrate both parsimony and convergent evolution?',
            'back': 'Both vertebrates and octopuses have complex camera eyes with a lens, retina, iris, and focusing mechanism. If camera eyes were HOMOLOGOUS (inherited from a common ancestor), then the common ancestor of vertebrates and cephalopods (~600 Mya) must have had a camera eye — and EVERY other lineage descending from that ancestor (arthropods, echinoderms, flatworms, annelids, etc.) must have LOST it. That would require many evolutionary steps. Under the CONVERGENT hypothesis, the camera eye evolved TWICE — once in the vertebrate lineage, once in the cephalopod lineage — requiring only 2 steps. Parsimony favors the convergent interpretation. Additionally, cephalopod eyes have their photoreceptors facing the light (better design), while vertebrate eyes have them facing backward (creating the blind spot) — strong evidence of independent origin through different evolutionary paths.',
        },
        quiz={
            'question': 'The principle of parsimony in phylogenetics states that:',
            'correct': 'The best hypothesis requires the fewest evolutionary steps',
            'distractors': [
                'The simplest organism is the ancestor',
                'Evolution always takes the shortest path',
                'Older lineages have fewer mutations',
            ],
        },
        visual={
            'type': 'comparison',
            'description': 'Homoplasy: reversal vs convergence',
            'regions': [
                {'label': 'Homology ✓', 'color': '#7de2d1', 'items': ['Same due to common ancestry', 'e.g., tetrapod limb bones']},
                {'label': 'Convergence (homoplasy)', 'color': '#f77f00', 'items': ['Independent origin', 'Similar pressure', 'e.g., octopus/vertebrate eye']},
                {'label': 'Reversal (homoplasy)', 'color': '#e63946', 'items': ['Derived → ancestral', 'e.g., snake limb loss']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Homology = real kinship. Homoplasy = false resemblance.',
            'trap': 'Two species sharing a trait does NOT prove common ancestry. Always test with multiple independent characters.',
        },
    ))

    # ---- Node 4: Fins to Limbs & Tiktaalik (slides 30-37) ----
    sections = slides_to_sections(d, (30, 37))
    sections.append(audio_section(
        'Coelacanths, Tiktaalik, Shubin prediction (recorded 2026-04-06)',
        APR6_FINS_LIMBS,
    ))
    nodes.append(build_node(
        id='lec15-fins-to-limbs',
        title='Fins to Limbs: Tiktaalik as Transitional Fossil',
        subtitle='Phylogenies generate TESTABLE predictions (Lec 15 slides 30-37)',
        color='amber', row=13,
        heading='Lecture 15 — The Vertebrate Transition to Land',
        sections=sections,
        examples=[
            'Coelacanths: lobe-finned fish thought extinct since Cretaceous — found ALIVE in 1938 off South Africa. Living fossil, close living relative of tetrapods.',
            'Lobe-finned fish have fin bones HOMOLOGOUS to tetrapod limb bones (humerus, radius/ulna). They are cousins, not ancestors, but they preserve the transitional anatomy.',
            'Phylogenies generate HYPOTHESES. Given that tetrapods arose from lobe-finned fish in the Devonian (~370 Mya), transition fossils should exist in mid-Devonian coastal wetland rocks.',
            'Neil Shubin + Ted Daeschler searched exactly those rocks in Northern Canada (Ellesmere Island).',
            'Tiktaalik (2004): transitional fossil with weight-bearing elbows, bending wrist, neck (lost bony operculum), lateral line (still aquatic), eyes on top of head (looking up).',
            'Tiktaalik could do "push-ups" — support body weight on its pectoral fins. Probably not walking on land, but could prop itself at the water surface to look around.',
            'Transitional features: from fins → arms, from no neck → neck, from gills-only → lungs + gills, from aquatic ear → terrestrial ear.',
        ],
        warnings=[
            'Tiktaalik is NOT "our ancestor" in the strict sense — it\'s a cousin preserving transitional anatomy. The direct ancestor probably existed in the same environment but has not been found as a fossil.',
            '"Missing link" is a misleading phrase — evolution doesn\'t have a single chain of links. Tiktaalik is ONE of many transitional forms (Acanthostega, Ichthyostega, Eusthenopteron all show stages).',
        ],
        mnemonic='Phylogeny → prediction → dig in the right rocks → Tiktaalik (2004). Science works.',
        flashcard={
            'front': 'How did Neil Shubin use phylogenetic reasoning to predict where transitional fish-to-tetrapod fossils would be found?',
            'back': 'Shubin and Daeschler reasoned: (1) Tetrapods (4-legged vertebrates) are closely related to lobe-finned fish based on phylogenetic analysis and existing fossil evidence. (2) The transition fish → tetrapod must have occurred during the mid-to-late DEVONIAN period (~380-360 Mya) based on the age of known early tetrapod fossils (Acanthostega, Ichthyostega). (3) The environment where this transition occurred should be COASTAL WETLANDS — shallow, warm, freshwater habitats where a transitional animal could benefit from push-up style locomotion. (4) Therefore, they needed to find mid-Devonian COASTAL WETLAND rocks that were accessible. They found exactly that in Northern Canada (Ellesmere Island, Nunavut). After multiple field seasons, in 2004 they discovered TIKTAALIK — a fish with weight-bearing elbows, bending wrist, a NECK (loss of bony operculum), and other "fishapod" features. This was a triumph of phylogenetically-guided prediction: science using theory to direct empirical discovery, rather than stumbling upon fossils by accident.',
        },
        quiz={
            'question': 'Which Tiktaalik feature most strongly suggests it could support its body weight?',
            'correct': 'Weight-bearing elbows and a bending wrist',
            'distractors': [
                'A dorsal fin',
                'A long tail',
                'Scales covering its body',
            ],
        },
        visual={
            'type': 'transition',
            'description': 'Fin-to-limb transition',
            'regions': [
                {'label': 'Lobe-finned fish', 'color': '#4ea8de', 'items': ['Bony fin bones', 'No neck', 'Fully aquatic']},
                {'label': 'Tiktaalik', 'color': '#ffc857', 'items': ['Weight-bearing elbows', 'Bending wrist', 'Neck, no operculum', 'Top-of-head eyes']},
                {'label': 'Early tetrapods', 'color': '#7de2d1', 'items': ['Acanthostega, Ichthyostega', 'True limbs with digits', 'Mostly aquatic']},
                {'label': 'Modern tetrapods', 'color': '#8a5cf6', 'items': ['Limbs, digits', 'Fully terrestrial capable']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fins → Fishapod (Tiktaalik) → Limbs.',
            'trap': 'Tiktaalik was NOT a land-walker. It still had gills, a lateral line, and was aquatic. "Walking on land" came later with Acanthostega and Ichthyostega.',
        },
    ))

    # ---- Node 5: Feathers, Archaeopteryx & Exaptation (slides 38-44) ----
    sections = slides_to_sections(d, (38, 44))
    sections.append(audio_section(
        'Feathers before flight, Velociraptor quill nodes, exaptation, swim bladder (recorded 2026-04-06)',
        APR6_FEATHERS,
    ))
    nodes.append(build_node(
        id='lec15-feathers-exaptation',
        title='Feathers Evolved BEFORE Flight: Exaptation',
        subtitle='Archaeopteryx, quill nodes, swim bladder (Lec 15 slides 38-44)',
        color='coral', row=13,
        heading='Lecture 15 — Phylogenies Track Trait Evolution',
        sections=sections,
        examples=[
            'Archaeopteryx (discovered 1860, ~145 Mya): classic transitional form between theropod dinosaurs and modern birds. Has feathers AND teeth, claws on wings, long bony tail.',
            'Feathered non-flying dinosaurs: Velociraptor, Oviraptor, Tyrannosauroid relatives — small arms, could NOT have used feathers for flight. Feathers preceded flight.',
            'Pre-flight feather functions: species recognition, mate attraction (color), insulation, egg incubation (Oviraptor was found brooding eggs, 1993).',
            'Quill nodes: regularly-spaced bumps on the ulna where feather quills attach. Found on modern bird bones (turkey vulture example) AND on Velociraptor ulna fossils — direct evidence of feather attachment in non-flying dinosaurs.',
            'Exaptation: a trait that originally evolved for one function, later co-opted for a NEW function. Feathers (insulation) → flight. Not the same as adaptation (trait evolved FOR its current function).',
            'Another exaptation: swim bladders are HOMOLOGOUS to lungs. The earliest fish had primitive lungs to gulp air at the surface in low-oxygen water. Tetrapods kept lungs; many fish modified lungs into gas-filled buoyancy organs (swim bladders).',
            'Flight stroke may have evolved as running-assist (flapping while chasing prey or escaping predators) — wing-assisted incline running (WAIR) is hypothesized as the bridge.',
        ],
        warnings=[
            'Exaptation does NOT require gene duplication (unlike co-option at the molecular level). The same structure is REPURPOSED without gaining a copy.',
            'Birds ARE dinosaurs (theropod dinosaurs, specifically). They are the only surviving dinosaur lineage.',
            'Do not confuse exaptation with LAMARCKISM. The feather-to-flight transition was driven by SELECTION at each stage, not by an organism "striving" toward flight.',
        ],
        mnemonic='Exaptation = "ex-adaptation" — same trait, NEW function. Feathers → insulation → FLIGHT.',
        flashcard={
            'front': 'What is exaptation, and how do feathers illustrate this concept?',
            'back': 'EXAPTATION is a trait that originally evolved via selection for ONE function, but was later CO-OPTED for a different function — with or without further modification. Coined by Gould and Vrba in 1982. Feathers are the classic example: early theropod dinosaurs (long before birds and flight) had feathers that likely served INSULATION (keeping warm in cold climates, since many were small) and/or DISPLAY (mate attraction, species recognition, egg incubation). Evidence: (1) Feathered non-flying dinosaurs like Velociraptor and Sinosauropteryx, which had arms too short to fly. (2) Oviraptor fossils found brooding their eggs (1993) — feathers useful for insulation. (3) Velociraptor ulna shows QUILL NODES — regularly-spaced bumps where feathers attached, matching modern birds. Flight evolved LATER, using the already-present feathers. Another example: swim bladders are HOMOLOGOUS to lungs — early fish used primitive lungs to gulp air at the surface; many fish lineages later repurposed those lungs into buoyancy organs. Exaptation is crucial because it explains how complex adaptations can "sneak up" on a new function.',
        },
        quiz={
            'question': 'Why is the evolution of feathers considered an example of EXAPTATION rather than adaptation for flight?',
            'correct': 'Feathers evolved first for other functions (insulation, display), then were co-opted for flight',
            'distractors': [
                'Feathers are made of the same protein as scales',
                'All dinosaurs had feathers',
                'Flight evolved before feathers',
            ],
        },
        visual={
            'type': 'exaptation',
            'description': 'Feather functional evolution',
            'regions': [
                {'label': 'Origin', 'color': '#6e6a80', 'items': ['Small theropods', 'Insulation, display']},
                {'label': 'Expansion', 'color': '#ffc857', 'items': ['Egg incubation', 'Larger feathers', 'Quill nodes on ulna']},
                {'label': 'Flight stroke', 'color': '#f77f00', 'items': ['WAIR hypothesis', 'Running-assist', 'Escape predators']},
                {'label': 'True flight', 'color': '#7de2d1', 'items': ['Archaeopteryx ~145 Mya', 'Modern birds']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Insulation → Display → Running-assist → Flight. Exaptation every step.',
            'trap': 'Do NOT say "feathers evolved FOR flight." That is a teleological error. Feathers evolved for OTHER reasons and were LATER useful for flight.',
        },
    ))

    return nodes
