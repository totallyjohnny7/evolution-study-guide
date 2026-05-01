/* Images + remaining content gaps (group 2: L05, L07, L08) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  // ===================== L05 =====================
  window.addCardPatches('L05', {
    "Quantitative trait": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Galton_experiment.png/800px-Galton_experiment.png",
          caption: "Galton's parent–offspring height regression: 928 offspring vs 205 mid-parent values produces a continuous, bell-shaped distribution — the textbook signature of a polygenic quantitative trait.",
          credit: "Wikimedia Commons / Puekai (Public domain)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Galton-height-regress.png/800px-Galton-height-regress.png",
          caption: "Galton's height regression scatter — quantitative traits like stature inherit smoothly because many small-effect loci sum together.",
          credit: "Wikimedia Commons / Madeleine Price Ball (CC0)" }
      ]
    },
    "V_A — Additive genetic variance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "Response to selection (R) is the slice of phenotypic variance that V_A converts into across-generation change — without additive variance, S has nothing to grip on.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "V_D — Dominance variance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Additive_and_Dominance_Effects.png/800px-Additive_and_Dominance_Effects.png",
          caption: "Additive vs dominance components at a single locus — V_D arises from heterozygote effects that don't transmit faithfully across generations.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "V_I — Epistatic (interaction) variance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Galton_experiment.png/800px-Galton_experiment.png",
          caption: "Cross-locus interactions (epistasis) inflate V_I but rearrange under recombination, so selection extracts them inefficiently — which is why slope of regression captures only V_A.",
          credit: "Wikimedia Commons / Puekai (Public domain)" }
      ]
    },
    "V_E — Environmental variance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "Two clones grown in different environments produce different phenotypes — that vertical spread between environments is V_E, the non-heritable component.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" }
      ]
    },
    "Broad-sense heritability (H²)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Additive_and_Dominance_Effects.png/800px-Additive_and_Dominance_Effects.png",
          caption: "H² = V_G/V_P captures all genetic variance (additive + dominance + epistasis); H² > h² when dominance and interaction terms are non-trivial.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Narrow-sense heritability (h²)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Galton_experiment.png/800px-Galton_experiment.png",
          caption: "Slope of offspring on mid-parent regression directly estimates h² — the only heritability that predicts response to selection.",
          credit: "Wikimedia Commons / Puekai (Public domain)" }
      ]
    },
    "Parent-offspring regression": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Galton_experiment.png/800px-Galton_experiment.png",
          caption: "Galton's parent–offspring height regression: the slope of this line ≈ h². A slope of ~0.6 here implies a strongly heritable trait that will respond to selection.",
          credit: "Wikimedia Commons / Puekai (Public domain)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Galton-height-regress.png/800px-Galton-height-regress.png",
          caption: "Mid-parent vs offspring scatter — the founding visualization of regression toward the mean and the operational definition of heritability.",
          credit: "Wikimedia Commons / Madeleine Price Ball (CC0)" }
      ]
    },
    "Selection differential (S)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "S is the gap between the breeders' mean and the original population mean. R is the next-generation shift. h² = R/S.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Response to selection (R)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "R is the realized shift in mean across one generation — the breeder's payoff from selection differential S, scaled by heritability.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Breeder's equation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "R = h²·S in one diagram. h² scales how much of the selection differential transmits to the next generation; if h² = 0, no shift regardless of S.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Phenotypic plasticity": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "One genotype produces a range of phenotypes across environments — the textbook reaction-norm picture of phenotypic plasticity.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Daphnia_pulex.png/800px-Daphnia_pulex.png",
          caption: "Daphnia pulex — when fish-derived kairomones appear, the same genotype induces a defensive helmet/spine. Single genotype, two phenotypes: classic plasticity.",
          credit: "Wikimedia Commons / Paul Hebert (CC BY 2.5)" }
      ]
    },
    "Reaction norm": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "A reaction norm plots one genotype's phenotype across an environmental gradient — flat = canalized, sloped = plastic, crossing lines = G×E.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" }
      ]
    },
    "G×E interaction (V_G×E)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "When reaction-norm lines cross, the rank order of genotypes flips between environments — the diagnostic signature of G×E interaction.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" }
      ]
    },
    "Polyphenic trait": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Termites_polymorphism.jpg/800px-Termites_polymorphism.jpg",
          caption: "Termite caste polyphenism: queens, kings, soldiers, workers — discrete morphs from one genotype, triggered by pheromonal/environmental cues.",
          credit: "Wikimedia Commons / Public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Daphnia_pulex.png/800px-Daphnia_pulex.png",
          caption: "Daphnia switch between helmeted and helmetless morphs based on predator cues — discrete alternatives, not continuous variation.",
          credit: "Wikimedia Commons / Paul Hebert (CC BY 2.5)" }
      ]
    },
    "Canalization": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "A flat reaction-norm line is canalization — the genotype produces the same phenotype across environments, buffering development against perturbation.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" }
      ]
    },
    // L05 extra-card content gaps
    "V_P = V_A + V_D + V_I + V_E": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Additive_and_Dominance_Effects.png/800px-Additive_and_Dominance_Effects.png",
          caption: "Single-locus partition: additive vs dominance effects diagram — the conceptual building block for partitioning V_P at the genome scale.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Directional selection": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Selection_Types_Chart.png/800px-Selection_Types_Chart.png",
          caption: "Directional selection (top): one tail favored, distribution mean shifts toward it across one generation — the deep-beak finch pattern.",
          credit: "Wikimedia Commons / Azcolvin429 (CC BY-SA 3.0)" }
      ]
    },
    "Stabilizing selection": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Selection_Types_Chart.png/800px-Selection_Types_Chart.png",
          caption: "Stabilizing selection: extremes are pruned, mean unchanged, variance shrinks — the human birth-weight pattern.",
          credit: "Wikimedia Commons / Azcolvin429 (CC BY-SA 3.0)" }
      ]
    },
    "Disruptive selection": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Selection_Types_Chart.png/800px-Selection_Types_Chart.png",
          caption: "Disruptive selection: both extremes favored, intermediates removed, distribution becomes bimodal — sets the stage for sympatric divergence.",
          credit: "Wikimedia Commons / Azcolvin429 (CC BY-SA 3.0)" }
      ]
    },
    "Selection-type discrimination cheat": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Selection_Types_Chart.png/800px-Selection_Types_Chart.png",
          caption: "All three selection signatures side-by-side: mean-move = directional, squeeze = stabilizing, split = disruptive.",
          credit: "Wikimedia Commons / Azcolvin429 (CC BY-SA 3.0)" }
      ]
    },
    "Breeder's equation R = h²·S": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "Breeder's equation diagram: S (breeders − population mean) × h² yields R (next-gen shift). h² = 0 zeros R no matter how strong S is.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Narrow vs broad heritability": {
      exAnswer: "h² = V_A/V_P responds to selection because additive effects transmit predictably from parent to offspring (each allele contributes independently). H² = V_G/V_P also includes dominance (V_D, depends on which alleles meet) and epistasis (V_I, depends on which loci combine) — these reshuffle every generation under random mating, so selecting on them gives unpredictable offspring. The breeder's equation uses h², not H², for this reason.",
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Additive_and_Dominance_Effects.png/800px-Additive_and_Dominance_Effects.png",
          caption: "Single-locus diagram showing additive vs dominance contributions — only the additive part transmits faithfully and shows up in h².",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Parent-offspring regression estimates h²": {
      exAnswer: "A slope of ~0 (offspring trait does not track parental trait) means the trait is essentially environmental — h² ≈ 0, so R = h²·S = 0 regardless of selection strength. Even if you select the tallest parents every generation, offspring revert to the population distribution because the variation isn't heritable. This is why field biologists ALWAYS estimate h² before predicting evolutionary response.",
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Galton_experiment.png/800px-Galton_experiment.png",
          caption: "Galton parent–offspring scatter: regression slope ≈ h². Steeper slope, more heritable; flat line, environmentally driven.",
          credit: "Wikimedia Commons / Puekai (Public domain)" }
      ]
    },
    "Reaction norm": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Phenotypic_plasticity_diagram.svg/800px-Phenotypic_plasticity_diagram.svg.png",
          caption: "Reaction norm plot — phenotype as a function of environment for a single genotype. Crossing lines between genotypes signal G×E.",
          credit: "Wikimedia Commons / Smartse (CC BY-SA 3.0)" }
      ]
    }
  });

  // ===================== L07 =====================
  window.addCardPatches('L07', {
    "Selection in the wild": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "Galápagos medium ground finch — the species in which the Grants tracked selection in the wild and verified the breeder's equation in real time.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" }
      ]
    },
    "Geospiza fortis": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "Geospiza fortis — the medium ground finch on Daphne Major; its ~9.3 mm mean beak depth shifted to ~9.7 mm after the 1977 drought.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg",
          caption: "Gould's 1845 illustration of Darwin's Galápagos finches; G. fortis is one of the four species drawn — the long-term study system for measurable selection.",
          credit: "Wikimedia Commons / John Gould (Public domain)" }
      ]
    },
    "Selection on beak depth": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "After the 1977 Daphne Major drought, only deeper-beaked G. fortis cracked the surviving hard seeds; the next generation inherited deeper beaks — selection caught in action within a single year.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" }
      ]
    },
    "Industrial melanism": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Lichte_en_zwarte_versie_berkenspanner.jpg/800px-Lichte_en_zwarte_versie_berkenspanner.jpg",
          caption: "Light (typica) and dark (carbonaria) peppered moth morphs on a clean tree: typica camouflaged on lichen; under industrial soot, the visibility relationship inverts and carbonaria wins.",
          credit: "Wikimedia Commons / Martinowksy (CC BY-SA 3.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Biston.betularia.7200.jpg/800px-Biston.betularia.7200.jpg",
          caption: "Biston betularia f. typica — the pale form that dominated pre-industrial England.",
          credit: "Wikimedia Commons / Public domain" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Biston.betularia.f.carbonaria.7209.jpg/800px-Biston.betularia.f.carbonaria.7209.jpg",
          caption: "Biston betularia f. carbonaria — the dark melanic form that surged to >95% in polluted areas.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Biston betularia": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Lichte_en_zwarte_versie_berkenspanner.jpg/800px-Lichte_en_zwarte_versie_berkenspanner.jpg",
          caption: "Both peppered-moth morphs side-by-side on the same trunk — bird predation differentially favored each form depending on background, providing the cleanest 'textbook case' of natural selection.",
          credit: "Wikimedia Commons / Martinowksy (CC BY-SA 3.0)" }
      ]
    },
    "Antibiotic resistance": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Human_neutrophil_ingesting_MRSA.jpg/800px-Human_neutrophil_ingesting_MRSA.jpg",
          caption: "MRSA cells (yellow) being engulfed by a neutrophil — antibiotic selection pressure in hospitals selected for pre-existing methicillin-resistant variants of S. aureus.",
          credit: "Wikimedia Commons / NIAID (Public domain)" }
      ]
    },
    "Artificial selection": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Adisey_fox.JPG/800px-Adisey_fox.JPG",
          caption: "A tame Russian silver fox descended from Belyaev's domestication experiment — striking evidence that artificial selection on a single behavioral trait (tameness) reshapes morphology and physiology in only ~10 generations.",
          credit: "Wikimedia Commons / Infykun (CC BY-SA 3.0)" }
      ]
    },
    // L07 extra-card images (definitions complete; just images)
    "Three requirements for measurable evolution in nature": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "The Grants' Daphne Major study satisfies all three criteria — heritable beak variation, differential drought survival, and measurable trait shift across generations.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" }
      ]
    },
    "Grants' Galápagos finches — predicted vs observed R": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "G. fortis on Daphne Major — pre-drought beak depth 9.31 mm, post-drought survivors 9.84 mm. With h² ≈ 0.78 and S ≈ 0.53 mm, predicted R ≈ 0.41 mm matched the observed shift.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "Independent measurement of S, h², and R is what makes the Grants' finch study a complete real-world test of the breeder's equation.",
          credit: "Wikimedia Commons / Public domain" }
      ]
    },
    "Peppered moth industrial melanism — what was actually selected?": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Lichte_en_zwarte_versie_berkenspanner.jpg/800px-Lichte_en_zwarte_versie_berkenspanner.jpg",
          caption: "Both morphs of Biston betularia on a lichen-covered trunk: bird predators selectively pick off the visible morph, shifting allele frequencies based on background — not by inducing the cortex-transposon mutation itself.",
          credit: "Wikimedia Commons / Martinowksy (CC BY-SA 3.0)" }
      ]
    },
    "Antibiotic resistance — speed and predictability": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Human_neutrophil_ingesting_MRSA.jpg/800px-Human_neutrophil_ingesting_MRSA.jpg",
          caption: "MRSA — methicillin-resistant S. aureus rose to clinical dominance within ~2 years of methicillin's introduction. Strong directional selection on pre-existing rare variants.",
          credit: "Wikimedia Commons / NIAID (Public domain)" }
      ]
    },
    "Domestication = artificial selection (greyhound case)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Adisey_fox.JPG/800px-Adisey_fox.JPG",
          caption: "Belyaev's tame silver fox: artificial selection drove visible behavioral, coat, and skull changes in ~50 years — selection differentials orders of magnitude larger than wild rates.",
          credit: "Wikimedia Commons / Infykun (CC BY-SA 3.0)" }
      ]
    },
    "Why field selection studies need longitudinal data": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Geospiza_fortis.jpg/800px-Geospiza_fortis.jpg",
          caption: "The Grants spent 40+ years on Daphne Major banding individual G. fortis — only multi-year tracking ruled out drift, migration, plasticity, and sampling bias as alternatives.",
          credit: "Wikimedia Commons / putneymark (CC BY-SA 2.0)" }
      ]
    },
    "Influenza antigenic drift vs antigenic shift": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Human_neutrophil_ingesting_MRSA.jpg/800px-Human_neutrophil_ingesting_MRSA.jpg",
          caption: "Pathogen evolution under host immunity (here MRSA, conceptually similar to flu) — surface-protein change drives the host immune-escape that necessitates annual flu vaccines.",
          credit: "Wikimedia Commons / NIAID (Public domain)" }
      ]
    },
    "When does R = h²·S fail to predict the next generation?": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Response_to_selection.jpg/800px-Response_to_selection.jpg",
          caption: "When predicted R diverges sharply from observed, one of the breeder's-equation assumptions has broken — most often parent-offspring environmental correlation inflated h².",
          credit: "Wikimedia Commons / Public domain" }
      ]
    }
  });

  // ===================== L08 =====================
  window.addCardPatches('L08', {
    "Adaptation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Eye evolution sequence — the textbook example illustrating adaptation as both trait (a finished eye) and process (cumulative selection through functional intermediates).",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    },
    "Gradual evolution": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "'Half an eye' is useful — every stage from photoreceptor patch to lensed camera-eye exists in living taxa today, refuting the irreducibility critique.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    },
    "Stepwise eye evolution": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Light-sensitive patch → cup → pinhole → lensed eye. Each intermediate is a functional design seen in extant lineages (flatworms, limpets, Nautilus, vertebrates).",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Nautilus_pompilius_%28head%29.jpg/800px-Nautilus_pompilius_%28head%29.jpg",
          caption: "Nautilus pompilius — its eye is a true pinhole with no lens; living proof that the pinhole stage is functional and selectable.",
          credit: "Wikimedia Commons / Hans Hillewaert (CC BY-SA 4.0)" }
      ]
    },
    "Convergent evolution of eyes": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Evolution_eye.svg/800px-Evolution_eye.svg.png",
          caption: "Vertebrate (left) and octopus (right) camera eyes — same overall design, but vertebrate retina has photoreceptors facing AWAY from light (with a blind spot); octopus has them facing toward light. Independent origins via similar selective routes.",
          credit: "Wikimedia Commons / Caerbannog (CC BY-SA 3.0)" }
      ]
    },
    "Cis-regulatory mutation": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Drosophila Hox cluster — body-plan diversity across insects mostly tracks WHERE/WHEN these genes are expressed (cis-regulatory changes), not the proteins themselves.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Gene duplication": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Hox genes themselves arose by tandem duplication of an ancestral gene; the four vertebrate Hox clusters trace to two whole-genome duplications.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Neofunctionalization": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "After Hox duplication, individual paralogs evolved tissue-specific roles — the daughter copy gained novel patterning function while the original retained ancestral expression.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Subfunctionalization": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Hox paralogs show sub-functionalization — each copy specializes on a body region/timing window that the ancestor handled alone.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Protein promiscuity": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Eye-lens crystallins were co-opted from heat-shock proteins and metabolic enzymes — selection refined weak side-activities into the primary lens function.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    },
    "Heterochrony": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Antennapedia.jpg/800px-Antennapedia.jpg",
          caption: "Antennapedia mutant fruit fly (right) — a single homeotic mutation re-times/re-locates an entire developmental program. Heterochrony works through similar regulatory levers.",
          credit: "Wikimedia Commons / Ktbn (Public domain)" }
      ]
    },
    "Paedomorphosis": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Antennapedia.jpg/800px-Antennapedia.jpg",
          caption: "Developmental retiming (here a homeotic mutation) illustrates how flipping a single regulatory switch can keep an organism in a juvenile or alternative form — the mechanism behind axolotl paedomorphosis.",
          credit: "Wikimedia Commons / Ktbn (Public domain)" }
      ]
    },
    "Peramorphosis": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Antennapedia.jpg/800px-Antennapedia.jpg",
          caption: "Single-gene developmental shifts (Antennapedia transforms antennae into legs) parallel peramorphic evolution — extending or redirecting growth past the ancestral end-point.",
          credit: "Wikimedia Commons / Ktbn (Public domain)" }
      ]
    },
    "Hox gene": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Drosophila Hox cluster — homeotic transcription factors patterning the anterior-posterior axis. Functionally interchangeable across phyla.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Antennapedia.jpg/800px-Antennapedia.jpg",
          caption: "Antennapedia mutant: gain-of-function Hox mutation transforms antennae into legs — a single regulator dramatically rewires body identity.",
          credit: "Wikimedia Commons / Ktbn (Public domain)" }
      ]
    },
    "Colinearity": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Drosophila Hox genes are arranged on the chromosome in the same order as their expression along the body — colinearity, conserved across bilaterians.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Conservation of developmental networks": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "The Hox toolkit is conserved across all bilaterians — flies and mice use homologous genes to pattern the head-to-tail axis, evidence of a single deep-time origin.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Pax6 initiates eye development across phyla; despite radically different eye morphologies, the regulatory backbone is conserved from flies to vertebrates.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    },
    "Vestigial structure": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Whales_skeletal_system_comparison.png/800px-Whales_skeletal_system_comparison.png",
          caption: "Whale skeletons preserve vestigial pelvic bones — leftover hindlimb anchors from terrestrial mammalian ancestors, expected if cetaceans are modified land mammals (not designed de novo).",
          credit: "Wikimedia Commons / Bosio et al. (CC BY 4.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Tiktaalik_Chicago.JPG/800px-Tiktaalik_Chicago.JPG",
          caption: "Tiktaalik fossil — a transitional fish-tetrapod with both fins and proto-wrist bones, the kind of intermediate that vestigials predict and special-creation does not.",
          credit: "Wikimedia Commons / Eduard Solà (CC BY-SA 3.0)" }
      ]
    },
    "Trade-off": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Evolution_eye.svg/800px-Evolution_eye.svg.png",
          caption: "Vertebrate vs cephalopod eye — the vertebrate retina's inverted layout creates a blind spot, a trade-off (developmental constraint) the octopus eye avoids.",
          credit: "Wikimedia Commons / Caerbannog (CC BY-SA 3.0)" }
      ]
    },
    "Constraint": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Evolution_eye.svg/800px-Evolution_eye.svg.png",
          caption: "Vertebrate eye blind spot — selection cannot 'redesign' the inverted retina mid-history; the inherited developmental layout is a historical constraint.",
          credit: "Wikimedia Commons / Caerbannog (CC BY-SA 3.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Whales_skeletal_system_comparison.png/800px-Whales_skeletal_system_comparison.png",
          caption: "Whale skeletons retain vestigial pelvis — selection couldn't erase the inherited tetrapod body plan even after 50+ million years of marine life.",
          credit: "Wikimedia Commons / Bosio et al. (CC BY 4.0)" }
      ]
    },
    // L08 extra-card images
    "Stepwise eye evolution stages": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Patch → cup → pinhole → lens — the canonical eye-evolution sequence. Each stage exists in living animals and confers fitness on its own.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Nautilus_pompilius_%28head%29.jpg/800px-Nautilus_pompilius_%28head%29.jpg",
          caption: "Nautilus pompilius — a living organism with a true pinhole eye, no lens; demonstrates the pinhole stage is functional in the wild.",
          credit: "Wikimedia Commons / Hans Hillewaert (CC BY-SA 4.0)" }
      ]
    },
    "Neofunctionalization vs subfunctionalization": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Hox paralogs illustrate both fates: some daughter copies took on novel patterning roles (neo-), others split ancestral A-P expression domains (sub-).",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Heterochrony (paedo vs peramorphosis)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Antennapedia.jpg/800px-Antennapedia.jpg",
          caption: "Wild type vs Antennapedia mutant — a regulatory rewiring transforms one body part into another, the same kind of timing/identity switch heterochrony exploits.",
          credit: "Wikimedia Commons / Ktbn (Public domain)" }
      ]
    },
    "Hox genes — A-P body axis": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Drosophila Hox cluster — colinearity between chromosomal order and body-axis expression is conserved from worms to vertebrates.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Cis-regulatory mutations vs structural": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoxgenesoffruitfly.svg/800px-Hoxgenesoffruitfly.svg.png",
          caption: "Pleiotropic developmental TFs (like Hox or Pitx1) tolerate cis-regulatory tweaks because each enhancer is tissue-specific — structural changes break every function the protein had.",
          credit: "Wikimedia Commons / PhiLiP (Public domain)" }
      ]
    },
    "Vestigial structure (definition + examples)": {
      mnem: "Vestiges = leftovers — expected only if structures were inherited from ancestors and modified, never if designed from scratch.",
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Whales_skeletal_system_comparison.png/800px-Whales_skeletal_system_comparison.png",
          caption: "Whale pelvic bones — anchored to nothing, doing nothing locomotor; positive evidence of common descent from terrestrial ancestors.",
          credit: "Wikimedia Commons / Bosio et al. (CC BY 4.0)" },
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Archaeopteryx_lithographica_%28Berlin_specimen%29.jpg/800px-Archaeopteryx_lithographica_%28Berlin_specimen%29.jpg",
          caption: "Archaeopteryx Berlin specimen — feathered theropod with reptilian teeth and tail bones; transitional fossils satisfy the prediction that ancestral features should appear in modified form.",
          credit: "Wikimedia Commons / H. Raab (CC BY-SA 3.0)" }
      ]
    },
    "Adaptation — noun vs verb (trait vs process)": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Saying the eye 'is an adaptation FOR vision' is a strong functional claim — defended only by showing heritability, fitness benefit, and exclusion of exaptation/byproduct alternatives.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    },
    "Protein promiscuity → cooption": {
      images: [
        { src: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Diagram_of_eye_evolution.svg/800px-Diagram_of_eye_evolution.svg.png",
          caption: "Crystallins — the proteins that focus light in the lens — were co-opted from heat-shock proteins and metabolic enzymes. Eye evolution is largely a story of cooption, not de novo invention.",
          credit: "Wikimedia Commons / Matticus78 (CC BY-SA 3.0)" }
      ]
    }
  });
})();
