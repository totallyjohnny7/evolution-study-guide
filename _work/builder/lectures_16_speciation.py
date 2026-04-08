"""Chapter 13 — Species Concepts, Reproductive Isolation & Speciation.

4 nodes targeting BIOL 4340 Exam 3 / Final exam coverage:
  ch13-species-concepts    — BSC, PSC, General Lineage Concept
  ch13-isolating-barriers  — Prezygotic (6 types) + Postzygotic (3 types)
  ch13-speciation-modes    — Allopatric, Parapatric, Sympatric, Ecological, Allopolyploidy
  ch13-bdm-cryptic         — BDM incompatibilities + Cryptic species + Bacteria problem

All nodes assigned row=14 (FINAL — SPECIATION & BIOGEOGRAPHY).
"""

from helpers import build_node
from ch13_svgs import (
    SVG_FIG_13_4, SVG_FIG_13_7, SVG_FIG_13_8, SVG_FIG_13_9, SVG_FIG_13_10,
    SVG_FIG_13_11, SVG_FIG_13_13, SVG_FIG_13_14, SVG_FIG_13_15, SVG_FIG_13_16,
    SVG_FIG_13_17, SVG_FIG_13_18, SVG_FIG_13_19, SVG_FIG_13_22,
)


def ch13_nodes():
    nodes = []

    # ------------------------------------------------------------------ #
    # NODE 1 — Species Concepts (BSC / PSC / General Lineage)
    # ------------------------------------------------------------------ #
    nodes.append(build_node(
        id='ch13-species-concepts',
        title='Species Concepts — The Big Three',
        subtitle='BSC vs PSC vs General Lineage: limits and when each works (Ch 13)',
        color='teal',
        row=14,
        heading='Chapter 13 — Species Concepts',
        sections=[
            {
                'label': 'Biological Species Concept (BSC) — Ernst Mayr, 1942',
                'body': (
                    'Definition: A species = a group of actually or potentially interbreeding '
                    'populations that are reproductively isolated from other groups.\n\n'
                    'Focus: What KEEPS species apart — reproductive isolation mechanisms.\n'
                    'Key: if gene flow occurs between two populations, they are the same species.\n\n'
                    'LIMITS (exam targets):\n'
                    '• Useless for asexual organisms (bacteria, archaea, some lizards, bdelloid '
                    'rotifers) — no sex = no reproductive isolation = concept breaks down.\n'
                    '• Useless for allopatric populations (geographically separated) — cannot '
                    'test whether they WOULD interbreed. Example: North American elk vs European '
                    'red deer — can interbreed in captivity, but separated by an ocean.\n'
                    '• Useless for fossils — cannot test mating behavior in dead organisms.'
                ),
            },
            {
                'label': 'Phylogenetic Species Concept (PSC)',
                'body': (
                    'Definition: A species = the SMALLEST monophyletic group (clade) descended '
                    'from a common ancestor, diagnosably distinct from other groups by at least '
                    'one shared derived character (synapomorphy).\n\n'
                    'Focus: Evolutionary history — look at the tips of the phylogenetic tree.\n\n'
                    'LIMITS:\n'
                    '• Tends to OVERSPLIT — any uniquely derived lineage qualifies as a species, '
                    'producing far more "species" than BSC would recognize.\n'
                    '• Creates thousands of microspecies that can be impractical for conservation '
                    '(too many units to track and fund).\n'
                    '• Works for asexuals and fossils unlike BSC.'
                ),
            },
            {
                'label': 'General Lineage Species Concept — Kevin de Queiroz',
                'body': (
                    'Definition: A species = a METAPOPULATION of organisms that exchange alleles '
                    'frequently enough to be the same gene pool and the same independently '
                    'evolving lineage.\n\n'
                    'Key term — METAPOPULATION: spatially separated subpopulations that interact '
                    'and exchange alleles at some rate.\n\n'
                    'Why it is the modern standard:\n'
                    '• Measurable with GENOMIC DATA — quantify actual gene flow between populations.\n'
                    '• Best for identifying CRYPTIC SPECIES: organisms that look identical but '
                    'are genetically distinct, separately evolving lineages.\n\n'
                    'LIMITS: Requires sequencing data; harder to apply directly in field conditions.'
                ),
            },
            {
                'label': 'Comparison Table',
                'body': (
                    'Concept          | Key Criterion          | Asexual? | Fossils? | Splits?  \n'
                    '-----------------|------------------------|----------|----------|---------\n'
                    'BSC (Mayr)       | Reproductive isolation | NO       | NO       | Lumper  \n'
                    'PSC              | Smallest monophyletic  | YES      | YES      | Splitter\n'
                    'General Lineage  | Same gene pool/lineage | YES      | NO       | Moderate\n\n'
                    'Bottom line: No single concept works for all life. The common thread: '
                    'species = independently evolving lineages.'
                ),
            },
        ],
        quotes=[
            '"Species are groups of actually or potentially interbreeding natural populations '
            'which are reproductively isolated from other such groups." — Ernst Mayr, 1942',
        ],
        examples=[
            'BSC failure — Asexual: Bdelloid rotifers reproduce entirely asexually. '
            'Under BSC, every individual would be its own "species." Concept is inapplicable.',
            'BSC failure — Allopatry: Elk (North America) and red deer (Europe) can interbreed '
            'in captivity. BSC cannot classify them without geographic context.',
            'PSC success — Cryptic bird species: Willow flycatcher and Alder flycatcher look '
            'identical but differ in song and are reproductively isolated — PSC correctly '
            'separates them; BSC also works here but requires behavioral data.',
            'General Lineage success — Anopheles mosquitoes: The Anopheles gambiae complex '
            'contains 7 cryptic species invisible to morphology but distinguished by genomics. '
            'Matters enormously for malaria vector control.',
        ],
        warnings=[
            'EXAM TRAP: BSC fails for BOTH asexual organisms AND allopatric populations — '
            '"both b and c" type answers are common.',
            'Reproductive isolation ≠ morphological difference. Cryptic species are '
            'reproductively isolated but look identical.',
            '"Potentially interbreeding" in the BSC definition means would interbreed if '
            'they came into contact — but this is untestable for many allopatric pairs.',
        ],
        mnemonic=(
            'BSC = "Mayr says you gotta bang to be the same gang" (gene flow = same species). '
            'PSC = "unique branch = your own species." '
            'General Lineage = "same gene pool, same team."'
        ),
        flashcard={
            'front': 'What are the three main species concepts and a key failure of each?',
            'back': (
                'BSC (Mayr 1942): species = interbreeding + reproductively isolated. '
                'FAILS for asexual organisms (no sex = no concept) and allopatric populations '
                '(cannot test potential interbreeding across geographic gaps). Also fails for fossils.\n\n'
                'PSC: species = smallest monophyletic group with a diagnosable synapomorphy. '
                'FAILS by oversplitting — every uniquely derived lineage qualifies, producing '
                'impractically many species units.\n\n'
                'General Lineage (de Queiroz): species = same metapopulation / gene pool / '
                'independently evolving lineage. Best for genomic era — works for asexuals, '
                'best for cryptic species. FAILS without molecular data.'
            ),
        },
        quiz={
            'question': (
                'A population of bacteria divides asexually. Which species concept CANNOT '
                'be applied to determine if two bacterial populations are different species?'
            ),
            'correct': 'Biological Species Concept — requires interbreeding, impossible for asexual organisms',
            'distractors': [
                'Phylogenetic Species Concept — based on shared derived characters, works for asexuals',
                'General Lineage Concept — based on gene pool boundaries, works for asexuals',
                'Morphological Species Concept — based on physical features, works for all organisms',
            ],
        },
        visual={
            'type': 'side-by-side',
            'description': 'Three species concepts: what each measures and where each fails',
            'regions': [
                {
                    'label': 'BSC (Mayr)',
                    'color': '#00c9a7',
                    'items': [
                        'Gene flow = same species',
                        'Reproductive isolation = different species',
                        'FAILS: asexuals, allopatry, fossils',
                        '"Gotta bang to be same gang"',
                    ],
                },
                {
                    'label': 'PSC',
                    'color': '#7c6cf7',
                    'items': [
                        'Monophyletic + synapomorphy',
                        'Works for asexuals & fossils',
                        'FAILS: oversplits drastically',
                        '"Unique branch = own species"',
                    ],
                },
                {
                    'label': 'General Lineage',
                    'color': '#4ea8de',
                    'items': [
                        'Same metapopulation / gene pool',
                        'Best for genomics era',
                        'Best for cryptic species',
                        '"Same gene pool = same team"',
                    ],
                },
            ],
            'arrows': [],
            'tooltips': [
                {
                    'term': 'metapopulation',
                    'plain': 'Spatially separated subpopulations that interact and exchange alleles at some rate — key term for General Lineage Concept.',
                },
                {
                    'term': 'cryptic species',
                    'plain': 'Species that look morphologically identical but are genetically distinct independently evolving lineages — detected only by genomics.',
                },
            ],
            'mnemonic': 'BSC = bang. PSC = branch. General = gene pool.',
            'trap': (
                'BSC says BOTH asexual organisms AND allopatric populations are problematic — '
                'not just one of them. Know both failure modes.'
            ),
        },
    ))

    # ------------------------------------------------------------------ #
    # NODE 2 — Isolating Barriers (all 9 mechanisms)
    # ------------------------------------------------------------------ #
    nodes.append(build_node(
        id='ch13-isolating-barriers',
        title='Reproductive Isolating Barriers',
        subtitle='Pre-mating → post-mating prezygotic → postzygotic — 9 mechanisms (Ch 13)',
        color='orange',
        row=14,
        heading='Chapter 13 — Reproductive Isolating Barriers',
        sections=[
            {
                'label': 'The Reproductive Timeline Framework',
                'body': (
                    'Reproductive isolation = anything that reduces or blocks gene flow between populations.\n\n'
                    'Timeline:\n'
                    'FIND MATE → MATE → TRANSFER GAMETES → FERTILIZATION → ZYGOTE → EMBRYO → OFFSPRING\n'
                    '     ↑ PREZYGOTIC barriers (before zygote)          ↑ POSTZYGOTIC barriers (after)\n\n'
                    'Geographic barriers (rivers, mountains, oceans) = EXTRINSIC/abiotic.\n'
                    'Reproductive barriers = INTRINSIC/biological.\n\n'
                    'Key: geographic isolation ALONE does not create new species under BSC. '
                    'Reproductive isolation must also develop.'
                ),
            },
            {
                'label': 'Prezygotic Barriers — Pre-Mating (before gametes transfer)',
                'body': (
                    '1. BEHAVIORAL ISOLATION — individuals not attracted to heterospecific signals.\n'
                    '   Example: firefly flash patterns are species-specific; wrong flash = no mate.\n\n'
                    '2. HABITAT ISOLATION — species breed in different microhabitats in the same area.\n'
                    '   Example: one frog breeds in ponds, another in streams — same forest, never meet.\n\n'
                    '3. TEMPORAL ISOLATION — species breed at different times (seasons or time of day).\n'
                    '   Example: coral species release gametes at dawn vs dusk — never mix.\n\n'
                    '4. POLLINATOR ISOLATION (plants) — different pollinators used, or pollen deposited\n'
                    '   on different body parts of the same pollinator. Pollen never reaches wrong stigma.\n\n'
                    '5. MECHANICAL ISOLATION — reproductive structures physically incompatible.\n'
                    '   Example: duck genitalia are notoriously species-specific (anatomical lock-and-key).'
                ),
            },
            {
                'label': 'Prezygotic Barriers — Post-Mating (gametes transferred, fertilization blocked)',
                'body': (
                    '6. GAMETIC INCOMPATIBILITY — sperm reaches egg but CANNOT fertilize it.\n'
                    '   Mechanism: sperm-egg binding proteins are species-specific (lock-and-key).\n'
                    '   Example: sea urchins and abalone — heterospecific sperm cannot penetrate the\n'
                    '   egg coat because bindin/VERL proteins don\'t match.\n'
                    '   Also: female immune cells can attack and destroy foreign sperm.\n\n'
                    '   EXAM TRAP: Gametic ≠ mechanical (wrong genitalia) ≠ habitat (species don\'t meet).\n'
                    '   Gametic incompatibility = sperm ARRIVES but FAILS to fertilize.'
                ),
            },
            {
                'label': 'Postzygotic Barriers — After Zygote Forms',
                'body': (
                    '7. HYBRID INVIABILITY — hybrid embryo develops abnormally and dies before\n'
                    '   reaching reproductive maturity. Diverged alleles from two genomes cannot\n'
                    '   cooperate in development.\n\n'
                    '8. HYBRID STERILITY — hybrid survives and is healthy, but cannot reproduce.\n'
                    '   Example: MULE (horse × donkey). Horse 2n=64, donkey 2n=62 → mule has 63\n'
                    '   chromosomes. Cannot pair in meiosis → completely sterile.\n'
                    '   Why it blocks gene flow: mules cannot breed back into either population.\n\n'
                    '9. HYBRID BREAKDOWN — F1 hybrids are viable/fertile, but F2 generation shows\n'
                    '   reduced fitness. Recombination exposes incompatible allele combinations.'
                ),
            },
            {
                'label': 'BDM Incompatibilities — The Molecular Mechanism',
                'body': (
                    'Bateson-Dobzhansky-Muller (BDM) incompatibilities = the molecular basis for\n'
                    'hybrid inviability and sterility.\n\n'
                    'HOW IT WORKS:\n'
                    '• Population A diverges and fixes allele A (always paired with ancestral b → fine).\n'
                    '• Population B diverges and fixes allele B (always paired with ancestral a → fine).\n'
                    '• Hybrid inherits both A + B together → EPISTATIC INCOMPATIBILITY → broken fitness.\n'
                    '• Allele A never "met" allele B during either population\'s evolution — they are\n'
                    '  incompatible even though each is fine on its own.\n\n'
                    'Real example: Mimulus guttatus × M. nasutus (monkeyflowers).\n'
                    '  Two loci: Hms1 + Hms2. Hms1 from M. guttatus + Hms2 from M. nasutus → sterile pollen.\n'
                    '  Neither locus is broken alone — only the combination is lethal.\n\n'
                    'Mnemonic: "BDM = Broken-Dick Mating — genes that never co-evolved are incompatible."'
                ),
            },
            {
                'label': 'Which Barrier Evolves Faster?',
                'body': (
                    'PREZYGOTIC isolation evolves FASTER than postzygotic.\n\n'
                    'Evidence: Coyne & Orr studied Drosophila pairs at different degrees of genetic\n'
                    'divergence. Prezygotic barriers accumulate more quickly than postzygotic barriers.\n\n'
                    'Why: Behavioral/habitat barriers can evolve rapidly under direct selection\n'
                    '(especially reinforcement — selection AGAINST hybrids drives stronger prezygotic\n'
                    'barriers). BDM incompatibilities require specific multi-locus evolutionary changes\n'
                    'that take longer to accumulate.\n\n'
                    'EXAM TRAP: "Postzygotic evolves faster" → FALSE. Prezygotic is faster.'
                ),
            },
        ],
        quotes=[],
        examples=[
            'Behavioral isolation — firefly flash patterns: each species has a species-specific '
            'flash pattern and interval. Females only respond to conspecific patterns → classic '
            'pre-mating behavioral barrier.',
            'Gametic incompatibility — sea urchins: Strongylocentrotus purpuratus and S. franciscanus '
            'can be found in the same tide pools. Heterospecific sperm cannot penetrate the egg coat '
            'because the bindin protein (sperm) doesn\'t match the receptor on the egg surface.',
            'Hybrid sterility — mule: Horse (2n=64) × donkey (2n=62) = mule (2n=63). The odd '
            'chromosome number prevents proper meiosis. Mules are vigorous but completely sterile — '
            'no gene flow returns to either parent species.',
            'BDM — Mimulus monkeyflowers: Two specific gene loci (Hms1, Hms2) each function '
            'normally in their own species but produce sterile pollen when combined from different '
            'species. Discovered by Sweigart & Willis.',
        ],
        warnings=[
            'EXAM TRAP: "Which is NOT a pre-mating prezygotic barrier?" — Hybrid sterility is '
            'POSTZYGOTIC, not pre-mating. Gametic incompatibility is POST-mating prezygotic.',
            'Geographic isolation = extrinsic, not a reproductive barrier. Alone, it does not '
            'make two populations separate species under BSC.',
            'Prezygotic barriers evolve FASTER than postzygotic (Coyne & Orr Drosophila data).',
            'Gametic incompatibility: sperm physically arrives at the egg — it just cannot '
            'fertilize it. This is different from mechanical isolation (genitalia incompatibility).',
        ],
        mnemonic=(
            'Timeline: FIND → MATE → GAMETES → ZYGOTE → EMBRYO → OFFSPRING\n'
            'Barriers before ZYGOTE = PRE-zygotic. After ZYGOTE = POST-zygotic.\n'
            'Pre-mating types: "Be Happy To Play Music" = Behavioral, Habitat, Temporal, '
            'Pollinator, Mechanical.\n'
            'Post-mating prezygotic: Gametic incompatibility.\n'
            'Postzygotic: Inviability, Sterility, Breakdown.'
        ),
        flashcard={
            'front': (
                'What is the difference between hybrid inviability, hybrid sterility, '
                'and hybrid breakdown?'
            ),
            'back': (
                'HYBRID INVIABILITY: The hybrid embryo forms but dies before reaching '
                'reproductive age. Genomes from diverged species cannot cooperate in development.\n\n'
                'HYBRID STERILITY: The hybrid survives and is healthy but CANNOT REPRODUCE. '
                'Classic example: mule (horse × donkey) — vigorous animal, completely sterile '
                'because 63 chromosomes cannot pair in meiosis.\n\n'
                'HYBRID BREAKDOWN: F1 hybrids are fine, but F2 generation (offspring of hybrids) '
                'shows reduced viability/fertility as recombination exposes incompatible allele '
                'combinations that were masked in F1.\n\n'
                'All three are POSTZYGOTIC barriers — fertilization succeeded, but something '
                'goes wrong afterward.'
            ),
        },
        quiz={
            'question': (
                'Sea urchin sperm from species A reaches the egg of species B but cannot '
                'penetrate the egg coat. This is an example of:'
            ),
            'correct': 'Gametic incompatibility — a post-mating prezygotic barrier',
            'distractors': [
                'Mechanical isolation — reproductive structures are physically incompatible',
                'Hybrid inviability — the hybrid embryo dies after fertilization',
                'Behavioral isolation — species do not recognize each other as mates',
            ],
        },
        visual={
            'type': 'timeline',
            'description': 'Reproductive isolation barriers mapped to the reproductive sequence',
            'svg': SVG_FIG_13_7,
            'extraSvgs': [
                {'title': 'Fig 13.4 — Temporal Isolation: Coral Spawning Histogram', 'svg': SVG_FIG_13_4},
                {'title': 'Fig 13.14 — Reproductive Isolation vs Genetic Distance (Coyne & Orr 2004)', 'svg': SVG_FIG_13_14},
            ],
            'regions': [
                {
                    'label': 'PRE-MATING PREZYGOTIC',
                    'color': '#00c9a7',
                    'items': [
                        '1. Behavioral',
                        '2. Habitat',
                        '3. Temporal',
                        '4. Pollinator',
                        '5. Mechanical',
                    ],
                },
                {
                    'label': 'POST-MATING PREZYGOTIC',
                    'color': '#ffc857',
                    'items': [
                        '6. Gametic incompatibility',
                        '(sperm arrives, fails to fertilize)',
                    ],
                },
                {
                    'label': 'POSTZYGOTIC',
                    'color': '#e63946',
                    'items': [
                        '7. Hybrid inviability',
                        '8. Hybrid sterility (mule)',
                        '9. Hybrid breakdown (F2)',
                    ],
                },
            ],
            'arrows': [],
            'tooltips': [
                {
                    'term': 'BDM incompatibility',
                    'plain': 'Bateson-Dobzhansky-Muller: alleles that each work fine alone become '
                             'incompatible together in a hybrid because they never co-evolved.',
                },
                {
                    'term': 'reinforcement',
                    'plain': 'Natural selection strengthens prezygotic barriers when hybrids are unfit — '
                             'explains why prezygotic evolves faster in sympatry.',
                },
            ],
            'mnemonic': '"Be Happy To Play Music" for pre-mating prezygotic barriers.',
            'trap': (
                'Prezygotic evolves FASTER than postzygotic. '
                'Gametic incompatibility is PREZYGOTIC even though mating already occurred.'
            ),
        },
    ))

    # ------------------------------------------------------------------ #
    # NODE 3 — Speciation Modes
    # ------------------------------------------------------------------ #
    nodes.append(build_node(
        id='ch13-speciation-modes',
        title='Speciation Models',
        subtitle='Allopatric, parapatric, sympatric, ecological + allopolyploidy (Ch 13)',
        color='purple',
        row=14,
        heading='Chapter 13 — Speciation Models',
        sections=[
            {
                'label': 'Speciation = Cladogenesis — The 4 Stages',
                'body': (
                    'Speciation = cladogenesis — one lineage splits into two or more independently\n'
                    'evolving lineages.\n\n'
                    'Stage 1: Continuous gene flow, no barriers — one species.\n'
                    'Stage 2: Minor barriers emerge → partial genetic discontinuity.\n'
                    'Stage 3: Stronger barriers → more discontinuity (still reversible).\n'
                    'Stage 4: Complete, IRREVERSIBLE reproductive isolation = new species.\n\n'
                    'Key: If secondary contact occurs BEFORE stage 4, gene flow can erase divergence\n'
                    'and populations remerge into one species.'
                ),
            },
            {
                'label': 'Allopatric Speciation — Most Common',
                'body': (
                    'What: A GEOGRAPHIC BARRIER splits a population. Both halves evolve independently\n'
                    'via drift, mutation, and selection. Eventually diverge enough that reproductive\n'
                    'isolation develops — even if the barrier later disappears.\n\n'
                    'Order of events:\n'
                    '  Geographic separation → Genetic divergence → Reproductive isolation\n\n'
                    'Example: A river shifts and cuts across a salamander population. Two halves\n'
                    'accumulate different alleles over thousands of generations. River dries up —\n'
                    'they meet again but don\'t recognize each other as mates. → New species.\n\n'
                    'Why most common: geographic barriers are abundant; they stop ALL gene flow\n'
                    'simultaneously, making divergence most efficient.'
                ),
            },
            {
                'label': 'Parapatric Speciation',
                'body': (
                    'What: Barrier only PARTIALLY separates populations — gene flow is reduced but\n'
                    'not eliminated. Populations at the contact zone can still interbreed, but diverge\n'
                    'if selection + drift are STRONGER than the gene flow keeping them connected.\n\n'
                    'When it works: Strong differential selection across a habitat gradient (e.g.,\n'
                    'different soil types, elevations) can overcome low-level gene flow.\n\n'
                    'Example: Heavy-metal tolerant plant populations at mine tailings adjacent to\n'
                    'normal soil populations — diverge despite some pollen exchange at the boundary.'
                ),
            },
            {
                'label': 'Sympatric Speciation',
                'body': (
                    'What: NO geographic barrier. Same location. Individuals begin mating\n'
                    'nonrandomly — preferring genetically or phenotypically similar mates.\n'
                    'Two groups diverge in the same geographic range.\n\n'
                    'Mechanism: Disruptive selection + assortative mating.\n\n'
                    'Classic example: Rhagoletis flies\n'
                    '• Originally bred exclusively on hawthorn trees in North America.\n'
                    '• ~150 years ago, some individuals switched to apple trees (an introduced species).\n'
                    '• Now: hawthorn-race and apple-race flies prefer their own host species.\n'
                    '• Same field, different host = assortative mating = reproductive isolation beginning.\n'
                    '• No geographic barrier — FULLY SYMPATRIC.\n\n'
                    'Why controversial: Requires strong disruptive selection to overcome the\n'
                    'homogenizing effect of gene flow within the same range. Hardest model to prove.'
                ),
            },
            {
                'label': 'Ecological Speciation',
                'body': (
                    'What: Reproductive barriers evolve as a BYPRODUCT of adapting to different\n'
                    'environments or ecological niches.\n\n'
                    'Two populations specialize on different prey, soil types, host plants, etc.\n'
                    'This: (1) reduces contact between them, (2) makes hybrids unfit for either niche,\n'
                    '(3) may trigger REINFORCEMENT — selection strengthens prezygotic barriers further\n'
                    'to avoid producing unfit hybrids.\n\n'
                    'Key: Reproductive isolation emerges FROM ecological divergence, not random drift.\n\n'
                    'ISOLATION BY DISTANCE: No explicit barrier, but individuals disperse only short\n'
                    'distances. Gene flow decreases as a function of distance across the range.\n'
                    'Populations near each other = genetically similar; far apart = divergent.'
                ),
            },
            {
                'label': 'Allopolyploidy — Instant Speciation (mostly plants)',
                'body': (
                    'What: Two DIFFERENT species hybridize. Hybrid is sterile (chromosomes from two\n'
                    'species cannot pair in meiosis). But if the hybrid ACCIDENTALLY DUPLICATES its\n'
                    'entire genome, every chromosome now has a pairing partner → meiosis works →\n'
                    'NEW SPECIES potentially in ONE GENERATION.\n\n'
                    'Step-by-step:\n'
                    '  Species A (2n=4) × Species B (2n=6)\n'
                    '  → Sterile hybrid (2n=5, chromosomes cannot pair)\n'
                    '  → Genome doubling\n'
                    '  → Fertile allotetraploid (2n=10, all chromosomes paired)\n'
                    '  = NEW SPECIES\n\n'
                    'Real example: Tragopogon salsify (plants, North America)\n'
                    '  T. dubius × T. pratensis → new species T. miscellus (~100 years ago)\n'
                    '  T. dubius × T. porrifolius → new species T. mirus (~100 years ago)\n\n'
                    'Scale: POSSIBLY HALF of all ~300,000 flowering plant species originated through\n'
                    'allopolyploidy.\n\n'
                    'EXAM TRAP: "Allopolyploidy occurs ONLY in plants" → FALSE. Also found in\n'
                    'insects, fish, amphibians, and some mammals — just rare outside plants.'
                ),
            },
        ],
        quotes=[],
        examples=[
            'Allopatric — Galápagos finches: Ancestral finch population colonized islands. Each '
            'island population evolved independently. Secondary contact in some islands confirms '
            'reproductive isolation — separate species formed.',
            'Sympatric — Rhagoletis flies: Same geographic range; hawthorn-race and apple-race '
            'flies diverged within ~150 years of host shift. Host plant = assortative mating '
            'criterion → sympatric speciation in real time.',
            'Allopolyploidy — wheat: Bread wheat (Triticum aestivum, 6n=42) is a natural hybrid '
            'of three different grass species. Three rounds of hybridization + genome doubling '
            'over thousands of years produced the wheat we eat.',
            'Ecological speciation — threespine stickleback: Marine (open-water) and lake '
            '(benthic) ecotypes of Gasterosteus aculeatus have evolved reproductive isolation '
            'driven by divergent habitat use — a textbook ecological speciation example.',
        ],
        warnings=[
            'EXAM TRAP: "Geographic isolation = new species under BSC" — FALSE. Geographic '
            'isolation is necessary but NOT sufficient. Reproductive isolation must ALSO develop.',
            'EXAM TRAP: Allopatric speciation ORDER — Geographic separation → genetic divergence '
            '→ reproductive isolation. NOT "isolation develops first, THEN separation occurs."',
            'EXAM TRAP: Allopolyploidy is plants-only → FALSE. Rare but documented in insects, '
            'frogs, fish, and mammals.',
            'Sympatric speciation is the most CONTROVERSIAL model — requires strong '
            'disruptive selection within a single freely mixing population.',
        ],
        mnemonic=(
            'Speciation modes: "APPLE" = Allopatric, Parapatric, Polyploidy, Lateral (Lineage/'
            'Ecological), sympatric (Extra). '
            'Allopatric = wall between them. Parapatric = wall with a crack. '
            'Sympatric = no wall but they stop dating. '
            'Allopolyploidy = sterile baby somehow has double the chromosomes and is now a new species.'
        ),
        flashcard={
            'front': 'What is allopolyploidy and why can it produce a new species in one generation?',
            'back': (
                'Allopolyploidy = hybridization of TWO DIFFERENT SPECIES followed by doubling of '
                'the entire hybrid genome.\n\n'
                '1. Two species (A: 2n=4, B: 2n=6) hybridize → sterile hybrid (2n=5, chromosomes '
                'from different species cannot pair in meiosis).\n'
                '2. Genome doubles (via unreduced gametes or spontaneously) → 2n=10.\n'
                '3. Every chromosome now has a homologous pair → meiosis works → FERTILE.\n\n'
                'The new polyploid is reproductively isolated from BOTH parent species:\n'
                '• Cross with species A (2n=4) → offspring with odd chromosome number → sterile.\n'
                '• Cross with species B (2n=6) → same problem.\n'
                'Therefore it can ONLY breed with other individuals of the same polyploid genotype '
                '→ independently evolving lineage = new species by definition.\n\n'
                'Real example: Tragopogon salsify — two new species arose in North America within '
                'the last ~100 years. Possibly half of all flowering plant species originated this way.'
            ),
        },
        quiz={
            'question': (
                'Two sister salamander species live on opposite sides of a mountain range. '
                'The range erodes over millions of years and they come into contact but do '
                'not interbreed. What type of speciation occurred?'
            ),
            'correct': 'Allopatric — geographic barrier separated them; reproductive isolation evolved during separation',
            'distractors': [
                'Sympatric — they now occupy the same range and still do not interbreed',
                'Parapatric — they retained some contact zone during divergence',
                'Ecological — differences in habitat use drove the divergence',
            ],
        },
        visual={
            'type': 'side-by-side',
            'description': 'Speciation modes compared by geographic context',
            'svg': SVG_FIG_13_8,
            'extraSvgs': [
                {'title': 'Fig 13.9 — Isthmus of Panama: Allopatric Speciation Test (Knowlton 1993)', 'svg': SVG_FIG_13_9},
                {'title': 'Fig 13.10 — Rhagoletis Fly Host-Race Temporal Isolation', 'svg': SVG_FIG_13_10},
                {'title': 'Fig 13.15 — Allopolyploidy: Step-by-Step Chromosome Diagram', 'svg': SVG_FIG_13_15},
                {'title': 'Fig 13.16 — Tragopogon Allopolyploidy: Two New Species in ~100 Years', 'svg': SVG_FIG_13_16},
            ],
            'regions': [
                {
                    'label': 'Allopatric',
                    'color': '#4ea8de',
                    'items': [
                        'Geographic barrier',
                        'Complete gene flow stop',
                        'Most common mode',
                        'Drift + selection both work',
                    ],
                },
                {
                    'label': 'Parapatric',
                    'color': '#ffc857',
                    'items': [
                        'Partial barrier / contact zone',
                        'Reduced but not zero gene flow',
                        'Selection > gene flow to diverge',
                        'Mine tailings example',
                    ],
                },
                {
                    'label': 'Sympatric',
                    'color': '#e63946',
                    'items': [
                        'No geographic barrier',
                        'Assortative mating drives split',
                        'Rhagoletis fly host shift',
                        'Most controversial model',
                    ],
                },
            ],
            'arrows': [],
            'tooltips': [
                {
                    'term': 'reinforcement',
                    'plain': 'Selection strengthens prezygotic barriers when hybrids are unfit — '
                             'can occur after secondary contact in allopatric or in parapatric zones.',
                },
                {
                    'term': 'isolation by distance',
                    'plain': 'Gene flow decreases as geographic distance increases even without a '
                             'discrete barrier — gradual divergence across a range.',
                },
            ],
            'mnemonic': 'Allopatric = wall. Parapatric = crack in wall. Sympatric = no wall but they stop talking.',
            'trap': (
                'Geographic isolation is NECESSARY but NOT SUFFICIENT for allopatric speciation. '
                'Allopolyploidy is NOT plants-only.'
            ),
        },
    ))

    # ------------------------------------------------------------------ #
    # NODE 4 — BDM Incompatibilities + Cryptic Species + Bacteria Problem
    # ------------------------------------------------------------------ #
    nodes.append(build_node(
        id='ch13-bdm-cryptic',
        title='BDM Incompatibilities + Cryptic Species',
        subtitle='Molecular basis of hybrid sterility, cryptic species detection, bacteria problem (Ch 13)',
        color='red',
        row=14,
        heading='Chapter 13 — BDM Model, Cryptic Species & Bacteria',
        sections=[
            {
                'label': 'Bateson-Dobzhansky-Muller (BDM) Incompatibilities',
                'body': (
                    'BDM incompatibilities = the molecular mechanism behind hybrid inviability\n'
                    'and hybrid sterility.\n\n'
                    'The scenario:\n'
                    '• Ancestral population has alleles a and b at two loci (compatible).\n'
                    '• Population 1 diverges → fixes allele A at locus 1 (A+b works fine).\n'
                    '• Population 2 diverges → fixes allele B at locus 2 (a+B works fine).\n'
                    '• They hybridize → offspring gets A+B together.\n'
                    '• A and B never co-evolved → EPISTATIC INCOMPATIBILITY → broken fitness.\n\n'
                    'Critical insight: Neither allele alone is broken. The COMBINATION in the\n'
                    'hybrid is what fails. This is why BDM incompatibilities accumulate over\n'
                    'time — each additional substitution exponentially increases the number of\n'
                    'possible incompatible pairings ("Dobzhansky-Muller complexity").\n\n'
                    'Mimulus example:\n'
                    '  Loci Hms1 and Hms2 each function normally in M. guttatus or M. nasutus.\n'
                    '  Hms1 (from M. guttatus) + Hms2 (from M. nasutus) in a hybrid → sterile pollen.\n'
                    '  Neither locus alone causes sterility — only the combination is lethal.\n\n'
                    'Mnemonic: "BDM = genes that never dated shouldn\'t be forced to live together."'
                ),
            },
            {
                'label': 'Cryptic Species',
                'body': (
                    'Definition: Two or more species that are morphologically IDENTICAL but are\n'
                    'genetically distinct, independently evolving lineages with no gene flow.\n\n'
                    'How found: Genetic/genomic tools — populations that don\'t interbreed diverge\n'
                    'genetically over time even if morphology stays identical.\n\n'
                    'Why BSC & morphological species concept miss them: no visible difference.\n'
                    'Why General Lineage Concept finds them: measures gene flow directly.\n\n'
                    'Biomedical relevance:\n'
                    '• Anopheles gambiae complex: 7+ cryptic species of African malaria mosquitoes.\n'
                    '  They look identical but differ in vector competence, insecticide resistance,\n'
                    '  biting behavior, and habitat. Treating as one species leads to failed control.\n'
                    '• Leishmania, Trypanosoma: cryptic species complexes differ in virulence.\n'
                    '• Aspergillus fumigatus: cryptic fungal species differ in antifungal resistance.'
                ),
            },
            {
                'label': 'The Bacteria/Archaea Problem',
                'body': (
                    'BSC does not apply to prokaryotes:\n'
                    '• Asexual reproduction → no sex = no reproductive isolation → BSC meaningless.\n\n'
                    'Horizontal gene transfer (HGT) further blurs lineage boundaries:\n'
                    '• Bacteria swap genes between entirely unrelated lineages.\n'
                    '• A single cell can acquire antibiotic resistance from a distant relative via\n'
                    '  plasmid transfer — a "gene" jumping species boundaries.\n'
                    '• This makes species boundaries porous in ways completely unlike eukaryotes.\n\n'
                    'How bacterial "speciation" is conceptualized:\n'
                    '• Ecologically specialized clusters (ecotypes) form when natural selection\n'
                    '  favors particular variants in particular niches.\n'
                    '• Gene flow between ecotypes decreases over ecological divergence even without\n'
                    '  reproductive isolation.\n'
                    '• General Lineage Concept is most applicable: measure gene flow by genomics.'
                ),
            },
            {
                'label': 'Speed of Speciation',
                'body': (
                    'Variable — depends on organism and mode:\n\n'
                    'FAST:\n'
                    '• Allopolyploidy in plants: potentially ONE GENERATION.\n'
                    '• Rhagoletis host shift: detectable divergence within 150 years.\n\n'
                    'MODERATE:\n'
                    '• Drosophila (Coyne & Orr): hundreds of thousands of years for complete\n'
                    '  reproductive isolation.\n\n'
                    'SLOW:\n'
                    '• Birds and mammals: often millions of years.\n\n'
                    'General pattern: Prezygotic isolation accumulates FASTER than postzygotic,\n'
                    'so behavioral/habitat barriers arise before BDM incompatibilities fully develop.'
                ),
            },
        ],
        quotes=[],
        examples=[
            'BDM — Drosophila: Hybrid male rescue (Hmr) gene in D. melanogaster and Lethal hybrid '
            'rescue (Lhr) gene in D. simulans — neither is lethal alone, but together in a hybrid '
            'male they cause lethality. Classic BDM pair.',
            'BDM — Monkeyflowers: Mimulus guttatus × M. nasutus hybrid males show sterile pollen '
            'caused by interaction of Hms1 and Hms2 loci from different species. Neither locus '
            'alone causes sterility.',
            'Cryptic species — Anopheles gambiae complex: 7 morphologically identical species. '
            'Only genomics distinguishes them. Critical for malaria control targeting.',
            'HGT — antibiotic resistance: methicillin-resistant Staphylococcus aureus (MRSA) '
            'acquired the mecA resistance gene from another Staphylococcus species via HGT. '
            'Not speciation, but illustrates how HGT blurs lineage boundaries in bacteria.',
        ],
        warnings=[
            'EXAM TRAP: "The Dobzhansky-Muller model requires that one of the two alleles be '
            'deleterious" → FALSE. BOTH alleles work fine individually — the incompatibility is '
            'PURELY EPISTATIC (the interaction between them in the hybrid).',
            'Cryptic species demonstrate that reproductive isolation is PRIMARY — morphological '
            'divergence can be zero and they are still separate species.',
            'HGT makes species concepts especially difficult in bacteria — do not apply BSC to '
            'prokaryotes on an exam without acknowledging its failure.',
        ],
        mnemonic=(
            '"BDM = genes that never dated shouldn\'t be forced to live together." '
            'Cryptic species = same face, different DNA. '
            'HGT = bacteria dating outside their species constantly.'
        ),
        flashcard={
            'front': (
                'Explain why neither allele alone causes problems in the BDM model, '
                'but their combination in a hybrid does.'
            ),
            'back': (
                'In the BDM model, two populations diverge from a common ancestor:\n'
                '• Population 1 fixes allele A (in the genetic background of ancestral b). '
                'A+b work together fine — they co-evolved in population 1.\n'
                '• Population 2 fixes allele B (in the genetic background of ancestral a). '
                'a+B work together fine — they co-evolved in population 2.\n\n'
                'When the two populations hybridize, the offspring may inherit BOTH A and B. '
                'A and B have never co-existed in the same organism — they never co-evolved. '
                'Their molecular interaction is UNTESTED by natural selection. The result: '
                'epistatic incompatibility — one allele disrupts the function of the other, '
                'producing sterility or inviability.\n\n'
                'Key insight: the more substitutions accumulate between populations, the more '
                'potential incompatible A+B pairings exist — BDM incompatibilities accumulate '
                'disproportionately fast as divergence increases.'
            ),
        },
        quiz={
            'question': (
                'A hybrid between two Mimulus species has sterile pollen ONLY when it inherits '
                'the Hms1 allele from species A AND the Hms2 allele from species B. When either '
                'allele is present alone, pollen is fertile. This is an example of:'
            ),
            'correct': 'BDM (Bateson-Dobzhansky-Muller) incompatibility — two alleles that each work fine alone are incompatible together',
            'distractors': [
                'Hybrid inviability — the hybrid dies before reaching reproductive age',
                'Gametic incompatibility — sperm cannot fertilize the egg',
                'Reinforcement — selection strengthens prezygotic barriers in sympatry',
            ],
        },
        visual={
            'type': 'side-by-side',
            'description': 'BDM model: divergence in isolation → incompatibility in hybrid',
            'extraSvgs': [
                {'title': 'Fig 13.17 — Astraptes Cryptic Species: DNA Barcoding Reveals 10 Species', 'svg': SVG_FIG_13_17},
                {'title': 'Fig 13.18 — E. coli Pan-Genome vs Core Genome (HGT blurs species boundaries)', 'svg': SVG_FIG_13_18},
                {'title': 'Fig 13.19 — HGT Mixes Bacterial Genomes Across All Lineages', 'svg': SVG_FIG_13_19},
                {'title': 'Fig 13.22 — Bacterial Speciation Model with HGT (Cohan Stable Ecotype)', 'svg': SVG_FIG_13_22},
            ],
            'regions': [
                {
                    'label': 'Ancestor',
                    'color': '#6e6a80',
                    'items': [
                        'Alleles: a + b',
                        'Both compatible',
                        'Single population',
                    ],
                },
                {
                    'label': 'Population 1',
                    'color': '#4ea8de',
                    'items': [
                        'Fixes allele A',
                        'A + b → fine',
                        'a never saw B',
                    ],
                },
                {
                    'label': 'Population 2',
                    'color': '#00c9a7',
                    'items': [
                        'Fixes allele B',
                        'a + B → fine',
                        'B never saw A',
                    ],
                },
                {
                    'label': 'Hybrid',
                    'color': '#e63946',
                    'items': [
                        'Gets A + B together',
                        'Never co-evolved',
                        '→ EPISTATIC INCOMPATIBILITY',
                        '→ Sterile or inviable',
                    ],
                },
            ],
            'arrows': [],
            'tooltips': [
                {
                    'term': 'epistasis',
                    'plain': 'When the effect of one gene depends on the presence of another gene — '
                             'the allele combination in the hybrid is what causes the problem, not either allele alone.',
                },
                {
                    'term': 'horizontal gene transfer',
                    'plain': 'Acquisition of genetic material from another organism other than a parent — '
                             'common in bacteria, blurs species boundaries.',
                },
            ],
            'mnemonic': '"Genes that never dated shouldn\'t be forced to live together." — BDM.',
            'trap': (
                'NEITHER allele is broken alone. Only the COMBINATION in the hybrid is '
                'incompatible. This is the defining feature of BDM incompatibilities.'
            ),
        },
    ))

    # ------------------------------------------------------------------ #
    # NODE 5 — Empirical Case Studies + DNA Barcoding + Bacteria 16S rRNA
    # ------------------------------------------------------------------ #
    nodes.append(build_node(
        id='ch13-empirical-cases',
        title='Speciation in Action — Case Studies',
        subtitle='Polar bears, Laupala crickets, Panama shrimp, DNA barcoding, bacteria 16S (Ch 13)',
        color='blue',
        row=14,
        heading='Chapter 13 — Empirical Case Studies in Speciation',
        sections=[
            {
                'label': 'Isthmus of Panama — Allopatric Speciation Test (Knowlton)',
                'body': (
                    'Before 3 million years ago: Atlantic and Pacific Oceans were joined; shrimp\n'
                    'populations ranged across both.\n\n'
                    'Isthmus of Panama formed ~3 mya → complete ocean barrier.\n\n'
                    'Knowlton et al. 1993: phylogeny of shrimp showed that sister taxa on each side\n'
                    'of Panama were each other\'s closest relatives — not same-ocean species.\n'
                    'Lab experiments: Atlantic + Pacific pairs would NOT interbreed even when placed\n'
                    'together. → Confirmed allopatric speciation via geological barrier.\n\n'
                    'Key takeaway: Geological evidence + phylogeny + mating experiments together\n'
                    'provide the strongest test of allopatric speciation hypotheses.'
                ),
            },
            {
                'label': 'Hawaiian Laupala Crickets — Sexual Selection Speciation (Shaw)',
                'body': (
                    '37 species of swordtail crickets found ONLY in Hawaii. Kerry Shaw (Cornell).\n\n'
                    'Phylogeny shows island-hopping westward to eastward tracks colonization history.\n'
                    'Rate: 6 new species on the Big Island in 430,000 years = 10× average arthropod rate.\n\n'
                    'Remarkable feature: Crickets show NO ecological divergence — they all eat the\n'
                    'same food, occupy the same habitat.\n\n'
                    'What DID diverge: MALE COURTSHIP SONGS (pulse rate) + FEMALE PREFERENCES.\n'
                    'QTL mapping: SAME locus controls BOTH male song production AND female preference\n'
                    '(Shaw & Lesnick 2009). This co-localization may explain rapid speciation.\n\n'
                    'Implication: Sexual selection (not ecology) can be a primary driver of speciation.'
                ),
            },
            {
                'label': 'Polar Bears — Ecological Speciation + Interspecies Gene Flow (Lorenzen)',
                'body': (
                    'Eline Lorenzen (Berkeley) sequenced full polar bear + brown bear genomes.\n'
                    'Liu et al. 2014: Polar bears diverged from brown bears 479,000–343,000 years ago\n'
                    '(NOT 5 million years ago as earlier estimates claimed).\n\n'
                    'Mechanism: ECOLOGICAL SPECIATION\n'
                    '• Warm climate allowed brown bears to expand to the high Arctic.\n'
                    '• Climate cooled → northern population isolated in allopatry.\n'
                    '• Strong selection for rapid ecological divergence: APOB (cholesterol binding for\n'
                    '  high-fat seal diet), heart function genes, pigmentation genes (transparent hairs).\n'
                    '• By 110,000 ya: fossils show polar bears already specialized as marine hunters.\n\n'
                    'Interspecies gene flow:\n'
                    '• Genomic evidence shows gene flow has continued AFTER speciation.\n'
                    '• Flow is ONE-WAY: polar bear alleles → brown bears, not the reverse.\n'
                    '• "Pizzly" / "grolar bear" hybrids documented in the wild.\n'
                    '• Species remain distinct despite gene flow — likely because most alleles\n'
                    '  from one species are selected against in the other\'s niche.'
                ),
            },
            {
                'label': 'Monkeyflower Pollinator Isolation — Mimulus cardinalis vs M. lewisii',
                'body': (
                    'Schemske & Bradshaw 1999 — Sierra Nevada, California.\n\n'
                    'Two overlapping Mimulus species — NOT hybridizing in nature:\n'
                    '• M. lewisii: visited 100% of the time by BEES. Broad petal landing pad,\n'
                    '  yellow ridges guiding bees, lower nectar.\n'
                    '• M. cardinalis: visited 97% of the time by HUMMINGBIRDS. Narrow tube, high\n'
                    '  nectar, pollen deposited on forehead.\n\n'
                    'Hybrid experiment: hand-pollination produced F1 hybrids with intermediate\n'
                    'flowers. F2 crosses produced full range from bee-adapted to hummingbird-adapted.\n'
                    'Field experiment: bees preferred large flowers low in red pigment; hummingbirds\n'
                    'preferred high nectar + red anthocyanin. Pollinators faithfully stuck to their\n'
                    'preferred type → pollinator isolation prevents gene flow even in sympatry.\n\n'
                    'Type of barrier: POLLINATOR ISOLATION (prezygotic, pre-mating).'
                ),
            },
            {
                'label': 'Cryptic Species — DNA Barcoding (Hebert & Janzen)',
                'body': (
                    'DNA barcoding: Use short fast-evolving mitochondrial DNA segments as "barcodes"\n'
                    'to detect species boundaries. Hebert (Guelph) pioneered the method.\n\n'
                    'Case: Astraptes fulgerator — neotropical skipper butterfly (Costa Rica).\n'
                    '• Described as ONE species since 1755.\n'
                    '• Daniel Janzen (Penn) noticed caterpillars fed on many different plants\n'
                    '  AND had different color patterns → hypothesis: multiple cryptic species.\n'
                    '• Hebert & Janzen 2004: DNA barcoding revealed 10 distinct genetic clusters,\n'
                    '  each with distinct caterpillar coloring. One "species" = 10 cryptic species.\n\n'
                    'Parasitoid wasp discovery: Apanteles leucostigmus — one named wasp species\n'
                    '→ DNA barcoding revealed it was actually 32 cryptic species.\n\n'
                    'Why it matters: Biodiversity is vastly underestimated. Conservation of a named\n'
                    '"species" may be inadequate if it is actually 10 cryptic lineages with separate\n'
                    'ecologies, ranges, and extinction risks.'
                ),
            },
            {
                'label': 'Microbial "Species" — 16S rRNA + HGT Problem',
                'body': (
                    'BSC fails for bacteria (asexual reproduction).\n'
                    'Early solution: Phylogenetic approach using 16S rRNA gene\n'
                    '  → if ≥97% identical = same OTU (operational taxonomic unit / "species").\n\n'
                    'Problem with 97% threshold — it is arbitrary:\n'
                    '• Streptococcus pneumoniae (lung pathogen) vs S. mitis (harmless on teeth):\n'
                    '  Traditionally classified as different species. Their 16S rRNA = 99% identical.\n'
                    '  Under the 97% rule = same species. But they have drastically different\n'
                    '  ecological roles and affect human health very differently.\n\n'
                    'Horizontal gene transfer (HGT) makes things worse:\n'
                    '• E. coli: comparing strains of the "same species" revealed only a small\n'
                    '  CORE GENOME shared by all strains.\n'
                    '• The remaining genes = PAN-GENOME — present in only some strains, acquired\n'
                    '  by HGT from entirely unrelated lineages.\n'
                    '• HGT makes bacterial "species" boundaries inherently porous.\n\n'
                    'Scale: 10,000 bacterial "species" in a single teaspoon of soil. Most cannot\n'
                    'be grown in pure culture. Total microbial diversity = unknowable by current methods.'
                ),
            },
        ],
        quotes=[
            '"It all comes, I believe, from trying to define the indefinable." — Charles Darwin, 1856 (on species concepts)',
        ],
        examples=[
            'Panama shrimp (Knowlton): Sister taxa on opposite sides of the isthmus + no lab '
            'interbreeding = confirmed allopatric speciation via a geological event.',
            'Laupala crickets (Shaw): 6 species in 430,000 years driven entirely by sexual '
            'selection (divergent courtship songs + female preferences), zero ecological divergence.',
            'Polar bears (Lorenzen): Diverged from brown bears ~479-343 kya. Strong positive '
            'selection on APOB cholesterol binding and heart genes for high-fat seal diet. '
            'Gene flow continued after speciation but only polar→brown direction.',
            'Astraptes butterfly (Janzen/Hebert): One described species → 10 cryptic species '
            'by DNA barcoding. Conservation listed the wrong units for 250 years.',
            'Apanteles wasp: One named wasp species → 32 cryptic species by DNA barcoding.',
            'S. pneumoniae vs S. mitis: 99% identical 16S rRNA yet dramatically different '
            'ecology and pathogenicity — illustrates why the 97% threshold is biologically arbitrary.',
        ],
        warnings=[
            'EXAM TRAP: Polar bear gene flow goes ONE WAY (polar → brown), NOT bidirectional.',
            'DNA barcoding uses MITOCHONDRIAL DNA, not nuclear DNA — fast-evolving segments '
            'used as species markers, not the actual cause of speciation.',
            'Core genome = genes in ALL strains of a species. Pan-genome = includes genes '
            'found in only some strains (acquired via HGT). E. coli core genome is surprisingly small.',
            'Laupala speciation is driven by sexual selection alone — NO ecological divergence. '
            'This challenges the assumption that speciation requires ecological differences.',
        ],
        mnemonic=(
            '"Panama splits shrimp." '
            '"Crickets sing themselves into new species." '
            '"Polar bears borrowed genes back from their ancestors." '
            '"DNA barcodes find the hidden 10 under the one."'
        ),
        flashcard={
            'front': (
                'What is DNA barcoding, and what did the Astraptes fulgerator study reveal?'
            ),
            'back': (
                'DNA barcoding = using short, fast-evolving mitochondrial DNA segments as '
                '"barcodes" to quickly identify and distinguish species, without full genome '
                'sequencing. Pioneered by Paul Hebert (University of Guelph).\n\n'
                'Astraptes fulgerator is a neotropical skipper butterfly in Costa Rica. '
                'Daniel Janzen had catalogued it as ONE species since 1755. He noticed the '
                'caterpillars fed on many different plant species and had different color '
                'patterns — suspicious for a single species.\n\n'
                'Hebert & Janzen (2004) DNA barcoded the butterflies → revealed 10 distinct '
                'genetic clusters, each with distinct caterpillar color patterns. One named '
                '"species" was actually 10 cryptic species.\n\n'
                'Implication: Global biodiversity is vastly underestimated. Conservation policy '
                'built on named species may inadequately protect cryptic lineages with separate '
                'ranges, ecologies, and extinction vulnerabilities.'
            ),
        },
        quiz={
            'question': (
                'Polar bears diverged from brown bears approximately 479,000–343,000 years ago. '
                'Genomic evidence shows gene flow has continued since divergence. '
                'Based on this, which of the following best characterizes polar bear speciation?'
            ),
            'correct': 'Ecological speciation with secondary interspecies gene flow — reproductive isolation is incomplete but maintained by selection against alleles in the other species\' niche',
            'distractors': [
                'Sympatric speciation — polar bears and brown bears live in the same geographic range',
                'Allopolyploidy — new species formed by genome doubling after hybridization',
                'Reinforcement speciation — prezygotic barriers strengthened by selection against sterile hybrids',
            ],
        },
        visual={
            'type': 'side-by-side',
            'description': 'Key empirical case studies testing speciation models',
            'svg': SVG_FIG_13_11,
            'extraSvgs': [
                {'title': 'Fig 13.13 — Polar Bear vs Brown Bear Population History (Liu et al. 2014)', 'svg': SVG_FIG_13_13},
            ],
            'regions': [
                {
                    'label': 'Panama Shrimp (Allopatric)',
                    'color': '#4ea8de',
                    'items': [
                        'Isthmus formed 3 mya',
                        'Sister taxa on each side',
                        'No lab interbreeding',
                        'Geo event → new species',
                    ],
                },
                {
                    'label': 'Laupala Crickets (Sexual Selection)',
                    'color': '#7c6cf7',
                    'items': [
                        '37 Hawaiian species',
                        '6 species in 430 kyr',
                        'No ecological divergence',
                        'Song + female preference diverged',
                    ],
                },
                {
                    'label': 'Polar Bears (Ecological + Gene Flow)',
                    'color': '#00c9a7',
                    'items': [
                        'Diverged 479-343 kya',
                        'APOB, heart, pigment genes',
                        'Gene flow polar → brown only',
                        'Species maintained despite flow',
                    ],
                },
            ],
            'arrows': [],
            'tooltips': [
                {
                    'term': 'DNA barcoding',
                    'plain': 'Using short fast-evolving mitochondrial DNA segments to rapidly identify species '
                             '— can find cryptic species that look identical but are genetically separate.',
                },
                {
                    'term': 'core genome / pan-genome',
                    'plain': 'Core genome = genes shared by ALL strains of a species. '
                             'Pan-genome = all genes found in ANY strain, including HGT acquisitions.',
                },
            ],
            'mnemonic': '"Panama splits shrimp. Crickets sing themselves apart. Polar bears borrowed genes back."',
            'trap': (
                'Polar bear gene flow is ONE-WAY (polar → brown), not bidirectional. '
                'Laupala speciation has NO ecological divergence — driven purely by sexual selection.'
            ),
        },
    ))

    return nodes
