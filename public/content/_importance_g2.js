/* Importance content (group 2: L05, L07, L08) — written by agent. */
(function () {
  if (!window.addCardPatches) return;

  /* ============================================================
   * L05 — Quantitative Genetics, Selection, Plasticity
   * ============================================================ */
  window.addCardPatches('L05', {
    "Quantitative trait": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Quantitative traits are the bridge between Mendelian genetics and the math of evolution — Robbins will hit you on this because the WHOLE rest of L05 (V_P partition, h², breeder's equation) only makes sense once you accept that height/beak-depth/yield aren't single-gene traits.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Continuous distribution = MANY loci of small effect + environment.</li>
  <li>The polygenic threshold ≈ "5+ loci" usually produces a roughly Gaussian phenotype distribution under additive contributions.</li>
  <li>Classic exam examples: human stature, milk yield, beak depth, fecundity, body mass.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation of L05.</strong> Every variance equation downstream (V_P = V_A + V_D + V_I + V_E, h² = V_A/V_P, R = h²·S) presupposes that the trait is quantitative.</li>
  <li><strong>It explains Darwin's puzzle.</strong> Continuous variation seemed incompatible with Mendelian "particle" inheritance until Fisher (1918) showed many small loci sum to a Gaussian — that's the whole logical bridge.</li>
  <li><strong>Robbins-bait.</strong> Expect a trick question where a discrete trait (sickle cell, blood type) is dressed up to look quantitative. The tell: continuous distribution, not discrete categories.</li>
</ol>
<h4>vs Mendelian (qualitative) trait</h4>
<ul>
  <li>Mendelian: 1-2 loci, discrete classes (purple/white pea flowers).</li>
  <li>Quantitative: many loci + environment, continuous distribution.</li>
</ul>`
    },

    "V_A — Additive genetic variance": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> V_A is the ONLY variance component that responds predictably to selection — if the breeder's equation works, V_A is doing the work. Robbins will hit you on this because students confuse V_A with "all genetic variance."</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_A = additive contributions of alleles, summed across loci.</li>
  <li>h² = V_A / V_P (narrow-sense heritability — the one that matters).</li>
  <li>If V_A = 0, then h² = 0, then R = h²·S = 0 — NO evolutionary response, no matter how strong the selection.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the engine of evolution.</strong> Additive effects are the only ones that pass faithfully from parent to offspring — because each allele contributes a fixed effect regardless of partner.</li>
  <li><strong>Robbins-bait: V_A is not "total genetic variance."</strong> V_G = V_A + V_D + V_I. Only the V_A piece of V_G predicts response to selection. Students who write h² = V_G/V_P are confusing broad- and narrow-sense.</li>
  <li><strong>Selection erodes V_A.</strong> Sustained directional selection fixes favored alleles, depleting V_A and slowing further response — that's why long-term selection eventually plateaus.</li>
  <li><strong>Connects to the breeder's equation.</strong> R = h²·S = (V_A/V_P)·S — V_A is buried inside h².</li>
</ol>`
    },

    "V_D — Dominance variance": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> V_D is the "non-additive same-locus" variance — it affects phenotypes but DOES NOT respond predictably to selection because heterozygote effects are reshuffled by recombination each generation. Exam-trap territory.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_D arises from interactions between alleles AT THE SAME LOCUS (e.g., heterozygote advantage).</li>
  <li>V_G = V_A + V_D + V_I (V_D is one of three genetic components).</li>
  <li>H² (broad) includes V_D; h² (narrow) does NOT.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Why it doesn't predict response.</strong> Dominance effects depend on which TWO alleles meet — segregation and recombination scramble these combinations every generation. Selection cannot "lock in" dominance gain.</li>
  <li><strong>Classic Robbins-trap.</strong> "If a trait has high broad-sense heritability, will it respond strongly to selection?" Wrong answer: yes. Right answer: only if V_A is the bulk of V_G. A trait whose H² is mostly V_D will respond weakly.</li>
  <li><strong>Inbreeding depression connects here.</strong> Inbreeding exposes recessive alleles → dominance variance becomes visible as fitness loss.</li>
</ol>
<h4>vs V_A</h4>
<ul>
  <li>V_A: additive effects, each allele contributes independently → predictable inheritance.</li>
  <li>V_D: same-locus interactions (heterozygote ≠ midpoint) → reshuffled, non-predictable.</li>
</ul>`
    },

    "V_I — Epistatic (interaction) variance": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> V_I is the "non-additive cross-locus" variance — alleles at DIFFERENT loci interacting. Like V_D, selection on V_I is inefficient because epistatic combinations get broken up by recombination.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_I = interaction variance from ≥2 loci (epistasis).</li>
  <li>V_G = V_A + V_D + V_I. V_I is the third genetic component.</li>
  <li>Classic example: B/E coat-color loci in mice — B+/ee gives yellow regardless of B genotype.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same logic as V_D, different scope.</strong> Recombination breaks up the multi-locus combinations each generation, so the interaction effect doesn't transmit faithfully.</li>
  <li><strong>Why the breeder's equation only uses V_A.</strong> R = h²·S works because additive effects are the ones that are "particulate" in Fisher's sense. Epistatic and dominance effects are context-dependent on partner alleles.</li>
  <li><strong>Robbins-bait.</strong> Be ready to write V_P = V_A + V_D + V_I + V_E from memory. The V_I term is easy to forget.</li>
</ol>
<h4>vs V_D</h4>
<ul>
  <li>V_D: alleles at the SAME locus interact (e.g., dominance).</li>
  <li>V_I: alleles at DIFFERENT loci interact (e.g., epistasis).</li>
</ul>`
    },

    "V_E — Environmental variance": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> V_E is phenotypic variance with NO genetic basis — selection on V_E produces ZERO evolution. This is THE recurring Robbins exam trap: "selection happened, but did evolution?"</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_P = V_G + V_E (environmental component is separate from genetic).</li>
  <li>If V_A = 0 and V_E > 0, h² = 0 and R = 0 regardless of S.</li>
  <li>V_E shrinks h² without changing what's evolutionarily possible — high V_E just dilutes the signal.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The "selection ≠ evolution" point.</strong> Selection on environmentally-determined trait differences produces no allele-frequency change. Critical exam concept.</li>
  <li><strong>Why heritability is environment-specific.</strong> Increase V_E (stressful, variable environment) → h² drops, even if V_A is unchanged. h² is NOT an intrinsic property of the trait.</li>
  <li><strong>Robbins-bait scenario.</strong> "Tall parents have tall offspring because they share rich nutrition" — that's V_E, not V_A. Looks like heritability but isn't.</li>
  <li><strong>Common-garden experiments separate V_E from V_G.</strong> Grow genotypes in identical conditions → any remaining variance is genetic.</li>
</ol>`
    },

    "Broad-sense heritability (H²)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> H² (capital H) is the TOTAL genetic share of phenotypic variance — but it does NOT predict response to selection. Robbins WILL test you on h² vs H² discrimination.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>H² = V_G / V_P = (V_A + V_D + V_I) / V_P.</li>
  <li>H² ranges 0 to 1. Always H² ≥ h².</li>
  <li>The gap (H² − h²) tells you how much of the genetic variance is non-additive (dominance + epistasis).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Distinguishes "is this trait genetic?" from "will it evolve?"</strong> H² answers the first, h² answers the second. Different questions.</li>
  <li><strong>Robbins-bait scenario.</strong> H² = 0.8 but h² = 0.4 → trait is 80% genetic but only 40% additive — selection responds modestly. Easy to get wrong.</li>
  <li><strong>Used in twin studies.</strong> Identical twins share V_G entirely, so MZ–DZ comparisons estimate H², not h².</li>
  <li><strong>Population/environment specific.</strong> Same caveat as h² — change the population or environment and H² shifts.</li>
</ol>
<h4>vs h² (narrow-sense)</h4>
<ul>
  <li>H²: V_G / V_P — total genetic share.</li>
  <li>h²: V_A / V_P — additive share, predicts evolution.</li>
</ul>`
    },

    "Narrow-sense heritability (h²)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> h² (lowercase) is THE most important number in quantitative genetics — it's the slope of the parent-offspring regression and the gating factor in the breeder's equation. Robbins will hit you on this.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>h² = V_A / V_P. Range 0 to 1.</li>
  <li>Estimated from parent-offspring regression slope.</li>
  <li>Predicted via breeder's equation: R = h²·S.</li>
  <li>Examples (memorize ranges, not absolute values): human height h² ≈ 0.7-0.8; Galápagos finch beak depth h² ≈ 0.78 (Grants); IQ h² ≈ 0.5 in well-fed populations, ~0.1 in malnourished.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the response-to-selection predictor.</strong> No other quantity directly converts a selection differential into next-gen mean change.</li>
  <li><strong>Population- and environment-specific.</strong> Same h² value isn't transferable. Increase V_E → h² drops; fix favorable alleles → V_A drops → h² drops.</li>
  <li><strong>Robbins-bait: h² ≠ "genetic determinism."</strong> A trait with h² = 0.8 is 80% additive-variance-explained IN THIS POPULATION. It does NOT mean an individual's trait is "80% genes."</li>
  <li><strong>Long-term selection erodes h².</strong> Strong selection fixes alleles → V_A → 0 → h² → 0. That's why dog-breed traits "plateau" after generations.</li>
</ol>`
    },

    "Parent-offspring regression": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The slope of offspring trait vs. mid-parent trait IS h². This is the operational, measurable definition Robbins expects you to know.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Slope of regression = h² (narrow-sense heritability).</li>
  <li>Slope = 0 → trait is purely environmental (V_A = 0).</li>
  <li>Slope = 1 → trait is fully additive-heritable (V_A = V_P).</li>
  <li>Mid-parent value = average of mother + father trait.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Connects theory to data.</strong> All the V_A/V_P math is abstract until you realize h² = a regression slope you can measure with a ruler.</li>
  <li><strong>How the Grants got h² ≈ 0.78 for finch beak depth.</strong> They measured 200+ parent-offspring pairs across years and fitted the regression — that's how h² became a real number, not a theoretical placeholder.</li>
  <li><strong>Robbins-bait.</strong> Be ready to interpret a slope: "Slope 0.6 means h² = 0.6, predict R = 0.6·S." The exam often gives a slope and asks for R.</li>
  <li><strong>Pitfall: shared environment inflates the slope.</strong> If parents and offspring share the same nutrition/microclimate, the slope captures V_A + (parent-offspring environment correlation), overestimating h². Cross-fostering experiments correct this.</li>
</ol>`
    },

    "Selection differential (S)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> S measures the STRENGTH of selection on phenotype — the gap between breeders' mean and population mean. Robbins will hit you on this in a numerical breeder's-equation problem.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>S = mean of breeders − mean of original population.</li>
  <li>Units: same as the trait (cm, g, mm).</li>
  <li>Grants 1977 finches: S ≈ 0.53 mm (post-drought survivors had beaks ~0.53 mm deeper than pre-drought mean).</li>
  <li>S can be positive (favoring larger), negative (favoring smaller), or zero (no selection).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Half of the breeder's equation.</strong> R = h²·S. S captures HOW STRONGLY phenotype is selected; h² captures HOW MUCH of that selection is heritable.</li>
  <li><strong>Measurable in the wild.</strong> Tag individuals, measure trait, see who reproduced — S is just the difference between reproducers' mean and total mean.</li>
  <li><strong>Robbins-bait.</strong> Big S with low h² → small R. Students assume strong selection always means strong evolution — wrong.</li>
  <li><strong>Artificial selection inflates S.</strong> Greyhound breeders pick the top 1% → enormous S → rapid evolution. In nature, S is constrained by ecology.</li>
</ol>`
    },

    "Response to selection (R)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> R is the actual evolutionary change between generations — the OUTPUT of the breeder's equation. Robbins's classic question is "given S and h², compute R."</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>R = mean of next generation − mean of current generation.</li>
  <li>R = h²·S (Lande's breeder's equation, single-trait version).</li>
  <li>Grants 1977: predicted R = 0.78 × 0.53 ≈ 0.41 mm; observed R was close to this.</li>
  <li>Units: same as trait.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>It's the per-generation evolutionary outcome.</strong> R quantifies how much the population mean shifts because of selection — the bottom-line evolutionary change.</li>
  <li><strong>R = 0 if h² = 0.</strong> Critical: even a huge S produces zero response if heritability is zero. This is the "selection ≠ evolution" lesson made numerical.</li>
  <li><strong>Iterating across generations is non-trivial.</strong> R for one generation uses current h². As alleles fix, V_A and h² shift, so R changes generation to generation.</li>
  <li><strong>Robbins exam mechanic.</strong> Expect: "S = X, h² = Y, predict next-generation mean." Step: R = h²·S, new mean = old + R.</li>
</ol>`
    },

    "Breeder's equation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> R = h²·S is THE central equation of quantitative genetics — Robbins will absolutely test it. Memorize and be ready to plug numbers.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>R = h²·S — Lande's breeder's equation.</li>
  <li>R = response to selection (next-gen change in mean).</li>
  <li>h² = narrow-sense heritability (V_A/V_P).</li>
  <li>S = selection differential (breeders mean − population mean).</li>
  <li>Grants finch test case: h² = 0.78, S = 0.53 mm → predicted R = 0.41 mm; observed match.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Predictive power.</strong> The breeder's equation makes evolution quantitative — you can PREDICT next-gen change from measurable inputs. The Grants used it to verify selection in real time.</li>
  <li><strong>The "h² gates everything" lesson.</strong> R = 0 when h² = 0, no matter how strong S. This is the math behind "selection ≠ evolution."</li>
  <li><strong>Single-generation only.</strong> Robbins-trap: don't iterate naively across many generations — V_A erodes as alleles fix, so h² changes too.</li>
  <li><strong>Assumptions matter.</strong> Equation assumes (a) only V_A counts, (b) no parent-offspring environment correlation, (c) no GxE, (d) no major environment shift between generations. Field deviations point to which assumption broke.</li>
</ol>
<h4>How to use on an exam</h4>
<ul>
  <li>Step 1: identify S (mean of breeders − mean of pop).</li>
  <li>Step 2: identify h² (given or from regression slope).</li>
  <li>Step 3: R = h²·S.</li>
  <li>Step 4: next-gen mean = current mean + R.</li>
</ul>`
    },

    "Phenotypic plasticity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> One genotype, many phenotypes — plasticity is the rule, not the exception, and the CAPACITY for plasticity is itself heritable. Robbins-bait: don't confuse "plastic" with "non-genetic."</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Plasticity = same genotype produces different phenotypes in different environments.</li>
  <li>Examples: Daphnia helmet defenses (predator-cue triggered), aphid wing morphs (density-triggered), plant leaf shape under shade vs sun.</li>
  <li>Polyphenism = discrete plasticity (two distinct morphs); continuous plasticity = gradient (height varies with nutrition).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Plasticity itself can evolve.</strong> The shape/slope of the reaction norm is genetically determined and can be selected. Plastic does NOT mean non-genetic.</li>
  <li><strong>Plasticity confounds field evolution studies.</strong> "Beetles are darker this year" could be selection OR plasticity (warmer year → more melanin). Common-garden experiments needed to separate.</li>
  <li><strong>Adaptive plasticity is favored when environment varies predictably.</strong> If the environment fluctuates faster than evolution can respond, plasticity wins.</li>
  <li><strong>Robbins exam trap.</strong> "Selection on a plastic trait" — the response depends on whether selection acts on the genotype's average phenotype or on the slope of plasticity itself.</li>
</ol>`
    },

    "Reaction norm": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A reaction norm IS the visual proof of plasticity — phenotype on Y, environment on X, one line per genotype. Sloped = plastic. Crossing lines = G×E. Robbins definitely shows you a reaction norm graph.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Flat horizontal line = canalized genotype (no plasticity).</li>
  <li>Sloped line = plastic genotype (phenotype responds to environment).</li>
  <li>Parallel lines among genotypes = plasticity but no G×E.</li>
  <li>Non-parallel/crossing lines = G×E (genotypes differ in HOW they respond).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Standard exam graph.</strong> Robbins-bait: "Interpret these reaction norms." Recognize flat (canalized), sloped-parallel (plasticity), and crossed (G×E).</li>
  <li><strong>Slope = magnitude of plasticity.</strong> Steeper slope, more plastic.</li>
  <li><strong>Crossing lines = no context-free "best" genotype.</strong> Genotype A wins in environment 1, B wins in environment 2 — this is G×E. Big deal for breeders: lab-best ≠ field-best.</li>
  <li><strong>Heritability is environment-specific.</strong> When G×E is large, h² estimated in one environment doesn't transfer.</li>
</ol>`
    },

    "G×E interaction (V_G×E)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> G×E means genotypes differ in how they respond to environment — non-parallel reaction norms. The smoking gun: rank order of genotypes flips across environments. Robbins exam trap territory.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_G×E = variance due to genotype-by-environment interaction (a fifth term sometimes added to V_P).</li>
  <li>Visual signature: reaction norms that cross or have very different slopes.</li>
  <li>If lines are parallel = no G×E (just plasticity).</li>
  <li>If lines cross = strong G×E (rank order changes).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>No "best genotype" in absolute terms.</strong> When G×E is strong, you must specify environment before ranking genotypes. Practical implications for crop breeding, animal husbandry.</li>
  <li><strong>Inflates V_P, deflates h² estimates.</strong> Unmeasured G×E gets lumped into noise, lowering apparent heritability.</li>
  <li><strong>Robbins-bait.</strong> Crossing reaction norms is the textbook diagnosis of G×E. Don't call it "just plasticity" — plasticity without G×E means parallel non-flat lines.</li>
  <li><strong>Source of maintained genetic variation.</strong> If G×E exists across patches and migration mixes populations, multiple genotypes can be maintained simultaneously.</li>
</ol>`
    },

    "Polyphenic trait": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Polyphenism = DISCRETE alternative phenotypes from one genotype, triggered by environmental cue. Distinct from continuous plasticity.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Classic examples: aphid winged vs wingless morphs (density cue), locust solitary vs gregarious (density cue), honeybee queen vs worker (royal jelly cue), butterfly seasonal morphs (photoperiod/temperature cue).</li>
  <li>Switch is binary: one threshold determines morph.</li>
  <li>Same genome → categorically different bodies/behaviors.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Adaptive specialization without genetic divergence.</strong> One species can occupy two niches by environmental cue, no speciation needed.</li>
  <li><strong>Tests how much "phenotype" is genetic.</strong> Queen and worker bees are genetically identical — phenotype divergence is 100% from a developmental switch (royal jelly → DNA methylation differences).</li>
  <li><strong>Robbins-bait: vs continuous plasticity.</strong> Continuous plasticity = trait varies along a gradient. Polyphenism = trait jumps between discrete states.</li>
  <li><strong>The threshold itself is heritable.</strong> Just like with plasticity, the switch sensitivity can be selected.</li>
</ol>`
    },

    "Canalization": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Canalization = LACK of plasticity — the same phenotype across environments. Often selected for in core developmental traits where reliable output matters.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Reaction norm = flat horizontal line (no slope).</li>
  <li>Selected for when phenotype optimum is stable across environments.</li>
  <li>Selected against when environment variation requires phenotype adjustment (e.g., body size in variable food regimes).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Counterpoint to plasticity.</strong> Plasticity vs canalization is a classic trade-off — when does the trait need to be reliable vs flexible?</li>
  <li><strong>Buffers development.</strong> Canalized traits (e.g., vertebrate body plan) are robust to perturbations — small mutations or environmental noise don't break them.</li>
  <li><strong>Hidden variation released by stress.</strong> Heat-shock or starvation can decanalize traits, exposing previously-buffered genetic variation to selection — Waddington's classic experiment.</li>
  <li><strong>Robbins-bait.</strong> "Why might selection favor canalization?" — when the optimum is stable. "Why select against?" — when the optimum varies with environment.</li>
</ol>`
    },

    /* L05 extra (flashcards-extra.js) */
    "V_P = V_A + V_D + V_I + V_E": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> THE equation Robbins asks you to write. Phenotypic variance = additive + dominance + epistasis + environment. Memorize letter-perfect.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>V_P = V_A + V_D + V_I + V_E.</li>
  <li>V_G = V_A + V_D + V_I (total genetic variance).</li>
  <li>H² = V_G / V_P (broad-sense).</li>
  <li>h² = V_A / V_P (narrow-sense — predicts response to selection).</li>
  <li>Mnemonic: PADIE — P = A + D + I + E.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Foundation of quantitative genetics.</strong> Every subsequent calculation (h², breeder's equation) starts from this partition.</li>
  <li><strong>Robbins explicitly asks for this expression.</strong> The study guide flags it as a write-from-memory item.</li>
  <li><strong>Only V_A is "evolutionarily clean."</strong> V_D and V_I get reshuffled by recombination; V_E doesn't transmit at all. Hence h² uses V_A alone.</li>
  <li><strong>Sample calculation.</strong> Tomato height: 60% V_A, 10% V_D, 30% V_E. h² = 0.6/(0.6+0.1+0.3) = 0.6. H² = 0.7. Be ready to do this on the exam.</li>
</ol>`
    },

    "Directional selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> One extreme of the distribution is favored — the mean MOVES. Robbins gives you a before/after distribution diagram and asks you to identify which type. Mean shift = directional.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mean shifts toward the favored extreme; variance often shrinks slightly.</li>
  <li>Predicted R = h²·S, with S = mean shift in selected breeders.</li>
  <li>Classic field example: Grants' finches 1977 — drought favored deeper beaks → mean shifted deeper.</li>
  <li>Industrial melanism — pollution favored dark moths → mean shifted darker.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Most common selection mode in changing environments.</strong> When the optimum moves (climate, predator regime, food availability), directional selection is the response.</li>
  <li><strong>The breeder's equation is built for it.</strong> R = h²·S directly predicts the per-generation mean shift.</li>
  <li><strong>Long-term limit: V_A erodes.</strong> Sustained directional selection fixes favored alleles, reducing V_A → h² drops → response slows. Plateau effect in dog breeds.</li>
  <li><strong>Robbins-bait.</strong> Mean MOVES = directional. Mean SAME, variance SHRINKS = stabilizing. Variance INCREASES, two peaks = disruptive. Memorize the discrimination cheat.</li>
</ol>`
    },

    "Stabilizing selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Both extremes selected against, intermediate favored — mean STAYS, variance SHRINKS. Robbins tests this with the human birth weight example.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mean unchanged; variance decreases.</li>
  <li>Classic example: human birth weight — optimal at ~3.5 kg, mortality rises at extremes.</li>
  <li>Long-term variance set by mutation–selection balance: new mutations introduce variance, stabilizing selection prunes it.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Most common selection mode in stable environments.</strong> When the optimum is unchanging, deviations are punished — keeps the population at peak fitness.</li>
  <li><strong>Maintains low variance.</strong> Strong stabilizing selection makes traits look "designed" — narrow distribution around an optimum.</li>
  <li><strong>Robbins-bait.</strong> Mean SAME + variance SHRINKS is the signature. Don't confuse with no-selection (variance unchanged).</li>
  <li><strong>Eliminates V_A over time.</strong> Just like directional, sustained stabilizing erodes additive variance, making future response weaker.</li>
</ol>`
    },

    "Disruptive selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> BOTH extremes favored, intermediates pruned — variance INCREASES, distribution becomes BIMODAL. Robbins flags this because it can seed sympatric speciation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mean often unchanged; variance INCREASES; distribution becomes bimodal.</li>
  <li>Classic example: African seed-cracker finch (Pyrenestes ostrinus) — small beaks crack soft seeds, large beaks crack hard ones; intermediates fail at both.</li>
  <li>Stickleback divergence into limnetic and benthic morphs in lakes is partly disruptive.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Can seed sympatric speciation.</strong> If assortative mating evolves alongside the bimodality, the two peaks become reproductively isolated lineages — speciation without geographic separation.</li>
  <li><strong>Without assortative mating, unstable.</strong> Random mating between morphs regenerates intermediates each generation — costly equilibrium.</li>
  <li><strong>Robbins-bait.</strong> Bimodal distribution = disruptive. Don't confuse with the "two species coexisting" pattern — disruptive is one population splitting.</li>
  <li><strong>Rarer than directional or stabilizing in the wild.</strong> Most environments don't have such sharp two-niche structure.</li>
</ol>`
    },

    "Selection-type discrimination cheat": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Mean-Move = Directional · Squeeze = Stabilizing · Split = Disruptive. THE memorization for Robbins's "identify the selection type" exam question.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Mean shifts → directional. Variance often slightly down.</li>
  <li>Mean unchanged, variance ↓ → stabilizing.</li>
  <li>Mean unchanged or shifted, variance ↑, two peaks → disruptive.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Standard exam mechanic.</strong> Robbins shows you a before/after distribution graph and asks you to name the selection type.</li>
  <li><strong>Each type has a different evolutionary outcome.</strong> Directional → mean change; stabilizing → variance loss; disruptive → potential speciation.</li>
  <li><strong>The discrimination is purely about distribution shape.</strong> Don't overthink — focus on (a) does mean move? (b) does variance grow or shrink? (c) is there bimodality?</li>
</ol>`
    },

    "Breeder's equation R = h²·S": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> R = h²·S — Lande's breeder's equation. Robbins's go-to numerical exam item. Memorize and be ready to plug in.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>R = response = next-gen mean − current mean.</li>
  <li>h² = V_A/V_P = narrow-sense heritability.</li>
  <li>S = mean of selected breeders − population mean.</li>
  <li>Worked example: mean height 170 cm, breeders 178 → S = 8 cm. h² = 0.5. R = 4 cm. Next-gen mean = 174 cm.</li>
  <li>If h² = 0, R = 0, regardless of S.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The math link between selection and evolution.</strong> Quantifies how a phenotypic difference between breeders and pop becomes a genetic difference next gen.</li>
  <li><strong>Why h² (not H²) is in the equation.</strong> Only V_A passes faithfully — V_D and V_I get reshuffled by recombination.</li>
  <li><strong>Single-generation idealization.</strong> Iterating naively is wrong: V_A erodes, h² changes.</li>
  <li><strong>Field test: Grants' 1977 finch data.</strong> h² = 0.78, S = 0.53 mm → predicted R = 0.41 mm; observed shift matched. The equation is testable, not just theoretical.</li>
</ol>`
    },

    "Narrow vs broad heritability": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> h² (narrow) predicts evolution; H² (broad) doesn't. The single most-tested discrimination in L05. Memorize both formulas.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>h² = V_A / V_P (narrow-sense, additive only).</li>
  <li>H² = V_G / V_P = (V_A + V_D + V_I) / V_P (broad-sense, all genetic).</li>
  <li>Always H² ≥ h². The gap = (V_D + V_I) / V_P.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Different questions.</strong> H² answers "is this trait genetic?" h² answers "will it respond to selection?"</li>
  <li><strong>Why dominance/epistasis don't predict response.</strong> Recombination breaks up multi-allele combinations every generation — only additive effects transmit faithfully.</li>
  <li><strong>Twin studies estimate H².</strong> MZ vs DZ twin variance comparisons → broad-sense, not narrow-sense.</li>
  <li><strong>Robbins-bait scenario.</strong> Trait with H² = 0.8 but h² = 0.4 → 80% genetic but only 40% additive → modest response to selection. Easy to get wrong.</li>
</ol>`
    },

    "Parent-offspring regression estimates h²": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Slope of offspring trait vs. mid-parent trait IS h². Operational definition Robbins expects.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Slope = h² (narrow-sense heritability).</li>
  <li>Slope 0 → trait purely environmental.</li>
  <li>Slope 1 → trait fully additive-genetic.</li>
  <li>Grants' finches: h² = 0.78 measured this way for beak depth.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Connects abstract V_A/V_P to a measurable line slope.</strong> You don't have to dissect tomatoes to estimate h² — just measure parents and offspring and fit a line.</li>
  <li><strong>Standard field method.</strong> The Grants used this on Daphne Major; agriculture uses it for crop breeding.</li>
  <li><strong>Pitfall: shared environment inflates slope.</strong> If parents and offspring share microclimate, slope captures V_A + environmental similarity, overestimating h². Cross-fostering or common-garden corrects this.</li>
  <li><strong>Robbins-bait.</strong> Given a slope of 0.6, h² = 0.6 → predicted R = 0.6·S. Be ready for the plug-in.</li>
</ol>`
    },
  });

  /* ============================================================
   * L07 — Empirical Studies of Natural Selection
   * ============================================================ */
  window.addCardPatches('L07', {
    "Selection in the wild": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection IN nature requires THREE pieces of evidence — heritability, differential reproduction, AND frequency change across generations. Robbins-bait: students stop at "differential survival" and miss the heritability requirement.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Three requirements: (1) heritable variation, (2) differential reproduction, (3) cross-generation frequency change.</li>
  <li>Field methods: longitudinal individual tracking, parent-offspring regression, marked-individual recapture.</li>
  <li>Per-generation S in nature is typically small (tenths of a SD) but accumulates over years.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The "is this evolution?" filter.</strong> Differential survival alone could be plasticity, drift, migration, or sampling. Need heritability + frequency change to confirm selection-driven evolution.</li>
  <li><strong>Why the Grants are the gold standard.</strong> They measured all three: h² from parent-offspring regression, S from survivor vs pop mean, R from next-gen mean. Closed the loop.</li>
  <li><strong>Robbins exam trap.</strong> "Beetles are darker this year." That's a snapshot. Need: h² estimate, individual-level reproduction data, multi-generation tracking.</li>
  <li><strong>Small per-gen S still produces big long-term change.</strong> Don't dismiss small shifts — they sum.</li>
</ol>`
    },

    "Geospiza fortis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Geospiza fortis = THE textbook example of measurable evolution in real time. Robbins WILL ask about this study. Memorize the numbers.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Species: Geospiza fortis (medium ground finch) on Daphne Major, Galápagos.</li>
  <li>Study: Peter and Rosemary Grant, decades-long (started 1973).</li>
  <li>1977 drought: ~85% of population died. Survivors had deeper beaks.</li>
  <li>Pre-drought mean beak depth ≈ 9.31 mm; post-drought survivors ≈ 9.84 mm → S ≈ 0.53 mm.</li>
  <li>h² ≈ 0.78 (parent-offspring regression).</li>
  <li>Predicted R = h²·S ≈ 0.41 mm. Observed next-gen shift matched.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Closed the evolution-by-selection causal chain.</strong> Every variable (h², S, R) measured independently; predicted R matched observed. No gaps.</li>
  <li><strong>Disproved the "evolution requires millions of years" caricature.</strong> Selection produced detectable mean shift in ONE generation under strong pressure.</li>
  <li><strong>Robbins-bait: selection direction can REVERSE.</strong> 1983 wet El Niño — small soft seeds dominant → smaller beaks favored, mean shifted back. Selection responds to ecology.</li>
  <li><strong>Hybridization wrinkle.</strong> Gene flow with G. scandens introduces new variation — selection + gene flow interact.</li>
</ol>`
    },

    "Selection on beak depth": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The 1977 drought selected deeper beaks → next-gen finches had deeper beaks → measurable evolution in ONE generation. Robbins's favorite empirical case.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>1977 drought killed most small-seed plants → large hard seeds dominated.</li>
  <li>Survivors had ~6% deeper beaks than pre-drought mean (S ≈ 0.53 mm).</li>
  <li>h² ≈ 0.78 (high additive variance for beak depth).</li>
  <li>Predicted R ≈ 0.41 mm; observed next-gen mean shift matched.</li>
  <li>1983 El Niño wet year reversed pressure — smaller seeds dominant → smaller beaks favored.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Disproved "evolution is too slow to observe."</strong> Strong selection + heritable trait = detectable mean shift in one generation.</li>
  <li><strong>Direction reverses with environment.</strong> Drought favors big beaks; flood favors small. Selection isn't unidirectional — it tracks ecology.</li>
  <li><strong>Robbins exam mechanic.</strong> Be ready to plug into R = h²·S with the actual finch numbers.</li>
  <li><strong>Independent verification of the breeder's equation.</strong> Predicted R from prior h² × current S matched observed R — testable theory.</li>
</ol>`
    },

    "Industrial melanism": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Industrial melanism = peppered moths went from light to dark and back, all driven by bird predation on visible morphs. THE textbook case of human-driven natural selection.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Pre-1850 England: ~99% light morph (typica) on lichen-covered trees.</li>
  <li>Industrial peak (~1900): >95% melanic (carbonaria) in polluted regions like Manchester.</li>
  <li>Post-Clean-Air Act (1956): light morph rebounded as lichen returned.</li>
  <li>Selection mechanism: differential bird predation on visible morphs.</li>
  <li>Genetic basis: TRANSPOSON insertion in the cortex gene (Hof et al. 2016 — memorize this).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Classic test case for natural selection.</strong> Documented in real time, with reversal when conditions changed — selection direction tracks environment.</li>
  <li><strong>Disproves "mutation directed by environment."</strong> The cortex transposon insertion existed before industrialization at low frequency. Pollution didn't create the mutation — it shifted the selective balance.</li>
  <li><strong>Robbins-bait: the SELECTIVE AGENT is bird predation, not pollution toxicity.</strong> Easy to mis-state.</li>
  <li><strong>Modern replication confirms Kettlewell.</strong> Older critiques of the experimental setup have been answered with newer work.</li>
</ol>`
    },

    "Biston betularia": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Biston betularia = the peppered moth species, exemplar of microevolution under human-altered conditions. Robbins expects you to name the species and the gene.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Two main morphs: typica (light, peppered) and carbonaria (dark, melanic).</li>
  <li>Genetic basis: cortex gene with TRANSPOSON insertion (Hof 2016).</li>
  <li>Insertion is a single ancient event — all melanic individuals share the same insertion.</li>
  <li>Frequency tracking: <1% melanic (1848) → >95% (1900) → ~10% (post-Clean-Air).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Clean documentation.</strong> Decades of frequency data, mark-release-recapture predation experiments (Kettlewell), and now molecular genetics — most thoroughly documented selection case.</li>
  <li><strong>The cortex transposon is exam gold.</strong> Robbins-bait: name the gene (cortex), name the mutation type (transposable element insertion), name the discoverers (Hof 2016).</li>
  <li><strong>Single-origin then selection.</strong> The insertion arose once at low frequency, then rose under industrial pollution — proves selection on standing variation, not induced mutation.</li>
  <li><strong>Reversibility = direct test.</strong> Clean Air Act → frequencies reversed → selection's role confirmed beyond doubt.</li>
</ol>`
    },

    "Antibiotic resistance": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Antibiotic resistance = real-time, public-health-critical natural selection. Resistant variants pre-EXIST; antibiotics SELECT them. Robbins-bait: the antibiotic does NOT cause the mutation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Time to detectable resistance after a new drug: typically <2 years.</li>
  <li>Mutation rate: ~10⁻⁹ per gene per generation. Bacteria divide ~every 20 min → ~50 generations/day.</li>
  <li>Mechanisms: enzymatic destruction (β-lactamases), efflux pumps, target-protein mutations, alternative pathways.</li>
  <li>Combination therapy: needing 2 simultaneous mutations reduces resistance probability from 10⁻⁹ to ~10⁻¹⁸.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strong directional selection in action.</strong> Antibiotic kills susceptibles → only resistant survive → resistant strains take over.</li>
  <li><strong>Robbins-bait: NOT induced mutation.</strong> Mutations are random. The antibiotic selects pre-existing resistant variants. Lamarck would predict drug-induced resistance — selection theory predicts pre-existing variation.</li>
  <li><strong>Why "finish your antibiotics" has evolutionary logic.</strong> Stopping early leaves partially-resistant survivors with sub-lethal exposure, fueling further evolution.</li>
  <li><strong>Combination therapy is selection-aware design.</strong> Probability of two simultaneous resistance mutations is the product of individual probabilities — astronomically small.</li>
</ol>`
    },

    "Artificial selection": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Artificial selection = same mechanism as natural selection, just with humans as the selective agent. The empirical foundation Darwin used to argue for natural selection.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Wild teosinte → modern maize: ~9000 years of selection, ear size grew from ~6 small kernels to hundreds of large kernels.</li>
  <li>Greyhound speed: ~64 km/h, ~20% faster than dog ancestor over centuries.</li>
  <li>Belyaev silver foxes: visible behavioral and morphological "domestication syndrome" in ~10 generations.</li>
  <li>Domestication rates ~10–100× faster than natural-selection rates because S is enormously inflated.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same R = h²·S equation applies.</strong> Mechanism is identical to natural selection — only the selective agent differs.</li>
  <li><strong>Why domestication is so fast.</strong> Humans pick top 1-5% as breeders → S is huge. Plus uniform short generation times.</li>
  <li><strong>Darwin's strategy.</strong> Artificial selection → tangible proof that selection produces large change. Natural selection extrapolates the same logic with ecology as the agent.</li>
  <li><strong>Robbins-bait.</strong> "Differs from natural selection how?" — only the selective agent (humans vs ecology). Mechanism, math, and outcome are identical.</li>
</ol>`
    },

    /* L07 extra (flashcards-extra.js) */
    "Three requirements for measurable evolution in nature": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection in the wild requires (1) heritable variation, (2) differential reproduction, and (3) cross-generation frequency change. Robbins's standard "what counts as evidence" question.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>(1) HERITABLE variation — measured by parent-offspring regression.</li>
  <li>(2) DIFFERENTIAL reproduction — some variants leave more offspring (S > 0).</li>
  <li>(3) FREQUENCY change across generations — observed allele or trait shift.</li>
  <li>Grants' finches satisfy all three on Daphne Major.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Selection vs. plasticity vs. drift vs. migration.</strong> All can produce trait changes — only the three-condition test confirms selection-driven evolution.</li>
  <li><strong>Why a one-year snapshot isn't enough.</strong> Need longitudinal data: cross-generation tracking proves the change isn't just plasticity.</li>
  <li><strong>Common Robbins-trap.</strong> "Darker beetles in polluted areas" — could be plasticity (warmth-induced melanin) or migration. Need heritability test and multi-gen tracking.</li>
  <li><strong>Why it's a high bar.</strong> Field studies meeting all three are rare — that's why the Grants' work is canonical.</li>
</ol>`
    },

    "Grants' Galápagos finches — predicted vs observed R": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The Grants MEASURED h² and S independently, PREDICTED R, then OBSERVED R — and predicted matched observed. THE textbook closed-loop demonstration of evolution by natural selection.</p>
<h4>The numbers (memorize these — Robbins exam gold)</h4>
<ul>
  <li>Pre-drought mean beak depth: 9.31 mm.</li>
  <li>Post-drought survivor mean: 9.84 mm.</li>
  <li>S = 0.53 mm (selection differential).</li>
  <li>h² = 0.78 (from parent-offspring regression).</li>
  <li>Predicted R = h² × S = 0.78 × 0.53 ≈ 0.41 mm.</li>
  <li>Observed next-gen mean shift was close to 0.41 mm.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Closed every gap in the causal chain.</strong> h² measured BEFORE selection event. S measured during. R measured after. No after-the-fact rationalization.</li>
  <li><strong>Quantitative test of the breeder's equation in the wild.</strong> Predicted ≈ observed → equation works under field conditions.</li>
  <li><strong>Robbins will ask for the numbers.</strong> Memorize 0.53, 0.78, 0.41. These are the empirical anchors of L07.</li>
  <li><strong>Time scale: ONE year/generation.</strong> Disproves the "evolution requires millions of years" caricature in one stroke.</li>
</ol>`
    },

    "Peppered moth industrial melanism — what was actually selected?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The selective agent was bird PREDATION on visible moths — NOT direct toxicity of pollution. The cortex transposon insertion was pre-existing standing variation, not pollution-induced. Robbins-bait both ways.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Genetic basis: TRANSPOSON (transposable element) insertion in the cortex gene. Single ancient origin.</li>
  <li>Discovery: Hof et al. 2016 — memorize this citation.</li>
  <li>Frequency: <1% melanic (1848) → >95% (industrial peak ~1900) → ~10% (post-Clean-Air).</li>
  <li>Selective agent: visual bird predation (Kettlewell mark-recapture, modernly replicated).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Decisively rules out Lamarckism.</strong> The cortex insertion existed BEFORE industrialization at low frequency. Pollution didn't create the mutation — it shifted the visibility-vs-predation balance, selecting pre-existing variants.</li>
  <li><strong>Reversibility confirms selection.</strong> Clean Air Act → lichen returned → light morphs rebounded. Mutation theory cannot explain reversal; selection theory predicts it perfectly.</li>
  <li><strong>Single-origin transposon = phylogenetic smoking gun.</strong> All carbonaria moths share the SAME insertion → arose once, then selected — not repeated independent mutations.</li>
  <li><strong>Robbins-bait pitfalls.</strong> (a) The selective agent is bird predation, NOT pollution toxicity. (b) The mutation existed before, not after, industrialization started.</li>
</ol>`
    },

    "Antibiotic resistance — speed and predictability": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Antibiotic resistance evolves in <2 years for most new drugs because bacterial populations are huge, generation times are short, and standing variation already harbors resistant variants. Public-health-critical exam material.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Bacterial mutation rate: ~10⁻⁹ per gene per generation.</li>
  <li>Bacteria divide every ~20 min → ~50 generations/day.</li>
  <li>Time to clinical resistance after new drug: typically <2 years.</li>
  <li>Combination therapy reduces resistance probability from 10⁻⁹ to 10⁻¹⁸ (need both mutations).</li>
  <li>Mechanisms: β-lactamases (enzymatic destruction), efflux pumps, target-protein mutations, alternative pathways.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strong directional selection in real time.</strong> The most urgent ongoing demonstration of evolution in human health.</li>
  <li><strong>"Finish your course" has evolutionary logic.</strong> Stopping early leaves partially-resistant survivors with sub-MIC exposure → they accumulate further mutations → multi-drug resistance.</li>
  <li><strong>Combination therapy is selection-aware design.</strong> Two-drug regimens require simultaneous mutations — exponentially smaller probability.</li>
  <li><strong>Robbins-bait: NOT Lamarckian.</strong> The drug doesn't cause the mutation. The mutation pre-exists; the drug selects.</li>
</ol>`
    },

    "Domestication = artificial selection (greyhound case)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Domestication = same R = h²·S logic as natural selection, but humans inflate S massively. Belyaev's foxes show visible morphological evolution in 10 generations.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Greyhound: modern racing speed ~64 km/h, ~20% faster than dog ancestors.</li>
  <li>Belyaev silver foxes: 10 generations → tame, floppy-eared, piebald — "domestication syndrome."</li>
  <li>Domestication rates: 10–100× faster than typical wild natural-selection rates.</li>
  <li>Maize from teosinte: ~9000 years, ears scaled from ~6 kernels to hundreds.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same equation, larger S.</strong> Humans pick top 1-5% as breeders → S is huge compared to nature, where S is bounded by ecology.</li>
  <li><strong>Belyaev fox experiment is iconic.</strong> Selecting only for tameness produced full domestication syndrome — pleiotropy in action.</li>
  <li><strong>Darwin's leverage.</strong> Used artificial selection's tangible results to argue natural selection works the same way.</li>
  <li><strong>Robbins-bait: it's selection, not engineering.</strong> Humans choose breeders; they don't directly modify genes. Same Mendelian inheritance applies.</li>
</ol>`
    },

    "Why field selection studies need longitudinal data": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> A snapshot doesn't distinguish selection from drift, plasticity, migration, or sampling bias. You need TRACKED individuals across generations. Robbins-bait test of methodological rigor.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Four alternative explanations for an observed trait shift: drift, migration, plasticity, sampling bias.</li>
  <li>Need: (1) marked individuals tracked across years, (2) parent-offspring h² estimate, (3) replicate populations to control for drift, (4) genetic markers to rule out migration.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>The methodological gold standard.</strong> Why the Grants spent decades — only multi-generation tracking distinguishes selection from confounds.</li>
  <li><strong>Drift matters in small populations.</strong> Single-population shifts could be sampling chance — replicate sites needed.</li>
  <li><strong>Migration looks like selection.</strong> If dark beetles move IN, frequency rises without selection. Genetic markers detect this.</li>
  <li><strong>Plasticity is the sneakiest confound.</strong> Same beetles, warmer year, more melanin → looks like evolution but is reversible. Common-garden experiment is the test.</li>
</ol>`
    },

    "Influenza antigenic drift vs antigenic shift": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> DRIFT = gradual mutation; SHIFT = abrupt reassortment. Drift = annual flu vaccine; shift = pandemic. Robbins exam staple.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>DRIFT: HA/NA mutate ~0.5% per year, escape antibodies → annual vaccine.</li>
  <li>SHIFT: two flu strains co-infect one cell → genome segments reassort → big antigenic jump → pandemic potential.</li>
  <li>Examples: 1918 (H1N1, ~50M deaths), 1957 (H2N2), 1968 (H3N2), 2009 (H1N1pdm09).</li>
  <li>Measles HA/NA evolve much slower → childhood vaccine is near-lifelong.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Drift = strong selection from human immune memory.</strong> Last year's antibodies select for escape mutants → continuous evolution.</li>
  <li><strong>Shift = pandemic mechanism.</strong> Reassortment in pigs or birds → completely novel HA/NA → no human immunity → pandemic.</li>
  <li><strong>Annual vaccines target drift.</strong> Predict next year's drifted strains and pre-make the vaccine.</li>
  <li><strong>Robbins-bait.</strong> "Why annual flu shot but not annual measles?" — Faster pathogen evolution = shorter vaccine validity.</li>
</ol>`
    },

    "When does R = h²·S fail to predict the next generation?": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> The breeder's equation is an idealization. Field deviations point to which assumption broke. Robbins flags this as discriminator material.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Assumptions: (1) only V_A counts, (2) no parent-offspring environment correlation, (3) selection on focal trait only, (4) no GxE correlation, (5) no major environment shift between gens.</li>
  <li>Common deviations: shared-environment inflation of h², inbreeding depression in offspring, environment shift, correlated selection, frequency-dependent selection.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Equation is single-generation.</strong> Iterating naively is wrong because V_A erodes as alleles fix.</li>
  <li><strong>Shared environment inflates h² estimate.</strong> Parents and offspring share microclimate/nutrition → regression slope captures both heritability AND environmental similarity.</li>
  <li><strong>Robbins-bait scenario.</strong> Predicted R = 4 cm but observed R = 1 cm → inflated h², or environment changed, or correlated trait was selected. Multiple plausible answers.</li>
  <li><strong>Frequency-dependent selection erodes V_A faster.</strong> If rare variants are favored, fitness depends on frequency → equilibrium forces.</li>
</ol>`
    },
  });

  /* ============================================================
   * L08 — Complex Adaptations
   * ============================================================ */
  window.addCardPatches('L08', {
    "Adaptation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> "Adaptation" has TWO meanings — a trait shaped by past selection (noun), and the process producing such traits (verb). Robbins-bait: students conflate them.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>NOUN: "the wing IS an adaptation FOR flight" — a heritable feature shaped by past selection FOR a specific function.</li>
  <li>VERB: "the population is undergoing adaptation" — the act of evolving under selection.</li>
  <li>Calling something an adaptation FOR X is a strong claim — needs evidence of (1) heritable variation, (2) historical fitness benefit specifically for X, (3) ideally a comparative test.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Same word, two distinct claims.</strong> The verb is descriptive (population is changing). The noun is a strong inference (this trait was shaped FOR this function).</li>
  <li><strong>Distinguishes from exaptation and byproduct.</strong> Feathers were thermoregulatory before flight (exaptation). Chin shape may be a byproduct (no selection at all).</li>
  <li><strong>Robbins-bait.</strong> "Bat wings are an adaptation for flight" — noun sense, requires evidence beyond just functionality.</li>
  <li><strong>Drives the rest of L08.</strong> Complex adaptations build incrementally; each intermediate stage must be itself functional.</li>
</ol>
<h4>vs Exaptation</h4>
<ul>
  <li>Adaptation: trait selected FOR its current function.</li>
  <li>Exaptation: trait co-opted from another original function (feathers thermal → flight).</li>
  <li>Byproduct: trait with no selection at all (e.g., human chin per some accounts).</li>
</ul>`
    },

    "Gradual evolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Complex traits build incrementally — each step must itself be functional and selected. The answer to "what use is half an eye?" The classic creationist objection demolished.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Eyes have evolved INDEPENDENTLY ≥40 times across animals.</li>
  <li>Each stage in eye evolution exists in living organisms today: light-sensitive patch (planarian), cup (limpet), pinhole (Nautilus), lensed (vertebrate, octopus).</li>
  <li>Selection cannot "plan ahead" — every intermediate must currently confer fitness.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Defeats the "irreducible complexity" objection.</strong> Half an eye isn't a failed full eye — it's a simpler light-detecting structure with its own utility.</li>
  <li><strong>The intermediates aren't hypothetical.</strong> Each stage is documented in a living lineage today — extant evidence, not just a thought experiment.</li>
  <li><strong>Convergence proves climb-ability.</strong> Eyes evolved independently 40+ times → the gradient is climbable from many starting points.</li>
  <li><strong>Robbins-bait.</strong> Be ready to name a living organism for each eye-evolution stage.</li>
</ol>`
    },

    "Stepwise eye evolution": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Patch → Cup → Pinhole → Lens. Four stages, each functional, each represented by a living organism today. THE textbook example of gradual complex adaptation.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Stage 1 — light-sensitive patch: planarian, jellyfish (circadian, predator detection).</li>
  <li>Stage 2 — cupped patch: limpet, flatworm (directional sensitivity).</li>
  <li>Stage 3 — pinhole eye: Nautilus (image without lens).</li>
  <li>Stage 4 — lensed eye: vertebrates, octopus (sharp focus via crystallins, often co-opted from heat-shock proteins/metabolic enzymes).</li>
  <li>Eyes evolved independently >40 times across animals.</li>
  <li>Nilsson & Pelger (1994) calculation: ~400,000 generations from patch to lensed eye under modest selection.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Demolishes "irreducible complexity."</strong> Each step is functional on its own — no need for a "complete" eye to be useful.</li>
  <li><strong>Rapid in evolutionary time.</strong> Nilsson & Pelger showed ~400k generations is enough — fast on geological scales.</li>
  <li><strong>Robbins-bait.</strong> Be ready to name the living organism at each stage. Especially: Nautilus = pinhole.</li>
  <li><strong>Crystallins are repurposed proteins.</strong> Lens transparency emerged via cooption of pre-existing soluble proteins — no de novo invention.</li>
</ol>`
    },

    "Convergent evolution of eyes": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Vertebrate and cephalopod camera eyes look alike — but evolved INDEPENDENTLY. Same selective problem (image-forming vision), different starting points. Photoreceptor orientation is the key tell.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Eyes evolved independently >40 times across animals.</li>
  <li>Vertebrate retina: photoreceptors are INVERTED — light passes through neurons before hitting them. Has a blind spot where the optic nerve exits.</li>
  <li>Cephalopod retina: photoreceptors are EVERTED — facing light directly. NO blind spot.</li>
  <li>Same gene (Pax6) initiates both — deep homology in regulators.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Convergence with key differences = independent origin.</strong> Photoreceptor orientation reveals different evolutionary paths to the same functional outcome.</li>
  <li><strong>Vertebrate retinal inversion is a CONSTRAINT — not a design choice.</strong> Historical contingency: vertebrate eye started as outpouching of brain → photoreceptors face the back. Octopus eye started as skin invagination → photoreceptors face the front.</li>
  <li><strong>Robbins-bait: blind spot evidence for evolution.</strong> A designed eye wouldn't have a blind spot. An evolved one inherits its mistakes.</li>
  <li><strong>Pax6 conservation = deep homology in REGULATION.</strong> Same master regulator triggers eye development in flies, mice, humans, octopus — even though the eyes themselves are convergent.</li>
</ol>`
    },

    "Cis-regulatory mutation": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Cis-regulatory mutations change WHEN/WHERE a gene is expressed without changing the protein. THE leading-edge mechanism for body-plan evolution. Robbins favorite for evo-devo.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Cis = same chromosome (enhancer/promoter near the gene).</li>
  <li>Trans = different chromosome (transcription factor that binds enhancer).</li>
  <li>Stickleback fish: lost pelvic spines in lakes via repeated cis-regulatory loss in Pitx1 — Pitx1 protein still works in teeth and elsewhere.</li>
  <li>Drosophila pigmentation: ~99% identical pigmentation gene SEQUENCE between species, but very different wing patterns from regulatory differences.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Modularity.</strong> A cis-regulatory change alters expression in ONE tissue or time without affecting other uses of the gene. Structural mutations would break everything else.</li>
  <li><strong>Lower pleiotropic cost.</strong> Pitx1 has many essential roles — a structural change would be lethal. Only the pelvic enhancer changed → spines lost without breaking other functions.</li>
  <li><strong>Hox-gene expression is the classic case.</strong> Conserved Hox proteins; differences in body plan come from where/when Hox is expressed.</li>
  <li><strong>Robbins-bait.</strong> "Why is cis-regulatory evolution favored over structural change in pleiotropic genes?" Modularity → less cost.</li>
</ol>`
    },

    "Gene duplication": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Gene duplication creates redundant copies → relaxed selection on one copy → it can evolve a new function. Major source of evolutionary novelty WITHOUT inventing genes from scratch.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Vertebrate globin family arose via repeated duplications: α, β, γ, ε, δ, myoglobin.</li>
  <li>Vertebrates have 4 Hox clusters from 2 whole-genome duplications (1R, 2R) ~500 Mya.</li>
  <li>Teleost fish underwent a third (3R) → ~30,000-species radiation.</li>
  <li>~30% of human genes have detectable paralogs from duplication.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Solves the "constrained essential gene" problem.</strong> A single-copy essential gene can't easily evolve new functions — losing the original is lethal. A duplicate is free to drift/adapt.</li>
  <li><strong>Two fates: subfunctionalization or neofunctionalization.</strong> Both copies survive only if they collectively retain ancestral function or one gains something new.</li>
  <li><strong>Whole-genome duplications drive macroevolution.</strong> 1R, 2R correlate with vertebrate origin and elaboration; 3R with teleost diversification.</li>
  <li><strong>Robbins-bait.</strong> Be ready to distinguish neo- vs sub-functionalization with examples.</li>
</ol>`
    },

    "Neofunctionalization": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> One duplicate gene gains a NEW function; the other keeps the original. Robbins discrimination from subfunctionalization is exam-trap territory.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Classic example: hemoglobin (oxygen transport in RBC) and myoglobin (oxygen storage in muscle) — duplicated; myoglobin neofunctionalized for muscle oxygen storage.</li>
  <li>MYC family TFs accumulated new tissue-specific roles after duplication — neofunctionalization.</li>
  <li>Antifreeze glycoprotein in Antarctic notothenioid fish — co-opted from a digestive trypsinogen gene.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Source of evolutionary novelty.</strong> Without inventing new genes from scratch, neofunctionalization repurposes existing ones.</li>
  <li><strong>Requires relaxed selection on the duplicate.</strong> The redundant copy can accumulate mutations because the other copy still does the original job.</li>
  <li><strong>Often involves protein promiscuity.</strong> Pre-existing weak side-activities of the protein get refined into new primary functions.</li>
  <li><strong>Robbins-bait: vs subfunctionalization.</strong> Neo = NEW function. Sub = SPLIT existing function. Memorize the distinction.</li>
</ol>`
    },

    "Subfunctionalization": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Both duplicate genes specialize on DIFFERENT subsets of the original function. Each is now needed; together they cover the original role.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Classic example: hemoglobin α and β arose by duplication, then specialized for adult vs fetal oxygen binding.</li>
  <li>Original protein had functions A AND B → duplicates split: copy 1 does A, copy 2 does B.</li>
  <li>Often expressed in different tissues/timepoints after duplication.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Different from neofunctionalization.</strong> Sub = split existing job; neo = new job. Both fates explain why duplicate genes survive long-term.</li>
  <li><strong>Both copies become essential.</strong> Once specialized, neither alone can do the original full function — duplicates are locked in.</li>
  <li><strong>DDC model (duplication-degeneration-complementation).</strong> Each copy loses regulatory or coding elements such that they together complement the ancestral function — passive subfunctionalization.</li>
  <li><strong>Robbins exam mechanic.</strong> Given an example, classify as neo or sub. Hemoglobin α/β = sub (oxygen binding split). Myoglobin = neo (storage, not transport).</li>
</ol>`
    },

    "Protein promiscuity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Most proteins have weak side-activities. Selection refines those into new primary functions. Major source of evolutionary novelty without inventing genes from scratch.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Eye lens crystallins: co-opted from heat-shock proteins and metabolic enzymes (still have catalytic activity in some species).</li>
  <li>Antarctic notothenioid antifreeze: co-opted from trypsinogen (digestive enzyme).</li>
  <li>Steroid receptor families: ancestral receptor bound multiple steroids weakly; duplicates specialized for cortisol vs aldosterone.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Solves "where do new functions come from?"</strong> They don't appear de novo — they're refined from pre-existing weak activities.</li>
  <li><strong>Enables neofunctionalization.</strong> A duplicate that already has a weak side-activity can be pushed by selection toward that function.</li>
  <li><strong>Moonlighting proteins.</strong> Many enzymes have multiple roles — promiscuity is the norm, specificity is the exception.</li>
  <li><strong>Robbins-bait.</strong> "How do novel traits arise?" Not invention — refinement of existing capacity. Crystallins from heat-shock proteins is the canonical example.</li>
</ol>`
    },

    "Heterochrony": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Heterochrony = change in WHEN or HOW LONG developmental events run. Powerful source of morphological novelty from minimal genetic change.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Two main types: paedomorphosis (juvenile features retained) and peramorphosis (development extended past ancestor).</li>
  <li>Examples: axolotl = paedomorphic (gilled adult, sexually mature); Irish elk antlers = peramorphic; domestic dogs vs wolves = paedomorphic in some traits.</li>
  <li>Often controlled by a few mutations in regulatory genes (e.g., thyroid hormone signaling controls amphibian metamorphosis).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Big morphological change from small genetic change.</strong> Tweak when growth stops or when metamorphosis triggers → dramatically different adult.</li>
  <li><strong>Common across closely related species.</strong> Many cross-species differences are heterochronic, not due to new genes.</li>
  <li><strong>Robbins-bait: vs heterotopy.</strong> Heterochrony = TIMING change. Heterotopy = LOCATION change (where in the body something develops). Different concepts.</li>
  <li><strong>Connects to regulatory evolution.</strong> Timing changes often involve cis-regulatory mutations on developmental switch genes.</li>
</ol>`
    },

    "Paedomorphosis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Paedomorphosis = adult retains JUVENILE features. Axolotl is THE canonical example. "Pediatric" mnemonic.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Classic example: axolotl (Ambystoma mexicanum) — sexually mature with external gills, fin, larval body shape. Reproduces in larval form.</li>
  <li>Mechanism in axolotl: failure of thyroid-hormone surge → no metamorphosis. Treating with T4 induces full metamorphosis.</li>
  <li>Other examples: human cranial proportions resemble juvenile chimps (some paedomorphic features).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Selective context.</strong> Often favored in stable juvenile habitats where adult terrestrial life is risky (axolotl lakes — high-altitude, predator-poor, drought-resistant).</li>
  <li><strong>Big change from one regulatory shift.</strong> A single endocrine alteration produces a fully different adult body plan.</li>
  <li><strong>Robbins-bait.</strong> Paedo = pediatric (juvenile). Pera = past (extended). Memorize the distinction.</li>
  <li><strong>Connects to neoteny.</strong> Neoteny = subset of paedomorphosis where somatic development slows but reproductive development continues.</li>
</ol>`
    },

    "Peramorphosis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Peramorphosis = development EXTENDS past the ancestor's endpoint, producing more derived adults. Irish elk antlers are the icon.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Classic example: Irish elk (Megaloceros giganteus) antlers up to ~3.6 m wide — extension of ancestral antler-growth program.</li>
  <li>Other examples: large body size in some lineages (peramorphic from smaller ancestors), elaborate ornamental traits.</li>
  <li>Mechanism: extending growth duration, accelerating growth rate, or delaying terminal differentiation.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Counterpart to paedomorphosis.</strong> Paedo retains juvenile; pera extends past ancestor. Both are heterochrony types.</li>
  <li><strong>Often driven by sexual selection.</strong> Extended/exaggerated traits (big antlers, tail feathers) — peramorphic features under mate choice.</li>
  <li><strong>Trade-offs.</strong> Irish elk antlers may have contributed to extinction (energetic cost, mineral demand).</li>
  <li><strong>Robbins-bait.</strong> Pera = PAST the ancestor's endpoint. Distinguish from paedo (kept juvenile).</li>
</ol>`
    },

    "Hox gene": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Hox genes = transcription factors patterning the anterior-posterior axis of bilaterians. DEEPLY conserved across phyla — same toolkit in flies, mice, humans. The CENTRAL evo-devo discovery.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Hox genes are clustered on chromosomes; arrangement matches body-axis expression order (COLINEARITY).</li>
  <li>Vertebrates have 4 Hox clusters (HoxA, HoxB, HoxC, HoxD) from 2 whole-genome duplications (1R, 2R).</li>
  <li>Drosophila has 1 Hox complex (split into 2 in lab strain).</li>
  <li>Teleost fish have 7-8 clusters from a third whole-genome duplication (3R).</li>
  <li>Functional interchangeability: a fly Hox gene can substitute for a mouse Hox gene in early development.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Deep conservation across ~600 million years.</strong> Same gene family patterns body axes in flies, mice, humans → bilaterian common ancestor had it too.</li>
  <li><strong>Body-plan differences come from REGULATION, not new Hox proteins.</strong> Where/when Hox is expressed differs across species; the proteins themselves are nearly identical.</li>
  <li><strong>Cluster duplications correlate with body-plan elaboration.</strong> Vertebrate 1R + 2R → head, jaws, paired appendages, complex CNS. Teleost 3R → 30,000-species radiation.</li>
  <li><strong>Robbins-bait.</strong> Hox doesn't CAUSE segments — it specifies segment IDENTITY. Different concept. Also: name the cluster count for vertebrates (4) vs flies (1).</li>
</ol>`
    },

    "Colinearity": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Hox genes are arranged on the chromosome in the SAME ORDER as their expression along the body axis. Anterior genes in front, posterior in back. THE signature of Hox biology.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Spatial colinearity: chromosome order = body-axis expression order.</li>
  <li>Temporal colinearity: anterior Hox genes express earlier in development; posterior express later.</li>
  <li>Conserved from flies to vertebrates → ~600 Myr of preservation.</li>
  <li>Disrupting cluster order disrupts development → strong selection maintaining the arrangement.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strong constraint = strong selection.</strong> Why would chromosome order be conserved across 600 Myr? Because the regulatory architecture depends on the ordered cluster layout — a shared enhancer landscape.</li>
  <li><strong>Evidence of common ancestry.</strong> The shared linear arrangement across phyla is strong phylogenetic evidence.</li>
  <li><strong>Mechanism: chromatin and enhancer sharing.</strong> Adjacent Hox genes share regulatory elements; cluster integrity matters for expression timing.</li>
  <li><strong>Robbins-bait.</strong> Be ready to define spatial and temporal colinearity. The chromosomal arrangement matches body-axis output.</li>
</ol>`
    },

    "Conservation of developmental networks": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Core gene-regulatory networks (Hox, Pax, Wnt) are SHARED across all animals — evidence of deep common ancestry. Pax6 makes eyes in flies, mice, AND humans.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Pax6: master regulator of eye development. Functional in flies, mice, humans, octopus.</li>
  <li>Hox: anterior-posterior axis patterning. Conserved across bilaterians (~600 Myr).</li>
  <li>Wnt: signaling pathway in axis formation, stem-cell maintenance. Shared from sponges to humans.</li>
  <li>Hedgehog signaling: limb patterning, neural patterning — shared across bilaterians.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Implies an ancestral developmental toolkit.</strong> The bilaterian common ancestor (~600 Mya) already had these networks — they've been re-deployed in different lineages.</li>
  <li><strong>Eyes are convergent, but the regulator is homologous.</strong> Vertebrate and octopus eye structures evolved independently, but BOTH use Pax6 as the master switch.</li>
  <li><strong>Body-plan diversity from regulatory tinkering.</strong> Same toolkit, different deployment patterns → wildly different bodies.</li>
  <li><strong>Robbins-bait.</strong> "What does Pax6 conservation suggest?" — an ancestral eye-like structure (or at least an ancestral light-sensing apparatus) in the bilaterian ancestor.</li>
</ol>`
    },

    "Vestigial structure": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Vestigial = ancestral structure with reduced/no current function. Whale pelvis, human appendix, snake hindlimb buds, blind cave-fish eyes. Robbins-bait: vestigials are POSITIVE evidence FOR evolution.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Whale pelvis: small bone embedded in tissue, no skeletal connection to spine.</li>
  <li>Human appendix: cecum-derived, large in herbivorous ancestors, reduced as diet shifted.</li>
  <li>Snake hindlimb buds: present briefly in embryonic development, then regress.</li>
  <li>Blind cave fish (Astyanax mexicanus): eye-development genes still present but expression altered.</li>
  <li>Ostrich wings: too small for flight, retained for display/balance.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strongest evidence for common descent.</strong> A designed organism wouldn't have leftover parts. Evolution inherits and modifies, leaving fingerprints of ancestry.</li>
  <li><strong>Why "appendix is evidence against evolution" is wrong.</strong> The appendix is exactly what you'd PREDICT from descent + modification — not a problem for evolution, but a positive signature.</li>
  <li><strong>Reduction takes time.</strong> Selection against a no-longer-needed structure is weak (no fitness cost beyond resource investment) → vestigials persist for many generations.</li>
  <li><strong>Robbins-bait.</strong> Don't say vestigials are "useless" — many have residual minor functions. Define as REDUCED/altered ancestral, not fully nonfunctional.</li>
</ol>`
    },

    "Trade-off": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Improving one trait often costs performance in another. THE reason adaptations are "good enough" not "perfect." Robbins's go-to "why isn't X better?" answer.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Cheetah: ~100+ km/h sprint, but only sustainable for ~30 seconds. Trade-off: light frame for speed vs muscle mass for endurance.</li>
  <li>Newt-snake arms race: TTX-resistant snakes are slower → predation by birds caps escalation.</li>
  <li>Antibody breadth vs specificity: more general → less effective per pathogen.</li>
  <li>Reproductive vs survival investment: many offspring vs longer life.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Why selection doesn't optimize.</strong> Improving trait A often hurts trait B → equilibrium at the best COMBINATION, not the best single value.</li>
  <li><strong>Caps arms races.</strong> Predator-prey escalation hits trade-off limits — toxin resistance has metabolic cost, etc.</li>
  <li><strong>Pleiotropy is the molecular root.</strong> One gene often affects multiple traits → improving one phenotype constrains others.</li>
  <li><strong>Robbins-bait.</strong> "Why don't cheetahs sprint forever?" Trade-off: speed-frame vs endurance-frame are physically incompatible.</li>
</ol>`
    },

    "Constraint": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Selection works on what's available — historical and developmental constraints LIMIT what selection can produce. The reason adaptations are imperfect.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Historical constraint: vertebrate retinal photoreceptors are INVERTED (light passes through neurons first) → blind spot.</li>
  <li>Developmental constraint: tetrapod limb skeleton (one bone, two bones, many bones, digits) — pattern conserved across 400+ million years.</li>
  <li>Genetic constraint: pleiotropy means improving one trait often pulls others.</li>
  <li>Phylogenetic constraint: humans inherited a quadrupedal spine — bipedal posture causes back pain.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Imperfections are predicted by evolution.</strong> A designed system would be optimal. An evolved one is constrained by ancestry.</li>
  <li><strong>Why human spines hurt.</strong> Inherited quadrupedal architecture re-purposed for bipedalism — selection couldn't redesign from scratch.</li>
  <li><strong>Octopus eye lacks the blind spot.</strong> Not because it's "better designed" but because it had a different developmental starting point — skin invagination vs brain outpouching.</li>
  <li><strong>Robbins-bait.</strong> "Why doesn't selection produce optimum?" → constraints. Three types: historical, developmental, genetic (pleiotropy).</li>
</ol>`
    },

    /* L08 extra (flashcards-extra.js) */
    "Stepwise eye evolution stages": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Patch → Cup → Pinhole → Lens. Four functional stages, each represented by a living organism today, demonstrating that "irreducible complexity" arguments fail for eyes.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Stage 1 — patch: planarian, jellyfish (light/dark + circadian).</li>
  <li>Stage 2 — cup: limpet, flatworm (directional sensing).</li>
  <li>Stage 3 — pinhole: Nautilus (rough image, no lens).</li>
  <li>Stage 4 — lens: vertebrates, octopus (sharp focus via crystallins).</li>
  <li>Eyes evolved independently >40 times.</li>
  <li>Nilsson & Pelger (1994) modeled ~400,000 generations from patch to lensed eye.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Defeats "irreducible complexity."</strong> Each step is functional alone — selection has a target at every intermediate.</li>
  <li><strong>40+ independent origins prove the gradient is climbable.</strong> Convergence on the camera-eye solution from many starting points.</li>
  <li><strong>Crystallins were co-opted.</strong> Lens transparency emerged from heat-shock proteins / metabolic enzymes — not invented.</li>
  <li><strong>Robbins-bait.</strong> Memorize the four stages and a living organism for each. Especially: Nautilus = pinhole.</li>
</ol>`
    },

    "Neofunctionalization vs subfunctionalization": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> NEO = NEW function on one duplicate. SUB = SPLIT existing function across both. Robbins's classic discrimination — memorize the difference with examples.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>NEO example: myoglobin (oxygen storage in muscle) gained a NEW role; hemoglobin retained ancestral oxygen transport.</li>
  <li>NEO example: MYC family of TFs accumulated new tissue-specific roles after duplication.</li>
  <li>SUB example: hemoglobin α and β specialized for adult vs fetal oxygen — split the binding range.</li>
  <li>SUB mechanism: DDC model (duplication-degeneration-complementation) — each copy loses some regulatory elements such that they together complement the ancestor.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Both fates explain why duplicate genes survive.</strong> Without one of these, redundant copies typically degenerate to pseudogenes.</li>
  <li><strong>NEO is novelty; SUB is specialization.</strong> Different evolutionary outcomes from the same starting point.</li>
  <li><strong>Robbins-bait.</strong> Given an example, classify. "Hemoglobin α/β specialized for adult/fetal oxygen" = SUB. "Myoglobin acquired muscle-storage role" = NEO.</li>
  <li><strong>Mnemonic.</strong> Neo = Novelty. Sub = Split.</li>
</ol>`
    },

    "Heterochrony (paedo vs peramorphosis)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Heterochrony = changes in developmental TIMING. Paedo = juvenile retained. Pera = past the ancestor's endpoint. Big morphological change from minimal genetic change.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Paedomorphosis example: axolotl (gilled, larval-bodied, sexually mature). Mechanism: failed thyroid-hormone surge.</li>
  <li>Paedomorphosis example: human cranial proportions resemble juvenile chimps.</li>
  <li>Peramorphosis example: Irish elk antlers up to ~3.6 m wide.</li>
  <li>Often controlled by a few mutations in regulatory genes (timing switches).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Powerful source of morphological novelty.</strong> Tweak when growth stops or when metamorphosis triggers → dramatically different adult.</li>
  <li><strong>Cheap genetic change → big phenotypic change.</strong> No new genes needed; just regulatory shifts on developmental clocks.</li>
  <li><strong>Common in closely related species.</strong> Many cross-species differences are heterochronic, not de novo invention.</li>
  <li><strong>Robbins-bait.</strong> Paedo = Pediatric (juvenile features kept). Pera = Past (development extended). Memorize and apply to examples.</li>
</ol>`
    },

    "Hox genes — A-P body axis": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Hox genes pattern the anterior-posterior axis of bilaterians, are clustered with COLINEARITY (chromosomal order = body-axis expression order), and are deeply conserved across phyla. Vertebrate cluster duplications correlate with body-plan transitions.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Vertebrates: 4 Hox clusters (HoxA, B, C, D) from 2 whole-genome duplications (1R, 2R) ~500 Mya.</li>
  <li>Drosophila: 1 Hox complex.</li>
  <li>Teleost fish: 7-8 clusters from third (3R) duplication, correlated with >30,000-species radiation.</li>
  <li>Spatial colinearity: chromosome 3' → 5' = anterior → posterior body axis.</li>
  <li>Temporal colinearity: anterior genes express earlier; posterior later.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Cluster duplications drive macroevolution.</strong> 1R + 2R → vertebrate body plan elaboration (head, jaws, paired limbs, complex CNS). 3R → teleost diversity explosion.</li>
  <li><strong>Body-plan differences come from REGULATION.</strong> The Hox proteins themselves are nearly identical across phyla; differences in WHERE/WHEN they're expressed produce body-plan diversity.</li>
  <li><strong>Functional interchangeability.</strong> A fly Hox gene can substitute for a mouse one — proves deep conservation of the biochemical role.</li>
  <li><strong>Robbins-bait.</strong> Hox doesn't CAUSE segments. It specifies segment IDENTITY (what a segment becomes) given an underlying segmentation process.</li>
</ol>`
    },

    "Cis-regulatory mutations vs structural": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> CIS = changes WHEN/WHERE a gene is expressed (enhancer/promoter); STRUCTURAL = changes the protein. Cis is the leading edge of body-plan evolution because it's MODULAR.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Stickleback fish: lost pelvic spines in lakes via repeated cis-regulatory loss in Pitx1. The Pitx1 PROTEIN still works in teeth and elsewhere — only the pelvic enhancer was lost.</li>
  <li>Stickleback armor reduction: ~10 generations after lake colonization.</li>
  <li>Drosophila: ~99% identical pigmentation gene SEQUENCE between species, but very different wing patterns from regulatory differences.</li>
  <li>Hox gene example: same Hox proteins in flies and vertebrates; body-plan differences from regulatory differences.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Modularity = lower pleiotropic cost.</strong> A cis-regulatory change alters expression in ONE tissue/timepoint without breaking other uses of the gene. Structural changes affect the protein everywhere → typically lethal in essential genes.</li>
  <li><strong>Pitx1 is the textbook case.</strong> Pleiotropic gene (essential for teeth, jaw, etc.) — only the pelvic spine enhancer mutated → spines lost without breaking other functions.</li>
  <li><strong>Why morphological evolution is so often regulatory.</strong> Structural mutations in conserved developmental genes have large pleiotropic costs; cis-regulatory mutations don't.</li>
  <li><strong>Robbins-bait.</strong> "Why is cis-regulatory evolution favored over structural change in pleiotropic genes?" Modularity → lower cost → more evolvable.</li>
</ol>`
    },

    "Vestigial structure (definition + examples)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Vestigial structures = ancestral forms with reduced function. They are POSITIVE evidence for evolution because design wouldn't predict leftover parts.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Whale pelvis: small bone, no spinal connection — relic of terrestrial ancestor.</li>
  <li>Human appendix: cecum-derived, large in herbivorous ancestors, reduced in modern humans.</li>
  <li>Snake hindlimb buds: present briefly in embryos, regress.</li>
  <li>Ostrich wings: too small for flight, retained for display/balance.</li>
  <li>Astyanax mexicanus blind cave fish: eye-development genes still present, expression altered.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strongest evidence for descent + modification.</strong> Design predicts no useless parts. Evolution predicts inherited-but-modified structures.</li>
  <li><strong>Many vestigials retain minor functions.</strong> Robbins-bait: don't say "useless." Appendix has some immune role; whale pelvis anchors muscles.</li>
  <li><strong>Why they persist.</strong> Selection AGAINST a minor structure is weak — no major fitness cost beyond resource investment.</li>
  <li><strong>Connects to common descent.</strong> Phylogenetic interpretation: vestigials map onto ancestor-descendant transitions (whales from artiodactyls, snakes from limbed lizards).</li>
</ol>`
    },

    "Adaptation — noun vs verb (trait vs process)": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Adaptation has TWO meanings — a TRAIT shaped by past selection (noun) OR the PROCESS of evolving under selection (verb). Robbins discriminator question.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Trait sense (noun): "the wing IS an adaptation FOR flight."</li>
  <li>Process sense (verb): "the population is undergoing adaptation."</li>
  <li>Calling something AN adaptation FOR X requires evidence: (1) heritable variation, (2) historical fitness benefit specifically for X, (3) ideally a comparative or experimental test.</li>
  <li>Alternatives: EXAPTATION (co-opted from another role — feathers thermal → flight), BYPRODUCT (no selection — chin shape per some accounts).</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Strong claim vs weak claim.</strong> The verb sense just labels change. The noun sense commits to a specific selection history for a specific function.</li>
  <li><strong>Tests for adaptation are not trivial.</strong> Need historical, comparative, or experimental evidence — observing functionality alone is not enough.</li>
  <li><strong>Robbins-bait.</strong> "Bat wings are an adaptation for flight" — noun sense, requires evidence beyond just functionality. Could feathers be an exaptation? (Yes — thermoregulation first.)</li>
  <li><strong>Avoid panglossian reasoning.</strong> "It works, therefore it was selected for that function" is a logical leap. Need historical evidence.</li>
</ol>`
    },

    "Protein promiscuity → cooption": {
      importance: `<p class="big-deal"><strong>The big deal in one line:</strong> Most "novel" traits are NOT invented from scratch — they're refined from pre-existing weak side-activities of existing proteins. Major source of evolutionary novelty.</p>
<h4>The numbers (memorize these)</h4>
<ul>
  <li>Eye lens crystallins: co-opted from heat-shock proteins and metabolic enzymes (some retain catalytic activity).</li>
  <li>Antarctic notothenioid antifreeze glycoprotein: co-opted from a digestive trypsinogen gene.</li>
  <li>Snake venoms: co-opted from various secreted enzymes (e.g., phospholipases, peptide hormones).</li>
  <li>Mammalian milk proteins: co-opted from immune-defense and metabolic proteins.</li>
</ul>
<h4>Why it's important</h4>
<ol>
  <li><strong>Solves "where do novel traits come from?"</strong> Not de novo invention — refinement of existing capacity.</li>
  <li><strong>Why complex new organs share deep homology with old machinery.</strong> Lenses ↔ heat-shock proteins; antifreeze ↔ digestive enzymes.</li>
  <li><strong>Real innovation = regulatory tweaking + sequence refinement.</strong> Cooption is the dominant mode; pure invention is rare.</li>
  <li><strong>Robbins-bait.</strong> "How did the eye lens evolve transparency?" — co-opted from heat-shock proteins. Lens crystallins are NOT a new gene family.</li>
</ol>`
    },
  });
})();
