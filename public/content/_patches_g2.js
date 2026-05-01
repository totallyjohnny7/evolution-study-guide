/* Patches group 2: L05, L07, L08 — written by agent. */
(function () {
  if (!window.FLASHCARD_PATCHES) window.FLASHCARD_PATCHES = {};
  Object.assign(window.FLASHCARD_PATCHES, {
    L05: {
      "Quantitative trait": {
        exAnswer: "It is called quantitative because the phenotype varies along a continuous numerical scale rather than falling into a few discrete classes. Continuous variation arises when MANY loci each contribute a small additive effect (polygenic) and the environment adds noise on top — the central limit theorem then smears the genotype contributions into a smooth bell curve. Implication: there is no single 'tall gene'; height is the sum of small effects from hundreds of loci plus environmental input (nutrition, hormones).",
        mnem: "Quantitative = Continuous + many small genes (polygenic). Mendelian = discrete + one or two big genes."
      },
      "V_A — Additive genetic variance": {
        exAnswer: "V_A must be non-zero. Only V_A passes predictably from parent to offspring because additive allelic effects sum and are transmitted directly through gametes; dominance (V_D) and epistasis (V_I) depend on which alleles HAPPEN to meet at fertilization, so they get scrambled each generation and don't reliably predict offspring values. The breeder's equation R = h²S is built on h² = V_A/V_P — if V_A = 0, h² = 0 and the response R = 0 no matter how strong the selection.",
        mnem: "V_A is the only variance you can SHIP — it travels predictably from parent to kid in gametes."
      },
      "V_D — Dominance variance": {
        exAnswer: "Because dominance depends on the COMBINATION of two alleles at one locus (Aa heterozygote effects), and meiosis breaks that combination apart into single-allele gametes. Each generation the heterozygote-specific effects must be reassembled by chance at fertilization — they don't transmit faithfully. Selection that 'works' on a dominant heterozygote phenotype rebuilds it only when two specific alleles meet again, so V_D doesn't accumulate response across generations the way V_A does.",
        mnem: "Dominance dies at meiosis — the Aa pairing breaks apart and has to be re-rolled each generation."
      },
      "V_I — Epistatic (interaction) variance": {
        exAnswer: "Selection on V_I is inefficient because the favored phenotype depends on a SPECIFIC combination of alleles at TWO OR MORE loci, and recombination breaks those combinations apart every generation. Even if you select B+/E+ black mice, their gametes carry single alleles that get reshuffled at the next fertilization — only a fraction of offspring will inherit the precise multi-locus combo that produces the desired phenotype. Like V_D, V_I depends on co-occurrence that meiosis disrupts.",
        mnem: "Epistasis = teamwork between loci, but recombination keeps shuffling the team — bad for inheritance."
      },
      "V_E — Environmental variance": {
        exAnswer: "NO — selecting the larger-flowered clone produces no evolutionary change in the lineage. The size difference between identical clones is 100% V_E (environmental), so V_A = 0 for that variation, h² = 0, and R = h²·S = 0. The clone's offspring (vegetative or sexual) will revert to the genotype's mean phenotype in whatever environment they grow in. You can pick the bigger clone every generation and never produce a heritable shift — you're selecting on noise.",
        mnem: "V_E vanishes at the next generation — environment isn't inherited, only genes are."
      },
      "Broad-sense heritability (H²)": {
        exAnswer: "The 0.4 gap (H² – h² = 0.4) is non-additive genetic variance — V_D (dominance) plus V_I (epistasis). The trait has substantial total genetic determination (80%), but only HALF of that genetic variance is the additive kind that responds predictably to selection. So the trait is 'genetic' in the broad sense but won't respond to artificial selection as strongly as H² would suggest. Implication: dominance/epistasis dominate the architecture; expect inbreeding depression and heterosis.",
        mnem: "H² is the GENETIC ceiling; h² is the SELECTABLE floor. Gap = dominance + epistasis hiding inside H²."
      },
      "Narrow-sense heritability (h²)": {
        exAnswer: "Heritability is a population/environment-specific RATIO, not an intrinsic property of the trait. h² = V_A/V_P. In malnourished populations, V_E is huge (some kids get enough food, some don't), inflating V_P and shrinking the ratio. In well-fed populations V_E is small, V_P shrinks, and h² goes up — even though V_A is the same. Same genes, different denominators. Higher h² doesn't mean 'more genetic'; it means the environment has been STANDARDIZED so genetic differences shine through.",
        mnem: "h² is a ratio — shrink V_E and h² goes up without changing one gene."
      },
      "Parent-offspring regression": {
        exAnswer: "h² ≈ 0.6 (the slope of offspring vs. mid-parent regression directly estimates narrow-sense heritability). This is a HIGH heritability — selection on tail length should produce a strong, predictable response: R = h²·S, so a selection differential of 1 cm yields ~0.6 cm of next-generation shift. Any value of h² > 0.3 is considered selectable; 0.6 means the trait is one of the more responsive in quantitative genetics.",
        mnem: "Slope = h². Steep parent-kid regression → highly heritable; flat → environmental."
      },
      "Selection differential (S)": {
        exAnswer: "S = 120 – 100 = 20 g (the gap between breeders' mean and population mean). Using R = h²·S = 0.5 × 20 = 10 g. Next-generation predicted mean = 100 + 10 = 110 g. Note: only HALF of the 20 g gap is recovered because half the phenotypic variance is non-additive/environmental. If h² were 1.0 (pure additive genetic), the next-gen mean would equal the breeders' mean (120 g); if h² = 0, no response at all (still 100 g).",
        mnem: "S is the BIG gap (you-vs-the-pack); R is the small gap that actually evolves. R = h²·S."
      },
      "Response to selection (R)": {
        exAnswer: "R = h²·S = 0.5 × 20 g = 10 g. R is the realized shift in the population mean from one generation to the next, which is always less than or equal to S because only the additive genetic fraction (h²) of phenotypic variance is heritable. Here, half of the 20 g breeders-vs-population gap is converted into actual evolutionary change. The other half is non-heritable (V_D, V_I, V_E) and cannot transmit.",
        mnem: "R is the REALIZED shift — what actually moves between generations. R ≤ S always."
      },
      "Breeder's equation": {
        exAnswer: "Because only the ADDITIVE genetic fraction of phenotypic variance — i.e., h² = V_A/V_P — is reliably transmitted to offspring. The breeders' mean differs from the population mean by S, but that S includes BOTH heritable and non-heritable contributions to phenotype (genetic + environmental). Multiplying by h² down-weights S to its heritable share. If h² = 1 (all additive genetic), R = S; if h² = 0 (no heritability), R = 0; for intermediate cases, R is the corresponding fraction of S that the next generation actually inherits.",
        mnem: "R = h²·S — only the heritable SHARE (h²) of the selected gap (S) gets passed on."
      },
      "Phenotypic plasticity": {
        exAnswer: "This is phenotypic plasticity — a single GENOTYPE producing multiple phenotypes depending on environment. It is adaptive because the predator-detection chemicals reliably correlate with predation risk: helmets reduce vulnerability when predators are present, but cost energy and slow swimming when they're absent. A facultative response that matches the environment beats a fixed phenotype that's wrong half the time. Selection acts on the REACTION NORM (the rule for switching), not on the phenotype directly — so the genotype itself is what evolves, by improving the environment-to-phenotype mapping.",
        mnem: "Plasticity = ONE genotype, MANY phenotypes. Same blueprint, environment-dependent build."
      },
      "Reaction norm": {
        mnem: "Flat line = canalized (rigid). Sloped = plastic. Two genotypes' lines crossing = G×E."
      },
      "G×E interaction (V_G×E)": {
        exAnswer: "Crossing reaction norms = G×E interaction. There is NO context-free 'best' genotype — A wins in one environment, B wins in the other, and selection has opposite effects in each. Practical consequences: (1) heritability estimates are environment-specific; (2) breeders selecting in one environment may pick the wrong line for another; (3) maintaining genetic variation is easier (different alleles favored in different conditions); (4) lab-validated genotypes can fail in field deployment.",
        mnem: "G×E = lines CROSS on the reaction-norm plot. Rank order flips with environment."
      },
      "Polyphenic trait": {
        exAnswer: "Polyphenism is DISCRETE plasticity — instead of a smooth gradient of phenotypes (continuous plasticity), the genotype produces a few distinct alternative morphs (winged vs wingless, no in-between). The triggering cue here is population density and food quality (crowding plus nutrient stress). The mechanism is a developmental switch: the cue tips a hormonal threshold (e.g., juvenile hormone titer), which then deterministically drives one developmental path or the other. Same genome, two execution branches.",
        mnem: "Polyphenism = poly (many) phenotypes, but DISCRETE. Like a SWITCH, not a DIAL."
      },
      "Canalization": {
        exAnswer: "FAVORED when the optimum phenotype is the same across environments and developmental robustness reduces costly mismatches — buffering against noise (genetic, environmental, developmental) protects fitness. SELECTED AGAINST when the optimum varies across environments and a plastic response would track it: a canalized genotype is then 'stuck' producing a one-size-fits-all phenotype that's wrong in some conditions. Canalization vs plasticity is itself an evolvable trait that depends on environmental predictability and the cost-benefit of response.",
        mnem: "Canalization = development in a CANAL — same output regardless of input. Robust but rigid."
      }
    },
    L07: {
      "Selection in the wild": {
        exAnswer: "You need to show the selected trait is HERITABLE — that the differential survival translates into a frequency change in the next generation's gene pool. Differential survival alone is just ecology; if the trait isn't heritable (e.g., due to plasticity or pure environment), the next generation reverts and no evolution occurs. The Grants did this by combining (1) survival data with (2) parent-offspring regression for h² and then (3) measuring the actual next-generation mean to confirm R = h²·S.",
        mnem: "Selection in nature needs THREE things: heritable variation, differential reproduction, frequency change across generations."
      },
      "Geospiza fortis": {
        exAnswer: "Selection, not plasticity. The Grants distinguished them by parent-offspring regression: the offspring of deep-beaked survivors had deep beaks, and the slope (h² ≈ 0.78) was high — meaning the trait was heritable and the next-generation mean shift was predicted by R = h²·S. Plasticity would have predicted no slope (offspring revert to the baseline regardless of parent beak), and beak depth wouldn't track parental phenotype. The 1977 drought killed birds with shallow beaks because only large hard seeds remained, and survivors transmitted deep-beak genes to a measurable next-generation shift.",
        mnem: "G. fortis = Daphne Major medium ground finch — the Grants' poster bird for selection in real time."
      },
      "Selection on beak depth": {
        exAnswer: "It disproved the claim that evolution by natural selection is too slow to observe in real time — that you can only INFER it from fossils across millions of years. The Grants showed measurable, predicted, replicable evolution in ONE generation (1977 drought to 1978 hatchlings). Predicted R = h²·S ≈ 0.41 mm matched the observed shift. This was a falsifiable prediction met by data — the textbook proof that evolutionary biology is a predictive science, not a historical narrative.",
        mnem: "1977 drought + 1978 deep-beaked babies = evolution in 12 months."
      },
      "Industrial melanism": {
        exAnswer: "The melanic morph frequency DROPS and the light morph rebounds. With cleaner air, lichen returns and trunks lighten — the visibility-vs-bird-predation balance now favors LIGHT moths against pale bark. Selection direction reverses because the SAME predator pressure now sees dark moths as the more visible, attacked morph. This was actually observed in Britain post-Clean Air Act (1956): melanic frequency fell from >90% to ~10% in industrial areas by the 1990s — selection in BOTH directions documented in the same species.",
        mnem: "Industrial melanism = evolution toward black with soot, BACK to peppered with clean air."
      },
      "Biston betularia": {
        exAnswer: "Because it has every element a clean selection study needs: (1) clear MECHANISM — bird predation against contrasting backgrounds, demonstrated experimentally by Kettlewell's mark-recapture; (2) HISTORICAL records of morph frequencies tracking pollution; (3) GENETIC basis identified — a transposon insertion in the cortex gene (van't Hof et al., 2016); (4) REVERSAL after the Clean Air Act, providing two directions of selection, ruling out drift; (5) parallels in geographically separate populations. Few systems have all five.",
        mnem: "Biston betularia = the moth, the myth, the textbook example. Soot, predation, reversal."
      },
      "Antibiotic resistance": {
        exAnswer: "(1) FORCES: strong directional natural selection (drug kills susceptibles), with mutation and lateral gene transfer as variation sources. (2) ALLELE FREQUENCY CHANGE: pre-existing resistance alleles (β-lactamases, altered PBPs) rose from rare to dominant — drug doesn't CREATE resistance, it SELECTS pre-existing variants. (3) INTERVENTIONS: antibiotic stewardship (prescribe less, narrower-spectrum); finish full courses; rotate drugs; combination therapy (requires simultaneous mutations, probability drops to ~10⁻¹⁸); rapid diagnostics; infection control.",
        mnem: "Antibiotic resistance = directional selection on bacteria, real-time, in your hospital."
      },
      "Artificial selection": {
        exAnswer: "Mechanistically the SAME process: heritable variation + differential reproduction → frequency change in the next generation. The only difference is that HUMANS choose the breeders rather than the natural environment. In teosinte→maize: selection differential was massive (humans planted only the best ears each year over 9000+ years), so even a modest h² generated huge cumulative R. Same R = h²·S equation; just a much stronger S than nature typically delivers. Domestication is natural selection's evidence — Darwin used it as proof of principle in Origin.",
        mnem: "Artificial = same mechanism, human-chosen breeders. Big S, fast R, dramatic results in geological eyeblink."
      }
    },
    L08: {
      "Adaptation": {
        exAnswer: "TRAIT sense: the leaf-shaped body of Phyllium IS an adaptation — a heritable feature shaped by past selection FOR the current function of camouflage from predators. PROCESS sense: the lineage UNDERWENT adaptation — over many generations, less leaf-like ancestors were selected against by visual predators and gene frequencies shifted toward leaf-mimicking phenotypes. The trait is the noun (the result); the process is the verb (the cause). Calling something AN adaptation FOR X is a strong claim requiring evidence of historical selection for that specific function (otherwise it might be exaptation or byproduct).",
        mnem: "Adaptation = the noun (trait result) AND the verb (selection process). Same word, two claims."
      },
      "Gradual evolution": {
        exAnswer: "Living intermediates: (1) light-sensitive PATCH — flatworm eyespots (Planaria) detect light direction. (2) CUPPED patch — limpet eye, deeper cup gives directional info. (3) PINHOLE eye — Nautilus, no lens, blurry image. (4) Lensed CAMERA eye — vertebrates, octopuses. (5) Compound eye — insects, crustaceans. Each is functional in its bearer today; each provides fitness benefit at its level. 'Half an eye' is half-better than no eye — Darwin's own answer in Origin Ch. 6. Selection sees fitness gradients, not 'designs in progress'.",
        mnem: "Half an eye is BETTER than no eye — every step on the gradient confers fitness."
      },
      "Stepwise eye evolution": {
        exAnswer: "(1) Light-sensitive PATCH: planarian flatworm eyespot, jellyfish ocelli. (2) CUP: limpet (Patella), some snails — pigmented cup gives directional sensitivity. (3) PINHOLE: Nautilus — open chamber, no lens, dim and blurry but localizes images. (4) LENSED camera eye: vertebrates, cephalopods (squid, octopus); also independently in some snails (e.g., Strombus). All four stages exist in living animals TODAY — proof that intermediates are functional, not hypothetical.",
        mnem: "Patch (planarian) → Cup (limpet) → Pinhole (Nautilus) → Lens (vertebrate/octopus). Living museum."
      },
      "Convergent evolution of eyes": {
        exAnswer: "Independent origin from a common ancestor that had only a basic photoreceptor cell — convergent evolution onto similar engineering solutions, but from different developmental starting points. Vertebrate retinas have photoreceptors pointing AWAY from light (light passes through neurons first → blind spot at the optic nerve); cephalopod retinas have photoreceptors pointing TOWARD light (no blind spot). Same camera-eye 'design' can be reached by different developmental routes, showing selection finds similar optima while constraint-history differs. Common ancestor had photoreceptors but not eyes; eyes evolved >40 times.",
        mnem: "Vertebrate eye = backward retina (blind spot). Octopus eye = forward retina (none). Same engineering, different history."
      },
      "Cis-regulatory mutation": {
        exAnswer: "Most likely in a CIS-REGULATORY element (an enhancer or promoter) of the pigmentation gene — not in the protein-coding sequence itself, since the proteins are 99% identical. This means a mutation altering WHEN/WHERE the gene is expressed (which wing cells, which developmental stage) without changing the protein everywhere it's used. This pattern is now known to dominate morphological evolution: regulatory rewiring is more evolvable than protein-coding change because it's MODULAR — tissue-specific, low pleiotropic cost. (Carroll/evo-devo lab work; sticklebacks, Drosophila, finches.)",
        mnem: "Cis-regulatory = changes WHERE/WHEN, not WHAT. Modular tweaking, low pleiotropy."
      },
      "Gene duplication": {
        exAnswer: "Without duplication, any mutation that alters an essential gene (like the ancestral globin) would break the original function and likely be lethal. Duplication produces a REDUNDANT extra copy — one copy keeps doing the original job (oxygen transport), freeing the second copy from purifying selection so it can accumulate mutations and explore new functions (myoglobin oxygen storage, fetal-specific γ-globin, etc.). Without the spare, selection is too strong to permit divergence; duplication is a precondition because it provides a free-to-mutate substrate.",
        mnem: "Gene duplication = spare copy. Original keeps the day job; the spare is free to invent a new one."
      },
      "Neofunctionalization": {
        exAnswer: "The β-globin (or other globin) lineage RETAINED ancestral oxygen-transport function in red blood cells; the MYOGLOBIN copy NEOFUNCTIONALIZED — it diverged to specialize in oxygen storage in muscle tissue with much higher O₂ affinity (sigmoidal vs. hyperbolic binding curve). Sequence and function diverged in the myoglobin copy while the original globin job was preserved. Diagnostic: one copy retains the ancestral role, the other does something genuinely NEW.",
        mnem: "Neo = NEW function in one copy. The other copy keeps the original day job."
      },
      "Subfunctionalization": {
        exAnswer: "In NEOFUNCTIONALIZATION, one copy gains a brand-NEW function not in the ancestor; the other retains all original duties. In SUBFUNCTIONALIZATION, the ancestral protein already did A AND B; after duplication the copies SPLIT existing duties (one does A only, the other does B only) — no new function arises, just division of labor. Often happens via cis-regulatory mutations restricting expression to different tissues. Diagnostic: sum of derived functions = ancestral function (sub) vs. derived function exceeds ancestral (neo).",
        mnem: "Sub = SPLIT old duties (division of labor). Neo = NEW duty entirely."
      },
      "Protein promiscuity": {
        exAnswer: "Promiscuity provides a STARTING SUBSTRATE for selection — the duplicate doesn't have to invent a new activity from scratch, it has weak side-affinity for cortisol/aldosterone already, and selection sharpens that weak activity into a primary function via successive point mutations in the binding pocket. Without pre-existing promiscuity, there'd be no fitness gradient for selection to climb. This is why MOST 'novel' enzymes evolve from ancestors with broad specificity rather than de novo: promiscuity = the raw material of innovation.",
        mnem: "Promiscuity = sloppy side-jobs that selection can sharpen into a new specialty."
      },
      "Heterochrony": {
        exAnswer: "PAEDOMORPHOSIS — domestic dogs retain JUVENILE-wolf traits into adulthood (floppy ears, shortened snout, playful behavior, retained begging/whining). Likely arose via slowed/extended development of certain tissues; the adult dog is essentially a juvenile wolf in body and behavior. Belyaev's silver-fox tameness experiment recapitulates this: selecting for tameness alone produced floppy ears, curled tails, piebald coats — the 'domestication syndrome' is a heterochronic shift toward neoteny.",
        mnem: "Heterochrony = HETERO (different) + CHRONOS (time) — change in developmental timing."
      },
      "Paedomorphosis": {
        exAnswer: "Paedomorphic because the axolotl reproduces while still in its larval (juvenile) form — gills, fins, aquatic morphology — instead of metamorphosing into a terrestrial adult salamander like its ancestor. The thyroid signaling that drives metamorphosis fails to fire; sexual maturity arrives in the larval body. SELECTIVE CONTEXT: stable aquatic environments (Mexican lake) where the cost of metamorphosis (predation risk during transition, resource shift) exceeds the benefit. If the water never dries up, why bother becoming a land salamander?",
        mnem: "Paedomorphic = PEDIATRIC (kid-like) shape kept by adult. Axolotl = forever larva."
      },
      "Peramorphosis": {
        exAnswer: "Peramorphosis EXTENDS development past the ancestral end-point, producing exaggerated/overgrown adult features (Irish elk antlers, ~4 m wide). Paedomorphosis does the OPPOSITE — TRUNCATES development so the adult retains juvenile features. Both are heterochronic mechanisms (timing changes), but pera = development continues longer/faster (more mature than ancestor) and paedo = development stops earlier/slower (less mature than ancestor). Same gene toolkit, different temporal program.",
        mnem: "Pera = PAST the endpoint (dev extended). Paedo = stops at PEDIATRIC stage (dev truncated)."
      },
      "Hox gene": {
        exAnswer: "It reveals deep HOMOLOGY — the body-plan-patterning toolkit was already present in the common ancestor of flies and mice (~600 mya) and has been conserved with minimal change. The protein domains binding DNA are nearly identical. Body-plan diversity comes not from inventing new Hox genes but from regulatory rewiring (when/where they're expressed) and downstream target evolution. The 'genetic toolkit' is shared; the deployment is what diverged. Foundational insight of evo-devo (Lewis, Gehring, Carroll).",
        mnem: "Hox genes = the universal body-axis toolkit. Same genes from fly to human."
      },
      "Colinearity": {
        exAnswer: "COLINEARITY — chromosomal arrangement matches body-axis expression order (3' anterior genes at one end, 5' posterior genes at the other). It's evolutionarily significant because it suggests a tightly conserved regulatory mechanism: progressive activation along the chromosome correlates with progressive activation along the body axis (timing colinearity in vertebrates). This deep order constraint has been preserved across >600 million years from flies to humans — one of the most conserved features of bilaterian genomes — implying strong selection against rearrangement.",
        mnem: "Colinearity = chromosomal order = body order. Anterior genes at one end, posterior at the other."
      },
      "Conservation of developmental networks": {
        exAnswer: "It strongly suggests the bilaterian common ancestor (~600 mya) ALREADY had some kind of light-sensing organ that used Pax6 in its specification — not a 'modern' eye, but at least a photoreceptive structure with a Pax6-driven developmental program. Eyes then ELABORATED INDEPENDENTLY in different lineages (>40 times), each elaborating the same ancestral Pax6 toolkit into different eye types (compound, camera, etc.). Pax6 is the 'master switch'; the diversity of eye morphology reflects different downstream rewiring, not different upstream regulators. Convergence at the morphology level + homology at the developmental level.",
        mnem: "Pax6 turns on EYE in fly, mouse, octopus — shared switch from the bilaterian ancestor."
      },
      "Vestigial structure": {
        exAnswer: "STRONGEST evolutionary argument: vestigials are EXPECTED if structures are inherited from ancestors and modified by descent — they are leftovers of ancestral function (whale ancestors had legs; the pelvis is the bone-cage remnant). Evolution rules out PURE-DESIGN explanations: a designer building each species from scratch would not include nonfunctional appendix tissue or pelvic bones in a fully aquatic mammal. Vestigials are positive evidence FOR descent with modification, not against evolution — they're the smoking gun of common ancestry.",
        mnem: "Vestigial = old hardware not yet uninstalled. Whale pelvis = legacy code from a four-legged ancestor."
      },
      "Trade-off": {
        exAnswer: "Trade-off between speed and endurance — cheetah muscle is dominated by FAST-TWITCH (Type IIb) fibers optimized for explosive ATP production via anaerobic glycolysis. These produce maximum force but generate massive heat and lactate; body temperature can spike from 38°C to 41°C in a 30-second sprint, forcing the cheetah to stop or risk heat stroke. Designing muscle for sustained pace would require slow-twitch (Type I, aerobic) fibers, which sacrifice peak speed. Cheetahs cannot be both fastest and most enduring; selection picked sprint at the cost of endurance.",
        mnem: "Trade-off = improving X costs Y. Cheetah picked SPRINT, paid for it in heat and endurance."
      },
      "Constraint": {
        exAnswer: "The vertebrate spine evolved as a horizontal beam in 4-legged ancestors (load distributed across four columns); when humans became bipedal (~5–7 mya), the same beam was repurposed vertically as a load-bearing tower — a HISTORICAL CONSTRAINT. Selection cannot redesign from scratch; it can only tweak the inherited horizontal-spine plan. So we get an S-curve compromise that works but is structurally suboptimal — back pain, slipped discs, sciatica. A purpose-built bipedal spine would look very different, but no gradual mutation-by-mutation path from quadruped to such a design exists. Constraint = path-dependence.",
        mnem: "Constraint = selection works on what it INHERITED, not what it would build from scratch."
      }
    }
  });
})();
