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
        quiz=[
            {
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
            {
                'question': (
                    'North American elk and European red deer can interbreed and produce fertile '
                    'offspring when placed together in captivity. Why does the BSC create a '
                    'classification problem for these two groups?'
                ),
                'correct': (
                    'The BSC requires ACTUAL interbreeding (sympatric populations) or demonstrably '
                    'POTENTIAL interbreeding — allopatric populations separated by an ocean cannot '
                    'be tested in nature, so the BSC cannot definitively determine whether they are '
                    'one species or two without the artificial context of captivity'
                ),
                'distractors': [
                    'BSC classifies elk and red deer as the same species because their interbreeding '
                    'in captivity proves they are not reproductively isolated — any pair that can '
                    'produce fertile offspring is the same species regardless of geography',
                    'BSC classifies them as different species because they live on different continents '
                    '— geographic separation is the defining criterion of the BSC, not reproductive '
                    'compatibility, which is only relevant to the General Lineage Concept',
                    'BSC is inapplicable to large mammals because they do not have discrete mating '
                    'seasons — the concept was designed for seasonally breeding organisms and fails '
                    'whenever populations can potentially reproduce year-round',
                ],
            },
            {
                'question': (
                    'The General Lineage Concept (de Queiroz) uses genomic data to measure ACTUAL '
                    'gene flow between populations. How does this make it superior to the BSC for '
                    'detecting cryptic species like the Anopheles gambiae complex?'
                ),
                'correct': (
                    'The 7 Anopheles gambiae cryptic species look morphologically identical — BSC '
                    'cannot detect their distinctness without observing reproductive behavior. '
                    'Genomic analysis directly measures whether alleles are flowing between '
                    'populations; zero gene flow = independently evolving lineages = separate species, '
                    'regardless of morphological similarity'
                ),
                'distractors': [
                    'The General Lineage Concept is superior because it uses a stricter definition — '
                    'it requires zero gene flow for separate species, whereas BSC allows some gene '
                    'flow between species as long as interbreeding is infrequent',
                    'BSC could detect Anopheles cryptic species equally well by testing whether '
                    'mosquitoes from different populations mate in laboratory conditions — the General '
                    'Lineage Concept just provides faster results using sequencing technology',
                    'The General Lineage Concept is superior because it does not require any biological '
                    'evidence — any two populations with different common names are classified as '
                    'separate species, while BSC incorrectly lumps them based on shared morphology',
                ],
            },
            {
                'question': (
                    'Bdelloid rotifers are microscopic invertebrates that reproduce entirely '
                    'asexually and have done so for tens of millions of years. Why do they '
                    'represent a fundamental breakdown of the BSC rather than just an exception?'
                ),
                'correct': (
                    'BSC defines species by reproductive isolation — but reproductive isolation '
                    'is literally meaningless for asexual organisms that never sexually reproduce. '
                    'Every individual is genetically isolated from every other by definition of '
                    'asexual reproduction, yet bdelloid rotifers clearly form identifiable, '
                    'ecologically distinct lineages that need classification'
                ),
                'distractors': [
                    'Bdelloid rotifers are exceptions to the BSC rather than a fundamental breakdown '
                    'because exceptions to any rule are expected — the BSC remains valid for the '
                    'majority of sexually reproducing organisms and the rotifer case is simply noted '
                    'as an anomaly requiring a separate classification approach',
                    'BSC can be applied to bdelloid rotifers by treating clonal lineages as '
                    '"potentially interbreeding" — if rotifers encountered conditions allowing '
                    'sexual reproduction, they would interbreed with close relatives, satisfying '
                    'the BSC\'s "potentially" criterion',
                    'Bdelloid rotifers do have sex occasionally under stress conditions, so the BSC '
                    'does technically apply — the claim that they are fully asexual is an '
                    'oversimplification that does not reflect the current understanding of their '
                    'reproductive biology',
                ],
            },
            {
                'question': (
                    'Robbins quoted Darwin (1856): "It all comes, I believe, from trying to define '
                    'the indefinable." Why is this quote still relevant to modern species concepts '
                    'when ~25 different definitions of "species" are in current use?'
                ),
                'correct': (
                    'Species are EMERGENT entities in a continuous evolutionary process — they '
                    'arise gradually and there is no single feature that perfectly marks the boundary '
                    'between one species and another. Every definition captures one aspect (mating, '
                    'phylogeny, gene flow) of what is fundamentally a fuzzy transition, which is why '
                    'multiple partial definitions exist and no single one works universally'
                ),
                'distractors': [
                    'The quote is obsolete because modern genomics has finally resolved the species '
                    'concept problem — with whole-genome sequencing we can now precisely identify '
                    'species boundaries in any organism, and the multiple definitions are only '
                    'historical remnants from before sequencing was available',
                    'The quote illustrates that Darwin rejected the concept of species entirely — '
                    'he believed only individual organisms and populations exist, and the idea of '
                    '"species" is a human-imposed category with no biological reality whatsoever',
                    'The quote is a statement about taxonomy specifically — it refers to the '
                    'difficulty of naming species in Latin nomenclature rather than the biological '
                    'problem of defining species boundaries, which Darwin considered straightforward',
                ],
            },
            {
                'question': (
                    'Mules (horse × donkey hybrids) are viable but sterile. Robbins asked: '
                    '"Where do you draw the line? They can mate, but the offspring can\'t reproduce." '
                    'How does the BSC resolve this edge case, and why might a strict BSC '
                    'interpretation still feel unsatisfying?'
                ),
                'correct': (
                    'BSC classifies horses and donkeys as separate species because hybrid sterility '
                    'prevents gene flow — the mule\'s genetic line ends with it, so no alleles are '
                    'exchanged between parental species. The interpretation may feel unsatisfying '
                    'because mating clearly CAN occur and some hybrids survive, blurring the '
                    'intuitive "cannot interbreed" criterion'
                ),
                'distractors': [
                    'BSC classifies horses and donkeys as the same species because mules are viable '
                    '— any hybrid that can be born represents potential gene flow between the parent '
                    'species, and sterility is irrelevant to the BSC definition',
                    'BSC cannot resolve the mule case at all and assigns horses and donkeys to an '
                    'intermediate category called "semispecies" that is neither fully the same nor '
                    'fully different species — this special category is reserved for hybridizing pairs',
                    'BSC places the mule itself into a third species separate from both horses and '
                    'donkeys — mules constitute their own species because they are reproductively '
                    'isolated from both parental lineages by their sterility',
                ],
            },
            {
                'question': (
                    'Trilobites (~22,000 described species) can only be classified using the '
                    'MORPHOLOGICAL species concept because they are extinct and known only from '
                    'fossils. What is the main weakness of the morphological species concept that '
                    'Robbins emphasized in lecture?'
                ),
                'correct': (
                    'Morphology within a single species can vary enormously due to age, sex, '
                    'environmental conditions, or geographic variation — a morphological '
                    '"species" count can be inflated by lumping developmental stages (juvenile '
                    'vs adult) as separate species, or deflated by missing cryptic differences; '
                    'without mating or genetic data there is no way to verify the boundaries'
                ),
                'distractors': [
                    'The morphological species concept is weak because it requires physical '
                    'preservation of soft tissues — since most fossils preserve only hard parts, '
                    'the morphological concept cannot be applied to the majority of extinct '
                    'organisms including trilobites',
                    'The main weakness is that morphological traits cannot be measured objectively '
                    '— different researchers produce different species counts based on personal '
                    'judgment, so no two morphological classifications of the same fossil set ever '
                    'agree on species boundaries',
                    'The morphological species concept was proven wrong when fossil DNA was '
                    'extracted from trilobites in 2015 — the DNA revealed that the 22,000 '
                    '"species" were actually only ~500 true species with extensive environmental '
                    'variation',
                ],
            },
            {
                'question': (
                    'The General Lineage Species Concept (Kevin de Queiroz) uses the term '
                    'METAPOPULATION to describe spatially separated subpopulations that exchange '
                    'alleles at some rate. Why is the metapopulation framing particularly useful '
                    'for applying the concept to real-world organisms?'
                ),
                'correct': (
                    'Real populations are rarely uniform — they consist of subpopulations with '
                    'varying connectivity. Metapopulation framing acknowledges that gene flow is '
                    'a MATTER OF DEGREE (not zero vs. total), and species status depends on whether '
                    'the overall exchange is frequent enough to maintain a single evolving lineage '
                    '— this allows the concept to handle the continuous spectrum of real biological '
                    'situations that BSC\'s binary classification cannot'
                ),
                'distractors': [
                    'Metapopulation framing is useful because it requires all subpopulations to be '
                    'sampled exhaustively — only when every local group is genotyped can species '
                    'boundaries be determined, making the General Lineage Concept the only rigorous '
                    'approach available',
                    'The metapopulation term is borrowed from ecology and has no special relevance '
                    'to speciation — it is used only as a synonym for "population" in the de Queiroz '
                    'framework without adding any conceptual advantage over BSC or PSC',
                    'Metapopulation means that the concept applies only to island-dwelling organisms '
                    'with discrete subpopulations — continuously distributed species on mainlands '
                    'cannot be classified under the General Lineage Concept without first being '
                    'subdivided into artificial metapopulation units',
                ],
            },
            {
                'question': (
                    'Ernst Mayr published the BSC in 1942 as part of the Modern Synthesis. A student '
                    'argues that the BSC is the "correct" species concept because it is the oldest '
                    'and most widely used in biology textbooks. Why is this appeal to tradition a '
                    'bad argument against the more recent General Lineage Species Concept?'
                ),
                'correct': (
                    'Scientific concepts are judged by their empirical utility and coverage, not '
                    'by age or popularity — the BSC has well-documented failures (asexuals, '
                    'allopatry, fossils, cryptic species) that the General Lineage Concept handles '
                    'better because it uses direct genomic measurement of gene flow; a newer '
                    'concept that solves old problems is an improvement, not a violation of '
                    'scientific tradition'
                ),
                'distractors': [
                    'The student is correct — the BSC has been validated by 80 years of use, and '
                    'any proposed replacement must be rejected until it accumulates an equivalent '
                    'track record, which the General Lineage Concept has not yet achieved',
                    'The student is correct because Mayr was one of the founders of the Modern '
                    'Synthesis and his authority settles the question — later researchers like '
                    'de Queiroz lack the standing to override Mayr\'s classic formulation',
                    'The student is wrong because the BSC was never widely accepted — biology '
                    'textbooks have always used the Morphological Species Concept as the default, '
                    'and the BSC was only a niche theoretical proposal until the 2000s',
                ],
            },
            {
                'question': (
                    'The PSC defines a species as the smallest monophyletic group diagnosable by '
                    'at least one shared derived character (synapomorphy). One advantage of the PSC '
                    'over BSC is that it works for extinct organisms like trilobites. Why does '
                    'the PSC "work" for fossils where BSC completely fails?'
                ),
                'correct': (
                    'PSC depends only on morphological or molecular characters that can be observed '
                    'in preserved specimens — a diagnosable synapomorphy can be recognized from '
                    'fossil bone, shell, or tooth morphology without requiring any information about '
                    'reproduction. BSC by contrast requires data on mating and reproductive isolation, '
                    'which cannot be obtained from fossils, so PSC is the only option for extinct taxa'
                ),
                'distractors': [
                    'PSC works for fossils because it uses DNA preserved in the fossil material — '
                    'trilobite DNA can be extracted from Cambrian specimens and used to build '
                    'molecular phylogenies, giving PSC access to the same data types available for '
                    'living organisms',
                    'PSC works for fossils because extinct organisms are automatically considered '
                    'separate species from all living ones — the boundary between extant and extinct '
                    'is always a species boundary under PSC regardless of morphological evidence',
                    'PSC works for fossils only if a living descendant can be found and used to '
                    'test interbreeding compatibility — without a living relative the PSC cannot be '
                    'applied to any fossil taxon',
                ],
            },
        ],
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
        quiz=[
            {
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
            {
                'question': (
                    'A male duck mates with a female of a closely related species. Copulation '
                    'occurs and sperm is transferred, but fertilization does not occur because '
                    'sperm-egg binding proteins are species-specific. Which isolating barrier '
                    'category does this represent, and which category does it NOT represent?'
                ),
                'correct': (
                    'This is POST-MATING PREZYGOTIC isolation (gametic incompatibility — sperm '
                    'reaches the egg but cannot fertilize it due to protein mismatch). It is NOT '
                    'mechanical isolation (which would prevent copulation from occurring at all) '
                    'and NOT postzygotic isolation (which requires a zygote to have formed first)'
                ),
                'distractors': [
                    'This is mechanical isolation — species-specific genital morphology prevents '
                    'fertilization even when mating occurs; sperm-egg protein compatibility is part '
                    'of the genital lock-and-key system and belongs in the same prezygotic category',
                    'This is postzygotic hybrid inviability — the sperm and egg from different species '
                    'form an incompatible zygote that dies during early cell division before implantation, '
                    'which is why no offspring results from the cross',
                    'This is behavioral isolation — the female duck\'s nervous system detects '
                    'the heterospecific chemical signals in the sperm and triggers an immune '
                    'rejection response before fertilization, classifying this as a pre-mating barrier',
                ],
            },
            {
                'question': (
                    'A mule (horse × donkey hybrid) is vigorous and healthy but completely sterile. '
                    'The horse has 2n=64 chromosomes and the donkey has 2n=62. Why is the mule '
                    'sterile, and why does this sterility prevent gene flow between horses and donkeys?'
                ),
                'correct': (
                    'The mule has 63 chromosomes — one set from horse and one from donkey. During '
                    'meiosis, chromosomes must pair with homologs, but the horse and donkey chromosomes '
                    'are too divergent to pair properly, so meiosis fails and no functional gametes '
                    'form. The mule cannot breed back into either parental species, ending that '
                    'hybrid\'s genetic line'
                ),
                'distractors': [
                    'Mules are sterile because horse and donkey genomes carry reciprocal chromosomal '
                    'inversions that prevent proper crossing-over during meiosis — the inversions are '
                    'a BDM incompatibility that causes all hybrid cells to undergo apoptosis before '
                    'gametes can mature',
                    'Mules are sterile because the horse X chromosome and donkey X chromosome carry '
                    'incompatible dosage compensation systems — females are affected more severely than '
                    'males, which is why female mules are completely infertile but male mules occasionally '
                    'produce viable sperm',
                    'Mule sterility is postzygotic hybrid breakdown rather than hybrid sterility — '
                    'mules can occasionally produce gametes, but any F2 offspring (mule × horse or '
                    'mule × donkey) are inviable, so gene flow is prevented at the F2 generation '
                    'rather than in the mule itself',
                ],
            },
            {
                'question': (
                    'Coyne and Orr studied Drosophila species pairs at varying levels of genetic '
                    'divergence and found that prezygotic isolation accumulates FASTER than '
                    'postzygotic isolation. What mechanism — reinforcement — specifically accelerates '
                    'prezygotic isolation in sympatric populations but not allopatric ones?'
                ),
                'correct': (
                    'When previously allopatric populations come into secondary contact and their '
                    'hybrids are unfit, selection DIRECTLY favors individuals that avoid mating with '
                    'heterospecifics — any behavioral or habitat preference that reduces hybrid '
                    'production increases fitness, rapidly strengthening prezygotic barriers. '
                    'Allopatric populations have no hybrid-forming contact so reinforcement cannot act'
                ),
                'distractors': [
                    'Reinforcement acts on both allopatric and sympatric populations equally — it '
                    'is simply the accumulation of random mutations in mate-recognition genes over '
                    'time, and the rate is determined by generation time and population size rather '
                    'than by whether populations are in contact',
                    'Reinforcement accelerates postzygotic isolation in sympatric populations by '
                    'selecting against hybrid genomes — BDM incompatibilities accumulate faster when '
                    'two gene pools are mixing, because the incompatible allele combinations are '
                    'continuously tested and purged by selection',
                    'Reinforcement specifically accelerates gametic incompatibility (post-mating '
                    'prezygotic isolation) rather than behavioral isolation, because sperm-egg '
                    'protein evolution is faster than nervous-system evolution for mate preference',
                ],
            },
            {
                'question': (
                    'Firefly flash patterns are species-specific: each species has a characteristic '
                    'pulse interval, pulse length, and flight pattern that females recognize as '
                    'conspecific signals. Which category of reproductive isolation does the firefly '
                    'flash pattern illustrate, and what is its position on the reproductive timeline?'
                ),
                'correct': (
                    'BEHAVIORAL isolation — a PRE-MATING PREZYGOTIC barrier acting at the mate-'
                    'recognition stage before any gamete transfer occurs. Females that do not '
                    'respond to heterospecific flash patterns simply never initiate mating with the '
                    'wrong species, blocking gene flow at the earliest possible point in the '
                    'reproductive sequence'
                ),
                'distractors': [
                    'Mechanical isolation — flash patterns are a physical lock-and-key system '
                    'that prevents heterospecific mating even if the female approaches the male, '
                    'functioning as a post-mating prezygotic barrier',
                    'Temporal isolation — different firefly species flash at different times of '
                    'night, so they are never active simultaneously and cannot encounter each other, '
                    'making flash patterns a form of temporal rather than behavioral isolation',
                    'Gametic incompatibility — the species-specific flash pattern triggers the '
                    'release of chemically distinct pheromones that bind to sperm-egg recognition '
                    'proteins, making flash patterns a post-mating prezygotic barrier'
                ],
            },
            {
                'question': (
                    'In sea urchins (Strongylocentrotus purpuratus and S. franciscanus) that '
                    'spawn in the same tide pools, heterospecific sperm physically reaches eggs but '
                    'cannot fertilize them because the sperm BINDIN protein and the egg surface '
                    'receptor are species-specific. Why is this classified as PRE-ZYGOTIC isolation '
                    'rather than post-zygotic?'
                ),
                'correct': (
                    'No zygote is formed — fertilization (sperm-egg fusion and pronuclei formation) '
                    'never occurs because the binding step fails. The reproductive timeline places '
                    'this step BEFORE zygote formation, making gametic incompatibility the 6th '
                    'barrier: post-mating (sperm transferred) but prezygotic (no zygote created)'
                ),
                'distractors': [
                    'It is prezygotic because the sperm die before reaching the egg — the species-'
                    'specific binding proteins trigger sperm apoptosis on contact with the wrong '
                    'egg coat, so gamete transfer technically fails and nothing post-mating happens',
                    'It is prezygotic because bindin proteins act during courtship signaling '
                    'before mating rather than at fertilization — sea urchin females assess '
                    'bindin chemistry in the water before releasing eggs, making this a pre-mating '
                    'barrier',
                    'It is prezygotic because the BSC excludes all fertilization-related barriers '
                    'from the postzygotic category — any barrier involving gametes is classified '
                    'as prezygotic regardless of whether a zygote forms or not',
                ],
            },
            {
                'question': (
                    'Hybrid BREAKDOWN is the 9th isolating barrier: F1 hybrids are viable and '
                    'fertile, but the F2 generation (offspring of F1 × F1 crosses) shows reduced '
                    'fitness. Why does the fitness reduction appear in F2 rather than F1?'
                ),
                'correct': (
                    'F1 hybrids are heterozygous at every locus that differs between the parental '
                    'species — incompatible allele combinations are MASKED by the presence of at '
                    'least one parental allele per locus. In F2, meiotic recombination and '
                    'segregation produce homozygous combinations that expose the BDM incompatibilities '
                    'for the first time, causing reduced fitness only in the F2 generation'
                ),
                'distractors': [
                    'F1 hybrids inherit mitochondria exclusively from the mother, so cytoplasmic '
                    'incompatibilities only appear when F2 individuals develop their own mitochondrial '
                    'populations from mixed F1 cytoplasm',
                    'F1 hybrids undergo compensatory gene expression that temporarily suppresses '
                    'incompatible alleles — this compensation requires a specific parent-of-origin '
                    'imprint that is lost in F2 generation, exposing the incompatibilities',
                    'F1 hybrid breakdown only appears in F2 because environmental stress accumulates '
                    'over generations — F2 individuals are raised in more stressful conditions '
                    'due to F1 parental competition, so the fitness reduction is ecological rather '
                    'than genetic',
                ],
            },
            {
                'question': (
                    'Robbins described a "weird" post-mating prezygotic case: in some insects, '
                    'females can refuse to USE sperm even after it has been transferred during '
                    'mating, if the male does something unacceptable during a concurrent courtship '
                    'dance. Why is this classified as post-mating prezygotic rather than behavioral '
                    'isolation?'
                ),
                'correct': (
                    'Behavioral isolation acts BEFORE mating — it prevents mating from starting. '
                    'In this case mating and sperm transfer have already occurred, so the barrier '
                    'is post-mating by definition. But no zygote has been formed because the female '
                    'controls whether the sperm ever fertilizes the egg, so it is still prezygotic'
                ),
                'distractors': [
                    'This is actually behavioral isolation because the courtship dance is a pre-'
                    'mating behavior — the dance outcome is determined during courtship, so the '
                    'barrier is classified by when the behavior originates, not by when the sperm '
                    'is rejected',
                    'It is classified as gametic incompatibility because the female uses chemical '
                    'signals to destroy heterospecific sperm — this is equivalent to the sea urchin '
                    'bindin system and belongs in the same category',
                    'It is classified as postzygotic because sperm rejection occurs after fertilization '
                    'is initiated — the female aborts zygote development in response to the unacceptable '
                    'courtship dance, placing this barrier after zygote formation',
                ],
            },
            {
                'question': (
                    'Some salamander species breed in the spring while closely related congeners '
                    'breed in the fall. Even when their geographic ranges overlap completely, they '
                    'never produce hybrids because they never encounter each other during the '
                    'reproductive season. Which isolating barrier is this, and where does it fit '
                    'in the reproductive timeline?'
                ),
                'correct': (
                    'TEMPORAL isolation — a PRE-MATING PREZYGOTIC barrier; the two species are '
                    'simply not reproductively active at the same time, so gene flow is blocked '
                    'before any mate encounter can occur. Temporal isolation is particularly '
                    'effective because it prevents contact entirely and does not require any '
                    'species-recognition machinery to operate'
                ),
                'distractors': [
                    'This is habitat isolation because the different seasons represent different '
                    'microhabitats — spring salamanders live in damp spring habitats while fall '
                    'salamanders live in drier fall habitats, classifying this as habitat rather '
                    'than temporal isolation',
                    'This is behavioral isolation because the salamanders actively choose when to '
                    'breed based on species-specific behavioral cues — the timing difference is '
                    'a behavioral preference and belongs in the behavioral isolation category',
                    'This is post-mating prezygotic isolation because the seasonal difference '
                    'affects sperm viability — salamander sperm stored from spring cannot survive '
                    'until fall mating occurs, preventing fertilization after gamete transfer',
                ],
            },
            {
                'question': (
                    'In Mimulus monkeyflowers, two genes labeled Hms1 and Hms2 each work normally '
                    'within their own species but produce sterile pollen when combined from '
                    'different species (Sweigart & Willis). Why is this a textbook Bateson-'
                    'Dobzhansky-Muller (BDM) incompatibility, and what kind of isolating barrier '
                    'does it produce?'
                ),
                'correct': (
                    'Each gene evolved neutrally in its own species without being tested against '
                    'alleles from the other species — when combined in a hybrid, the two alleles '
                    'have never "co-evolved" and produce a dysfunctional interaction. This creates '
                    'postzygotic hybrid sterility, because the zygote forms and develops but the '
                    'adult produces no viable gametes, blocking gene flow at the F1 reproductive step'
                ),
                'distractors': [
                    'This is a gametic incompatibility (post-mating prezygotic) because the Hms1 '
                    'and Hms2 genes encode pollen recognition proteins on the stigma surface — '
                    'the incompatibility blocks fertilization before any zygote is formed, not after',
                    'This is hybrid inviability (postzygotic) because the incompatible Hms1/Hms2 '
                    'combination kills the developing embryo before it can mature — the classical '
                    'BDM mechanism always produces inviability rather than sterility',
                    'This is an example of dominance-based incompatibility rather than BDM — the '
                    'dominant allele at Hms1 suppresses the recessive allele at Hms2, and vice '
                    'versa, creating a double-knockout phenotype that appears only in hybrids',
                ],
            },
        ],
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
        quiz=[
            {
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
            {
                'question': (
                    'In allopatric speciation, geographic isolation is NECESSARY but NOT '
                    'SUFFICIENT for speciation. What must additionally occur for two geographically '
                    'separated populations to become separate species under the BSC?'
                ),
                'correct': (
                    'Reproductive isolation must develop while the populations are separated — '
                    'through accumulated genetic divergence (mutation, drift, or local selection). '
                    'If they come back into secondary contact before reproductive isolation is complete, '
                    'gene flow can erase the divergence and merge them back into one species'
                ),
                'distractors': [
                    'The geographic barrier must persist long enough for one population to go extinct '
                    'and be replaced by the other — speciation requires one lineage to outcompete and '
                    'replace the other rather than two separate lineages both persisting',
                    'The populations must accumulate at least 2% nucleotide divergence — this threshold '
                    'corresponds to the point where BDM incompatibilities become strong enough to '
                    'prevent fertilization in nearly all crosses between the two populations',
                    'One population must colonize a new ecological niche during the period of separation '
                    '— allopatry alone can produce only subspecies, while ecological divergence is '
                    'required to produce fully separate species under the BSC',
                ],
            },
            {
                'question': (
                    'Sympatric speciation via the Rhagoletis host-shift has been challenged with the '
                    '"micro-allopatry" argument. What is the argument, and how does it attempt to '
                    'reduce sympatric speciation to allopatric speciation?'
                ),
                'correct': (
                    'At the landscape scale Rhagoletis races share the same field (sympatric), '
                    'but at the local scale each race lives on a different tree species — flies '
                    'rarely encounter heterospecific hosts. Critics argue that individual apple '
                    'and hawthorn trees act as micro-allopatric patches, so the divergence is '
                    'really allopatric at the scale where mating decisions are made'
                ),
                'distractors': [
                    'The micro-allopatry argument claims that Rhagoletis races are not truly '
                    'diverging — the observed host preference differences are purely phenotypic '
                    'plasticity without a genetic basis, so no speciation is occurring and the '
                    'apparent race divergence will disappear if hosts are mixed',
                    'The micro-allopatry argument is that allopatry always precedes sympatric '
                    'divergence — Rhagoletis populations must have been geographically separated '
                    'during the last glacial maximum and secondary contact produced the host-race '
                    'divergence, not sympatric host-shift selection within a continuously '
                    'interbreeding population',
                    'Micro-allopatry refers to the temporal rather than spatial separation of '
                    'host races — because apple and hawthorn flies emerge at different times, '
                    'their temporal isolation is equivalent to geographic isolation, and the '
                    'speciation process is therefore classified as allopatric by definition',
                ],
            },
            {
                'question': (
                    'Bread wheat (Triticum aestivum) has 6n=42 chromosomes and originated through '
                    'two rounds of allopolyploidy involving three different ancestral grass species. '
                    'Why is bread wheat reproductively isolated from ALL three of its parental species?'
                ),
                'correct': (
                    'Crossing wheat (6n=42) with any parental species produces offspring with an '
                    'odd, unpaired chromosome number — the resulting hybrid has some sets from wheat '
                    'and some from the parent that cannot pair in meiosis, making the hybrid sterile. '
                    'Wheat can only reproduce with other wheat-ploidy individuals, making it an '
                    'independently evolving lineage by definition'
                ),
                'distractors': [
                    'Bread wheat is reproductively isolated from its parents because the polyploidy '
                    'process triggered a genome-wide wave of BDM mutations — the rapid genome '
                    'doubling introduced thousands of new allele combinations that are incompatible '
                    'with the parental gene backgrounds',
                    'Bread wheat is isolated from its parents because humans have selectively bred '
                    'it for thousands of years, accumulating so many artificial selection mutations '
                    'that gene flow with wild progenitors is prevented by hybrid breakdown in F2 '
                    'populations grown without agricultural conditions',
                    'Bread wheat is only reproductively isolated from two of the three parental '
                    'species — it retains the full chromosome set of the most recently added '
                    'parental genome and can still exchange pollen with that donor species in '
                    'experimental crosses, though this rarely occurs in nature',
                ],
            },
            {
                'question': (
                    'Parapatric speciation requires that STRONG DIFFERENTIAL SELECTION across a '
                    'habitat gradient be able to overcome the homogenizing effect of ongoing gene '
                    'flow at the contact zone. In the heavy-metal plant example (mine tailings '
                    'adjacent to normal soil), what specific balance makes parapatric divergence '
                    'possible?'
                ),
                'correct': (
                    'Plants on mine tailings experience extremely strong selection for metal '
                    'tolerance (non-tolerant individuals die); plants on normal soil experience '
                    'selection against metal-tolerance alleles because those alleles carry fitness '
                    'costs when not needed. The selection differential at the boundary is strong '
                    'enough to maintain genetic divergence despite pollen exchange between adjacent '
                    'populations'
                ),
                'distractors': [
                    'Parapatric speciation works in this case because pollen from mine-tailings '
                    'plants is physically heavier than normal pollen and cannot be carried by wind '
                    'to normal-soil populations — the weight difference creates a physical barrier '
                    'that blocks gene flow at the boundary',
                    'The parapatric plants actually evolve gametic incompatibility — their pollen '
                    'tubes cannot grow in the stigmas of the adjacent soil type, creating a '
                    'prezygotic barrier that functions at the boundary without requiring any '
                    'geographic separation',
                    'Parapatric divergence is actually impossible in plants and has only been '
                    'documented in animals — the heavy-metal plant case was later reclassified '
                    'as sympatric speciation because plants cannot have discrete parapatric '
                    'contact zones',
                ],
            },
            {
                'question': (
                    'Allopolyploidy in Tragopogon salsify produced two new species (T. miscellus '
                    'and T. mirus) in North America within the last ~100 years. What makes this '
                    'case especially powerful evidence that allopolyploidy can produce speciation '
                    'in a single generation?'
                ),
                'correct': (
                    'The formation of these species can be DATED precisely — T. dubius, T. pratensis, '
                    'and T. porrifolius were all introduced to North America as garden escapes in '
                    'the early 20th century, and the new allopolyploid species appeared within '
                    'decades; researchers could track the origin of entirely new species in '
                    'real-time, something nearly impossible for slower speciation modes'
                ),
                'distractors': [
                    'The Tragopogon case is powerful because the allopolyploids are phenotypically '
                    'identical to their parent species — this proves that new species can form '
                    'without any morphological change, overturning the assumption that speciation '
                    'requires visible phenotypic divergence',
                    'The power of the Tragopogon case comes from DNA barcoding — the new species '
                    'were distinguished from their parents using mitochondrial markers, validating '
                    'DNA barcoding as the primary tool for detecting allopolyploid speciation '
                    'in all flowering plants',
                    'The Tragopogon case is unique because the species arose through autopolyploidy '
                    '(doubling within a single species) rather than allopolyploidy — it provides '
                    'the first evidence that single-species genome doubling is a viable speciation '
                    'mechanism in plants',
                ],
            },
            {
                'question': (
                    'The threespine stickleback (Gasterosteus aculeatus) exists in sympatric marine '
                    '(open-water) and benthic (lake-bottom) ecotypes that have evolved reproductive '
                    'isolation. This is a textbook example of ECOLOGICAL speciation. What '
                    'distinguishes ecological speciation from pure allopatric speciation?'
                ),
                'correct': (
                    'In ecological speciation, reproductive barriers evolve as a BYPRODUCT of '
                    'adaptation to different ecological niches — divergent selection on traits '
                    'like body shape, feeding apparatus, and mate preferences directly causes '
                    'reproductive isolation without requiring a geographic barrier. In pure '
                    'allopatric speciation, isolation can evolve via neutral drift alone during '
                    'geographic separation, independent of ecological divergence'
                ),
                'distractors': [
                    'Ecological speciation specifically requires TWO stages: first allopatric '
                    'separation for millions of years, then ecological divergence after secondary '
                    'contact — without an initial allopatric phase, ecological speciation cannot '
                    'occur because gene flow would prevent any divergence',
                    'Ecological speciation is distinguished by producing hybrids that are '
                    'ecologically intermediate (unable to survive in either parental environment), '
                    'while allopatric speciation produces hybrids with random phenotypes that can '
                    'survive in any environment they encounter',
                    'The two modes are identical in mechanism and differ only in terminology — '
                    '"ecological speciation" is a modern name for any case of allopatric speciation '
                    'that happens to involve ecological differences between the separated '
                    'populations',
                ],
            },
            {
                'question': (
                    'ISOLATION BY DISTANCE describes a situation where no discrete barrier exists, '
                    'but individuals disperse only short distances, so gene flow decreases gradually '
                    'with geographic distance across a species\' range. Why can isolation by distance '
                    'alone eventually produce speciation without any geographic event?'
                ),
                'correct': (
                    'In isolation-by-distance populations, genetic divergence accumulates at the '
                    'ENDS of the range because mutations and drift in one end rarely reach the '
                    'other end before being replaced; given enough time and range length, '
                    'populations at opposite ends can become reproductively isolated even though '
                    'intermediate populations are still connected — producing a "ring species" '
                    'pattern where the two ends are separate species despite a chain of '
                    'interbreeding populations between them'
                ),
                'distractors': [
                    'Isolation by distance cannot actually produce speciation — without a discrete '
                    'barrier, gene flow always exceeds the divergence rate, so any populations '
                    'along a continuous range will remain a single species indefinitely regardless '
                    'of how large the range is',
                    'Isolation by distance produces speciation only when combined with strong '
                    'reinforcement — selection must specifically favor shorter-range dispersers '
                    'so that the populations become physically separated, at which point the '
                    'mechanism becomes indistinguishable from allopatric speciation',
                    'Isolation by distance produces rapid speciation because mutation rates are '
                    'highest in populations at the edges of a species range — edge populations '
                    'accumulate new alleles faster than central populations and diverge into '
                    'separate species within a few generations',
                ],
            },
            {
                'question': (
                    'Allopatric speciation is considered the most common speciation mode in '
                    'animals, while sympatric speciation is the most CONTROVERSIAL. What specific '
                    'conditions must be met for sympatric speciation to overcome its main '
                    'theoretical obstacle?'
                ),
                'correct': (
                    'Sympatric speciation requires DISRUPTIVE SELECTION strong enough to overcome '
                    'the homogenizing effect of gene flow within a freely mixing population — '
                    'selection must favor two different phenotypes (e.g., host preference in '
                    'Rhagoletis) while selecting against intermediate forms, AND a mechanism '
                    'for assortative mating must link mate choice to the disruptive trait so '
                    'that the two forms stop interbreeding'
                ),
                'distractors': [
                    'Sympatric speciation requires that the population first experience a genetic '
                    'bottleneck — small founder populations can diverge through drift even in the '
                    'face of gene flow, which is why sympatric speciation is usually associated '
                    'with founder effects rather than selection',
                    'Sympatric speciation requires the population to be polyploid — only polyploid '
                    'organisms can sustain the chromosomal divergence needed to overcome gene flow '
                    'in a sympatric setting, which is why sympatric speciation is nearly restricted '
                    'to flowering plants',
                    'Sympatric speciation occurs whenever a new mutation arises that affects mate '
                    'choice — a single mutation in a mate-recognition gene is always sufficient '
                    'to trigger sympatric speciation regardless of the selection environment',
                ],
            },
            {
                'question': (
                    'Allopolyploidy is common in flowering plants (possibly ~half of all species) '
                    'but rare in animals. Why can allopolyploidy still produce new animal species '
                    'despite being rare, and which animal groups have documented allopolyploid '
                    'species?'
                ),
                'correct': (
                    'Allopolyploidy has been documented in insects, frogs, fish, and even some '
                    'mammals — it is rare because most animals have separate sexes with chromosomal '
                    'sex determination, which is disrupted by genome doubling. But in groups where '
                    'sex determination is flexible or species can reproduce via parthenogenesis, '
                    'allopolyploid speciation can occasionally succeed, producing real cases of '
                    'one-generation speciation outside of plants'
                ),
                'distractors': [
                    'Allopolyploidy cannot actually produce animal species — every claimed animal '
                    'allopolyploid has turned out to be a misidentified hybrid with diploid '
                    'chromosome number; allopolyploidy is strictly a plant phenomenon',
                    'Allopolyploidy in animals only works for organisms that lack a circulatory '
                    'system — without blood, the metabolic problems of doubled genome size do '
                    'not prevent viability, which is why some insects and small invertebrates '
                    'can be allopolyploid but no vertebrates can',
                    'Allopolyploidy in animals only occurs in species with multiple mating types '
                    '(three or more sexes) — because standard male/female systems cannot '
                    'accommodate doubled genomes, only protists and some fungi can speciate via '
                    'this mechanism',
                ],
            },
        ],
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
        quiz=[
            {
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
            {
                'question': (
                    'The Mimulus guttatus × M. nasutus hybrid produces sterile pollen due to '
                    'interaction of loci Hms1 (from M. guttatus) and Hms2 (from M. nasutus). '
                    'Neither locus causes sterility in its own species. What does this tell us '
                    'about how BDM incompatibilities accumulate over time as populations diverge?'
                ),
                'correct': (
                    'As populations diverge and fix more alleles independently, the NUMBER of '
                    'potential incompatible pairings increases disproportionately fast — each new '
                    'substitution in one population can be incompatible with any of the previous '
                    'substitutions in the other population, so incompatibilities accumulate faster '
                    'than linearly with divergence time (the "snowball" effect)'
                ),
                'distractors': [
                    'The Mimulus case shows that BDM incompatibilities are always caused by exactly '
                    'two loci interacting — the two-locus BDM model is the maximum complexity '
                    'possible because adding a third incompatible locus would make hybrids '
                    'inviable rather than merely sterile',
                    'The Hms1/Hms2 case shows that BDM incompatibilities are always reciprocal — '
                    'if Hms1+Hms2 causes sterility in M. guttatus × M. nasutus hybrids, then '
                    'Hms2+Hms1 must also cause identical sterility in M. nasutus × M. guttatus '
                    'hybrids, making hybrid sterility symmetric in all BDM cases',
                    'BDM incompatibilities accumulate at a constant linear rate proportional to '
                    'divergence time — one new incompatible locus pair per million years on average, '
                    'regardless of which genes are evolving or how many substitutions have occurred',
                ],
            },
            {
                'question': (
                    'Horizontal gene transfer (HGT) allows bacteria to acquire genes from '
                    'entirely unrelated lineages. The E. coli pan-genome contains genes present '
                    'in some strains but absent from others, acquired by HGT. Why does HGT '
                    'make traditional species concepts especially problematic for bacteria?'
                ),
                'correct': (
                    'Species concepts assume that organisms within a species share a single '
                    'shared evolutionary history (common descent). HGT means bacterial strains '
                    'can have different evolutionary histories for different genes — some genes '
                    'trace to one ancestor, others to completely unrelated donors. A single '
                    '"species" may have no consistent gene tree, making lineage-based species '
                    'concepts incoherent'
                ),
                'distractors': [
                    'HGT makes species concepts problematic because it causes the same species '
                    'to have different 16S rRNA sequences — since 16S rRNA is the standard '
                    'bacterial species marker, HGT directly corrupts the measurement tool '
                    'used to identify bacterial species',
                    'HGT forces bacteria to evolve faster than eukaryotes, so species concepts '
                    'designed for slowly diverging organisms cannot be applied — the 97% '
                    'sequence-identity threshold needs to be recalibrated to a lower number '
                    'for organisms with HGT-accelerated evolution',
                    'HGT is only problematic for species concepts in pathogenic bacteria because '
                    'antibiotic resistance genes are the ones most commonly transferred — '
                    'environmental bacteria that lack plasmids can still be classified using '
                    'standard eukaryotic species concepts without modification',
                ],
            },
            {
                'question': (
                    'Polar bears diverged from brown bears ~479,000–343,000 years ago (Liu et al. '
                    '2014), much more recently than earlier estimates of ~5 million years. Strong '
                    'positive selection acted on APOB (cholesterol binding) and heart function genes. '
                    'Yet genomic evidence shows continued gene flow FROM polar bears INTO brown bears '
                    '(one-way). How do polar bears remain distinct species despite ongoing gene flow?'
                ),
                'correct': (
                    'Most alleles transferred from polar bears to brown bears are selected against '
                    'in the brown bear\'s ecological context (open forest, omnivorous diet) — '
                    'polar bear-specific adaptations (APOB for high-fat seal diet, Arctic '
                    'pigmentation genes) reduce fitness in brown bears so they are purged by '
                    'selection, preventing integration of the polar-bear genome into brown bear populations'
                ),
                'distractors': [
                    'Polar bears and brown bears remain distinct because gene flow is so rare that '
                    'fewer than one allele per generation crosses the species boundary — at this '
                    'rate, drift within each population is far stronger than the homogenizing '
                    'effect of gene flow, maintaining the species distinction',
                    'The species remain distinct because gene flow is only one-way — polar bear '
                    'alleles entering brown bears do not provide any reproductive feedback that '
                    'would allow brown bear alleles to enter the polar bear population, so '
                    'the polar bear genome remains uncontaminated and fully isolated',
                    'Polar bears and brown bears remain distinct because they have strong '
                    'behavioral isolation — brown bears flee from polar bears on contact '
                    'and never voluntarily interbreed, so the "pizzly" hybrids documented '
                    'in the wild are the result of captive escapes rather than natural mating',
                ],
            },
            {
                'question': (
                    'The Drosophila "Hybrid male rescue" (Hmr) gene in D. melanogaster and the '
                    '"Lethal hybrid rescue" (Lhr) gene in D. simulans each function normally in '
                    'their own species, but together in a male hybrid they cause lethality. '
                    'How does this specific gene pair exemplify the classical BDM model?'
                ),
                'correct': (
                    'Hmr and Lhr evolved independently in the two Drosophila lineages with each '
                    'allele functioning normally against the ancestral background of its own '
                    'species — in the hybrid, the two derived alleles meet for the first time '
                    'and interact pathogenically. This is exactly the BDM prediction: neither '
                    'allele is broken alone, but their epistatic interaction in hybrids is lethal'
                ),
                'distractors': [
                    'Hmr and Lhr are named for their "rescue" function — they act as second-site '
                    'suppressors that restore viability in hybrids. The BDM model describes their '
                    'function as partial rescuers of hybrid lethality, not as the direct cause '
                    'of the lethality itself',
                    'The Hmr/Lhr pair is a BDM example because both genes are on the X chromosome '
                    '— all BDM incompatibilities are located on sex chromosomes, which is why '
                    'only male hybrids are affected while female hybrids carry both X chromosomes '
                    'and remain viable',
                    'Hmr and Lhr illustrate BDM because they duplicate each other\'s function — '
                    'having both alleles together in a hybrid creates a dosage imbalance rather '
                    'than an epistatic incompatibility, and dosage effects are the primary '
                    'mechanism of BDM lethality',
                ],
            },
            {
                'question': (
                    'The term "snowball effect" describes the observation that BDM incompatibilities '
                    'accumulate faster than linearly with divergence time. If two populations have '
                    'each fixed 10 substitutions independently, how does the number of potential '
                    'incompatible pairs compare to a case of only 2 substitutions per population?'
                ),
                'correct': (
                    'With 2 substitutions each, there are 2×2=4 potential incompatible pairs. '
                    'With 10 substitutions each, there are 10×10=100 potential incompatible pairs '
                    '— a 25-fold increase from only a 5-fold increase in per-population substitutions. '
                    'The number of possible incompatibilities grows as the PRODUCT of substitutions '
                    'on each side, explaining why hybrid fitness deteriorates faster than linearly '
                    'as divergence proceeds'
                ),
                'distractors': [
                    'The number of incompatible pairs grows linearly with substitutions — with 2 '
                    'substitutions each there are 2+2=4 pairs, and with 10 substitutions each there '
                    'are 10+10=20 pairs. The "snowball" name is misleading because the actual '
                    'accumulation is linear rather than accelerating',
                    'The number of incompatibilities is constant regardless of substitution count '
                    '— only a small fixed number of genes are capable of causing BDM incompatibilities, '
                    'so additional substitutions beyond those critical genes do not affect hybrid '
                    'fitness at all',
                    'The number of incompatibilities is determined by chromosomal rearrangements '
                    'rather than point substitutions — the snowball effect refers to the rapid '
                    'accumulation of inversions and translocations between diverging populations, '
                    'not to single-nucleotide incompatibilities'
                ],
            },
            {
                'question': (
                    '10,000 bacterial "species" can be found in a single teaspoon of soil, and '
                    'most cannot be grown in pure culture. How does this finding illustrate why '
                    'species concepts are especially problematic for bacteria?'
                ),
                'correct': (
                    'Most bacterial diversity is measured only through environmental DNA and '
                    '16S rRNA sequencing rather than through culturable isolates — researchers '
                    'can detect genetic clusters but cannot test reproductive compatibility (there '
                    'is no sex), cannot observe phenotype (no pure cultures), and cannot distinguish '
                    'true species from environmental strains exchanging genes via HGT. The scale '
                    'of unmeasured diversity makes traditional species concepts impractical'
                ),
                'distractors': [
                    'The 10,000 bacterial species in a teaspoon of soil demonstrate that bacteria '
                    'reproduce faster than eukaryotes, producing so many species per generation '
                    'that no classification scheme could keep up — the problem is taxonomic rate '
                    'rather than conceptual',
                    'Soil bacteria are mostly close relatives of gut bacteria and can be classified '
                    'by analogy to the human microbiome — the 10,000 species figure is an '
                    'overestimate that reflects sequencing artifacts rather than true diversity',
                    'The teaspoon figure proves that bacteria have already been fully classified '
                    'using 16S rRNA — only the 97% identity threshold is needed to delimit bacterial '
                    'species, and soil diversity does not pose any conceptual problems for bacterial '
                    'taxonomy',
                ],
            },
            {
                'question': (
                    'DNA barcoding revealed that Apanteles leucostigmus parasitoid wasp was actually '
                    '32 cryptic species. Cryptic species complexes like this are documented in '
                    'Anopheles gambiae (7 species) and Leishmania (multiple). What does the '
                    'prevalence of cryptic species tell us about the relationship between '
                    'morphology and reproductive isolation?'
                ),
                'correct': (
                    'Reproductive isolation can evolve WITHOUT any morphological change — two '
                    'populations can diverge into fully separate species (zero gene flow, '
                    'independent evolutionary trajectories) while remaining morphologically '
                    'indistinguishable. This demonstrates that morphological similarity is a '
                    'POOR indicator of species status, and that traditional morphology-based '
                    'taxonomy has systematically undercounted real species diversity'
                ),
                'distractors': [
                    'Cryptic species prove that morphological evolution and reproductive isolation '
                    'are inversely related — species that look identical have high reproductive '
                    'isolation, while species that look different often freely interbreed. This '
                    'is why cryptic species are the most rigorously isolated of all species types',
                    'The prevalence of cryptic species shows that morphology evolves by drift '
                    'rather than selection — since cryptic species have identical morphology '
                    'despite genetic divergence, morphological traits must not be under any '
                    'selection and are simply neutral markers',
                    'Cryptic species are rare exceptions that confirm the general rule — in '
                    'most taxa, morphological divergence closely tracks reproductive isolation, '
                    'and cryptic species complexes like Anopheles and Apanteles are unusual '
                    'cases caused by recent rapid speciation',
                ],
            },
            {
                'question': (
                    'Paul Hebert and Daniel Janzen\'s 2004 DNA barcoding study of Astraptes fulgerator '
                    'in Costa Rica used the mitochondrial CO1 gene to reveal that the "species" was '
                    'actually 10 distinct cryptic species. What specific advantage does mitochondrial '
                    'CO1 have over nuclear markers for cryptic species detection?'
                ),
                'correct': (
                    'CO1 is present in every animal cell as multiple mitochondrial copies (making '
                    'it easy to amplify from small or degraded samples), evolves fast enough to '
                    'distinguish recently diverged species, and is inherited maternally (so it '
                    'reflects matrilineal evolutionary history without recombination complications) '
                    '— these features make it a standardized "barcode" that works across animal '
                    'groups, unlike nuclear genes that vary in copy number and are often too '
                    'conserved to resolve recent divergences'
                ),
                'distractors': [
                    'CO1 is advantageous because it encodes a cell-surface marker expressed on '
                    'all mitochondria — the protein can be detected with antibodies in fresh '
                    'tissue, allowing researchers to identify species without any DNA sequencing',
                    'CO1 works because it is the only gene that is fully conserved across all '
                    'insect species — the conserved sequence allows researchers to directly '
                    'compare any two insects without needing species-specific primers',
                    'The CO1 gene has the advantage of being selectively neutral in all animal '
                    'lineages — because it does not affect fitness, its evolution is a perfect '
                    'molecular clock that gives the same divergence time estimate for every '
                    'species pair regardless of ecology',
                ],
            },
            {
                'question': (
                    'The 97% sequence identity threshold is commonly used to distinguish bacterial '
                    '"species" based on 16S rRNA. A student asks why 97% was chosen rather than 99% '
                    'or 95%. What is the best answer to this question?'
                ),
                'correct': (
                    'The 97% threshold is a PRAGMATIC convention, not a biological law — it was '
                    'chosen because it roughly corresponds to the level of 16S divergence typically '
                    'seen between bacterial groups that also differ in DNA-DNA hybridization and '
                    'average nucleotide identity at the genome level. It has known problems '
                    '(S. pneumoniae vs S. mitis are 99% identical at 16S but clearly different '
                    'species) and is continually debated, illustrating that bacterial species '
                    'boundaries are operational rather than fundamental'
                ),
                'distractors': [
                    'The 97% threshold was calculated from the mutation rate of bacteria — at the '
                    'average bacterial generation time, 3% divergence represents exactly one '
                    'million years of evolution, which corresponds to the standard definition of '
                    'species-level divergence in all taxonomic groups',
                    'The 97% threshold is the point at which horizontal gene transfer between '
                    'bacterial strains stops — once two strains are less than 97% identical, '
                    'HGT becomes impossible and the two lineages begin evolving independently, '
                    'satisfying the lineage definition of a species',
                    'The 97% threshold is a biological constant derived from the ribosomal '
                    'structure — at less than 97% identity, the 30S ribosomal subunit cannot '
                    'function, proving that bacteria with different 16S sequences cannot be '
                    'the same species because they would have incompatible ribosomes',
                ],
            },
        ],
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
        quiz=[
            {
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
            {
                'question': (
                    'Laupala crickets show 37 species with NO ecological divergence — all eat '
                    'the same food and live in the same habitat, diverging only in courtship '
                    'song. How does this challenge the assumption that speciation typically '
                    'requires ecological differentiation?'
                ),
                'correct': (
                    'It demonstrates that SEXUAL SELECTION alone — divergent mate recognition '
                    'signals and matching female preferences — can drive complete reproductive '
                    'isolation between populations inhabiting the same ecological niche, without '
                    'any contribution from differential adaptation or disruptive natural selection '
                    'on resource use'
                ),
                'distractors': [
                    'Laupala speciation does not challenge the ecological assumption because the '
                    '37 species occupy different elevational zones in Hawaii — the ecological '
                    'gradient is invisible to a lab researcher but acts as a strong selective '
                    'force separating populations in the field',
                    'Laupala speciation confirms the ecological requirement — the divergent '
                    'courtship songs function as ecological signals that allow females to identify '
                    'mates from the same local population, so sexual selection IS a form of '
                    'ecological divergence in this context',
                    'The absence of ecological divergence means Laupala are not truly separate '
                    'species — without ecological isolation, any behavioral barriers are transient '
                    'and the 37 "species" will eventually fuse back into one species when '
                    'populations come into secondary contact',
                ],
            },
            {
                'question': (
                    'DNA barcoding uses short mitochondrial DNA segments as species markers. '
                    'Hebert and Janzen (2004) used DNA barcoding to reveal that Astraptes '
                    'fulgerator was actually 10 cryptic species. What is one important '
                    'LIMITATION of DNA barcoding that should be considered when interpreting '
                    'such results?'
                ),
                'correct': (
                    'DNA barcoding uses only MITOCHONDRIAL DNA, which has a single maternal '
                    'inheritance pattern and no recombination — it may overestimate species '
                    'diversity if deep mitochondrial lineages exist within a single sexually '
                    'reproducing species (mito-nuclear discordance), or fail to detect cryptic '
                    'species that have identical mitochondria but divergent nuclear genomes'
                ),
                'distractors': [
                    'DNA barcoding cannot work for insects because insect mitochondrial DNA '
                    'evolves too slowly to distinguish recently diverged species — the technique '
                    'is only reliable for vertebrates where mitochondrial substitution rates '
                    'are calibrated against fossil-dated divergence events',
                    'DNA barcoding can only identify cryptic species within a single geographic '
                    'region — applying it across different continents produces false positives '
                    'because mitochondrial haplotypes diverge with geography even within a '
                    'single species, creating spurious species boundaries',
                    'DNA barcoding requires the prior identification of at least one known species '
                    'boundary to calibrate the threshold — without this reference, the technique '
                    'has no way to distinguish within-species variation from between-species '
                    'divergence in the mitochondrial marker region',
                ],
            },
            {
                'question': (
                    'The Schemske & Bradshaw (1999) Mimulus experiment in the Sierra Nevada '
                    'showed that M. lewisii (bee-pollinated) and M. cardinalis (hummingbird-'
                    'pollinated) do not hybridize in nature despite overlapping ranges. In '
                    'the greenhouse, hand-pollination produces viable F1 and F2 hybrids. '
                    'Which type of isolating barrier is PRIMARY, and why does it prevent '
                    'gene flow even in sympatry?'
                ),
                'correct': (
                    'Pollinator isolation (pre-mating prezygotic) — bees visit M. lewisii '
                    '100% of the time and hummingbirds visit M. cardinalis ~97% of the time '
                    'because flower morphology, color, and nectar reward match each pollinator '
                    'guild\'s sensory preferences. Pollen from one species is never deposited '
                    'on the stigma of the other in the field, even though the plants are '
                    'physically capable of producing viable hybrids'
                ),
                'distractors': [
                    'Temporal isolation is primary — M. lewisii flowers in spring when bees '
                    'are active and M. cardinalis flowers in summer when hummingbirds migrate '
                    'through the Sierra Nevada, so the two species simply never have pollen '
                    'available at the same time regardless of pollinator identity',
                    'Gametic incompatibility is the primary barrier — bee-transferred M. lewisii '
                    'pollen cannot fertilize M. cardinalis ovules because the pollen tube '
                    'recognition proteins diverged under the different pollinator-mediated '
                    'selection pressures, making the post-mating barrier complete',
                    'Hybrid inviability is the primary barrier — F1 hybrids between the two '
                    'species die before reaching flowering stage because the intermediate '
                    'flower morphology is recognized by neither bees nor hummingbirds, so '
                    'hybrids cannot be pollinated and produce zero seeds',
                ],
            },
            {
                'question': (
                    'Knowlton (1993) tested Panama shrimp species pairs from opposite sides of '
                    'the isthmus by placing them together in lab tanks — they refused to '
                    'interbreed. Phylogenetic analysis showed sister taxa on each side of the '
                    'isthmus. Why does the COMBINATION of phylogenetic sister-pair data AND '
                    'lab mating experiments provide stronger evidence for allopatric speciation '
                    'than either line of evidence alone?'
                ),
                'correct': (
                    'The phylogeny shows the speciation event was driven by the geological '
                    'barrier (sister taxa diverged precisely at the isthmus closure time, not '
                    'at other times). The mating experiment independently confirms that the '
                    'divergence has produced complete reproductive isolation (not just neutral '
                    'drift). Together they establish both the cause (geography) AND the outcome '
                    '(species-level reproductive isolation) — each alone would leave one of the '
                    'two questions unanswered'
                ),
                'distractors': [
                    'The combination is stronger because both lines of evidence test the same '
                    'hypothesis (genetic divergence) using independent methods — their agreement '
                    'reduces the probability that one of them is artifactually biased, with the '
                    'phylogeny serving as a quality control check on the mating experiment',
                    'The combined approach is stronger because mating experiments are the only '
                    'way to test speciation in extinct lineages — the phylogeny documents which '
                    'lineages were extinct and the mating experiments confirm the extant ones are '
                    'separate species, giving complete coverage of the taxonomic group',
                    'The two lines of evidence are equivalent and one alone would suffice for '
                    'allopatric speciation claims — Knowlton included both only to publish in a '
                    'journal that required multiple experimental methods per paper',
                ],
            },
            {
                'question': (
                    'Kerry Shaw\'s Laupala crickets show 37 species on Hawaii with a rate of ~6 new '
                    'species in 430,000 years on the Big Island — approximately 10× the average '
                    'arthropod speciation rate. How do male courtship songs provide the mechanistic '
                    'explanation for this unusually fast speciation rate?'
                ),
                'correct': (
                    'Laupala males produce species-specific pulse-rate songs by rubbing their legs '
                    'together; females respond only to conspecific songs. Because the SAME genetic '
                    'locus controls both male song production AND female preference (Shaw & Lesnick '
                    '2009), a single mutation can simultaneously shift both sender and receiver, '
                    'producing immediate prezygotic isolation without needing separate sequential '
                    'mutations in male and female traits — this one-step coupling enables the '
                    'unusually rapid speciation rate'
                ),
                'distractors': [
                    'Laupala speciation is fast because courtship songs evolve under drift rather '
                    'than selection — drift always produces faster trait change than selection, '
                    'so song-based speciation is automatically faster than ecology-based speciation '
                    'in any organism',
                    'Laupala\'s speed comes from having very short generation times — the crickets '
                    'reproduce many times per year, and speciation rate scales directly with the '
                    'number of generations per calendar year regardless of the genetic architecture '
                    'of mating signals',
                    'The Laupala case is actually an example of ecological speciation disguised '
                    'as sexual selection — the songs function as species markers for different '
                    'elevational habitats, and the observed song divergence reflects underlying '
                    'ecological isolation',
                ],
            },
            {
                'question': (
                    'The Astraptes fulgerator butterfly had been catalogued as ONE species since '
                    '1755 until Hebert & Janzen (2004) used DNA barcoding to reveal it was actually '
                    '10 cryptic species. What initial OBSERVATION made Janzen suspect cryptic '
                    'species before the DNA barcoding was performed?'
                ),
                'correct': (
                    'Janzen had noticed that Astraptes CATERPILLARS fed on many different plant '
                    'species AND had distinctly different color patterns — both observations are '
                    'inconsistent with a single species (most species have specific host '
                    'preferences and uniform color patterns), so he hypothesized that multiple '
                    'cryptic species were being lumped together as one. DNA barcoding then '
                    'confirmed his hypothesis by identifying 10 distinct genetic clusters '
                    'corresponding to different host-plant associations'
                ),
                'distractors': [
                    'Janzen noticed that adult butterflies showed different flight patterns and '
                    'mating behaviors in different forest regions — behavioral differences in '
                    'adults were the initial clue that led him to hypothesize multiple species '
                    'later confirmed by DNA barcoding',
                    'The initial suspicion came from finding Astraptes populations that refused '
                    'to interbreed in captivity — reproductive isolation was established through '
                    'mating experiments before any genetic data was collected, and DNA barcoding '
                    'simply confirmed the experimental results',
                    'Hebert identified the cryptic species first by genetic analysis, and Janzen '
                    'only later found ecological differences that correlated with the genetic '
                    'clusters — the discovery was driven entirely by DNA barcoding rather than '
                    'by any prior ecological observation',
                ],
            },
            {
                'question': (
                    'Streptococcus pneumoniae (lung pathogen) and S. mitis (harmless oral '
                    'commensal) have 99% identical 16S rRNA sequences — above the 97% '
                    '"same species" threshold commonly used in bacterial taxonomy. Yet they '
                    'are considered distinct species because of their dramatically different '
                    'ecologies. Why does this case illustrate the fundamental arbitrariness '
                    'of the 97% 16S rRNA threshold?'
                ),
                'correct': (
                    'The 97% threshold is a convenience, not a principled cutoff — bacteria '
                    'with nearly identical 16S rRNA (above 97%) can differ dramatically in '
                    'virulence, ecology, and pathogenicity because 16S rRNA is just one gene '
                    'and does not capture the full genomic and phenotypic diversity. Species '
                    'boundaries in bacteria do not map cleanly onto any single sequence metric'
                ),
                'distractors': [
                    'The 97% threshold is arbitrary because 16S rRNA evolves too slowly to '
                    'distinguish recent speciation events — for species that diverged within '
                    'the last 10 million years, 16S identity will always be above 97% even '
                    'for biologically distinct species, requiring a different gene marker '
                    'for modern taxonomy',
                    'The threshold is arbitrary because it only works for Gram-positive bacteria '
                    '— for Gram-negative bacteria like E. coli, a different threshold (99.5%) '
                    'is required, so the 97% rule cannot be applied universally across '
                    'bacterial diversity',
                    'The 97% threshold was originally set for archaea and later extended to '
                    'bacteria without recalibration — the correct bacterial threshold is '
                    'actually 95% identity, and the 97% figure is a persistent error in '
                    'microbiology textbooks that has never been corrected',
                ],
            },
            {
                'question': (
                    'The Laupala cricket phylogeny shows TWO independent colonizations of the '
                    'Big Island of Hawaii, each followed by rapid in situ radiation. Why does '
                    'the pattern of two independent colonizations strengthen rather than '
                    'weaken the sexual selection hypothesis for Laupala speciation?'
                ),
                'correct': (
                    'Two independent colonizations that each produced rapid radiations is '
                    'an example of REPLICATED speciation — if sexual selection drives Laupala '
                    'speciation, each independent colonization should generate similarly fast '
                    'diversification, which is exactly what is observed. This replication rules '
                    'out hypotheses that depend on unique historical events and supports the '
                    'mechanistic claim that the signal-preference genetic architecture itself '
                    'is what enables the fast rate'
                ),
                'distractors': [
                    'Two independent colonizations weaken the sexual selection hypothesis '
                    'because they prove Laupala diversity is driven by dispersal rather than '
                    'by within-island speciation — without in situ divergence, sexual '
                    'selection plays no role in species formation',
                    'The two colonizations are evidence of geographic isolation rather than '
                    'sexual selection — each colonization established a new allopatric '
                    'population, and speciation proceeded by traditional allopatric mechanisms '
                    'within each colonizing lineage independently',
                    'Two colonizations suggest that the Laupala species on the Big Island are '
                    'actually two completely unrelated groups incorrectly lumped as one genus '
                    '— molecular phylogeny should be used to separate them into two genera, '
                    'invalidating the "37 species in one genus" claim',
                ],
            },
            {
                'question': (
                    'Polar bears and brown bears diverged ~479-343 kya (Liu et al. 2014), and '
                    'strong positive selection acted on the APOB gene for cholesterol binding. '
                    'How does the APOB selection signature specifically support the hypothesis '
                    'that the seal-based polar bear diet drove speciation from brown bears?'
                ),
                'correct': (
                    'APOB (apolipoprotein B) is critical for binding and transporting cholesterol '
                    'in the blood — a polar bear\'s diet of seal blubber is extraordinarily '
                    'high in saturated fat and cholesterol, which would cause cardiovascular '
                    'disease in brown bears. Strong positive selection on APOB indicates that '
                    'the gene was rapidly modified to tolerate the new diet, directly linking '
                    'a specific ecological shift (marine seal predation) to the genomic signature '
                    'of adaptation and confirming that ecological divergence accompanied the '
                    'speciation event'
                ),
                'distractors': [
                    'APOB selection supports the diet hypothesis because APOB is the gene that '
                    'controls fat taste preferences — polar bears evolved to prefer the taste '
                    'of seal blubber through APOB mutations, without any underlying metabolic '
                    'change',
                    'APOB selection is unrelated to the diet hypothesis — APOB simply happens '
                    'to be on the same chromosome as the pigmentation genes that made polar '
                    'bears white, and the observed selection is a hitchhiking effect of '
                    'selection on coat color rather than diet',
                    'APOB selection refutes the diet hypothesis — if diet were driving speciation, '
                    'we would expect selection on digestive enzyme genes, not on blood lipid '
                    'transport genes, so the APOB signature actually points to a climate-driven '
                    'rather than diet-driven speciation event',
                ],
            },
        ],
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
