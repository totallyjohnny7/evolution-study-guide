"""Node generators for Lectures 1-7 (Exam 1 coverage).
Row numbering: Lec1=row 1, Lec2=row 2, Lec3=row 3, Lec4=row 4, Lec5-6=row 5, Lec7=row 6.
"""
from helpers import load_lec, slides_to_sections, build_node

def lec1_nodes():
    d = load_lec('lec1')
    nodes = []
    nodes.append(build_node(
        id='lec1-intro-evolution',
        title='What Is Evolution? Course Intro',
        subtitle='Why evolution unifies biology + practical applications (Lec 1 slides 1-9)',
        color='purple', row=1,
        heading='Lecture 1 — What Is Evolution?',
        sections=slides_to_sections(d, (1, 9)),
        examples=[
            "Dobzhansky: \"Nothing in biology makes sense except in the light of evolution\"",
            "Practical applications include antibiotic resistance, vaccine design, crop improvement, conservation.",
        ],
        warnings=[
            'EXAM TRAP: Evolution is NOT "organisms improving over time" and NOT "individuals changing." It is POPULATION-LEVEL change in allele frequencies across generations.',
            'Individuals do not evolve — populations do. A giraffe\'s neck does not grow longer because it stretches. The population shifts toward longer necks over generations.',
        ],
        mnemonic='CHANGE: Change in allele frequencies over generations — the minimal definition of evolution.',
        flashcard={
            'front': 'Why is evolution considered the unifying theory of biology?',
            'back': 'Every subfield of biology — from cell biology to ecology — rests on the insight that organisms share common ancestry and have been modified over time by natural selection, drift, mutation, and gene flow. Without evolution, biological diversity and shared traits across species have no causal explanation (Dobzhansky 1973).',
        },
        quiz={
            'question': 'Which of the following is the most precise scientific definition of evolution?',
            'correct': 'A change in the frequency of alleles in a population across generations',
            'distractors': [
                'Organisms becoming more complex over time',
                'The appearance of new species through sudden mutation',
                'Improvement of individuals during their lifetime',
            ],
        },
        visual={
            'type': 'concept-map',
            'description': 'Evolution as the unifying hub of biology',
            'regions': [
                {'label': 'Core claim', 'color': '#8a5cf6', 'items': ['Change in allele frequencies over generations']},
                {'label': 'Explains', 'color': '#4ea8de', 'items': ['Biodiversity', 'Shared homologies', 'Fossil record', 'Adaptation']},
                {'label': 'Practical uses', 'color': '#ffc857', 'items': ['Antibiotic resistance', 'Vaccine design', 'Crop breeding', 'Conservation']},
            ],
            'arrows': [],
            'tooltips': [],
            'mnemonic': 'Allele frequency change = evolution. Everything else is a consequence.',
            'trap': 'Common misconception: evolution means "progress" or "improvement." Evolution is directional only in the sense of local fitness — there is no global ladder.',
        },
    ))
    nodes.append(build_node(
        id='lec1-flu-case-study',
        title='Flu Virus: Evolution in Action',
        subtitle='H1N1 rapid evolution — a real-time case study (Lec 1 slides 10-21)',
        color='coral', row=1,
        heading='Lecture 1 — Influenza as Evolution Case Study',
        sections=slides_to_sections(d, (10, 21)),
        examples=[
            'H1N1 2009 pandemic: traced back to swine-origin reassortment; tracked in real time via global genomic sampling.',
            'Hemagglutinin and neuraminidase surface proteins accumulate amino acid substitutions — driving antigenic drift.',
        ],
        warnings=[
            'Not all mutations are selected for — most are neutral or deleterious. Only rare beneficial substitutions are fixed.',
        ],
        mnemonic='HA-NA: HemAgglutinin and NeurAminidase — the flu\'s two most-evolving proteins, and the targets of vaccines.',
        flashcard={
            'front': 'How does influenza virus illustrate rapid evolution by natural selection?',
            'back': 'Influenza has an 8-segment RNA genome and a high error-rate RNA polymerase (no proofreading). Errors create variants constantly. Host immunity selects for variants whose surface proteins (HA, NA) evade recognition, so amino acid substitutions accumulate on the surface. Comparing samples worldwide showed that the 2009 H1N1 pandemic strain descended from reassortment between human, avian, and swine flu lineages — tracked in real time by phylogenetic analysis.',
        },
        quiz={
            'question': 'Which feature of influenza most directly explains why new vaccine formulations are needed each year?',
            'correct': 'High mutation rate in surface proteins HA and NA drives antigenic drift',
            'distractors': [
                'The virus physically grows larger each year',
                'Humans gradually lose immunity to all pathogens over time',
                'New animal hosts invent new flu types annually',
            ],
        },
        visual={
            'type': 'flow',
            'description': 'Flu evolution loop: error-prone replication → surface mutation → selection by host immunity',
            'regions': [
                {'label': '1. Replication', 'color': '#ff6b6b', 'items': ['No proofreading RNA pol', 'Mutations per replication']},
                {'label': '2. Surface change', 'color': '#ffc857', 'items': ['HA/NA amino acid substitutions', 'Antigenic drift']},
                {'label': '3. Host selection', 'color': '#4ea8de', 'items': ['Immune escape', 'Reinfection possible']},
                {'label': '4. Spread', 'color': '#7de2d1', 'items': ['New dominant strain', 'Repeat cycle']},
            ],
            'arrows': [],
            'tooltips': [],
            'mnemonic': 'Error → Drift → Escape → Spread.',
            'trap': 'Antigenic DRIFT (small mutations, gradual) ≠ antigenic SHIFT (reassortment of whole RNA segments, sudden pandemic strains).',
        },
    ))
    nodes.append(build_node(
        id='lec1-takehome-course',
        title='Lecture 1 Take-Home & Course Info',
        subtitle='Why evolution matters + course logistics (Lec 1 slides 22-30)',
        color='gray', row=1,
        heading='Lecture 1 — Take-Home & Course Information',
        sections=slides_to_sections(d, (22, 30)),
        mnemonic='Read → Attend → Apply: passive reading isn\'t enough for BIOL 4230.',
        flashcard={
            'front': 'What are the three main reasons the instructor gives for why understanding evolutionary principles is important?',
            'back': '(1) It explains patterns we observe in all living organisms; (2) It has direct practical applications (medicine, agriculture, conservation); (3) It provides the only coherent framework for asking "why" questions in biology.',
        },
        quiz={
            'question': 'According to Lecture 1, which feature most distinguishes evolutionary biology as a SCIENCE rather than just a historical account of life?',
            'correct': 'It generates testable, falsifiable predictions about allele frequencies, fitness, and adaptation — not just post-hoc narratives',
            'distractors': [
                'It relies on direct observation of speciation events, which occur over human-observable timescales',
                'It explains only past events and makes no predictions about future population change',
                'Its claims are insulated from genetic evidence because behavior cannot be fossilized',
            ],
        },
        visual={
            'type': 'bullet',
            'description': 'Course pillars',
            'regions': [
                {'label': 'Pillars', 'color': '#888', 'items': ['Mechanisms', 'Evidence', 'Applications']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'MEA: Mechanisms → Evidence → Applications.',
            'trap': '',
        },
    ))
    return nodes


def lec2_nodes():
    d = load_lec('lec2')
    nodes = []
    nodes.append(build_node(
        id='lec2-pre-darwin',
        title='Pre-Darwin Evolutionary Thinking',
        subtitle='Linnaeus, Cuvier, Lamarck — the road to Darwin (Lec 2 slides 1-9)',
        color='amber', row=2,
        heading='Lecture 2 — Evolutionary Thinking Before Darwin',
        sections=slides_to_sections(d, (1, 9)),
        quotes=['"Special creation" = the pre-Darwinian view that each species was divinely created in its present form.'],
        examples=[
            'Linnaeus (1707-1778): classified organisms into hierarchical groups — kingdom, class, order, genus, species.',
            'Cuvier: documented extinction using fossils, proposed catastrophism.',
            'Lamarck: first formal theory of evolution — inheritance of acquired characteristics (incorrect mechanism, but correctly recognized change).',
            'Lyell: uniformitarianism — geological processes are gradual and ongoing (influenced Darwin).',
        ],
        mnemonic='LCLLL: Linnaeus (classification) → Cuvier (extinction) → Lamarck (first mechanism) → Lyell (deep time) → Darwin.',
        flashcard={
            'front': 'What was Lamarck\'s theory of evolution and why was its mechanism ultimately rejected?',
            'back': 'Lamarck proposed that organisms change during their lifetime in response to use/disuse, and that these acquired traits are passed to offspring (e.g., giraffe necks stretching). Modern genetics shows that changes to somatic tissues are not inherited — only changes to germ line DNA pass to offspring. Lamarck was correct that evolution happens and that it is an ongoing process, but the mechanism (inheritance of acquired characteristics) is false for most traits. Lamarck deserves credit for being the first to propose a mechanistic theory.',
        },
        quiz={
            'question': 'Which of these pre-Darwin thinkers FIRST articulated a formal mechanism for evolutionary change, even though that mechanism was wrong?',
            'correct': 'Jean-Baptiste Lamarck',
            'distractors': ['Carl Linnaeus', 'Georges Cuvier', 'Charles Lyell'],
        },
        visual={
            'type': 'timeline',
            'description': 'Pre-Darwin influences',
            'regions': [
                {'label': 'Linnaeus', 'color': '#ffc857', 'items': ['Taxonomy', 'Nested hierarchy']},
                {'label': 'Cuvier', 'color': '#ff6b6b', 'items': ['Extinction', 'Catastrophism']},
                {'label': 'Lamarck', 'color': '#4ea8de', 'items': ['First mechanism', 'Acquired traits (wrong)']},
                {'label': 'Lyell', 'color': '#7de2d1', 'items': ['Deep time', 'Uniformitarianism']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Linnaeus named, Cuvier buried, Lamarck mechanized, Lyell stretched time.',
            'trap': 'Do NOT confuse Lamarck\'s (wrong) inheritance of acquired characteristics with modern epigenetic inheritance — the latter is real but rare and does not explain most adaptation.',
        },
    ))
    nodes.append(build_node(
        id='lec2-darwin-voyage',
        title='Darwin\'s Voyage of the Beagle',
        subtitle='The observational foundation of evolutionary theory (Lec 2 slides 10-12)',
        color='teal', row=2,
        heading='Lecture 2 — Darwin\'s Voyage',
        sections=slides_to_sections(d, (10, 12)),
        examples=[
            '1831-1836: HMS Beagle circumnavigation. Darwin is 22 at departure.',
            'Galápagos finches: slight morphological differences between islands — a key observation that later fueled natural selection theory.',
            'Darwin waited over 20 years before publishing On the Origin of Species (1859), partly due to fear of controversy.',
        ],
        mnemonic='Beagle→Book: 5 years voyage (1831-36) + 23 years thinking = Origin (1859).',
        flashcard={
            'front': 'Why did Darwin wait so long (more than 20 years) to publish his theory of evolution by natural selection?',
            'back': 'Darwin was a meticulous scientist who wanted his argument to be airtight. He spent the decades after the Beagle voyage accumulating evidence from barnacles, pigeon breeding, plant hybridization, biogeography, and correspondence with other naturalists. He also knew the theory would be religiously and socially controversial. He was finally prompted to publish in 1858 when Alfred Russel Wallace independently arrived at the same theory and sent Darwin a manuscript — both read joint papers to the Linnean Society in 1858, and Origin followed in 1859.',
        },
        quiz={
            'question': 'Darwin\'s Voyage of the Beagle (1831-1836) contributed most directly to his theory because:',
            'correct': 'He observed variation between isolated populations that no single region alone would have revealed',
            'distractors': [
                'He isolated DNA from island species',
                'He performed laboratory breeding experiments on finches',
                'He measured gene frequencies across populations',
            ],
        },
        visual={
            'type': 'bullet',
            'description': 'Key Beagle observations',
            'regions': [
                {'label': 'Observations', 'color': '#7de2d1', 'items': ['Finch variation across islands', 'Fossils of extinct mammals', 'Volcanic island formation', 'Andes uplift']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'FIVA: Finches, Island biogeography, Volcanoes, Andes.',
            'trap': 'Darwin did not "see evolution in action" on the Beagle — he built the theory later from the totality of his observations.',
        },
    ))
    nodes.append(build_node(
        id='lec2-natural-selection-ingredients',
        title='Natural Selection: The Four Ingredients',
        subtitle='Variation, heritability, differential reproduction → evolution (Lec 2 slides 13-23)',
        color='blue', row=2,
        heading='Lecture 2 — The Logic of Natural Selection',
        sections=slides_to_sections(d, (13, 23)),
        examples=[
            'Variation: individuals in a population differ in traits (beak size, coat color, etc.)',
            'Heritability: offspring resemble parents more than unrelated individuals.',
            'Differential reproductive success: some variants leave more descendants.',
            'Inference: the successful variants\' traits become more common each generation.',
        ],
        warnings=[
            'If ANY ingredient is missing, natural selection cannot occur. A trait must be heritable — non-heritable differences (e.g., sunburn) do not evolve.',
            'Natural selection acts on phenotypes, but evolution is measured as allele frequency change at the genotype level.',
        ],
        mnemonic='VHI-DRS: Variation + Heritability + Inference-from-Differential-Reproductive-Success = Evolution.',
        flashcard={
            'front': 'What are the four necessary ingredients for evolution by natural selection, and what is the logical inference that follows from combining them?',
            'back': '(1) Phenotypic variation among individuals; (2) Heritability of that variation (offspring resemble parents); (3) Differential survival and reproduction based on phenotype (i.e., fitness differences); (4) More offspring produced than can survive (Malthusian overproduction). INFERENCE: The phenotypes linked to higher fitness will become more common each generation — the population evolves. If ANY ingredient is missing, no evolution by natural selection occurs.',
        },
        quiz={
            'question': 'A population of plants shows variation in leaf shape, but leaf shape is entirely determined by soil chemistry and not passed from parent to offspring. Can natural selection act on this variation?',
            'correct': 'No — without heritability, differential reproduction will not change allele frequencies',
            'distractors': [
                'Yes — any phenotypic variation is sufficient for evolution by natural selection',
                'Yes — but only if the variation produces differences in germination rate',
                'No — but only because plants reproduce vegetatively rather than sexually',
            ],
        },
        visual={
            'type': 'cycle',
            'description': 'The natural selection cycle',
            'regions': [
                {'label': '1. Variation', 'color': '#4ea8de', 'items': ['Phenotypic differences among individuals']},
                {'label': '2. Heritability', 'color': '#7de2d1', 'items': ['Traits passed to offspring']},
                {'label': '3. Overproduction', 'color': '#ffc857', 'items': ['More offspring than can survive']},
                {'label': '4. Differential fitness', 'color': '#ff6b6b', 'items': ['Some variants survive/reproduce more']},
                {'label': '5. Next generation', 'color': '#8a5cf6', 'items': ['Winning variants more common']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'VHOD→N: Variation, Heritability, Overproduction, Differential fitness → Next generation changed.',
            'trap': 'Natural selection does NOT produce traits — it only sorts among existing variants. The source of variation is mutation + recombination.',
        },
    ))
    nodes.append(build_node(
        id='lec2-finches-case',
        title='Galápagos Finches: Selection Case Study',
        subtitle='Grant & Grant beak size evolution (Lec 2 slides 24-31)',
        color='green', row=2,
        heading='Lecture 2 — Evolution of Beak Shape in Galápagos Finches',
        sections=slides_to_sections(d, (24, 31)),
        examples=[
            'Peter and Rosemary Grant measured beak depth in Geospiza fortis on Daphne Major across decades.',
            '1977 drought: small soft seeds disappeared; only large hard seeds remained. Birds with larger, deeper beaks survived at higher rates.',
            'Next generation had significantly larger average beak size — directly measured evolution by natural selection.',
        ],
        warnings=[
            'EXAM TRAP: The Grant finch study showed selection REVERSED in wet years — larger beaks were selected AGAINST when large hard seeds were gone and small soft seeds dominated again. Selection direction tracks the environment, it is NOT unidirectional.',
            'Heritability of beak depth (h² ≈ 0.65-0.8) was measured by parent-offspring regression in the Grant study — not assumed. Without measuring heritability, you cannot confirm the R = h²S prediction.',
        ],
        mnemonic='4 conditions confirmed in finches: Variable beaks, Heritable beaks, Survival differences, Beak size mattered → Positive selection for larger beaks.',
        flashcard={
            'front': 'How did the Grants\' Galápagos finch study provide direct empirical evidence for each ingredient of natural selection?',
            'back': '(1) VARIATION: Beak depth varied among individual Geospiza fortis. (2) HERITABILITY: Parent-offspring regression showed beak depth is heritable (h² ≈ 0.65-0.8). (3) DIFFERENTIAL SURVIVAL: During the 1977 drought, birds with deeper beaks ate hard Tribulus seeds and survived while smaller-beaked birds died. (4) INFERENCE CONFIRMED: The next generation had significantly larger average beak depth — selection was measured, not inferred.',
        },
        quiz={
            'question': 'In the Grant finch study, what was the selective pressure that drove evolution of larger beaks in 1977?',
            'correct': 'A drought eliminated small, soft seeds, leaving mostly large, hard seeds that only birds with deep beaks could crack',
            'distractors': [
                'A new predator preferred small-beaked birds',
                'Birds intentionally grew larger beaks during the drought',
                'Climate cooling caused beaks to grow larger',
            ],
        },
        visual={
            'type': 'before-after',
            'description': 'Drought-driven selection on beak size',
            'regions': [
                {'label': 'Pre-drought (1976)', 'color': '#7de2d1', 'items': ['Diverse seed sizes', 'Beak depth ~9.2 mm average']},
                {'label': 'Drought (1977)', 'color': '#ff6b6b', 'items': ['Only large hard seeds remain', 'Selection against small beaks']},
                {'label': 'Post-drought (1978)', 'color': '#4ea8de', 'items': ['Average beak depth shifted larger', '~4% increase measured']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Drought → Hard seeds → Deep beaks win.',
            'trap': 'After the drought ended, selection sometimes reversed direction (wet years favored smaller beaks). Selection is not unidirectional — it tracks environment.',
        },
    ))
    nodes.append(build_node(
        id='lec2-descent-modification',
        title='Descent with Modification & Common Ancestry',
        subtitle='Artificial selection, homology, tree-thinking (Lec 2 slides 32-41)',
        color='pink', row=2,
        heading='Lecture 2 — Descent with Modification',
        sections=slides_to_sections(d, (32, 41)),
        examples=[
            'Artificial selection on dogs, cabbage (all Brassica oleracea cultivars), corn — proves phenotypes can be dramatically reshaped by selection in few generations.',
            'Vertebrate embryonic homologies: pharyngeal arches, notochord — shared developmental stages reveal common ancestry.',
            'Vestigial organs: whale pelvis, human appendix, cave-fish eyes — traces of ancestral use.',
        ],
        warnings=[
            'The "march of progress" image (ape → human) is misleading — evolution is branching, not linear. Humans did not evolve FROM modern chimpanzees; we share a common ancestor.',
        ],
        mnemonic='DHA-V: Descent + Homology + Artificial selection + Vestigial organs = evidence for common ancestry.',
        flashcard={
            'front': 'How do vestigial organs provide evidence for descent with modification?',
            'back': 'Vestigial organs (e.g., whale hip bones, human appendix, flightless bird wings, cave fish eye sockets) are structures that have lost their original function but persist as reduced, functionless remnants. Their existence is only explicable under descent with modification: an ancestor used the structure, selection pressure for that function was relaxed, and the structure degraded over generations but was not fully eliminated. Under special creation, these "useless" structures would require ad-hoc explanations.',
        },
        quiz={
            'question': 'Which evidence most directly refutes the "march of progress" interpretation of evolution?',
            'correct': 'Phylogenies show evolution is a branching tree, with modern species as tips — not a linear sequence',
            'distractors': [
                'Mutations never happen in modern populations',
                'All modern species are equally ancient',
                'Fossils are rare and poorly preserved',
            ],
        },
        visual={
            'type': 'tree',
            'description': 'Branching vs linear models of evolution',
            'regions': [
                {'label': 'WRONG: linear', 'color': '#ff6b6b', 'items': ['Implies progress toward humans', 'Implies modern species are primitive', 'Hides branching diversity']},
                {'label': 'RIGHT: branching tree', 'color': '#7de2d1', 'items': ['Common ancestors at internal nodes', 'Modern species at tips', 'All tips equally "modern"']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Tree not ladder.',
            'trap': 'Humans are not descended from chimps — humans and chimps share a common ancestor ~7 million years ago.',
        },
    ))
    return nodes


def lec3_nodes():
    d = load_lec('lec3')
    nodes = []
    nodes.append(build_node(
        id='lec3-genes-proteins',
        title='Genes, Proteins & Gene Expression',
        subtitle='DNA-RNA-protein and regulatory networks (Lec 3 slides 1-9)',
        color='blue', row=3,
        heading='Lecture 3 — Genes and Heritable Variation',
        sections=slides_to_sections(d, (1, 9)),
        examples=[
            'DNA is a universal homology across all life — the code itself is evidence of common ancestry.',
            'Dolphin hindlimb genes are still present but transcriptionally silenced — regulation, not gene loss, explains limb absence.',
            'Gene expression is regulated by complex networks: enhancers, transcription factors, miRNA, chromatin state.',
        ],
        warnings=[
            'EXAM TRAP: "Central dogma" (DNA → RNA → Protein) does NOT mean every gene is always expressed. Transcriptional regulation determines WHICH genes are ON or OFF — the same genome can produce hundreds of different cell types.',
            'Reverse transcription (RNA → DNA) occurs in retroviruses and in the cell\'s own retrotransposons. This does NOT contradict the central dogma, which refers to information flow in normal cellular protein synthesis.',
        ],
        mnemonic='DNA → RNA → Protein (Central dogma), but REGULATION of this flow is what determines phenotype.',
        flashcard={
            'front': 'Why are dolphin hindlimb genes a surprising illustration of gene expression regulation?',
            'back': 'Dolphins are limbless in hindquarters, but genomic sequencing reveals the genes for building hindlimbs are still present in their DNA. Their hindlimbs do not develop because the regulatory pathway controlling limb outgrowth is suppressed during development — not because the genes were deleted. This shows that evolution can "lose" traits not by removing genes but by changing expression patterns. Occasionally, a dolphin is born with vestigial hindlimbs, revealing the dormant genetic capacity.',
        },
        quiz={
            'question': 'The observation that DNA is used as the hereditary molecule in all domains of life (bacteria, archaea, eukaryotes) is evidence for:',
            'correct': 'Common ancestry of all extant life',
            'distractors': [
                'Independent origins of each domain',
                'Convergent molecular evolution',
                'Horizontal gene transfer eliminating other molecules',
            ],
        },
        visual={
            'type': 'flow',
            'description': 'Genotype to phenotype pipeline',
            'regions': [
                {'label': 'DNA', 'color': '#4ea8de', 'items': ['Sequence of nucleotides']},
                {'label': 'mRNA', 'color': '#7de2d1', 'items': ['Transcription', 'Splicing']},
                {'label': 'Protein', 'color': '#ffc857', 'items': ['Translation', 'Folding']},
                {'label': 'Phenotype', 'color': '#ff6b6b', 'items': ['Structure + function']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Genes code, regulation decides.',
            'trap': 'Having a gene does NOT mean the trait is expressed. Regulation is just as important as sequence.',
        },
    ))
    nodes.append(build_node(
        id='lec3-mutations',
        title='Mutations: Raw Material of Evolution',
        subtitle='Types, rates, and effects (Lec 3 slides 10-17)',
        color='red', row=3,
        heading='Lecture 3 — Mutations',
        sections=slides_to_sections(d, (10, 17)),
        examples=[
            'Point mutations: substitution (silent / missense / nonsense), insertion, deletion.',
            'Arabidopsis thaliana mutation rate: ~7 × 10⁻⁹ per site per generation.',
            'Human germ-line mutation rate: ~70 new mutations per generation (of ~3 billion bp).',
            'Mutations in multicellular organisms: only germline mutations are heritable; somatic mutations affect only the individual.',
        ],
        warnings=[
            'Most mutations are neutral or slightly deleterious. Strongly beneficial mutations are rare.',
            'Mutation rate is NOT determined by need — it is a stochastic process.',
        ],
        mnemonic='MRS-BE: Mutations are Random, Stochastic, Beneficial-rarely, Essential (no evolution without them).',
        flashcard={
            'front': 'Compare the evolutionary consequences of somatic versus germline mutations.',
            'back': 'SOMATIC mutations occur in non-reproductive cells (skin, liver, etc.). They affect only the individual and die with that individual — they cannot be inherited, so they do not contribute to population-level evolution. GERMLINE mutations occur in cells that give rise to gametes (eggs and sperm). These can be passed to offspring and become the raw material of evolution. Cancer is typically caused by accumulated somatic mutations; evolution is driven by germline mutations.',
        },
        quiz={
            'question': 'A woman develops a BRCA1 mutation in breast tissue during adulthood. This mutation is:',
            'correct': 'Somatic — it will not be inherited by her children',
            'distractors': [
                'Germline — her children will inherit it with 50% probability',
                'Both somatic and germline — all cell mutations are heritable',
                'Not a true mutation because it occurred after birth',
            ],
        },
        visual={
            'type': 'classification',
            'description': 'Mutation types and consequences',
            'regions': [
                {'label': 'Silent', 'color': '#7de2d1', 'items': ['Same amino acid', 'No protein change']},
                {'label': 'Missense', 'color': '#ffc857', 'items': ['Different amino acid', 'May alter protein function']},
                {'label': 'Nonsense', 'color': '#ff6b6b', 'items': ['Premature stop codon', 'Truncated protein']},
                {'label': 'Frameshift', 'color': '#8a5cf6', 'items': ['Insertion/deletion', 'Usually severe']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'SMNF: Silent, Missense, Nonsense, Frameshift — ordered by typical severity.',
            'trap': 'A "silent" mutation is not always silent — some affect mRNA stability, splicing, or codon usage and can have phenotypic effects.',
        },
    ))
    nodes.append(build_node(
        id='lec3-sex-meiosis',
        title='Sex Cells & Meiotic Variation',
        subtitle='How meiosis generates diversity (Lec 3 slides 18-19)',
        color='pink', row=3,
        heading='Lecture 3 — Meiotic Sources of Variation',
        sections=slides_to_sections(d, (18, 19)),
        examples=[
            'Meiotic crossing over (recombination) during prophase I — shuffles alleles between homologs.',
            'Independent assortment of homologs during metaphase I — 2^n possible combinations for n chromosome pairs (2^23 ≈ 8 million in humans).',
            'Random fertilization: any sperm can meet any egg, multiplying variation further.',
        ],
        warnings=[
            'EXAM TRAP: Crossing over occurs during PROPHASE I (when homologs are synapsed), NOT during anaphase. Independent assortment is the metaphase I process.',
            'Meiosis generates variation; mitosis does NOT — mitosis produces genetically identical daughter cells. Only meiosis + fertilization expand the genotypic space.',
        ],
        mnemonic='CIR: Crossing over + Independent assortment + Random fertilization = meiotic variation engine.',
        flashcard={
            'front': 'How many genetically distinct gametes can a single human potentially produce, ignoring new mutations?',
            'back': 'Humans have 23 pairs of chromosomes. Through independent assortment alone, 2²³ ≈ 8.4 million different combinations of homologs are possible. Adding crossing over (recombination) between homologs dramatically increases this number to effectively infinite (~10^1000+ depending on crossover positions). Random fertilization then multiplies this by the same factor in the partner — so each human offspring is effectively genetically unique (identical twins excepted).',
        },
        quiz={
            'question': 'Which meiotic process contributes to genetic variation by shuffling alleles between homologous chromosomes?',
            'correct': 'Crossing over (recombination) during prophase I',
            'distractors': [
                'Independent assortment during metaphase I',
                'Mitotic division of germ cells',
                'Sister chromatid separation during anaphase II',
            ],
        },
        visual={
            'type': 'diagram',
            'description': 'Sources of meiotic variation',
            'regions': [
                {'label': 'Prophase I', 'color': '#4ea8de', 'items': ['Crossing over', 'Chiasmata form']},
                {'label': 'Metaphase I', 'color': '#7de2d1', 'items': ['Independent assortment of homologs', '2^n combinations']},
                {'label': 'Fertilization', 'color': '#ffc857', 'items': ['Random gamete fusion', 'Multiplies variation further']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Three levels of mixing in sex.',
            'trap': 'Mitosis does not generate variation — only meiosis + fertilization do. This is why asexual lineages accumulate mutations linearly while sexual lineages can recombine them.',
        },
    ))
    nodes.append(build_node(
        id='lec3-genotype-phenotype',
        title='Genotype-Phenotype Map: Polygenic Traits & Environment',
        subtitle='How genes + environment shape phenotypes (Lec 3 slides 20-29)',
        color='teal', row=3,
        heading='Lecture 3 — Linking Genotype and Phenotype',
        sections=slides_to_sections(d, (20, 29)),
        examples=[
            'Genetic polymorphism: simultaneous existence of two or more discrete forms in a population (e.g., blood types, color morphs).',
            'Polygenic traits: phenotype determined by many genes (e.g., height, skin color, disease risk) — produces continuous variation.',
            'Environmental effects: same genotype can produce different phenotypes (reaction norms — covered more in Lec 5-6).',
        ],
        warnings=[
            'EXAM TRAP: Continuous variation in a trait does NOT mean the trait is environmentally determined. Human height is ~80% heritable but is continuous because MANY genes contribute (polygenic). Heritability and discrete vs continuous are independent dimensions.',
            'Genetic polymorphism ≠ allele. A polymorphism is a population-level phenomenon (two or more forms coexist). An individual has alleles, not polymorphisms.',
        ],
        mnemonic='PPE: Polymorphism (discrete) vs Polygenic (continuous) vs Environmental (plasticity).',
        flashcard={
            'front': 'What is the difference between a genetic polymorphism and a polygenic trait? Give an example of each.',
            'back': 'A POLYMORPHISM is the presence of two or more DISCRETE phenotypic variants in a population maintained by genetic variation at one or a few loci — e.g., human ABO blood types (3 alleles → 4 phenotypes), Mendelian pea flower color. A POLYGENIC trait is continuous variation controlled by MANY genes each contributing a small amount, usually producing a bell-curve distribution — e.g., human height, skin color, IQ, disease risk (BMI, hypertension). Polygenic traits can also be influenced by environment, producing gene × environment effects.',
        },
        quiz={
            'question': 'Human height is considered a polygenic trait because:',
            'correct': 'It is influenced by many genes each contributing a small amount, producing continuous variation',
            'distractors': [
                'It is controlled by a single dominant/recessive gene pair',
                'It is determined entirely by environment and nutrition',
                'It does not vary within populations',
            ],
        },
        visual={
            'type': 'distribution',
            'description': 'Polymorphism vs polygenic distributions',
            'regions': [
                {'label': 'Polymorphism', 'color': '#ff6b6b', 'items': ['Discrete classes', 'Few alleles', 'e.g., blood type']},
                {'label': 'Polygenic', 'color': '#4ea8de', 'items': ['Continuous bell curve', 'Many loci', 'e.g., height']},
                {'label': 'Plastic', 'color': '#7de2d1', 'items': ['Same genotype, many phenotypes', 'Environment-dependent']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Discrete vs Continuous vs Plastic.',
            'trap': 'Continuous variation does NOT mean purely environmental — many continuous traits are highly heritable.',
        },
    ))
    return nodes


def lec4_nodes():
    d = load_lec('lec4')
    nodes = []
    nodes.append(build_node(
        id='lec4-sources-evolution',
        title='Sources of Evolutionary Change',
        subtitle='The 5 mechanisms that change allele frequencies (Lec 4 slides 1-3)',
        color='amber', row=4,
        heading='Lecture 4 — Sources of Evolutionary Change',
        sections=slides_to_sections(d, (1, 3)),
        examples=[
            'Five evolutionary forces: mutation, genetic drift, gene flow, natural selection, non-random mating.',
            'In a Hardy-Weinberg "null" population, all five forces are absent and allele frequencies do not change.',
        ],
        warnings=[
            'EXAM TRAP: Non-random mating (inbreeding, assortative mating) changes GENOTYPE frequencies but does NOT directly change ALLELE frequencies — so it violates HWE but does not cause allele frequency evolution by itself.',
            'Only MUTATION creates NEW genetic variation. Drift, gene flow, selection, and non-random mating only redistribute existing variation.',
        ],
        mnemonic='MUD-GAS: Mutation, Unequal (drift), Drift, Gene flow, Assortative mating, Selection.',
        flashcard={
            'front': 'Name the five evolutionary forces that can change allele frequencies in a population, and briefly describe each.',
            'back': '(1) MUTATION — new alleles appear via DNA replication errors. (2) GENETIC DRIFT — random sampling causes allele frequencies to fluctuate between generations (stronger in small populations). (3) GENE FLOW (migration) — alleles move between populations when individuals immigrate/emigrate. (4) NATURAL SELECTION — differential reproductive success based on heritable traits. (5) NON-RANDOM MATING (assortative or inbreeding) — affects genotype frequencies (but technically not allele frequencies). All five disrupt Hardy-Weinberg equilibrium.',
        },
        quiz={
            'question': 'A population that satisfies Hardy-Weinberg assumptions will:',
            'correct': 'Have allele frequencies that do not change from generation to generation',
            'distractors': [
                'Evolve rapidly due to random mutation',
                'Lose all genetic variation within a few generations',
                'Exhibit directional natural selection',
            ],
        },
        visual={
            'type': 'summary',
            'description': 'The five forces of evolution',
            'regions': [
                {'label': 'Forces', 'color': '#ffc857', 'items': ['Mutation', 'Drift', 'Gene flow', 'Selection', 'Non-random mating']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Five forces disrupt H-W equilibrium.',
            'trap': 'Only mutation creates NEW variation. The others sort and redistribute existing variation.',
        },
    ))
    nodes.append(build_node(
        id='lec4-hardy-weinberg',
        title='Hardy-Weinberg Theorem',
        subtitle='The null model of population genetics (Lec 4 slides 4-12)',
        color='blue', row=4,
        heading='Lecture 4 — Hardy-Weinberg Principle',
        sections=slides_to_sections(d, (4, 12)),
        examples=[
            'Hardy-Weinberg equations: p + q = 1, p² + 2pq + q² = 1.',
            'Five assumptions: (1) no mutation, (2) no selection, (3) no migration, (4) random mating, (5) infinite population (no drift).',
            'Example: ADH locus in fruit flies — allele frequencies calculated from electrophoresis phenotypes.',
            'If observed genotype frequencies match p² + 2pq + q² predictions, the population is in HWE for that locus.',
        ],
        warnings=[
            'HWE is a NULL hypothesis — we test whether a population is in equilibrium to detect evolutionary forces.',
            'A population can be in HWE for one locus and not others.',
        ],
        mnemonic='p² + 2pq + q² = 1. If observed ≠ expected → something is causing evolution.',
        flashcard={
            'front': 'State the five assumptions of the Hardy-Weinberg principle and explain what happens if each one is violated.',
            'back': '(1) NO MUTATION — if violated, new alleles enter the population and allele frequencies drift. (2) NO NATURAL SELECTION — if violated, fitness differences skew genotype frequencies. (3) NO MIGRATION (GENE FLOW) — if violated, alleles move in/out and frequencies change. (4) RANDOM MATING — if violated (e.g., assortative mating or inbreeding), genotype frequencies deviate from p² + 2pq + q² even without allele frequency change. (5) INFINITE POPULATION SIZE — if violated, genetic drift randomly changes allele frequencies (stronger in smaller populations). HWE gives us a NULL model: if observed genotype frequencies deviate from the predictions, one of these five assumptions is being violated.',
        },
        quiz={
            'question': 'In a population with alleles A and a at frequencies p = 0.6 and q = 0.4, what is the expected frequency of heterozygotes under Hardy-Weinberg equilibrium?',
            'correct': '0.48 (2pq = 2 × 0.6 × 0.4)',
            'distractors': [
                '0.36 (p²)',
                '0.16 (q²)',
                '0.50 (always one-half)',
            ],
        },
        visual={
            'type': 'equation',
            'description': 'The Hardy-Weinberg equations',
            'regions': [
                {'label': 'Allele', 'color': '#4ea8de', 'items': ['p + q = 1']},
                {'label': 'Genotype', 'color': '#7de2d1', 'items': ['p² + 2pq + q² = 1']},
                {'label': 'Homozygous dom', 'color': '#ffc857', 'items': ['p² (AA)']},
                {'label': 'Heterozygous', 'color': '#ff6b6b', 'items': ['2pq (Aa)']},
                {'label': 'Homozygous rec', 'color': '#8a5cf6', 'items': ['q² (aa)']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'p² + 2pq + q² = 1 always works when population is at equilibrium.',
            'trap': 'Rare dominant alleles hide rarer recessive alleles. Always calculate q from q² (homozygous recessives), not from a count of dominant phenotypes.',
        },
    ))
    nodes.append(build_node(
        id='lec4-genetic-drift',
        title='Genetic Drift, Bottlenecks & Founder Effects',
        subtitle='Random allele frequency change in finite populations (Lec 4 slides 13-22)',
        color='gray', row=4,
        heading='Lecture 4 — Genetic Drift',
        sections=slides_to_sections(d, (13, 22)),
        examples=[
            'Drift in Drosophila (Buri 1956): small populations fixed or lost bw75 allele randomly within ~19 generations.',
            'Genetic bottleneck: dramatic population reduction causes major allele frequency changes that persist long after recovery (e.g., cheetahs, northern elephant seals).',
            'Founder effect: a few individuals colonize a new area and carry a non-random sample of the source allele pool (e.g., Amish populations, Polynesian colonization).',
        ],
        warnings=[
            'Drift is NOT directional — it is random. But its effects are STRONGEST in small populations.',
            'Bottleneck effects persist for many generations even after population recovers, because lost alleles are gone permanently.',
        ],
        mnemonic='BFS: Bottleneck, Founder effect, Small population = strong drift.',
        flashcard={
            'front': 'Explain how the founder effect differs from a genetic bottleneck, and give an example of each.',
            'back': 'A GENETIC BOTTLENECK occurs when an existing population is dramatically reduced in size (disease, disaster, overhunting), eliminating many alleles by chance. The survivors rebuild the population from a non-representative sample — example: cheetahs (~10,000 years ago bottleneck reduced genetic diversity to near-clonal levels; northern elephant seals reduced to ~20 individuals in the 1890s). A FOUNDER EFFECT occurs when a small number of individuals colonize a new habitat, bringing only a subset of the source population\'s alleles. The new population is genetically distinct from the source not by selection but by sampling chance — example: Amish populations in Pennsylvania show elevated frequencies of recessive disorders (e.g., polydactyly) because founders happened to carry those alleles. Both reduce genetic diversity through drift.',
        },
        quiz={
            'question': 'Genetic drift has the strongest effect on allele frequency change in which type of population?',
            'correct': 'Small populations',
            'distractors': [
                'Large populations with equal sex ratios',
                'Populations at Hardy-Weinberg equilibrium',
                'Populations with high gene flow',
            ],
        },
        visual={
            'type': 'comparison',
            'description': 'Bottleneck vs founder effect',
            'regions': [
                {'label': 'Bottleneck', 'color': '#ff6b6b', 'items': ['Pop crashes', 'Alleles lost', 'Recovery retains low diversity']},
                {'label': 'Founder', 'color': '#4ea8de', 'items': ['Few colonizers', 'Carry only a sample', 'New pop drifts from source']},
                {'label': 'Both', 'color': '#ffc857', 'items': ['Reduced diversity', 'Random, not directional', 'Effect stronger in small N']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Crash vs Colonize.',
            'trap': 'Drift can fix DELETERIOUS alleles if the population is small enough — selection is too weak to remove them.',
        },
    ))
    nodes.append(build_node(
        id='lec4-selection-mechanism',
        title='Natural Selection as Mechanism',
        subtitle='Selection coefficients, allele interactions, response to selection (Lec 4 slides 23-31)',
        color='green', row=4,
        heading='Lecture 4 — Natural Selection as a Mechanism of Evolution',
        sections=slides_to_sections(d, (23, 31)),
        examples=[
            'Selection coefficient (s): the fitness reduction of a genotype relative to the best. Relative fitness w = 1-s.',
            'Dominant, recessive, and additive allele interactions produce different rates of allele frequency change under selection.',
            'Most complex traits are influenced by many loci — selection on one trait changes allele frequencies at many loci simultaneously.',
        ],
        warnings=[
            'EXAM TRAP: Selection against a RECESSIVE deleterious allele becomes progressively LESS EFFICIENT as the allele gets rarer — it hides more and more in heterozygotes. You CANNOT fully eliminate a recessive allele by selection alone.',
            'Relative fitness is always scaled to the BEST genotype (w = 1). A selection coefficient of s = 0.1 means that genotype leaves 10% fewer offspring than the most fit genotype — it is NOT eliminated, just disadvantaged.',
        ],
        mnemonic='SCAR: Selection Coefficient = 1 - (fitness / best fitness). Relative fitness drives allele frequency change.',
        flashcard={
            'front': 'How do the rates of allele frequency change differ when selection acts on a dominant versus a recessive allele?',
            'back': 'When selection FAVORS a DOMINANT allele, it rises in frequency rapidly at first because even heterozygotes express the trait — but fixing the last copies of the recessive allele is slow because rare recessives hide in heterozygotes (2pq is hard to eliminate). When selection FAVORS a RECESSIVE allele, it rises SLOWLY at first because only q² homozygotes are exposed to selection — but once it becomes common, it increases rapidly. SELECTING AGAINST a recessive deleterious allele is also inefficient: as q decreases, more and more of the remaining allele hides in heterozygotes, making it nearly impossible to fully eliminate.',
        },
        quiz={
            'question': 'A recessive lethal allele is under strong negative selection. Why does it persist at low frequencies rather than being eliminated entirely?',
            'correct': 'Heterozygotes are not exposed to selection, so rare alleles hide in 2pq',
            'distractors': [
                'New copies are constantly replenished by back-mutation from the dominant allele at the same rate selection removes them',
                'Balancing selection maintains both alleles because heterozygotes have higher fitness than either homozygote',
                'Genetic drift counteracts selection in large populations, preventing fixation of the favorable dominant allele',
            ],
        },
        visual={
            'type': 'curve',
            'description': 'Allele frequency change under selection',
            'regions': [
                {'label': 'Dominant favored', 'color': '#4ea8de', 'items': ['Fast rise at low freq', 'Slow fixation at high freq']},
                {'label': 'Recessive favored', 'color': '#7de2d1', 'items': ['Slow rise at low freq', 'Fast rise at high freq']},
                {'label': 'Additive', 'color': '#ffc857', 'items': ['Constant selection', 'Most predictable']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Dominance hides rare alleles from selection.',
            'trap': 'You cannot eliminate a deleterious recessive allele completely by selection alone — it always hides in heterozygotes at low frequencies.',
        },
    ))
    return nodes


def lec5_6_nodes():
    d = load_lec('lec5_6')
    nodes = []
    nodes.append(build_node(
        id='lec56-quant-intro',
        title='Qualitative vs Quantitative Traits',
        subtitle='Mendelian vs continuous inheritance (Lec 5-6 slides 1-13)',
        color='teal', row=5,
        heading='Lecture 5-6 — Introduction to Quantitative Genetics',
        sections=slides_to_sections(d, (1, 13)),
        examples=[
            'Qualitative: discrete categories (flower color, presence/absence) — often Mendelian, 1 or 2 loci.',
            'Quantitative: continuous variation (height, weight, yield) — many loci each contributing a small effect.',
            'Phenotypic variance: V_P = V_G + V_E + V_GxE (+ covariance terms). Genetic variance (V_G) includes additive, dominance, and epistatic components.',
        ],
        warnings=[
            'EXAM TRAP: V_G includes THREE components — additive (V_A), dominance (V_D), and epistatic (V_I). ONLY V_A (additive genetic variance) responds to selection. The breeders equation uses h² = V_A/V_P, not V_G/V_P.',
            'V_P = V_G + V_E only when G and E are uncorrelated and non-interacting. In natural populations, there are often gene-environment CORRELATIONS (e.g., tall parents provide better nutrition) that inflate or deflate the apparent genetic component.',
        ],
        mnemonic='VP = VG + VE: Phenotypic variance = Genetic + Environmental. Add interaction term V_GxE if relevant.',
        flashcard={
            'front': 'Why do quantitative (polygenic) traits show a continuous bell-curve distribution?',
            'back': 'Quantitative traits are controlled by MANY genes, each with a small additive effect. When many independent small contributions are added (multi-locus segregation), the central limit theorem produces a continuous, approximately normal distribution. Environmental variation adds further to the continuous spread. This contrasts with Mendelian traits controlled by 1-2 loci, which produce discrete categories.',
        },
        quiz={
            'question': 'The equation V_P = V_G + V_E describes:',
            'correct': 'Decomposition of phenotypic variance into genetic and environmental components',
            'distractors': [
                'Total mutation rate in a population',
                'The fitness of each genotype',
                'The rate of genetic drift in small populations',
            ],
        },
        visual={
            'type': 'decomposition',
            'description': 'Variance decomposition',
            'regions': [
                {'label': 'VP', 'color': '#4ea8de', 'items': ['Total phenotypic variance']},
                {'label': 'VG', 'color': '#7de2d1', 'items': ['Genetic: VA + VD + VI']},
                {'label': 'VE', 'color': '#ffc857', 'items': ['Environmental variance']},
                {'label': 'VGxE', 'color': '#ff6b6b', 'items': ['Gene × environment interaction']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Separate genes, environment, and their interaction.',
            'trap': 'VA (additive genetic variance) is the component that RESPONDS to selection. Dominance and epistatic variance do not transmit as predictably across generations.',
        },
    ))
    nodes.append(build_node(
        id='lec56-heritability-breeders',
        title='Heritability & Breeders Equation',
        subtitle='R = h² × S — predicting evolutionary response (Lec 5-6 slides 14-30)',
        color='blue', row=5,
        heading='Lecture 5-6 — Heritability and Response to Selection',
        sections=slides_to_sections(d, (14, 30)),
        examples=[
            'Broad-sense heritability (H²) = VG / VP.',
            'Narrow-sense heritability (h²) = VA / VP — the proportion of phenotypic variance due to ADDITIVE genetic effects.',
            'Breeders equation: R = h² × S, where R = response to selection, S = selection differential.',
            'Parent-offspring regression: slope estimates h² directly.',
            'Stabilizing selection (human birth weight), disruptive selection (oil content of corn), directional selection (beak size).',
        ],
        warnings=[
            'High h² does NOT mean the trait is "genetic" in common speech — it means phenotypic variance IN THAT POPULATION IN THAT ENVIRONMENT is mostly due to additive genetic variance.',
            'Heritability is population- and environment-specific.',
        ],
        mnemonic='R = h² × S. Big h² + big S → big response. Any zero → no response.',
        flashcard={
            'front': 'State the breeders equation, define each term, and explain what determines the response to selection.',
            'back': 'BREEDERS EQUATION: R = h² × S. R = RESPONSE to selection (change in mean phenotype from parent generation to offspring generation). h² = NARROW-SENSE HERITABILITY = V_A / V_P (proportion of phenotypic variance due to additive genetic variance). S = SELECTION DIFFERENTIAL = mean phenotype of breeding individuals minus mean of whole population. The response depends on BOTH h² (how much heritable variation there is) AND S (how strong selection is). If h² is zero, NO response even with strong selection. If S is zero (no selection), NO response even with high h².',
        },
        quiz={
            'question': 'In a population with h² = 0.5 for body size, a selection differential of S = 10 g is imposed. What is the predicted response R in offspring?',
            'correct': '5 g (R = 0.5 × 10)',
            'distractors': [
                '10 g (no heritability correction)',
                '0.5 g (only additive variance matters)',
                '20 g (R = 2 × h² × S)',
            ],
        },
        visual={
            'type': 'equation',
            'description': 'Breeders equation components',
            'regions': [
                {'label': 'R', 'color': '#4ea8de', 'items': ['Response to selection', 'Change in mean next gen']},
                {'label': 'h²', 'color': '#7de2d1', 'items': ['Narrow-sense heritability', 'V_A / V_P']},
                {'label': 'S', 'color': '#ffc857', 'items': ['Selection differential', 'Mean parents - mean pop']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'R = h² × S. Multiplicative — any zero = no response.',
            'trap': 'h² is specific to a population and environment. Changing the environment changes V_E and therefore h².',
        },
    ))
    nodes.append(build_node(
        id='lec56-reaction-norms',
        title='Phenotypic Plasticity & Reaction Norms',
        subtitle='When same genotype gives different phenotypes (Lec 5-6 slides 31-45)',
        color='green', row=5,
        heading='Lecture 5-6 — Phenotypic Plasticity',
        sections=slides_to_sections(d, (31, 45)),
        examples=[
            'Reaction norm: a plot showing the phenotype of one genotype across an environmental gradient.',
            'Plasticity types: continuous (reaction norm) vs discrete (polyphenism — e.g., seasonal coat color, caste in social insects).',
            'G × E interaction: different genotypes have different reaction-norm shapes. Detect by common-garden experiments.',
            'Common garden: grow multiple genotypes in the same environment to separate genetic from environmental effects.',
        ],
        warnings=[
            'EXAM TRAP: Phenotypic plasticity is NOT the same as evolution. A single individual showing different phenotypes in different environments is plasticity — not a change in allele frequency. Plasticity can evolve (the REACTION NORM shape is heritable), but the individual\'s plastic response is not evolution.',
            'G × E interaction means the BEST GENOTYPE CHANGES WITH ENVIRONMENT. If reaction norms cross, there is no single "best" genotype across all environments — this is why adaptation is always environment-specific.',
        ],
        mnemonic='Plastic vs Genetic: Common garden test answers "is the difference genetic or environmental?"',
        flashcard={
            'front': 'What is a reaction norm, and how does a common garden experiment distinguish genetic from environmental contributions to phenotype?',
            'back': 'A REACTION NORM is the relationship between a genotype\'s phenotype and an environmental variable — plotted as a line showing how the same genotype expresses different phenotypes in different environments. A COMMON GARDEN experiment grows multiple genotypes (populations, sibships, clones) in a SHARED environment, removing environmental differences as an explanation. Any remaining phenotypic differences must be GENETIC. A reciprocal transplant (growing each genotype in multiple environments) can reveal G × E interactions — genotypes may differ in HOW they respond to environment, not just their mean.',
        },
        quiz={
            'question': 'Two plant populations from high and low elevations are grown together in a single common garden at sea level. The populations still differ in growth rate. What does this show?',
            'correct': 'The difference is at least partly genetic — environment alone cannot explain it',
            'distractors': [
                'The difference must be entirely environmental',
                'The two populations are the same species',
                'Plasticity is absent in these populations',
            ],
        },
        visual={
            'type': 'reaction-norm',
            'description': 'Reaction norms across environments',
            'regions': [
                {'label': 'Flat RN', 'color': '#4ea8de', 'items': ['No plasticity', 'Constant phenotype across envs']},
                {'label': 'Sloped RN', 'color': '#7de2d1', 'items': ['Linear plasticity', 'Phenotype tracks env']},
                {'label': 'Crossing RNs', 'color': '#ff6b6b', 'items': ['G × E interaction', 'Best genotype varies by env']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Crossing lines = G × E.',
            'trap': 'Plasticity itself is a heritable trait — selection can shape reaction norms. But plasticity ≠ adaptation.',
        },
    ))
    return nodes


def lec7_nodes():
    d = load_lec('lec7')
    nodes = []
    nodes.append(build_node(
        id='lec7-review-empirical',
        title='Empirical Natural Selection: Overview',
        subtitle='Case-study methodology for measuring selection in the wild (Lec 7 slides 1-6)',
        color='amber', row=6,
        heading='Lecture 7 — Empirical Studies of Natural Selection',
        sections=slides_to_sections(d, (1, 6)),
        warnings=[
            'EXAM TRAP: A phenotype-fitness CORRELATION is NOT sufficient proof of natural selection. The correlation could be driven by an environmental confound (e.g., better-fed animals are bigger AND survive longer — but diet, not size, drives survival). You need experimental manipulation or heritability data.',
            'Observing that a trait CHANGED across generations (R > 0) is NOT sufficient either — you must confirm h² > 0 for that trait and show S ≠ 0.',
        ],
        mnemonic='MOD: Measure → Observe differential success → Document inheritance.',
        flashcard={
            'front': 'Why are empirical studies of natural selection in wild populations so difficult, and what three kinds of evidence must be gathered to prove selection is occurring?',
            'back': 'Field selection studies are difficult because: (1) populations are large and individuals must be marked and tracked; (2) the environmental variable causing selection must be identified and often experimentally manipulated; (3) heritability of the trait must be shown separately. To prove selection, you must show: (1) phenotypic VARIATION in the trait, (2) differential FITNESS (survival or reproduction) correlated with the trait, (3) HERITABILITY of the trait. Only then can you predict an evolutionary response (R = h² × S).',
        },
        quiz={
            'question': 'Which of these alone is NOT sufficient evidence that natural selection is occurring on a trait?',
            'correct': 'Observing phenotypic variation in the population',
            'distractors': [
                'Heritable differences in fitness correlated with the trait',
                'Measured change in mean phenotype across generations matching breeders equation',
                'Experimental manipulation of the trait causing altered fitness',
            ],
        },
        visual={
            'type': 'checklist',
            'description': 'Proving natural selection in the field',
            'regions': [
                {'label': 'Required evidence', 'color': '#ffc857', 'items': ['Variation', 'Differential fitness', 'Heritability', 'Prediction matches']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'VFHP: Variation, Fitness, Heritability, Prediction.',
            'trap': 'Showing a phenotype-fitness correlation alone is NOT proof of selection — the correlation could be due to confounded environmental effects.',
        },
    ))
    nodes.append(build_node(
        id='lec7-beach-mice',
        title='Beach Mice: Parallel Evolution of Camouflage',
        subtitle='Peromyscus polionotus — two independent origins of light coat color (Lec 7 slides 7-10)',
        color='coral', row=6,
        heading='Lecture 7 — Beach Mice Case Study',
        sections=slides_to_sections(d, (7, 10)),
        examples=[
            'Dark mainland Peromyscus polionotus populations gave rise to two independent light-colored beach populations.',
            'Beach populations match the light sand habitat (cryptic coloration).',
            'Hoekstra et al.: a single amino acid change in the Mc1r gene causes the light coat color.',
            'The Mc1r mutation is different in each beach population — so camouflage evolved TWICE independently from the same starting genetic variation (parallel evolution at the gene level).',
        ],
        warnings=[
            'EXAM TRAP: "Parallel evolution" is NOT the same as "convergent evolution." Parallel evolution involves the SAME gene (Mc1r) in closely related populations. Convergent evolution involves different genes or lineages arriving at similar phenotypes independently.',
            'Mc1r is only one of several genes contributing to coat color in Peromyscus. The beach mouse studies showed MOST (not all) of the light-coat phenotype maps to Mc1r, but other loci also contribute.',
        ],
        mnemonic='MMMP: Mc1r mutation → Melanin loss → Match sand → Predation protection.',
        flashcard={
            'front': 'How does the beach mouse study illustrate the interaction between genetics, phenotype, environment, and selection?',
            'back': 'MAINLAND Peromyscus polionotus have dark fur, matching forest soil. Two BEACH populations (Atlantic and Gulf coasts) have light fur, matching white sand. GENETICS: Hoekstra and colleagues identified a single amino acid change in the Mc1r gene causes the light color in both populations — but the exact mutation differs between the two beach populations. PHENOTYPE: Light fur is cryptic on sand. ENVIRONMENT: Visual predators (birds, mammals) hunt by sight. SELECTION: Predators preferentially eat mice that contrast with the substrate. Barrett & Hoekstra showed this experimentally using plasticine mouse models placed on light and dark substrates — the mismatched models were attacked at higher rates. This case study proves all four ingredients of natural selection in a single system AND shows parallel evolution.',
        },
        quiz={
            'question': 'Beach mice on the Atlantic and Gulf coasts have similar light coat colors but different Mc1r mutations. This is an example of:',
            'correct': 'Parallel evolution — same phenotypic outcome from independent genetic changes',
            'distractors': [
                'Convergent evolution between different species',
                'Genetic drift eliminating variation',
                'Hybridization between populations',
            ],
        },
        visual={
            'type': 'comparison',
            'description': 'Beach mouse parallel evolution',
            'regions': [
                {'label': 'Mainland ancestor', 'color': '#6e6a80', 'items': ['Dark fur', 'Forest habitat']},
                {'label': 'Atlantic beach pop', 'color': '#ffc857', 'items': ['Light fur', 'Mc1r mutation A']},
                {'label': 'Gulf beach pop', 'color': '#7de2d1', 'items': ['Light fur', 'Mc1r mutation B']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two beaches, two mutations, one solution.',
            'trap': 'Parallel ≠ convergent. Parallel evolution = same gene in related lineages. Convergent = different genes or lineages arriving at similar phenotypes.',
        },
    ))
    nodes.append(build_node(
        id='lec7-tsd',
        title='Temperature-Dependent Sex Determination',
        subtitle='Plasticity as an evolved trait (Lec 7 slides 11-22)',
        color='red', row=6,
        heading='Lecture 7 — Temperature-Dependent Sex Determination (TSD)',
        sections=slides_to_sections(d, (11, 22)),
        examples=[
            'In many reptiles (turtles, crocodilians), egg incubation temperature determines offspring sex.',
            'Different species have different temperature-sex curves — some favor females at high temps, others at low temps.',
            'Charnov-Bull model: TSD is adaptive when a temperature affects male and female fitness differently.',
            'Climate change concern: rising temperatures can skew sex ratios, threatening TSD species.',
        ],
        warnings=[
            'TSD is a derived trait, not an ancestral one — it evolved multiple times independently.',
        ],
        mnemonic='Charnov-Bull: TSD is adaptive when temperature ≠ sex × fitness interaction differs.',
        flashcard={
            'front': 'Under what conditions is temperature-dependent sex determination (TSD) expected to be adaptive, according to the Charnov-Bull model?',
            'back': 'The CHARNOV-BULL model predicts TSD is adaptive when the environment (temperature) experienced during development differentially affects the fitness of males versus females. If a certain temperature makes males successful but females unsuccessful (or vice versa), producing the sex that benefits more at that temperature maximizes parental fitness. For example, if warmer nest temperatures produce larger offspring and female reproductive success depends on body size more than male success, then warm-temperature eggs should develop as females. Climate change can make TSD maladaptive if temperatures exceed the historical range.',
        },
        quiz={
            'question': 'Which of the following is the greatest conservation threat posed by temperature-dependent sex determination in sea turtles?',
            'correct': 'Rising global temperatures may skew sex ratios so strongly that breeding populations cannot be sustained',
            'distractors': [
                'Genetic drift will eliminate TSD',
                'Predators will preferentially eat one sex',
                'Sea turtles will lose the TSD gene entirely',
            ],
        },
        visual={
            'type': 'curve',
            'description': 'TSD curves by species type',
            'regions': [
                {'label': 'Type Ia', 'color': '#4ea8de', 'items': ['Low T → males', 'High T → females', 'e.g., many turtles']},
                {'label': 'Type Ib', 'color': '#ffc857', 'items': ['Low T → females', 'High T → males', 'e.g., some lizards']},
                {'label': 'Type II', 'color': '#ff6b6b', 'items': ['Males at extreme temps', 'Females in middle', 'e.g., crocodiles']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Three temperature-sex curve shapes across reptiles.',
            'trap': 'TSD is NOT a primitive trait — it evolved multiple times and can be lost again. Genetic sex determination is ancestral in most vertebrates.',
        },
    ))
    nodes.append(build_node(
        id='lec7-fitness-landscape',
        title='Fitness Landscapes',
        subtitle='Wright\'s metaphor for evolutionary dynamics (Lec 7 slides 23-26)',
        color='purple', row=6,
        heading='Lecture 7 — Fitness Landscape',
        sections=slides_to_sections(d, (23, 26)),
        examples=[
            'Sewall Wright (1932): fitness landscape — a metaphorical surface where x,y axes are genotypes/traits and z (height) is fitness.',
            'Adaptive peaks: high-fitness genotype combinations.',
            'Valleys: low-fitness genotype combinations between peaks.',
            'Populations tend to climb local peaks via natural selection, but may get stuck on suboptimal peaks (can\'t cross valleys).',
            'Drift or gene flow can help populations cross valleys and reach higher peaks.',
        ],
        warnings=[
            'EXAM TRAP: The fitness landscape metaphor is a SIMPLIFICATION. Real genotype space is >10,000-dimensional — there is no simple 2D landscape. Two-dimensional diagrams are teaching tools, not reality.',
            'Fitness landscapes CHANGE over time when environments change. A local peak in one environment may be a valley in another — environmental change can "shift the landscape" and re-start the climbing process.',
        ],
        mnemonic='Peaks & Valleys: Selection → local peak; Drift/flow → cross valley to higher peak.',
        flashcard={
            'front': 'What is a fitness landscape and why can selection alone get "stuck" on a local peak?',
            'back': 'A FITNESS LANDSCAPE (Wright 1932) is a metaphorical surface where axes represent allele combinations (or trait values) and the height at each point is the fitness of that combination. Populations evolve by "climbing" up the landscape — selection pushes them toward higher fitness. However, natural selection only moves a population LOCALLY UPHILL. If a population reaches a LOCAL PEAK, any small change reduces fitness — selection prevents the population from leaving. To reach a HIGHER peak across a valley, the population must temporarily pass through lower-fitness states, which selection opposes. GENETIC DRIFT or GENE FLOW can help populations cross valleys by randomly moving them off the current peak — a classic example of how drift and flow can actually accelerate adaptation under some conditions.',
        },
        quiz={
            'question': 'A population is stuck on a local fitness peak while a much higher peak exists across a fitness valley. Which process is most likely to help the population move to the higher peak?',
            'correct': 'Genetic drift temporarily pushing the population off the local peak',
            'distractors': [
                'Stronger stabilizing selection',
                'Elimination of all mutations',
                'Reduced population size to zero',
            ],
        },
        visual={
            'type': 'landscape',
            'description': 'Wright\'s fitness landscape',
            'regions': [
                {'label': 'Local peak', 'color': '#ffc857', 'items': ['Selection traps here']},
                {'label': 'Global peak', 'color': '#7de2d1', 'items': ['Highest fitness combination']},
                {'label': 'Valley', 'color': '#ff6b6b', 'items': ['Low fitness', 'Selection opposes crossing']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Selection is blind to height beyond its immediate neighborhood.',
            'trap': 'Real fitness landscapes are high-dimensional (thousands of genes). 2D visualizations are radical simplifications.',
        },
    ))
    return nodes
