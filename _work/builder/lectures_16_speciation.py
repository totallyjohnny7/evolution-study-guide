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
            '"It all comes, I believe, from trying to define the indefinable." — Charles Darwin, 1856',
            'Robbins (lecture): "There are approximately 25 definitions of what species are. '
            'They all agree on one thing: species = groups of interbreeding individuals that '
            'share common ancestry — they have the same evolutionary trajectory."',
        ],
        examples=[
            'BSC failure — Asexual: Bdelloid rotifers reproduce entirely asexually. '
            'Under BSC, every individual would be its own "species." Concept is inapplicable.',
            'BSC failure — Allopatry: Elk (North America) and red deer (Europe) can interbreed '
            'in captivity. BSC cannot classify them without geographic context.',
            'Morphological SC — Trilobites: ~22,000 described species identified entirely from '
            'fossils. The only option when there is no DNA. Robbins: "We have no idea how much '
            'environmental variation a trilobite might show — might be juvenile vs adult."',
            'PSC problem — Splitter tendency: Robbins: "Garbage in, garbage out — totally '
            'dependent on what characters you use to build the phylogeny. Two molecular trees '
            'can disagree slightly, meaning PSC would give you different species lists."',
            'Hybrids complicate BSC — Mule: horse × donkey → mule. Viable but sterile. '
            'Robbins: "Where do you draw the line? They can mate, but the offspring can\'t reproduce. '
            'Is that a species barrier or not? BSC says yes — the offspring\'s line ends there."',
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
            'Robbins exam angle: PSC is "garbage in, garbage out" — the species list you get '
            'totally depends on which characters or which gene you used to build the tree.',
            '~25 species definitions exist — Robbins says they all agree on ONE thing: '
            'species = evolutionarily independent lineages.',
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
                'A research team applies the PSC to a gecko group using skin-pattern characters '
                'and identifies 40 distinct species. A second team uses skull morphology on the '
                'same geckos and finds only 18 species. Robbins called this the "garbage in, '
                'garbage out" problem. Which fundamental weakness does this illustrate?'
            ),
            'correct': (
                'PSC species boundaries are entirely dependent on WHICH characters are chosen — '
                'different character sets produce different tree topologies and different species '
                'counts, with no objective criterion for selecting the correct character set'
            ),
            'distractors': [
                'PSC cannot recognize species that share a common ancestor, since all life is '
                'ultimately related through common descent',
                'PSC requires molecular (DNA) data to be valid — any morphological application '
                'automatically undercounts species due to phenotypic plasticity',
                'PSC always identifies FEWER species than the BSC because it requires a minimum '
                'threshold of genetic divergence before recognizing a new species',
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
            'Ecological isolation — Rhagoletis flies (Robbins lecture example): Hawthorn and apple '
            'flies are sympatric (flying by each other in the same field). They COULD mate '
            'genetically, but behavioral choice of host fruit prevents it. One group only deposits '
            'eggs in hawthorn; the other only in apples — same area, zero gene flow.',
            'Temporal isolation — Robbins: flower phenology (blooming times). One species flowers '
            'in early spring, another in late spring. The hummingbird pollinator won\'t freeze and '
            'wait between them. In a greenhouse where you force them to flower simultaneously, you '
            'can get viable hybrids — the barrier is purely temporal, not genetic.',
            'Post-mating prezygotic (weird one) — Robbins: "Insects sometimes do a courtship dance '
            'WHILE mating. If the male does something the female doesn\'t like, she can refuse to '
            'use the sperm even though it was already transferred." Female controls sperm use.',
            'Mechanical isolation — Robbins: plant genitalia (flower structure) and animal genital '
            'lock-and-key morphology. "The mechanics or protein which is still basically biochemistry '
            '— ultimately gonna be genetically associated."',
            'Gametic incompatibility — sea urchins: Strongylocentrotus purpuratus and S. franciscanus '
            'can be found in the same tide pools. Heterospecific sperm cannot penetrate the egg coat '
            'because the bindin protein (sperm) doesn\'t match the receptor on the egg surface.',
            'Hybrid sterility — mule: Robbins: "Male donkeys mate with female horses to produce '
            'mules — the ONLY way it works. The other way doesn\'t." Mule (2n=63) is vigorous but '
            'completely sterile. Each mule is "the end of its line."',
            'Geographic vicariance — Grand Canyon squirrels (Robbins): Abert\'s squirrel (south rim) '
            'and Kaibab squirrel (north rim). They\'re so close but don\'t interbreed because the '
            'bottom of the canyon is desert — no trees. The top has forests. They just never cross.',
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
            'Mule direction: male DONKEY × female HORSE → mule. The reverse cross does not work '
            '(Robbins emphasized this). Mules are sterile — their line ends there.',
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
                'Rhagoletis pomonella flies historically fed on hawthorn berries. ~140 years '
                'ago, some switched to apples. Today, apple-race flies emerge 2–3 weeks '
                'EARLIER than hawthorn-race flies, timed to match apple ripening. Females '
                'lay eggs on the fruit where they hatched; males perch on the same fruit '
                'to find mates. Which category of isolation is PRIMARY here, and why is '
                'this significant for sympatric speciation theory?'
            ),
            'correct': (
                'Habitat isolation + temporal isolation acting together as pre-mating '
                'prezygotic barriers — mate choice on host fruit AND emergence timing '
                'together reduce cross-race encounters to near zero, all arising within '
                '~140 years with NO geographic separation, making it a strong sympatric '
                'speciation candidate'
            ),
            'distractors': [
                'Post-mating prezygotic isolation — apple-race sperm cannot penetrate '
                'hawthorn-race eggs due to gametic incompatibilities that evolved rapidly '
                'over 140 years of host divergence',
                'Postzygotic hybrid inviability — F1 hawthorn × apple larvae cannot '
                'survive on either host plant because each genome is mis-tuned to its '
                'host\'s chemistry',
                'BDM incompatibility — hawthorn-race and apple-race alleles produce '
                'sterile hybrids when combined, constituting complete postzygotic isolation',
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
                    'Classic example: Rhagoletis flies (Robbins lecture)\n'
                    '• Originally bred exclusively on hawthorn trees in North America.\n'
                    '• ~140 years ago, some individuals switched to apple trees (apples introduced).\n'
                    '• Key mechanism: some hawthorn flies were ALREADY emerging slightly earlier.\n'
                    '  That earlier emergence matched when apples became ripe. Low competition for\n'
                    '  the new resource → higher fitness for early-emerging apple users → genetic\n'
                    '  component of emergence timing spread rapidly through the apple-using population.\n'
                    '• Now: hawthorn-race and apple-race flies prefer their own host species.\n'
                    '• Same field, different host = assortative mating = reproductive isolation beginning.\n'
                    '• No geographic barrier — FULLY SYMPATRIC. Robbins: "They watched it happen."\n\n'
                    'Why controversial: Requires strong disruptive selection to overcome the\n'
                    'homogenizing effect of gene flow within the same range. Hardest model to prove.\n'
                    'Robbins: "Micro-allopatry argument — maybe they\'re only truly in the same\n'
                    'place at a landscape scale, but at a local scale they\'re on different trees."'
                ),
            },
            {
                'label': 'Ecological Speciation',
                'body': (
                    'What: Reproductive barriers evolve as a BYPRODUCT of adapting to different\n'
                    'environments or ecological niches.\n\n'
                    'Two populations specialize on different prey, soil types, host plants, etc.\n'
                    'This: (1) reduces contact between them, (2) makes hybrids unfit for either niche,\n'
                    '(3) may trigger REINFORCEMENT.\n\n'
                    'REINFORCEMENT (Robbins definition): When two previously allopatric populations\n'
                    'come back into secondary contact and their hybrids have low fitness, natural\n'
                    'selection REINFORCES (confirms and strengthens) the reproductive isolation.\n'
                    'It\'s "reinforcing their divergence" — now they can\'t hybridize even if they try.\n'
                    'Robbins: "It\'s also confirming it — there\'s no way they\'re gonna become one\n'
                    'species again because they can\'t. It\'s called reinforcement."\n\n'
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
                'The Isthmus of Panama closed ~3 mya, splitting Atlantic and Pacific '
                'populations of snapping shrimp. Molecular data show the sister pairs '
                'diverged right at the closure event. Knowlton (1993) then placed Atlantic '
                'and Pacific pairs together in the lab — they refused to interbreed. '
                'Why is the LAB MATING EXPERIMENT considered a stronger test of allopatric '
                'speciation than molecular divergence data alone?'
            ),
            'correct': (
                'Genetic divergence alone can reflect neutral drift or local adaptation '
                'without reproductive isolation — the BSC definition requires that the '
                'populations CANNOT interbreed. Lab mating tests directly verify that '
                'the geographic barrier produced COMPLETE reproductive isolation, not '
                'just genetic difference'
            ),
            'distractors': [
                'Molecular clocks are unreliable for marine invertebrates, so mating '
                'experiments are needed to establish the true divergence time independently '
                'of the uncertain geological closure date',
                'Shrimp have very low mutation rates, so any genetic divergence detected '
                'after only 3 million years must reflect balancing selection rather than '
                'allopatric divergence — behavioral tests rule out this alternative',
                'The Isthmus closure changed ocean temperature and salinity on both sides, '
                'so behavioral experiments are needed to rule out ecological speciation '
                'as the cause rather than simple geographic isolation',
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
                'Apanteles leucostigmus was described as ONE parasitoid wasp species. '
                'DNA barcoding of specimens attacking Astraptes caterpillars in Costa Rica '
                'revealed it was actually 32 distinct cryptic species. A conservation '
                'agency had been managing it as a single species. What is the most '
                'serious conservation implication of this result?'
            ),
            'correct': (
                'If 32 cryptic species each have distinct host associations, geographic '
                'ranges, and population sizes, the single-species management plan may '
                'have protected some lineages while allowing others to go extinct '
                'invisibly — biodiversity loss occurs beneath a single taxonomic name, '
                'making true extinction risk impossible to assess'
            ),
            'distractors': [
                'Since all 32 cryptic species attack the same caterpillar host, the '
                'ecological function of "A. leucostigmus" is unchanged and no '
                'conservation reassessment is required',
                'DNA barcoding only detects mitochondrial lineages, which do not '
                'correspond to biological species — the 32 "species" almost certainly '
                'represent within-species population structure, not true speciation',
                'Because the wasp is a parasitoid (a natural pest-control agent), '
                'discovering 32 cryptic species is a benefit: each one can be deployed '
                'independently to control specific Astraptes host races',
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
                    'Colonization history: Phylogeny shows island-hopping westward to eastward.\n'
                    'TWO INDEPENDENT COLONIZATIONS to the Big Island -- visible as two separate\n'
                    'lineages (two arrows) in the phylogeny. Robbins: "similar to frogs --\n'
                    'probably the same general mechanism."\n\n'
                    'Rate: ~6 new species on the Big Island in 430,000 years = 10× average arthropod rate.\n\n'
                    'Remarkable feature: NO ecological divergence — all species eat the same food,\n'
                    'live in the same habitat.\n\n'
                    'What DID diverge: MALE COURTSHIP SONGS (pulse rate) + FEMALE PREFERENCES.\n'
                    'HOW males sing: males RUB THEIR LEGS TOGETHER to produce the pulse signal.\n'
                    'Females HEAR and RESPOND to the call — same mechanism as frogs (Robbins).\n\n'
                    'QTL mapping: SAME locus controls BOTH male song production AND female preference\n'
                    '(Shaw & Lesnick 2009). Co-localization = single mutation changes signal AND\n'
                    'receiver simultaneously → explains explosive speciation rate.\n\n'
                    'Implication: Sexual selection (not ecology) can be the PRIMARY driver of speciation.'
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
                'Hawaiian Laupala crickets: 37 species, Big Island only, diverging at '
                '~10× the average arthropod speciation rate. Males rub their legs together '
                'to produce a pulse-rate song; females hear and respond to it. QTL mapping '
                '(Shaw & Lesnick 2009) showed the SAME genetic locus controls BOTH male '
                'song production AND female song preference. Two independent colonizations '
                'of the Big Island are visible in the phylogeny. What does co-localization '
                'of the signal and preference loci most directly explain about the rapid '
                'speciation rate?'
            ),
            'correct': (
                'A single mutation at the shared locus simultaneously shifts the male song '
                'AND the female preference — signal and receiver co-evolve in one step, '
                'so reproductive isolation between newly diverged populations is immediate '
                'rather than requiring slow sequential accumulation of separate sender and '
                'receiver mutations across different loci'
            ),
            'distractors': [
                'Co-localization means song and preference alleles are always inherited '
                'together, preventing females from ever preferring the wrong male — this '
                'removes the cost of sexual selection entirely and allows populations to '
                'drift apart faster under neutral evolution',
                'The shared locus links courtship song to ecological habitat selection, '
                'so a single mutation simultaneously changes mating preference AND '
                'microhabitat use, amplifying the rate of both ecological and sexual '
                'speciation simultaneously',
                'Because the locus is on the X chromosome, only females experience '
                'selection on preference while males evolve songs neutrally — this '
                'asymmetric selection pressure accelerates divergence between islands',
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
