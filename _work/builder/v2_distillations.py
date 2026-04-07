"""5-slot Lecture-Notes distillations for all 57 nodes.

Hard schema rules (enforced by audit_v2.py):
  - definition:        single sentence, <=25 words
  - keyTerms:          exactly 4, each def <=6 words, color in {teal,purple,coral,pink}
  - mnemonic.hook:     <=8 words
  - mnemonic.explanation: <=20 words
  - examTrap:          <=25 words, concrete "Wrong: '...'" framing
  - actions:           quizPrompt + flashcardFront + flashcardBack

Color taxonomy:
  teal   = mechanism / process
  purple = entity / unit
  coral  = outcome / trait
  pink   = exception / edge case

Lectures 1-15 follow build.py RL dict. Lectures 16-17 are promoted from
final-exam rows 14 and 15 to give them proper lecture identity:
  Lec 16 = Speciation & Biogeography (row 14)
  Lec 17 = Applied Evolution         (row 15)
"""

V2 = {
    # =====================================================================
    # LEC 1 — INTRODUCTION TO EVOLUTION (Ch 1)
    # =====================================================================
    'lec1-intro-evolution': {
        'lecture': 1, 'lectureTitle': 'Introduction to Evolution',
        'order': 1, 'chapter': 'Ch 1', 'slideRange': '1-9',
        'v2': {
            'definition': 'Evolution is descent with modification, the heritable change in populations across generations producing biological diversity from common ancestors.',
            'keyTerms': [
                {'term': 'Descent',         'def': 'ancestors pass traits to offspring',  'color': 'teal'},
                {'term': 'Modification',    'def': 'traits change between generations',   'color': 'teal'},
                {'term': 'Population',      'def': 'interbreeding individuals sharing genes', 'color': 'purple'},
                {'term': 'Common Ancestry', 'def': 'all life shares one lineage',         'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Descent plus Modification equals Evolution',
                'explanation': 'Inherit then change, two ingredients build all biodiversity from one ancestor over time.',
            },
            'examTrap': "Wrong: 'Individuals evolve.' Only POPULATIONS evolve. A single organism cannot change its allele frequencies during its lifetime.",
            'actions': {
                'quizPrompt':     'Why do biologists say populations, not individuals, evolve?',
                'flashcardFront': 'Define evolution in one sentence.',
                'flashcardBack':  'Descent with modification, heritable change in populations across generations.',
            },
        },
    },
    'lec1-flu-case-study': {
        'lecture': 1, 'lectureTitle': 'Introduction to Evolution',
        'order': 2, 'chapter': 'Ch 1', 'slideRange': '10-21',
        'v2': {
            'definition': 'Influenza H1N1 evolves rapidly through mutation, antigenic drift, and antigenic shift, requiring annual vaccine updates worldwide.',
            'keyTerms': [
                {'term': 'Antigenic Drift',  'def': 'small mutations change surface proteins', 'color': 'teal'},
                {'term': 'Antigenic Shift',  'def': 'reassortment swaps whole gene segments',  'color': 'teal'},
                {'term': 'Hemagglutinin',    'def': 'virus protein binding host cells',        'color': 'purple'},
                {'term': 'Vaccine Escape',   'def': 'immunity evading strains spread',         'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Drift mutates, Shift swaps',
                'explanation': 'Drift accumulates point mutations. Shift recombines whole RNA segments between strains creating pandemic risk.',
            },
            'examTrap': "Wrong: 'Drift and shift mean the same thing.' Drift is small mutations, shift is whole-segment reassortment causing pandemics.",
            'actions': {
                'quizPrompt':     'Distinguish antigenic drift from antigenic shift in influenza.',
                'flashcardFront': 'Why do we need a flu shot every year?',
                'flashcardBack':  'Antigenic drift continually mutates surface proteins, evading prior immunity.',
            },
        },
    },
    'lec1-takehome-course': {
        'lecture': 1, 'lectureTitle': 'Introduction to Evolution',
        'order': 3, 'chapter': 'Ch 1', 'slideRange': '22-30',
        'v2': {
            'definition': 'Evolution unifies all biology and provides practical tools for medicine, agriculture, and conservation through testable hypotheses.',
            'keyTerms': [
                {'term': 'Hypothesis Testing', 'def': 'observation predicts measurable outcome',   'color': 'teal'},
                {'term': 'Unification',        'def': 'evolution connects all life sciences',     'color': 'purple'},
                {'term': 'Application',        'def': 'real world solutions from theory',         'color': 'coral'},
                {'term': 'Misconception',      'def': 'common evolution myths to avoid',          'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Evolution: the OS of biology',
                'explanation': 'Like a computer operating system, evolution is the framework every other biological process runs on.',
            },
            'examTrap': "Wrong: 'Evolution is just a theory.' In science, theory means well tested explanation supported by overwhelming evidence.",
            'actions': {
                'quizPrompt':     'Name three real-world applications where evolutionary theory is essential.',
                'flashcardFront': 'Why study evolution?',
                'flashcardBack':  'It unifies biology and powers medicine, agriculture, and conservation.',
            },
        },
    },

    # =====================================================================
    # LEC 2 — DARWIN AND NATURAL SELECTION (Ch 2)
    # =====================================================================
    'lec2-pre-darwin': {
        'lecture': 2, 'lectureTitle': 'Darwin and Natural Selection',
        'order': 1, 'chapter': 'Ch 2', 'slideRange': '1-9',
        'v2': {
            'definition': 'Pre-Darwinian thinkers Linnaeus, Cuvier, and Lamarck laid groundwork by classifying species and proposing change without selection.',
            'keyTerms': [
                {'term': 'Linnaeus',             'def': 'founded modern taxonomy',         'color': 'purple'},
                {'term': 'Cuvier',               'def': 'documented extinction from fossils', 'color': 'purple'},
                {'term': 'Lamarck',              'def': 'use disuse and acquired inheritance', 'color': 'teal'},
                {'term': 'Acquired Inheritance', 'def': 'lifetime traits passed down, wrong', 'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Linnaeus, Cuvier, Lamarck = LCL',
                'explanation': 'Linnaeus named life, Cuvier proved extinction, Lamarck guessed how, then Darwin synthesized them all.',
            },
            'examTrap': "Wrong: 'Lamarck believed in natural selection.' Lamarck believed in inheritance of acquired characteristics, an incorrect mechanism.",
            'actions': {
                'quizPrompt':     'What did Linnaeus, Cuvier, and Lamarck each contribute to evolutionary thought?',
                'flashcardFront': "Lamarck's mistake?",
                'flashcardBack':  'He believed traits acquired during life were inherited (wrong mechanism).',
            },
        },
    },
    'lec2-darwin-voyage': {
        'lecture': 2, 'lectureTitle': 'Darwin and Natural Selection',
        'order': 2, 'chapter': 'Ch 2', 'slideRange': '10-12',
        'v2': {
            'definition': "Darwin's five-year Beagle voyage gathered fossil and biogeographic evidence that inspired his natural selection theory.",
            'keyTerms': [
                {'term': 'HMS Beagle',        'def': '1831 to 1836 survey ship',    'color': 'purple'},
                {'term': 'Galapagos',         'def': 'island laboratory of variation', 'color': 'purple'},
                {'term': 'Biogeography',      'def': 'geographic pattern of species',  'color': 'coral'},
                {'term': 'Glyptodon Fossils', 'def': 'extinct giant matched living armadillos', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Beagle: five years, one theory',
                'explanation': 'Darwin spent half a decade observing patterns then twenty more years building the explanation.',
            },
            'examTrap': "Wrong: 'Darwin published immediately after the voyage.' He waited 23 years until Wallace's letter forced publication in 1859.",
            'actions': {
                'quizPrompt':     'What evidence from the Beagle voyage shaped Darwin\'s thinking?',
                'flashcardFront': 'When did Origin of Species publish?',
                'flashcardBack':  '1859, twenty-three years after Darwin returned from the Beagle voyage.',
            },
        },
    },
    'lec2-natural-selection-ingredients': {
        'lecture': 2, 'lectureTitle': 'Darwin and Natural Selection',
        'order': 3, 'chapter': 'Ch 2', 'slideRange': '13-23',
        'v2': {
            'definition': 'Natural selection requires variation, heritability, and differential reproductive success, the three ingredients that produce evolution by selection.',
            'keyTerms': [
                {'term': 'Variation',                 'def': 'individuals differ in traits',    'color': 'purple'},
                {'term': 'Heritability',              'def': 'traits pass to offspring',        'color': 'teal'},
                {'term': 'Differential Reproduction', 'def': 'some leave more offspring',       'color': 'teal'},
                {'term': 'Adaptation',                'def': 'trait increases relative fitness', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'VIDA: Variation, Inheritance, Differential, Adaptation',
                'explanation': "Latin for 'life', the four ingredients that produce evolutionary life from random differences.",
            },
            'examTrap': "Wrong: 'Selection requires intent.' Natural selection has no goal. Organisms with higher fitness simply leave more descendants.",
            'actions': {
                'quizPrompt':     'List the four ingredients required for natural selection.',
                'flashcardFront': 'VIDA stands for?',
                'flashcardBack':  'Variation, Inheritance, Differential reproduction, Adaptation.',
            },
        },
    },
    'lec2-finches-case': {
        'lecture': 2, 'lectureTitle': 'Darwin and Natural Selection',
        'order': 4, 'chapter': 'Ch 2', 'slideRange': '24-31',
        'v2': {
            'definition': 'Grant and Grant tracked Galapagos finches across droughts, showing beak size evolved measurably within just a few generations.',
            'keyTerms': [
                {'term': 'Geospiza fortis',  'def': 'medium ground finch species',   'color': 'purple'},
                {'term': 'Beak Depth',       'def': 'heritable trait under selection', 'color': 'teal'},
                {'term': 'Drought 1977',     'def': 'selected larger seeds and beaks', 'color': 'coral'},
                {'term': 'Wet Year Reversal','def': 'small beaks recover advantage',   'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Drought equals deeper beaks',
                'explanation': 'Hard seeds during drought favor strong beaks. Wet years reverse the trend within months.',
            },
            'examTrap': "Wrong: 'The finches evolved during the drought.' The POPULATION evolved as birds with shallow beaks died.",
            'actions': {
                'quizPrompt':     'How did the 1977 drought drive beak-size evolution in Geospiza fortis?',
                'flashcardFront': 'Who studied Galapagos finch evolution in real time?',
                'flashcardBack':  'Peter and Rosemary Grant on Daphne Major (40 plus years).',
            },
        },
    },
    'lec2-descent-modification': {
        'lecture': 2, 'lectureTitle': 'Darwin and Natural Selection',
        'order': 5, 'chapter': 'Ch 2', 'slideRange': '32-41',
        'v2': {
            'definition': 'Common descent links all species through a tree of life evidenced by homology, artificial selection, and shared development.',
            'keyTerms': [
                {'term': 'Homology',            'def': 'same structure, shared ancestor',      'color': 'coral'},
                {'term': 'Artificial Selection','def': 'humans choose breeding individuals',   'color': 'teal'},
                {'term': 'Common Ancestor',     'def': 'lineage every species traces back',    'color': 'purple'},
                {'term': 'Analogy',             'def': 'similar function, different ancestors','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Same bones, different jobs',
                'explanation': 'Bat wing, whale flipper, and human arm share bone structure inherited from one ancestor.',
            },
            'examTrap': "Wrong: 'Bird wings and bat wings are homologous as wings.' Wings are analogous, the bones underneath are homologous.",
            'actions': {
                'quizPrompt':     "How does artificial selection support Darwin's natural selection argument?",
                'flashcardFront': 'Homology versus analogy?',
                'flashcardBack':  'Homology equals shared ancestor; analogy equals similar function only.',
            },
        },
    },

    # =====================================================================
    # LEC 3 — GENETICS AND MUTATION (Ch 5)
    # =====================================================================
    'lec3-genes-proteins': {
        'lecture': 3, 'lectureTitle': 'Genetics and Mutation',
        'order': 1, 'chapter': 'Ch 5', 'slideRange': '1-9',
        'v2': {
            'definition': 'Genes encode proteins through DNA to RNA to protein, with regulatory networks controlling when and where genes activate.',
            'keyTerms': [
                {'term': 'Transcription',      'def': 'DNA copied into mRNA',          'color': 'teal'},
                {'term': 'Translation',        'def': 'mRNA built into protein',       'color': 'teal'},
                {'term': 'Regulatory Network', 'def': 'switches controlling gene expression', 'color': 'purple'},
                {'term': 'Phenotype',          'def': 'observable trait from gene action', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'DNA to RNA to Protein to Trait',
                'explanation': 'The central dogma flows one way, plus regulation determines when each gene speaks aloud.',
            },
            'examTrap': "Wrong: 'One gene equals one trait.' Most traits involve regulatory networks plus environment, polygenic not single gene.",
            'actions': {
                'quizPrompt':     'Trace the central dogma from DNA to phenotype.',
                'flashcardFront': 'Central dogma steps?',
                'flashcardBack':  'Transcription (DNA to mRNA) then translation (mRNA to protein).',
            },
        },
    },
    'lec3-mutations': {
        'lecture': 3, 'lectureTitle': 'Genetics and Mutation',
        'order': 2, 'chapter': 'Ch 5', 'slideRange': '10-17',
        'v2': {
            'definition': 'Mutations are random heritable changes in DNA, the ultimate source of all genetic variation that fuels evolution.',
            'keyTerms': [
                {'term': 'Point Mutation', 'def': 'single base substitution',          'color': 'teal'},
                {'term': 'Indel',          'def': 'insertion or deletion of bases',    'color': 'teal'},
                {'term': 'Neutral',        'def': 'no fitness effect on carrier',      'color': 'pink'},
                {'term': 'Germline',       'def': 'mutations in reproductive cells inherited', 'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Random source, selected fate',
                'explanation': 'Mutations arise blindly. Selection then sorts beneficial from harmful: random input, non random output.',
            },
            'examTrap': "Wrong: 'Mutations happen to help organisms adapt.' Mutations are random with respect to need, selection filters them.",
            'actions': {
                'quizPrompt':     "Why are mutations called 'random with respect to fitness'?",
                'flashcardFront': 'Ultimate source of genetic variation?',
                'flashcardBack':  'Mutation, random heritable changes in DNA sequence.',
            },
        },
    },
    'lec3-sex-meiosis': {
        'lecture': 3, 'lectureTitle': 'Genetics and Mutation',
        'order': 3, 'chapter': 'Ch 5', 'slideRange': '18-19',
        'v2': {
            'definition': 'Meiosis generates genetic diversity through independent assortment and recombination, shuffling parental alleles into novel offspring combinations.',
            'keyTerms': [
                {'term': 'Independent Assortment', 'def': 'chromosomes sort randomly',       'color': 'teal'},
                {'term': 'Recombination',          'def': 'homologs exchange DNA segments',  'color': 'teal'},
                {'term': 'Crossing Over',          'def': 'physical chromosome breakpoints', 'color': 'purple'},
                {'term': 'Gamete Diversity',       'def': 'trillions of unique combinations','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Shuffle then deal',
                'explanation': 'Meiosis shuffles chromosomes and trades parts before dealing each gamete a new genetic hand.',
            },
            'examTrap': "Wrong: 'Meiosis creates new mutations.' It SHUFFLES existing variation; mutations come from DNA replication errors only.",
            'actions': {
                'quizPrompt':     'How does meiosis generate genetic diversity without new mutations?',
                'flashcardFront': 'Two diversity sources in meiosis?',
                'flashcardBack':  'Independent assortment of chromosomes and recombination via crossing over.',
            },
        },
    },
    'lec3-genotype-phenotype': {
        'lecture': 3, 'lectureTitle': 'Genetics and Mutation',
        'order': 4, 'chapter': 'Ch 5', 'slideRange': '20-29',
        'v2': {
            'definition': 'Phenotype emerges from genotype interacting with environment, often through polygenic traits showing continuous quantitative variation.',
            'keyTerms': [
                {'term': 'Genotype',          'def': 'the underlying DNA sequence',     'color': 'purple'},
                {'term': 'Phenotype',         'def': 'the observable physical trait',   'color': 'coral'},
                {'term': 'Polygenic Trait',   'def': 'many genes contribute additively','color': 'teal'},
                {'term': 'GxE Interaction',   'def': 'environment alters gene expression','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Genes propose, environment disposes',
                'explanation': 'DNA sets the possibilities. Environment determines which possibilities become real, neither alone is destiny.',
            },
            'examTrap': "Wrong: 'Identical twins have identical phenotypes.' Same genotype but different environments produce different heights and weights.",
            'actions': {
                'quizPrompt':     "Why don't identical twins have identical phenotypes?",
                'flashcardFront': 'Phenotype equals?',
                'flashcardBack':  'Genotype times Environment (gene expression depends on context).',
            },
        },
    },

    # =====================================================================
    # LEC 4 — MICROEVOLUTION AND HARDY-WEINBERG (Ch 6)
    # =====================================================================
    'lec4-sources-evolution': {
        'lecture': 4, 'lectureTitle': 'Microevolution and Hardy-Weinberg',
        'order': 1, 'chapter': 'Ch 6', 'slideRange': '1-3',
        'v2': {
            'definition': 'Five forces change allele frequencies: mutation, gene flow, genetic drift, non random mating, and natural selection.',
            'keyTerms': [
                {'term': 'Mutation',          'def': 'introduces new alleles',     'color': 'teal'},
                {'term': 'Gene Flow',         'def': 'migration mixes populations','color': 'teal'},
                {'term': 'Drift',             'def': 'random sampling of alleles', 'color': 'teal'},
                {'term': 'Non Random Mating', 'def': 'biased pair formation',      'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'MMDNS: Mutation, Migration, Drift, Nonrandom, Selection',
                'explanation': 'Five forces push allele frequencies. Remove all five and Hardy-Weinberg equilibrium holds perfectly.',
            },
            'examTrap': "Wrong: 'Natural selection is the only force of evolution.' Drift, gene flow, and mutation also change allele frequencies.",
            'actions': {
                'quizPrompt':     'Name the five evolutionary forces and their effects.',
                'flashcardFront': 'Five sources of evolutionary change?',
                'flashcardBack':  'Mutation, gene flow, drift, non-random mating, selection.',
            },
        },
    },
    'lec4-hardy-weinberg': {
        'lecture': 4, 'lectureTitle': 'Microevolution and Hardy-Weinberg',
        'order': 2, 'chapter': 'Ch 6', 'slideRange': '4-12',
        'v2': {
            'definition': 'Hardy-Weinberg equilibrium predicts allele frequencies stay constant when no evolutionary forces act, the null model of population genetics.',
            'keyTerms': [
                {'term': 'p squared plus 2pq plus q squared', 'def': 'genotype frequency equation',     'color': 'teal'},
                {'term': 'Null Model',                        'def': 'baseline expecting no change',    'color': 'purple'},
                {'term': 'Five Assumptions',                  'def': 'no mutation, drift, migration, mating, selection', 'color': 'pink'},
                {'term': 'Equilibrium',                       'def': 'frequencies stable across generations', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'p squared plus 2pq plus q squared',
                'explanation': 'The genotype equation works ONLY when all five evolutionary forces are absent, a hypothetical baseline.',
            },
            'examTrap': "Wrong: 'HWE describes real populations.' HWE is a NULL model. Deviation from HWE is how we DETECT evolution.",
            'actions': {
                'quizPrompt':     'What are the five assumptions of Hardy-Weinberg equilibrium?',
                'flashcardFront': 'HWE genotype equation?',
                'flashcardBack':  'p squared plus 2pq plus q squared equals 1 (null model).',
            },
        },
    },
    'lec4-genetic-drift': {
        'lecture': 4, 'lectureTitle': 'Microevolution and Hardy-Weinberg',
        'order': 3, 'chapter': 'Ch 6', 'slideRange': '13-22',
        'v2': {
            'definition': 'Genetic drift is random change in allele frequencies due to finite sampling, stronger in small populations than large ones.',
            'keyTerms': [
                {'term': 'Sampling Error', 'def': 'chance changes allele counts',    'color': 'teal'},
                {'term': 'Bottleneck',     'def': 'population crash reduces variation','color': 'coral'},
                {'term': 'Founder Effect', 'def': 'small group establishes new population', 'color': 'coral'},
                {'term': 'Fixation',       'def': 'allele reaches 100 percent',      'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Small populations drift further',
                'explanation': "Drift's strength scales inversely with population size. Fewer individuals means bigger random swings.",
            },
            'examTrap': "Wrong: 'Drift only matters in tiny populations.' Drift acts in all finite populations, selection just dominates in large ones.",
            'actions': {
                'quizPrompt':     'Distinguish bottleneck from founder effect.',
                'flashcardFront': 'Genetic drift equals?',
                'flashcardBack':  'Random allele frequency change from finite-sample chance effects.',
            },
        },
    },
    'lec4-selection-mechanism': {
        'lecture': 4, 'lectureTitle': 'Microevolution and Hardy-Weinberg',
        'order': 4, 'chapter': 'Ch 6', 'slideRange': '23-31',
        'v2': {
            'definition': 'Selection coefficients quantify fitness differences between genotypes, predicting how allele frequencies change each generation.',
            'keyTerms': [
                {'term': 'Selection Coefficient (s)', 'def': 'fitness disadvantage measured',     'color': 'teal'},
                {'term': 'Relative Fitness (w)',      'def': 'reproductive success vs best',      'color': 'teal'},
                {'term': 'Dominance',                 'def': 'heterozygote phenotype matches homozygote', 'color': 'purple'},
                {'term': 'Selection Differential',    'def': 'shift in selected parent mean',     'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'w equals 1 minus s',
                'explanation': 'Relative fitness equals one minus selection coefficient, a clean numerical way to compare genotypes.',
            },
            'examTrap': "Wrong: 'Fitness equals strength or survival.' Fitness equals NUMBER of offspring left in next generation, reproduction is the metric.",
            'actions': {
                'quizPrompt':     'How do selection coefficient and relative fitness relate?',
                'flashcardFront': 'Define fitness in evolution.',
                'flashcardBack':  'Number of viable offspring left in next generation (relative).',
            },
        },
    },

    # =====================================================================
    # LEC 5 — QUANTITATIVE GENETICS (Ch 7, slides 1-30)
    # LEC 6 — PHENOTYPIC PLASTICITY (Ch 7, slides 31-45)
    # =====================================================================
    'lec56-quant-intro': {
        'lecture': 5, 'lectureTitle': 'Quantitative Genetics and Heritability',
        'order': 1, 'chapter': 'Ch 7', 'slideRange': '1-13',
        'v2': {
            'definition': 'Quantitative traits show continuous variation produced by many genes plus environment, unlike Mendelian discrete categorical traits.',
            'keyTerms': [
                {'term': 'Mendelian Trait',    'def': 'single gene, discrete categories', 'color': 'purple'},
                {'term': 'Quantitative Trait', 'def': 'many genes, continuous range',     'color': 'purple'},
                {'term': 'Polygenic',          'def': 'many loci contribute additively',  'color': 'teal'},
                {'term': 'Normal Distribution','def': 'bell curve phenotype shape',       'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Many genes equal bell curve',
                'explanation': 'Adding many small additive effects produces normal distributions, central limit theorem applied to genetics.',
            },
            'examTrap': "Wrong: 'Continuous traits aren't genetic.' Continuous variation comes from MANY genes acting together plus environment, still heritable.",
            'actions': {
                'quizPrompt':     'Why do polygenic traits produce bell-curve distributions?',
                'flashcardFront': 'Quantitative versus Mendelian trait?',
                'flashcardBack':  'Quantitative equals many genes continuous; Mendelian equals single gene discrete.',
            },
        },
    },
    'lec56-heritability-breeders': {
        'lecture': 5, 'lectureTitle': 'Quantitative Genetics and Heritability',
        'order': 2, 'chapter': 'Ch 7', 'slideRange': '14-30',
        'v2': {
            'definition': "The breeder's equation R equals h squared times S predicts evolutionary response from heritability and the selection differential.",
            'keyTerms': [
                {'term': 'h squared (Heritability)',   'def': 'proportion of variation genetic', 'color': 'teal'},
                {'term': 'S (Differential)',           'def': 'selected vs population mean',     'color': 'teal'},
                {'term': 'R (Response)',               'def': 'offspring mean shift',            'color': 'coral'},
                {'term': 'Population Specific',        'def': 'h squared changes by environment','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'R equals h squared S',
                'explanation': "Response to selection equals heritability times selection differential, the breeder's recipe for predictable change.",
            },
            'examTrap': "Wrong: 'High heritability means genes determine the trait.' Heritability measures variation explained genetically WITHIN one specific population.",
            'actions': {
                'quizPrompt':     'Apply R equals h squared S to predict beak depth response under drought.',
                'flashcardFront': "Breeder's equation?",
                'flashcardBack':  'R equals h squared times S (response equals heritability times selection differential).',
            },
        },
    },
    'lec56-reaction-norms': {
        'lecture': 6, 'lectureTitle': 'Phenotypic Plasticity and Reaction Norms',
        'order': 1, 'chapter': 'Ch 7', 'slideRange': '31-45',
        'v2': {
            'definition': 'Reaction norms map how a single genotype produces different phenotypes across environments, phenotypic plasticity made visible.',
            'keyTerms': [
                {'term': 'Plasticity',     'def': 'phenotype changes with environment', 'color': 'teal'},
                {'term': 'Genotype',       'def': 'fixed underlying DNA sequence',      'color': 'purple'},
                {'term': 'Reaction Norm',  'def': 'phenotype graph across environments','color': 'coral'},
                {'term': 'Canalization',   'def': 'buffered against environmental change','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Same genes, different shows',
                'explanation': 'One genotype performs different phenotypes depending on the environmental stage it lives on.',
            },
            'examTrap': "Wrong: 'Plasticity is not adaptive.' Plasticity itself can BE the adaptation when environments fluctuate predictably between states.",
            'actions': {
                'quizPrompt':     'How can phenotypic plasticity itself be adaptive?',
                'flashcardFront': 'Reaction norm equals?',
                'flashcardBack':  "Genotype's phenotype profile across environments (plasticity graph).",
            },
        },
    },

    # =====================================================================
    # LEC 7 — SELECTION IN ACTION (Ch 8)
    # =====================================================================
    'lec7-review-empirical': {
        'lecture': 7, 'lectureTitle': 'Selection in Action: Empirical Studies',
        'order': 1, 'chapter': 'Ch 8', 'slideRange': '1-6',
        'v2': {
            'definition': 'Empirical selection studies measure trait variation, fitness differences, and heritability in wild populations to confirm evolution.',
            'keyTerms': [
                {'term': 'Field Study',        'def': 'observation in natural habitat', 'color': 'teal'},
                {'term': 'Mark Recapture',     'def': 'track individuals over time',    'color': 'teal'},
                {'term': 'Selection Gradient', 'def': 'fitness slope along trait',      'color': 'coral'},
                {'term': 'Replication',        'def': 'multiple sites confirm pattern', 'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Vary, Inherit, Differ, Track',
                'explanation': 'Confirm variation, prove heritability, measure fitness differences, track changes, the empirical recipe for selection.',
            },
            'examTrap': "Wrong: 'Selection requires controlled lab conditions.' Most classic selection studies are fieldwork in wild populations across decades.",
            'actions': {
                'quizPrompt':     'What four pieces of evidence demonstrate selection in the wild?',
                'flashcardFront': 'Empirical selection study requirements?',
                'flashcardBack':  'Variation, heritability, fitness differences, generational change measured in nature.',
            },
        },
    },
    'lec7-beach-mice': {
        'lecture': 7, 'lectureTitle': 'Selection in Action: Empirical Studies',
        'order': 2, 'chapter': 'Ch 8', 'slideRange': '7-10',
        'v2': {
            'definition': 'Beach mice evolved light coats independently in Florida and Alabama through Mc1r mutations, classic parallel evolution under predator selection.',
            'keyTerms': [
                {'term': 'Peromyscus polionotus', 'def': 'beach mouse study species',    'color': 'purple'},
                {'term': 'Mc1r Gene',             'def': 'controls coat melanin',        'color': 'teal'},
                {'term': 'Parallel Evolution',    'def': 'same trait, separate origins', 'color': 'coral'},
                {'term': 'Cryptic Coloration',    'def': 'camouflage hides from predators','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Two beaches, two Mc1r solutions',
                'explanation': "Florida's gulf coast and Alabama mice evolved pale coats from different Mc1r mutations, identical adaptive phenotype.",
            },
            'examTrap': "Wrong: 'Parallel evolution means identical mutations.' Parallel means same TRAIT from different mutations, convergence at the phenotype level only.",
            'actions': {
                'quizPrompt':     'Why are beach mice considered an example of parallel evolution?',
                'flashcardFront': 'What gene drives beach mouse coat color?',
                'flashcardBack':  'Mc1r, with different mutations producing the same pale phenotype on each coast.',
            },
        },
    },
    'lec7-tsd': {
        'lecture': 7, 'lectureTitle': 'Selection in Action: Empirical Studies',
        'order': 3, 'chapter': 'Ch 8', 'slideRange': '11-22',
        'v2': {
            'definition': 'Temperature-dependent sex determination ties offspring sex to nest temperature, an evolved plastic response to environmental cues.',
            'keyTerms': [
                {'term': 'TSD',                   'def': 'sex set by incubation temperature', 'color': 'teal'},
                {'term': 'Pivotal Temperature',   'def': 'threshold producing equal sex ratio', 'color': 'purple'},
                {'term': 'Charnov-Bull Model',    'def': 'plasticity favored when sexes differ', 'color': 'coral'},
                {'term': 'Climate Skew',          'def': 'warming biases turtle sex ratios', 'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Hot mommas, cool poppas',
                'explanation': "Many turtles produce females at warm nest temperatures and males at cool temperatures, plasticity tuned by climate.",
            },
            'examTrap': "Wrong: 'TSD is a primitive flaw.' TSD is an EVOLVED adaptation: it works when temperature predicts which sex benefits more.",
            'actions': {
                'quizPrompt':     'Why is temperature-dependent sex determination considered adaptive plasticity?',
                'flashcardFront': 'TSD pivotal temperature?',
                'flashcardBack':  'The threshold temperature producing a 1:1 sex ratio (species specific).',
            },
        },
    },
    'lec7-fitness-landscape': {
        'lecture': 7, 'lectureTitle': 'Selection in Action: Empirical Studies',
        'order': 4, 'chapter': 'Ch 8', 'slideRange': '23-26',
        'v2': {
            'definition': "Fitness landscapes plot fitness as elevation across trait space, Sewall Wright's metaphor for visualizing evolutionary trajectories.",
            'keyTerms': [
                {'term': 'Adaptive Peak',  'def': 'local fitness maximum',         'color': 'coral'},
                {'term': 'Fitness Valley', 'def': 'low fitness intermediate state','color': 'pink'},
                {'term': 'Ridge',          'def': 'connected high fitness path',   'color': 'teal'},
                {'term': 'Topography',     'def': 'shape of fitness landscape',    'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Climb peaks, avoid valleys',
                'explanation': 'Selection pushes populations uphill toward local fitness peaks but cannot cross deep adaptive valleys.',
            },
            'examTrap': "Wrong: 'Selection always reaches the highest peak.' Selection only climbs LOCAL peaks, populations get stuck on suboptimal ridges.",
            'actions': {
                'quizPrompt':     'Why might natural selection fail to find the global fitness optimum?',
                'flashcardFront': 'Who proposed fitness landscapes?',
                'flashcardBack':  'Sewall Wright, in 1932, as a metaphor for evolutionary dynamics.',
            },
        },
    },

    # =====================================================================
    # LEC 8 — ADAPTATION AND EVO-DEVO (Ch 10)
    # =====================================================================
    'lec8-adaptations-intro': {
        'lecture': 8, 'lectureTitle': 'Adaptation and Evo-Devo',
        'order': 1, 'chapter': 'Ch 10', 'slideRange': '1-6',
        'v2': {
            'definition': 'Adaptation is both a heritable trait increasing fitness and the historical process producing such traits.',
            'keyTerms': [
                {'term': 'Trait Adaptation', 'def': 'feature improving current fitness', 'color': 'coral'},
                {'term': 'Process Adaptation','def': 'evolutionary history producing trait', 'color': 'teal'},
                {'term': 'Novel Trait',      'def': 'evolutionarily new feature',        'color': 'purple'},
                {'term': 'Vestigial',        'def': 'reduced ancestral structure',       'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Adaptation: noun and verb',
                'explanation': 'A wing IS an adaptation (noun) and wings BECOME adaptations through selection (verb), one word, two meanings.',
            },
            'examTrap': "Wrong: 'Every trait is an adaptation.' Some traits are byproducts, vestiges, or genetic drift outcomes, not adaptations.",
            'actions': {
                'quizPrompt':     'Distinguish trait adaptation from process adaptation.',
                'flashcardFront': 'Two meanings of adaptation?',
                'flashcardBack':  'A fitness-enhancing trait, AND the process that produced it.',
            },
        },
    },
    'lec8-evo-devo': {
        'lecture': 8, 'lectureTitle': 'Adaptation and Evo-Devo',
        'order': 2, 'chapter': 'Ch 10', 'slideRange': '7-22',
        'v2': {
            'definition': 'Evo-devo studies how regulatory gene networks build body plans, explaining major evolutionary novelty through developmental change.',
            'keyTerms': [
                {'term': 'Hox Genes',           'def': 'body axis patterning switches',  'color': 'teal'},
                {'term': 'Cis Regulation',      'def': 'enhancer change shifts expression', 'color': 'teal'},
                {'term': 'Toolkit Genes',       'def': 'shared developmental gene set',  'color': 'purple'},
                {'term': 'Heterochrony',        'def': 'timing change creates novelty',  'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Same toolkit, different blueprints',
                'explanation': 'Animals share the same developmental toolkit genes; regulatory rewiring builds wildly different body plans.',
            },
            'examTrap': "Wrong: 'New body plans need new genes.' New body plans usually come from REWIRING existing toolkit genes through regulatory mutations.",
            'actions': {
                'quizPrompt':     'How does cis-regulatory mutation produce major morphological change?',
                'flashcardFront': 'What does evo-devo study?',
                'flashcardBack':  'How developmental gene networks evolve to produce body-plan novelty.',
            },
        },
    },
    'lec8-eye-evolution': {
        'lecture': 8, 'lectureTitle': 'Adaptation and Evo-Devo',
        'order': 3, 'chapter': 'Ch 10', 'slideRange': '23-30',
        'v2': {
            'definition': 'Eyes evolved gradually from photosensitive patches through cup, pinhole, and lens stages, with each stage adaptive on its own.',
            'keyTerms': [
                {'term': 'Eyespot',     'def': 'simple photoreceptor patch',     'color': 'purple'},
                {'term': 'Eye Cup',     'def': 'curved light direction sensor',  'color': 'purple'},
                {'term': 'Pax6',        'def': 'master eye development gene',    'color': 'teal'},
                {'term': 'Camera Eye',  'def': 'lens focused image vision',      'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Patch to cup to pinhole to lens',
                'explanation': 'Eye evolution proceeds through four functional stages, each one selectable and useful in its own right.',
            },
            'examTrap': "Wrong: 'Half an eye is useless.' Every intermediate stage detected light and conferred a fitness advantage over having no eye.",
            'actions': {
                'quizPrompt':     'Walk through the four functional stages of eye evolution.',
                'flashcardFront': 'Master gene shared by all eyes?',
                'flashcardBack':  'Pax6, conserved across animals from flies to humans.',
            },
        },
    },
    'lec8-flaws-pleiotropy': {
        'lecture': 8, 'lectureTitle': 'Adaptation and Evo-Devo',
        'order': 4, 'chapter': 'Ch 10', 'slideRange': '31-35',
        'v2': {
            'definition': 'Antagonistic pleiotropy and developmental constraints produce imperfect adaptations because selection cannot redesign organisms from scratch.',
            'keyTerms': [
                {'term': 'Pleiotropy',           'def': 'one gene, multiple effects',     'color': 'teal'},
                {'term': 'Antagonistic',         'def': 'helps one trait, harms another', 'color': 'pink'},
                {'term': 'Developmental Constraint','def': 'history limits what can evolve','color': 'pink'},
                {'term': 'Trade Off',            'def': 'fitness gain offset by loss',    'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Tinker, never redesign',
                'explanation': "Selection can only modify existing structures, never start over, so flaws like the human spine persist.",
            },
            'examTrap': "Wrong: 'Natural selection produces optimal designs.' Selection produces COMPROMISES because of trade-offs, history, and pleiotropy.",
            'actions': {
                'quizPrompt':     'Why is the human back not perfectly designed for upright walking?',
                'flashcardFront': 'Antagonistic pleiotropy?',
                'flashcardBack':  'One gene improving one trait while harming another (trade off).',
            },
        },
    },

    # =====================================================================
    # LEC 9 — COEVOLUTION (Ch 16)
    # =====================================================================
    'lec9-coevolution-intro': {
        'lecture': 9, 'lectureTitle': 'Coevolution',
        'order': 1, 'chapter': 'Ch 16', 'slideRange': '1-5',
        'v2': {
            'definition': 'Coevolution is reciprocal evolutionary change between two or more interacting species, each driving selection on the other.',
            'keyTerms': [
                {'term': 'Reciprocal Selection', 'def': 'each species drives the other', 'color': 'teal'},
                {'term': 'Pairwise',             'def': 'just two species coevolve',     'color': 'purple'},
                {'term': 'Diffuse',              'def': 'whole community coevolves',     'color': 'purple'},
                {'term': 'Coadaptation',         'def': 'matched traits across species', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Two species, one dance',
                'explanation': 'Coevolution requires SELECTION going both ways: one species evolves, the other responds, and the cycle continues.',
            },
            'examTrap': "Wrong: 'Two species evolving together is coevolution.' Coevolution requires RECIPROCAL selection, not just simultaneous evolution.",
            'actions': {
                'quizPrompt':     'Distinguish pairwise from diffuse coevolution.',
                'flashcardFront': 'Coevolution definition?',
                'flashcardBack':  'Reciprocal evolutionary change between two or more interacting species.',
            },
        },
    },
    'lec9-antagonistic-arms': {
        'lecture': 9, 'lectureTitle': 'Coevolution',
        'order': 2, 'chapter': 'Ch 16', 'slideRange': '6-16',
        'v2': {
            'definition': 'Antagonistic coevolution drives escalating arms races, like garter snakes evolving resistance to newt tetrodotoxin in geographic mosaics.',
            'keyTerms': [
                {'term': 'Arms Race',         'def': 'escalating offense and defense',  'color': 'teal'},
                {'term': 'Tetrodotoxin (TTX)','def': 'newt sodium channel blocker',     'color': 'purple'},
                {'term': 'Geographic Mosaic', 'def': 'coevolution varies by location',  'color': 'pink'},
                {'term': 'Resistance Cost',   'def': 'snake speed slows with resistance','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Newt poison, snake immunity, slower snake',
                'explanation': 'Newts make tetrodotoxin, snakes evolve sodium channel resistance, but the resistant snakes pay the cost in speed.',
            },
            'examTrap': "Wrong: 'Arms races escalate forever.' Costs eventually balance benefits, freezing the race or causing local extinction.",
            'actions': {
                'quizPrompt':     'Describe the geographic mosaic of garter snake and newt coevolution.',
                'flashcardFront': 'What toxin do newts use against snakes?',
                'flashcardBack':  'Tetrodotoxin (TTX), a powerful sodium channel blocker.',
            },
        },
    },
    'lec9-mutualistic': {
        'lecture': 9, 'lectureTitle': 'Coevolution',
        'order': 3, 'chapter': 'Ch 16', 'slideRange': '17-20',
        'v2': {
            'definition': 'Mutualistic coevolution produces partnerships where both species benefit, like flowers and pollinators evolving matched traits.',
            'keyTerms': [
                {'term': 'Mutualism',         'def': 'both species gain fitness',     'color': 'coral'},
                {'term': 'Pollinator Syndrome','def': 'flower traits matched to vector','color': 'coral'},
                {'term': 'Reward',            'def': 'nectar and pollen for service', 'color': 'teal'},
                {'term': 'Cheater',           'def': 'takes reward without service',  'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Reward me, I serve you',
                'explanation': 'Plants offer nectar bribes, pollinators carry pollen, neither could thrive alone, both win together.',
            },
            'examTrap': "Wrong: 'Mutualism is always stable.' Cheaters that take rewards without pollinating destabilize mutualisms unless punished or excluded.",
            'actions': {
                'quizPrompt':     'How does cheating threaten mutualistic coevolution?',
                'flashcardFront': 'Pollinator syndrome?',
                'flashcardBack':  'Set of flower traits (color, shape, scent) matched to pollinator type.',
            },
        },
    },
    'lec9-mimicry': {
        'lecture': 9, 'lectureTitle': 'Coevolution',
        'order': 4, 'chapter': 'Ch 16', 'slideRange': '21-29',
        'v2': {
            'definition': 'Mimicry evolves when species converge on warning signals: Batesian mimics fake danger, Mullerian mimics share real danger.',
            'keyTerms': [
                {'term': 'Aposematism',     'def': 'warning coloration of toxins', 'color': 'coral'},
                {'term': 'Batesian Mimicry','def': 'harmless mimics dangerous model', 'color': 'teal'},
                {'term': 'Mullerian Mimicry','def': 'two toxic species share signal','color': 'teal'},
                {'term': 'Frequency Dependence','def': 'mimic rare to stay effective','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Bates fakes, Muller shares',
                'explanation': 'Batesian mimics are LIARS imitating toxic models; Mullerian mimics are HONEST partners sharing one warning.',
            },
            'examTrap': "Wrong: 'Mimicry always benefits both species.' In Batesian mimicry, the model is HARMED because predators eventually attack the warning signal.",
            'actions': {
                'quizPrompt':     'Distinguish Batesian from Mullerian mimicry.',
                'flashcardFront': 'Why must Batesian mimics stay rare?',
                'flashcardBack':  'If too common, predators learn the signal does not always mean danger.',
            },
        },
    },
    'lec9-endosymbiosis': {
        'lecture': 9, 'lectureTitle': 'Coevolution',
        'order': 5, 'chapter': 'Ch 16', 'slideRange': '30-36',
        'v2': {
            'definition': 'Endosymbiosis is intimate coevolution where one organism lives inside another, producing mitochondria, chloroplasts, and insect symbionts.',
            'keyTerms': [
                {'term': 'Endosymbiont',      'def': 'lives inside host cells',       'color': 'purple'},
                {'term': 'Mitochondria',      'def': 'former free-living bacterium',  'color': 'purple'},
                {'term': 'Genome Reduction',  'def': 'symbiont loses unneeded genes', 'color': 'teal'},
                {'term': 'Vertical Transmission','def': 'inherited from mother',       'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Outside swallowed, inside forever',
                'explanation': "An ancient cell ate a bacterium and never digested it; the bacterium became your mitochondria.",
            },
            'examTrap': "Wrong: 'Mitochondria are part of the original cell.' Mitochondria descend from ENGULFED alpha-proteobacteria and still keep their own DNA.",
            'actions': {
                'quizPrompt':     'What evidence shows mitochondria began as free-living bacteria?',
                'flashcardFront': 'Endosymbiotic origin of eukaryotes?',
                'flashcardBack':  'Mitochondria from alpha-proteobacteria, chloroplasts from cyanobacteria.',
            },
        },
    },

    # =====================================================================
    # LEC 10 — SEXUAL SELECTION ORIGINS (Ch 11, slides 1-22)
    # LEC 11 — SPERM COMPETITION (Ch 11, slides 23-45)
    # =====================================================================
    'lec1011-why-sex': {
        'lecture': 10, 'lectureTitle': 'Sexual Selection: Origins and Why Sex',
        'order': 1, 'chapter': 'Ch 11', 'slideRange': '1-13',
        'v2': {
            'definition': 'Sex is costly because males contribute only genes, yet the Red Queen and recombination benefits keep sex universal.',
            'keyTerms': [
                {'term': 'Twofold Cost',    'def': 'males halve population fecundity', 'color': 'pink'},
                {'term': 'Red Queen',       'def': 'race against coevolving parasites','color': 'teal'},
                {'term': 'Recombination',   'def': 'shuffles deleterious mutations',   'color': 'teal'},
                {'term': 'Mullers Ratchet', 'def': 'asexual lineages accumulate mutations','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Run to stay in place',
                'explanation': "The Red Queen runs forever just to stay still; sexual species recombine to outpace evolving parasites.",
            },
            'examTrap': "Wrong: 'Sex evolved for genetic diversity.' Sex is COSTLY; the question is what benefit overcomes the twofold cost of producing males.",
            'actions': {
                'quizPrompt':     'Explain the twofold cost of sex and how the Red Queen resolves it.',
                'flashcardFront': "Muller's ratchet?",
                'flashcardBack':  'Asexual lineages accumulate deleterious mutations because they cannot recombine.',
            },
        },
    },
    'lec1011-anisogamy': {
        'lecture': 10, 'lectureTitle': 'Sexual Selection: Origins and Why Sex',
        'order': 2, 'chapter': 'Ch 11', 'slideRange': '14-22',
        'v2': {
            'definition': 'Anisogamy is the asymmetry between large eggs and small sperm, the gamete-size difference that defines males and females.',
            'keyTerms': [
                {'term': 'Isogamy',           'def': 'gametes equal in size',          'color': 'purple'},
                {'term': 'Anisogamy',         'def': 'big egg, small sperm',           'color': 'purple'},
                {'term': 'Bateman Principle', 'def': 'males vary more in success',     'color': 'teal'},
                {'term': 'Parental Investment','def': 'cost of producing offspring',   'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Big egg defines female',
                'explanation': "Females are simply the sex with bigger gametes; everything else (size, behavior) flows from that asymmetry.",
            },
            'examTrap': "Wrong: 'Males and females are defined by chromosomes.' Males and females are defined by GAMETE SIZE (small vs large), not chromosomes.",
            'actions': {
                'quizPrompt':     'How does anisogamy explain the origin of sexual selection?',
                'flashcardFront': 'Female versus male definition?',
                'flashcardBack':  'Female produces large gametes (eggs); male produces small gametes (sperm).',
            },
        },
    },
    'lec1011-male-female-strategies': {
        'lecture': 11, 'lectureTitle': 'Sexual Selection: Strategies and Conflict',
        'order': 1, 'chapter': 'Ch 11', 'slideRange': '23-37',
        'v2': {
            'definition': 'Males compete for mates while females choose, producing ornaments, leks, sensory bias, and runaway sexual selection on display traits.',
            'keyTerms': [
                {'term': 'Intrasexual Selection','def': 'males fight other males',      'color': 'teal'},
                {'term': 'Intersexual Selection','def': 'females choose mates',         'color': 'teal'},
                {'term': 'Lek',                  'def': 'communal male display arena',  'color': 'purple'},
                {'term': 'Runaway',              'def': 'preference and trait coevolve','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Fight or display',
                'explanation': "Males compete by fighting (intrasexual) or displaying (intersexual) — two paths to the same goal: more matings.",
            },
            'examTrap': "Wrong: 'Female choice is always for honest signals.' Females may pick traits like long tails simply because of pre-existing sensory biases.",
            'actions': {
                'quizPrompt':     'Distinguish intrasexual from intersexual selection with examples.',
                'flashcardFront': 'Runaway sexual selection?',
                'flashcardBack':  'Female preference and male trait coevolve, escalating beyond utility.',
            },
        },
    },
    'lec1011-sperm-competition': {
        'lecture': 11, 'lectureTitle': 'Sexual Selection: Strategies and Conflict',
        'order': 2, 'chapter': 'Ch 11', 'slideRange': '38-45',
        'v2': {
            'definition': 'Sperm competition occurs when females mate with multiple males, selecting for sperm traits and antagonistic male strategies.',
            'keyTerms': [
                {'term': 'Polyandry',       'def': 'female mates multiple males',  'color': 'purple'},
                {'term': 'Sperm Plug',      'def': 'blocks rival fertilization',   'color': 'teal'},
                {'term': 'Cryptic Choice',  'def': 'female biases sperm use',      'color': 'teal'},
                {'term': 'Sexual Conflict', 'def': 'male and female fitness diverge','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Mate, plug, displace, defend',
                'explanation': 'Males evolve plugs, displacement structures, and mate guarding when females mate with multiple partners.',
            },
            'examTrap': "Wrong: 'Sperm competition only happens after mating.' It begins WHEN females mate with multiple males, before AND after copulation.",
            'actions': {
                'quizPrompt':     'How does polyandry drive the evolution of sperm plugs?',
                'flashcardFront': 'Cryptic female choice?',
                'flashcardBack':  'Female reproductive tract biases which sperm fertilizes the egg.',
            },
        },
    },

    # =====================================================================
    # LEC 12 — LIFE HISTORY (Ch 13)
    # =====================================================================
    'lec12-life-history-intro': {
        'lecture': 12, 'lectureTitle': 'Life History Evolution',
        'order': 1, 'chapter': 'Ch 13', 'slideRange': '1-11',
        'v2': {
            'definition': 'Life history is the schedule of birth, growth, reproduction, and death shaped by trade-offs between competing fitness components.',
            'keyTerms': [
                {'term': 'r Strategy',     'def': 'many small fast offspring',   'color': 'teal'},
                {'term': 'K Strategy',     'def': 'few large slow offspring',    'color': 'teal'},
                {'term': 'Trade Off',      'def': 'energy spent here, not there','color': 'coral'},
                {'term': 'Iteroparity',    'def': 'reproduces multiple times',   'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Many cheap kids or few quality',
                'explanation': "r-selected species flood with offspring while K-selected species invest deeply in fewer survivors.",
            },
            'examTrap': "Wrong: 'r and K strategies are absolute categories.' They are ENDPOINTS of a continuum; most species blend both strategies.",
            'actions': {
                'quizPrompt':     'Explain the trade-off between offspring number and offspring quality.',
                'flashcardFront': 'r versus K strategy?',
                'flashcardBack':  'r equals many small fast offspring; K equals few large slow offspring.',
            },
        },
    },
    'lec12-aging': {
        'lecture': 12, 'lectureTitle': 'Life History Evolution',
        'order': 2, 'chapter': 'Ch 13', 'slideRange': '12-27',
        'v2': {
            'definition': 'Senescence evolves because selection weakens with age, allowing late-acting deleterious mutations to accumulate beyond reproduction.',
            'keyTerms': [
                {'term': 'Mutation Accumulation','def': 'late deleterious alleles unfiltered', 'color': 'teal'},
                {'term': 'Antagonistic Pleiotropy','def': 'good early, bad late',         'color': 'teal'},
                {'term': 'Disposable Soma',     'def': 'invest in reproduction over repair', 'color': 'coral'},
                {'term': 'Extrinsic Mortality', 'def': 'predation rate sets aging speed',    'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Selection fades after reproduction',
                'explanation': "Selection cannot remove harmful mutations that act after reproduction is finished, so aging accumulates.",
            },
            'examTrap': "Wrong: 'Aging is wear and tear.' Aging EVOLVES because selection weakens with age, not because cells simply break down over time.",
            'actions': {
                'quizPrompt':     'Why do mice age faster than naked mole rats?',
                'flashcardFront': "Williams' antagonistic pleiotropy theory of aging?",
                'flashcardBack':  'Genes good for early reproduction harm late life and persist anyway.',
            },
        },
    },
    'lec12-sex-allocation': {
        'lecture': 12, 'lectureTitle': 'Life History Evolution',
        'order': 3, 'chapter': 'Ch 13', 'slideRange': '28-41',
        'v2': {
            'definition': "Parental investment and sex allocation are shaped by Trivers-Willard theory and Fisher's principle of equal sex-ratio investment.",
            'keyTerms': [
                {'term': 'Parental Investment',  'def': 'cost per offspring raised',      'color': 'teal'},
                {'term': 'Trivers Willard',      'def': 'good moms favor sons',           'color': 'teal'},
                {'term': "Fisher's Principle",   'def': 'invest 1 to 1 in sexes',         'color': 'coral'},
                {'term': 'Local Mate Competition','def': 'biases ratio toward females',   'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Equal investment, not equal numbers',
                'explanation': "Fisher's principle says parents should INVEST equally in sons and daughters, not necessarily produce equal counts.",
            },
            'examTrap': "Wrong: 'Sex ratios are always 50:50.' They equalize INVESTMENT, not numbers; if sons cost twice as much, expect 2:1 daughter bias.",
            'actions': {
                'quizPrompt':     'How does the Trivers-Willard hypothesis predict offspring sex ratios?',
                'flashcardFront': "Fisher's sex ratio principle?",
                'flashcardBack':  'Parents should invest equally in male and female offspring (1:1 by cost).',
            },
        },
    },

    # =====================================================================
    # LEC 13 — GAME THEORY AND ALTRUISM (Ch 12)
    # =====================================================================
    'lec13-ess-game': {
        'lecture': 13, 'lectureTitle': 'Game Theory, Altruism, and Kin Selection',
        'order': 1, 'chapter': 'Ch 12', 'slideRange': '1-7',
        'v2': {
            'definition': 'An evolutionarily stable strategy (ESS) is a behavior that, once common, cannot be invaded by any rare alternative strategy.',
            'keyTerms': [
                {'term': 'ESS',                  'def': 'uninvadable behavior strategy',      'color': 'teal'},
                {'term': 'Hawk-Dove Game',       'def': 'classic aggression payoff matrix',   'color': 'purple'},
                {'term': 'Frequency Dependence', 'def': 'payoff depends on strategy frequency','color': 'teal'},
                {'term': 'Mixed Strategy',       'def': 'population stable at trait ratio',   'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Stable means uninvadable',
                'explanation': "An ESS is a strategy locked in by frequency dependence: rare alternatives always do worse and disappear.",
            },
            'examTrap': "Wrong: 'ESS means optimal strategy.' ESS means UNINVADABLE in current population, often suboptimal compared to coordinated alternatives.",
            'actions': {
                'quizPrompt':     'Why does hawk-dove produce a stable mix instead of all hawks or all doves?',
                'flashcardFront': 'ESS definition?',
                'flashcardBack':  'A strategy that, when common, no rare mutant strategy can invade.',
            },
        },
    },
    'lec13-group-individual': {
        'lecture': 13, 'lectureTitle': 'Game Theory, Altruism, and Kin Selection',
        'order': 2, 'chapter': 'Ch 12', 'slideRange': '8-13',
        'v2': {
            'definition': 'Selection mostly acts on individuals, not groups, because cheaters within groups exploit altruists faster than group-level selection.',
            'keyTerms': [
                {'term': 'Group Selection',     'def': 'selection between whole groups',  'color': 'teal'},
                {'term': 'Individual Selection','def': 'selection among individuals',     'color': 'teal'},
                {'term': 'Cheater',             'def': 'takes group benefit, free riders','color': 'pink'},
                {'term': 'Levels of Selection', 'def': 'gene, individual, kin, group',    'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Cheaters always invade groups',
                'explanation': "Groups of altruists do better than groups of cheaters, but within any group, cheaters always win.",
            },
            'examTrap': "Wrong: 'Animals act for the good of the species.' Selection acts on INDIVIDUALS; species-level benefit is a misconception called naive group selection.",
            'actions': {
                'quizPrompt':     'Why does naive group selection generally fail?',
                'flashcardFront': 'Why selection mostly acts on individuals?',
                'flashcardBack':  'Cheaters within groups exploit altruists faster than groups can be selected.',
            },
        },
    },
    'lec13-kin-altruism': {
        'lecture': 13, 'lectureTitle': 'Game Theory, Altruism, and Kin Selection',
        'order': 3, 'chapter': 'Ch 12', 'slideRange': '14-21',
        'v2': {
            'definition': "Hamilton's rule rB > C explains altruism: helping relatives spreads helper alleles when benefit times relatedness exceeds cost.",
            'keyTerms': [
                {'term': 'Inclusive Fitness', 'def': 'own plus relatives offspring',     'color': 'teal'},
                {'term': 'r (Relatedness)',   'def': 'fraction of shared alleles',       'color': 'purple'},
                {'term': 'Kin Selection',     'def': 'help spreads via relatives',       'color': 'teal'},
                {'term': 'Eusociality',       'def': 'sterile workers help queen',       'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'rB greater than C',
                'explanation': "Help kin when relatedness times benefit exceeds your own cost, the math behind every altruistic act.",
            },
            'examTrap': "Wrong: 'Altruism is selfless.' Altruism evolves only when it serves the gene's COPIES in relatives (rB greater than C).",
            'actions': {
                'quizPrompt':     "Apply Hamilton's rule to a worker bee giving up reproduction.",
                'flashcardFront': "Hamilton's rule?",
                'flashcardBack':  'rB greater than C: relatedness times benefit must exceed cost for altruism to evolve.',
            },
        },
    },

    # =====================================================================
    # LEC 14 — HISTORY OF LIFE (Ch 3)
    # =====================================================================
    'lec14-age-earth': {
        'lecture': 14, 'lectureTitle': 'History of Life',
        'order': 1, 'chapter': 'Ch 3', 'slideRange': '1-5',
        'v2': {
            'definition': 'Earth is 4.568 billion years old, dated by radiometric decay of uranium and other isotopes in zircon crystals.',
            'keyTerms': [
                {'term': 'Radiometric Dating', 'def': 'isotope decay measures age', 'color': 'teal'},
                {'term': 'Half Life',          'def': 'time for half decay',        'color': 'teal'},
                {'term': 'Zircon',             'def': 'oldest dateable mineral',    'color': 'purple'},
                {'term': 'Deep Time',          'def': 'geological vast time scale', 'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Four point five six eight billion',
                'explanation': "Earth is 4.568 billion years old, time enough for all biological evolution including humans appearing in the last second.",
            },
            'examTrap': "Wrong: 'Carbon-14 dates dinosaurs.' Carbon-14 only works under 60,000 years; older fossils need uranium or potassium isotopes.",
            'actions': {
                'quizPrompt':     'Why do geologists use zircon crystals to date the oldest rocks?',
                'flashcardFront': 'Age of Earth?',
                'flashcardBack':  '4.568 billion years (radiometric dating of zircon crystals).',
            },
        },
    },
    'lec14-origin-life': {
        'lecture': 14, 'lectureTitle': 'History of Life',
        'order': 2, 'chapter': 'Ch 3', 'slideRange': '6-11',
        'v2': {
            'definition': 'Life began through abiogenesis, with Miller-Urey showing amino acids form spontaneously and the RNA world preceding DNA-based life.',
            'keyTerms': [
                {'term': 'Abiogenesis',      'def': 'life from non living chemistry', 'color': 'teal'},
                {'term': 'Miller Urey',      'def': 'lightning made amino acids',     'color': 'purple'},
                {'term': 'RNA World',        'def': 'self replicating RNA first',     'color': 'teal'},
                {'term': 'Hydrothermal Vents','def': 'alternative origin location',   'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'RNA before DNA before protein',
                'explanation': 'RNA can both store info AND catalyze reactions, so it likely arose first as the original self-replicator.',
            },
            'examTrap': "Wrong: 'Life began as DNA.' RNA evolved first because it both stores genetic information AND can catalyze chemical reactions.",
            'actions': {
                'quizPrompt':     'Why does the RNA-world hypothesis precede DNA-based life?',
                'flashcardFront': 'Miller-Urey experiment showed?',
                'flashcardBack':  'Amino acids form spontaneously from inorganic gases plus electricity.',
            },
        },
    },
    'lec14-early-life': {
        'lecture': 14, 'lectureTitle': 'History of Life',
        'order': 3, 'chapter': 'Ch 3', 'slideRange': '12-20',
        'v2': {
            'definition': 'Early life included stromatolite-forming bacteria 3.5 billion years ago, with eukaryotes by 2.1 Gya and animals by 600 Mya.',
            'keyTerms': [
                {'term': 'Stromatolites',     'def': 'layered cyanobacterial mats',     'color': 'purple'},
                {'term': 'LUCA',              'def': 'last universal common ancestor',  'color': 'purple'},
                {'term': 'Eukaryote',         'def': 'cells with nucleus, organelles',  'color': 'coral'},
                {'term': 'Multicellularity',  'def': 'cells cooperate, then specialize','color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Bacteria, archaea, eukaryote, animal',
                'explanation': "Life climbed four major levels of organization across three billion years before animals finally appeared.",
            },
            'examTrap': "Wrong: 'Multicellularity evolved once.' Multicellularity evolved INDEPENDENTLY at least 25 times across plants, animals, fungi, and algae.",
            'actions': {
                'quizPrompt':     'What are stromatolites and why are they important?',
                'flashcardFront': 'When did eukaryotes appear?',
                'flashcardBack':  'About 2.1 billion years ago, via endosymbiosis.',
            },
        },
    },
    'lec14-cambrian-paleozoic': {
        'lecture': 14, 'lectureTitle': 'History of Life',
        'order': 4, 'chapter': 'Ch 3', 'slideRange': '21-30',
        'v2': {
            'definition': 'The Cambrian Explosion (541 Mya) produced almost all major animal body plans, beginning the Paleozoic vertebrate radiation.',
            'keyTerms': [
                {'term': 'Cambrian Explosion','def': 'rapid animal phyla appearance',  'color': 'coral'},
                {'term': 'Burgess Shale',     'def': 'famous Cambrian fossil site',    'color': 'purple'},
                {'term': 'Body Plan',         'def': 'fundamental anatomical layout',  'color': 'purple'},
                {'term': 'Paleozoic',         'def': '541 to 252 million years ago',   'color': 'teal'},
            ],
            'mnemonic': {
                'hook': 'Cambrian: every body plan once',
                'explanation': "Every major animal phylum showed up in a 20-million-year window 541 million years ago, then no new phyla since.",
            },
            'examTrap': "Wrong: 'The Cambrian Explosion was instantaneous.' It spanned roughly 20 million years, fast in geological time but slow in human terms.",
            'actions': {
                'quizPrompt':     'Why is the Cambrian Explosion considered evolutionary unique?',
                'flashcardFront': 'When was the Cambrian Explosion?',
                'flashcardBack':  '541 million years ago, producing nearly all modern animal phyla.',
            },
        },
    },
    'lec14-mesozoic-cenozoic': {
        'lecture': 14, 'lectureTitle': 'History of Life',
        'order': 5, 'chapter': 'Ch 3', 'slideRange': '31-36',
        'v2': {
            'definition': 'The Mesozoic was the age of dinosaurs ending with the K-Pg asteroid impact 66 Mya, opening the Cenozoic mammal radiation.',
            'keyTerms': [
                {'term': 'Mesozoic',         'def': 'age of reptiles and dinosaurs',  'color': 'teal'},
                {'term': 'K-Pg Boundary',    'def': '66 Mya asteroid extinction',     'color': 'coral'},
                {'term': 'Iridium Layer',    'def': 'asteroid impact chemical signature','color': 'purple'},
                {'term': 'Cenozoic',         'def': 'age of mammals and humans',      'color': 'teal'},
            ],
            'mnemonic': {
                'hook': 'Asteroid ends dinos, mammals win',
                'explanation': "A six-mile asteroid struck Yucatan 66 Mya, ending non-avian dinosaurs and opening niches for mammals to radiate.",
            },
            'examTrap': "Wrong: 'All dinosaurs died at K-Pg.' Bird dinosaurs survived and still live today; only NON-avian dinosaurs went extinct.",
            'actions': {
                'quizPrompt':     'What evidence supports the asteroid extinction hypothesis?',
                'flashcardFront': 'When was the K-Pg extinction?',
                'flashcardBack':  '66 million years ago, ending non-avian dinosaurs.',
            },
        },
    },

    # =====================================================================
    # LEC 15 — PHYLOGENETICS (Ch 4)
    # =====================================================================
    'lec15-tree-thinking': {
        'lecture': 15, 'lectureTitle': 'Phylogenetics and Tree Thinking',
        'order': 1, 'chapter': 'Ch 4', 'slideRange': '1-12',
        'v2': {
            'definition': 'Phylogenetic trees diagram evolutionary relationships using tips, nodes, branches, and roots to show common ancestry through time.',
            'keyTerms': [
                {'term': 'Tip',    'def': 'extant species or sample',        'color': 'purple'},
                {'term': 'Node',   'def': 'common ancestor branching point', 'color': 'purple'},
                {'term': 'Clade',  'def': 'ancestor plus all descendants',   'color': 'coral'},
                {'term': 'Root',   'def': 'deepest common ancestor',         'color': 'teal'},
            ],
            'mnemonic': {
                'hook': 'Read trees by topology',
                'explanation': 'A tree shows relationships by branching pattern, not by tip order; rotate any branch and meaning stays.',
            },
            'examTrap': "Wrong: 'Species closer on the page are more related.' Relatedness depends on shared NODES, not visual proximity.",
            'actions': {
                'quizPrompt':     'How do you read a phylogenetic tree to find sister taxa?',
                'flashcardFront': 'Tree definition of clade?',
                'flashcardBack':  'A common ancestor plus all of its descendants (monophyletic group).',
            },
        },
    },
    'lec15-cladistics-synapomorphy': {
        'lecture': 15, 'lectureTitle': 'Phylogenetics and Tree Thinking',
        'order': 2, 'chapter': 'Ch 4', 'slideRange': '13-22',
        'v2': {
            'definition': 'Cladistics builds trees from synapomorphies, shared derived characters that mark monophyletic groups inherited from common ancestors.',
            'keyTerms': [
                {'term': 'Synapomorphy',   'def': 'shared derived character',     'color': 'teal'},
                {'term': 'Plesiomorphy',   'def': 'shared ancestral character',   'color': 'pink'},
                {'term': 'Monophyletic',   'def': 'ancestor and all descendants', 'color': 'coral'},
                {'term': 'Paraphyletic',   'def': 'ancestor but missing descendants','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Synapomorphies build clades',
                'explanation': "Only DERIVED shared traits prove common ancestry; ancestral shared traits like 'has DNA' tell you nothing.",
            },
            'examTrap': "Wrong: 'Reptiles are a valid clade.' Reptiles are PARAPHYLETIC because they exclude birds, which descend from the same ancestor.",
            'actions': {
                'quizPrompt':     'Why are synapomorphies more useful than plesiomorphies for building trees?',
                'flashcardFront': 'Monophyletic versus paraphyletic?',
                'flashcardBack':  'Mono includes ALL descendants; para excludes some descendants of a common ancestor.',
            },
        },
    },
    'lec15-homoplasy-convergence': {
        'lecture': 15, 'lectureTitle': 'Phylogenetics and Tree Thinking',
        'order': 3, 'chapter': 'Ch 4', 'slideRange': '23-29',
        'v2': {
            'definition': 'Parsimony picks the tree requiring fewest character changes, but homoplasy from convergence and reversal can mislead the analysis.',
            'keyTerms': [
                {'term': 'Parsimony',      'def': 'fewest changes wins tree',      'color': 'teal'},
                {'term': 'Homoplasy',      'def': 'similarity not from ancestry',  'color': 'pink'},
                {'term': 'Convergence',    'def': 'independent evolution of trait','color': 'pink'},
                {'term': 'Reversal',       'def': 'derived trait reverts ancestral','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Similarity sometimes lies',
                'explanation': 'Convergence and reversals create matching traits that came from independent origins, not from common ancestry.',
            },
            'examTrap': "Wrong: 'Similar traits always indicate close relatives.' Convergence (dolphins and fish) creates similarity from completely independent evolutionary origins.",
            'actions': {
                'quizPrompt':     'How does convergence violate cladistic assumptions?',
                'flashcardFront': 'Parsimony principle?',
                'flashcardBack':  'Pick the tree requiring the fewest evolutionary changes.',
            },
        },
    },
    'lec15-fins-to-limbs': {
        'lecture': 15, 'lectureTitle': 'Phylogenetics and Tree Thinking',
        'order': 4, 'chapter': 'Ch 4', 'slideRange': '30-37',
        'v2': {
            'definition': 'Tiktaalik is a fish-tetrapod transitional fossil predicted by phylogeny and discovered in 375-million-year-old Devonian rocks.',
            'keyTerms': [
                {'term': 'Tiktaalik',          'def': 'fish with limb like fins', 'color': 'purple'},
                {'term': 'Devonian',           'def': '375 Mya tetrapod origin',  'color': 'purple'},
                {'term': 'Transitional Form',  'def': 'links two body plans',     'color': 'coral'},
                {'term': 'Phylogenetic Prediction','def': 'tree predicts where to dig','color': 'teal'},
            ],
            'mnemonic': {
                'hook': 'Fish wrist, fish neck, fish lung',
                'explanation': "Tiktaalik had a real wrist, neck, and lungs while still living in water, exactly the predicted fish-tetrapod intermediate.",
            },
            'examTrap': "Wrong: 'Transitional fossils are missing.' Tiktaalik was PREDICTED by phylogeny, then found in the predicted age and rock layer.",
            'actions': {
                'quizPrompt':     'How did phylogenetic prediction lead to the discovery of Tiktaalik?',
                'flashcardFront': 'Tiktaalik age and significance?',
                'flashcardBack':  '375 Mya fish-tetrapod transitional form (Devonian period).',
            },
        },
    },
    'lec15-feathers-exaptation': {
        'lecture': 15, 'lectureTitle': 'Phylogenetics and Tree Thinking',
        'order': 5, 'chapter': 'Ch 4', 'slideRange': '38-44',
        'v2': {
            'definition': 'Feathers evolved before flight as insulation or display, then were co-opted for flight, a classic example of exaptation.',
            'keyTerms': [
                {'term': 'Exaptation',         'def': 'old trait, new function',      'color': 'teal'},
                {'term': 'Feathered Dinosaur', 'def': 'fossil with proto-feathers',   'color': 'purple'},
                {'term': 'Archaeopteryx',      'def': '150 Mya bird-like dinosaur',   'color': 'purple'},
                {'term': 'Swim Bladder',       'def': 'lung exapted for buoyancy',    'color': 'coral'},
            ],
            'mnemonic': {
                'hook': 'Old part, new job',
                'explanation': 'Feathers warmed dinosaurs before they ever flew; selection then co-opted them for gliding and flight.',
            },
            'examTrap': "Wrong: 'Feathers evolved for flight.' Feathers evolved FIRST for insulation or display, then were co-opted (exapted) for flight much later.",
            'actions': {
                'quizPrompt':     'Why is exaptation crucial for evolving complex novel traits?',
                'flashcardFront': 'Exaptation example?',
                'flashcardBack':  'Feathers evolved for insulation, then were co-opted for flight.',
            },
        },
    },

    # =====================================================================
    # LEC 16 — SPECIATION AND BIOGEOGRAPHY (promoted from row 14)
    # =====================================================================
    'species-concepts': {
        'lecture': 16, 'lectureTitle': 'Speciation and Biogeography',
        'order': 1, 'chapter': 'Ch 13', 'slideRange': '1-15',
        'v2': {
            'definition': 'Species concepts define what counts as a species, with the biological species concept relying on reproductive isolation between populations.',
            'keyTerms': [
                {'term': 'BSC',                   'def': 'biological species concept', 'color': 'purple'},
                {'term': 'Reproductive Isolation','def': 'barriers prevent gene flow', 'color': 'teal'},
                {'term': 'Allopatric',            'def': 'geographic barrier separates','color': 'teal'},
                {'term': 'Sympatric',             'def': 'speciation without separation','color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Two pools, no flow, two species',
                'explanation': "Biological species are defined by reproductive isolation: no gene flow means independent evolutionary trajectories.",
            },
            'examTrap': "Wrong: 'BSC works for all life.' BSC fails for asexual species, fossils, and ring species: each species concept has limits.",
            'actions': {
                'quizPrompt':     'When does the biological species concept break down?',
                'flashcardFront': 'Allopatric versus sympatric speciation?',
                'flashcardBack':  'Allopatric needs geographic barrier; sympatric occurs without one.',
            },
        },
    },
    'biogeography-extinction': {
        'lecture': 16, 'lectureTitle': 'Speciation and Biogeography',
        'order': 2, 'chapter': 'Ch 14', 'slideRange': '16-30',
        'v2': {
            'definition': 'Biogeography traces how geography and adaptive radiation shape species distributions, while mass extinctions reset diversity globally.',
            'keyTerms': [
                {'term': 'Vicariance',         'def': 'land split divides population', 'color': 'teal'},
                {'term': 'Adaptive Radiation', 'def': 'rapid speciation fills niches', 'color': 'coral'},
                {'term': 'Mass Extinction',    'def': 'global biodiversity collapse',  'color': 'pink'},
                {'term': 'Big Five',           'def': 'five worst extinction events',  'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Big Five: Ord, Dev, Per, Tri, K-Pg',
                'explanation': "Five mass extinctions hit Ordovician, Devonian, Permian, Triassic, and Cretaceous-Paleogene boundaries through Earth's history.",
            },
            'examTrap': "Wrong: 'The K-Pg was the worst extinction.' The PERMIAN-Triassic was Earth's worst, killing roughly 96 percent of marine species.",
            'actions': {
                'quizPrompt':     'How does vicariance generate biogeographic patterns?',
                'flashcardFront': 'Worst mass extinction?',
                'flashcardBack':  'Permian-Triassic (252 Mya), killed about 96 percent of marine species.',
            },
        },
    },

    # =====================================================================
    # LEC 17 — APPLIED EVOLUTION (promoted from row 15)
    # =====================================================================
    'conservation': {
        'lecture': 17, 'lectureTitle': 'Applied Evolution: Medicine, Humans, Conservation',
        'order': 1, 'chapter': 'Ch 8', 'slideRange': '1-10',
        'v2': {
            'definition': 'Humans drive contemporary evolution through hunting, habitat fragmentation, and climate change, often selecting against the very traits we value.',
            'keyTerms': [
                {'term': 'Anthropogenic Selection','def': 'humans as evolutionary force',  'color': 'teal'},
                {'term': 'Trophy Hunting',         'def': 'selects against big horns',     'color': 'pink'},
                {'term': 'Inbreeding Depression',  'def': 'small populations lose fitness','color': 'coral'},
                {'term': 'Genetic Rescue',         'def': 'translocation restores diversity','color': 'teal'},
            ],
            'mnemonic': {
                'hook': 'Hunters shrink the horns',
                'explanation': "Trophy hunters select against big-horned rams; within decades populations evolve smaller horns, the opposite of natural selection.",
            },
            'examTrap': "Wrong: 'Humans don't drive evolution.' Humans are now Earth's strongest selective agent: hunting, fishing, and antibiotics all select within decades.",
            'actions': {
                'quizPrompt':     'Give an example of human-driven contemporary evolution.',
                'flashcardFront': 'Anthropogenic selection example?',
                'flashcardBack':  'Trophy hunting selects against big horns in bighorn sheep within decades.',
            },
        },
    },
    'human-evolution': {
        'lecture': 17, 'lectureTitle': 'Applied Evolution: Medicine, Humans, Conservation',
        'order': 2, 'chapter': 'Ch 17', 'slideRange': '11-25',
        'v2': {
            'definition': 'Humans evolved in Africa about 300,000 years ago, with bipedalism, brain expansion, and culture as our defining derived traits.',
            'keyTerms': [
                {'term': 'Bipedalism',     'def': 'walking on two legs',         'color': 'coral'},
                {'term': 'Australopith',   'def': 'early bipedal ancestor',      'color': 'purple'},
                {'term': 'Encephalization','def': 'brain size relative to body', 'color': 'teal'},
                {'term': 'Introgression',  'def': 'Neanderthal DNA in humans',   'color': 'pink'},
            ],
            'mnemonic': {
                'hook': 'Walk first, brains later',
                'explanation': 'Bipedalism evolved at least four million years ago; large brains came two million years later in Homo.',
            },
            'examTrap': "Wrong: 'Humans evolved from chimps.' Humans and chimps SHARE a common ancestor; neither descended from the other.",
            'actions': {
                'quizPrompt':     'In what order did bipedalism, large brains, and culture evolve?',
                'flashcardFront': 'When did Homo sapiens originate?',
                'flashcardBack':  'About 300,000 years ago in Africa.',
            },
        },
    },
    'evolutionary-medicine': {
        'lecture': 17, 'lectureTitle': 'Applied Evolution: Medicine, Humans, Conservation',
        'order': 3, 'chapter': 'Ch 18', 'slideRange': '26-40',
        'v2': {
            'definition': 'Evolutionary medicine explains why we get sick: pathogen evolution, mismatch with ancestral environments, and trade-offs in our biology.',
            'keyTerms': [
                {'term': 'Antibiotic Resistance', 'def': 'bacteria evolve drug escape',      'color': 'teal'},
                {'term': 'Mismatch Disease',      'def': 'modern environment versus ancient body','color': 'pink'},
                {'term': 'Trade Off',             'def': 'fitness cost of useful trait',     'color': 'coral'},
                {'term': 'Sickle Cell',           'def': 'malaria heterozygote advantage',   'color': 'purple'},
            ],
            'mnemonic': {
                'hook': 'Sick bodies, evolved reasons',
                'explanation': "Disease often reflects evolutionary mismatch, pathogen evolution, or unavoidable trade-offs baked into our biology.",
            },
            'examTrap': "Wrong: 'Sickle cell is just a defective allele.' Sickle cell HETEROZYGOTES resist malaria, a textbook heterozygote-advantage trade-off.",
            'actions': {
                'quizPrompt':     'How does antibiotic resistance illustrate evolution in real time?',
                'flashcardFront': 'Why does sickle cell allele persist?',
                'flashcardBack':  'Heterozygote advantage: carriers resist malaria infection.',
            },
        },
    },
}


def assert_57():
    assert len(V2) == 57, f'expected 57 entries, got {len(V2)}'
    return V2


if __name__ == '__main__':
    print(f'V2 distillations: {len(V2)} entries')
    rows = {}
    for nid, n in V2.items():
        rows.setdefault(n['lecture'], []).append(nid)
    for lec in sorted(rows):
        print(f'  Lec {lec:2d}: {len(rows[lec])} nodes')
