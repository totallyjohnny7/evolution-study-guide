"""Node generators for Lectures 8-13 (Exam 2 coverage)."""
from helpers import load_lec, slides_to_sections, build_node


def lec8_nodes():
    d = load_lec('lec8')
    nodes = []
    nodes.append(build_node(
        id='lec8-adaptations-intro',
        title='Adaptations: Trait vs Process',
        subtitle='Defining adaptation and novel traits (Lec 8 slides 1-6)',
        color='amber', row=7,
        heading='Lecture 8 — Complex Adaptations',
        sections=slides_to_sections(d, (1, 6)),
        examples=[
            'Adaptation as TRAIT: a heritable feature that increases fitness in a particular environment.',
            'Adaptation as PROCESS: the ongoing evolutionary change driven by natural selection.',
            'Novel traits: arise de novo (not inherited) — e.g., limbs in tetrapods, wings in birds.',
            'Complex traits: require coordination of multiple genes and developmental modules.',
        ],
        mnemonic='Trait vs Process: the word "adaptation" carries both meanings — always specify which.',
        flashcard={
            'front': 'What is the difference between "adaptation" as a trait and "adaptation" as a process?',
            'back': 'As a TRAIT (noun): an adaptation is a specific heritable feature shaped by past selection that increases fitness — e.g., the woodpecker\'s long tongue, the giraffe\'s neck, antifreeze proteins in Antarctic fish. As a PROCESS (verb): adaptation is the ongoing evolutionary mechanism by which populations become better matched to their environment through natural selection. These two meanings are related but distinct: the process produces the traits. In scientific papers, careful writers specify which they mean.',
        },
        quiz={
            'question': 'Which statement best describes a "novel trait" in evolution?',
            'correct': 'A trait that arises de novo and is not directly inherited from an ancestor',
            'distractors': [
                'Any new mutation that appears in a population',
                'A trait that never existed before life began',
                'A trait unique to a single individual',
            ],
        },
        visual={
            'type': 'distinction',
            'description': 'Adaptation as noun vs verb',
            'regions': [
                {'label': 'Trait (noun)', 'color': '#ffc857', 'items': ['Heritable feature', 'Shaped by past selection', 'Increases fitness']},
                {'label': 'Process (verb)', 'color': '#4ea8de', 'items': ['Ongoing change', 'Population-level', 'Driven by selection']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Trait = what. Process = how.',
            'trap': 'Not every trait is an adaptation. Some are byproducts of other adaptations, some are vestigial, some are selectively neutral.',
        },
    ))
    nodes.append(build_node(
        id='lec8-evo-devo',
        title='Evo-Devo & Regulatory Networks',
        subtitle='How gene networks build body plans (Lec 8 slides 7-22)',
        color='teal', row=7,
        heading='Lecture 8 — Evolutionary Developmental Biology',
        sections=slides_to_sections(d, (7, 22)),
        examples=[
            'Evo-devo: the study of how developmental processes evolve and how gene regulation shapes morphology.',
            'Hox genes: conserved master regulators of body plan across animals. Small changes in Hox expression → large morphological changes.',
            'Limb development: same gene network (Hox, Tbx, Sonic hedgehog) is used by all tetrapods to build limbs.',
            'Galapagos finches: beak size differences are controlled by Bmp4 and calmodulin expression differences, not new genes.',
        ],
        mnemonic='Small regulatory changes → Big morphological differences. Same toolkit, different deployment.',
        flashcard={
            'front': 'Why do evolutionary biologists emphasize regulatory evolution over protein-coding evolution for explaining body plan differences?',
            'back': 'Most animals share the SAME toolkit of developmental genes — Hox, Pax, Tbx, BMP, Wnt, Sonic hedgehog. These genes are nearly identical in fruit flies, mice, and humans. Major morphological differences (legs vs. no legs, big beak vs. small beak, limbs vs. fins) arise mostly from CHANGES IN WHEN, WHERE, AND HOW MUCH these genes are expressed — not from new protein-coding genes. A single mutation in a cis-regulatory element can shift the domain of expression, producing large phenotypic effects. This is why "small changes in networks lead to new complex traits."',
        },
        quiz={
            'question': 'The striking morphological differences in beak size among Galápagos finches are produced primarily by:',
            'correct': 'Differences in the expression levels of regulatory genes like Bmp4 and calmodulin during beak development',
            'distractors': [
                'Completely different sets of genes in each species',
                'New proteins that evolved only in finches',
                'Environmental sculpting of beak bone after hatching',
            ],
        },
        visual={
            'type': 'network',
            'description': 'Regulatory network producing diversity',
            'regions': [
                {'label': 'Shared toolkit', 'color': '#4ea8de', 'items': ['Hox genes', 'BMP, Wnt, SHH', 'Pax, Tbx']},
                {'label': 'Regulatory changes', 'color': '#7de2d1', 'items': ['Cis-regulatory elements', 'Enhancer mutations', 'Expression timing/level']},
                {'label': 'Output', 'color': '#ffc857', 'items': ['Novel body plans', 'Species-specific traits']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Same genes, different expression = different species.',
            'trap': 'Coding sequence changes matter too (e.g., Mc1r in beach mice) but regulatory changes dominate for large morphological differences.',
        },
    ))
    nodes.append(build_node(
        id='lec8-eye-evolution',
        title='Eye Evolution: From Photoreceptors to Camera Eyes',
        subtitle='Classic complex trait case study (Lec 8 slides 23-30)',
        color='blue', row=7,
        heading='Lecture 8 — Evolution of the Eye',
        sections=slides_to_sections(d, (23, 30)),
        examples=[
            'Photoreceptive cells were the earliest step — a single opsin molecule in a light-sensitive cell.',
            'Opsin gene was duplicated twice early in animal evolution, creating different light-sensitivity classes.',
            'Crystallins: transparent proteins that make up the lens — many are recruited from pre-existing enzymes (e.g., lactate dehydrogenase in some species).',
            'Eye stages: simple photoreceptor patch → pit → pinhole → lensed camera eye.',
            'Mollusks alone show ALL intermediate eye stages today — flat eyespots (limpets), pit eyes (abalone), pinhole eyes (Nautilus), lensed eyes (squid, octopus).',
        ],
        mnemonic='From patch to camera: each stage provides its own fitness advantage. No "half eye" problem.',
        flashcard={
            'front': 'How does eye evolution refute the creationist claim of "irreducible complexity" for complex organs?',
            'back': 'The argument from irreducible complexity claims complex organs like the eye cannot evolve because "half an eye" is useless. However, eye evolution shows INTERMEDIATE stages are each FUNCTIONAL and BENEFICIAL: (1) A photoreceptive patch detects light vs. dark (useful for circadian rhythm or shadow warning). (2) A cupped patch gives directional information. (3) A deepened cup becomes a pinhole, giving crude image formation. (4) A lens sharpens the image. All these stages exist TODAY in different mollusks (flatworms, limpets, abalone, Nautilus, squid) — providing living evidence of each intermediate. Crystallins (lens proteins) were recruited from pre-existing enzymes via gene duplication and co-option, not invented from scratch.',
        },
        quiz={
            'question': 'Why is the evolution of the eye often used to refute "irreducible complexity" arguments?',
            'correct': 'Every intermediate stage of eye evolution (patch, pit, pinhole, lensed) is functional and provides fitness benefit',
            'distractors': [
                'The eye evolved in a single mutational step',
                'Only vertebrates have eyes',
                'Eye evolution required miraculous intervention',
            ],
        },
        visual={
            'type': 'stages',
            'description': 'Eye evolution stages',
            'regions': [
                {'label': '1. Patch', 'color': '#6e6a80', 'items': ['Opsin photoreceptors', 'Light/dark only']},
                {'label': '2. Pit', 'color': '#8a5cf6', 'items': ['Directional light', 'Crude vision']},
                {'label': '3. Pinhole', 'color': '#4ea8de', 'items': ['Image formation', 'No lens']},
                {'label': '4. Lensed', 'color': '#7de2d1', 'items': ['Focused image', 'Crystallin lens']},
                {'label': '5. Camera eye', 'color': '#ffc857', 'items': ['Variable focus', 'Iris, cornea']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Patch → Pit → Pinhole → Lens → Camera.',
            'trap': 'Vertebrate and cephalopod camera eyes are CONVERGENT (not homologous as complete organs) — they share the opsin toolkit but arrived at the camera design independently.',
        },
    ))
    nodes.append(build_node(
        id='lec8-flaws-pleiotropy',
        title='Imperfect Adaptations & Antagonistic Pleiotropy',
        subtitle='Why organisms are not optimally designed (Lec 8 slides 31-35)',
        color='red', row=7,
        heading='Lecture 8 — Flaws in Complex Adaptations',
        sections=slides_to_sections(d, (31, 35)),
        examples=[
            'Vertebrate retina: photoreceptors face AWAY from incoming light; blood vessels and optic nerve pass in front of the retina, creating a blind spot. Cephalopod retinas do NOT have this flaw.',
            'Human spine: evolved from a quadruped\'s horizontal backbone — bipedalism causes chronic back pain.',
            'Antagonistic pleiotropy: a gene that increases early reproduction but shortens lifespan (or causes disease later) will be favored because reproduction happens first.',
        ],
        warnings=[
            'Evolution cannot design from scratch — it can only modify what already exists. This "tinkering" produces jury-rigged solutions, not engineered ones.',
        ],
        mnemonic='AP + Tinkering = Flaws. Evolution optimizes locally, not globally.',
        flashcard={
            'front': 'What is antagonistic pleiotropy and how does it explain why aging and age-related diseases persist in human populations?',
            'back': 'ANTAGONISTIC PLEIOTROPY: one gene affects multiple traits (pleiotropy), with OPPOSING (antagonistic) fitness effects — beneficial for one trait but harmful for another. A classic example: a gene allele that INCREASES REPRODUCTIVE SUCCESS in young adulthood but CAUSES DISEASE or death in old age. Because reproduction happens first, the early benefit outweighs the late cost in terms of passing the allele on — so selection FAVORS the allele. This explains why humans suffer age-related diseases (Alzheimer\'s, cancer, heart disease): alleles contributing to these conditions in old age were (and are) maintained because they improved reproductive success earlier in life. This is why "why do organisms age" has a clear evolutionary answer: selection is weak on traits expressed after reproduction.',
        },
        quiz={
            'question': 'The vertebrate retina has a blind spot because photoreceptors face away from incoming light and the optic nerve passes in front. This is best explained as:',
            'correct': 'Evolutionary tinkering — constrained by ancestral developmental pathways, not optimal design',
            'distractors': [
                'Optimal design for human vision',
                'A necessary consequence of using opsins',
                'A sign that vision evolved recently',
            ],
        },
        visual={
            'type': 'concept',
            'description': 'Flaws reveal tinkering',
            'regions': [
                {'label': 'Examples of flaws', 'color': '#ff6b6b', 'items': ['Blind spot (vertebrate retina)', 'Back pain (bipedal spine)', 'Choking (crossed food/air paths)', 'Aging (antagonistic pleiotropy)']},
                {'label': 'Why', 'color': '#ffc857', 'items': ['Constrained by ancestry', 'Selection optimizes locally', 'No global design']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Design ≠ Evolution. Tinkering leaves traces.',
            'trap': 'Flaws DO NOT refute evolution — they support it. They show the jury-rigged nature of descent with modification.',
        },
    ))
    return nodes


def lec9_nodes():
    d = load_lec('lec9')
    nodes = []
    nodes.append(build_node(
        id='lec9-coevolution-intro',
        title='Coevolution: Species as Selective Agents',
        subtitle='When evolution of one species drives evolution of another (Lec 9 slides 1-5)',
        color='purple', row=8,
        heading='Lecture 9 — Coevolution Introduction',
        sections=slides_to_sections(d, (1, 5)),
        examples=[
            'Coevolution: reciprocal evolutionary change in two or more interacting species.',
            'Types of interaction: antagonistic (predator-prey, parasite-host), mutualistic (pollinator-flower), neutral/commensal.',
            'Strong coevolution requires intimate, long-term, specific interaction — generalists coevolve weakly.',
        ],
        mnemonic='Coevolution = Reciprocal change. Both species adapt to each other, not just to environment.',
        flashcard={
            'front': 'What is the difference between coevolution and simple adaptation to another species?',
            'back': 'COEVOLUTION requires RECIPROCAL evolutionary change: species A adapts to species B, AND species B adapts to species A in response. Each species acts as a selective force on the other. SIMPLE ADAPTATION occurs when one species evolves to use another as a resource without that other species evolving in response — e.g., a generalist herbivore that eats many plants doesn\'t significantly affect any single plant\'s evolution. True coevolution is most visible in tightly coupled pairs: predator-prey arms races (newt/snake TTX), mutualisms (fig/fig wasp), parasite-host (Red Queen dynamics). The key test: did the second species evolve specifically in response to the first?',
        },
        quiz={
            'question': 'Which of these best illustrates true coevolution?',
            'correct': 'The garter snake and rough-skinned newt, where newts evolved TTX toxicity and snakes evolved TTX resistance in tight reciprocal fashion',
            'distractors': [
                'A deer eating tree leaves',
                'A bird building a nest in a tree',
                'Humans domesticating dogs over 15,000 years',
            ],
        },
        visual={
            'type': 'interaction',
            'description': 'Types of species interactions',
            'regions': [
                {'label': 'Antagonistic', 'color': '#ff6b6b', 'items': ['Predator/prey', 'Parasite/host', 'Arms race']},
                {'label': 'Mutualistic', 'color': '#7de2d1', 'items': ['Pollinator/flower', 'Gut microbe/host', 'Cleaner fish/client']},
                {'label': 'Commensal', 'color': '#6e6a80', 'items': ['One benefits', 'Other unaffected']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Antagonistic, Mutualistic, Commensal.',
            'trap': 'Not all species interactions are coevolutionary. Coevolution requires RECIPROCAL evolution — both sides respond to each other.',
        },
    ))
    nodes.append(build_node(
        id='lec9-antagonistic-arms',
        title='Antagonistic Coevolution & Arms Races',
        subtitle='Garter snake vs newt + geographic mosaic (Lec 9 slides 6-16)',
        color='red', row=8,
        heading='Lecture 9 — Antagonistic Coevolution',
        sections=slides_to_sections(d, (6, 16)),
        examples=[
            'Rough-skinned newt (Taricha granulosa) produces tetrodotoxin (TTX) — powerful neurotoxin.',
            'Garter snake (Thamnophis sirtalis) evolved TTX-resistant sodium channels, can eat newts without dying.',
            'Both toxicity and resistance have COSTS: TTX-resistant snakes move slower; highly toxic newts are energetically expensive.',
            'Geographic mosaic theory (Thompson): coevolution is locally variable — some populations are coevolutionary "hotspots," others "coldspots."',
        ],
        mnemonic='Arms race: each side escalates + pays costs. Locally variable = mosaic.',
        flashcard={
            'front': 'Describe the garter snake / rough-skinned newt arms race and why it illustrates the costs of coevolutionary escalation.',
            'back': 'Rough-skinned newts (Taricha granulosa) produce TETRODOTOXIN (TTX), one of the most powerful neurotoxins known — it blocks voltage-gated sodium channels, causing paralysis and death in most predators. Garter snakes (Thamnophis sirtalis) in contact with toxic newts have evolved MUTATIONS IN THEIR Na+ CHANNEL GENES that prevent TTX binding — making them resistant. The snakes eat newts, and newts respond by becoming MORE toxic, driving further snake resistance — an escalating arms race. CRUCIALLY, BOTH SIDES PAY COSTS: (1) Resistant snakes have slower movement because their Na+ channels work less efficiently, (2) Highly toxic newts expend energy producing TTX. The geographic mosaic theory (Thompson) explains why coevolution varies by location — some populations are coevolutionary HOTSPOTS with extreme toxicity and resistance, while others are COLDSPOTS with little of either. The snake-newt system is a paradigmatic example of coevolution in action.',
        },
        quiz={
            'question': 'The garter snake/newt arms race demonstrates that coevolutionary escalation:',
            'correct': 'Carries fitness costs on both sides, because the traits that win the arms race come at a price',
            'distractors': [
                'Always produces perfectly adapted species',
                'Only occurs in laboratory conditions',
                'Has no measurable impact on population fitness',
            ],
        },
        visual={
            'type': 'arms-race',
            'description': 'Snake-newt reciprocal evolution',
            'regions': [
                {'label': 'Newt', 'color': '#ff6b6b', 'items': ['TTX toxin', 'More toxic over time', 'Energetic cost']},
                {'label': 'Snake', 'color': '#4ea8de', 'items': ['Na+ channel mutations', 'More resistant over time', 'Slower movement cost']},
                {'label': 'Mosaic', 'color': '#ffc857', 'items': ['Hotspots: high escalation', 'Coldspots: weak escalation', 'Varies by geography']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Poison + Resistance + Costs + Mosaic.',
            'trap': 'Arms races are not infinitely escalating — costs constrain how far escalation can go.',
        },
    ))
    nodes.append(build_node(
        id='lec9-mutualistic',
        title='Mutualistic Coevolution',
        subtitle='Flowers, pollinators, and mutual benefit (Lec 9 slides 17-20)',
        color='pink', row=8,
        heading='Lecture 9 — Mutualistic Coevolution',
        sections=slides_to_sections(d, (17, 20)),
        examples=[
            'Mutualisms: both species benefit from the interaction.',
            'Specialized fly pollinators and matching flowers — e.g., long-tongued flies and long-spurred orchids coevolved.',
            'Darwin\'s prediction: seeing a Madagascar orchid with a 30 cm nectary, Darwin predicted a moth with a matching 30 cm proboscis existed — confirmed 40 years later (Xanthopan morganii praedicta).',
        ],
        mnemonic='Mutual benefit = coevolution with reward not punishment. Each side gets paid.',
        flashcard={
            'front': 'Give an example of mutualistic coevolution where a specific prediction was made and later confirmed.',
            'back': 'DARWIN\'S MADAGASCAR ORCHID PREDICTION: In 1862, Darwin examined a Madagascar orchid (Angraecum sesquipedale) with an unusually long nectary spur — 28-30 cm. He predicted that a pollinator with a matching 25-30 cm proboscis must exist, even though none was known at the time, because the orchid\'s nectar would otherwise be inaccessible. This was a bold prediction from coevolutionary theory. FORTY YEARS LATER (1903), after Darwin\'s death, the moth Xanthopan morganii praedicta (the "predicted" one) was discovered with exactly that proboscis length. This is a textbook case of a successful evolutionary prediction — and it demonstrated that coevolution can produce matching morphologies without either species having to "know" what the other is doing.',
        },
        quiz={
            'question': 'Darwin predicted the existence of a Madagascar moth with a 25+ cm proboscis based on what observation?',
            'correct': 'A Madagascar orchid with a nectary 28-30 cm long that no known pollinator could reach',
            'distractors': [
                'Fossil evidence of ancient moths',
                'DNA analysis of modern moths',
                'Direct observation of pollination',
            ],
        },
        visual={
            'type': 'match',
            'description': 'Mutualistic morphological matching',
            'regions': [
                {'label': 'Orchid', 'color': '#7de2d1', 'items': ['Long nectar spur', '28-30 cm']},
                {'label': 'Moth', 'color': '#ffc857', 'items': ['Long proboscis', '25-30 cm match']},
                {'label': 'Benefit', 'color': '#4ea8de', 'items': ['Pollen transfer', 'Nectar reward']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Length matches length. Darwin predicted, nature confirmed.',
            'trap': 'Many mutualisms can break down if one partner evolves to cheat — obligate mutualisms can be vulnerable.',
        },
    ))
    nodes.append(build_node(
        id='lec9-mimicry',
        title='Mullerian & Batesian Mimicry',
        subtitle='Signal evolution under predator selection (Lec 9 slides 21-29)',
        color='coral', row=8,
        heading='Lecture 9 — Mimicry',
        sections=slides_to_sections(d, (21, 29)),
        examples=[
            'MÜLLERIAN mimicry: multiple UNPALATABLE/dangerous species converge on similar warning signals. Benefits both — predators learn faster. e.g., Heliconius butterflies, coral snakes.',
            'BATESIAN mimicry: a PALATABLE species mimics a dangerous/unpalatable model. Benefits only the mimic — cost to the model as predators sometimes attack (naive or if mimic becomes too common).',
            'Mimicry requires (1) a model, (2) a mimic, (3) a deceivable predator.',
            'Tūī bird (New Zealand): Some plants mimic flowers normally pollinated by tūīs to attract them.',
        ],
        warnings=[
            'Batesian mimicry is DECEPTIVE — mimics exploit the predator\'s learned avoidance. If mimics become too common relative to the model, the deception breaks down.',
        ],
        mnemonic='Müllerian = Mutual protection (both toxic). Batesian = Bluffing (mimic is safe).',
        flashcard={
            'front': 'Compare Müllerian and Batesian mimicry. Which is a mutualism and which is a form of parasitism?',
            'back': 'MÜLLERIAN MIMICRY: Multiple UNPALATABLE/dangerous species converge on similar warning colorations (often bright red/yellow/black bands). All the mimicking species BENEFIT because predators only need to learn ONE aposematic signal to avoid all of them — pooling the "teaching cost" of predator learning across many species. This is a MUTUALISM: every species gains. Example: Heliconius butterflies in the Amazon, where many toxic species share similar wing patterns. BATESIAN MIMICRY: A PALATABLE species mimics an unpalatable model. Only the MIMIC benefits (escaping predation by bluffing); the MODEL pays a cost because naive or confused predators may attack mistaken individuals. This is a form of PARASITISM — the mimic exploits the model\'s honest signal. Example: some flies and moths resemble stinging bees or wasps despite being harmless. KEY DIFFERENCE: Müllerian = both defended, mutual. Batesian = one defended, one not, parasitic.',
        },
        quiz={
            'question': 'Two unrelated toxic butterfly species gradually evolve the same warning color pattern. This is:',
            'correct': 'Müllerian mimicry — mutually beneficial convergence on a shared warning signal',
            'distractors': [
                'Batesian mimicry — one is palatable, one is not',
                'Camouflage — both are trying to hide',
                'Coincidental convergence with no fitness effect',
            ],
        },
        visual={
            'type': 'comparison',
            'description': 'Mimicry types',
            'regions': [
                {'label': 'Müllerian', 'color': '#ff6b6b', 'items': ['Both toxic', 'Mutual benefit', 'Faster predator learning']},
                {'label': 'Batesian', 'color': '#ffc857', 'items': ['Mimic palatable', 'Model toxic', 'Parasitic on model']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'M = Mutual. B = Bluff.',
            'trap': 'Batesian mimics only work if rare relative to model. If mimics outnumber models, predators learn the signal is unreliable.',
        },
    ))
    nodes.append(build_node(
        id='lec9-endosymbiosis',
        title='Endosymbiosis & Microbes',
        subtitle='Mitochondria, chloroplasts, and leafhopper symbionts (Lec 9 slides 30-36)',
        color='green', row=8,
        heading='Lecture 9 — Microbes and Endosymbiosis',
        sections=slides_to_sections(d, (30, 36)),
        examples=[
            'Endosymbiosis theory (Margulis): mitochondria and chloroplasts are descendants of free-living bacteria engulfed by ancestral eukaryotes.',
            'Evidence: mitochondria and chloroplasts have their own circular DNA, double membranes, and divide by binary fission like bacteria.',
            'Aster leafhoppers carry bacterial endosymbionts that provide essential amino acids.',
            'Plant plastids are derived from free-living cyanobacteria.',
            'Many insects depend on bacterial symbionts for survival — without them, they cannot develop.',
        ],
        mnemonic='Endosymbiosis: not just a historical event — happening continuously today. Life is collaborative.',
        flashcard={
            'front': 'What is the endosymbiotic theory, and what evidence supports it for mitochondria and chloroplasts?',
            'back': 'ENDOSYMBIOTIC THEORY (Lynn Margulis, 1967): mitochondria and chloroplasts originated as FREE-LIVING BACTERIA that were engulfed by (or entered) ancestral eukaryotic cells and became permanent intracellular symbionts. Mitochondria descend from an alpha-proteobacterium; chloroplasts descend from a cyanobacterium. EVIDENCE: (1) Mitochondria and chloroplasts have their OWN circular DNA (like bacteria), separate from the nuclear genome. (2) They have DOUBLE MEMBRANES — the inner membrane derived from the bacterial cell membrane, the outer from the host phagosome. (3) They DIVIDE BY BINARY FISSION, like bacteria. (4) Their ribosomes are 70S (bacterial type), not 80S (eukaryotic). (5) Some antibiotics that target bacterial ribosomes also affect mitochondria (but not cytoplasmic ribosomes). (6) Phylogenetic analysis of mitochondrial/chloroplast DNA places them within specific bacterial clades. The theory is now universally accepted and is one of the most important ideas in evolution.',
        },
        quiz={
            'question': 'Which feature of mitochondria provides the strongest evidence for their bacterial origin?',
            'correct': 'They have their own circular DNA, double membrane, and divide by binary fission',
            'distractors': [
                'They contain ATP',
                'They are found only in animal cells',
                'They produce oxygen as a byproduct',
            ],
        },
        visual={
            'type': 'origin',
            'description': 'Endosymbiosis: two major events',
            'regions': [
                {'label': 'Mitochondria', 'color': '#ff6b6b', 'items': ['Alpha-proteobacterium', '~2 Ga engulfment', 'Universal in eukaryotes']},
                {'label': 'Chloroplasts', 'color': '#7de2d1', 'items': ['Cyanobacterium', '~1.5 Ga engulfment', 'Plants & algae only']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two bacterial ancestors, two major leaps.',
            'trap': 'Only some eukaryotes (plants, algae) have chloroplasts — all eukaryotes have mitochondria (or mitochondrial remnants).',
        },
    ))
    return nodes


def lec10_11_nodes():
    d = load_lec('lec10_11')
    nodes = []
    nodes.append(build_node(
        id='lec1011-why-sex',
        title='Why Sex? Costs & Benefits',
        subtitle='The twofold cost of sex and the Red Queen (Lec 10-11 slides 1-13)',
        color='pink', row=9,
        heading='Lecture 10-11 — Why Sexual Reproduction?',
        sections=slides_to_sections(d, (1, 13)),
        examples=[
            'Twofold cost of sex: an asexual female passes 100% of her genes to each offspring; a sexual female passes only 50%. Asexual lineages should grow twice as fast.',
            'Other costs: finding a mate, courtship energy, risk of STDs, loss of coadapted gene combinations.',
            'Benefits: (1) combining beneficial mutations, (2) clearing deleterious mutations (Muller\'s ratchet), (3) reducing sibling competition through variation, (4) Red Queen effect — staying ahead of coevolving parasites.',
        ],
        mnemonic='Red Queen: "It takes all the running you can do, to keep in the same place." Sex = running against parasites.',
        flashcard={
            'front': 'What is the Red Queen hypothesis for the maintenance of sexual reproduction, and what evidence supports it?',
            'back': 'The RED QUEEN HYPOTHESIS (named after Lewis Carroll\'s Red Queen): sexual reproduction persists despite its twofold cost because it allows hosts to stay AHEAD of rapidly coevolving parasites. Parasites evolve fast (short generations, large populations) and constantly generate new genotypes that evade host defenses. Asexual hosts cannot shuffle their genes, so parasites adapt to them. Sexual hosts produce genetically variable offspring, some of which are resistant to current parasite genotypes — a moving target. EVIDENCE: (1) Lively studied New Zealand freshwater snails (Potamopyrgus antipodarum) that have both sexual and asexual lineages. In populations with high parasite pressure, sexual lineages dominate; in low-parasite populations, asexuals dominate. (2) Experimental coevolution of bacteria and phages shows sexual hosts maintain higher fitness under parasite pressure. The Red Queen provides the strongest answer to why sex is worth its twofold cost.',
        },
        quiz={
            'question': 'The "twofold cost of sex" refers to:',
            'correct': 'An asexual female passes 100% of her genes to each offspring, while a sexual female passes only 50%',
            'distractors': [
                'Sexual reproduction requires twice as much energy per offspring',
                'Males are twice as likely to get sick as females',
                'Sexual offspring have half the survival rate of asexual offspring',
            ],
        },
        visual={
            'type': 'cost-benefit',
            'description': 'Why sex persists despite costs',
            'regions': [
                {'label': 'Costs', 'color': '#ff6b6b', 'items': ['2× gene dilution', 'Mate finding', 'STDs', 'Lost gene combos']},
                {'label': 'Benefits', 'color': '#7de2d1', 'items': ['Combine beneficials', 'Clear deleterious', 'Red Queen', 'Reduced sib competition']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Costs 2×, Benefits variable.',
            'trap': 'No single benefit fully explains sex — most evolutionary biologists believe multiple benefits (not one alone) outweigh the costs.',
        },
    ))
    nodes.append(build_node(
        id='lec1011-anisogamy',
        title='Anisogamy: The Origin of Sexual Selection',
        subtitle='Why males and females exist + investment asymmetry (Lec 10-11 slides 14-22)',
        color='purple', row=9,
        heading='Lecture 10-11 — Anisogamy and Sexual Selection',
        sections=slides_to_sections(d, (14, 22)),
        examples=[
            'Anisogamy: gametes of unequal size. Small cheap gametes (sperm) = male. Large expensive gametes (egg) = female.',
            'Isogamy → anisogamy evolved because disruptive selection on gamete size: a few large, well-provisioned gametes + many small, cheap gametes outperform intermediates.',
            'Anisogamy leads to differential reproductive investment: females invest more per offspring → fewer offspring per female.',
            'Result: males benefit from MORE MATINGS, females benefit from BETTER MATES. Leads to sexual selection.',
        ],
        mnemonic='Small sperm, Big eggs → different strategies → Sexual selection.',
        flashcard={
            'front': 'Explain how anisogamy leads to differential reproductive investment and, ultimately, sexual selection.',
            'back': 'ANISOGAMY = unequal gamete sizes. It evolved from isogamy (equal gametes) because disruptive selection favored two strategies: (A) a few large, nutrient-rich gametes (EGGS) that give each offspring a survival advantage, and (B) many small, cheap gametes (SPERM) that can contact more eggs. Intermediates lose to both strategies. Because EGGS are expensive, each female can produce only a LIMITED number of eggs per lifetime. Because SPERM are cheap, males can produce nearly unlimited sperm. CONSEQUENCE: Females are limited by RESOURCES (to make eggs and invest in offspring). Males are limited by MATINGS (access to females). This creates an ASYMMETRY: males benefit from many matings with any available female; females benefit from selective mating with the BEST male. This is the foundation of sexual selection — male-male competition AND female choice both arise directly from anisogamy. This logic (Bateman 1948, Trivers 1972) is one of the most important ideas in evolutionary biology.',
        },
        quiz={
            'question': 'Why do anisogamy and differential investment lead to sexual selection?',
            'correct': 'Males compete for limited female matings while females choose carefully among many available males',
            'distractors': [
                'Males and females are fundamentally equal in reproductive strategy',
                'Sexual selection is independent of gamete size',
                'Only females experience sexual selection',
            ],
        },
        visual={
            'type': 'asymmetry',
            'description': 'Anisogamy drives sexual asymmetry',
            'regions': [
                {'label': 'Egg', 'color': '#ff6b6b', 'items': ['Large', 'Expensive', 'Limited per lifetime', '→ Female is choosy']},
                {'label': 'Sperm', 'color': '#4ea8de', 'items': ['Small', 'Cheap', 'Nearly unlimited', '→ Male competes']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Small + Many + Cheap vs Big + Few + Expensive.',
            'trap': 'Sex ROLES are not fixed — in some species (pipefish, seahorses) males invest more and females compete. The rule is: the sex investing MORE becomes the choosy one.',
        },
    ))
    nodes.append(build_node(
        id='lec1011-male-female-strategies',
        title='Male Strategies & Female Choice',
        subtitle='Ornaments, leks, nuptial gifts, sensory bias (Lec 10-11 slides 23-37)',
        color='teal', row=9,
        heading='Lecture 10-11 — Sexual Selection Strategies',
        sections=slides_to_sections(d, (23, 37)),
        examples=[
            'Side-blotched lizards: three morphs (rock-paper-scissors) maintained by negative frequency-dependent selection.',
            'Nuptial gifts: male provides food to female (e.g., scorpionflies, crickets, spiders). Female evaluates gift quality as a signal of male quality.',
            'Redback spiders: males voluntarily sacrifice themselves to be eaten, prolonging copulation and siring more offspring.',
            'Leks: males gather at display sites for female inspection (sage grouse, manakins).',
            'Sensory bias: female preferences may arise from pre-existing sensory biases (e.g., swordtail fish — females prefer swords even in species without them).',
            'Ornaments can signal GENETIC QUALITY (handicap principle) or arbitrary runaway selection.',
        ],
        mnemonic='Costly signal = honest. Ornaments can\'t be faked if they are genuinely handicapping.',
        flashcard={
            'front': 'What is the "handicap principle" for sexual ornaments, and why must the ornaments be costly to function as honest signals?',
            'back': 'The HANDICAP PRINCIPLE (Zahavi 1975): exaggerated male ornaments (peacock tails, elaborate colors, long calls) evolve because they serve as HONEST SIGNALS OF QUALITY precisely BECAUSE they are costly. Only a high-quality male can afford to grow and maintain an extravagant ornament — low-quality males would die or fail to reproduce under the handicap. Therefore, a male with a massive ornament is demonstrating "I can thrive even with this burden." If ornaments were cheap, ANY male could grow one, and the signal would become uninformative (dishonest). The cost ENFORCES honesty — it\'s a signal that cannot be faked. Low-quality males could grow fake ornaments only at unsustainable fitness cost, so they don\'t. This is why peacock tails, male deer antlers, and stag beetle mandibles are so extravagant and metabolically expensive — the expense is the point.',
        },
        quiz={
            'question': 'According to the handicap principle, why do peacock tails evolve to be so large and metabolically expensive?',
            'correct': 'The cost ensures the signal is honest — only high-quality males can afford it, so the tail truthfully signals genetic quality',
            'distractors': [
                'Peahens cannot distinguish different tail sizes, so size is random',
                'Large tails are actually free to produce',
                'Large tails improve peacock flight ability',
            ],
        },
        visual={
            'type': 'strategies',
            'description': 'Male reproductive strategies',
            'regions': [
                {'label': 'Competition', 'color': '#ff6b6b', 'items': ['Male-male fighting', 'Weaponry', 'Territory defense']},
                {'label': 'Choice', 'color': '#7de2d1', 'items': ['Ornaments', 'Handicap signals', 'Lek display', 'Nuptial gifts']},
                {'label': 'Alternatives', 'color': '#ffc857', 'items': ['Sneaker males', 'Alt morphs', 'Freq-dependent']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fight, Display, or Cheat.',
            'trap': 'Runaway selection (Fisherian) and handicap signals (Zahavian) are not mutually exclusive — both can operate simultaneously.',
        },
    ))
    nodes.append(build_node(
        id='lec1011-sperm-competition',
        title='Sperm Competition & Sexual Conflict',
        subtitle='When females mate with multiple males (Lec 10-11 slides 38-45)',
        color='red', row=9,
        heading='Lecture 10-11 — Sperm Competition and Sexual Conflict',
        sections=slides_to_sections(d, (38, 45)),
        examples=[
            'Sperm competition: when multiple males\' sperm compete within the female reproductive tract to fertilize eggs.',
            'Male strategies: (1) Spines remove rival sperm (Odonata), (2) Larger testes produce more sperm (primates with promiscuous females), (3) Sperm cooperate by forming swimming trains (some rodents), (4) Mate guarding / mating plugs / copulatory prolongation.',
            'Drosophila seminal fluid contains chemicals that suppress female remating and reduce sperm of previous males — BUT also shorten female lifespan (sexually antagonistic).',
            'Sexual conflict: what is optimal for males may harm females.',
        ],
        warnings=[
            'Sexual conflict can drive rapid reciprocal evolution — an arms race between the sexes within a species.',
        ],
        mnemonic='Remove, Out-produce, Cooperate, Prevent remating.',
        flashcard={
            'front': 'What is sexual conflict and how does it manifest in Drosophila seminal fluid proteins?',
            'back': 'SEXUAL CONFLICT arises when what is optimal for male reproductive success is HARMFUL to female fitness (or vice versa). Because males and females share most of their genomes, evolution of male-beneficial traits can reduce female fitness and drive counter-adaptations in females — a sexually antagonistic coevolutionary arms race WITHIN a species. DROSOPHILA EXAMPLE: Male seminal fluid contains proteins (ACPs) that (1) suppress female remating with other males, (2) increase female egg-laying rate, and (3) kill sperm of previously mated males. These adaptations BENEFIT the male (by monopolizing paternity and accelerating reproduction). HOWEVER, the same chemicals ALSO SHORTEN FEMALE LIFESPAN and REDUCE HER LIFETIME REPRODUCTIVE SUCCESS. Females experience selection to resist the harmful effects, potentially by evolving detoxifying enzymes or refusing to mate. This drives reciprocal evolution between male offense and female defense — a form of intragenomic arms race. Sexual conflict is one of the most important insights of modern sexual selection theory.',
        },
        quiz={
            'question': 'A species where females mate with many males during one estrus period is most likely to have evolved:',
            'correct': 'Relatively large testes to produce more sperm for competition',
            'distractors': [
                'Elaborate male display ornaments for female choice',
                'Complete monogamy',
                'Reduced sexual dimorphism',
            ],
        },
        visual={
            'type': 'strategies',
            'description': 'Sperm competition strategies',
            'regions': [
                {'label': 'Remove rivals', 'color': '#ff6b6b', 'items': ['Dragonfly penis spines', 'Scrape previous sperm']},
                {'label': 'Out-produce', 'color': '#4ea8de', 'items': ['Bigger testes', 'More sperm per ejaculate']},
                {'label': 'Cooperate', 'color': '#7de2d1', 'items': ['Sperm trains', 'Cooperative swimming']},
                {'label': 'Prevent remating', 'color': '#ffc857', 'items': ['Mating plugs', 'Mate guarding', 'Chemicals in semen']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'RCOP: Remove, Cooperate, Out-produce, Prevent.',
            'trap': 'Testis size (relative to body mass) is a strong predictor of mating system — promiscuous species have large testes, monogamous species have small ones.',
        },
    ))
    return nodes


def lec12_nodes():
    d = load_lec('lec12')
    nodes = []
    nodes.append(build_node(
        id='lec12-life-history-intro',
        title='Life History Strategies & Trade-offs',
        subtitle='r-K strategies, energy and time trade-offs (Lec 12 slides 1-11)',
        color='amber', row=10,
        heading='Lecture 12 — Life History Evolution',
        sections=slides_to_sections(d, (1, 11)),
        examples=[
            'Life history: the schedule of birth, maturation, reproduction, and death.',
            'r-strategy: many small offspring, little parental care, fast maturation (insects, weeds).',
            'K-strategy: few large offspring, heavy parental care, slow maturation (elephants, humans, oak trees).',
            'Trade-offs: energy spent on reproduction CANNOT be spent on growth or survival. Time spent finding a mate cannot be spent foraging.',
        ],
        mnemonic='r vs K: rabbits (r) vs K-apes. Live fast, die young OR slow and steady.',
        flashcard={
            'front': 'What are the classic r vs K life history strategies, and what trade-off underlies the distinction?',
            'back': 'The r/K strategy framework describes two ends of a continuum of life-history strategies. r-SELECTED species (named for r in population growth models) live in unstable or unpredictable environments. They evolve FAST reproduction: many small offspring, rapid maturation, little parental care, short lifespan. Examples: insects, dandelions, mice. Each offspring has low survival probability, but sheer numbers compensate. K-SELECTED species (K = carrying capacity) live in stable, competitive environments. They evolve SLOW reproduction: few large offspring, long maturation, heavy parental investment, long lifespan. Examples: elephants, humans, oak trees. Each offspring has high survival probability. The UNDERLYING TRADE-OFF is that energy/time devoted to reproduction cannot be used for growth or maintenance, and vice versa. The r/K framework is now considered a simplification — modern life history theory uses continuous traits and optimization models — but it remains a useful conceptual starting point.',
        },
        quiz={
            'question': 'An r-selected species is most likely to:',
            'correct': 'Produce many small offspring with little parental care and mature quickly',
            'distractors': [
                'Produce few large offspring with heavy parental care',
                'Have very long lifespans',
                'Live in highly stable environments',
            ],
        },
        visual={
            'type': 'continuum',
            'description': 'r-K strategy continuum',
            'regions': [
                {'label': 'r-strategy', 'color': '#ff6b6b', 'items': ['Many small offspring', 'Fast maturation', 'Unstable environments']},
                {'label': 'K-strategy', 'color': '#4ea8de', 'items': ['Few large offspring', 'Slow maturation', 'Stable environments']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'r = reckless; K = careful.',
            'trap': 'r/K is a continuum, not a binary. Most species are somewhere between the extremes.',
        },
    ))
    nodes.append(build_node(
        id='lec12-aging',
        title='Extrinsic Mortality, Aging, & Senescence',
        subtitle='Why organisms age — Medawar and Williams (Lec 12 slides 12-27)',
        color='gray', row=10,
        heading='Lecture 12 — Why Organisms Age',
        sections=slides_to_sections(d, (12, 27)),
        examples=[
            'High extrinsic mortality (predators, disease) favors fast reproduction and short lifespan — there\'s no point "saving" resources for old age if you probably won\'t reach it.',
            'Low extrinsic mortality favors slow development and longer lifespan — energy investment in maintenance pays off.',
            'Reznick\'s guppy experiment: high-predation Trinidad populations evolve faster maturation and higher reproductive rates than low-predation populations. Experimentally confirmed in 11 years after transplant.',
            'MEDAWAR\'S THEORY: mutations with late-life harmful effects escape selection because most individuals die before expressing them.',
            'WILLIAMS\' antagonistic pleiotropy theory: genes beneficial early in life can be maintained even if harmful later.',
        ],
        warnings=[
            'Aging is NOT inevitable in all species — some organisms (hydra, some clams, lobsters) show negligible senescence.',
        ],
        mnemonic='MEDI: Mutation accumulation + Extrinsic mortality → Declining selection → Inevitable aging.',
        flashcard={
            'front': 'Why does high extrinsic mortality favor the evolution of shorter lifespans and earlier reproduction?',
            'back': 'EXTRINSIC MORTALITY = death from environmental sources (predation, disease, accidents, starvation) that are NOT age-related. When extrinsic mortality is HIGH, few individuals survive to old age regardless of their biology — so selection for traits that extend life has little effect (because the life extension never happens before extrinsic death). Instead, selection strongly favors EARLY, RAPID REPRODUCTION to pass on genes before random death strikes. GUPPY EXPERIMENTS (Reznick et al.): In Trinidad streams, guppies below waterfalls face predation from pike cichlids (high extrinsic mortality) and evolve FAST maturation and HIGH reproductive rates. Guppies above waterfalls face killifish (low extrinsic mortality) and evolve SLOW maturation and LOWER reproductive rates. When Reznick experimentally transplanted low-predation guppies to high-predation sites, within 11 years (roughly 30 guppy generations) they evolved the fast life history of native high-predation fish. This is a textbook demonstration that extrinsic mortality shapes life history evolution.',
        },
        quiz={
            'question': 'Reznick\'s guppy transplant experiment showed that after 11 years in high-predation streams, guppies evolved:',
            'correct': 'Faster maturation and earlier, higher reproductive rates',
            'distractors': [
                'Longer lifespans and delayed reproduction',
                'Increased body size and reduced fertility',
                'No detectable evolutionary change',
            ],
        },
        visual={
            'type': 'comparison',
            'description': 'Mortality regime shapes life history',
            'regions': [
                {'label': 'High extrinsic mortality', 'color': '#ff6b6b', 'items': ['Fast maturation', 'Early reproduction', 'Short lifespan', 'e.g., high-predation guppies']},
                {'label': 'Low extrinsic mortality', 'color': '#4ea8de', 'items': ['Slow maturation', 'Late reproduction', 'Long lifespan', 'e.g., low-predation guppies']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Dangerous world → live fast. Safe world → live slow.',
            'trap': 'Aging is not "programmed" — it emerges from weakened selection at older ages, not from an evolved death program.',
        },
    ))
    nodes.append(build_node(
        id='lec12-sex-allocation',
        title='Parental Investment & Sex Allocation',
        subtitle='When to invest in which sex (Lec 12 slides 28-41)',
        color='pink', row=10,
        heading='Lecture 12 — Parental Investment and Sex Allocation',
        sections=slides_to_sections(d, (28, 41)),
        examples=[
            'Parental investment: any contribution of resources or time to one offspring that reduces the parent\'s ability to invest in others.',
            'Sex role reversal: pipefish and seahorses — males carry offspring in brood pouches; females compete for male mates.',
            'Female-biased operational sex ratios create male choice and female competition.',
            'Fisher\'s principle: at equilibrium, parents should invest equally in males and females. If one sex is rare, selection favors producing more of it.',
            'Trivers-Willard: parents in good condition should invest in sons (in species where male RS depends on condition); poor-condition parents should invest in daughters (safer reproductive return).',
        ],
        mnemonic='Fisher says 50/50. Trivers-Willard says adjust by condition. Seahorses reverse it all.',
        flashcard={
            'front': 'State Fisher\'s principle of sex allocation and explain why the equilibrium sex ratio is 1:1.',
            'back': 'FISHER\'S PRINCIPLE (R.A. Fisher 1930): at evolutionary equilibrium, parents should invest equally in male and female offspring, which produces (roughly) a 1:1 SEX RATIO at sexual maturity. REASONING: Suppose males become rare. Each male then has higher mating success than each female (because there are fewer males to share the females). Parents who happen to produce more sons gain a fitness advantage because their sons have higher per-capita reproductive success. Selection favors producing more sons, UNTIL males stop being rare. The reverse applies if females become rare. The only STABLE (evolutionarily stable strategy) equilibrium is when producing either sex yields equal expected fitness returns — which happens when the SEX RATIO is 1:1 (weighted by INVESTMENT cost, not counts, if sexes are unequally costly). This explains why most species with genetic sex determination produce ~50/50 sex ratios despite the apparent waste of producing "surplus" males.',
        },
        quiz={
            'question': 'In a pipefish species where males carry offspring in a brood pouch and females compete for males, who is expected to be the choosier sex?',
            'correct': 'Males, because they invest more per offspring and have limited brood capacity',
            'distractors': [
                'Females, because they produce eggs',
                'Neither — pipefish mate randomly',
                'Both are equally choosy',
            ],
        },
        visual={
            'type': 'principle',
            'description': 'Sex allocation principles',
            'regions': [
                {'label': 'Fisher', 'color': '#4ea8de', 'items': ['1:1 investment', 'Frequency-dependent', 'Stable equilibrium']},
                {'label': 'Trivers-Willard', 'color': '#7de2d1', 'items': ['Adjust by condition', 'Good parents → sons', 'Poor parents → daughters']},
                {'label': 'Role reversal', 'color': '#ffc857', 'items': ['Pipefish, seahorses', 'Males invest more', 'Females compete']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Fisher = baseline. Trivers-Willard = condition. Pipefish = reverse.',
            'trap': 'Fisher\'s principle is about INVESTMENT not COUNT. If males are cheaper to produce, more males are expected.',
        },
    ))
    return nodes


def lec13_nodes():
    d = load_lec('lec13')
    nodes = []
    nodes.append(build_node(
        id='lec13-ess-game',
        title='Game Theory & Evolutionarily Stable Strategies',
        subtitle='ESS, hawk-dove, frequency-dependent selection (Lec 13 slides 1-7)',
        color='purple', row=11,
        heading='Lecture 13 — Evolutionary Game Theory',
        sections=slides_to_sections(d, (1, 7)),
        examples=[
            'ESS: a strategy that, if adopted by most of the population, cannot be invaded by a rare alternative.',
            'Hawk-Dove game (Maynard Smith 1973): hawks fight for resources, doves share. At equilibrium, a mixed population of hawks and doves is stable.',
            'Rock-paper-scissors dynamics: side-blotched lizards with orange/yellow/blue throat morphs maintained by negative frequency-dependent selection.',
            'Game theory assumes frequency-dependent payoff — your fitness depends on what others are doing.',
        ],
        mnemonic='ESS = Evolutionarily Stable Strategy. Stable = can\'t be invaded by a rare mutant.',
        flashcard={
            'front': 'What is an Evolutionarily Stable Strategy (ESS) and why can a population of hawks-only or doves-only NOT be an ESS in the Hawk-Dove game?',
            'back': 'An EVOLUTIONARILY STABLE STRATEGY (ESS; Maynard Smith & Price 1973) is a strategy that, once common in a population, CANNOT be invaded by any rare alternative mutant strategy — that is, a rare mutant playing something different has LOWER fitness than the common strategy. HAWK-DOVE GAME: Hawks always fight over resources (high win-or-lose payoff). Doves always share/retreat (low but safe payoff). (1) PURE HAWK POPULATION: Every contest results in a fight, so every hawk suffers expected injury. A rare DOVE mutant avoids all fights and gets lower but consistent payoff — sometimes higher than the hawks. So Dove INVADES — hawk-only is NOT an ESS. (2) PURE DOVE POPULATION: Every contest is shared peacefully. A rare HAWK mutant takes all resources without competition and has much higher fitness than doves. Hawk INVADES — dove-only is NOT an ESS. (3) MIXED EQUILIBRIUM: At a specific ratio of hawks to doves, both strategies have equal expected fitness, and neither can invade. This mixed ratio IS the ESS — and shows how multiple strategies can coexist within a single species.',
        },
        quiz={
            'question': 'Why are side-blotched lizards (with orange, yellow, and blue throat morphs) maintained in a rock-paper-scissors pattern?',
            'correct': 'Negative frequency-dependent selection — each morph is favored when the morph it beats is common',
            'distractors': [
                'Random mutation constantly generates new morphs',
                'Genetic drift randomly shifts morph frequencies',
                'The environment changes each year',
            ],
        },
        visual={
            'type': 'payoff-matrix',
            'description': 'Hawk-Dove game',
            'regions': [
                {'label': 'Hawk vs Hawk', 'color': '#ff6b6b', 'items': ['Fight', 'Win - Injury cost']},
                {'label': 'Hawk vs Dove', 'color': '#ffc857', 'items': ['Hawk wins resource', 'Dove yields']},
                {'label': 'Dove vs Dove', 'color': '#7de2d1', 'items': ['Share resource', 'No injury']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Rock beats scissors beats paper beats rock — cycles without winner.',
            'trap': 'Frequency-dependent selection can maintain multiple alleles indefinitely — heterozygote advantage is only ONE way genetic variation is maintained.',
        },
    ))
    nodes.append(build_node(
        id='lec13-group-individual',
        title='Levels of Selection: Group vs Individual',
        subtitle='Why selection mostly acts on individuals (Lec 13 slides 8-13)',
        color='blue', row=11,
        heading='Lecture 13 — Levels of Selection',
        sections=slides_to_sections(d, (8, 13)),
        examples=[
            'Classical group selection (Wynne-Edwards) proposed that traits "good for the species" evolve because groups with those traits outcompete others.',
            'Williams\' critique (1966): naive group selection usually fails because individual-level selection is stronger — selfish individuals in a group invade and destroy group traits.',
            'Group hunting in African wild dogs works not because it helps the species but because each individual hunter gets more food than hunting alone.',
            'Cliff swallows: colonies provide anti-predator vigilance, but each individual benefits from being in the group.',
        ],
        mnemonic='Selection acts on the INDIVIDUAL. "Good for the species" is a common but wrong framing.',
        flashcard={
            'front': 'Why is "group selection" controversial and why does most modern evolutionary biology emphasize individual-level selection?',
            'back': 'GROUP SELECTION hypothesizes that traits evolve because they benefit the GROUP (or species), even if they reduce individual fitness. CLASSICAL EXAMPLE: "Lemmings leap off cliffs to prevent overpopulation." PROBLEM (Williams 1966): individual selection is much STRONGER than group selection in most cases, because the fitness differences between individuals WITHIN a group are larger and change faster than fitness differences between groups. A "selfish" individual who does NOT cooperate gains an immediate fitness advantage within the group — their genes spread. Within a few generations, the cooperative trait is replaced by the selfish one. For group selection to work, groups must have very restricted gene flow, very high extinction/founding rates, and the group-beneficial trait must be strongly heritable at the group level. Modern biology generally explains "group-like" behavior through (1) KIN SELECTION (helping relatives who share your genes), (2) RECIPROCAL ALTRUISM (I help you expecting future help), or (3) MUTUALISTIC BENEFIT (cooperation that also helps the cooperator directly). MODERN MULTI-LEVEL SELECTION theory accepts some group selection under narrow conditions but emphasizes that most apparent "group selection" is really selection at lower levels.',
        },
        quiz={
            'question': 'A population of wolves hunts in packs. What level of selection best explains pack hunting?',
            'correct': 'Individual selection — each wolf gets more food per hunt when hunting as a pack than alone',
            'distractors': [
                'Group selection only — for the good of the pack',
                'Kin selection only — because wolves are related',
                'Pure altruism with no individual benefit',
            ],
        },
        visual={
            'type': 'levels',
            'description': 'Levels of selection',
            'regions': [
                {'label': 'Gene', 'color': '#8a5cf6', 'items': ['Selfish gene view', 'Dawkins 1976']},
                {'label': 'Individual', 'color': '#4ea8de', 'items': ['Classical Darwinian', 'Most cases']},
                {'label': 'Kin group', 'color': '#7de2d1', 'items': ['Inclusive fitness', 'Hamilton\'s rule']},
                {'label': 'Group/Species', 'color': '#ff6b6b', 'items': ['Rarely works', 'Requires strict conditions']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Gene → Individual → Kin → Rarely group.',
            'trap': 'Do NOT say a trait evolved "for the good of the species" unless you can rule out individual-level explanations.',
        },
    ))
    nodes.append(build_node(
        id='lec13-kin-altruism',
        title='Kin Selection, Inclusive Fitness & Altruism',
        subtitle='Hamilton\'s rule and the evolution of helping (Lec 13 slides 14-21)',
        color='teal', row=11,
        heading='Lecture 13 — Kin Selection and Altruism',
        sections=slides_to_sections(d, (14, 21)),
        examples=[
            'Coefficient of relatedness (r): the probability that two individuals share an allele by descent. Full siblings: r = 0.5. Half siblings: r = 0.25. First cousins: r = 0.125.',
            'Hamilton\'s rule: altruism evolves when rB > C, where r = relatedness, B = benefit to recipient, C = cost to actor.',
            'Inclusive fitness: an individual\'s total fitness = direct fitness (own reproduction) + indirect fitness (from helping relatives reproduce).',
            'Haldane: "I would lay down my life for two brothers or eight cousins" — illustrates rB > C logic.',
            'Haplodiploidy in Hymenoptera: sisters are more related to each other (r = 0.75) than to their own offspring (r = 0.5), which may have facilitated eusociality in ants, bees, wasps.',
        ],
        mnemonic='Hamilton\'s rule: rB > C. Relatedness × Benefit > Cost.',
        flashcard={
            'front': 'State Hamilton\'s rule and use it to explain why an alarm call that alerts relatives to a predator can evolve despite putting the caller at risk.',
            'back': 'HAMILTON\'S RULE (1964): an altruistic behavior can evolve whenever rB > C, where r = the COEFFICIENT OF RELATEDNESS between actor and recipient (probability of sharing an allele by descent), B = the FITNESS BENEFIT received by the beneficiary, and C = the FITNESS COST to the altruist. APPLICATION TO ALARM CALLS: Suppose a ground squirrel spots a hawk. Calling out attracts the hawk\'s attention (COST = increased risk of predation on the caller). But the alarm alerts nearby squirrels who escape to burrows (BENEFIT to them). If the nearby squirrels are RELATIVES (mother, siblings, cousins), they share many alleles with the caller — so genes for alarm-calling behavior benefit copies of themselves in the bodies of saved relatives. When rB > C (where r is typically averaged across all beneficiaries), alarm-calling spreads even though individual callers suffer. This is INCLUSIVE FITNESS: the actor\'s fitness = own direct reproduction + indirect reproduction through helped relatives. HALDANE QUOTE: "I would lay down my life for two brothers [r = 0.5, 2 × 0.5 = 1.0] or eight cousins [r = 0.125, 8 × 0.125 = 1.0]" — the math of kin selection in one joke.',
        },
        quiz={
            'question': 'According to Hamilton\'s rule, an altruistic behavior is favored when:',
            'correct': 'rB > C, where r is the coefficient of relatedness, B is the benefit to the recipient, and C is the cost to the actor',
            'distractors': [
                'B > rC — benefit exceeds cost scaled by relatedness',
                'r + B > C — relatedness plus benefit exceeds cost',
                'r > B/C — relatedness exceeds benefit-to-cost ratio',
            ],
        },
        visual={
            'type': 'equation',
            'description': 'Hamilton\'s rule visualized',
            'regions': [
                {'label': 'r', 'color': '#4ea8de', 'items': ['Relatedness', 'Siblings: 0.5', 'Cousins: 0.125']},
                {'label': 'B', 'color': '#7de2d1', 'items': ['Benefit to recipient', 'Measured in offspring']},
                {'label': 'C', 'color': '#ff6b6b', 'items': ['Cost to actor', 'Lost direct reproduction']},
                {'label': 'Test', 'color': '#ffc857', 'items': ['rB > C → altruism evolves', 'rB < C → altruism fails']},
            ],
            'arrows': [], 'tooltips': [],
            'mnemonic': 'Two brothers or eight cousins.',
            'trap': 'Altruism doesn\'t require conscious calculation — the rB > C condition operates through selection over evolutionary time.',
        },
    ))
    return nodes
