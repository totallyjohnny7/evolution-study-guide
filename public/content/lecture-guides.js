/* Hand-authored lecture guides for BIOL 4230 Evolution.
   Auto-merged by scripts-v2/merge-lecture-guides.py — edit data/lecture-guides/L*.json instead. */
window.MANUAL_LECTURE_GUIDES = {
  "L01": {
    "title": "What Is Evolution? Course Intro",
    "intro": "First lecture frames evolution as the unifying theory of biology — a process of heritable change in populations over generations — and previews the four mechanisms (selection, drift, gene flow, mutation) the rest of the course will dissect.",
    "sections": [
      {
        "letter": "A",
        "title": "Defining evolution",
        "overview": "Evolution is descent with modification — change in the heritable traits of populations across generations. It is a population-level, multi-generational phenomenon, not something that happens to an individual.",
        "key_points": [
          "Evolution = change in allele frequencies in a population over generations.",
          "The unit of evolution is the population, not the individual.",
          "Individuals are selected; populations evolve.",
          "Heritable variation is required for evolutionary change to occur."
        ],
        "key_terms": [
          {
            "term": "Evolution",
            "def": "Change in the heritable traits (allele frequencies) of a population across generations."
          },
          {
            "term": "Population",
            "def": "A group of interbreeding individuals of the same species in a defined area."
          },
          {
            "term": "Heritable variation",
            "def": "Trait differences among individuals that have a genetic basis and can be passed to offspring."
          }
        ],
        "exam_traps": [
          "An individual cannot 'evolve' — even if they change during their lifetime, evolution requires change across generations in a population.",
          "If trait differences are NOT heritable (e.g., purely environmental), selection on those traits produces no evolutionary change."
        ]
      },
      {
        "letter": "B",
        "title": "Why evolution unifies biology",
        "overview": "Dobzhansky's 1973 essay — 'Nothing in biology makes sense except in the light of evolution' — captures the role evolution plays as the explanatory glue across every biological subdiscipline.",
        "key_points": [
          "Theodosius Dobzhansky (1973) wrote the famous essay establishing evolution as biology's unifying theory.",
          "Evolution explains both unity (shared features from common descent) and diversity (lineage-specific adaptations).",
          "Practical applications include antibiotic resistance, vaccine design, conservation biology, and crop improvement."
        ],
        "key_terms": [
          {
            "term": "Common descent",
            "def": "All life on Earth shares a common ancestor; similarities reflect shared inheritance."
          },
          {
            "term": "Adaptation",
            "def": "A heritable trait that increases fitness in a given environment, produced by natural selection."
          }
        ],
        "exam_traps": [
          "'Adaptation' has two meanings — a trait (the noun) AND the process that produces it (the verb). Context matters."
        ]
      },
      {
        "letter": "C",
        "title": "The four evolutionary mechanisms (preview)",
        "overview": "Four forces change allele frequencies. The course spends the next several lectures dissecting each one in turn.",
        "key_points": [
          "Natural selection — non-random; differential survival/reproduction based on heritable trait differences.",
          "Genetic drift — random sampling of alleles; strongest in small populations.",
          "Gene flow — movement of alleles between populations via migration; tends to homogenize.",
          "Mutation — the ultimate source of new genetic variation; random with respect to fitness."
        ],
        "key_terms": [
          {
            "term": "Natural selection",
            "def": "Differential reproductive success based on heritable trait variation; non-random with respect to fitness."
          },
          {
            "term": "Genetic drift",
            "def": "Random change in allele frequencies due to chance sampling, especially in small populations."
          },
          {
            "term": "Gene flow",
            "def": "Movement of alleles between populations through migration of individuals or gametes."
          },
          {
            "term": "Mutation",
            "def": "Heritable change in DNA sequence; the ultimate source of new alleles."
          }
        ],
        "exam_traps": [
          "Mutation is RANDOM with respect to fitness (it doesn't 'know' what's useful), but selection acting on the resulting variation is NON-random.",
          "Drift and selection both change allele frequencies — but only selection systematically increases fitness."
        ]
      }
    ]
  },
  "L02": {
    "title": "Evolutionary Thinking — From Pre-Darwinian Worldviews to Natural Selection",
    "intro": "How biologists came to think about life as a tree, not a ladder. This lecture traces the conceptual road from the Great Chain of Being to Darwin and Wallace, and frames the scientific method (hypothesis vs. theory) that lets evolutionary claims be tested.",
    "sections": [
      {
        "letter": "A",
        "title": "The Great Chain of Being and pre-Darwinian thinking",
        "overview": "Before Darwin, the dominant Western view of life was the Scala Naturae — a fixed hierarchical ladder with humans at the top and 'lower' organisms at the bottom. Species were considered immutable; extinction was not yet recognized as a real phenomenon.",
        "key_points": [
          "The Great Chain of Being arranged organisms in a fixed hierarchy with humans at the apex.",
          "Species were assumed to be immutable — created in their final form, not changing over time.",
          "Extinction was either denied outright or chalked up to local catastrophes; the idea that whole lineages had vanished was controversial well into the 1700s.",
          "There was no concept of 'common ancestry' — similarities between organisms were attributed to a shared design template, not shared descent."
        ],
        "key_terms": [
          {
            "term": "Great Chain of Being (Scala Naturae)",
            "def": "Pre-Darwinian view of life as a fixed hierarchy with humans at the top — non-evolutionary, no shared descent."
          },
          {
            "term": "Immutability of species",
            "def": "The pre-Darwinian assumption that species do not change over time."
          }
        ],
        "exam_traps": [
          "The Great Chain of Being is NOT an evolutionary tree — it is a fixed ladder with no branching, no common ancestry, and no extinction.",
          "Don't confuse the Chain of Being's 'progression toward humans' with evolution. Evolution does not progress toward any goal."
        ]
      },
      {
        "letter": "B",
        "title": "Extinction recognized — William Smith and stratigraphy",
        "overview": "The realization that whole groups of organisms had disappeared came from geology. William Smith showed that fossil sequences in rock layers had a consistent pattern across geography — and that some forms simply stopped appearing in younger rock.",
        "key_points": [
          "William Smith (early 1800s) used fossils + stratigraphy to map rock layers across England.",
          "He showed that distinct fossil assemblages characterize specific rock strata, in a consistent worldwide order — the principle of FAUNAL SUCCESSION.",
          "The disappearance of fossil types from younger strata established extinction as a real phenomenon.",
          "Georges Cuvier independently demonstrated extinction by comparing extinct fossil mammals (like mastodons) to all known living species."
        ],
        "key_terms": [
          {
            "term": "Stratigraphy",
            "def": "The study of rock layers; younger rocks lie atop older ones, and fossils within them mark time."
          },
          {
            "term": "Faunal succession",
            "def": "The principle that distinct fossil assemblages occur in a consistent vertical order in rock strata, allowing rocks to be dated by their fossils."
          },
          {
            "term": "Extinction",
            "def": "The complete disappearance of a species or lineage from Earth."
          }
        ],
        "exam_traps": [
          "The study guide explicitly flags William Smith's role in establishing extinction — be ready to attribute him.",
          "Faunal succession is descriptive (which fossils where) — it doesn't on its own explain WHY species disappeared. Extinction as a concept comes from observing the pattern."
        ]
      },
      {
        "letter": "C",
        "title": "Lamarck, Lyell, and the road to Darwin",
        "overview": "Several thinkers helped clear the conceptual ground before Darwin. Lamarck proposed an evolutionary mechanism (wrong about the details). Lyell argued for deep time and gradual geological change. Both shaped how Darwin framed natural selection.",
        "key_points": [
          "Jean-Baptiste Lamarck (1809) was the first to propose a systematic mechanism of evolution: inheritance of ACQUIRED CHARACTERISTICS — traits acquired during an individual's life are passed to offspring (e.g., the giraffe stretching its neck).",
          "Lamarck was wrong about the mechanism (acquired traits aren't inherited via the standard germline) but right that species change over time.",
          "Charles Lyell argued for UNIFORMITARIANISM — the same gradual processes operating today shaped Earth over enormous spans of time.",
          "Lyell's gift to Darwin: the concept of DEEP TIME — Earth is millions/billions of years old, plenty of time for slow evolutionary change to accumulate."
        ],
        "key_terms": [
          {
            "term": "Inheritance of acquired characteristics (Lamarckism)",
            "def": "Lamarck's proposed mechanism: traits gained during life pass to offspring. Now known to be wrong as a general mechanism."
          },
          {
            "term": "Uniformitarianism",
            "def": "Lyell's principle that observable, gradual processes (erosion, sedimentation) operating over deep time produced Earth's geological features."
          },
          {
            "term": "Deep time",
            "def": "The vast time spans (millions to billions of years) over which Earth's history has unfolded."
          }
        ],
        "exam_traps": [
          "Lamarck is famous as a wrong example, but the study guide calls for matching him to 'inheritance of acquired traits.' Don't dismiss him without naming his contribution.",
          "Lyell was a geologist, not an evolutionary biologist. His contribution to evolution was indirect — providing deep time as a backdrop."
        ]
      },
      {
        "letter": "D",
        "title": "Darwin, Wallace, and natural selection",
        "overview": "Darwin's voyage on the Beagle (1831–1836) and decades of subsequent work led him to natural selection. Alfred Russel Wallace independently arrived at the same idea — and his 1858 letter is what finally pushed Darwin to publish.",
        "key_points": [
          "Charles Darwin developed the theory of evolution by natural selection through observations on the Beagle voyage and later work, especially on Galápagos finches and barnacles.",
          "Darwin's three observations + one inference: (1) populations have heritable variation; (2) more offspring are produced than can survive; (3) survival/reproduction is non-random; → therefore (4) heritable traits associated with higher reproductive success increase in frequency.",
          "Alfred Russel Wallace independently conceived natural selection while working in the Malay Archipelago. His 1858 letter to Darwin spurred the joint Darwin-Wallace paper that year.",
          "Darwin published On the Origin of Species in 1859."
        ],
        "key_terms": [
          {
            "term": "Natural selection",
            "def": "The process by which individuals with heritable trait variants that increase reproductive success leave more offspring, increasing those variants' frequency over generations."
          },
          {
            "term": "Heritability",
            "def": "The proportion of phenotypic variation that is genetically inherited rather than environmental."
          },
          {
            "term": "Selection differential (S)",
            "def": "The difference between the mean trait value of breeders and the mean trait value of the original population."
          }
        ],
        "exam_traps": [
          "The study guide explicitly tests: 'identifying which naturalist spurred Darwin to make his work public' — that's WALLACE, via his 1858 letter.",
          "Natural selection requires variation, heritability, AND differential reproductive success. All three. Missing any one and the population doesn't evolve."
        ]
      },
      {
        "letter": "E",
        "title": "Hypotheses vs. theories — the scientific method",
        "overview": "Lay usage of 'theory' often means 'guess,' but in science it means something quite different. Distinguishing hypothesis from theory is a small but reliably testable item.",
        "key_points": [
          "A HYPOTHESIS is a tentative, testable explanation for an observation — narrow in scope, designed to be falsified.",
          "A SCIENTIFIC THEORY is a well-substantiated, broad explanation supported by a large body of evidence and capable of generating many testable hypotheses.",
          "Evolution is a theory in the strong scientific sense: a unifying explanation supported by molecular, fossil, biogeographic, and experimental evidence.",
          "A good hypothesis is FALSIFIABLE — it specifies observations that would prove it wrong."
        ],
        "key_terms": [
          {
            "term": "Hypothesis",
            "def": "A tentative, testable, falsifiable explanation for an observation."
          },
          {
            "term": "Scientific theory",
            "def": "A broad, well-supported explanation for a major aspect of the natural world; generates testable hypotheses."
          },
          {
            "term": "Falsifiability",
            "def": "The criterion that a scientific claim must specify observations that could prove it wrong."
          }
        ],
        "exam_traps": [
          "'Theory' in everyday language ≠ 'theory' in science. Saying evolution is 'just a theory' confuses the two senses.",
          "A good hypothesis says what observations would falsify it. 'Evolution happens' is too broad to be a hypothesis; 'antibiotic resistance increases when antibiotics are widely used' is testable."
        ]
      }
    ]
  },
  "L03": {
    "title": "Genes and Heritable Variation",
    "intro": "Evolution requires heritable variation. This lecture is the genetics-and-genomics foundation: what genes ARE, how genomes are built, how alleles differ in their phenotypic effects, and how gene expression is regulated at multiple levels.",
    "sections": [
      {
        "letter": "A",
        "title": "Genome architecture — coding vs. noncoding DNA",
        "overview": "Eukaryotic genomes are mostly NOT made of protein-coding genes. The bulk is noncoding DNA — pseudogenes, mobile elements, regulatory sequences, and stretches with no known function. This matters because evolution acts on genome content as a whole.",
        "key_points": [
          "Protein-coding genes typically make up only a small fraction of eukaryotic genomes (humans: ~1–2% of the genome).",
          "Noncoding DNA includes pseudogenes (broken former genes), mobile genetic elements (transposons, retroelements), regulatory sequences, and repetitive DNA.",
          "GENOME SIZE does NOT correlate with organismal complexity (the C-value paradox) — some amoebas have larger genomes than humans.",
          "Pseudogenes are evolutionary fossils — once functional, now not — and provide direct evidence of evolutionary history."
        ],
        "key_terms": [
          {
            "term": "Pseudogene",
            "def": "A nonfunctional sequence resembling a known gene, usually disabled by stop codons, frameshifts, or loss of regulation."
          },
          {
            "term": "Mobile genetic element (MGE)",
            "def": "DNA sequences that can change position within a genome — transposons, retroelements (LINEs, SINEs)."
          },
          {
            "term": "C-value paradox",
            "def": "The observation that genome size does not correlate with organismal complexity."
          }
        ],
        "exam_traps": [
          "Genome size ≠ gene count ≠ complexity. The study guide flags this directly: 'genome size does not necessarily correlate with organismal complexity.'",
          "Pseudogenes ARE part of the genome — they are real DNA, just not functional. Don't exclude them when listing genome contents."
        ]
      },
      {
        "letter": "B",
        "title": "Levels of gene expression regulation",
        "overview": "Cells regulate gene expression at multiple stages — pre-transcriptional, transcriptional, post-transcriptional, and post-translational. Knowing which mechanism acts at which level is a core test item.",
        "key_points": [
          "PRE-TRANSCRIPTIONAL: chromatin structure, histone modification (acetylation, methylation), DNA methylation. Controls whether the gene is even ACCESSIBLE for transcription.",
          "TRANSCRIPTIONAL: transcription factors binding to promoters and enhancers; regulates the rate of mRNA synthesis.",
          "POST-TRANSCRIPTIONAL: alternative splicing of pre-mRNA, microRNA-mediated mRNA degradation, mRNA stability/localization.",
          "POST-TRANSLATIONAL: protein phosphorylation, ubiquitination, proteolytic cleavage, subcellular targeting — alters protein activity AFTER it is made."
        ],
        "key_terms": [
          {
            "term": "DNA methylation",
            "def": "Addition of methyl groups to DNA (typically CpG sites); usually represses transcription. PRE-TRANSCRIPTIONAL regulation."
          },
          {
            "term": "Histone modification",
            "def": "Chemical changes to histone tails (acetylation, methylation) that alter chromatin packing and gene accessibility. PRE-TRANSCRIPTIONAL."
          },
          {
            "term": "MicroRNA (miRNA)",
            "def": "Small noncoding RNA that binds complementary mRNAs to suppress translation or trigger degradation. POST-TRANSCRIPTIONAL."
          },
          {
            "term": "Alternative splicing",
            "def": "Production of multiple mRNA variants from a single gene by including/excluding different exons. POST-TRANSCRIPTIONAL."
          }
        ],
        "exam_traps": [
          "DNA methylation = PRE-transcriptional (controls access). MicroRNA = POST-transcriptional (degrades mRNAs after they're made). Don't mix them up.",
          "Phosphorylation can occur during transcription factor activation (transcriptional) or as a post-translational modification of any protein. Context tells you which level."
        ]
      },
      {
        "letter": "C",
        "title": "Alleles — dominant, recessive, additive",
        "overview": "Alleles are alternative versions of a gene at the same locus. How they interact with one another (dominance) — and how the homozygote/heterozygote phenotypes relate — sets how quickly selection can change allele frequencies.",
        "key_points": [
          "DOMINANT alleles mask the expression of recessive alleles in heterozygotes (Aa shows the A phenotype).",
          "ADDITIVE alleles each contribute incrementally to the phenotype — Aa is intermediate between AA and aa, and the effect scales linearly with copy number.",
          "RECESSIVE beneficial mutations spread SLOWLY from rarity — most copies hide in heterozygotes where they're masked.",
          "DOMINANT beneficial mutations spread FAST — every heterozygote already shows the phenotype.",
          "Additive variance (V_A) is the only variance component that responds predictably to selection (covered more in L05)."
        ],
        "key_terms": [
          {
            "term": "Allele",
            "def": "A specific variant of a gene at a given locus."
          },
          {
            "term": "Dominant",
            "def": "An allele whose phenotype is fully expressed in heterozygotes."
          },
          {
            "term": "Recessive",
            "def": "An allele whose phenotype is hidden in heterozygotes; only expressed when homozygous."
          },
          {
            "term": "Additive",
            "def": "Allelic effects that combine linearly — phenotype is proportional to the dose of the allele."
          },
          {
            "term": "Locus",
            "def": "The chromosomal location of a gene."
          }
        ],
        "exam_traps": [
          "Beneficial RECESSIVE alleles increase slowly when rare (most are in Aa heterozygotes, hidden from selection). Beneficial DOMINANT alleles increase quickly when rare. Selection efficiency depends on dominance.",
          "Don't confuse 'additive' (linear dose-response across copies) with 'codominant' (both alleles' phenotypes are visible in the heterozygote, but not necessarily linearly intermediate)."
        ]
      },
      {
        "letter": "D",
        "title": "Mutation as the source of new variation",
        "overview": "Mutation is the ULTIMATE source of new genetic variation. Selection cannot create new alleles — it can only sort among existing variants. Mutation is random with respect to fitness.",
        "key_points": [
          "Mutations are heritable changes in DNA sequence; they are the only source of NEW genetic variation.",
          "Mutations are RANDOM with respect to fitness — they don't preferentially generate beneficial alleles when those would be useful.",
          "Most mutations are neutral or slightly deleterious; beneficial mutations are rare.",
          "Mutation rate per base per generation in eukaryotes is roughly 10⁻⁸ to 10⁻⁹, but compounded across the whole genome each individual carries dozens of new mutations."
        ],
        "key_terms": [
          {
            "term": "Mutation",
            "def": "Heritable change in DNA sequence — point mutations, insertions, deletions, duplications, inversions, translocations."
          },
          {
            "term": "Mutation rate",
            "def": "The probability of a mutation per base per generation; ~10⁻⁸ to 10⁻⁹ in mammals."
          },
          {
            "term": "Random with respect to fitness",
            "def": "Mutations don't preferentially generate alleles that would be beneficial in the current environment."
          }
        ],
        "exam_traps": [
          "Mutation is random WITH RESPECT TO FITNESS. Mutation rates can vary across the genome (hotspots) and respond to environmental stressors — but the randomness referred to is about fitness-direction, not uniform per-base probability.",
          "Selection requires variation; mutation generates it. Without mutation, selection eventually exhausts genetic variation."
        ]
      }
    ]
  },
  "L04": {
    "title": "Genetic Evolution in Populations — Hardy-Weinberg",
    "intro": "Hardy-Weinberg equilibrium is the null model of population genetics. It predicts genotype frequencies from allele frequencies in an idealized non-evolving population, so any deviation tells you something is going on (selection, drift, mutation, gene flow, or non-random mating).",
    "sections": [
      {
        "letter": "A",
        "title": "Allele frequencies vs genotype frequencies",
        "overview": "An allele frequency is the proportion of a given allele at a locus across the whole population's gene pool. Genotype frequencies are the proportions of homozygotes and heterozygotes.",
        "key_points": [
          "For a biallelic locus with alleles A and a, let p = freq(A), q = freq(a). Then p + q = 1.",
          "Allele frequencies are computed from genotype counts: p = (2·N_AA + N_Aa) / (2·N_total).",
          "Genotype frequencies should add to 1: freq(AA) + freq(Aa) + freq(aa) = 1."
        ],
        "key_terms": [
          {
            "term": "Allele frequency",
            "def": "The proportion of all gene copies in a population that are a given allele."
          },
          {
            "term": "Genotype frequency",
            "def": "The proportion of individuals in a population with a given genotype (e.g., AA, Aa, aa)."
          }
        ],
        "exam_traps": [
          "Don't confuse allele counts with individual counts — each diploid individual contributes TWO allele copies.",
          "Heterozygotes contribute ONE A and ONE a to the allele tally, not two of one."
        ]
      },
      {
        "letter": "B",
        "title": "The Hardy-Weinberg equation",
        "overview": "Under five idealizing assumptions, expected genotype frequencies are p², 2pq, q². The cross-multiplication comes from random union of gametes — Punnett-square logic at the population level.",
        "key_points": [
          "Hardy-Weinberg expectation: p² + 2pq + q² = 1.",
          "p² is the expected frequency of homozygous AA; 2pq of heterozygous Aa; q² of homozygous aa.",
          "The five assumptions: (1) no mutation, (2) no gene flow / migration, (3) no genetic drift (infinite population size), (4) no natural selection, (5) random mating."
        ],
        "key_terms": [
          {
            "term": "Hardy-Weinberg equilibrium (HWE)",
            "def": "The state of a population where allele and genotype frequencies remain constant across generations because none of the five evolutionary forces are acting."
          },
          {
            "term": "Random mating (panmixia)",
            "def": "Each individual is equally likely to mate with any other; no preference based on genotype."
          }
        ],
        "exam_traps": [
          "Hardy-Weinberg gives EXPECTED genotype frequencies under the null. If observed frequencies differ, that's evidence the population is NOT in HWE — i.e., one or more forces are acting.",
          "HWE is achieved in ONE generation of random mating from any starting genotype frequencies (allele freq p stays the same; genotype freq snaps to p²/2pq/q²)."
        ]
      },
      {
        "letter": "C",
        "title": "Detecting deviations and what they mean",
        "overview": "Excess homozygotes vs. excess heterozygotes are diagnostic of different evolutionary processes. Spotting and interpreting deviations is a core exam skill.",
        "key_points": [
          "Excess HOMOZYGOTES (more AA + aa than expected) → suggests inbreeding or population subdivision (Wahlund effect).",
          "Excess HETEROZYGOTES → suggests heterozygote advantage (overdominant selection) or disassortative mating.",
          "Selection against a homozygote shifts allele frequencies AND warps genotype ratios away from HWE.",
          "Drift in small populations causes random departures from HWE that aren't directional."
        ],
        "key_terms": [
          {
            "term": "Inbreeding",
            "def": "Mating between close relatives; increases homozygosity and exposes deleterious recessive alleles (inbreeding depression)."
          },
          {
            "term": "Heterozygote advantage",
            "def": "Heterozygotes have higher fitness than either homozygote; classic example is sickle-cell trait conferring malaria resistance."
          },
          {
            "term": "Wahlund effect",
            "def": "Apparent excess of homozygotes when distinct subpopulations are pooled together as if they were one."
          }
        ],
        "exam_traps": [
          "Selection AGAINST the recessive homozygote (aa) makes a slow change because most a alleles hide in heterozygotes — selection on rare recessives is inefficient.",
          "Inbreeding does NOT change allele frequencies on its own — it only changes genotype frequencies (more homozygotes, fewer heterozygotes)."
        ]
      },
      {
        "letter": "D",
        "title": "Worked computation pattern",
        "overview": "Exam questions often hand you genotype counts and ask you to compute allele frequencies, then expected genotype frequencies under HWE, then compare to observed.",
        "key_points": [
          "Step 1 — count alleles: each AA contributes 2 A; each Aa contributes 1 A and 1 a; each aa contributes 2 a.",
          "Step 2 — compute p and q from the totals.",
          "Step 3 — compute expected counts: N · p², N · 2pq, N · q².",
          "Step 4 — compare expected vs observed; if they don't match, identify which mechanism best explains the pattern."
        ],
        "key_terms": [],
        "exam_traps": [
          "Common arithmetic slip: forgetting to multiply expected genotype FREQUENCIES by N (population size) when comparing to observed COUNTS.",
          "If only allele frequencies are given, you cannot detect HWE deviations — you need genotype counts."
        ]
      }
    ]
  },
  "L05": {
    "title": "Quantitative Genetics, Selection, and Plasticity",
    "intro": "How traits with continuous variation (height, milk yield, beak depth) evolve. This lecture covers phenotypic variance partitioning, heritability, the breeder's equation, and phenotypic plasticity — the ways environment shapes phenotype without changing genotype.",
    "sections": [
      {
        "letter": "A",
        "title": "Quantitative traits and partitioning phenotypic variance",
        "overview": "Quantitative traits are continuously varying (height, mass, fitness components) — many genes plus environment. The total phenotypic variance V_P can be decomposed into components, each with a different evolutionary meaning.",
        "key_points": [
          "Phenotypic variance equation: V_P = V_A + V_D + V_I + V_E.",
          "V_A (ADDITIVE genetic variance) — additive effects of alleles; the only component that responds predictably to selection.",
          "V_D (DOMINANCE variance) — interaction effects of alleles at the same locus.",
          "V_I (EPISTATIC / INTERACTION variance) — interaction effects of alleles at different loci.",
          "V_E (ENVIRONMENTAL variance) — variation in phenotype caused by environment, not heritable."
        ],
        "key_terms": [
          {
            "term": "Quantitative trait",
            "def": "A trait with continuous variation, typically influenced by many genes plus environment (height, weight, fecundity)."
          },
          {
            "term": "V_A — Additive genetic variance",
            "def": "The portion of genetic variance from additive allelic effects; passes predictably from parents to offspring; the engine of response to selection."
          },
          {
            "term": "V_D — Dominance variance",
            "def": "Genetic variance arising from interactions between alleles at the same locus (heterozygote effects)."
          },
          {
            "term": "V_I — Epistatic (interaction) variance",
            "def": "Genetic variance arising from interactions between alleles at different loci."
          },
          {
            "term": "V_E — Environmental variance",
            "def": "Phenotypic variance attributable to environmental differences; not inherited."
          }
        ],
        "exam_traps": [
          "Only V_A responds predictably to selection. V_D and V_I get reshuffled by recombination each generation, so selection on them produces inconsistent gains.",
          "The study guide explicitly asks for the V_P expression — be ready to write it: V_P = V_A + V_D + V_I + V_E."
        ]
      },
      {
        "letter": "B",
        "title": "Heritability — broad-sense vs. narrow-sense",
        "overview": "Heritability is the fraction of phenotypic variance attributable to genetic causes. The narrow-sense version (h²) — using only V_A — is what predicts response to selection.",
        "key_points": [
          "BROAD-SENSE heritability H² = V_G / V_P, where V_G = V_A + V_D + V_I (total genetic variance).",
          "NARROW-SENSE heritability h² = V_A / V_P — uses only the additive component.",
          "h² ranges from 0 (no genetic basis) to 1 (purely genetic, no environmental influence).",
          "h² can be estimated from a PARENT-OFFSPRING REGRESSION — the slope of offspring trait values regressed on the mid-parent value.",
          "h² is a PROPERTY OF A POPULATION IN AN ENVIRONMENT — it changes when allele frequencies or environmental variance change. It is not an intrinsic property of the trait."
        ],
        "key_terms": [
          {
            "term": "Broad-sense heritability (H²)",
            "def": "Total genetic variance divided by total phenotypic variance: V_G / V_P."
          },
          {
            "term": "Narrow-sense heritability (h²)",
            "def": "Additive genetic variance divided by total phenotypic variance: V_A / V_P. Predicts response to selection."
          },
          {
            "term": "Parent-offspring regression",
            "def": "Plot of offspring trait values vs. mid-parent values; slope estimates h²."
          }
        ],
        "exam_traps": [
          "h² (lowercase, narrow-sense) ≠ H² (uppercase, broad-sense). The study guide tests h² because it's the one that predicts evolution.",
          "Heritability is population-and-environment specific. A trait with h² = 0.6 in one population can have h² = 0.2 in another. Don't quote heritability values as universal facts."
        ]
      },
      {
        "letter": "C",
        "title": "The breeder's equation — predicting response to selection",
        "overview": "The breeder's equation R = h² · S links heritability to selection differential to predict the per-generation response to selection. It is the central equation of quantitative genetics.",
        "key_points": [
          "Breeder's equation: R = h² · S.",
          "S (SELECTION DIFFERENTIAL) = mean of breeders − mean of original population. Captures the strength of selection on the phenotype.",
          "R (RESPONSE TO SELECTION) = mean of next generation − mean of current generation. Captures the actual evolutionary change.",
          "Larger S → larger R (selection is stronger). Larger h² → larger R (more of the variance is heritable).",
          "If h² = 0 (no heritability), R = 0 — no response, regardless of how strong the selection."
        ],
        "key_terms": [
          {
            "term": "Selection differential (S)",
            "def": "The phenotypic difference between selected breeders and the original population mean."
          },
          {
            "term": "Response to selection (R)",
            "def": "The change in population mean from one generation to the next, due to selection."
          },
          {
            "term": "Breeder's equation",
            "def": "R = h² · S. Predicts evolutionary response from heritability and selection strength."
          }
        ],
        "exam_traps": [
          "If you select strongly (large S) but h² is near zero, the population doesn't evolve. Heritability is the gating factor.",
          "The breeder's equation works for ONE generation at a time. Iterating across generations requires knowing how V_A and h² change as allele frequencies shift (they don't stay constant)."
        ]
      },
      {
        "letter": "D",
        "title": "Phenotypic plasticity and reaction norms",
        "overview": "A single genotype can produce different phenotypes in different environments. Phenotypic plasticity is the rule, not the exception, and the patterns reveal whether plasticity itself can evolve.",
        "key_points": [
          "PHENOTYPIC PLASTICITY = the ability of a single genotype to produce different phenotypes in different environments.",
          "POLYPHENIC traits = single genotype producing DISCRETE alternative phenotypes (e.g., aphid winged vs. wingless morphs depending on density).",
          "REACTION NORM = a plot of phenotype (y) vs. environment (x) for a given genotype. Sloped lines = plasticity. Horizontal lines = no plasticity (canalization).",
          "GENOTYPE-BY-ENVIRONMENT INTERACTION (G×E, V_G×E) = genotypes differ in HOW they respond to environment (non-parallel reaction norms).",
          "G×E adds to phenotypic variance and can confound heritability estimates."
        ],
        "key_terms": [
          {
            "term": "Phenotypic plasticity",
            "def": "A genotype's capacity to produce different phenotypes in different environments."
          },
          {
            "term": "Reaction norm",
            "def": "A graph of phenotype vs. environment for one genotype."
          },
          {
            "term": "G×E interaction (V_G×E)",
            "def": "Differences among genotypes in their response to environment — reaction norms with different slopes."
          },
          {
            "term": "Polyphenic trait",
            "def": "A genotype producing two or more discrete alternative phenotypes triggered by environmental cues."
          },
          {
            "term": "Canalization",
            "def": "Lack of plasticity — the genotype produces the same phenotype across environments."
          }
        ],
        "exam_traps": [
          "Sloped reaction norms = plasticity. Non-parallel reaction norms = G×E. The study guide asks about interpreting these graphs.",
          "Plasticity is itself heritable and can evolve. A 'plastic' trait isn't the same as a 'non-genetic' trait — the capacity to be plastic is genetic."
        ]
      },
      {
        "letter": "E",
        "title": "Selection vs. evolution — a recurring distinction",
        "overview": "Selection ACTING on a trait does not guarantee EVOLUTION. The link is heritability. This is the integrative concept the study guide returns to repeatedly.",
        "key_points": [
          "Selection produces evolution ONLY when the selected trait has heritable variation (h² > 0).",
          "If trait differences are entirely environmental (V_A = 0), selection can be strong but no evolution occurs.",
          "Evolution = change in allele frequencies across generations. Selection on phenotypes only matters evolutionarily if those phenotypes correlate with genotypes.",
          "This is the bedrock distinction between within-generation differences in survival/reproduction and between-generation evolutionary change."
        ],
        "key_terms": [],
        "exam_traps": [
          "Common exam scenario: selection clearly happens (some individuals reproduce more than others) but the trait is environmentally determined → NO evolutionary response. R = h² · S = 0.",
          "Selection is a within-generation process. Evolution is a between-generation outcome that requires heritability."
        ]
      }
    ]
  },
  "L07": {
    "title": "Empirical Studies of Natural Selection",
    "intro": "How biologists actually MEASURE natural selection in the wild — landmark long-term studies that move 'selection' from theory to observation. Grants' finches, peppered moths, and similar systems are the empirical canon.",
    "sections": [
      {
        "letter": "A",
        "title": "How selection is measured in nature",
        "overview": "To demonstrate natural selection in the field, you need to (1) measure heritable variation in a trait, (2) measure differential survival or reproduction associated with that variation, and (3) ideally see allele-frequency change across generations.",
        "key_points": [
          "Field measurement of selection requires longitudinal data — tracking marked individuals across years.",
          "Selection differential S can be measured directly by comparing the mean trait of breeders to the population mean.",
          "Heritability h² can be estimated from parent-offspring resemblance in the wild.",
          "Predicted response R = h² · S can be checked against the observed change in the next generation."
        ],
        "key_terms": [
          {
            "term": "Selection in the wild",
            "def": "Demonstrated when individuals with certain heritable trait values reproduce more than others in a natural setting."
          }
        ],
        "exam_traps": [
          "Selection in the field can produce TINY per-generation changes that nonetheless add up over decades. Don't dismiss small year-on-year shifts.",
          "Without heritability data, observed differential reproduction is selection but doesn't predict evolution."
        ]
      },
      {
        "letter": "B",
        "title": "Grants' Galápagos finches",
        "overview": "Peter and Rosemary Grant's decades-long study of medium ground finches (Geospiza fortis) on Daphne Major is the gold standard of natural selection in action.",
        "key_points": [
          "After the 1977 drought, large hard seeds dominated the food supply. Birds with deeper, stronger beaks survived better.",
          "The trait (beak depth) was heritable; the next generation had measurably deeper beaks — natural selection caught in real time.",
          "Subsequent wet years reversed the selective pressure (smaller seeds favored), demonstrating that selection direction is environment-contingent.",
          "Hybridization with a related species also introduced variation, showing how gene flow and selection can interact."
        ],
        "key_terms": [
          {
            "term": "Geospiza fortis",
            "def": "The medium ground finch on Daphne Major, focus of the Grants' long-term study."
          },
          {
            "term": "Selection on beak depth",
            "def": "After the 1977 drought, deeper-beaked birds survived better and the next generation had deeper beaks on average."
          }
        ],
        "exam_traps": [
          "The classic finch result is one-direction selection (deeper beaks) followed by reversal in different conditions. Selection can flip direction.",
          "The Grants observed evolution over a few generations — not 'gradualism takes millions of years' as caricatured. Natural selection can act rapidly given strong pressure."
        ]
      },
      {
        "letter": "C",
        "title": "Peppered moths and industrial melanism",
        "overview": "Peppered moths (Biston betularia) shifted from light to dark forms during the Industrial Revolution and back again with pollution control. The textbook case of rapid microevolution under human-caused selection.",
        "key_points": [
          "Pre-industrial: light morph dominant; rested camouflaged on lichen-covered tree trunks.",
          "Industrial-era pollution killed lichen and blackened tree trunks; dark (melanic) form had a survival advantage and rose to >95% in polluted regions.",
          "Selection mechanism: differential bird predation on visible morphs.",
          "After clean-air legislation reduced soot, lichen returned, and the light morph rebounded — selection direction reversed.",
          "The genetic basis is now known: a transposon insertion in the cortex gene."
        ],
        "key_terms": [
          {
            "term": "Industrial melanism",
            "def": "Increase of dark (melanic) morphs in animal populations due to human-caused environmental darkening; classic in Biston betularia."
          },
          {
            "term": "Biston betularia",
            "def": "The peppered moth species in which industrial melanism was documented."
          }
        ],
        "exam_traps": [
          "The peppered moth case is sometimes attacked as bad evidence; modern replication of Kettlewell's experiments confirms differential predation does drive the morph frequencies.",
          "The selective agent is bird predation on resting moths — not direct toxicity of pollutants."
        ]
      },
      {
        "letter": "D",
        "title": "Other documented examples — flu, antibiotics, domestication",
        "overview": "Beyond classic natural systems, human activities provide many real-time tests of selection: pathogens evolving resistance, domesticated species evolving under artificial selection.",
        "key_points": [
          "Influenza evolves antigenic variation rapidly under selection from host immune systems and (where used) antiviral drugs.",
          "Antibiotic resistance in bacteria is a textbook case of strong, directional natural selection by humans.",
          "Domestication is artificial selection — humans choose breeders. Greyhounds bred for speed show measurable evolution of sprint biomechanics over decades.",
          "These cases share a structure: heritable variation + strong directional selection → rapid measurable change."
        ],
        "key_terms": [
          {
            "term": "Antibiotic resistance",
            "def": "Evolution of bacteria able to survive antibiotic exposure; driven by selection on rare resistant variants in large populations."
          },
          {
            "term": "Artificial selection",
            "def": "Selection in which humans (rather than the natural environment) determine which individuals reproduce."
          }
        ],
        "exam_traps": [
          "Antibiotic resistance is NOT caused by the antibiotic mutating bacteria. The mutations occur randomly; the antibiotic selects existing variants.",
          "Artificial selection follows the same logic as natural selection — the only difference is who/what is doing the selecting."
        ]
      }
    ]
  },
  "L08": {
    "title": "Complex Adaptations",
    "intro": "How complex traits — eyes, wings, body plans — evolve through stepwise mutations, regulatory changes, and gene-network conservation. This lecture is the EVO-DEVO chapter, integrating molecular biology with classical evolutionary thinking.",
    "sections": [
      {
        "letter": "A",
        "title": "Adaptation as both trait and process",
        "overview": "The word 'adaptation' has two meanings: a trait that has been shaped by past selection, AND the process by which selection produces such traits. Complex adaptations build incrementally — they do not appear in their finished form.",
        "key_points": [
          "Adaptation (noun) = a heritable trait whose current form is the product of past natural selection in service of some function.",
          "Adaptation (verb) = the process by which selection improves fit between organism and environment.",
          "Complex adaptations arise through MANY small mutational steps, each conferring some fitness advantage along the way.",
          "Each intermediate stage must itself be functional and selectively advantageous — selection cannot 'plan ahead.'"
        ],
        "key_terms": [
          {
            "term": "Adaptation",
            "def": "Either a trait shaped by past selection (noun) OR the process producing such traits (verb)."
          },
          {
            "term": "Gradual evolution",
            "def": "Complex traits accumulate from many small mutational changes, each itself favorable."
          }
        ],
        "exam_traps": [
          "The classic 'half an eye is useless' objection ignores that early eyes are not failed full eyes — they are simpler light-detecting structures with their own value.",
          "Selection works on what's available. A trait can be 'good enough' rather than perfect — historical contingency leaves limits."
        ]
      },
      {
        "letter": "B",
        "title": "Evolution of the vertebrate eye — gradual stepwise model",
        "overview": "The vertebrate eye is the textbook example of complex adaptation evolving through functional intermediates. Each step (light-sensitive patch → cup → pinhole → lensed eye) is itself useful.",
        "key_points": [
          "Stage 1: light-sensitive patch — distinguishes light from dark; useful for circadian rhythms and predator detection.",
          "Stage 2: cupped patch — adds directional sensitivity; can detect WHERE light comes from.",
          "Stage 3: pinhole eye (e.g., Nautilus) — narrows the aperture, producing a crude image without a lens.",
          "Stage 4: lens added — focuses light; sharper image. Lenses likely evolved from co-opted crystallin proteins.",
          "Eyes have evolved INDEPENDENTLY at least 40 times across animals — convergent solutions to a common selective problem."
        ],
        "key_terms": [
          {
            "term": "Stepwise eye evolution",
            "def": "The gradual elaboration from light-sensitive patch to cup to pinhole to lensed eye, each step functional."
          },
          {
            "term": "Convergent evolution of eyes",
            "def": "Eyes have arisen independently in many animal lineages; the camera eye of vertebrates and cephalopods is the classic case."
          }
        ],
        "exam_traps": [
          "The vertebrate camera eye and the cephalopod camera eye look superficially similar but evolved independently — convergent, not homologous.",
          "Each eye-evolution stage is documented in a living organism today (flatworm patches, Nautilus pinhole, etc.). The intermediates are not hypothetical."
        ]
      },
      {
        "letter": "C",
        "title": "Regulatory networks and gene duplication",
        "overview": "A lot of evolutionary novelty comes from RE-WIRING existing genes rather than inventing new ones. Mutations in regulatory regions, gene duplication followed by sub- or neofunctionalization, and changes in expression timing/location all reshape phenotype without changing the underlying protein-coding repertoire.",
        "key_points": [
          "Mutations in cis-regulatory elements (enhancers, promoters) can reshape WHEN and WHERE a gene is expressed without changing the protein.",
          "Gene duplication produces redundant copies — one can retain the original function while the other evolves a new role (NEOFUNCTIONALIZATION) or a subset of the old role (SUBFUNCTIONALIZATION).",
          "Many adaptations are 'tinkering' on conserved gene networks rather than de novo invention.",
          "PROTEIN PROMISCUITY — proteins often have weak side-activities that can be co-opted and refined into new primary functions."
        ],
        "key_terms": [
          {
            "term": "Cis-regulatory mutation",
            "def": "Mutation in a regulatory sequence (enhancer, promoter) that alters when/where a gene is expressed without changing the protein."
          },
          {
            "term": "Gene duplication",
            "def": "Production of an extra copy of a gene; relaxed selection on the duplicate enables new function evolution."
          },
          {
            "term": "Neofunctionalization",
            "def": "One copy of a duplicated gene evolves a novel function while the other retains the original."
          },
          {
            "term": "Subfunctionalization",
            "def": "Both copies of a duplicated gene specialize on different subsets of the ancestral function."
          },
          {
            "term": "Protein promiscuity",
            "def": "Proteins often have weak side-activities; selection can refine these into new primary functions."
          }
        ],
        "exam_traps": [
          "Cis-regulatory evolution is a major route to morphological novelty — Hox-gene expression changes reshape body plans without changing the Hox proteins themselves.",
          "Don't confuse subfunctionalization with neofunctionalization. Sub: each copy does part of the original. Neo: one copy gains a new function."
        ]
      },
      {
        "letter": "D",
        "title": "Heterochrony — changes in developmental timing",
        "overview": "Many morphological differences across species reflect changes in WHEN developmental processes occur, not WHAT they do. Speeding up, slowing down, or shifting the onset of a process produces dramatically different adult forms.",
        "key_points": [
          "HETEROCHRONY = evolutionary change in the relative TIMING or RATE of developmental events.",
          "Examples: paedomorphosis (juvenile features retained in adults — axolotl salamander), peramorphosis (extension of growth past ancestral state — large antlers).",
          "Small changes in timing (a few hours of extra cell proliferation) can produce dramatic morphological differences.",
          "Heterochronic changes often have a simple genetic basis — a few mutations in regulatory genes."
        ],
        "key_terms": [
          {
            "term": "Heterochrony",
            "def": "Evolutionary change in the timing or rate of developmental events between species."
          },
          {
            "term": "Paedomorphosis",
            "def": "Retention of juvenile features in the adult form (e.g., axolotl reproduces while still in larval form)."
          },
          {
            "term": "Peramorphosis",
            "def": "Extension of development past the ancestral end-point, producing more derived adult forms."
          }
        ],
        "exam_traps": [
          "Heterochrony explains a lot of variation among closely related species without invoking many new genes.",
          "Don't conflate heterochrony with heterotopy (changes in WHERE in the body something develops). Different concept, often paired."
        ]
      },
      {
        "letter": "E",
        "title": "Hox genes and conserved developmental networks",
        "overview": "Hox genes encode transcription factors that pattern the anterior-posterior axis of bilaterian animals. They are deeply conserved across phyla — the same Hox toolkit patterns flies, mice, and humans.",
        "key_points": [
          "Hox genes are clustered in a chromosomal arrangement that mirrors their expression pattern along the body axis (COLINEARITY).",
          "Hox proteins are transcription factors that turn on segment-specific developmental programs.",
          "The same Hox genes pattern the body axes of vastly different animals — flies, mice, humans — testifying to deep evolutionary conservation.",
          "Differences in WHERE Hox genes are expressed (regulatory evolution) underlie many morphological differences across species.",
          "Hox-cluster duplications correlate with major body-plan transitions (the vertebrate genome has 4 Hox clusters; invertebrates typically have 1)."
        ],
        "key_terms": [
          {
            "term": "Hox gene",
            "def": "Member of a family of transcription factors that pattern the anterior-posterior body axis in bilaterian animals."
          },
          {
            "term": "Colinearity",
            "def": "The arrangement of Hox genes along the chromosome matches their expression order along the body axis."
          },
          {
            "term": "Conservation of developmental networks",
            "def": "Core gene-regulatory networks (Hox, Pax, Wnt) are shared across distantly related animals — evidence of deep common ancestry."
          }
        ],
        "exam_traps": [
          "Hox-gene CONSERVATION across phyla is the headline. Differences in body plan come largely from differences in REGULATION, not from new Hox proteins.",
          "Don't say Hox genes 'cause' segments. They specify segment IDENTITY — what each segment becomes — given an underlying segmentation process."
        ]
      },
      {
        "letter": "F",
        "title": "Imperfect adaptation — limits and constraints",
        "overview": "Selection produces traits that are 'good enough,' not optimal. Historical legacy, developmental constraints, and trade-offs leave fingerprints of imperfection — and those imperfections are often the strongest evidence of evolution.",
        "key_points": [
          "Adaptations are constrained by history — selection can only modify what's already there.",
          "Vestigial structures (whale pelvis, human appendix, ostrich wings) reflect ancestral function with no current use.",
          "Trade-offs — improving one trait often comes at the cost of another (running speed vs. heat dissipation).",
          "The vertebrate retina has the photoreceptors BACKWARDS (light passes through neurons before reaching them) — a historical accident, not a design choice."
        ],
        "key_terms": [
          {
            "term": "Vestigial structure",
            "def": "A structure that retains ancestral form but has lost most or all of its original function."
          },
          {
            "term": "Trade-off",
            "def": "Improving one trait comes at the cost of reduced performance in another."
          },
          {
            "term": "Constraint",
            "def": "Historical or developmental factors that limit what selection can produce."
          }
        ],
        "exam_traps": [
          "Imperfections are powerful evidence of evolution. A designed system would not have a blind spot; an evolved one inherits its 'mistakes.'",
          "'Good enough' is the right framing — selection lifts fitness, but is not an optimization algorithm with foresight."
        ]
      }
    ]
  },
  "L09": {
    "title": "Coevolution",
    "intro": "Coevolution is reciprocal evolutionary change in two interacting species — each lineage's adaptations are evolutionary responses to the other. It produces arms races, mutualisms, and the geographic mosaic of selection.",
    "sections": [
      {
        "letter": "A",
        "title": "Defining reciprocal coevolution",
        "overview": "Coevolution is not just any pair of species coexisting — it requires that adaptations in one lineage drive adaptive responses in the other, in a feedback loop.",
        "key_points": [
          "Coevolution = reciprocal evolutionary change between two (or more) interacting lineages, each responding to selective pressure from the other.",
          "Coexistence alone is not coevolution; the interaction must shape heritable trait change in both directions.",
          "The interaction can be antagonistic (predator-prey, host-parasite) or mutualistic (pollinators-flowers)."
        ],
        "key_terms": [
          {
            "term": "Coevolution",
            "def": "Reciprocal evolutionary change in two or more interacting species driven by selective pressures each imposes on the others."
          },
          {
            "term": "Reciprocal selection",
            "def": "Selection imposed by one species on another, which then imposes selection back on the first."
          }
        ],
        "exam_traps": [
          "Mere ecological association ≠ coevolution. The textbook bar is: changes in species A drive changes in species B, which drive further changes in A.",
          "Convergent evolution (similar solutions in unrelated lineages) is NOT coevolution — there's no reciprocal feedback."
        ]
      },
      {
        "letter": "B",
        "title": "Antagonistic arms races",
        "overview": "When predator-prey or host-parasite interactions persist, each side evolves countermeasures, which selects for new adaptations in the other side, in an open-ended escalation.",
        "key_points": [
          "Classic case: rough-skinned newts (Taricha) produce tetrodotoxin (TTX); garter snakes (Thamnophis) evolve TTX-resistant sodium channels.",
          "Geographic variation is striking: where snakes are highly resistant, newts are highly toxic; where snakes are sensitive, newts are weakly toxic.",
          "Arms races can be asymmetric — one side may 'win' temporarily, with the other lagging behind in evolutionary response time."
        ],
        "key_terms": [
          {
            "term": "Coevolutionary arms race",
            "def": "Reciprocal escalation of offense/defense traits in interacting species, driven by ongoing antagonistic selection."
          },
          {
            "term": "Tetrodotoxin (TTX)",
            "def": "Potent neurotoxin produced by newts that blocks voltage-gated sodium channels; basis of the newt-snake arms race."
          }
        ],
        "exam_traps": [
          "Arms races don't always escalate forever — fitness costs (e.g., snake speed cost of TTX resistance) can cap the escalation.",
          "Variation across geography is the key signature of a true arms race; uniform 'one-size-fits-all' adaptations argue against ongoing coevolution."
        ]
      },
      {
        "letter": "C",
        "title": "Mutualistic coevolution",
        "overview": "Mutualisms are coevolutionary too: each partner's traits are adapted to the other, and selection on one drives change in the other in a cooperative direction.",
        "key_points": [
          "Pollinator-plant mutualisms (e.g., long-tongued moths and long-spurred orchids — Darwin's prediction) show co-adapted morphology.",
          "Endosymbiosis (mitochondria from ancestral alphaproteobacteria, chloroplasts from cyanobacteria) is the deepest mutualism — now obligate.",
          "Mutualisms can break down or shift to parasitism if cost/benefit balance changes."
        ],
        "key_terms": [
          {
            "term": "Mutualism",
            "def": "An interaction in which both species gain net fitness benefit."
          },
          {
            "term": "Endosymbiosis",
            "def": "One organism living inside another; classic origin of eukaryotic mitochondria and plastids."
          }
        ],
        "exam_traps": [
          "Mutualists often cheat — selection favors taking benefits without paying costs. Stable mutualisms typically have enforcement mechanisms.",
          "Mutualism is not 'cooperation for the good of the species' — each partner is selected for individual fitness; mutual benefit is a coincidence of interests."
        ]
      },
      {
        "letter": "D",
        "title": "Mimicry — Batesian vs. Müllerian",
        "overview": "Mimicry is a coevolutionary product where one species' phenotype evolves to resemble another. The two flavors differ in who pays the cost.",
        "key_points": [
          "Batesian mimicry — a HARMLESS mimic resembles a HARMFUL model; mimic gains protection without bearing the cost of being toxic. Mimic must stay rare or predators learn the trick.",
          "Müllerian mimicry — multiple HARMFUL species converge on a shared warning signal; predators learn 'this color = bad' faster, benefiting all.",
          "Both are products of frequency-dependent selection by shared predators."
        ],
        "key_terms": [
          {
            "term": "Batesian mimicry",
            "def": "A palatable species evolves to resemble an unpalatable model species, gaining protection from predators."
          },
          {
            "term": "Müllerian mimicry",
            "def": "Multiple unpalatable species converge on a similar warning signal, sharing the cost of educating predators."
          },
          {
            "term": "Aposematism",
            "def": "Conspicuous warning coloration in unpalatable or dangerous species."
          }
        ],
        "exam_traps": [
          "Batesian mimicry breaks down at high mimic-to-model ratios — predators encounter the harmless mimic too often and stop avoiding the warning signal.",
          "Müllerian mimicry is technically convergent evolution AND coevolution — both species evolve toward each other's signal."
        ]
      },
      {
        "letter": "E",
        "title": "Geographic Mosaic Theory of Coevolution",
        "overview": "Thompson's framework: coevolutionary outcomes vary across geography because local ecological conditions tilt the cost/benefit balance differently in different places.",
        "key_points": [
          "Coevolution happens in 'hotspots' (intense reciprocal selection) and 'coldspots' (weak or no reciprocal selection).",
          "Gene flow between hotspots and coldspots, plus local trait evolution, generates a mosaic of coevolutionary states across the species' range.",
          "Predictions: trait values mismatched in some places (showing the mosaic), no single 'optimal' coevolutionary outcome."
        ],
        "key_terms": [
          {
            "term": "Geographic Mosaic Theory of Coevolution",
            "def": "Thompson's hypothesis that coevolution proceeds at different rates and in different directions across a species' geographic range, producing spatially variable trait combinations."
          }
        ],
        "exam_traps": [
          "Mosaic theory predicts trait MISMATCH in some areas — this is evidence FOR ongoing coevolution, not against it.",
          "Don't confuse the geographic mosaic with simple local adaptation; mosaic theory specifically requires reciprocal feedback between species."
        ]
      }
    ]
  },
  "L11": {
    "title": "Sex and Sexual Selection",
    "intro": "Why does sex exist at all, given its costs? Once it exists, why do males and females differ so dramatically? This lecture covers the evolution of sexual reproduction, the origin of anisogamy, and the consequences — sexual selection, sexual conflict, sperm competition.",
    "sections": [
      {
        "letter": "A",
        "title": "The cost of sex and why sex evolved anyway",
        "overview": "Sexual reproduction has obvious costs (the 'twofold cost of males,' searching for mates, recombination breaking up good gene combinations) — yet sex is widespread. The benefits must outweigh these costs.",
        "key_points": [
          "TWOFOLD COST OF SEX (Maynard Smith): in sexual species, males don't directly produce offspring, so a sexual mother passes on only HALF as many genes per offspring as an asexual one would.",
          "BENEFIT 1 — Genetic diversity through recombination: sexual reproduction shuffles alleles, creating new combinations selection can act on.",
          "BENEFIT 2 — MULLER'S RATCHET: in asexual lineages, deleterious mutations accumulate irreversibly; sex purges them via recombination.",
          "BENEFIT 3 — RED QUEEN HYPOTHESIS: parasites coevolve rapidly with hosts; sexual recombination lets hosts 'run faster' to stay ahead of parasites.",
          "BENEFIT 4 — Sib competition reduction: sexual offspring are genetically diverse, reducing competition among siblings for the same niche."
        ],
        "key_terms": [
          {
            "term": "Twofold cost of sex",
            "def": "Sexual females produce half the gene-copies per offspring that asexual ones would, because they share parentage with males."
          },
          {
            "term": "Muller's ratchet",
            "def": "In asexual populations, deleterious mutations accumulate over generations; without recombination, the mutation-free class is irreversibly lost."
          },
          {
            "term": "Red Queen hypothesis",
            "def": "Sex provides genetic novelty needed to keep up with rapidly evolving parasites; named after Lewis Carroll's Red Queen ('it takes all the running you can do, to keep in the same place')."
          }
        ],
        "exam_traps": [
          "The 'twofold cost' is sometimes phrased as the cost of MALES, sometimes the cost of SEX. The cost is real either way — sexual mothers transmit half the gene copies per offspring vs. asexual.",
          "Muller's ratchet specifically requires that recombination be ABSENT. Bacteria recombine via horizontal gene transfer and can purge mutations by other routes."
        ]
      },
      {
        "letter": "B",
        "title": "Anisogamy — the foundation of male and female",
        "overview": "ANISOGAMY = unequal gamete sizes. Females (by definition) produce few large gametes (eggs); males produce many small gametes (sperm). This asymmetry is the foundation of nearly all sex differences.",
        "key_points": [
          "ANISOGAMY = unequal gamete sizes; the OPERATIONAL DEFINITION of male and female (rather than secondary sex characteristics).",
          "Female = the sex that makes the larger, costlier gamete; male = the sex with the smaller, cheaper gamete.",
          "Asymmetric gamete investment leads to asymmetric reproductive strategies: females typically more selective, males typically compete for mates.",
          "Anisogamy evolved in the deep past as a stable evolutionary endpoint of disruptive selection on gamete size."
        ],
        "key_terms": [
          {
            "term": "Anisogamy",
            "def": "Unequal gamete sizes — the foundation of biological sex differences."
          },
          {
            "term": "Isogamy",
            "def": "Equal-sized gametes — found in some algae and fungi; the ancestral state from which anisogamy evolved."
          }
        ],
        "exam_traps": [
          "Sex is defined by GAMETE SIZE, not by secondary sex characteristics, behavior, or chromosomes. Don't define 'female' as 'the one that nurtures' — that's downstream of anisogamy.",
          "Anisogamy is not 'why' sex exists; it's a feature of HOW sex is organized once it exists."
        ]
      },
      {
        "letter": "C",
        "title": "Sexual selection — Darwin's second mechanism",
        "overview": "Sexual selection is selection on traits that increase MATING success rather than survival. It explains otherwise-puzzling traits (peacock tails, antlers) that reduce survival.",
        "key_points": [
          "SEXUAL SELECTION = selection arising from competition for mates, distinct from survival selection (though both fall under 'natural selection' in a broad sense).",
          "INTRASEXUAL selection (male-male competition): direct contests between same-sex individuals for access to mates. Produces weapons, large body size in the more competitive sex.",
          "INTERSEXUAL selection (mate choice, typically female choice): one sex chooses mates based on signal traits. Produces ornaments — peacock tails, bird songs.",
          "Sexual selection can OPPOSE survival selection: showy ornaments attract mates AND predators. Net fitness = mating gain − survival cost.",
          "FISHERIAN RUNAWAY: an arbitrary preference for a trait can amplify itself if 'sexy' offspring inherit both the trait and the preference (positive feedback)."
        ],
        "key_terms": [
          {
            "term": "Sexual selection",
            "def": "Selection for traits increasing mating success rather than survival."
          },
          {
            "term": "Intrasexual selection",
            "def": "Same-sex competition for mates (e.g., male-male combat)."
          },
          {
            "term": "Intersexual selection",
            "def": "Mate choice — one sex selects partners based on signal traits."
          },
          {
            "term": "Sexual dimorphism",
            "def": "Difference in form between males and females; often a product of sexual selection."
          }
        ],
        "exam_traps": [
          "Sexual selection IS a form of natural selection — Darwin distinguished them but they share the same logic of differential reproduction.",
          "Sexually selected traits (peacock tails) often REDUCE survival. Their fitness gain comes from mating, which more than offsets the survival cost."
        ]
      },
      {
        "letter": "D",
        "title": "Sexual conflict and sperm competition",
        "overview": "Male and female evolutionary interests often diverge. Sexual CONFLICT — selection pressures pulling males and females in different directions — drives much of the elaborate biology of mating.",
        "key_points": [
          "SEXUAL CONFLICT: males benefit from many matings; females typically benefit from FEW matings with HIGH-quality partners. Their interests diverge.",
          "SPERM COMPETITION: when females mate with multiple males, sperm from different males compete to fertilize her eggs. Drives evolution of large testes, long sperm, mating plugs, and sperm-removal devices.",
          "Cryptic FEMALE choice: females can bias paternity post-copulation through reproductive-tract physiology.",
          "ANTAGONISTIC COEVOLUTION: an arms race within species — male traits coercing females, female traits resisting. Examples: ducks (sexually antagonistic genital coevolution), bedbugs (traumatic insemination).",
          "Sexual conflict can drive RAPID evolutionary change in reproductive structures."
        ],
        "key_terms": [
          {
            "term": "Sexual conflict",
            "def": "Mismatch between the reproductive interests of males and females, generating opposing selection pressures."
          },
          {
            "term": "Sperm competition",
            "def": "Competition between sperm from different males to fertilize the same female's eggs."
          },
          {
            "term": "Cryptic female choice",
            "def": "Female biasing paternity after mating, via reproductive-tract mechanisms."
          },
          {
            "term": "Antagonistic coevolution",
            "def": "Reciprocal evolutionary change between sexes (or between species) driven by conflicting interests."
          }
        ],
        "exam_traps": [
          "Sexual conflict is INTRA-species coevolution — males and females are members of the same species and yet are evolutionary antagonists.",
          "Sperm competition implies polyandry (multiple mating by females). In strictly monogamous species, sperm competition is weak."
        ]
      }
    ]
  },
  "L12": {
    "title": "Life History Evolution",
    "intro": "Life history is the schedule of an organism's birth, growth, reproduction, and death. Selection cannot maximize all these at once — trade-offs between traits force compromises, and the form those compromises take depends on the environment.",
    "sections": [
      {
        "letter": "A",
        "title": "Trade-offs in energy allocation",
        "overview": "An organism has finite resources and time. Energy spent on growth cannot be spent on reproduction; reproduction now reduces resources available for survival and future reproduction.",
        "key_points": [
          "Life-history trade-offs: growth vs. reproduction, current vs. future reproduction, offspring number vs. offspring size.",
          "These trade-offs are physiological constraints — selection cannot break them, only navigate them.",
          "OPTIMAL allocation depends on the environment: high adult survival favors investment in future reproduction; low adult survival favors current reproduction.",
          "Reaction norms for life-history traits show context-dependent allocation."
        ],
        "key_terms": [
          {
            "term": "Life history",
            "def": "The schedule of major events in an organism's life — age at maturity, fecundity, longevity, reproductive timing."
          },
          {
            "term": "Trade-off",
            "def": "An inverse relationship between two fitness-related traits enforced by limited resources or physiological constraints."
          },
          {
            "term": "Reproductive effort",
            "def": "The fraction of an organism's resources allocated to current reproduction vs. survival/future reproduction."
          }
        ],
        "exam_traps": [
          "Trade-offs are physical/physiological — they are not optional. Selection works WITHIN trade-offs to optimize, not to escape them.",
          "Don't expect organisms to maximize one fitness component (e.g., longevity). Selection maximizes lifetime reproductive success, integrated over all life-history traits."
        ]
      },
      {
        "letter": "B",
        "title": "Extrinsic mortality and life-history strategies",
        "overview": "Extrinsic mortality — the rate at which adults die from external causes (predation, disease) — is the single most important determinant of optimal life-history strategy.",
        "key_points": [
          "HIGH extrinsic mortality (e.g., heavy predation) → favors EARLY reproduction, MANY offspring, short lifespan ('live fast, die young').",
          "LOW extrinsic mortality → favors DELAYED reproduction, FEWER but better-provisioned offspring, longer lifespan.",
          "Classic comparison: opossums on predator-rich mainland mature earlier and produce more offspring than opossums on predator-free islands.",
          "These life-history shifts evolve quickly — within tens of generations under strong selection."
        ],
        "key_terms": [
          {
            "term": "Extrinsic mortality",
            "def": "Death from external causes (predation, disease, accident) — outside the organism's physiological control."
          },
          {
            "term": "Intrinsic mortality / senescence",
            "def": "Death from internal causes (aging, organ failure) — physiological decline."
          }
        ],
        "exam_traps": [
          "When the study guide asks about predation effects, the answer is usually: high predation → early/fast reproduction; low predation → delayed/slow reproduction.",
          "Extrinsic mortality affects optimal age at maturity, even if intrinsic survival is high."
        ]
      },
      {
        "letter": "C",
        "title": "Theories of senescence — why we age",
        "overview": "Why doesn't selection prevent aging? Two main answers, both rooted in the fact that selection becomes weaker at older ages.",
        "key_points": [
          "MUTATION ACCUMULATION (Medawar): late-life deleterious mutations escape selection because they affect individuals who've already reproduced. Such mutations accumulate.",
          "ANTAGONISTIC PLEIOTROPY (Williams): some genes have BENEFICIAL effects early in life and HARMFUL effects late. Selection favors them on net because early-life effects on reproduction outweigh late-life costs.",
          "DISPOSABLE SOMA (Kirkwood): organisms allocate finite resources between somatic maintenance (long life) and reproduction (more offspring). Investment in soma reduces fecundity.",
          "These theories are not mutually exclusive — all may contribute."
        ],
        "key_terms": [
          {
            "term": "Senescence",
            "def": "Age-related decline in survival and reproduction; aging."
          },
          {
            "term": "Mutation accumulation theory",
            "def": "Late-acting deleterious mutations escape selection and accumulate, causing senescence."
          },
          {
            "term": "Antagonistic pleiotropy",
            "def": "A single gene with beneficial early-life effects and harmful late-life effects; selection favors the early benefit."
          },
          {
            "term": "Disposable soma theory",
            "def": "Trade-off between somatic maintenance and reproduction; selection favors reproduction at the cost of long-term cell repair."
          }
        ],
        "exam_traps": [
          "Antagonistic pleiotropy is a single-gene story (one gene, two effects at different ages). Mutation accumulation is a many-gene story (many late-acting mutations escape selection).",
          "'Why we age' has multiple non-exclusive answers — be ready to name and distinguish at least two of the three theories."
        ]
      },
      {
        "letter": "D",
        "title": "Age at maturity and offspring size",
        "overview": "When to start reproducing, and how to package each offspring, are central life-history decisions. Both depend on environmental risk and resource availability.",
        "key_points": [
          "AGE AT MATURITY: earlier maturity → reproduce sooner but at smaller size (less invested in growth). Optimal age depends on growth rate, mortality risk, and reproductive payoff.",
          "OFFSPRING SIZE-NUMBER trade-off: a fixed reproductive budget can be split into MANY SMALL offspring (high mortality of each, but bet-hedging) OR FEW LARGE offspring (each well-provisioned, higher per-offspring survival).",
          "r-selected species (high mortality, ephemeral resources): many small offspring, early maturity. (Mice, weeds.)",
          "K-selected species (stable, competitive environments): few large offspring, delayed maturity, parental care. (Elephants, oaks.)"
        ],
        "key_terms": [
          {
            "term": "Age at maturity",
            "def": "Age at which an individual first reproduces."
          },
          {
            "term": "r/K selection",
            "def": "Classical (and somewhat dated) framework distinguishing fast-living, high-fecundity (r) from slow-living, low-fecundity (K) life histories."
          }
        ],
        "exam_traps": [
          "r/K is a useful heuristic but not a strict dichotomy. Many species are intermediate. Modern life-history theory uses continuous variables.",
          "Earlier maturity does NOT always mean smaller offspring; the trade-off is about TOTAL reproductive investment, not necessarily individual offspring size."
        ]
      },
      {
        "letter": "E",
        "title": "Case study — Seychelles warblers",
        "overview": "The Seychelles warbler (Acrocephalus sechellensis) population on Cousin Island provides one of the best documented life-history datasets, including sex-biased dispersal driven by territory quality.",
        "key_points": [
          "Seychelles warblers cooperatively breed: offspring help parents raise subsequent broods.",
          "Territory quality varies dramatically; high-quality territories support more breeding success.",
          "FEMALE OFFSPRING are more likely to remain on natal high-quality territories as helpers; MALE OFFSPRING disperse — sex-biased dispersal driven by territory value.",
          "Demonstrates how ecological constraints (territory quality, helping opportunities) shape life-history decisions about dispersal, helping, and breeding."
        ],
        "key_terms": [
          {
            "term": "Cooperative breeding",
            "def": "A breeding system in which adult helpers (often offspring from previous broods) assist parents in raising young."
          },
          {
            "term": "Sex-biased dispersal",
            "def": "One sex disperses from the natal site more than the other; common in birds and mammals."
          }
        ],
        "exam_traps": [
          "Sex-biased dispersal in Seychelles warblers is FEMALE-PHILOPATRIC (females stay on good territories, males disperse). The direction of bias is testable.",
          "Helping is not pure altruism — helpers gain inclusive fitness through helping kin and may inherit territories later."
        ]
      }
    ]
  },
  "L13": {
    "title": "Evolution of Social Behavior",
    "intro": "How can selection favor cooperative or self-sacrificing behavior when those behaviors apparently lower the actor's fitness? The answer — kin selection, inclusive fitness, evolutionarily stable strategies — is a foundational result in modern evolutionary biology.",
    "sections": [
      {
        "letter": "A",
        "title": "Individual vs. group selection",
        "overview": "An old idea: traits evolve 'for the good of the species' or 'good of the group.' Modern evolutionary biology rejects naïve group selection — selection acts predominantly at the level of individuals (or genes), and selfish individuals usually outcompete cooperative ones.",
        "key_points": [
          "GROUP SELECTION (naïve form): traits spread because they benefit the group, even at individual cost.",
          "Problem with naïve group selection: a 'cheater' that benefits from cooperation without contributing has higher individual fitness. Cheaters spread; cooperation collapses.",
          "Modern view: selection mostly works at the individual or genic level; apparent group benefits arise from individual benefits.",
          "Special conditions (frequent population extinctions, strict subdivision) can permit some forms of group-level selection, but it's the exception."
        ],
        "key_terms": [
          {
            "term": "Group selection",
            "def": "Selection in which differential reproduction of GROUPS (not individuals) drives evolutionary change."
          },
          {
            "term": "Selfish gene perspective",
            "def": "Dawkins's framing: selection favors alleles that increase their own propagation, even if that means promoting altruistic behavior toward genetic relatives."
          }
        ],
        "exam_traps": [
          "'Good of the species' is a non-explanation. Always ask: what's in it for the individual (or the gene)?",
          "Group selection isn't strictly impossible, but it's overwhelmed by individual selection in nearly all real-world cases."
        ]
      },
      {
        "letter": "B",
        "title": "Kin selection and inclusive fitness",
        "overview": "Hamilton's insight: an altruistic gene can spread if its bearers help GENETIC RELATIVES, who share copies of the gene. The propagation of the gene matters, not the survival of the individual.",
        "key_points": [
          "HAMILTON'S RULE: rB > C, where r = coefficient of relatedness, B = benefit to recipient, C = cost to actor. Altruism evolves when rB > C.",
          "Coefficient of relatedness r: parent-offspring r = 0.5; full siblings r = 0.5; half-siblings r = 0.25; first cousins r = 0.125.",
          "INCLUSIVE FITNESS = direct fitness (own offspring) + indirect fitness (extra offspring of relatives that wouldn't have existed without your help, weighted by relatedness).",
          "Eusociality (worker bees, ants, naked mole-rats) is the extreme case — workers forgo reproduction entirely to raise relatives.",
          "Haplodiploidy in hymenopterans: sisters share r = 0.75 (more than they'd share with their own offspring, r = 0.5), favoring sister-helping behavior. Disputed as a complete explanation, but suggestive."
        ],
        "key_terms": [
          {
            "term": "Hamilton's rule",
            "def": "Altruism is favored when rB > C; rB is the indirect benefit through relatives, C is the cost to the actor."
          },
          {
            "term": "Coefficient of relatedness (r)",
            "def": "Probability that two individuals share a given allele by recent common descent."
          },
          {
            "term": "Inclusive fitness",
            "def": "Direct fitness from own offspring plus indirect fitness gained through helping relatives reproduce."
          },
          {
            "term": "Eusociality",
            "def": "Highly social organization with reproductive division of labor — workers forgo reproduction to raise relatives."
          }
        ],
        "exam_traps": [
          "Hamilton's rule is rB > C, NOT B > C. Forgetting the r is the classic error.",
          "Helping random strangers does not satisfy Hamilton's rule (r = 0). Apparent altruism toward strangers usually involves reciprocity, reputation, or other mechanisms."
        ]
      },
      {
        "letter": "C",
        "title": "Evolutionarily stable strategies (ESS)",
        "overview": "An ESS is a behavioral strategy that, once common in a population, cannot be invaded by a rare alternative. ESS reasoning predicts which behaviors persist under frequency-dependent selection.",
        "key_points": [
          "ESS = a strategy that, when adopted by most of a population, cannot be invaded by a rare alternative — a Nash equilibrium in evolutionary terms.",
          "ESS depends on FREQUENCY-DEPENDENT payoffs: the fitness of a strategy depends on what other strategies are common.",
          "Hawk-Dove game: pure-Hawk is unstable (Hawks fight, costs mount); pure-Dove is unstable (a rare Hawk exploits all the Doves). Mixed equilibrium emerges.",
          "ESS is solved with game-theory tools — payoff matrices and frequency-dependent fitness."
        ],
        "key_terms": [
          {
            "term": "Evolutionarily Stable Strategy (ESS)",
            "def": "A strategy that, when adopted by most members of a population, cannot be invaded by any rare alternative strategy."
          },
          {
            "term": "Frequency-dependent selection",
            "def": "Fitness of a strategy depends on its frequency in the population — common strategies may be at advantage or disadvantage."
          },
          {
            "term": "Hawk-Dove game",
            "def": "Classic ESS model: aggressive (Hawk) and submissive (Dove) strategies in resource competition; equilibrium is a mix."
          }
        ],
        "exam_traps": [
          "An ESS is not necessarily the BEST strategy on average — it's the strategy that can't be displaced once common. Mixed ESS solutions are common.",
          "Frequency-dependent selection can MAINTAIN diversity at equilibrium — different strategies coexist because each is favored when rare."
        ]
      },
      {
        "letter": "D",
        "title": "Side-blotched lizards — rock-paper-scissors in nature",
        "overview": "Male side-blotched lizards (Uta stansburiana) come in three throat-color morphs that play a rock-paper-scissors mating game — a real-world demonstration of frequency-dependent ESS dynamics.",
        "key_points": [
          "Three male morphs: ORANGE (aggressive, defends large territories with many females), BLUE (defends small territories with one mate, vigilant against sneakers), YELLOW (sneaker, mimics females, sneaks copulations).",
          "Orange beats Blue (Orange's aggression overwhelms Blue's small-territory defense).",
          "Blue beats Yellow (Blue's vigilance catches Yellow sneakers).",
          "Yellow beats Orange (Orange spreads thin defending many females; Yellow sneaks in unnoticed).",
          "Result: frequencies of the three morphs cycle over years — no single ESS, but a stable cyclic dynamic."
        ],
        "key_terms": [
          {
            "term": "Side-blotched lizard (Uta stansburiana)",
            "def": "Lizard species with three male throat-color morphs displaying rock-paper-scissors mating dynamics."
          }
        ],
        "exam_traps": [
          "The 'rock-paper-scissors' framing: Orange > Blue, Blue > Yellow, Yellow > Orange. Cyclic dominance, not one winner.",
          "This is a real demonstration of NEGATIVE frequency-dependent selection — each morph is favored when rare, disadvantaged when common."
        ]
      },
      {
        "letter": "E",
        "title": "Cooperation among non-kin — reciprocity, reputation, byproducts",
        "overview": "Cooperation among unrelated individuals does occur. The mechanisms are different from kin-selected altruism — reciprocity, reputation, partner choice, or mutual benefit.",
        "key_points": [
          "DIRECT RECIPROCITY: 'I help you now if you help me later.' Requires repeat interaction and memory.",
          "INDIRECT RECIPROCITY: helping confers a reputation that attracts future help from third parties. Requires public visibility.",
          "MUTUALISTIC BYPRODUCT: cooperation costs nothing (or even directly benefits the actor) — pure self-interest aligns.",
          "Cheating is always tempting; cooperation among non-kin is fragile and requires enforcement, sanctions, or partner choice to persist."
        ],
        "key_terms": [
          {
            "term": "Direct reciprocity",
            "def": "Cooperation maintained by tit-for-tat exchange between two individuals over repeated interactions."
          },
          {
            "term": "Indirect reciprocity",
            "def": "Cooperation maintained because helpful behavior earns a reputation that attracts future help from others."
          }
        ],
        "exam_traps": [
          "Reciprocity requires REPEATED INTERACTION — it doesn't work in one-shot games or anonymous encounters.",
          "Cooperation among non-kin is often unstable; cheating invades unless mechanisms exist to detect and punish defectors."
        ]
      }
    ]
  },
  "L14": {
    "title": "History of Life",
    "intro": "A 4-billion-year overview of life on Earth — when, where, and roughly how. The lecture covers Earth's age, key evolutionary milestones (origin of life, photosynthesis, eukaryotes, multicellularity, Cambrian explosion), mass extinctions, and the dating tools that anchor it all.",
    "sections": [
      {
        "letter": "A",
        "title": "Earth's age and dating methods",
        "overview": "Earth is ~4.568 billion years old. We know this from radiometric dating of Earth and meteorite materials. Dating life's milestones depends on the same physics — measuring ratios of radioactive isotopes in rocks.",
        "key_points": [
          "Earth's age: ~4.568 billion years (radiometric dating of meteorites, oldest Earth zircons).",
          "RADIOMETRIC DATING measures the ratio of a parent isotope to its daughter (decay product). Each isotope has a known half-life.",
          "Different isotope systems for different time scales: ¹⁴C for tens of thousands of years; U-Pb for billions of years; K-Ar for millions.",
          "BIOMARKERS (chemical signatures in rocks like specific lipid molecules) suggest life by ~3.5–3.8 billion years ago."
        ],
        "key_terms": [
          {
            "term": "Radiometric dating",
            "def": "Determining the age of a rock by measuring ratios of parent and daughter isotopes; uses known half-lives."
          },
          {
            "term": "Half-life",
            "def": "Time required for half of a radioactive isotope to decay."
          },
          {
            "term": "Biomarker",
            "def": "A chemical molecule (often a lipid) preserved in ancient rocks that indicates the past presence of specific organisms."
          }
        ],
        "exam_traps": [
          "Carbon-14 dating only works back ~50,000 years (5 half-lives × 5,730 yr ≈ 28k yr; method becomes unreliable beyond that). For deep time, you need U-Pb, K-Ar, etc.",
          "Earth's age is ~4.568 billion years — close to but distinct from the universe's age (~13.8 Gyr) or the age of the oldest rocks on Earth (~4.0 Gyr)."
        ]
      },
      {
        "letter": "B",
        "title": "Major milestones in life's history",
        "overview": "Life appeared early. Then for a couple billion years, very little visible happened. Then in a few hundred million years, all the modern phyla appeared. The timeline matters.",
        "key_points": [
          "~3.5–3.8 GYA: earliest evidence of life (microbial mats, biomarkers).",
          "~2.4 GYA: GREAT OXIDATION EVENT — cyanobacteria producing oxygen accumulate atmospheric O₂; redox-sensitive minerals show the shift in rocks worldwide.",
          "~2.1–1.6 GYA: first eukaryotes (mitochondrial endosymbiosis).",
          "~1.0 GYA: first multicellular life.",
          "~541 MYA: CAMBRIAN EXPLOSION — most modern animal phyla appear in the fossil record over ~20 million years.",
          "~444 MYA (Ordovician): early bony fishes; first land plants.",
          "~419 MYA (Silurian): first land animals (millipedes, arthropods).",
          "~359 MYA (Devonian): age of fishes; early tetrapods (Tiktaalik, etc.).",
          "~251 MYA (Permian-Triassic boundary): largest mass extinction; ~95% marine species lost.",
          "~66 MYA (K-T or K-Pg boundary): asteroid impact; non-avian dinosaurs go extinct."
        ],
        "key_terms": [
          {
            "term": "Great Oxidation Event",
            "def": "Rise of atmospheric oxygen ~2.4 GYA driven by cyanobacterial photosynthesis; transformed Earth's chemistry and life."
          },
          {
            "term": "Cambrian explosion",
            "def": "Rapid (~541–520 MYA) diversification of most modern animal phyla, recorded in the fossil record."
          }
        ],
        "exam_traps": [
          "The Cambrian explosion is RAPID on a geological timescale (~20 MYR) but is NOT instant. It also represents the appearance of HARD PARTS that fossilize, not necessarily the origin of phyla.",
          "Don't confuse the Permian-Triassic extinction (~252 MYA, biggest) with the K-T / K-Pg extinction (~66 MYA, dinosaurs)."
        ]
      },
      {
        "letter": "C",
        "title": "Geological time periods to recognize",
        "overview": "The study guide explicitly lists Ordovician, Silurian, Devonian, Permian. Be ready to associate each period with its key biological event.",
        "key_points": [
          "ORDOVICIAN (~488–444 MYA): early bony fishes; first land plants.",
          "SILURIAN (~444–416 MYA): first land animals (arthropods, including millipedes).",
          "DEVONIAN (~416–359 MYA): age of fishes; early tetrapod evolution; early forests; major reef expansion.",
          "PERMIAN (~299–251 MYA): origin of reptiles and proto-mammals (synapsids); ends with the Permian-Triassic mass extinction."
        ],
        "key_terms": [
          {
            "term": "Devonian",
            "def": "Geological period (~416–359 MYA) marked by major fish diversification and the origin of land vertebrates."
          },
          {
            "term": "Permian",
            "def": "Geological period (~299–251 MYA) ending in Earth's largest mass extinction."
          }
        ],
        "exam_traps": [
          "The study guide explicitly tests these period-event associations. Memorize the canonical pairings.",
          "The Devonian = 'Age of Fishes'; the Permian-Triassic boundary = the largest mass extinction."
        ]
      },
      {
        "letter": "D",
        "title": "Mass extinctions",
        "overview": "Five 'Big Five' mass extinctions punctuate the Phanerozoic. Each reset evolutionary trajectories — opening new niches for survivors. Mass extinction is not unidirectional; it shapes which lineages get to radiate next.",
        "key_points": [
          "BIG FIVE mass extinctions: end-Ordovician (~444 MYA), Late Devonian (~375 MYA), end-Permian (~252 MYA), end-Triassic (~201 MYA), end-Cretaceous (K-Pg, ~66 MYA).",
          "End-PERMIAN: largest, ~95% marine species lost; cause likely Siberian Trap volcanism + climate change + ocean acidification.",
          "K-T (end-CRETACEOUS): asteroid impact at the Yucatán (Chicxulub crater); iridium layer is the smoking gun. Non-avian dinosaurs eliminated.",
          "Mass extinctions clear out dominant groups, opening niches for survivors to radiate (mammals diversified after the K-Pg).",
          "Many biologists argue we are now in the SIXTH MASS EXTINCTION driven by humans."
        ],
        "key_terms": [
          {
            "term": "Mass extinction",
            "def": "A geologically rapid event eliminating a large fraction of Earth's species, usually defined as >75% species loss."
          },
          {
            "term": "K-T (K-Pg) boundary",
            "def": "End-Cretaceous boundary (~66 MYA) marked by asteroid impact and the extinction of non-avian dinosaurs."
          },
          {
            "term": "Iridium layer",
            "def": "A thin global layer of iridium-rich sediment at the K-Pg boundary, evidence for an extraterrestrial impact."
          }
        ],
        "exam_traps": [
          "The study guide directly asks about the K-T boundary's significance — be ready: asteroid impact, end-Cretaceous, non-avian dinosaur extinction, mammal radiation thereafter.",
          "K-T (K-Pg) is the dinosaur extinction; the Permian-Triassic is the bigger one. Don't confuse them."
        ]
      }
    ]
  },
  "L15": {
    "title": "Phylogenetics and the Tree of Life",
    "intro": "Phylogenetic trees are hypotheses about evolutionary relationships built from shared derived characters. The skill on this exam is reading trees correctly and choosing the right kind of character (synapomorphy, not symplesiomorphy or homoplasy) to define groups.",
    "sections": [
      {
        "letter": "A",
        "title": "Reading phylogenetic trees",
        "overview": "A phylogenetic tree depicts hypothesized evolutionary relationships among taxa. Tips are extant or extinct organisms; internal nodes are common ancestors; branches represent lineages over time.",
        "key_points": [
          "A NODE is a common ancestor of the taxa above it (toward the tips).",
          "Two taxa that share a more RECENT common ancestor are more CLOSELY related — measured by node depth, NOT by physical distance on the page.",
          "Trees can be rotated at any node without changing relationships — only the order of branching matters."
        ],
        "key_terms": [
          {
            "term": "Tip / Terminal taxon",
            "def": "An extant (or extinct) organism at the end of a branch — what's being classified."
          },
          {
            "term": "Node",
            "def": "A point in the tree where lineages diverge — represents the most recent common ancestor of all descendants."
          },
          {
            "term": "Branch",
            "def": "A line in the tree representing a lineage existing through time."
          },
          {
            "term": "Sister groups",
            "def": "Two clades that share an immediate common ancestor (a single node)."
          }
        ],
        "exam_traps": [
          "Visual proximity on the page does NOT equal evolutionary closeness — trees can be drawn with branches in any rotation.",
          "Don't assume tips on adjacent branches are sister groups; trace back to the node and see what it joins."
        ]
      },
      {
        "letter": "B",
        "title": "Synapomorphies vs. symplesiomorphies vs. homoplasies",
        "overview": "Only SYNAPOMORPHIES — shared derived characters — define monophyletic groups. Symplesiomorphies (shared ancestral traits) and homoplasies (independent acquisitions) mislead.",
        "key_points": [
          "Synapomorphy = a derived character STATE shared because of inheritance from a common ancestor that first evolved it.",
          "Symplesiomorphy = a shared ANCESTRAL state — present in more distant ancestors, not informative about which lineages cluster.",
          "Homoplasy = a similar state arising independently (convergence) or by reversal — misleading; not a synapomorphy."
        ],
        "key_terms": [
          {
            "term": "Synapomorphy",
            "def": "A shared, derived (evolutionarily novel) character state that is informative for defining a monophyletic group."
          },
          {
            "term": "Symplesiomorphy",
            "def": "A shared ancestral character state; widespread among lineages and uninformative about closer relationships."
          },
          {
            "term": "Homoplasy",
            "def": "Similar character states in different lineages that did NOT come from a common ancestor — produced by convergence, parallelism, or reversal."
          }
        ],
        "exam_traps": [
          "'Has a backbone' is a synapomorphy of vertebrates as a whole, but a SYMPLESIOMORPHY for any subgroup (e.g., mammals + birds) — i.e., the same character can play different roles depending on the level you're working at.",
          "If two distantly related lineages share a feature, suspect homoplasy — check whether the common ancestor likely had it."
        ]
      },
      {
        "letter": "C",
        "title": "Monophyletic, paraphyletic, polyphyletic",
        "overview": "Modern systematics requires named groups to be monophyletic. Para- and polyphyletic groups are rejected because they don't reflect evolutionary history.",
        "key_points": [
          "MONOPHYLETIC (clade) = a common ancestor + ALL its descendants. Defined by synapomorphies.",
          "PARAPHYLETIC = common ancestor + SOME (not all) descendants. Example: 'Reptilia' excluding birds — birds are reptiles by descent but were left out historically.",
          "POLYPHYLETIC = group built from members that do NOT share an immediate common ancestor; based on convergent traits. Example: 'warm-blooded animals' (mammals + birds, not their reptilian common ancestor)."
        ],
        "key_terms": [
          {
            "term": "Clade / Monophyletic group",
            "def": "A common ancestor and all of its descendants — the only kind of group that reflects an evolutionary unit."
          },
          {
            "term": "Paraphyletic group",
            "def": "A group containing a common ancestor but NOT all of its descendants; rejected in modern systematics."
          },
          {
            "term": "Polyphyletic group",
            "def": "A group whose members do not share an immediate common ancestor; based on convergent (homoplasic) traits."
          }
        ],
        "exam_traps": [
          "Birds nest within reptiles — calling 'Reptilia' (without birds) a valid group makes it paraphyletic. Modern usage either includes birds or uses 'Sauropsida'.",
          "Polyphyletic groups are diagnosed by SHARED CONVERGENT FEATURES, not common ancestry."
        ]
      },
      {
        "letter": "D",
        "title": "Species concepts",
        "overview": "Different species concepts emphasize different criteria. The Biological Species Concept (BSC) is the most famous, but it has limits.",
        "key_points": [
          "Biological Species Concept (BSC, Mayr): species = groups of actually or potentially interbreeding populations, reproductively isolated from others. Strength: clear mechanism (gene flow). Limit: can't apply to asexual organisms or fossils.",
          "Morphological Species Concept: species defined by distinctive form. Strength: usable on fossils and any organism. Limit: cryptic species and morphological plasticity confuse it.",
          "Phylogenetic Species Concept: species = smallest monophyletic group with shared derived characters. Strength: works for asexuals and fossils. Limit: depends on chosen markers; tends to split lineages aggressively."
        ],
        "key_terms": [
          {
            "term": "Biological Species Concept (BSC)",
            "def": "Mayr's definition: a species is a group of interbreeding (or potentially interbreeding) natural populations reproductively isolated from others."
          },
          {
            "term": "Morphological species concept",
            "def": "Species defined by distinct, diagnosable morphological differences."
          },
          {
            "term": "Phylogenetic species concept",
            "def": "Species defined as the smallest monophyletic group identifiable by shared derived characters."
          }
        ],
        "exam_traps": [
          "The BSC requires reproductive isolation — but two morphologically distinct populations that occasionally hybridize can still be 'good' biological species if hybrids have reduced fitness.",
          "Asexual organisms (bacteria, parthenogenetic animals) are not species under the BSC. Use morphology or phylogeny instead."
        ]
      }
    ]
  },
  "L16": {
    "title": "Species Concepts and Reproductive Isolation",
    "intro": "What IS a species, exactly? Different concepts emphasize different criteria, each with strengths and limits. This lecture covers species concepts and the reproductive isolation mechanisms — pre- and postzygotic — that keep species apart.",
    "sections": [
      {
        "letter": "A",
        "title": "Major species concepts",
        "overview": "There is no single universal species definition. The Biological Species Concept dominates animal biology; alternatives handle cases where the BSC fails.",
        "key_points": [
          "BIOLOGICAL SPECIES CONCEPT (BSC, Mayr): species = groups of actually or potentially interbreeding natural populations, reproductively isolated from other such groups. Strength: clear mechanism (gene flow). Limits: can't apply to asexual organisms or fossils.",
          "MORPHOLOGICAL SPECIES CONCEPT: species defined by distinct, diagnosable morphological differences. Strength: applies to fossils and asexuals. Limit: cryptic species (genetically distinct but morphologically identical) and morphological plasticity create errors.",
          "PHYLOGENETIC SPECIES CONCEPT: species = the smallest monophyletic group identifiable by shared derived characters. Strength: works for asexuals, applies cladistic logic. Limit: sensitive to sampling and characters chosen; tends to split lineages aggressively.",
          "ECOLOGICAL SPECIES CONCEPT: species = populations occupying the same adaptive zone (niche). Useful but sometimes blurry."
        ],
        "key_terms": [
          {
            "term": "Biological Species Concept (BSC)",
            "def": "Mayr's definition: species = group of interbreeding natural populations reproductively isolated from others."
          },
          {
            "term": "Morphological species concept",
            "def": "Species defined by diagnosable morphological differences."
          },
          {
            "term": "Phylogenetic species concept",
            "def": "Species = smallest monophyletic group sharing derived characters."
          }
        ],
        "exam_traps": [
          "The BSC fails for asexual organisms (bacteria, parthenogenetic species) and for fossils — you can't test interbreeding with extinct populations.",
          "Different concepts can disagree about what counts as a species in the same case (e.g., a hybridizing species pair). The 'right' concept depends on what you need it for."
        ]
      },
      {
        "letter": "B",
        "title": "Reproductive isolation — prezygotic vs postzygotic",
        "overview": "The BSC requires reproductive isolation. Mechanisms split into PREZYGOTIC (preventing zygote formation) and POSTZYGOTIC (acting after zygote formation).",
        "key_points": [
          "PREZYGOTIC barriers prevent fertilization or gamete contact:",
          "  • TEMPORAL — populations breed at different times (different seasons, different times of day).",
          "  • BEHAVIORAL — different mating displays/courtship songs prevent recognition between species.",
          "  • MECHANICAL — incompatible reproductive structures (e.g., insect genital morphology) prevent successful copulation.",
          "  • GAMETIC — sperm cannot fertilize eggs of different species (incompatible surface proteins).",
          "  • HABITAT/ECOLOGICAL — populations live in different microhabitats and rarely encounter each other.",
          "POSTZYGOTIC barriers act AFTER zygote formation:",
          "  • HYBRID INVIABILITY — hybrid embryos fail to develop or survive.",
          "  • HYBRID STERILITY — hybrids survive but are sterile (e.g., mules, zorses).",
          "  • HYBRID BREAKDOWN — F1 hybrids viable and fertile, but F2 (or later) generations show reduced fitness."
        ],
        "key_terms": [
          {
            "term": "Prezygotic isolation",
            "def": "Reproductive barriers preventing successful fertilization between species (temporal, behavioral, mechanical, gametic, habitat)."
          },
          {
            "term": "Postzygotic isolation",
            "def": "Reproductive barriers acting after zygote formation: hybrid inviability, sterility, or breakdown."
          },
          {
            "term": "Hybrid sterility",
            "def": "Hybrid offspring survive but cannot reproduce; classic example is the mule (horse × donkey)."
          }
        ],
        "exam_traps": [
          "Pre-zygotic = before zygote (no successful fertilization). Post-zygotic = after zygote (hybrid problems). The dividing line is fertilization.",
          "Hybrid INVIABILITY ≠ hybrid STERILITY. Inviability: hybrids die. Sterility: hybrids live but can't reproduce."
        ]
      },
      {
        "letter": "C",
        "title": "Speciation — how new species arise",
        "overview": "Speciation is the evolutionary process by which one species splits into two or more reproductively isolated descendants. Geography is often (but not always) involved.",
        "key_points": [
          "ALLOPATRIC speciation: populations geographically separated → independent evolution → reproductive isolation accumulates → new species. Most common.",
          "PERIPATRIC speciation: a small founder population becomes geographically isolated; drift + selection in the small population accelerates divergence.",
          "PARAPATRIC speciation: populations are partially separated (adjacent ranges, narrow contact zone); divergence occurs despite some gene flow.",
          "SYMPATRIC speciation: divergence WITHOUT geographic separation, often via niche differentiation, polyploidy (especially in plants), or strong assortative mating.",
          "REINFORCEMENT: when populations come back into secondary contact, selection can favor stronger prezygotic isolation IF hybrids have low fitness."
        ],
        "key_terms": [
          {
            "term": "Allopatric speciation",
            "def": "New species form in geographically separated populations."
          },
          {
            "term": "Sympatric speciation",
            "def": "New species form within the same geographic range, often via niche shifts or polyploidy."
          },
          {
            "term": "Reinforcement",
            "def": "Selection strengthens prezygotic isolation when hybrids between two populations are unfit, accelerating completion of speciation."
          }
        ],
        "exam_traps": [
          "Allopatric is the DEFAULT speciation mode for most animals. Sympatric is rare in animals but more common in plants (polyploidy is sympatric).",
          "Reinforcement is a SECONDARY-CONTACT phenomenon — it only operates AFTER initial divergence in allopatry, when populations meet again."
        ]
      },
      {
        "letter": "D",
        "title": "Hybrid zones and viable hybrids",
        "overview": "Real populations don't always fit clean species boundaries. Hybrid zones — where two species meet and interbreed — reveal incomplete reproductive isolation.",
        "key_points": [
          "HYBRID ZONES are geographic regions where two species' ranges overlap and they interbreed.",
          "VIABLE HYBRIDS can exist (offspring survive) but typically have REDUCED FITNESS — outcompeted by parental species, often sterile, or maladapted to either parental habitat.",
          "Hybrid zones can be stable (selection against hybrids balanced by gene flow) or move over time.",
          "Sometimes hybrids THRIVE in intermediate environments — hybrid zones can also be sites of evolution and even hybrid speciation."
        ],
        "key_terms": [
          {
            "term": "Hybrid zone",
            "def": "Geographic region where two species' ranges overlap and they interbreed, typically producing hybrids of intermediate or reduced fitness."
          },
          {
            "term": "Viable hybrid",
            "def": "Hybrid offspring that survives but typically with reduced fitness."
          }
        ],
        "exam_traps": [
          "Hybrid existence does NOT disprove species status under the BSC — hybrids with reduced fitness still leave the parental species reproductively isolated in the long run.",
          "Hybrid speciation (e.g., in sunflowers) is a real but special case where hybrids form a stable third lineage."
        ]
      }
    ]
  },
  "L17": {
    "title": "Biogeography, Speciation, and Extinction",
    "intro": "Why are species where they are? This lecture covers the geographic distribution of life — how dispersal, vicariance, and continental drift shape biodiversity, plus what determines diversity in a given place over time.",
    "sections": [
      {
        "letter": "A",
        "title": "What is biogeography?",
        "overview": "Biogeography is the study of WHERE species live and WHY. Past geological history (continental drift, glaciation) and ecological factors (climate, dispersal) jointly shape modern distributions.",
        "key_points": [
          "BIOGEOGRAPHY = the study of species distributions across geographic space and through geological time.",
          "Wallace and Darwin both argued that geographic patterns (e.g., distinct faunas on different continents) are best explained by descent and history, not independent creation.",
          "Modern biogeography integrates plate tectonics, climate history, dispersal ability, and ecological interactions."
        ],
        "key_terms": [
          {
            "term": "Biogeography",
            "def": "The study of the geographic distribution of species and ecosystems through space and time."
          },
          {
            "term": "Wallace line",
            "def": "A faunal boundary in the Indonesian archipelago separating Asian and Australasian biotas; named for Alfred Russel Wallace."
          }
        ],
        "exam_traps": [
          "Biogeography unites geology, ecology, and evolution — questions can pull from any of these.",
          "Patterns of distribution are clues to history; similar species in distant places may share ancestry (vicariance) or have dispersed."
        ]
      },
      {
        "letter": "B",
        "title": "Dispersal vs. vicariance",
        "overview": "Two opposing explanations for why related species are found in different places: organisms moved (dispersal) or the geography moved underneath them (vicariance).",
        "key_points": [
          "DISPERSAL: organisms move from one place to another; the same lineage now occupies multiple regions because individuals or propagules crossed geographic barriers.",
          "VICARIANCE: a geographic barrier (mountain range, sea-level change, continental drift) splits a previously continuous range, separating populations that diverge.",
          "Often both have operated; modern molecular phylogenies + dating help distinguish them.",
          "Classic vicariance example: the close relationship of South American and African biota reflects their shared Gondwanan ancestry — they were once continuous before continental drift split them."
        ],
        "key_terms": [
          {
            "term": "Dispersal",
            "def": "Movement of organisms from one location to another, crossing geographic barriers."
          },
          {
            "term": "Vicariance",
            "def": "Geographic separation of a once-continuous range by a new barrier (mountains, seaways, continental drift)."
          }
        ],
        "exam_traps": [
          "Distinguishing dispersal from vicariance requires DATING — vicariant splits should match the geological barrier formation; dispersal splits can be any age.",
          "Don't assume vicariance for every pair of similar species on different continents — some are dispersal events (especially birds, oceanic taxa)."
        ]
      },
      {
        "letter": "C",
        "title": "Standing diversity and species turnover",
        "overview": "STANDING DIVERSITY is how many species are present in a region at one time. TURNOVER is the rate at which species enter (originate, immigrate) and leave (go extinct, emigrate).",
        "key_points": [
          "Standing diversity at any moment = (cumulative origination) − (cumulative extinction) − (emigration) + (immigration).",
          "Turnover RATE = species replacement rate; high turnover means many species coming and going.",
          "Equilibrium theory of island biogeography (MacArthur & Wilson): diversity is set by the BALANCE between immigration (decreasing as species accumulate) and extinction (increasing as species accumulate).",
          "Standing diversity can be stable while turnover is high (membership of the species list constantly changes)."
        ],
        "key_terms": [
          {
            "term": "Standing diversity",
            "def": "The number of species present in a region at a given time."
          },
          {
            "term": "Turnover rate",
            "def": "The rate at which species are replaced — incoming species per unit time, balanced by extinctions/emigrations."
          }
        ],
        "exam_traps": [
          "Standing diversity is a SNAPSHOT; turnover is a RATE. Don't conflate them.",
          "Two communities with the same standing diversity can have very different turnover rates."
        ]
      },
      {
        "letter": "D",
        "title": "Mass extinctions and their consequences",
        "overview": "Mass extinctions reset the trajectory of life by clearing dominant lineages and opening niches for survivors to radiate into. The Big Five share certain features but had different causes.",
        "key_points": [
          "Big Five mass extinctions punctuate the Phanerozoic; each killed >50% of marine species.",
          "End-Ordovician (~444 MYA): glaciation/sea-level fall.",
          "Late Devonian (~375 MYA): multiple pulses; possibly anoxia / sea-level / climate.",
          "End-Permian (~252 MYA): largest. Likely Siberian Trap volcanism, ocean acidification, climate change. ~95% marine species lost.",
          "End-Triassic (~201 MYA): extinction cleared major reptilian groups, allowing dinosaurs to dominate.",
          "End-Cretaceous / K-Pg (~66 MYA): asteroid impact (Chicxulub). Iridium layer is the smoking gun. Non-avian dinosaurs extinct; mammals radiate.",
          "After mass extinctions, surviving lineages undergo ADAPTIVE RADIATIONS into newly empty niches."
        ],
        "key_terms": [
          {
            "term": "Adaptive radiation",
            "def": "Rapid diversification of a single lineage into many ecologically distinct species, often after mass extinction or invasion of a new habitat."
          }
        ],
        "exam_traps": [
          "End-Permian, NOT end-Cretaceous, is the largest mass extinction.",
          "The K-Pg extinction is closely linked to the Chicxulub impact, but additional factors (Deccan Trap volcanism) likely contributed."
        ]
      },
      {
        "letter": "E",
        "title": "Adaptive radiations",
        "overview": "When a lineage colonizes a new environment or survives a mass extinction, it can rapidly diversify into many species exploiting different niches. Galápagos finches and Hawaiian honeycreepers are classic examples.",
        "key_points": [
          "ADAPTIVE RADIATION = rapid diversification of one lineage into many ecologically diverse species.",
          "Conditions favoring adaptive radiation: open ecological space, new geographic colonization, key innovations, post-extinction recovery.",
          "Galápagos finches: ~14 species derived from a single ancestor, each specialized for a different food niche.",
          "Mammals radiated rapidly after the K-Pg extinction — the niches dinosaurs occupied were suddenly available.",
          "Adaptive radiations can be morphologically dramatic in a few million years."
        ],
        "key_terms": [
          {
            "term": "Adaptive radiation",
            "def": "Rapid evolutionary diversification of one lineage into many species occupying different ecological niches."
          },
          {
            "term": "Key innovation",
            "def": "An evolutionary novelty (jaws, wings, flowering) that opens new ecological possibilities and can trigger radiations."
          }
        ],
        "exam_traps": [
          "Adaptive radiation is fast diversification INTO DIFFERENT NICHES — not just speciation in general.",
          "Mammalian radiation didn't START at the K-Pg; mammals existed earlier but were small and ecologically restricted. The K-Pg removed dinosaur competitors and let mammals diversify."
        ]
      }
    ]
  },
  "L18": {
    "title": "Conservation and Humans as a Selective Force",
    "intro": "Humans are now a dominant evolutionary force — through habitat alteration, hunting, fishing, antibiotic use, and climate change, we are reshaping selection pressures on most species on Earth. This lecture is about that, plus what conservation biology can do.",
    "sections": [
      {
        "letter": "A",
        "title": "Humans as selective force",
        "overview": "Human activities apply strong, directional selection on countless species. Wherever we hunt, harvest, or otherwise selectively kill or capture organisms, we drive evolutionary change.",
        "key_points": [
          "FISHERIES SELECTION: minimum-size limits selectively remove large individuals; over decades, fish populations evolve toward earlier maturation and smaller size.",
          "TROPHY HUNTING: selecting for large-horned individuals can reduce average horn size in the population over time (e.g., bighorn sheep on Ram Mountain).",
          "ANTIBIOTIC RESISTANCE: heavy use selects for resistant bacterial strains.",
          "PESTICIDE RESISTANCE: insect pests evolve resistance under heavy spraying.",
          "URBANIZATION: city-dwelling species (urban pigeons, mice, peppered moths) evolve under novel selective pressures."
        ],
        "key_terms": [
          {
            "term": "Selective harvest",
            "def": "Hunting/fishing that targets specific phenotypes (large size, big horns) and applies directional selection."
          },
          {
            "term": "Fisheries-induced evolution",
            "def": "Evolutionary change in fish populations driven by size-selective fishing pressure."
          }
        ],
        "exam_traps": [
          "Human selection is the same evolutionary process as natural selection; we just play the selecting role.",
          "Selective harvest can REVERSE pre-existing selection (e.g., natural selection for large body, fishing for small) — populations evolve away from natural-equilibrium phenotypes."
        ]
      },
      {
        "letter": "B",
        "title": "Habitat destruction, fragmentation, and conservation genetics",
        "overview": "Habitat loss and fragmentation reduce population sizes and gene flow — making drift stronger, inbreeding more likely, and adaptive evolution slower.",
        "key_points": [
          "Small populations experience strong genetic drift, lose genetic variation, and are vulnerable to inbreeding depression.",
          "Population FRAGMENTATION reduces gene flow between subpopulations, accelerating local divergence and loss of variation.",
          "Florida panther example: a tiny remnant population suffered severe inbreeding depression (heart defects, reproductive issues); rescue via introduction from Texas pumas restored fitness.",
          "GENETIC RESCUE: introducing individuals from a related population can restore genetic variation and fitness in inbred populations."
        ],
        "key_terms": [
          {
            "term": "Inbreeding depression",
            "def": "Reduced fitness in inbred populations due to expression of deleterious recessive alleles in homozygotes."
          },
          {
            "term": "Genetic rescue",
            "def": "Introducing individuals from another population to restore genetic variation and reduce inbreeding depression."
          },
          {
            "term": "Fragmentation",
            "def": "Subdivision of habitat into smaller patches, reducing gene flow and population sizes."
          }
        ],
        "exam_traps": [
          "Small populations are vulnerable to BOTH demographic and genetic problems. Conservation must address both.",
          "Genetic rescue can fail if the introduced population is so distantly related that hybrids are maladapted (outbreeding depression)."
        ]
      },
      {
        "letter": "C",
        "title": "Climate change as selective pressure",
        "overview": "Anthropogenic climate change is a major and ongoing selective force. Some species track suitable climate by shifting range; others must evolve in place; many will fail to do either fast enough.",
        "key_points": [
          "Many species are shifting ranges poleward and upslope as climates warm.",
          "Species with limited dispersal (e.g., trees, mountain-top organisms) cannot track climate easily and face strong selection or extinction.",
          "Phenological shifts (flowering, migration timing) reflect rapid evolution and plastic responses to changing seasonal cues.",
          "MISMATCHES between interacting species (e.g., insect emergence vs. plant flowering) may break ecological networks."
        ],
        "key_terms": [
          {
            "term": "Phenological shift",
            "def": "Change in the timing of seasonal biological events (flowering, breeding, migration) in response to climate."
          },
          {
            "term": "Range shift",
            "def": "Geographic movement of a species' distribution, often poleward or upslope under warming."
          }
        ],
        "exam_traps": [
          "Species can RESPOND to climate change by shifting range, evolving, going plastic, or going extinct. The mix depends on dispersal ability, generation time, and severity.",
          "Phenological shifts driven by climate are evidence of climate change effects on biology, even when range hasn't shifted yet."
        ]
      },
      {
        "letter": "D",
        "title": "Conservation strategies",
        "overview": "Conservation biology applies evolutionary thinking to preserving biodiversity. The toolkit ranges from habitat protection to captive breeding to genetic rescue.",
        "key_points": [
          "HABITAT PROTECTION: protected areas (national parks, reserves) preserve in-situ biodiversity.",
          "CAPTIVE BREEDING: ex-situ programs maintain populations of critically endangered species (California condor, Arabian oryx) for eventual reintroduction.",
          "ASSISTED MIGRATION: moving species to climate-appropriate habitats (controversial for risk of unintended consequences).",
          "GENETIC RESCUE / outcrossing programs: see §B above.",
          "Effective conservation manages BOTH demographic decline (low N) AND genetic decline (low diversity, inbreeding)."
        ],
        "key_terms": [
          {
            "term": "Conservation biology",
            "def": "The study of preservation of biodiversity; applies evolutionary, ecological, and population-genetic principles."
          },
          {
            "term": "Captive breeding",
            "def": "Maintaining populations in human care to prevent extinction and supply individuals for reintroduction."
          }
        ],
        "exam_traps": [
          "Conservation is ALWAYS about both populations and the genes within them. A demographically large population with no genetic diversity is still vulnerable.",
          "Captive breeding can introduce its own selection pressures (adaptation to captivity) that may reduce wild fitness on release."
        ]
      }
    ]
  },
  "L19": {
    "title": "Human Evolution",
    "intro": "Where we came from. The hominin lineage diverged from chimpanzees ~6–7 million years ago in Africa; bipedalism came first, then expanding brain, then long migration out of Africa. This lecture also touches evolutionary medicine — how our evolutionary history shapes modern disease.",
    "sections": [
      {
        "letter": "A",
        "title": "The hominin lineage and bipedalism",
        "overview": "Humans share a common ancestor with chimpanzees ~6–7 MYA. The first major hominin innovation was BIPEDAL LOCOMOTION, which preceded brain enlargement.",
        "key_points": [
          "Hominins (the human lineage after splitting from chimpanzees) appeared ~6–7 MYA in Africa.",
          "Earliest possible hominins: Sahelanthropus tchadensis (~7 MYA, Chad), Orrorin tugenensis, and Ardipithecus.",
          "BIPEDALISM (walking upright on two legs) was the first major hominin trait, evident in skeletal anatomy of these earliest forms.",
          "Bipedalism is documented in skeletal features: foramen magnum (where the spinal cord exits the skull) is positioned UNDERNEATH the skull, indicating an upright spine.",
          "Brain enlargement came AFTER bipedalism in hominin evolution."
        ],
        "key_terms": [
          {
            "term": "Hominin",
            "def": "Members of the human lineage since the chimpanzee split — includes modern humans and all extinct relatives."
          },
          {
            "term": "Bipedalism",
            "def": "Habitual two-legged walking; the earliest hallmark hominin adaptation."
          },
          {
            "term": "Foramen magnum",
            "def": "The opening in the skull where the spinal cord exits; its position (rear vs. underneath) indicates posture."
          }
        ],
        "exam_traps": [
          "The study guide explicitly tests bipedalism: it began ~6–7 MYA. Brain enlargement is later.",
          "Sahelanthropus from Chad is the early hominin example the study guide flags. Recognize the Chad connection."
        ]
      },
      {
        "letter": "B",
        "title": "Australopithecines and early Homo",
        "overview": "After the earliest hominins, several species of Australopithecus dominated for several million years. Genus Homo appears ~2.5 MYA.",
        "key_points": [
          "Australopithecus afarensis (~3.9–2.9 MYA) — 'Lucy' is the famous specimen; small-brained but fully bipedal.",
          "Robust australopithecines (Paranthropus) — heavy chewing apparatus, evolutionary dead-end.",
          "Genus Homo appears ~2.5 MYA with H. habilis — first stone tools (Oldowan).",
          "Homo erectus (~1.9 MYA) — first hominin to leave Africa, larger brain, more sophisticated tools.",
          "Homo sapiens emerges in Africa ~300 KYA."
        ],
        "key_terms": [
          {
            "term": "Australopithecus",
            "def": "Genus of bipedal hominins (~4–2 MYA); 'Lucy' is the famous A. afarensis specimen."
          },
          {
            "term": "Homo habilis",
            "def": "Earliest member of genus Homo (~2.5 MYA); associated with first known stone tools."
          }
        ],
        "exam_traps": [
          "Homo erectus is the FIRST hominin to leave Africa, not Homo sapiens.",
          "Brain size increased gradually through the hominin lineage; H. erectus had ~1000 cc, H. sapiens ~1350 cc."
        ]
      },
      {
        "letter": "C",
        "title": "Out-of-Africa migrations and Neanderthal/Denisovan introgression",
        "overview": "Modern humans (Homo sapiens) originated in Africa, then dispersed worldwide ~70 KYA, encountering and partly interbreeding with archaic populations like Neanderthals and Denisovans.",
        "key_points": [
          "Anatomically modern Homo sapiens: ~300 KYA in Africa.",
          "Major out-of-Africa dispersal: ~70 KYA, replacing or absorbing earlier hominin populations across Eurasia.",
          "Modern non-African humans carry ~1–4% Neanderthal DNA from interbreeding ~40–60 KYA.",
          "Some Asian and Oceanic populations carry additional Denisovan DNA; this includes high-altitude adaptation alleles in Tibetans (EPAS1).",
          "Genetic introgression with archaic humans contributed alleles for immunity, skin pigmentation, altitude adaptation — partly accelerating modern-human adaptation to new environments."
        ],
        "key_terms": [
          {
            "term": "Out of Africa",
            "def": "The migration of anatomically modern humans from Africa to the rest of the world ~70 KYA."
          },
          {
            "term": "Introgression",
            "def": "Gene flow between populations or species via interbreeding, contributing alleles from one to the other."
          },
          {
            "term": "Neanderthal",
            "def": "Archaic human relative (Homo neanderthalensis) inhabiting Europe and West Asia; interbred with modern humans ~40–60 KYA."
          }
        ],
        "exam_traps": [
          "All non-African modern humans carry small amounts of Neanderthal DNA; African populations have very little or none (because the introgression happened after the migration out of Africa).",
          "The 'Out of Africa' model is now better called 'Recent African Origin' with admixture — it's not a simple replacement."
        ]
      },
      {
        "letter": "D",
        "title": "Evolutionary medicine — disease in evolutionary context",
        "overview": "Many modern health problems make more sense when viewed through an evolutionary lens. Pathogens evolve in response to our defenses; our bodies are evolutionary compromises shaped by ancestral environments different from modern ones.",
        "key_points": [
          "ANTIBIOTIC RESISTANCE: pathogens evolve resistance under selection. Once-treatable infections become untreatable. Solution: stewardship + new drug discovery.",
          "PATHOGEN VIRULENCE evolves. Mode of transmission shapes optimal virulence — directly transmitted (e.g., respiratory) pathogens often evolve toward LOWER virulence (need a healthy host to spread); waterborne / vector-borne pathogens can evolve high virulence (don't need the host mobile).",
          "MISMATCH HYPOTHESIS: many modern diseases (obesity, type 2 diabetes, atherosclerosis) reflect mismatch between our ancestral environment (food-scarce, high physical activity) and modern conditions (food-abundant, sedentary).",
          "Our bodies show evolutionary compromises: backaches from upright posture, difficult childbirth from large brains + narrow pelvis, vestigial appendix prone to infection."
        ],
        "key_terms": [
          {
            "term": "Evolutionary medicine",
            "def": "Application of evolutionary principles to understanding human health and disease."
          },
          {
            "term": "Virulence",
            "def": "The degree to which a pathogen damages its host; evolves in response to transmission mode and other ecological factors."
          },
          {
            "term": "Mismatch hypothesis",
            "def": "Modern diseases arise from mismatch between traits adapted to ancestral environments and the conditions of modern life."
          }
        ],
        "exam_traps": [
          "Pathogens evolve. Antibiotic resistance is one application; antigenic shift in flu is another.",
          "Evolutionary medicine doesn't say 'we should live like cave-people' — it says understanding the evolutionary mismatch helps explain susceptibility to certain modern diseases."
        ]
      }
    ]
  },
  "L20": {
    "title": "Evolutionary Medicine",
    "intro": "Evolution doesn't stop at the species boundary — it explains why we get sick, why pathogens evolve, and why some 'designs' of the human body are flawed. This lecture frames disease, drug resistance, virulence evolution, and modern lifestyle illnesses through an evolutionary lens.",
    "sections": [
      {
        "letter": "A",
        "title": "What evolutionary medicine is",
        "overview": "Evolutionary medicine applies evolutionary principles to human health. The central insight: many disease vulnerabilities make sense only as products of past selection in environments very different from the one we live in now.",
        "key_points": [
          "Evolutionary medicine asks WHY (in evolutionary terms) bodies are vulnerable to particular diseases — not just HOW (mechanistically) the disease works.",
          "Six common evolutionary explanations for disease: (1) mismatch with modern environments, (2) coevolution with rapidly evolving pathogens, (3) constraints (selection cannot start over), (4) trade-offs, (5) reproduction trumps health (selection optimizes reproductive success, not longevity), (6) defenses are misperceived as 'symptoms.'",
          "Modern medicine integrates evolutionary thinking into diagnosis, treatment, and public-health strategies (e.g., antibiotic stewardship, vaccine design, cancer treatment timing)."
        ],
        "key_terms": [
          {
            "term": "Evolutionary medicine",
            "def": "Application of evolutionary biology to understanding human health, disease, and medical practice."
          },
          {
            "term": "Proximate vs ultimate explanation",
            "def": "Proximate = mechanism (HOW); ultimate = evolutionary reason (WHY). Both are needed for full understanding."
          }
        ],
        "exam_traps": [
          "Evolutionary medicine doesn't claim modern medicine is wrong — it adds the WHY behind the HOW. Both are needed.",
          "'Why we get sick' is a question with at least six different evolutionary answer categories. Don't reduce all disease to one explanation."
        ]
      },
      {
        "letter": "B",
        "title": "Pathogen evolution and antibiotic resistance",
        "overview": "Pathogens evolve fast — large populations, short generation times, strong selection. The most consequential evolutionary process in clinical medicine is antibiotic resistance, but the same logic applies to antiviral resistance, vaccine escape, and host-immune evasion.",
        "key_points": [
          "ANTIBIOTIC RESISTANCE evolves whenever antibiotics are heavily used. Mutations conferring resistance occur randomly; the antibiotic kills susceptible bacteria and lets resistant rare variants reproduce.",
          "RESISTANCE GENES often spread between bacterial species via horizontal gene transfer (plasmids, transposons) — accelerating spread far beyond clonal reproduction.",
          "Common resistance mechanisms: enzymatic destruction of the drug (β-lactamases), efflux pumps, target-site modification, alternative metabolic pathways.",
          "ANTIBIOTIC STEWARDSHIP — limiting unnecessary antibiotic use, completing prescribed courses, restricting agricultural use — slows but does not stop the evolution of resistance.",
          "ANTIVIRAL RESISTANCE follows the same logic; HIV evolves resistance within a single patient given monotherapy, which is why combination therapy works.",
          "VACCINE ESCAPE: pathogens evolve antigenic variation to evade immune responses (influenza is the textbook annual case)."
        ],
        "key_terms": [
          {
            "term": "Antibiotic resistance",
            "def": "Heritable ability of bacteria to survive antibiotic exposure; arises from random mutation, then spreads under selection."
          },
          {
            "term": "Horizontal gene transfer (HGT)",
            "def": "Movement of DNA (often resistance genes) between bacterial species via plasmids, transformation, or transduction; accelerates resistance spread."
          },
          {
            "term": "Combination therapy",
            "def": "Use of multiple drugs simultaneously so that pathogens require multiple independent resistance mutations to survive — exponentially less likely than single resistance."
          },
          {
            "term": "Vaccine escape / antigenic drift",
            "def": "Pathogen evolution that alters surface antigens to evade prior immunity, requiring updated vaccines."
          }
        ],
        "exam_traps": [
          "Antibiotics do NOT cause resistance mutations — they SELECT for already-existing rare resistant variants. Random mutation + non-random selection.",
          "Stopping a course early can leave partially-resistant survivors and worsen the resistance problem. Complete the prescribed course (current best evidence is more nuanced than the old 'always finish' rule, but the evolutionary logic still favors fully suppressing the infection).",
          "Combination therapy works because the joint probability of multi-drug resistance is the product of single-drug resistance probabilities — for example, 10⁻⁹ × 10⁻⁹ = 10⁻¹⁸ per generation."
        ]
      },
      {
        "letter": "C",
        "title": "Virulence evolution and transmission mode",
        "overview": "How harmful (virulent) a pathogen is to its host is itself an evolutionary trait — and it depends on how the pathogen transmits. Mode of transmission shapes the cost-benefit balance for the pathogen.",
        "key_points": [
          "VIRULENCE = the degree of damage a pathogen causes its host (often measured as case-fatality or per-infection morbidity).",
          "Optimal virulence depends on the TRADE-OFF between transmission rate (often higher in more virulent infections, because pathogen load is higher) and host longevity (lower virulence keeps the host alive and infectious longer).",
          "DIRECTLY TRANSMITTED pathogens (respiratory, sexually transmitted) often evolve toward MODERATE OR LOWER virulence — they need a healthy, mobile host to spread.",
          "VECTOR-BORNE or WATERBORNE pathogens (cholera, malaria) can evolve HIGH virulence because the host's mobility doesn't matter — the vector or environment moves the pathogen.",
          "EWALD'S HYPOTHESIS: cleaner water supplies select for less-virulent diarrheal pathogens because immobile sick hosts can't be visited by vectors or contaminate clean water sources.",
          "Pathogen evolution can shift virulence quickly — e.g., the 1918 influenza pandemic strain evolved very high virulence under crowded WWI conditions."
        ],
        "key_terms": [
          {
            "term": "Virulence",
            "def": "The degree of damage a pathogen causes its host; subject to evolutionary optimization."
          },
          {
            "term": "Virulence-transmission trade-off",
            "def": "Higher within-host pathogen load increases transmission but reduces host survival — selection finds an intermediate optimum."
          },
          {
            "term": "Vector-borne",
            "def": "Transmitted by a third organism (mosquito, tick); the host's own movement doesn't drive transmission."
          },
          {
            "term": "Ewald's hypothesis",
            "def": "Mode of transmission shapes optimal virulence; hygiene improvements lower virulence in waterborne pathogens."
          }
        ],
        "exam_traps": [
          "Virulence is NOT 'always' selected to decrease — that old folk-rule (pathogens evolve to be benign) was wrong. The direction depends on transmission mode.",
          "Sexually-transmitted, respiratory, and vector-borne pathogens all face DIFFERENT virulence-transmission trade-offs. Predicting virulence evolution requires identifying the transmission route."
        ]
      },
      {
        "letter": "D",
        "title": "Host-pathogen coevolution",
        "overview": "Hosts and pathogens are locked in mutual evolutionary arms races. Each side's adaptations select for counter-adaptations in the other — driving rapid evolution on both sides.",
        "key_points": [
          "HOST-PATHOGEN COEVOLUTION is reciprocal: hosts evolve immune defenses; pathogens evolve evasion; hosts evolve new defenses; and so on.",
          "MAJOR HISTOCOMPATIBILITY COMPLEX (MHC) is one of the most variable gene regions in vertebrate genomes — under strong balancing selection from coevolving pathogens. Rare MHC alleles are favored because pathogens haven't adapted to them yet (negative frequency-dependent selection).",
          "RED QUEEN DYNAMICS at the population level: hosts must keep evolving genetic novelty (often via sexual recombination) just to keep up with parasites. This is one of the leading explanations for why sex evolved.",
          "Some pathogens drive long-term host evolution. Example: SICKLE-CELL ALLELE persists in human populations because heterozygotes have malaria resistance — heterozygote advantage maintained by pathogen selection.",
          "Pathogen counter-adaptations include antigenic variation (HIV, trypanosomes), immune-suppressive proteins, intracellular hiding, and rapid mutation rates."
        ],
        "key_terms": [
          {
            "term": "MHC (Major Histocompatibility Complex)",
            "def": "Highly polymorphic immune-system genes presenting pathogen-derived peptides to T cells; under balancing selection from coevolving pathogens."
          },
          {
            "term": "Sickle-cell heterozygote advantage",
            "def": "Heterozygotes (HbA/HbS) are protected against malaria; homozygotes (HbS/HbS) suffer sickle-cell anemia; selection by malaria maintains the allele in malaria-endemic regions."
          },
          {
            "term": "Antigenic variation",
            "def": "Pathogen evolution of surface antigens to evade host immunity (HIV, influenza, trypanosomes)."
          }
        ],
        "exam_traps": [
          "Sickle-cell anemia is a classic POPULATION-LEVEL example of pathogen-driven host evolution. The allele persists not despite the homozygous cost, but because of the heterozygous benefit.",
          "MHC diversity is maintained by BALANCING SELECTION — distinct from directional or stabilizing selection. Rare alleles benefit from being unfamiliar to pathogens."
        ]
      },
      {
        "letter": "E",
        "title": "Mismatch hypothesis — modern environments and chronic disease",
        "overview": "Many chronic diseases of the modern industrialized world (obesity, type 2 diabetes, atherosclerosis, certain autoimmune disorders) reflect a mismatch between traits that were adaptive in ancestral environments and the conditions of modern life.",
        "key_points": [
          "ANCESTRAL ENVIRONMENT (Pleistocene, hunter-gatherer): food often scarce, high physical activity, high pathogen load, modest reproductive lifespan.",
          "MODERN ENVIRONMENT: food abundant (especially refined sugars and fats), sedentary lifestyle, hygiene reduces pathogen exposure, longer lifespan.",
          "MISMATCH DISEASES: efficient fat storage and sweet/fat preferences (adaptive when food was scarce) contribute to obesity and metabolic syndrome in food-abundant environments.",
          "Type 2 DIABETES is rare in populations with traditional active lifestyles and rises sharply with sedentary, calorie-rich modern living.",
          "HYGIENE HYPOTHESIS: reduced early-life microbial exposure may underlie rising allergies, autoimmune diseases — the immune system 'expects' diverse pathogen exposure that no longer occurs.",
          "Many cancers and atherosclerotic heart diseases are diseases of OLD AGE not strongly experienced ancestrally — selection couldn't act against them because they manifest after reproduction."
        ],
        "key_terms": [
          {
            "term": "Mismatch hypothesis",
            "def": "Modern diseases arise from mismatch between ancestrally-adaptive traits and modern environmental conditions."
          },
          {
            "term": "Hygiene hypothesis",
            "def": "Reduced early-life microbial exposure may contribute to rising allergies and autoimmune diseases."
          },
          {
            "term": "Diseases of civilization",
            "def": "Chronic diseases (obesity, type 2 diabetes, atherosclerosis) prevalent in modernized populations and rare in traditional populations."
          }
        ],
        "exam_traps": [
          "Mismatch DOESN'T mean we should live like cave-people; it means understanding our evolutionary history helps explain why certain modern foods and habits are pathogenic.",
          "Diseases of old age (most cancers, Alzheimer's) escape selection because they manifest after reproduction. They aren't 'designed' against — selection just can't see them."
        ]
      },
      {
        "letter": "F",
        "title": "Cancer as somatic evolution",
        "overview": "Cancer is evolution playing out within an individual body. Cells acquire mutations, some of which give a growth advantage; selection within the body favors those cells; tumors are the result. This view reshapes treatment strategies.",
        "key_points": [
          "Cancer cells DIVIDE rapidly with HIGH MUTATION RATES — generating heritable variation among tumor cells.",
          "Tumor cells COMPETE for resources (oxygen, glucose, space). Cells with growth-promoting mutations outcompete neighbors.",
          "Therapies act as STRONG SELECTIVE PRESSURES — chemotherapy and targeted drugs kill susceptible cells but select for resistant subclones, often leading to relapse.",
          "ADAPTIVE THERAPY is an experimental strategy: instead of trying to kill all tumor cells (which selects for resistance), maintain susceptible cells to suppress resistant ones — leveraging competition among tumor subclones.",
          "Cancer susceptibility itself reflects evolutionary trade-offs: mechanisms protecting against cancer (apoptosis, senescence) trade off against tissue regeneration and longevity."
        ],
        "key_terms": [
          {
            "term": "Somatic evolution",
            "def": "Evolution by mutation + selection acting on cell lineages within a multicellular organism's body."
          },
          {
            "term": "Tumor heterogeneity",
            "def": "Genetic diversity among cells within a single tumor, generated by ongoing mutation; substrate for treatment-resistance evolution."
          },
          {
            "term": "Adaptive therapy",
            "def": "Cancer treatment strategy that maintains susceptible tumor cells to competitively suppress resistant subclones, rather than aggressive eradication."
          }
        ],
        "exam_traps": [
          "Cancer is evolution writ small — the same processes (variation, selection, heritability) operating on cell lineages.",
          "Aggressive cancer therapy can SELECT for resistance just like aggressive antibiotic use does. Treatment strategy is also an evolutionary problem."
        ]
      }
    ]
  }
};
console.log('[lecture-guides loaded]', Object.keys(window.MANUAL_LECTURE_GUIDES).length, 'lectures');
