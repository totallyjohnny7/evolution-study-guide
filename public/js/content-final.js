/* auto-generated — Final = Exam1+2+3 + Textbook + Visuals + Cheatsheets. */
window.COURSE = {
  "id": "final",
  "title": "BIOL 4230 — Final Exam · Everything",
  "subtitle": "Exam 1 + 2 + 3 consolidated · 56 sections · 407 MCQs · 0 flashcards · 170+ diagrams",
  "hasVisuals": true,
  "chapters": [
    {
      "id": "ch_s_evo_mech",
      "num": "I",
      "title": "Evolutionary Mechanisms",
      "tagline": "The five forces that change allele frequencies — the engine of evolution.",
      "sections": [
        {
          "id": "s_ns",
          "num": "",
          "title": "Natural Selection",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Natural selection** = differential survival and reproduction of individuals based on heritable traits. The NON-RANDOM mechanism of evolution. Requires 3 conditions: (1) phenotypic variation, (2) variation is heritable (genetic), (3) variation affects fitness (differential survival/reproduction).",
              "label": null
            },
            {
              "kind": "yb",
              "body": "Natural selection is the ONLY mechanism that consistently produces adaptation. All other forces (drift, mutation, gene flow) are either random or directionless. Selection specifically favors traits that improve reproductive success in the current environment.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **Breeder's Equation:** R = h² × S (Response = heritability × selection differential)\n\r\n2. **Selection Differential (S)** = mean of breeders − mean of total population\n\r\n3. **Heritability (h²)** = VA / VP = additive genetic variance / total phenotypic variance\n\r\n4. If h² = 0 OR S = 0 → R = 0 → NO evolutionary change (selection without heritability = no evolution)",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Natural selection CAN act on a trait without causing EVOLUTION if the variation is not heritable. Example: all tall plants grew in good soil (environment), not because of genes. Selection culls them, but allele frequencies don't change. R = h² × S: if h² = 0, then R = 0 regardless of how strong selection is.",
              "label": "&#9888; Trap — Selection Without Heritability &ne; Evolution"
            },
            {
              "kind": "trap",
              "body": "Selection is non-random (favors higher fitness genotypes) but outcomes are not guaranteed. In small populations, drift can overpower selection even for beneficial alleles. &ldquo;Evolution is not completely random&rdquo; is the key phrase — selection is directional but the environment + alleles determine direction.",
              "label": "&#9888; Trap — Selection is Non-Random, Not Deterministic"
            },
            {
              "kind": "rem",
              "body": "Selection acts on PHENOTYPES, but evolution occurs in ALLELE FREQUENCIES. The bridge is heritability (h²). No heritability = selection cannot move allele frequencies = no evolution.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "mn",
              "body": "&ldquo;**V-F-H-P**: Variation, Fitness differences, Heritable, Predictable change&rdquo; = the 4 conditions that guarantee natural selection produces evolution.",
              "label": "Mnemonic"
            },
            {
              "kind": "svg",
              "viz": "selection-types",
              "svg": "<span class='svg-title'>Three Modes of Natural Selection</span><div class='svg-ctrls'><button data-mode='stabilizing'>Stabilizing</button><button data-mode='directional'>Directional</button><button data-mode='disruptive'>Disruptive</button></div><svg viewBox='0 0 320 120' role='img' aria-label='Selection-mode distributions'><defs><linearGradient id='sel-g1' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#64646d' stop-opacity='.35'/><stop offset='1' stop-color='#64646d' stop-opacity='.05'/></linearGradient><linearGradient id='sel-g2' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#f5c542' stop-opacity='.55'/><stop offset='1' stop-color='#f5c542' stop-opacity='.08'/></linearGradient></defs><g class='axis'><line x1='20' y1='100' x2='300' y2='100' stroke='#31313a' stroke-width='1'/><text x='160' y='115' text-anchor='middle' fill='#8a8a94' font-size='10'>phenotype →</text></g><path id='sel-before' d='' fill='url(#sel-g1)' stroke='#8a8a94' stroke-width='1.1'/><path id='sel-after' d='' fill='url(#sel-g2)' stroke='#f5c542' stroke-width='1.4'/><g font-size='10' font-family='JetBrains Mono, monospace'><rect x='210' y='8' width='10' height='3' fill='#8a8a94'/><text x='224' y='12' fill='#b6b6bd'>before</text><rect x='260' y='8' width='10' height='3' fill='#f5c542'/><text x='274' y='12' fill='#b6b6bd'>after</text></g></svg><div id='sel-caption' class='svg-sub'></div>",
              "caption": "Click to switch modes — watch the shape of the post-selection distribution."
            },
            {
              "kind": "svg",
              "viz": "breeders-eq",
              "svg": "<span class='svg-title'>Breeder's Equation — R = h² × S</span><div class='svg-ctrls' style='gap:12px;align-items:center;'><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>h² <input data-range='h2' type='range' min='0' max='1' step='0.05' value='0.5'></label><span style='font-family:JetBrains Mono,monospace;font-size:11px;color:#f5c542;'>h² = <span data-val='h2'>0.50</span></span></div><svg viewBox='0 0 300 200' role='img' aria-label='Parent-offspring regression'><g class='axis'><line x1='34' y1='166' x2='286' y2='166' stroke='#31313a'/><line x1='34' y1='14' x2='34' y2='166' stroke='#31313a'/><text x='160' y='184' fill='#8a8a94' font-size='10' text-anchor='middle'>midparent phenotype →</text><text x='14' y='90' fill='#8a8a94' font-size='10' text-anchor='middle' transform='rotate(-90,14,90)'>offspring phenotype →</text><line x1='34' y1='90' x2='286' y2='90' stroke='#26262b' stroke-dasharray='2,3'/><line x1='160' y1='14' x2='160' y2='166' stroke='#26262b' stroke-dasharray='2,3'/><text x='158' y='24' fill='#64646d' font-size='9'>μ</text></g><g fill='#7cc4ff'><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/><circle class='be-pt' cx='0' cy='0' r='3' opacity='0'/></g><line id='be-line' stroke='#f5c542' stroke-width='2'/><line id='be-sel-arrow' stroke='#34d399' stroke-width='2' marker-end='url(#ar-head)'/><defs><marker id='ar-head' viewBox='0 0 10 10' refX='5' refY='5' markerWidth='6' markerHeight='6' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 Z' fill='#34d399'/></marker></defs><circle id='be-meanoff' r='5' fill='#34d399' stroke='#0a0a0c' stroke-width='1.5'/><text x='205' y='50' fill='#34d399' font-size='10' font-family='JetBrains Mono,monospace'>R (response)</text></svg><div class='svg-legend'><span><i style='background:#7cc4ff'></i>parent→offspring pairs</span><span><i style='background:#f5c542'></i>regression slope = h²</span><span><i style='background:#34d399'></i>mean offspring of breeders</span></div><div class='svg-sub'>S = <span data-val='S'>+10</span>  ·  h² = <span data-val='h2'>0.50</span>  ·  R = h²·S = <span data-val='R'>+5.0</span> <br>Selection differential S picks breeders from +10 above μ. Response R slides with heritability: at h²=0 → R=0 (no evolution despite selection).</div>",
              "caption": "Interactive — slide h² to see why selection without heritability produces no evolution."
            }
          ]
        },
        {
          "id": "s_drift",
          "num": "",
          "title": "Genetic Drift",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Genetic drift** = random fluctuation of allele frequencies due to chance sampling. Strongest in **small populations**. Can cause evolution even when selection is absent. Results in: (1) reduced genetic variation, (2) non-adaptive allele frequency changes, (3) fixation or loss of alleles by chance.",
              "label": null
            },
            {
              "kind": "yb",
              "body": "In small populations, drift OVERWHELMS natural selection — a beneficial allele can be lost by chance, a deleterious allele can fix. This is why conservation of small populations (Ne) is critical. Two types of extreme drift: Bottleneck Effect and Founder Effect.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Bottleneck Effect",
                "Founder Effect"
              ],
              "rows": [
                [
                  "**Trigger**",
                  "Catastrophic reduction in population size (disease, disaster)",
                  "Small group colonizes new area, isolated from source population"
                ],
                [
                  "**Result**",
                  "Reduced genetic diversity; allele frequencies changed by chance",
                  "New population has a subset of original alleles; may fix or lose alleles randomly"
                ],
                [
                  "**FST effect**",
                  "Population diverges from original",
                  "New population diverges from source; different allele frequencies"
                ],
                [
                  "**Example**",
                  "Tasmanian devils + facial tumor disease",
                  "Amish populations (Ellis-van Creveld syndrome)"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Drift is RANDOM — it can increase OR decrease ANY allele's frequency regardless of fitness. Selection is NON-RANDOM — it consistently favors higher-fitness genotypes. In a SMALL population, drift can overwhelm selection and fix a deleterious allele or lose a beneficial one. In a LARGE population, selection dominates. Population size determines which force wins.",
              "label": "&#9888; Trap — Drift vs. Selection"
            },
            {
              "kind": "rem",
              "body": "Drift = nonadaptive evolution. It can cause fixation of deleterious alleles in small populations — this is why genetic diversity matters for conservation. Drift reduces genetic variation; selection uses it.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "svg",
              "viz": "drift-sim",
              "svg": "<span class='svg-title'>Wright-Fisher Drift Simulation — 6 independent populations</span><div class='svg-ctrls' style='gap:12px;align-items:center;'><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>N = <span data-val='N'>20</span> <input data-range='N' type='range' min='4' max='200' step='2' value='20'></label><button data-action='run'>▶ Re-run</button><button data-action='reset'>Clear</button></div><svg viewBox='0 0 320 160' role='img'><g class='axis'><line x1='28' y1='132' x2='300' y2='132' stroke='#31313a'/><line x1='28' y1='10' x2='28' y2='132' stroke='#31313a'/><text x='160' y='150' fill='#8a8a94' font-size='10' text-anchor='middle'>generations →</text><text x='10' y='70' fill='#8a8a94' font-size='10' text-anchor='middle' transform='rotate(-90,10,70)'>p (allele A)</text><line x1='28' y1='10' x2='300' y2='10' stroke='#26262b' stroke-dasharray='3,3'/><text x='304' y='14' fill='#64646d' font-size='9'>1</text><line x1='28' y1='71' x2='300' y2='71' stroke='#26262b' stroke-dasharray='3,3'/><text x='304' y='75' fill='#64646d' font-size='9'>.5</text><text x='304' y='134' fill='#64646d' font-size='9'>0</text></g><g id='drift-plot'></g></svg><div class='svg-sub'>Each colored line = one 100-generation Wright-Fisher simulation starting at p=0.5. Small N → wild swings, fast fixation/loss. Large N → lines stay near 0.5.</div>",
              "caption": "Drag N to change population size — rerun to see how drift strength scales with 1/N."
            }
          ]
        },
        {
          "id": "s_gf_mut",
          "num": "",
          "title": "Gene Flow & Mutation",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Gene flow** = movement of alleles between populations via migration. Effect: **homogenizes populations** (makes them more similar). High gene flow → low FST (genetic differentiation). Low gene flow → populations diverge by drift/selection. Gene flow can PREVENT local adaptation by constantly importing alleles from other environments.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Mutation** = changes in DNA sequence. The ONLY source of NEW alleles that did not previously exist. Mutations are RANDOM with respect to fitness — not directed by need. Selection acting on mutations is NON-RANDOM. Mutations are rare events, so mutation pressure alone changes allele frequencies slowly.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Gene flow, drift, selection, and non-random mating only REDISTRIBUTE existing variation. Only MUTATION introduces truly new alleles. On multiple choice: \"which force is the ultimate source of all new genetic variation?\" = MUTATION. Every other force works with pre-existing alleles.",
              "label": "&#9888; Trap — Only Mutation Creates NEW Alleles"
            },
            {
              "kind": "trap",
              "body": "Mutations are random with respect to their EFFECTS on fitness. They do NOT occur &ldquo;because&rdquo; the organism needs them. Antibiotic resistance: bacteria don't mutate IN RESPONSE to antibiotics — pre-existing random mutations are selected when antibiotics kill susceptibles. The mutation was random; the selection is non-random.",
              "label": "&#9888; Trap — Mutations Are Random; Selection Is Not"
            }
          ]
        },
        {
          "id": "s_applied",
          "num": "",
          "title": "Applied Evolutionary Scenarios: Drug Resistance, Influenza & Domestication",
          "blocks": [
            {
              "kind": "wb",
              "body": "All three applied scenarios share the same evolutionary logic: **heritable variation** in a target trait exists in the population before selection begins, **selection** is non-random and consistently favors one variant, and the population **responds** with allele frequency change across generations. The agent of selection differs (antibiotic, immune pressure, human breeder) but the mechanism is identical.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "System",
                "Selective Force",
                "Heritable Variation Source",
                "Evolutionary Outcome"
              ],
              "rows": [
                [
                  "**Antibiotic Resistance**",
                  "Antibiotic kills susceptible bacteria",
                  "Pre-existing random mutations in bacterial DNA",
                  "Resistance allele frequency rises; population becomes resistant"
                ],
                [
                  "**Influenza Virulence**",
                  "Host immune response; antiviral drugs; transmission dynamics",
                  "High mutation rate of RNA polymerase generates standing variation",
                  "Strains with altered hemagglutinin/neuraminidase evade immunity; virulence can increase or decrease depending on selection pressure"
                ],
                [
                  "**Domestication (e.g., greyhounds)**",
                  "Human artificial selection for speed, tameness, morphology",
                  "Standing genetic variation in ancestral wolf/wild populations",
                  "Rapid allele frequency change at loci controlling selected traits; phenotypic divergence from wild ancestor"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Antibiotics do NOT cause bacteria to mutate toward resistance. Resistance mutations existed BEFORE the drug was introduced — they arose from random replication errors. The antibiotic kills susceptibles, leaving resistant variants to reproduce. The mutation was random; the selection is directional and non-random. This distinction is tested directly on exams.",
              "label": "&#9888; Trap — Mutations Are RANDOM; Selection Is NON-RANDOM"
            }
          ]
        },
        {
          "id": "s_inbreeding",
          "num": "",
          "title": "Inbreeding & Non-Random Mating",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Inbreeding** = mating between closely related individuals. Effect: increases HOMOZYGOSITY (both alleles identical by descent) and decreases heterozygosity. KEY: inbreeding changes GENOTYPE frequencies (more homozygotes, fewer heterozygotes) but does NOT directly change ALLELE frequencies (p and q are unchanged).",
              "label": null
            },
            {
              "kind": "yb",
              "body": "**Inbreeding depression**: increased expression of deleterious recessive alleles in homozygotes. Population shows excess homozygotes compared to HWE expectations. Inbreeding does NOT cause evolution directly (no allele frequency change) but EXPOSES hidden recessive variation to selection.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Inbreeding shifts GENOTYPE frequencies (more AA and aa, fewer Aa) but DOES NOT change p or q. You could calculate p from genotype counts before and after inbreeding and get the SAME p. This is why inbreeding violates HWE (changes genotype distribution) but is NOT itself a force that drives allele frequency change. However, inbreeding exposes recessives to selection, which THEN can change allele frequencies indirectly.",
              "label": "&#9888; Trap — Inbreeding Changes Genotypes, NOT Allele Frequencies"
            }
          ]
        }
      ],
      "group": "Exam 1",
      "cheatsheet": "**Ch I · Evolutionary Mechanisms** — The five forces that change allele frequencies — the engine of evolution.\n\n**§  Natural Selection**\n• **Natural selection** = differential survival and reproduction of individuals based on heritable traits.\n• ⚠ Natural selection CAN act on a trait without causing EVOLUTION if the variation is not heritable.\n\n**§  Genetic Drift**\n• **Genetic drift** = random fluctuation of allele frequencies due to chance sampling.\n• ⚠ Drift is RANDOM — it can increase OR decrease ANY allele's frequency regardless of fitness.\n\n**§  Gene Flow & Mutation**\n• **Gene flow** = movement of alleles between populations via migration.\n• ⚠ Gene flow, drift, selection, and non-random mating only REDISTRIBUTE existing variation.\n\n**§  Applied Evolutionary Scenarios: Drug Resistance, Influenza & Domestication**\n• All three applied scenarios share the same evolutionary logic: **heritable variation** in a target trait exists in the population before selection begins, **selection** is non-rand…\n• ⚠ Antibiotics do NOT cause bacteria to mutate toward resistance.\n\n**§  Inbreeding & Non-Random Mating**\n• **Inbreeding** = mating between closely related individuals.\n• ⚠ Inbreeding shifts GENOTYPE frequencies (more AA and aa, fewer Aa) but DOES NOT change p or q."
    },
    {
      "id": "ch_s_genetics",
      "num": "II",
      "title": "Genetics & Genomics",
      "tagline": "From DNA to phenotype — and back to allele frequencies.",
      "sections": [
        {
          "id": "s_hwe",
          "num": "Hardy",
          "title": "Weinberg Equilibrium",
          "blocks": [
            {
              "kind": "wb",
              "body": "The **Hardy-Weinberg equilibrium (HWE)** is the null hypothesis of population genetics: in a large, randomly mating population with no selection, mutation, gene flow, or drift, genotype frequencies p² + 2pq + q² = 1 remain constant across generations. Used to DETECT evolution by testing for deviations.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Count genotypes (AA, Aa, aa) in the population\n\r\n2. Calculate allele frequencies: p = (2×AA + Aa) / 2N ; q = (2×aa + Aa) / 2N ; or simply p + q = 1\n\r\n3. Calculate EXPECTED genotype counts: p²×N (AA), 2pq×N (Aa), q²×N (aa)\n\r\n4. Compare OBSERVED vs. EXPECTED — excess homozygotes suggests inbreeding/population structure; excess heterozygotes suggests heterozygote advantage",
              "label": null
            },
            {
              "kind": "trap",
              "body": "HWE at one locus means that ONE locus, at ONE moment, shows no deviation. It does NOT mean the entire population is not evolving at other loci. Also: if a population meets HWE, you CANNOT conclude &ldquo;no evolutionary forces are acting&rdquo; — only that no forces are DETECTABLY altering genotype frequencies at that locus at that moment.",
              "label": "&#9888; Trap — HWE at One Locus &ne; No Evolution"
            },
            {
              "kind": "wb",
              "body": "**FST** = measure of genetic differentiation between populations. Range: 0–1.**\r\n**FST ≈ 0**: populations genetically similar — high gene flow homogenizes them.**\r\n**FST ≈ 1**: populations completely differentiated — fixed for different alleles.**\r\n**Formula: FST = (HT − HS) / HT****\r\nHT = expected heterozygosity if all populations were one; HS = average expected heterozygosity within subpopulations.**\r\nHigh gene flow → low FST. Drift + isolation → high FST.",
              "label": null
            },
            {
              "kind": "svg",
              "viz": "hwe",
              "svg": "<span class='svg-title'>Hardy-Weinberg Genotype Frequencies</span><div class='svg-ctrls' style='gap:12px;align-items:center;'><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>p = <span data-val='p'>0.50</span> <input data-range='p' type='range' min='0' max='1' step='0.01' value='0.5'></label><span style='font-family:JetBrains Mono,monospace;font-size:11px;color:#7cc4ff;'>q = <span data-val='q'>0.50</span></span></div><svg viewBox='0 0 240 180' role='img' aria-label='Hardy-Weinberg bars'><g class='axis'><line x1='20' y1='142' x2='228' y2='142' stroke='#31313a'/><text x='56' y='158' text-anchor='middle' font-size='10' fill='#f5c542' font-family='JetBrains Mono,monospace'>p² = <tspan data-val='AA'>0.250</tspan></text><text x='120' y='158' text-anchor='middle' font-size='10' fill='#b197fc' font-family='JetBrains Mono,monospace'>2pq = <tspan data-val='Aa'>0.500</tspan></text><text x='184' y='158' text-anchor='middle' font-size='10' fill='#34d399' font-family='JetBrains Mono,monospace'>q² = <tspan data-val='aa'>0.250</tspan></text><text x='56' y='170' text-anchor='middle' font-size='9' fill='#8a8a94'>AA</text><text x='120' y='170' text-anchor='middle' font-size='9' fill='#8a8a94'>Aa</text><text x='184' y='170' text-anchor='middle' font-size='9' fill='#8a8a94'>aa</text></g><rect id='hwe-AA' x='36' width='40' fill='#f5c542' rx='2'/><rect id='hwe-Aa' x='100' width='40' fill='#b197fc' rx='2'/><rect id='hwe-aa' x='164' width='40' fill='#34d399' rx='2'/></svg><div class='svg-sub'>As p rises, heterozygote frequency peaks at p=q=0.5 (2pq=0.5). Rare allele is mostly in heterozygotes — q² is tiny when q is small. This is why recessives hide from selection.</div>",
              "caption": "Interactive — slide p from 0→1 and track p² + 2pq + q² = 1."
            }
          ]
        },
        {
          "id": "s_quant_gen",
          "num": "",
          "title": "Quantitative Genetics & Heritability",
          "blocks": [
            {
              "kind": "wb",
              "body": "Quantitative traits are continuous (height, weight, beak size). Their phenotypic variance is partitioned: **VP = VA + VD + VI + VE**. Only **VA** (additive genetic variance) responds predictably to natural selection. Narrow-sense heritability h² = VA/VP.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Component",
                "Symbol",
                "Definition",
                "Responds to Selection?"
              ],
              "rows": [
                [
                  "Additive genetic variance",
                  "VA",
                  "Variance due to additive effects of alleles (each copy adds a fixed amount)",
                  "**YES** — determines h² and R"
                ],
                [
                  "Dominance variance",
                  "VD",
                  "Variance from allele interactions within a locus (heterozygote vs. homozygote)",
                  "Less predictably"
                ],
                [
                  "Epistatic/Interaction variance",
                  "VI",
                  "Variance from interactions between different loci (gene × gene)",
                  "Less predictably"
                ],
                [
                  "Environmental variance",
                  "VE",
                  "Variance from environmental effects on phenotype (non-genetic)",
                  "NO"
                ]
              ]
            },
            {
              "kind": "hb",
              "body": "1. Measure trait values of parents and offspring\n\r\n2. Plot offspring phenotype (y-axis) vs. midparent phenotype (x-axis)\n\r\n3. Fit a regression line — the SLOPE of this parent-offspring regression = narrow-sense heritability (h²)\n\r\n4. Slope near 1.0 = highly heritable (offspring closely resemble parents). Slope near 0 = mostly environmental.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Broad-sense heritability H² = VG/VP (includes all genetic variance). NARROW-sense heritability h² = VA/VP (only ADDITIVE variance). The breeder's equation uses h², not H². Only additive variance produces predictable parent-offspring resemblance. Dominance and epistasis don't transfer cleanly across generations.",
              "label": "&#9888; Trap — h² = VA/VP, NOT VG/VP"
            },
            {
              "kind": "trap",
              "body": "h² = 0.9 means 90% of VARIATION in a population is explained by additive genetics — it does NOT mean environment is unimportant for the trait. Human height h² ≈ 0.8, yet adequate nutrition is essential for achieving genetic potential. Heritability describes variation within a population, not whether a trait can respond to environmental change.",
              "label": "&#9888; Trap — High Heritability Does NOT Mean Environment Is Unimportant"
            },
            {
              "kind": "hb",
              "body": "**VP = VA + VD + VI + VE****\r\nVA = Additive genetic variance — ONLY component that responds to selection (what h² measures)**\r\nVD = Dominance variance (allele interactions at same locus)**\r\nVI = Interaction/epistatic variance (interactions between loci)**\r\nVE = Environmental variance (non-heritable)**\r\n**h² = VA/VP** — estimated from slope of parent-offspring regression. Only VA responds to selection, so VD and VI do NOT contribute to the Breeder's equation response.",
              "label": null
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Phenotypic Variance Decomposition — V<tspan style='font-size:.8em'>P</tspan> = V<tspan style='font-size:.8em'>A</tspan> + V<tspan style='font-size:.8em'>D</tspan> + V<tspan style='font-size:.8em'>I</tspan> + V<tspan style='font-size:.8em'>E</tspan></span><svg viewBox='0 0 360 130' role='img' aria-label='Variance decomposition stacked bar'><defs><pattern id='hatch-a' width='6' height='6' patternUnits='userSpaceOnUse' patternTransform='rotate(45)'><rect width='6' height='6' fill='#f5c542'/></pattern></defs><g font-family='JetBrains Mono, monospace' font-size='11'><rect x='20' y='26' width='320' height='38' fill='#121216' stroke='#31313a'/><rect x='20' y='26' width='140' height='38' fill='#f5c542'/><rect x='160' y='26' width='60' height='38' fill='#b197fc'/><rect x='220' y='26' width='50' height='38' fill='#7cc4ff'/><rect x='270' y='26' width='70' height='38' fill='#34d399' opacity='.75'/><text x='90' y='49' text-anchor='middle' fill='#0a0a0c' font-weight='700'>V_A</text><text x='190' y='49' text-anchor='middle' fill='#0a0a0c' font-weight='700'>V_D</text><text x='245' y='49' text-anchor='middle' fill='#0a0a0c' font-weight='700'>V_I</text><text x='305' y='49' text-anchor='middle' fill='#0a0a0c' font-weight='700'>V_E</text><text x='20' y='18' fill='#f5c542' font-size='11'>Total phenotypic variance V_P</text><text x='20' y='82' fill='#b6b6bd' font-size='10'>Responds to selection:</text><line x1='20' y1='86' x2='160' y2='86' stroke='#34d399' stroke-width='3'/><text x='90' y='99' text-anchor='middle' fill='#34d399' font-size='10' font-weight='700'>✓ YES — h² = V_A / V_P</text><line x1='160' y1='86' x2='340' y2='86' stroke='#f87171' stroke-width='3' stroke-dasharray='4,2'/><text x='250' y='99' text-anchor='middle' fill='#f87171' font-size='10' font-weight='700'>✗ NOT cleanly</text><text x='20' y='118' fill='#8a8a94' font-size='9.5'>H² (broad-sense) = (V_A+V_D+V_I)/V_P   ·   h² (narrow-sense) = V_A/V_P — use h² in R = h²·S</text></g></svg>",
              "caption": "Only V_A — additive genetic variance — slides cleanly across generations. That's why h² uses V_A only."
            }
          ]
        },
        {
          "id": "s_alleles",
          "num": "",
          "title": "Alleles: Dominant, Recessive & Additive",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Dominant alleles** mask the expression of recessive alleles in heterozygotes (Aa looks like AA). One copy is sufficient to produce the dominant phenotype. ****\r\n**Recessive alleles** require two copies for expression (aa). In Aa heterozygotes the recessive allele is hidden — selection cannot see it. This has major consequences for how quickly rare recessive alleles spread.****\r\n**Additive alleles** contribute a fixed, equal increment per copy. The heterozygote Aa has a phenotype exactly at the midpoint between AA and aa. No masking occurs. Formally: if AA = 10 and aa = 0, then Aa = 5. Each copy of the A allele adds the same fixed amount. The effect is linear with copy number. Most quantitative traits (height, beak size) follow an approximately additive model across many loci.****\r\n**Key formulas:** Additive: phenotype(Aa) = [phenotype(AA) + phenotype(aa)] / 2. The additive genetic variance VA captures this linearity and is the basis of h² = VA/VP.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Allele Type",
                "Effect in Aa Heterozygote",
                "Phenotype of Aa",
                "Rate of Spread When Rare & Beneficial"
              ],
              "rows": [
                [
                  "**Dominant**",
                  "Masks recessive; one copy sufficient for expression",
                  "Same as AA (dominant phenotype)",
                  "**Fast** — even one copy is visible to selection in Aa heterozygotes"
                ],
                [
                  "**Recessive**",
                  "Hidden by dominant; requires two copies to be expressed",
                  "Same as AA (dominant phenotype); recessive effect invisible",
                  "**Slow** — when rare, nearly all copies are in Aa heterozygotes where they are masked from selection"
                ],
                [
                  "**Additive**",
                  "Both alleles contribute equally; no masking",
                  "Exactly intermediate between AA and aa",
                  "**Moderate** — each copy contributes a detectable phenotypic effect, so selection can act on heterozygotes"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "When a beneficial recessive allele is at low frequency q, Hardy-Weinberg predicts: frequency of heterozygotes Aa = 2pq &asymp; 2q (when q is small, p &asymp; 1). Frequency of aa homozygotes = q². Since q² << 2q when q is small, the vast majority of copies of the recessive allele are HIDDEN in Aa heterozygotes where they are masked and invisible to selection. Selection can only act on the phenotype — and since Aa looks like AA, selection cannot distinguish them. Only as q rises and q² becomes appreciable do meaningful numbers of aa homozygotes appear, and only then does selection become fully effective. A dominant beneficial allele by contrast is immediately visible in the very first Aa heterozygote and spreads rapidly.",
              "label": "&#9888; Trap — Rare Beneficial Recessives Spread Slowly"
            },
            {
              "kind": "rem",
              "body": "Additive alleles are the foundation of quantitative trait genetics. Because each copy adds a fixed amount, additive effects sum cleanly across loci and across copies, generating the continuous variation captured by VA and predicted by the breeder's equation R = h² × S. Dominance and recessiveness create non-linearities that are harder to predict across generations.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "svg",
              "viz": "allele-dose",
              "svg": "<span class='svg-title'>Allele Dose → Phenotype — Three Inheritance Models</span><div class='svg-ctrls'><button data-dose='dominant'>Dominant</button><button data-dose='recessive'>Recessive</button><button data-dose='additive'>Additive</button></div><svg viewBox='0 0 280 170' role='img'><g class='axis'><line x1='36' y1='136' x2='260' y2='136' stroke='#31313a'/><line x1='36' y1='14' x2='36' y2='136' stroke='#31313a'/><text x='36' y='150' text-anchor='middle' fill='#8a8a94' font-size='10'>aa</text><text x='148' y='150' text-anchor='middle' fill='#8a8a94' font-size='10'>Aa</text><text x='260' y='150' text-anchor='middle' fill='#8a8a94' font-size='10'>AA</text><text x='148' y='163' text-anchor='middle' fill='#64646d' font-size='9'>genotype (copies of A)</text><text x='20' y='75' text-anchor='middle' fill='#8a8a94' font-size='10' transform='rotate(-90,20,75)'>phenotype</text><text x='28' y='20' text-anchor='end' fill='#64646d' font-size='9'>10</text><text x='28' y='76' text-anchor='end' fill='#64646d' font-size='9'>5</text><text x='28' y='140' text-anchor='end' fill='#64646d' font-size='9'>0</text></g><path id='dose-line' d='' stroke='#f5c542' stroke-width='2.2' fill='none'/><circle class='dose-pt' cx='0' cy='0' r='5' fill='#f5c542' stroke='#0a0a0c' stroke-width='1.5'/><circle class='dose-pt' cx='0' cy='0' r='5' fill='#f5c542' stroke='#0a0a0c' stroke-width='1.5'/><circle class='dose-pt' cx='0' cy='0' r='5' fill='#f5c542' stroke='#0a0a0c' stroke-width='1.5'/></svg><div id='dose-caption' class='svg-sub'></div>",
              "caption": "Click mode — notice Aa position: identical to AA under dominance, identical to aa under recessive, exact midpoint when additive."
            }
          ]
        },
        {
          "id": "s_plasticity",
          "num": "",
          "title": "Phenotypic Plasticity & Reaction Norms",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Phenotypic plasticity** = one genotype produces different phenotypes in different environments. A **reaction norm** = a plot of phenotype (y-axis) vs. environment (x-axis) for a single genotype. Sloped reaction norm = plasticity. Non-parallel slopes between genotypes = genotype-by-environment interaction (G×E, VG×E).",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. FLAT line for a genotype = NO plasticity for that genotype (same phenotype in all environments)\n\r\n2. SLOPED line = plasticity (phenotype changes with environment)\n\r\n3. PARALLEL sloped lines for different genotypes = plasticity but NO G×E (all genotypes respond equally)\n\r\n4. NON-PARALLEL lines (crossing or different slopes) = G×E interaction (genotypes differ in HOW they respond to environment)",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Polyphenic traits = discrete phenotypes from one genotype (e.g., army ant castes, wasp queens vs. workers — same genes, completely different bodies based on larval conditions). Continuous plasticity = gradual phenotypic change with environment (e.g., plant height increasing with water). Both are phenotypic plasticity, but polypheny produces DISCRETE forms.",
              "label": "&#9888; Trap — Polyphenic vs. Continuous Plasticity"
            },
            {
              "kind": "wb",
              "body": "**Gene-by-Environment interaction (G×E)**: different genotypes respond differently to the same environmental change. On a reaction norm plot: **parallel lines** = no G×E (genotypes maintain same rank order across environments). **Non-parallel / crossing lines** = G×E present (one genotype is best in environment A, another is best in environment B). Crossing reaction norms mean there is NO single universally \"best\" genotype — selection favors different genotypes in different environments.",
              "label": null
            },
            {
              "kind": "svg",
              "viz": "reaction-norms",
              "svg": "<span class='svg-title'>Reaction Norms — Plasticity &amp; G×E Interaction</span><div class='svg-ctrls'><button data-rn='flat'>No plasticity</button><button data-rn='parallel'>Parallel (plastic, no G×E)</button><button data-rn='gxe'>Crossing (G×E)</button></div><svg viewBox='0 0 280 170' role='img'><g class='axis'><line x1='30' y1='138' x2='260' y2='138' stroke='#31313a'/><line x1='30' y1='14' x2='30' y2='138' stroke='#31313a'/><text x='146' y='156' text-anchor='middle' fill='#8a8a94' font-size='10'>environment →</text><text x='16' y='76' text-anchor='middle' fill='#8a8a94' font-size='10' transform='rotate(-90,16,76)'>phenotype</text><text x='44' y='153' fill='#64646d' font-size='9'>cold</text><text x='244' y='153' fill='#64646d' font-size='9' text-anchor='end'>warm</text></g><path id='rn-g1' d='' stroke='#f5c542' stroke-width='2.2' fill='none'/><path id='rn-g2' d='' stroke='#7cc4ff' stroke-width='2.2' fill='none'/><g font-family='JetBrains Mono,monospace' font-size='10'><rect x='195' y='18' width='10' height='3' fill='#f5c542'/><text x='210' y='22' fill='#b6b6bd'>Genotype 1</text><rect x='195' y='32' width='10' height='3' fill='#7cc4ff'/><text x='210' y='36' fill='#b6b6bd'>Genotype 2</text></g></svg><div id='rn-caption' class='svg-sub'></div>",
              "caption": "Each line = one genotype across two environments. Crossing lines = G×E (rank-reversal)."
            }
          ]
        },
        {
          "id": "s_genome",
          "num": "",
          "title": "Genome Structure & Gene Expression Regulation",
          "blocks": [
            {
              "kind": "wb",
              "body": "Eukaryotic genomes (including human) contain: protein-coding genes (~1.5% of human genome), pseudogenes (non-functional copies of genes), mobile genetic elements/transposons (~45% of human genome), introns, regulatory sequences, and other non-coding DNA. Genome SIZE does not correlate with organismal complexity (C-value paradox).",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Level of Regulation",
                "Mechanism",
                "When it Acts"
              ],
              "rows": [
                [
                  "**Pre-transcriptional**",
                  "DNA methylation, histone modification, chromatin remodeling",
                  "Before RNA is made — controls DNA accessibility"
                ],
                [
                  "**Transcriptional**",
                  "Transcription factors binding promoters/enhancers",
                  "During RNA synthesis — affects how much mRNA is made"
                ],
                [
                  "**Post-transcriptional**",
                  "Alternative splicing, microRNA (miRNA), RNA degradation",
                  "After RNA is made, before/during translation"
                ],
                [
                  "**Post-translational**",
                  "Protein phosphorylation, ubiquitination, glycosylation, cleavage",
                  "After protein is made — affects protein activity/stability"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "DNA methylation = PRE-transcriptional (controls whether a gene is accessible for transcription). microRNA (miRNA) = POST-transcriptional (binds to mRNA and promotes its degradation or blocks translation). These are TWO DIFFERENT levels. Robbins tests whether you know which regulatory mechanism acts at which stage.",
              "label": "&#9888; Trap — microRNA vs. DNA Methylation Levels"
            }
          ]
        }
      ],
      "group": "Exam 1",
      "cheatsheet": "**Ch II · Genetics & Genomics** — From DNA to phenotype — and back to allele frequencies.\n\n**§ Hardy Weinberg Equilibrium**\n• The **Hardy-Weinberg equilibrium (HWE)** is the null hypothesis of population genetics: in a large, randomly mating population with no selection, mutation, gene flow, or drift, gen…\n• ⚠ HWE at one locus means that ONE locus, at ONE moment, shows no deviation.\n\n**§  Quantitative Genetics & Heritability**\n• Quantitative traits are continuous (height, weight, beak size).\n• ⚠ Broad-sense heritability H² = VG/VP (includes all genetic variance).\n\n**§  Alleles: Dominant, Recessive & Additive**\n• **Dominant alleles** mask the expression of recessive alleles in heterozygotes (Aa looks like AA).\n• ⚠ When a beneficial recessive allele is at low frequency q, Hardy-Weinberg predicts: frequency of heterozygotes Aa = 2pq &asymp; 2q (when q is…\n\n**§  Phenotypic Plasticity & Reaction Norms**\n• **Phenotypic plasticity** = one genotype produces different phenotypes in different environments.\n• ⚠ Polyphenic traits = discrete phenotypes from one genotype (e.g., army ant castes, wasp queens vs.\n\n**§  Genome Structure & Gene Expression Regulation**\n• Eukaryotic genomes (including human) contain: protein-coding genes (~1.5% of human genome), pseudogenes (non-functional copies of genes), mobile genetic elements/transposons (~45%…\n• ⚠ DNA methylation = PRE-transcriptional (controls whether a gene is accessible for transcription)."
    },
    {
      "id": "ch_s_hist",
      "num": "III",
      "title": "Evolutionary History & Key Figures",
      "tagline": "Who discovered what, and why it mattered.",
      "sections": [
        {
          "id": "s_key_figures",
          "num": "",
          "title": "Key Figures in Evolutionary Thought",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "Figure",
                "Key Contribution",
                "Key Detail"
              ],
              "rows": [
                [
                  "**Lamarck**",
                  "Proposed inheritance of acquired characteristics (use/disuse)",
                  "Wrong mechanism (acquired traits aren't heritable), but right that species change over time. First serious evolutionary framework."
                ],
                [
                  "**Charles Lyell**",
                  "Uniformitarianism — gradual geological processes, deep time",
                  "Influenced Darwin: if geology takes millions of years, there was enough time for biological evolution to occur gradually"
                ],
                [
                  "**William Smith**",
                  "Stratigraphy — used fossils to date rock layers; established reality of extinction",
                  "Different rock layers contain different fossil assemblages → species have gone extinct; Earth has a history"
                ],
                [
                  "**Darwin**",
                  "Theory of evolution by natural selection; descent with modification",
                  "Required VARIATION + HERITABILITY + DIFFERENTIAL SURVIVAL/REPRODUCTION. Origin of Species 1859."
                ],
                [
                  "**Alfred Russel Wallace**",
                  "Independently conceived natural selection simultaneously with Darwin",
                  "Wallace's letter to Darwin in 1858 **prompted Darwin to publish**. Darwin had been sitting on his theory for ~20 years."
                ],
                [
                  "**Great Chain of Being**",
                  "Pre-Darwinian: fixed hierarchical chain of life, humans at top",
                  "No evolution, no extinction in the modern sense. Aristotelian concept. Replaced by evolutionary thinking."
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "**Alfred Russel Wallace** is the answer. Wallace sent Darwin a letter in 1858 describing natural selection independently. Darwin, who had been developing the theory since ~1838, realized he had to publish or lose priority. Darwin and Wallace presented jointly to the Linnean Society in 1858, then Darwin published Origin of Species in 1859.",
              "label": "&#9888; Trap — Who Spurred Darwin to Publish?"
            },
            {
              "kind": "mn",
              "body": "&ldquo;**Lamarck Lifts Wrong Weights; Darwin Wins**&rdquo; = Lamarck (wrong mechanism but evolutionary), Lyell (deep time), William Smith (stratigraphy/extinction), Darwin (natural selection), Wallace (co-discoverer who forced Darwin to publish).",
              "label": "Mnemonic — Key Figures"
            },
            {
              "kind": "wb",
              "body": "**Scala Naturae / Great Chain of Being**: pre-Darwinian concept organizing all life in a fixed, ranked hierarchy (minerals → plants → animals → humans → angels). Three key flaws: (1) Species were **fixed and immutable** — no mechanism for change. (2) **No concept of extinction**. (3) **No common ancestry** — each link was separately created. Aristotle and early Linnaeus worked within this framework. Darwin's tree-of-life model replaced this with branching descent from common ancestors.",
              "label": null
            }
          ]
        },
        {
          "id": "s_sci_method",
          "num": "",
          "title": "Scientific Method: Hypothesis vs. Theory",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Hypothesis:** A tentative, testable explanation for a specific observation. It is provisional — it can be supported or refuted by evidence. A good hypothesis is falsifiable (can be proven wrong by a conceivable experiment) and generates specific, testable predictions.****\r\n**Scientific Theory:** A well-substantiated explanation of a broad phenomenon that has withstood extensive testing across many independent lines of evidence. A theory generates many testable hypotheses. Theories are MORE supported than hypotheses, not less certain. In science, calling something a \"theory\" is the highest level of confidence, not a statement of doubt.****\r\n**Key distinction:** In everyday English, \"theory\" means a guess or hunch. In science, \"theory\" means a framework supported by massive, converging evidence from multiple independent methods. Evolution is a theory in the scientific sense — it is one of the most strongly supported frameworks in all of biology.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Hypothesis",
                "Scientific Theory"
              ],
              "rows": [
                [
                  "**Definition**",
                  "Tentative, testable explanation for a specific observation",
                  "Well-substantiated explanation of a broad phenomenon supported by extensive evidence"
                ],
                [
                  "**Level of support**",
                  "Provisional — awaits testing",
                  "High — has survived repeated testing from multiple independent lines of evidence"
                ],
                [
                  "**Examples**",
                  "\"Bacteria survive penicillin due to a pre-existing resistance mutation\"",
                  "Theory of evolution, germ theory, cell theory, theory of gravity"
                ],
                [
                  "**Common misuse**",
                  "Incorrectly used to mean \"proven fact\" in everyday speech",
                  "Incorrectly used to mean \"guess\" or \"unproven idea\" in everyday English — the opposite of the scientific meaning"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "In everyday English, \"theory\" = a guess or speculation. In science, \"theory\" = the highest level of explanatory framework, supported by massive converging evidence. When someone says \"evolution is just a theory,\" they are using the word in the everyday sense. In the scientific sense, a theory is more strongly supported than a hypothesis, not less. The theory of evolution is supported by genetics, paleontology, comparative anatomy, biogeography, and direct observation — it is not a guess.",
              "label": "&#9888; Trap — \"Theory\" in Science vs. Everyday English"
            }
          ]
        }
      ],
      "group": "Exam 1",
      "cheatsheet": "**Ch III · Evolutionary History & Key Figures** — Who discovered what, and why it mattered.\n\n**§  Key Figures in Evolutionary Thought**\n• **Scala Naturae / Great Chain of Being**: pre-Darwinian concept organizing all life in a fixed, ranked hierarchy (minerals → plants → animals → humans → angels).\n• ⚠ **Alfred Russel Wallace** is the answer.\n\n**§  Scientific Method: Hypothesis vs. Theory**\n• **Hypothesis:** A tentative, testable explanation for a specific observation.\n• ⚠ In everyday English, \"theory\" = a guess or speculation."
    },
    {
      "id": "ch_s_ch10",
      "num": "10",
      "title": "Complex Adaptations & Evo Devo",
      "tagline": "How do complex traits evolve? Molecular mechanisms of morphological change.",
      "sections": [
        {
          "id": "s_evoeye",
          "num": "10.1",
          "title": "Evolution of Complex Traits (Vertebrate Eye)",
          "blocks": [
            {
              "kind": "wb",
              "body": "Complex traits evolve GRADUALLY via many small mutations, each providing a slight fitness advantage. No single mutation produces a fully-formed complex organ. Darwin himself addressed the eye: every intermediate step from a light-sensitive patch to a camera eye is an improvement over having no light detection. Each step is favored by selection.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Gene duplication** is a key mechanism for evolving new complex traits: (1) One copy retains original function (no fitness cost). (2) Duplicate copy is free to accumulate mutations and evolve new functions (**neofunctionalization**). Alternatively, both copies can sub-divide the original function (**subfunctionalization**). Examples: globin gene family (hemoglobin α/β), Hox clusters (vertebrates have 4 Hox clusters vs. 1 in invertebrates due to duplication). Gene duplication explains how a complex pathway can evolve incrementally from a simpler ancestral function.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **Regulatory networks:** Mutations in genes that CONTROL other genes (transcription factors, enhancers) produce large morphological changes from small genetic changes\n\r\n2. **Protein promiscuity:** Proteins can adopt NEW functions while retaining old ones — allows novel traits to evolve from existing proteins\n\r\n3. **Heterochrony:** Changes in TIMING or RATE of gene expression (earlier/later, faster/slower) produce new phenotypes without changing the genes themselves\n\r\n4. **Hox genes:** Master regulatory genes that define body segment IDENTITY along the anterior-posterior axis. Highly conserved across animals (Drosophila and mice use the same Hox genes). Changes in Hox expression = major body plan changes\n\r\n5. **Pax6:** Master regulator of eye development. Found in animals as diverse as flies and humans — shows conserved genetic toolkit for eye development despite very different final eye structures",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Evolution produces traits that are &ldquo;good enough&rdquo; but not optimal. The human eye has a BLIND SPOT (where the optic nerve attaches, no photoreceptors) — an engineering flaw that the octopus eye avoids because octopus eyes evolved independently. Complex traits are constrained by historical contingency (what existed before). Selection cannot design from scratch.",
              "label": "&#9888; Trap — Complex Traits Are NOT Perfect"
            },
            {
              "kind": "rem",
              "body": "Evo Devo = evolution of REGULATORY machinery is more important than evolution of coding sequences. Same genes (e.g., Pax6, Hox) control development across vastly different organisms = deep conservation. Change WHERE and WHEN genes are expressed, not necessarily the genes themselves.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Incremental Evolution of the Vertebrate Eye — Nilsson &amp; Pelger stages</span><svg viewBox='0 0 520 170' role='img' aria-label='Five stages of eye evolution'><defs><radialGradient id='sky' cx='.35' cy='.3'><stop offset='0' stop-color='#1a1a1d'/><stop offset='1' stop-color='#0b0b0c'/></radialGradient></defs><g font-family='JetBrains Mono, monospace' font-size='9.5' fill='#b6b6bd' text-anchor='middle'><g transform='translate(52,30)'><rect x='-34' y='-12' width='68' height='60' fill='#17171a' stroke='#26262b' rx='4'/><rect x='-24' y='14' width='48' height='12' fill='#f5c542' opacity='.55'/><path d='M-30,-8 L30,-8' stroke='#f5c542' stroke-width='.8' opacity='.35'/><path d='M-20,-4 L-10,14' stroke='#f5c542' stroke-width='1' opacity='.6'/><path d='M0,-4 L0,14' stroke='#f5c542' stroke-width='1' opacity='.6'/><path d='M20,-4 L10,14' stroke='#f5c542' stroke-width='1' opacity='.6'/><text y='70' fill='#f5c542' font-weight='700'>1. Flat patch</text><text y='84' fill='#8a8a94'>photosensitive</text><text y='96' fill='#8a8a94'>cells, no image</text></g><g transform='translate(156,30)'><rect x='-34' y='-12' width='68' height='60' fill='#17171a' stroke='#26262b' rx='4'/><path d='M-22,30 Q0,6 22,30' fill='#f5c542' opacity='.55' stroke='#9c7c20' stroke-width='1'/><path d='M-30,-8 L30,-8' stroke='#f5c542' stroke-width='.8' opacity='.35'/><path d='M-15,-4 L-10,12' stroke='#f5c542' stroke-width='1' opacity='.7'/><path d='M0,-4 L0,10' stroke='#f5c542' stroke-width='1' opacity='.7'/><path d='M15,-4 L10,12' stroke='#f5c542' stroke-width='1' opacity='.7'/><text y='70' fill='#f5c542' font-weight='700'>2. Eye cup</text><text y='84' fill='#8a8a94'>crude direction</text><text y='96' fill='#8a8a94'>detection</text></g><g transform='translate(260,30)'><rect x='-34' y='-12' width='68' height='60' fill='#17171a' stroke='#26262b' rx='4'/><path d='M-22,30 Q-14,4 -6,-2 L6,-2 Q14,4 22,30' fill='#f5c542' opacity='.55' stroke='#9c7c20' stroke-width='1'/><circle cx='0' cy='-6' r='4' fill='url(#sky)' stroke='#f5c542' stroke-width='.6'/><path d='M0,-2 L-8,20' stroke='#f5c542' stroke-width='.8' opacity='.6'/><path d='M0,-2 L8,20' stroke='#f5c542' stroke-width='.8' opacity='.6'/><path d='M0,-2 L0,22' stroke='#f5c542' stroke-width='.8' opacity='.7'/><text y='70' fill='#f5c542' font-weight='700'>3. Pinhole</text><text y='84' fill='#8a8a94'>narrow aperture</text><text y='96' fill='#8a8a94'>crude image</text></g><g transform='translate(364,30)'><rect x='-34' y='-12' width='68' height='60' fill='#17171a' stroke='#26262b' rx='4'/><path d='M-22,30 Q-18,4 -10,-6 L10,-6 Q18,4 22,30' fill='#17171a' stroke='#9c7c20' stroke-width='1'/><ellipse cx='0' cy='-2' rx='11' ry='9' fill='rgba(245,197,66,.16)' stroke='#f5c542' stroke-width='1.3'/><path d='M-18,24 Q0,6 18,24' fill='#f5c542' opacity='.55' stroke='#9c7c20' stroke-width='.8'/><text y='70' fill='#f5c542' font-weight='700'>4. Primitive lens</text><text y='84' fill='#8a8a94'>transparent cell</text><text y='96' fill='#8a8a94'>mass, focuses</text></g><g transform='translate(468,30)'><rect x='-34' y='-12' width='68' height='60' fill='#17171a' stroke='#26262b' rx='4'/><path d='M-22,30 Q-18,4 -10,-6 L10,-6 Q18,4 22,30' fill='#17171a' stroke='#9c7c20' stroke-width='1'/><ellipse cx='0' cy='2' rx='14' ry='12' fill='rgba(245,197,66,.2)' stroke='#f5c542' stroke-width='1.5'/><circle cx='0' cy='2' r='4' fill='#0a0a0c'/><path d='M-18,24 Q0,8 18,24' fill='#f5c542' opacity='.7' stroke='#9c7c20' stroke-width='.8'/><text y='70' fill='#f5c542' font-weight='700'>5. Camera eye</text><text y='84' fill='#8a8a94'>adjustable iris +</text><text y='96' fill='#8a8a94'>corneal lens</text></g></g><g stroke='#9c7c20' stroke-width='1.2' fill='none' marker-end='url(#ev-arr)'><line x1='88' y1='30' x2='120' y2='30'/><line x1='192' y1='30' x2='224' y2='30'/><line x1='296' y1='30' x2='328' y2='30'/><line x1='400' y1='30' x2='432' y2='30'/></g><defs><marker id='ev-arr' viewBox='0 0 10 10' refX='8' refY='5' markerWidth='6' markerHeight='6' orient='auto'><path d='M0,0 L10,5 L0,10 Z' fill='#9c7c20'/></marker></defs><text x='260' y='155' text-anchor='middle' font-size='10.5' fill='#8a8a94' font-family='JetBrains Mono,monospace'>Each stage is a viable eye AND an improvement — selection climbs a continuous fitness gradient.</text></svg>",
              "caption": "Nilsson & Pelger (1994) showed ~364,000 generations of 1% selection could traverse stages 1→5 — refutes \"irreducible complexity.\""
            }
          ]
        },
        {
          "id": "s_homoana",
          "num": "10.2",
          "title": "Homology vs. Analogy in Complex Traits",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Homologous traits** = similar structures INHERITED from a common ancestor (same developmental origin). May differ in function. **Analogous traits (convergence)** = similar in function but evolved INDEPENDENTLY in separate lineages (different developmental origins). Identifying the correct relationship is critical for phylogenetics.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Homology",
                "Analogy (Convergence)"
              ],
              "rows": [
                [
                  "**Cause**",
                  "Shared ancestry (common descent)",
                  "Same selective pressure, independent evolution"
                ],
                [
                  "**Developmental origin**",
                  "SAME (same genes, same embryonic tissue)",
                  "DIFFERENT (different genes, different tissue)"
                ],
                [
                  "**Example**",
                  "Human arm + bat wing + whale flipper (same bones)",
                  "Bat wing + insect wing (both fly; different structure)"
                ],
                [
                  "**Phylo relevance**",
                  "✓ Evidence of common ancestry",
                  "✗ Misleading if used as evidence of relationship"
                ]
              ]
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Tetrapod Limb Homology — Same Bones, Different Jobs</span><svg viewBox='0 0 520 220' role='img' aria-label='Homologous tetrapod limbs'><defs><style>.bone-H{fill:#f5c542}.bone-R{fill:#7cc4ff}.bone-U{fill:#b197fc}.bone-C{fill:#34d399}.bone-P{fill:#f87171}.bone-O{stroke:#0a0a0c;stroke-width:.8}</style></defs><g font-family='JetBrains Mono, monospace' font-size='10' fill='#b6b6bd' text-anchor='middle'><g transform='translate(70,32)'><text y='-8' fill='#f5c542' font-weight='700'>Human arm</text><rect class='bone-H bone-O' x='-7' y='0' width='14' height='50' rx='3'/><rect class='bone-R bone-O' x='-11' y='52' width='8' height='46' rx='2'/><rect class='bone-U bone-O' x='3' y='52' width='8' height='46' rx='2'/><g class='bone-C bone-O'><rect x='-10' y='100' width='4' height='12' rx='1'/><rect x='-4' y='100' width='4' height='12' rx='1'/><rect x='2' y='100' width='4' height='12' rx='1'/><rect x='8' y='100' width='4' height='12' rx='1'/></g><g class='bone-P bone-O'><rect x='-12' y='114' width='4' height='30' rx='1.5'/><rect x='-6' y='114' width='4' height='36' rx='1.5'/><rect x='0' y='114' width='4' height='38' rx='1.5'/><rect x='6' y='114' width='4' height='34' rx='1.5'/><rect x='12' y='114' width='4' height='22' rx='1.5'/></g><text y='170' fill='#8a8a94'>manipulate</text></g><g transform='translate(190,32)'><text y='-8' fill='#f5c542' font-weight='700'>Bat wing</text><rect class='bone-H bone-O' x='-6' y='0' width='12' height='40' rx='3'/><rect class='bone-R bone-O' x='-10' y='42' width='7' height='52' rx='2'/><rect class='bone-U bone-O' x='3' y='42' width='7' height='52' rx='2'/><g class='bone-C bone-O'><rect x='-8' y='96' width='3' height='10' rx='1'/><rect x='-4' y='96' width='3' height='10' rx='1'/><rect x='0' y='96' width='3' height='10' rx='1'/><rect x='4' y='96' width='3' height='10' rx='1'/></g><g class='bone-P bone-O'><rect x='-28' y='108' width='4' height='70' rx='1.5' transform='rotate(-14 -26 142)'/><rect x='-12' y='108' width='4' height='80' rx='1.5' transform='rotate(-6 -10 148)'/><rect x='-2' y='108' width='4' height='86' rx='1.5' transform='rotate(2 0 150)'/><rect x='8' y='108' width='4' height='76' rx='1.5' transform='rotate(10 10 146)'/><rect x='22' y='108' width='4' height='58' rx='1.5' transform='rotate(22 24 138)'/></g><path d='M-30,178 Q-8,188 0,192 Q8,188 28,168' fill='rgba(245,197,66,.06)' stroke='#9c7c20' stroke-width='.5' stroke-dasharray='2,2'/><text y='210' fill='#8a8a94'>fly</text></g><g transform='translate(310,32)'><text y='-8' fill='#f5c542' font-weight='700'>Whale flipper</text><rect class='bone-H bone-O' x='-8' y='0' width='16' height='30' rx='3'/><rect class='bone-R bone-O' x='-10' y='32' width='8' height='26' rx='2'/><rect class='bone-U bone-O' x='2' y='32' width='8' height='26' rx='2'/><g class='bone-C bone-O'><rect x='-9' y='60' width='4' height='10' rx='1'/><rect x='-4' y='60' width='4' height='10' rx='1'/><rect x='1' y='60' width='4' height='10' rx='1'/><rect x='6' y='60' width='4' height='10' rx='1'/></g><g class='bone-P bone-O'><rect x='-11' y='72' width='4' height='70' rx='1.5'/><rect x='-5' y='72' width='4' height='82' rx='1.5'/><rect x='1' y='72' width='4' height='86' rx='1.5'/><rect x='7' y='72' width='4' height='72' rx='1.5'/></g><path d='M-18,70 L-18,170 Q0,180 18,170 L18,70 Z' fill='rgba(124,196,255,.08)' stroke='#7cc4ff' stroke-width='.5' stroke-dasharray='2,2'/><text y='195' fill='#8a8a94'>swim</text></g><g transform='translate(430,32)'><text y='-8' fill='#f5c542' font-weight='700'>Horse leg</text><rect class='bone-H bone-O' x='-6' y='0' width='12' height='32' rx='3'/><rect class='bone-R bone-O' x='-7' y='34' width='6' height='40' rx='2'/><rect class='bone-U bone-O' x='1' y='34' width='6' height='40' rx='2'/><g class='bone-C bone-O'><rect x='-3' y='76' width='6' height='10' rx='1'/></g><g class='bone-P bone-O'><rect x='-3' y='88' width='6' height='60' rx='1.5'/></g><path d='M-7,148 L7,148 L9,162 L-9,162 Z' fill='#8a8a94' stroke='#0a0a0c'/><text y='180' fill='#8a8a94'>run</text></g></g><g font-family='JetBrains Mono, monospace' font-size='10' transform='translate(30,192)'><rect width='10' height='10' class='bone-H'/><text x='16' y='9' fill='#b6b6bd'>Humerus</text><rect x='96' width='10' height='10' class='bone-R'/><text x='112' y='9' fill='#b6b6bd'>Radius</text><rect x='176' width='10' height='10' class='bone-U'/><text x='192' y='9' fill='#b6b6bd'>Ulna</text><rect x='246' width='10' height='10' class='bone-C'/><text x='262' y='9' fill='#b6b6bd'>Carpals</text><rect x='326' width='10' height='10' class='bone-P'/><text x='342' y='9' fill='#b6b6bd'>Phalanges</text></g></svg>",
              "caption": "Same color = same bone inherited from common tetrapod ancestor. Proportions differ by function — homology in structure, analogy in use."
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Convergent Analogy — Bat vs Insect Wing (different origin, same function)</span><svg viewBox='0 0 440 180' role='img' aria-label='Analogous wings'><g font-family='JetBrains Mono, monospace' font-size='10.5' text-anchor='middle'><g transform='translate(110,90)'><text y='-70' fill='#f5c542' font-weight='700'>Bat wing — vertebrate forelimb</text><ellipse cx='0' cy='0' rx='14' ry='18' fill='#f5c542' opacity='.25' stroke='#9c7c20'/><rect x='-2' y='-18' width='4' height='20' fill='#f5c542' stroke='#0a0a0c' stroke-width='.5' rx='1'/><rect x='-1' y='2' width='2' height='22' fill='#7cc4ff' stroke='#0a0a0c' stroke-width='.5'/><g stroke='#f87171' stroke-width='2' stroke-linecap='round'><line x1='0' y1='22' x2='-78' y2='-18'/><line x1='0' y1='22' x2='-64' y2='38'/><line x1='0' y1='22' x2='-22' y2='70'/><line x1='0' y1='22' x2='32' y2='62'/></g><path d='M0,22 L-78,-18 Q-90,10 -64,40 Q-56,56 -22,70 Q8,70 32,62 Z' fill='rgba(248,113,113,.1)' stroke='#f87171' stroke-width='.7'/><text y='100' fill='#b6b6bd'>bones + skin membrane</text><text y='114' fill='#8a8a94'>modified finger bones</text></g><g transform='translate(330,90)'><text y='-70' fill='#b197fc' font-weight='700'>Insect wing — cuticular outgrowth</text><ellipse cx='0' cy='0' rx='10' ry='16' fill='#b197fc' opacity='.25' stroke='#7c5fd6'/><path d='M0,-6 Q-10,-40 -70,-50 Q-86,-30 -86,10 Q-60,30 -20,28 Q0,20 0,-6 Z' fill='rgba(177,151,252,.1)' stroke='#b197fc' stroke-width='.8'/><g stroke='#b197fc' stroke-width='.6' fill='none'><path d='M-4,-6 Q-24,-18 -66,-40'/><path d='M-4,-4 Q-24,-10 -72,-18'/><path d='M-4,0 Q-34,4 -82,6'/><path d='M-4,4 Q-30,14 -70,24'/><path d='M-4,6 Q-18,20 -36,26'/></g><text y='100' fill='#b6b6bd'>chitinous membrane</text><text y='114' fill='#8a8a94'>NO internal bones</text></g><g transform='translate(220,150)'><text y='0' fill='#34d399' font-size='11' font-weight='700'>Same function (flight) · Different developmental origin · Not evidence of shared ancestry</text></g></g></svg>",
              "caption": "Bat wing = modified homologous forelimb bones. Insect wing = cuticle outgrowth with NO skeleton. Same function ≠ same ancestry."
            }
          ]
        }
      ],
      "group": "Exam 2",
      "cheatsheet": "**Ch 10 · Complex Adaptations & Evo Devo** — How do complex traits evolve? Molecular mechanisms of morphological change.\n\n**§ 10.1 Evolution of Complex Traits (Vertebrate Eye)**\n• Complex traits evolve GRADUALLY via many small mutations, each providing a slight fitness advantage.\n• ⚠ Evolution produces traits that are &ldquo;good enough&rdquo; but not optimal.\n\n**§ 10.2 Homology vs. Analogy in Complex Traits**\n• **Homologous traits** = similar structures INHERITED from a common ancestor (same developmental origin)."
    },
    {
      "id": "ch_s_ch11",
      "num": "11",
      "title": "Sexual Reproduction & Sexual Selection",
      "tagline": "Why sex? The paradox of the twofold cost and its solutions.",
      "sections": [
        {
          "id": "s_whysex",
          "num": "11.1",
          "title": "The Paradox of Sex & Its Benefits",
          "blocks": [
            {
              "kind": "wb",
              "body": "Sexual reproduction has a **twofold cost**: in an asexual population, EVERY individual reproduces. In a sexual population, only ~half (females) produce offspring. An asexual mutant in a sexual population would double in frequency each generation. Despite this massive disadvantage, sex persists in almost all multicellular organisms. WHY?",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Benefit of Sex",
                "Mechanism",
                "Key Example"
              ],
              "rows": [
                [
                  "**Combines beneficial mutations**",
                  "Recombination can put two beneficial mutations in the same genome (without recombination, competing beneficial mutations must wait — Clonal Interference)",
                  "E. coli experiments: sexual populations adapt faster when multiple beneficial mutations are available simultaneously"
                ],
                [
                  "**Muller's Ratchet**",
                  "Asexual populations accumulate deleterious mutations irreversibly (ratchet clicks only forward). Recombination can reassemble low-mutation genomes.",
                  "Bacterial pathogens using sexual recombination are more evolvable than obligate asexuals"
                ],
                [
                  "**Reduces sibling competition**",
                  "Asexual offspring are genetically identical — compete for same niche. Sexual offspring are genetically diverse — occupy different niches",
                  "Genetically diverse litters compete less intensely than clones"
                ],
                [
                  "**Red Queen Hypothesis**",
                  "Parasites evolve to exploit COMMON host genotypes. Sex generates rare genotypes that parasites can't easily exploit",
                  "New Zealand snails (Potamopyrgus): sexual populations persist where parasites are common; asexual populations take over where parasites are rare"
                ]
              ]
            },
            {
              "kind": "hb",
              "body": "**Muller's Ratchet**: asexual populations irreversibly accumulate deleterious mutations. Mechanism: (1) In asexual reproduction, the \"least-loaded\" class (fewest mutations) can be lost by drift. (2) Once lost, it cannot be recovered (no recombination). (3) Each loss = one \"click\" of the ratchet — forward only, never back. (4) Over time, mean fitness declines. **Sexual reproduction prevents this** via recombination: can reassemble low-mutation genomes from two high-mutation parents (recombinational repair).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "In a SEXUAL population, males don't directly produce offspring. A population that is 50% male, 50% female has only HALF as many individuals producing offspring as an all-female asexual population of the same size. An asexual mutant in a sexual population doubles in frequency every generation. This is the twofold cost (also called the &ldquo;cost of males&rdquo;). The benefits of sex must OUTWEIGH this 2× disadvantage to be maintained.",
              "label": "&#9888; Trap — Twofold Cost of Sex"
            },
            {
              "kind": "rem",
              "body": "Muller's Ratchet: asexual lineages irreversibly accumulate mutations (ratchet clicks only one direction — more mutations). Red Queen: sex is an evolutionary arms race against parasites — constant genotype shuffling prevents parasites from &ldquo;locking on.&rdquo; Both are about generating variation faster than asexuals can.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "svg",
              "viz": "twofold-cost",
              "svg": "<span class='svg-title'>Twofold Cost of Sex — Asexual Mutant Doubles Each Generation</span><div class='svg-ctrls'><button data-action='step'>Advance 1 generation →</button><button data-action='reset'>Reset</button></div><svg viewBox='0 0 280 140' role='img' aria-label='Sexual vs asexual population'><g font-family='JetBrains Mono, monospace' font-size='10' text-anchor='middle'><text x='70' y='18' fill='#f5c542' font-weight='700'>Sexual</text><text x='210' y='18' fill='#34d399' font-weight='700'>Asexual mutant</text><text x='140' y='18' fill='#b6b6bd'>gen <tspan data-val='gen'>0</tspan></text><rect id='tc-sex-bar' x='46' width='48' fill='#f5c542' opacity='.7' rx='2'/><rect id='tc-asex-bar' x='186' width='48' fill='#34d399' opacity='.7' rx='2'/><text id='tc-sex-label' x='70' fill='#f5c542' font-weight='700'>10</text><text id='tc-asex-label' x='210' fill='#34d399' font-weight='700'>1</text><line x1='10' y1='130' x2='270' y2='130' stroke='#31313a'/><text x='140' y='133' fill='#64646d' font-size='9'>individuals producing offspring</text></g></svg><div class='svg-sub'>Sexual = <span data-val='sex'>10</span> ; Asexual = <span data-val='asex'>1</span>. With equal offspring/female but males don't birth, asexual clones double each generation → within ~4 generations they overtake.</div>",
              "caption": "Click to step generations — asexuals double (8 → 16 → 32), sexuals hold flat at 10 because only half bear young."
            }
          ]
        },
        {
          "id": "s_sexsel",
          "num": "11.2",
          "title": "Sexual Selection & Anisogamy",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Sexual selection** = selection arising from differential MATING success. **Anisogamy** = production of differently-sized gametes (large eggs vs. small sperm). Females invest MORE per gamete (large, few eggs) → more selective. Males invest LESS per gamete (many small sperm) → compete for access to females. This creates the Bateman gradient and sexual dimorphism.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Females",
                "Males"
              ],
              "rows": [
                [
                  "**Gametes**",
                  "Few, large, energetically costly eggs",
                  "Many, small, cheap sperm"
                ],
                [
                  "**Limiting resource**",
                  "Quality mates with good genes / resources",
                  "Access to females (mate number)"
                ],
                [
                  "**Strategy**",
                  "CHOOSY — discriminate; assess mate quality",
                  "COMPETE — for access to as many females as possible"
                ],
                [
                  "**Sexual selection type**",
                  "Intersexual: prefers traits in males (mate choice)",
                  "Intrasexual: competes with other males (male-male competition)"
                ],
                [
                  "**Result**",
                  "Males evolve elaborate displays/traits",
                  "Sexual dimorphism — males often larger, showier"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Sexual selection can favor traits that REDUCE survival (e.g., peacock's tail — attracts predators) if they sufficiently increase MATING success. Natural selection maximizes SURVIVAL; sexual selection maximizes MATINGS. These can conflict. The peacock's tail is maintained because the mating advantage outweighs the predation cost.",
              "label": "&#9888; Trap — Sexual Selection vs. Natural Selection"
            },
            {
              "kind": "trap",
              "body": "All of sexual selection — female choosiness, male competition, sexual dimorphism — traces back to ANISOGAMY (unequal gamete sizes). It is NOT an arbitrary social pattern. It's a fundamental asymmetry: females invest more per gamete, so their time/energy is the limiting resource. Males &ldquo;compete&rdquo; for access to that limiting resource.",
              "label": "&#9888; Trap — Anisogamy Is the Root Cause"
            },
            {
              "kind": "wb",
              "body": "**Sperm competition** = competition between sperm from different males to fertilize a female's eggs (occurs when females mate with multiple males). Drives evolution of:\r\n\n\r\n1. Larger testes relative to body size (more sperm volume)\n\r\n2. Sperm with competitive morphologies (longer, faster)\n\r\n3. Anti-sperm-displacement mechanisms\n\r\n\n\r\n**Sexual conflict** = when the evolutionary interests of males and females diverge, creating arms races within a species:\r\n\n\r\n4. Example: Drosophila seminal proteins (SFPs) increase male reproductive success by reducing female remating and increasing egg-laying — but these same proteins **harm female longevity**\n\r\n5. Females evolve resistance to male manipulation → males evolve more potent SFPs → coevolutionary arms race WITHIN species\n\r\n6. Genital coevolution: male genitalia evolve to increase insemination; female reproductive tracts evolve to retain mate-choice control",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Sperm competition and sexual conflict are WITHIN-species coevolutionary arms races between males and females. This is DIFFERENT from predator-prey arms races between species. Both sexes share the same gene pool but have different reproductive interests, creating interlocus sexual conflict.",
              "label": "&#9888; Trap — Intraspecific vs Interspecific Arms Race"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Anisogamy — The Gamete Asymmetry That Starts Everything</span><svg viewBox='0 0 440 180' role='img' aria-label='Egg vs sperm size comparison'><g font-family='JetBrains Mono, monospace' font-size='11' text-anchor='middle'><g transform='translate(110,88)'><circle r='58' fill='rgba(245,197,66,.15)' stroke='#f5c542' stroke-width='2'/><circle r='52' fill='rgba(245,197,66,.08)' stroke='none'/><circle cx='-18' cy='-12' r='18' fill='rgba(245,197,66,.3)' stroke='#f5c542' stroke-width='1.2'/><circle cx='-18' cy='-12' r='7' fill='#f5c542' opacity='.7'/><text y='-72' fill='#f5c542' font-weight='700' font-size='13'>EGG (ovum)</text><text y='82' fill='#b6b6bd'>≈ 120 µm diameter</text><text y='94' fill='#8a8a94' font-size='9.5'>rich in cytoplasm, mitochondria,</text><text y='106' fill='#8a8a94' font-size='9.5'>mRNA, yolk — huge investment</text></g><g transform='translate(300,88)'><ellipse cx='-10' cy='0' rx='7' ry='5' fill='#7cc4ff'/><path d='M-4,0 Q10,-3 30,1 Q50,5 70,0' stroke='#7cc4ff' stroke-width='1.3' fill='none'/><text y='-72' fill='#7cc4ff' font-weight='700' font-size='13'>SPERM (cell)</text><text y='82' fill='#b6b6bd'>≈ 5 µm head · 50 µm tail</text><text y='94' fill='#8a8a94' font-size='9.5'>minimal cytoplasm — just DNA,</text><text y='106' fill='#8a8a94' font-size='9.5'>flagellum, small mito pod</text></g><g transform='translate(220,150)'><text y='0' fill='#34d399' font-size='11' font-weight='700'>Volume ratio ≈ 10,000,000 : 1 (human) → females limit, males compete</text></g></g></svg>",
              "caption": "Drawn to relative scale: human egg ≈ 120 μm, sperm head ≈ 5 μm. Volume ratio ~10⁷ — this single asymmetry drives all downstream sexual selection."
            },
            {
              "kind": "svg",
              "viz": "bateman",
              "svg": "<span class='svg-title'>Bateman Gradient — Reproductive Success vs Mate Number</span><svg viewBox='0 0 340 200' role='img' aria-label='Bateman gradient'><g class='axis'><line x1='40' y1='170' x2='310' y2='170' stroke='#31313a'/><line x1='40' y1='14' x2='40' y2='170' stroke='#31313a'/><text x='175' y='190' fill='#8a8a94' font-size='10.5' text-anchor='middle'>number of mates →</text><text x='22' y='92' fill='#8a8a94' font-size='10.5' text-anchor='middle' transform='rotate(-90,22,92)'>offspring produced →</text><g font-size='9.5' fill='#64646d'><text x='40' y='184' text-anchor='middle'>0</text><text x='175' y='184' text-anchor='middle'>5</text><text x='310' y='184' text-anchor='middle'>10</text></g></g><line x1='40' y1='170' x2='300' y2='30' stroke='#7cc4ff' stroke-width='3'/><line x1='40' y1='170' x2='310' y2='138' stroke='#f5c542' stroke-width='3'/><line x1='40' y1='170' x2='78' y2='110' stroke='#f5c542' stroke-width='3' stroke-dasharray='3,3' opacity='.6'/><g font-family='JetBrains Mono, monospace' font-size='10.5'><rect x='220' y='30' width='80' height='18' fill='rgba(124,196,255,.1)' stroke='#7cc4ff'/><text x='260' y='43' text-anchor='middle' fill='#7cc4ff'>MALES</text><text x='260' y='60' text-anchor='middle' fill='#7cc4ff' font-size='9.5'>steep slope — more</text><text x='260' y='72' text-anchor='middle' fill='#7cc4ff' font-size='9.5'>mates = more offspring</text><rect x='220' y='120' width='80' height='18' fill='rgba(245,197,66,.1)' stroke='#f5c542'/><text x='260' y='133' text-anchor='middle' fill='#f5c542'>FEMALES</text><text x='260' y='150' text-anchor='middle' fill='#f5c542' font-size='9.5'>flat — limited by</text><text x='260' y='162' text-anchor='middle' fill='#f5c542' font-size='9.5'>egg production, not mates</text></g></svg>",
              "caption": "Male fitness scales with mates; female fitness plateaus — extra mates don't add eggs. This drives male competition and female choosiness."
            }
          ]
        }
      ],
      "group": "Exam 2",
      "cheatsheet": "**Ch 11 · Sexual Reproduction & Sexual Selection** — Why sex? The paradox of the twofold cost and its solutions.\n\n**§ 11.1 The Paradox of Sex & Its Benefits**\n• Sexual reproduction has a **twofold cost**: in an asexual population, EVERY individual reproduces.\n• ⚠ In a SEXUAL population, males don't directly produce offspring.\n\n**§ 11.2 Sexual Selection & Anisogamy**\n• **Sexual selection** = selection arising from differential MATING success.\n• ⚠ Sexual selection can favor traits that REDUCE survival (e.g., peacock's tail — attracts predators) if they sufficiently increase MATING succ…"
    },
    {
      "id": "ch_s_ch12",
      "num": "12",
      "title": "Life History Evolution",
      "tagline": "Trade-offs between growth, reproduction, and survival. When to be born. How many babies. How long to live.",
      "sections": [
        {
          "id": "s_lifehistory",
          "num": "12.1",
          "title": "Life History Trade-offs",
          "blocks": [
            {
              "kind": "wb",
              "body": "Life history = the schedule of an organism's survival, growth, and reproduction across its lifespan. Energy/time are **finite** → allocation to one function REDUCES available for others. Key trade-offs: current reproduction vs. future survival; offspring number vs. offspring size; age at first reproduction vs. lifespan.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Extrinsic mortality** = death from external causes (predation, disease, accidents) — not influenced by the organism's own age or condition. Key rule: **high extrinsic mortality → favor fast life history** (early maturation, high reproductive effort, many offspring). Logic: if you're likely to die young anyway, selection favors getting reproduction done early. **Low extrinsic mortality → favor slow life history** (delayed maturation, low reproductive effort, parental investment). Classic test: island populations with few predators (tortoises, bats) evolve longer lifespans than mainland relatives facing high predation.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **Extrinsic mortality (predation risk):** HIGH predation → early reproduction (may not survive long enough to reproduce later) → shorter lifespan, more offspring per bout. LOW predation → delay reproduction, invest in growth and survival\n\r\n2. **Guppy experiment (Reznick):** Guppies from high-predation streams evolved earlier maturation, smaller body size at maturity, more offspring per litter compared to low-predation streams. ~30 generations for detectable evolution.\n\r\n3. **r/K selection continuum:** r-selected = fast life, many small offspring (unstable environments). K-selected = slow life, few large offspring (stable, near carrying capacity).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Reznick's guppy experiment showed detectable evolutionary change in life history traits in approximately **~30 generations** (not 18, not 100). Guppies were transplanted from high-predation to low-predation streams and evolved LATER maturation, LARGER body at maturity, FEWER offspring — in just ~30 generations. This demonstrates rapid evolution of life history traits under changed selective pressure.",
              "label": "&#9888; Trap — Guppy Experiment Duration"
            },
            {
              "kind": "trap",
              "body": "High current reproduction REDUCES future survival. Classic example: opossum experiment (Austad) — opossums on predator-free island evolved SLOWER aging (longer lifespan, delayed senescence) compared to mainland opossums with high predation. Less predation = more future to invest in = delayed reproduction possible = slower aging.",
              "label": "&#9888; Trap — Current vs. Future Reproduction"
            },
            {
              "kind": "wb",
              "body": "**Seychelles Warbler (Acrocephalus sechellensis)**: classic case study showing how life-history decisions (help vs. disperse vs. reproduce independently) depend on ecological context. Key findings:\r\n\n\r\n1. High-quality territories: Females sometimes stay as **helpers** (delay independent reproduction) — alleles for \"helping\" spread because territory quality limits reproductive success of independents\n\r\n2. Low-quality territories: Females disperse or suppress egg development — helping on poor territory yields no fitness return\n\r\n3. Demonstrates **condition-dependent life history decisions**: the same individual can choose different strategies based on environmental quality\n\r\n4. Illustrates **cooperative breeding as a life history tactic**, not just altruism: helpers wait for better opportunities while gaining experience",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Seychelles warbler helpers are NOT purely altruistic (kin-selected sacrificers). They choose to help when helping in a high-quality territory yields higher inclusive fitness than dispersing to a poor territory. If a high-quality territory opens up nearby, helpers leave. This is a life-history STRATEGY, not selfless altruism.",
              "label": "&#9888; Trap — Helpers Aren't Just Altruistic"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>r/K Selection Continuum — Life History Trade-offs</span><svg viewBox='0 0 480 200' role='img'><defs><linearGradient id='rk-grad' x1='0' x2='1' y1='0' y2='0'><stop offset='0' stop-color='#f87171'/><stop offset='1' stop-color='#34d399'/></linearGradient></defs><g font-family='JetBrains Mono, monospace' font-size='10.5'><rect x='40' y='50' width='400' height='14' fill='url(#rk-grad)' rx='7' opacity='.65'/><polygon points='40,57 28,51 28,63' fill='#f87171'/><polygon points='440,57 452,51 452,63' fill='#34d399'/><text x='40' y='40' fill='#f87171' font-weight='700'>r-selected (fast)</text><text x='440' y='40' fill='#34d399' font-weight='700' text-anchor='end'>K-selected (slow)</text><text x='240' y='40' text-anchor='middle' fill='#f5c542' font-weight='700'>LIFE-HISTORY CONTINUUM</text><g text-anchor='middle' font-size='10'><g transform='translate(60,110)'><circle r='16' fill='rgba(248,113,113,.2)' stroke='#f87171'/><text y='4' fill='#f87171'>🦟</text><text y='34' fill='#f87171' font-size='10'>mosquito</text></g><g transform='translate(130,110)'><circle r='18' fill='rgba(248,113,113,.16)' stroke='#f87171'/><text y='4' fill='#f87171'>🐭</text><text y='34' fill='#f87171' font-size='10'>mouse</text></g><g transform='translate(210,110)'><circle r='20' fill='rgba(245,197,66,.18)' stroke='#f5c542'/><text y='4' fill='#f5c542'>🐇</text><text y='34' fill='#f5c542' font-size='10'>rabbit</text></g><g transform='translate(290,110)'><circle r='22' fill='rgba(245,197,66,.18)' stroke='#f5c542'/><text y='4' fill='#f5c542'>🐺</text><text y='34' fill='#f5c542' font-size='10'>wolf</text></g><g transform='translate(360,110)'><circle r='24' fill='rgba(52,211,153,.2)' stroke='#34d399'/><text y='4' fill='#34d399'>🐘</text><text y='34' fill='#34d399' font-size='10'>elephant</text></g><g transform='translate(430,110)'><circle r='26' fill='rgba(52,211,153,.2)' stroke='#34d399'/><text y='4' fill='#34d399'>🦒</text><text y='34' fill='#34d399' font-size='10'>human</text></g></g><g font-size='9.5' fill='#b6b6bd'><text x='40' y='168' fill='#f87171' font-weight='700'>r-traits:</text><text x='40' y='180'>small · many offspring · no parental care</text><text x='40' y='192'>early maturation · short life · high mortality tolerance</text><text x='440' y='168' text-anchor='end' fill='#34d399' font-weight='700'>K-traits:</text><text x='440' y='180' text-anchor='end'>large · few offspring · heavy parental care</text><text x='440' y='192' text-anchor='end'>late maturation · long life · low extrinsic mortality</text></g></g></svg>",
              "caption": "High extrinsic mortality → r-side (fast life). Low extrinsic mortality → K-side (slow life). Reznick guppies evolved ~30 gens along this axis."
            }
          ]
        },
        {
          "id": "s_aging",
          "num": "12.2",
          "title": "Aging: Mutation Accumulation & Antagonistic Pleiotropy",
          "blocks": [
            {
              "kind": "wb",
              "body": "Aging (senescence) persists despite natural selection, which usually removes deleterious traits. Two evolutionary explanations:",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Mutation Accumulation",
                "Antagonistic Pleiotropy"
              ],
              "rows": [
                [
                  "**Core idea**",
                  "Deleterious mutations with late-acting effects accumulate because selection cannot &ldquo;see&rdquo; them (most organisms die of predation/accident before old age)",
                  "Genes that BENEFIT early reproduction may HARM survival later — selection maintains them for early benefits even at the cost of late-life damage"
                ],
                [
                  "**Mechanism**",
                  "Neutral or slightly deleterious late-acting alleles not removed by selection; pile up over generations",
                  "One allele = two effects: + fitness early, − fitness late. Selection favors the net positive early effect."
                ],
                [
                  "**Testable prediction**",
                  "Genes with late-onset effects should be less constrained by selection",
                  "Genes beneficial early in life should also cause problems late in life (if eliminated, would reduce both)"
                ],
                [
                  "**Example**",
                  "Many age-related diseases with no early-life fitness consequence",
                  "High testosterone: boosts mating success early → increases prostate cancer/heart disease risk late"
                ]
              ]
            },
            {
              "kind": "wb",
              "body": "**Antagonistic pleiotropy**: a single gene has beneficial effects early in life (↑ reproductive success) but harmful effects late in life (↑ aging/disease). These early benefits are strongly selected FOR because they increase fitness before reproduction, even though late-life costs are selected AGAINST only weakly (selection weakens with age). **Prediction:** genes that boost early reproduction should accelerate senescence. Classic example: testosterone — boosts early male fitness but increases cancer risk and reduces immune function later.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "**Mutation accumulation vs. antagonistic pleiotropy:** Both explain why selection can't eliminate aging, but via different mechanisms. Mutation accumulation = neutral/deleterious late-acting mutations drift to fixation because selection is weak late in life. Antagonistic pleiotropy = SAME gene has opposing effects at different life stages. The key distinction: antagonistic pleiotropy requires POSITIVE selection for the allele (because early benefit outweighs late cost); mutation accumulation requires only RELAXED selection (no positive pressure needed).",
              "label": "Exam Trap"
            },
            {
              "kind": "svg",
              "viz": "aging-curves",
              "svg": "<span class='svg-title'>Why Natural Selection Can't Eliminate Aging</span><div class='svg-ctrls'><button data-aging='mutation-accum'>Mutation Accumulation</button><button data-aging='antag-pleio'>Antagonistic Pleiotropy</button></div><svg viewBox='0 0 300 200' role='img'><g class='axis'><line x1='36' y1='166' x2='286' y2='166' stroke='#31313a'/><line x1='36' y1='14' x2='36' y2='166' stroke='#31313a'/><text x='160' y='184' fill='#8a8a94' font-size='10' text-anchor='middle'>age →</text><text x='20' y='90' fill='#8a8a94' font-size='10' text-anchor='middle' transform='rotate(-90,20,90)'>value</text><line x1='36' y1='90' x2='286' y2='90' stroke='#26262b' stroke-dasharray='2,3'/><text x='155' y='20' fill='#64646d' font-size='9' text-anchor='middle'>reproduction</text><line x1='128' y1='14' x2='128' y2='166' stroke='#26262b' stroke-dasharray='2,3'/></g><path id='aging-fit' d='' stroke='#f5c542' stroke-width='2.4' fill='none'/><path id='aging-sel' d='' stroke='#f87171' stroke-width='2' fill='none' stroke-dasharray='4,3'/><g font-family='JetBrains Mono,monospace' font-size='10'><rect x='198' y='20' width='10' height='3' fill='#f5c542'/><text x='214' y='24' fill='#b6b6bd'>fitness trajectory</text><rect x='198' y='34' width='10' height='3' fill='#f87171'/><text x='214' y='38' fill='#b6b6bd'>selection strength</text></g></svg><div id='aging-caption' class='svg-sub'></div>",
              "caption": "Selection strength drops with age — both mechanisms exploit this 'shadow' past reproduction."
            }
          ]
        }
      ],
      "group": "Exam 2",
      "cheatsheet": "**Ch 12 · Life History Evolution** — Trade-offs between growth, reproduction, and survival. When to be born. How many babies. How long to live.\n\n**§ 12.1 Life History Trade-offs**\n• Life history = the schedule of an organism's survival, growth, and reproduction across its lifespan.\n• ⚠ Reznick's guppy experiment showed detectable evolutionary change in life history traits in approximately **~30 generations** (not 18, not 10…\n\n**§ 12.2 Aging: Mutation Accumulation & Antagonistic Pleiotropy**\n• Aging (senescence) persists despite natural selection, which usually removes deleterious traits.\n• ⚠ **Mutation accumulation vs."
    },
    {
      "id": "ch_s_ch15",
      "num": "15",
      "title": "Coevolution",
      "tagline": "Species evolving in response to each other — arms races, mimicry, and mutualism.",
      "sections": [
        {
          "id": "s_coevo_basics",
          "num": "15.1",
          "title": "Coevolutionary Arms Races & Geographic Mosaic",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Coevolution** = reciprocal evolutionary change between interacting species. Each species acts as a selective agent on the other. An **arms race** is directional escalation: one species evolves better offense, the other evolves better defense, driving each to ever more extreme traits.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Geographic Mosaic Theory (John Thompson)**: coevolution is not uniform across a species' range. Three components: (1) **Hot spots** — locations where reciprocal selection between species is strong and both adapt to each other. (2) **Cold spots** — locations where one species is absent or selection is asymmetric (only one species adapts). (3) **Gene flow** — alleles move between hot spots and cold spots, causing a geographic mosaic of coevolved and non-coevolved populations. Result: populations of the same two interacting species can be at completely different stages of coevolutionary arms races in different locations.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Taricha newts (Pacific Coast) produce tetrodotoxin (TTX) — one of the most potent neurotoxins known. Garter snakes (Thamnophis sirtalis) have evolved voltage-gated sodium channel mutations that confer TTX resistance. Cost: slower locomotion in resistant snakes. Geography: some populations of snakes are highly resistant (live with toxic newts), others have little resistance (no toxic newts). Classic geographic mosaic.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Coevolution varies across landscapes: **Hotspots** = locations where both species are present and reciprocal selection is intense (e.g., highly toxic newts + highly resistant snakes). **Coldspots** = locations where the interaction is weak or one partner is absent. Gene flow between hotspots and coldspots creates a geographic mosaic of traits.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Arms race = DIRECTIONAL ESCALATION (both species evolve ever more extreme traits over time). Red Queen = FREQUENCY-DEPENDENT CYCLING (common genotypes are exploited; rare genotypes gain advantage; no directional escalation — traits cycle). Both are coevolutionary dynamics but in different directions. Newt-snake = arms race (escalation). Host-parasite common genotype cycling = Red Queen.",
              "label": "&#9888; Trap — Arms Race vs. Red Queen"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Arms Race — Newt TTX Toxicity vs Garter Snake Resistance</span><svg viewBox='0 0 400 220' role='img' aria-label='Coevolutionary escalation'><defs><linearGradient id='ar-newt' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#f87171' stop-opacity='.75'/><stop offset='1' stop-color='#f87171' stop-opacity='.08'/></linearGradient><linearGradient id='ar-snake' x1='0' x2='0' y1='0' y2='1'><stop offset='0' stop-color='#34d399' stop-opacity='.75'/><stop offset='1' stop-color='#34d399' stop-opacity='.08'/></linearGradient></defs><g class='axis'><line x1='40' y1='170' x2='380' y2='170' stroke='#31313a'/><line x1='40' y1='20' x2='40' y2='170' stroke='#31313a'/><text x='210' y='196' fill='#8a8a94' font-size='10' text-anchor='middle'>coevolutionary time →</text><text x='24' y='95' fill='#8a8a94' font-size='10' text-anchor='middle' transform='rotate(-90,24,95)'>trait magnitude</text></g><path d='M 40,160 C 90,155 140,130 190,100 C 240,70 290,45 380,25 L 380,170 L 40,170 Z' fill='url(#ar-newt)' stroke='#f87171' stroke-width='2'/><path d='M 40,165 C 90,160 140,140 190,115 C 240,85 290,55 380,35 L 380,170 L 40,170 Z' fill='url(#ar-snake)' stroke='#34d399' stroke-width='2' stroke-dasharray='4,2'/><g font-family='JetBrains Mono, monospace' font-size='10.5'><rect x='240' y='25' width='10' height='3' fill='#f87171'/><text x='256' y='29' fill='#f87171'>Newt TTX toxicity ↑</text><rect x='240' y='42' width='10' height='3' fill='#34d399'/><text x='256' y='46' fill='#34d399'>Snake resistance ↑</text><g transform='translate(330,150)'><text fill='#9c7c20' font-size='9' text-anchor='middle'>hotspot</text><line x1='-20' y1='-2' x2='20' y2='-2' stroke='#9c7c20' stroke-dasharray='1,2'/></g><g transform='translate(80,150)'><text fill='#64646d' font-size='9' text-anchor='middle'>coldspot</text><line x1='-20' y1='-2' x2='20' y2='-2' stroke='#64646d' stroke-dasharray='1,2'/></g></g><text x='210' y='210' text-anchor='middle' font-size='10' fill='#8a8a94' font-family='JetBrains Mono,monospace'>Directional escalation — both curves climb together across the geographic mosaic</text></svg>",
              "caption": "Escalating arms race — distinct from Red Queen cycling (which oscillates around an average rather than climbing)."
            }
          ]
        },
        {
          "id": "s_mimicry",
          "num": "15.2",
          "title": "Mimicry & Endosymbiosis",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Batesian mimicry:** A palatable (harmless) species mimics an unpalatable (toxic/dangerous) species. The mimic &ldquo;free rides&rdquo; on the model's reputation. Works ONLY when mimics are RARE (if mimics become common, predators learn the signal is unreliable).****\r\n**Müllerian mimicry:** Two or more UNPALATABLE species all converge on the same warning pattern. Both species benefit because predators learn the warning signal faster when it's common. Cooperation in defense. Heliconius butterflies = classic example.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Mitochondria and chloroplasts originated as FREE-LIVING BACTERIA engulfed by ancestral eukaryotic cells (~1.5-2 bya for mitochondria). Evidence: (1) circular DNA like bacteria, (2) double membranes, (3) 70S ribosomes (bacterial type — inhibited by bacterial antibiotics), (4) binary fission (divide like bacteria), (5) phylogeny places them within bacteria. Lynn Margulis proposed the endosymbiotic theory (initially rejected, now well-established).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Batesian: mimic is PALATABLE (harmless), model is UNPALATABLE. Mimic is &ldquo;lying.&rdquo; Works best when mimics are RARE (honest warning signal maintained). Müllerian: BOTH species are unpalatable. BOTH benefit. Works better when COMMON (shared signal learned faster). On exams: &ldquo;harmless species mimics harmful&rdquo; = Batesian. &ldquo;Two harmful species look alike&rdquo; = Müllerian.",
              "label": "&#9888; Trap — Batesian vs. Müllerian Mimicry"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Batesian vs Müllerian Mimicry — Who's Lying, Who Benefits</span><svg viewBox='0 0 520 260' role='img' aria-label='Batesian and Mullerian mimicry'><defs><pattern id='stripe-danger' width='6' height='6' patternUnits='userSpaceOnUse' patternTransform='rotate(45)'><rect width='3' height='6' fill='#f87171'/><rect x='3' width='3' height='6' fill='#f5c542'/></pattern></defs><g font-family='JetBrains Mono, monospace' font-size='10.5' text-anchor='middle'><rect x='10' y='20' width='240' height='230' fill='none' stroke='#31313a' stroke-dasharray='4,2' rx='8'/><text x='130' y='38' fill='#f5c542' font-weight='700' font-size='12'>BATESIAN — mimic lies</text><g transform='translate(65,90)'><ellipse rx='32' ry='22' fill='url(#stripe-danger)' stroke='#f87171' stroke-width='2'/><text y='4' fill='#0a0a0c' font-weight='700'>MODEL</text><text y='42' fill='#f87171' font-weight='700'>TOXIC</text><text y='54' fill='#b6b6bd' font-size='9.5'>coral snake</text></g><g transform='translate(195,90)'><ellipse rx='32' ry='22' fill='url(#stripe-danger)' stroke='#f5c542' stroke-width='2' stroke-dasharray='3,2'/><text y='4' fill='#0a0a0c' font-weight='700'>MIMIC</text><text y='42' fill='#34d399' font-weight='700'>HARMLESS</text><text y='54' fill='#b6b6bd' font-size='9.5'>king snake</text></g><g transform='translate(130,160)'><text fill='#b6b6bd' font-size='9.5'>predator sees stripes → avoids</text><text y='14' fill='#f87171' font-size='9.5'>→ fewer mimics = honest signal</text><text y='28' fill='#34d399' font-size='9.5'>✓ mimic benefits · model unchanged</text><text y='42' fill='#f5c542' font-size='9.5' font-weight='700'>Works only when mimics RARE</text></g><rect x='270' y='20' width='240' height='230' fill='none' stroke='#31313a' stroke-dasharray='4,2' rx='8'/><text x='390' y='38' fill='#f5c542' font-weight='700' font-size='12'>MÜLLERIAN — both honest</text><g transform='translate(325,90)'><ellipse rx='32' ry='22' fill='url(#stripe-danger)' stroke='#f87171' stroke-width='2'/><text y='4' fill='#0a0a0c' font-weight='700'>SPECIES A</text><text y='42' fill='#f87171' font-weight='700'>TOXIC</text><text y='54' fill='#b6b6bd' font-size='9.5'>Heliconius erato</text></g><g transform='translate(455,90)'><ellipse rx='32' ry='22' fill='url(#stripe-danger)' stroke='#f87171' stroke-width='2'/><text y='4' fill='#0a0a0c' font-weight='700'>SPECIES B</text><text y='42' fill='#f87171' font-weight='700'>TOXIC</text><text y='54' fill='#b6b6bd' font-size='9.5'>Heliconius melpomene</text></g><g transform='translate(390,160)'><text fill='#b6b6bd' font-size='9.5'>shared warning signal</text><text y='14' fill='#f87171' font-size='9.5'>→ predators learn faster</text><text y='28' fill='#34d399' font-size='9.5'>✓ BOTH species benefit</text><text y='42' fill='#f5c542' font-size='9.5' font-weight='700'>Better when COMMON</text></g></g></svg>",
              "caption": "Solid border = honest (truly toxic). Dashed border = liar (palatable). Batesian: one lies. Müllerian: both tell the truth."
            }
          ]
        }
      ],
      "group": "Exam 2",
      "cheatsheet": "**Ch 15 · Coevolution** — Species evolving in response to each other — arms races, mimicry, and mutualism.\n\n**§ 15.1 Coevolutionary Arms Races & Geographic Mosaic**\n• **Coevolution** = reciprocal evolutionary change between interacting species.\n• ⚠ Arms race = DIRECTIONAL ESCALATION (both species evolve ever more extreme traits over time).\n\n**§ 15.2 Mimicry & Endosymbiosis**\n• **Batesian mimicry:** A palatable (harmless) species mimics an unpalatable (toxic/dangerous) species.\n• ⚠ Batesian: mimic is PALATABLE (harmless), model is UNPALATABLE."
    },
    {
      "id": "ch_s_ch16",
      "num": "16",
      "title": "Evolution of Social Behavior",
      "tagline": "Cooperation vs. selfishness. Kin selection. The math of altruism.",
      "sections": [
        {
          "id": "s_ess",
          "num": "16.1",
          "title": "Evolutionarily Stable Strategy (ESS)",
          "blocks": [
            {
              "kind": "wb",
              "body": "An **ESS** (Maynard Smith & Price, 1973) is a strategy that, once adopted by most members of a population, CANNOT be invaded by any alternative rare mutant strategy. ESS is a GAME THEORETIC concept: payoffs depend on what others are doing (frequency-dependent). The most stable strategy is not necessarily the one that maximizes individual fitness in isolation.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Two strategies: Hawk (escalate fight until injury) and Dove (display, retreat if opponent escalates). If resource V > injury cost C: pure Hawk ESS (aggression pays). If V < C: MIXED ESS (H frequency = V/C; no pure strategy is stable). At ESS frequency, both strategies have equal fitness. **Side-blotched lizards**: Rock-Paper-Scissors ESS with 3 male throat-color strategies (orange dominates blue, blue dominates yellow, yellow dominates orange).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "An ESS is the strategy that RESISTS INVASION by mutants — not necessarily the strategy with highest absolute fitness for every individual. The mixed Hawk-Dove ESS has both strategies with EQUAL fitness at equilibrium (otherwise one would increase). If you understand that ESS fitness is frequency-dependent (payoff depends on what others play), you understand why no single strategy dominates in mixed ESS scenarios.",
              "label": "&#9888; Trap — ESS ≠ Optimal for Every Individual"
            },
            {
              "kind": "wb",
              "body": "Uta stansburiana (side-blotched lizard) males have 3 throat colors, each a different reproductive strategy:\r\nMorphStrategyBeatsLoses To\r\n**Orange**Ultra-dominant: controls large territories with many femalesBlue (outcompetes for territory)Yellow (sneakers enter undetected)\r\n**Blue**Mate-guards: forms pair bonds, guards individual femaleYellow (guards against sneakers)Orange (outcompeted territorially)\r\n**Yellow**Sneaker: mimics female, enters territories to mateOrange (undetected entry)Blue (blue males recognize and guard against sneakers)\r\n\r\nThis creates a **frequency-dependent cyclic ESS**: Orange → common → Yellow exploits → Yellow common → Blue exploits → Blue common → Orange exploits → cycle repeats. Population cycles in morph frequencies over years.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Hawk-Dove = stable mixed-strategy equilibrium (fixed proportion simultaneously). Side-blotched lizards = cyclic ESS where morph frequencies OSCILLATE over generations (like evolutionary rock-paper-scissors). Both are ESSs but in different forms. The question \"which ESS predicts cycling?\" = Rock-Paper-Scissors dynamics.",
              "label": "&#9888; Trap — Cyclic ESS vs. Mixed Strategy ESS"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Hawk-Dove Payoff Matrix — Maynard Smith &amp; Price</span><svg viewBox='0 0 360 220' role='img' aria-label='Hawk-Dove payoff matrix'><g font-family='JetBrains Mono, monospace' font-size='11' text-anchor='middle'><text x='180' y='18' fill='#f5c542' font-weight='700'>Opponent</text><text x='125' y='40' fill='#b6b6bd' font-weight='700'>Hawk</text><text x='245' y='40' fill='#b6b6bd' font-weight='700'>Dove</text><text x='50' y='95' fill='#b6b6bd' font-weight='700' transform='rotate(-90,50,95)'>You: Hawk</text><text x='50' y='170' fill='#b6b6bd' font-weight='700' transform='rotate(-90,50,170)'>You: Dove</text><rect x='75' y='50' width='100' height='60' fill='rgba(248,113,113,.15)' stroke='#f87171' stroke-width='1.3' rx='4'/><text x='125' y='78' fill='#f87171' font-weight='700'>½(V − C)</text><text x='125' y='96' fill='#b6b6bd' font-size='9.5'>both escalate</text><rect x='195' y='50' width='100' height='60' fill='rgba(245,197,66,.15)' stroke='#f5c542' stroke-width='1.3' rx='4'/><text x='245' y='78' fill='#f5c542' font-weight='700'>V</text><text x='245' y='96' fill='#b6b6bd' font-size='9.5'>hawk takes all</text><rect x='75' y='120' width='100' height='60' fill='rgba(124,196,255,.15)' stroke='#7cc4ff' stroke-width='1.3' rx='4'/><text x='125' y='148' fill='#7cc4ff' font-weight='700'>0</text><text x='125' y='166' fill='#b6b6bd' font-size='9.5'>dove retreats</text><rect x='195' y='120' width='100' height='60' fill='rgba(52,211,153,.15)' stroke='#34d399' stroke-width='1.3' rx='4'/><text x='245' y='148' fill='#34d399' font-weight='700'>½V</text><text x='245' y='166' fill='#b6b6bd' font-size='9.5'>share, no injury</text><text x='180' y='200' fill='#b6b6bd' font-size='10'>V = resource value · C = injury cost</text><text x='180' y='214' fill='#f5c542' font-size='10' font-weight='700'>If V &lt; C → mixed ESS with p(Hawk) = V/C</text></g></svg>",
              "caption": "When injury cost C exceeds resource value V, neither pure Hawk nor pure Dove is stable — evolution settles at Hawk frequency V/C."
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Cyclic ESS — Uta stansburiana Rock-Paper-Scissors</span><svg viewBox='0 0 360 260' role='img' aria-label='Side-blotched lizard RPS cycle'><defs><marker id='rps-arr' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='9' markerHeight='9' orient='auto'><path d='M0,0 L10,5 L0,10 Z' fill='#f5c542'/></marker></defs><g font-family='JetBrains Mono, monospace' font-size='10.5' text-anchor='middle'><circle cx='180' cy='60' r='38' fill='rgba(249,115,22,.18)' stroke='#f97316' stroke-width='2'/><text x='180' y='54' fill='#f97316' font-weight='700' font-size='13'>ORANGE</text><text x='180' y='68' fill='#b6b6bd' font-size='9'>ultra-dominant</text><text x='180' y='78' fill='#b6b6bd' font-size='9'>big territory</text><circle cx='92' cy='188' r='38' fill='rgba(124,196,255,.18)' stroke='#7cc4ff' stroke-width='2'/><text x='92' y='182' fill='#7cc4ff' font-weight='700' font-size='13'>BLUE</text><text x='92' y='196' fill='#b6b6bd' font-size='9'>mate-guarder</text><text x='92' y='206' fill='#b6b6bd' font-size='9'>monogamous</text><circle cx='268' cy='188' r='38' fill='rgba(245,197,66,.18)' stroke='#f5c542' stroke-width='2'/><text x='268' y='182' fill='#f5c542' font-weight='700' font-size='13'>YELLOW</text><text x='268' y='196' fill='#b6b6bd' font-size='9'>female-mimic</text><text x='268' y='206' fill='#b6b6bd' font-size='9'>sneaker</text><g stroke='#f5c542' stroke-width='2.2' fill='none' marker-end='url(#rps-arr)'><path d='M 208 88 Q 250 140 240 160'/><path d='M 126 168 Q 80 130 148 80'/><path d='M 224 206 Q 180 230 140 206'/></g><g font-size='9.5' fill='#f5c542'><text x='252' y='110'>beats</text><text x='110' y='112'>beats</text><text x='180' y='240'>beats</text></g><text x='180' y='20' fill='#f5c542' font-size='12' font-weight='700'>Orange → Blue → Yellow → Orange...</text></g></svg>",
              "caption": "Three strategies, each beaten by the next — frequencies oscillate over generations instead of settling. Cyclic ESS."
            }
          ]
        },
        {
          "id": "s_altruism",
          "num": "16.2",
          "title": "Kin Selection, Altruism & Hamilton's Rule",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Altruism** (biological) = behavior that REDUCES the actor's direct fitness while INCREASING the recipient's direct fitness. Paradoxical under individual selection. Explained by **kin selection**: altruism can be favored if the INDIRECT fitness gains (through enhanced reproduction of relatives sharing your genes) exceed the direct fitness cost.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Full sibling (diploid): r = 0.5\n\r\n2. Parent to offspring: r = 0.5\n\r\n3. Half-sibling: r = 0.25\n\r\n4. First cousin: r = 0.125\n\r\n5. In HAPLODIPLOIDY (Hymenoptera — bees, wasps, ants): full sisters r = 0.75 (!), brothers r = 0.25, mother r = 0.5",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Total fitness = direct fitness (own reproduction) + indirect fitness (reproduction of relatives, weighted by relatedness). Altruism &ldquo;works&rdquo; genetically because your relatives share your alleles — helping them reproduce propagates copies of your alleles.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "In haplodiploidy: worker bees are related to their FULL SISTERS at r = 0.75. But workers are related to the QUEEN'S SONS at r = 0.25 (not 0.75). Sons are haploid, from unfertilized eggs. Workers share the queen's genome but NOT the father's — they're only related to brothers through the queen (r = 0.5 × 0.5 = 0.25). This is why worker bees prefer raising SISTERS over BROTHERS if they can control sex ratio.",
              "label": "&#9888; Trap — Worker-to-Queen's-Son Relatedness (r = 0.25)"
            },
            {
              "kind": "trap",
              "body": "In Hamilton's Rule rB > C: you discount the BENEFIT by relatedness (how much of the benefit goes to shared alleles). The COST is NOT discounted — you always pay 100% of your own cost. If you incorrectly discounted C by r too, you'd overestimate when altruism should evolve.",
              "label": "&#9888; Trap — Only B is Discounted by r, NOT C"
            },
            {
              "kind": "mn",
              "body": "Haldane quip: &ldquo;**I would lay down my life for 2 brothers or 8 cousins**&rdquo; = 2 × r(0.5) = 1.0 = same as saving yourself. 8 × r(0.125) = 1.0. Break even = worth it; more = favored by kin selection.",
              "label": "Mnemonic — Hamilton's Rule"
            },
            {
              "kind": "wb",
              "body": "**Group selection** = the hypothesis that natural selection acts on GROUPS, not just individuals, favoring groups with more cooperators. Problem: **within any group, selfish individuals have higher fitness than cooperators** → selfishness spreads within groups even if cooperative groups outcompete selfish groups.\r\n\n\r\n1. **Multi-level selection framework**: total selection = within-group selection + between-group selection\n\r\n2. Within-group selection: almost always favors selfish individuals (defectors beat cooperators inside a group)\n\r\n3. Between-group selection: cooperating groups can outcompete all-selfish groups\n\r\n4. **Net result**: group selection is generally WEAK because within-group selection typically overwhelms between-group selection\n\r\n5. **Key insight (Wynne-Edwards critique)**: if animals voluntarily reduce reproduction for the \"good of the group,\" selfish individuals who don't reduce reproduction will quickly spread within the group",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Kin selection (Hamilton's Rule) is NOT group selection. Kin selection works through INDIVIDUAL inclusive fitness — the actor benefits genetically when related individuals reproduce. Group selection requires that whole GROUPS differ in productivity. Kin selection is well-supported; group selection is generally considered weak except in special circumstances (e.g., when groups are composed of close kin).",
              "label": "&#9888; Trap — Group Selection &ne; Kin Selection"
            },
            {
              "kind": "svg",
              "svg": "<span class='svg-title'>Coefficient of Relatedness (r) — Diploid Pedigree</span><svg viewBox='0 0 520 260' role='img' aria-label='Relatedness pedigree'><g font-family='JetBrains Mono, monospace' font-size='10' text-anchor='middle'><g fill='#17171a' stroke='#f5c542' stroke-width='1.5'><rect x='82' y='20' width='30' height='30' rx='3'/><circle cx='175' cy='35' r='16'/><circle cx='355' cy='35' r='16'/><rect x='425' y='20' width='30' height='30' rx='3'/></g><text x='97' y='40' fill='#f5c542'>GF</text><text x='175' y='40' fill='#f5c542'>GM</text><text x='355' y='40' fill='#f5c542'>GM'</text><text x='440' y='40' fill='#f5c542'>GF'</text><g fill='#17171a' stroke='#7cc4ff' stroke-width='1.5'><circle cx='165' cy='120' r='18'/><rect x='253' y='102' width='36' height='36' rx='3'/><circle cx='355' cy='120' r='18'/></g><text x='165' y='125' fill='#7cc4ff'>Mom</text><text x='271' y='125' fill='#7cc4ff'>Dad</text><text x='355' y='125' fill='#7cc4ff'>Aunt</text><g stroke='#64646d' stroke-width='1' fill='none'><line x1='112' y1='35' x2='160' y2='35'/><line x1='136' y1='35' x2='136' y2='80'/><line x1='136' y1='80' x2='165' y2='102'/><line x1='371' y1='35' x2='425' y2='35'/><line x1='398' y1='35' x2='398' y2='80'/><line x1='398' y1='80' x2='355' y2='102'/><line x1='398' y1='80' x2='271' y2='102'/><line x1='183' y1='120' x2='253' y2='120'/><line x1='218' y1='140' x2='218' y2='180'/><line x1='150' y1='180' x2='285' y2='180'/><line x1='150' y1='180' x2='150' y2='210'/><line x1='218' y1='180' x2='218' y2='210'/><line x1='285' y1='180' x2='285' y2='210'/></g><g fill='#17171a' stroke='#34d399' stroke-width='2'><rect x='132' y='210' width='36' height='36' rx='3'/><rect x='200' y='210' width='36' height='36' rx='3'/><circle cx='285' cy='228' r='18'/><circle cx='380' cy='210' r='16'/></g><text x='150' y='232' fill='#34d399' font-weight='700'>YOU</text><text x='218' y='232' fill='#34d399'>Bro</text><text x='285' y='233' fill='#34d399'>Sis</text><text x='380' y='215' fill='#34d399'>Cuz</text><g fill='#f5c542' font-weight='700' font-size='10.5'><text x='96' y='252'>self</text><text x='96' y='262'>r=1</text><text x='218' y='255'>r=0.5</text><text x='285' y='255'>r=0.5</text><text x='380' y='240'>r=0.125</text><text x='165' y='160' font-size='9' fill='#b6b6bd'>r=0.5</text><text x='355' y='160' font-size='9' fill='#b6b6bd'>r=0.25 (half) / aunt 0.25</text></g></g></svg>",
              "caption": "r = probability an allele is identical-by-descent. Halved at each meiosis — parent-offspring 0.5, full sibs 0.5, half-sibs 0.25, first cousins 0.125."
            },
            {
              "kind": "svg",
              "viz": "hamilton",
              "svg": "<span class='svg-title'>Hamilton's Rule — Altruism Evolves When rB &gt; C</span><div class='svg-ctrls' style='gap:16px;align-items:center;flex-wrap:wrap;'><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>r <input data-range='r' type='range' min='0' max='1' step='0.05' value='0.5'> <span data-val='r' style='color:#f5c542;'>0.50</span></label><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>B <input data-range='B' type='range' min='0' max='10' step='0.1' value='4'> <span data-val='B' style='color:#34d399;'>4.0</span></label><label style='font-family:JetBrains Mono,monospace;font-size:11px;color:#b6b6bd;'>C <input data-range='C' type='range' min='0' max='10' step='0.1' value='1'> <span data-val='C' style='color:#f87171;'>1.0</span></label></div><svg viewBox='0 0 360 140' role='img'><rect id='ham-verdict' x='20' y='16' width='320' height='108' fill='rgba(52,211,153,.12)' stroke='#34d399' stroke-width='2' rx='6'/><g font-family='JetBrains Mono, monospace' text-anchor='middle'><text x='180' y='50' font-size='16' fill='#f5c542' font-weight='700'>rB = <tspan data-val='rB'>2.00</tspan>     vs     C = <tspan data-val='C'>1.0</tspan></text><text x='180' y='82' font-size='11' fill='#b6b6bd'>benefit to recipient × relatedness</text><text x='180' y='96' font-size='11' fill='#b6b6bd'>VS cost to self (NEVER discounted by r)</text><text x='180' y='116' font-size='12.5' fill='#34d399' font-weight='700' data-val='verdict'>rB &gt; C ✓ altruism favored</text></g></svg><div class='svg-sub'>Haldane: 2 brothers × r(0.5) = 1.0 OR 8 cousins × r(0.125) = 1.0 → break-even. Worker bee sister: r=0.75 in Hymenoptera = strong kin selection.</div>",
              "caption": "Slide r, B, C — watch when altruism flips from favored (green) to disfavored (red). Remember: only B is multiplied by r, never C."
            }
          ]
        }
      ],
      "group": "Exam 2",
      "cheatsheet": "**Ch 16 · Evolution of Social Behavior** — Cooperation vs. selfishness. Kin selection. The math of altruism.\n\n**§ 16.1 Evolutionarily Stable Strategy (ESS)**\n• An **ESS** (Maynard Smith & Price, 1973) is a strategy that, once adopted by most members of a population, CANNOT be invaded by any alternative rare mutant strategy.\n• ⚠ An ESS is the strategy that RESISTS INVASION by mutants — not necessarily the strategy with highest absolute fitness for every individual.\n\n**§ 16.2 Kin Selection, Altruism & Hamilton's Rule**\n• **Altruism** (biological) = behavior that REDUCES the actor's direct fitness while INCREASING the recipient's direct fitness.\n• ⚠ In haplodiploidy: worker bees are related to their FULL SISTERS at r = 0.75."
    },
    {
      "id": "ch3",
      "num": "3",
      "title": "History of Life",
      "tagline": "4.5 billion years compressed for your exam.",
      "sections": [
        {
          "id": "c31",
          "num": "3.1",
          "title": "Age of the Earth & Radiometric Dating",
          "blocks": [
            {
              "kind": "wb",
              "body": "Earth is ~4.568 billion years old. **Radiometric dating**: measure the ratio of radioactive parent isotope to daughter isotope. Each isotope decays at a fixed rate (half-life) unaffected by temperature, pressure, or chemistry — that invariance makes it a reliable clock.",
              "label": null
            },
            {
              "kind": "yb",
              "body": "Without dates, no timeline. Lord Kelvin said ~20 million years (wrong — ignored radioactive heat). Darwin said billions from sediment rates (roughly right). Modern physics confirmed 4.568 bya.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Radioactive parent decays into daughter at a constant rate\n\r\n2. Measure current parent:daughter ratio in the rock\n\r\n3. Apply known half-life to calculate when rock solidified (reset to 100% parent / 0% daughter)\n\r\n4. Multiple isotope systems can cross-check the same sample",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Parent → Daughter",
                "Half-Life",
                "Best For"
              ],
              "rows": [
                [
                  "Carbon-14 → Nitrogen-14",
                  "5,730 yrs",
                  "Recent organic material (<50,000 yrs)"
                ],
                [
                  "Potassium-40 → Argon-40",
                  "1.3 billion yrs",
                  "Volcanic rocks; hominin fossils (million-year range)"
                ],
                [
                  "Uranium-238 → Lead-206",
                  "4.5 billion yrs",
                  "Ancient rocks (hundreds of millions to billions of years)"
                ],
                [
                  "Rubidium-87 → Strontium-87",
                  "47 billion yrs",
                  "Very ancient formations; solar system age"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "C-14 CANNOT date dinosaur fossils (~66+ mya). After ~250,000 years all C-14 has decayed. Use U-Pb or K-Ar. Robbins loves this.",
              "label": "⚠ Trap — C-14 and Dinosaurs"
            },
            {
              "kind": "rem",
              "body": "Short half-life = use for recent samples. Long half-life = use for ancient samples. Half-life is FIXED, unaffected by environment.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "mn",
              "body": "“**C**ool **K**ids **U**sually **R**ock” = C-14 (recent), K-Ar (medium), U-Pb (old), Rb-Sr (ancient).",
              "label": "Mnemonic"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p002_img1.jpeg",
              "caption": "Radiometric Decay Curve"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p004_img1.jpeg",
              "caption": "Tree of Life — Three Domains"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p004_img2.png",
              "caption": "Photosynthesis Chemical Equation"
            }
          ]
        },
        {
          "id": "c32",
          "num": "3.2",
          "title": "Origin of Life (Abiogenesis)",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Abiogenesis** = life from non-living chemistry. The **prebiotic soup hypothesis**: early Earth's pools/oceans contained organic molecules formed from inorganic chemistry. Energy (lightning, UV, volcanic heat) drove reactions. No O2 in early atmosphere.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **Miller-Urey (1953):** Simulated early atmosphere (CH4, H2, NH3, H2O; NO oxygen) + electric sparks → 20+ amino acids in ~1 week. Building blocks form abiotically.\n\r\n2. **Fox et al. (1977):** Heated amino acids at 120°C → peptide-like structures. Polymerization possible.\n\r\n3. **Murchison meteorite:** Purines, pyrimidines, amino acids in a meteorite — extraterrestrial organics may have seeded early Earth.\n\r\n4. **RNA World Hypothesis:** RNA can BOTH store genetic information AND catalyze reactions (ribozymes). May have been the first self-replicating functional molecule before DNA and proteins took specialized roles.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Produced amino acids — NOT cells, NOT DNA, NOT life. Only proves building blocks can form abiotically.",
              "label": "⚠ Trap — Miller-Urey Scope"
            },
            {
              "kind": "rem",
              "body": "RNA World = RNA did BOTH jobs (info storage + catalysis) before specialization. Ribosomes still use rRNA as catalytic core today — a molecular fossil of this.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p005_img1.jpeg",
              "caption": "Dictyostelium discoideum Life Cycle"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p005_img2.jpeg",
              "caption": "Ediacaran Biota Stratigraphic Distribution Chart"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p006_img1.jpeg",
              "caption": "Cambrian Seafloor Reconstruction — Burgess Shale"
            }
          ]
        },
        {
          "id": "c33",
          "num": "3.3",
          "title": "Early Life Milestones",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Biomarkers** = molecular evidence of life in ancient rocks (carbon isotope ratios, lipids). Earliest ~3.8 bya. **Stromatolites** = layered mounds from microbial biofilms; fossils at 3.45 bya. **LUCA** ~3.5–3.8 bya.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Domain",
                "Key Features",
                "Earliest Evidence"
              ],
              "rows": [
                [
                  "**Bacteria**",
                  "Prokaryote; peptidoglycan wall; 70S ribosomes; circular DNA",
                  "~3.5 bya photosynthetic cyanobacteria; first atmospheric O2"
                ],
                [
                  "**Archaea**",
                  "Prokaryote; unique membrane lipids; extremophiles; distinct biochemistry",
                  "Biologically-produced methane in Australian rocks"
                ],
                [
                  "**Eukarya**",
                  "Nuclear envelope; 80S ribosomes; organelles; ~100x larger than bacteria",
                  "~1.8 bya fossil eukaryotes"
                ]
              ]
            },
            {
              "kind": "wb",
              "body": "Evolved **independently many times** (≥25 origins): plants, animals, fungi, algae, slime molds. NOT a single event. Oldest multicellular eukaryote: red algae ~1.2 bya. Slime molds (Dictyostelium) show how: starved cells aggregate → slug → stalk + spores; some cells sacrifice themselves.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Did NOT evolve once. Convergently in many lineages. Never say \"multicellularity evolved in [one event].\"",
              "label": "⚠ Trap — Multicellularity Origin"
            },
            {
              "kind": "rem",
              "body": "Biomarkers (3.8 bya) → Stromatolites (3.45 bya) → Eukaryotes (1.8 bya) → Multicellular eukaryotes (1.2 bya). Simpler comes first.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p007_img1.png",
              "caption": "Temporal Fenestration in Reptile Skulls — Anapsid, Synapsid, Diapsid"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p009_img1.jpeg",
              "caption": "Miller–Urey Apparatus for Abiotic Synthesis"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p010_img1.png",
              "caption": "Timeline of Early Life on Earth"
            }
          ]
        },
        {
          "id": "c34",
          "num": "3.4",
          "title": "Geologic Timeline",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "Period",
                "Dates (mya)",
                "Key Events for Exam"
              ],
              "rows": [
                [
                  "**Ediacaran**",
                  "575–535",
                  "Earliest definitive animal fossils; soft-bodied multicellular organisms"
                ],
                [
                  "**Cambrian**",
                  "542–488",
                  "Cambrian explosion: arthropods, chordates, trilobites; Burgess Shale 505 mya (93 species)"
                ],
                [
                  "**Ordovician**",
                  "488–444",
                  "Early bony fishes; earliest land plants (475 mya, resemble mosses)"
                ],
                [
                  "**Silurian**",
                  "444–416",
                  "Earliest land animals: millipede fossil 428 mya; invertebrate tracks ~480 mya"
                ],
                [
                  "**Devonian**",
                  "416–359",
                  "**Age of Fishes**; Dunkleosteus (6m); Tiktaalik 375 mya; earliest tetrapods 370 mya; trees 385 mya"
                ],
                [
                  "**Carboniferous**",
                  "359–299",
                  "Age of Amphibians; coal swamps; land vertebrates + plants diversify"
                ],
                [
                  "**Permian**",
                  "299–251",
                  "Synapsid/sauropsid split; END-PERMIAN EXTINCTION (~96% loss — LARGEST mass extinction)"
                ],
                [
                  "**Triassic**",
                  "251–202",
                  "First dinosaurs (230 mya); first mammals; End-Triassic extinction"
                ],
                [
                  "**Jurassic**",
                  "202–145",
                  "Dinosaur diversification; birds within Dinosauria (~150 mya); mammal ancestor 200–180 mya"
                ],
                [
                  "**Cretaceous**",
                  "145–65",
                  "Flowering plants 132 mya; K-T EXTINCTION 66 mya: asteroid; non-avian dinosaurs + ~76% species"
                ],
                [
                  "**Cenozoic**",
                  "65–now",
                  "Mammal radiation; primates 50 mya; apes 20 mya; hominins 7 mya; H. sapiens ~300 kya"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "End-PERMIAN = LARGEST (~96% loss). K-T = most famous (~76% loss, dinosaurs). \"Most severe?\" = Permian. \"Killed non-avian dinosaurs?\" = K-T asteroid.",
              "label": "⚠ Trap — Permian vs K-T Severity"
            },
            {
              "kind": "trap",
              "body": "Birds are avian theropod dinosaurs. Non-avian dinosaurs went extinct at K-T; birds survived. 10,000+ species of dinosaurs alive today as birds.",
              "label": "⚠ Trap — Birds ARE Dinosaurs"
            },
            {
              "kind": "mn",
              "body": "“**Old Salamanders Don't Climb Poorly Traveled Jungle Crags**” = Ordovician, Silurian, Devonian, Carboniferous, Permian, Triassic, Jurassic, Cretaceous",
              "label": "Mnemonic — Periods"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p010_img2.jpeg",
              "caption": "Fossilization Process — Six Steps"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 3 · History of Life** — 4.5 billion years compressed for your exam.\n\n**§ 3.1 Age of the Earth & Radiometric Dating**\n• Earth is ~4.568 billion years old.\n• ⚠ C-14 CANNOT date dinosaur fossils (~66+ mya).\n\n**§ 3.2 Origin of Life (Abiogenesis)**\n• **Abiogenesis** = life from non-living chemistry.\n• ⚠ Produced amino acids — NOT cells, NOT DNA, NOT life.\n\n**§ 3.3 Early Life Milestones**\n• **Biomarkers** = molecular evidence of life in ancient rocks (carbon isotope ratios, lipids).\n• ⚠ Did NOT evolve once.\n\n**§ 3.4 Geologic Timeline**\n• ⚠ End-PERMIAN = LARGEST (~96% loss)."
    },
    {
      "id": "ch4",
      "num": "4",
      "title": "Phylogenetics",
      "tagline": "How to read, build, and USE evolutionary family trees.",
      "sections": [
        {
          "id": "c41",
          "num": "4.1",
          "title": "Tree Components",
          "blocks": [
            {
              "kind": "wb",
              "body": "A **phylogenetic tree** = hypothesis about evolutionary relationships. **Tips** = terminal taxa; **Branches** = lineages through time; **Nodes** = speciation events; **Root** = most recent common ancestor of all taxa shown; **Clade** = node + ALL descendants. Evolution is NOT a ladder — it is a branching bush.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Tip ORDER on a tree does NOT show relatedness. Trace back to the SHARED NODE. Two species sharing a more RECENT common node are more closely related regardless of page position. Rotating branches around a node does NOT change tree meaning.",
              "label": "⚠ Trap — Reading Relatedness"
            },
            {
              "kind": "rem",
              "body": "Relatedness = recency of shared ancestor (which node, not position). Trees are hypotheses — can be revised.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p011_img1.png",
              "caption": "Phylogenetic Tree Anatomy and Terminology"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p012_img1.jpeg",
              "caption": "Darwin's 'I Think' Phylogenetic Sketch — 1837"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p012_img2.jpeg",
              "caption": "Phylogenetic Tree Anatomy — Nodes, Branches, Clades"
            }
          ]
        },
        {
          "id": "c42",
          "num": "4.2",
          "title": "Synapomorphies & Mono/Paraphyletic Groups",
          "blocks": [
            {
              "kind": "wb",
              "body": "A **synapomorphy** = shared DERIVED character that evolved in the immediate ancestor of a clade and was inherited by ALL descendants. Defines a clade. **Cladistics** = building trees using synapomorphies only. Ancestral (plesiomorphic) characters shared by many are NOT informative for relationships within a group.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Group Type",
                "Definition",
                "Valid?",
                "Example"
              ],
              "rows": [
                [
                  "**Monophyletic**",
                  "Common ancestor + ALL descendants",
                  "✓",
                  "Mammals; Aves; Primates"
                ],
                [
                  "**Paraphyletic**",
                  "Common ancestor + SOME but not all descendants",
                  "✗",
                  "\"Reptiles\" without birds; \"Fish\" excluding tetrapods"
                ],
                [
                  "**Polyphyletic**",
                  "Group NOT including common ancestor of all members",
                  "✗",
                  "\"Warm-blooded animals\" (birds + mammals, separate origins)"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "\"Reptiles\" without birds is PARAPHYLETIC. Birds ARE theropod dinosaurs. Crocodilians are more closely related to birds than to lizards. To be monophyletic must include birds. Classic Robbins question.",
              "label": "⚠ Trap — Reptiles are Paraphyletic"
            },
            {
              "kind": "mn",
              "body": "“**MONO = All Kids Come Home. PARA = Some Kids Left. POLY = Different Parents Showed Up.**”",
              "label": "Mnemonic"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p012_img3.jpeg",
              "caption": "Tree Pruning and Clade Collapsing"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img1.jpeg",
              "caption": "Snail Island Evolution — Colonization and Initial Divergence (Panels a–c)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img2.jpeg",
              "caption": "Snail Island Evolution — Colonization, Extinction, and Character Divergence (Panels d–f)"
            }
          ]
        },
        {
          "id": "c43",
          "num": "4.3",
          "title": "Parsimony & Homoplasy",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Parsimony**: prefer the tree requiring FEWEST evolutionary changes. **Homoplasy**: similarity NOT due to common descent. Two types: (1) **Convergent evolution** — same trait independently evolves in separate lineages; (2) **Evolutionary reversal** — derived character reverts to ancestral state. Both create false groupings.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "",
                "Homology",
                "Homoplasy"
              ],
              "rows": [
                [
                  "**Cause**",
                  "Inherited from shared ancestor",
                  "Independent evolution OR reversal"
                ],
                [
                  "**Phylo use**",
                  "✓ Useful — defines clades",
                  "✗ Misleading — false groupings"
                ],
                [
                  "**Example**",
                  "Human arm + whale flipper (same bones)",
                  "Dolphin + shark body shape (different ancestry, same pressure)"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Both are homoplasy. **Convergent** = completely different genetic mechanisms (camera eye in vertebrates vs. octopus). **Parallel** = same genetic mechanism in related lineages (similar HOX changes). Both mislead phylogenies.",
              "label": "⚠ Trap — Convergent vs. Parallel"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img3.jpeg",
              "caption": "Snail Character-State Matrix — Island Evolution (Panel g)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img4.jpeg",
              "caption": "Unrooted Network to Rooted Trees — Root Placement Changes Topology"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img5.jpeg",
              "caption": "Humans Are Not the Endpoint of Evolution — Tree Rotation"
            }
          ]
        },
        {
          "id": "c44",
          "num": "4.4",
          "title": "Exaptation + Case Studies (Tiktaalik, Feathers)",
          "blocks": [
            {
              "kind": "wb",
              "body": "An **exaptation** = trait evolved for function A, later co-opted for function B. Evolution tinkers with existing parts; new functions arise from old structures.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Non-flying theropods had feathers (Velociraptor arm bones show quill nodes)\n\r\n2. Arms too short to fly — feathers had other functions first\n\r\n3. Original: insulation, species recognition, mate attraction, egg incubation\n\r\n4. LATER: feathers co-opted for powered flight in bird lineage = exaptation",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Phylogenetic analysis predicted a fish-tetrapod transitional form in mid-Devonian coastal wetland rocks. Scientists searched northern Canada → found **Tiktaalik roseae** (375 mya): weight-bearing elbows, bending wrist, neck, no bony operculum. Prediction confirmed by fossil = scientific success.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Fish swim bladders are homologous to lungs. Ancestral lung (breathing) was co-opted into a swim bladder (buoyancy) in many fish lineages. Tetrapods kept the lung for breathing.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "FALSE. Feathers evolved in non-flying dinosaurs for insulation/display. Flight came later via co-option. Original function ≠ current function = exaptation.",
              "label": "⚠ Trap — Feathers Did NOT Evolve FOR Flight"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p013_img6.jpeg",
              "caption": "Four Equivalent Representations of the Same Tree"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p014_img1.png",
              "caption": "Full Tree of Life — Circular Radial Phylogeny"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p014_img2.jpeg",
              "caption": "Vertebrate Phylogeny with Synapomorphies"
            }
          ]
        },
        {
          "id": "ch4_figs",
          "num": "",
          "title": "Diagram gallery (from lecture)",
          "blocks": [
            {
              "kind": "figure",
              "src": "/exam3/figures/p015_img1.jpeg",
              "caption": "Mammals as a Monophyletic Group"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p015_img2.jpeg",
              "caption": "Sauropsids/Reptiles as a Monophyletic Clade"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p015_img3.jpeg",
              "caption": "Tetrapoda as a Monophyletic Group"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p015_img4.jpeg",
              "caption": "Vertebrata as a Monophyletic Group"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p015_img5.jpeg",
              "caption": "Tetrapod Phylogeny with Labeled Synapomorphies"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p016_img1.jpeg",
              "caption": "Amniote Phylogeny — Synapsids and Diapsids with Illustrations"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p016_img2.png",
              "caption": "Reptiles Are Paraphyletic — Birds Must Be Included"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p016_img3.png",
              "caption": "Vertebrate Characters Mapped on Phylogeny"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p017_img1.png",
              "caption": "Character-State Matrix — Five Insect Taxa"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p017_img2.png",
              "caption": "Number of Possible Rooted Phylogenetic Trees by Number of Taxa"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p017_img3.jpeg",
              "caption": "Four Competing Parsimony Trees for Carnivore Phylogeny"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p017_img4.png",
              "caption": "Carnivore Phylogeny Character Legend"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p017_img5.png",
              "caption": "Carnivore Trees Showing Evolutionary Reversals"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p018_img1.jpeg",
              "caption": "Human Eye Cross-Section — Inverted Retina with Blind Spot"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p018_img2.jpeg",
              "caption": "Octopus Eye Cross-Section — Non-Inverted Retina, No Blind Spot"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p018_img3.jpeg",
              "caption": "Camera Eye: Two Hypotheses — Homology vs. Convergence"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p019_img1.jpeg",
              "caption": "Cetacean Evolution Phylogeny — Whale Origins 55–0 Ma"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p019_img2.jpeg",
              "caption": "Convergent Body Shape — Shark vs. Killer Whale"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p019_img3.jpeg",
              "caption": "Limb Reduction in Lerista Skinks"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p019_img4.jpeg",
              "caption": "Squamate Limb Reduction Phylogenies — 160+ Species"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p020_img1.jpeg",
              "caption": "Living Coelacanth — Latimeria chalumnae"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p020_img2.jpeg",
              "caption": "Fish Pectoral Fin vs. Coelacanth Lobe Fin — Bone Homology"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p020_img3.jpeg",
              "caption": "Three Extant Lungfish Species"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p021_img1.jpeg",
              "caption": "Fish-to-Tetrapod Transition Timeline — 420–360 Ma"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p021_img2.jpeg",
              "caption": "Tiktaalik Fossil — Key Transitional Fish-Tetrapod"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p022_img1.jpeg",
              "caption": "Forelimb Evolution — Eusthenopteron, Tiktaalik, Acanthostega Compared"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p023_img1.jpeg",
              "caption": "Complete Fish-to-Tetrapod Phylogeny with 8 Character Transitions"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p023_img2.jpeg",
              "caption": "Archaeopteryx Fossil and Reconstruction — ~150 Ma"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p023_img3.jpeg",
              "caption": "Dinosaur-to-Bird Phylogeny with 10+ Synapomorphies"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p023_img4.jpeg",
              "caption": "Dinosaurs Brooded Their Eggs — Evolutionary Continuity with Birds"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p024_img1.jpeg",
              "caption": "Velociraptor Quill Knobs — Evidence of Feathers"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p024_img2.jpeg",
              "caption": "Secretary Bird — Exaptation of Wings for Non-Flight Function"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p024_img3.jpeg",
              "caption": "Fish Swim Bladder — Exaptation Homologous to Tetrapod Lung"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p024_img4.jpeg",
              "caption": "Dissected Fish — Swim Bladder Visible in Body Cavity"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 4 · Phylogenetics** — How to read, build, and USE evolutionary family trees.\n\n**§ 4.1 Tree Components**\n• A **phylogenetic tree** = hypothesis about evolutionary relationships.\n• ⚠ Tip ORDER on a tree does NOT show relatedness.\n\n**§ 4.2 Synapomorphies & Mono/Paraphyletic Groups**\n• A **synapomorphy** = shared DERIVED character that evolved in the immediate ancestor of a clade and was inherited by ALL descendants.\n• ⚠ \"Reptiles\" without birds is PARAPHYLETIC.\n\n**§ 4.3 Parsimony & Homoplasy**\n• **Parsimony**: prefer the tree requiring FEWEST evolutionary changes.\n• ⚠ Both are homoplasy.\n\n**§ 4.4 Exaptation + Case Studies (Tiktaalik, Feathers)**\n• An **exaptation** = trait evolved for function A, later co-opted for function B.\n• ⚠ FALSE."
    },
    {
      "id": "ch13",
      "num": "13",
      "title": "Species Concepts & Reproductive Isolation",
      "tagline": "What is a species — and how do new ones form?",
      "sections": [
        {
          "id": "c131",
          "num": "13.1",
          "title": "The Four Species Concepts",
          "blocks": [
            {
              "kind": "wb",
              "body": "~25 definitions exist. All agree: species are groups sharing common ancestry that are evolutionarily independent — following different trajectories through time.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Concept",
                "Key Criterion",
                "Best For",
                "Fails When"
              ],
              "rows": [
                [
                  "**Biological (BSC)**",
                  "Interbreeding populations, reproductively isolated from others",
                  "Sexual animals; testable gene flow",
                  "Fossils; asexual species; hybridizing species"
                ],
                [
                  "**Morphospecies**",
                  "Measurable morphological differences",
                  "Fossils; field identification",
                  "Phenotypically plastic species; cryptic species"
                ],
                [
                  "**Phylogenetic (PSC, Cracraft)**",
                  "Smallest monophyletic group with defining synapomorphies",
                  "Any reproducing group; evolutionary history",
                  "Requires phylogeny; often over-splits taxa"
                ],
                [
                  "**Ecological (ESC, Van Valen)**",
                  "Species = lineage occupying an adaptive zone (distinct niche); species boundaries maintained by ecological selection, not just reproductive isolation",
                  "Ecologically divergent populations; bacteria and asexual taxa",
                  "Niche boundaries hard to define; overlapping niches in generalist species"
                ],
                [
                  "**General Lineage**",
                  "Metapopulations exchanging alleles frequently enough to be the same evolutionary lineage",
                  "Complex cases; unifies other concepts",
                  "Hard to quantify allele exchange threshold"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Know all three for Robbins' scenario questions: (1) FOSSILS — can't test gene flow; (2) ASEXUAL species — bacteria, archaea; (3) HYBRIDIZING species — fertile hybrids exist.",
              "label": "⚠ Trap — BSC Fails in 3 Scenarios"
            },
            {
              "kind": "mn",
              "body": "“**BSC = Babies Stop Crossing. Morpho = Looks Different. Phylo = Family Tree Says So. General = Gene Exchange Rate.**”",
              "label": "Mnemonic"
            },
            {
              "kind": "hb",
              "body": "**Biological Species Concept (BSC, Mayr):** species = groups that interbreed and are reproductively isolated from others. Works for sexually reproducing species; fails for asexuals, fossils, allopatric populations.****\r\n**Morphospecies Concept:** species = populations distinguishable by morphology. Works on fossils and asexual taxa. Misses cryptic species; over-splits polymorphic species.****\r\n**Phylogenetic Species Concept (PSC, Cracraft):** species = smallest diagnosable clade with a unique synapomorphy. Works for any organism. Tends to over-split (recognizes many more species than BSC).****\r\n**Ecological Species Concept (ESC, Van Valen):** species = lineage occupying a distinct adaptive zone (ecological niche). Species boundaries are maintained by ecological selection, independent of reproductive isolation. Useful for ecologically distinct but interbreeding populations and asexual taxa.",
              "label": null
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p026_img1.jpeg",
              "caption": "Parsimony Analysis with Homoplasy — Character Mapping on Tree"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p026_img2.jpeg",
              "caption": "Trilobite Diversity — Six Species"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p027_img1.jpeg",
              "caption": "Brachiopod Shell Morphology — Scanning Electron Micrographs"
            }
          ]
        },
        {
          "id": "c132",
          "num": "13.2",
          "title": "Reproductive Isolating Mechanisms",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "Type",
                "Mechanism",
                "Example"
              ],
              "rows": [
                [
                  "PREZYGOTIC — Pre-Mating"
                ],
                [
                  "**Habitat Isolation**",
                  "Same area, different microhabitats; populations don't meet",
                  "Hawthorn vs. apple maggot flies (same region, different host plants)"
                ],
                [
                  "**Temporal Isolation**",
                  "Different breeding or flowering times",
                  "Hummingbird-pollinated plants with staggered flowering phenology (Stiles 1977)"
                ],
                [
                  "PREZYGOTIC — Post-Mating, Pre-Fertilization"
                ],
                [
                  "**Behavioral/Mechanical**",
                  "Wrong courtship reduces sperm transfer; incompatible genitalia",
                  "Species-specific insect courtship dances"
                ],
                [
                  "**Gametic Incompatibility**",
                  "Sperm/pollen fails to penetrate egg of another species",
                  "Species-specific proteins on sperm affect attachment to egg"
                ],
                [
                  "POSTZYGOTIC"
                ],
                [
                  "**Hybrid Inviability**",
                  "Hybrid embryos fail to develop; die before reproducing",
                  "Incompatible allele interactions cause developmental failure"
                ],
                [
                  "**Hybrid Sterility**",
                  "Hybrids survive but can't reproduce (meiosis fails)",
                  "Mule: horse (64 chr) × donkey (62 chr) = mule (63 chr); meiosis impossible"
                ],
                [
                  "**Hybrid Breakdown**",
                  "F1 fertile; F2+ progressively less fit",
                  "Some cotton species hybrids"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Mules are healthy and vigorous but CANNOT REPRODUCE — 63 chromosomes can't pair in meiosis. Hybrid STERILITY (postzygotic). Inviability = can't survive. Sterility = survives, can't reproduce. Know the difference.",
              "label": "⚠ Trap — Mule = Sterility NOT Inviability"
            },
            {
              "kind": "rem",
              "body": "Prezygotic = before zygote forms. Postzygotic = after. **Reinforcement** = selection strengthening prezygotic barriers when hybrids have low fitness — prevents wasting gametes. Step 4 of allopatric speciation model.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "hb",
              "body": "**Prezygotic barriers** (prevent zygote formation):**\r\n• Temporal: different breeding seasons (two Rana frog species breed at different times)**\r\n• Behavioral/mate choice: different courtship signals (firefly flash patterns)**\r\n• Mechanical: incompatible reproductive structures (sage flower shapes)**\r\n• Gametic: sperm-egg surface protein incompatibility****\r\n**Postzygotic barriers** (reduce hybrid fitness):**\r\n• Hybrid inviability: hybrid embryo fails to develop normally (certain Drosophila crosses)**\r\n• Hybrid sterility: hybrids viable but infertile (mule = horse × donkey)**\r\n• Hybrid breakdown: F2 generation shows reduced fitness (some rice subspecies crosses)",
              "label": null
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p027_img2.jpeg",
              "caption": "Phenotypic Variance Equation — Genetic vs. Environmental Components"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p028_img1.jpeg",
              "caption": "Biological Species Concept — Gene Flow Defines Species Boundaries"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p029_img1.jpeg",
              "caption": "Biological Species Concept Limitations — Three Problem Cases"
            }
          ]
        },
        {
          "id": "c133",
          "num": "13.3",
          "title": "Allopatric vs. Sympatric Speciation",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "",
                "Allopatric",
                "Sympatric"
              ],
              "rows": [
                [
                  "**Geographic context**",
                  "Populations in DIFFERENT non-overlapping ranges",
                  "New species evolves WITHIN same geographic range"
                ],
                [
                  "**How gene flow stops**",
                  "Physical geographic barrier",
                  "Ecological divergence, resource shifts, polyploidy"
                ],
                [
                  "**Steps**",
                  "1) Barrier forms → 2) Genetic divergence → 3) Reproductive isolation → 4) Reinforcement",
                  "1) Ecological divergence → 2) Assortative mating → 3) Genetic divergence"
                ],
                [
                  "**Geographic mechanism**",
                  "**Dispersal:** organisms move to new area. **Vicariance:** barrier forms splitting existing range.",
                  "None — selection on resource use drives divergence"
                ],
                [
                  "**Classic example**",
                  "Hawaiian crickets (dispersal across volcanic islands)",
                  "Apple maggot fly Rhagoletis (host-plant shift within N. America)"
                ]
              ]
            },
            {
              "kind": "wb",
              "body": "Apple trees introduced ~400 ya. Hawthorn flies shifted to apples ~140 ya. Selection favored earlier emergence timing. Now apple and hawthorn populations genetically diverging — mate on host trees, so host shift = mating isolation. Neither moved. This is **ecological speciation**.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "**Dispersal** = organisms MOVE to new area. **Vicariance** = organisms STAY PUT, BARRIER appears. Hawaiian crickets = dispersal. Panama Isthmus = vicariance. Active vs. passive — the key distinction.",
              "label": "⚠ Trap — Dispersal vs. Vicariance"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p029_img2.jpeg",
              "caption": "Allopatric Speciation — Geographic Barrier Drives Divergence"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p029_img3.jpeg",
              "caption": "Dispersal Biogeography — Colonization of a New Island (Panel a)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p030_img1.jpeg",
              "caption": "Vicariance Biogeography — Barrier Splits an Existing Population (Panel b)"
            }
          ]
        },
        {
          "id": "c133b",
          "num": "13.4",
          "title": "Allopolyploidy (Instant Speciation) & Haldane's Rule",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Allopolyploidy** = hybridization between two different species + whole-genome duplication. The offspring has a complete chromosome set from BOTH parents. Because it has a different ploidy level from either parent species, it is **immediately reproductively isolated** from both parents — speciation in ONE GENERATION (instant speciation). Most common in plants; ~50% of all flowering plants have polyploid ancestry.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Species A (2n=14) × Species B (2n=14) → hybrid offspring (n=7 from each parent = 14 total, BUT chromosomes can't pair in meiosis — hybrid is sterile)\n\r\n2. Accidental genome duplication (e.g., failure of cell division) → allotetraploid offspring (2n=28: two complete sets from A + two from B)\n\r\n3. Chromosomes CAN now pair properly in meiosis (each set has a match)\n\r\n4. Allotetraploid is fertile but reproductively isolated from both parents — crossing back = ploidy mismatch → sterile offspring\n\r\n5. New species formed in a single generation with no geographic isolation required",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Tragopogon** (goatsbeard): two allopolyploid species formed in the Pacific Northwest within the last ~80 years from European species introduced to North America. Directly observed forming in real time. **Bread wheat** (Triticum aestivum): hexaploid (6n=42) from three ancestral grass species (AA + BB + DD) via two sequential allopolyploidy events over ~8,000 years.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "When hybrid offspring of one sex are inviable or sterile, it is more often the **heterogametic sex** (XY males in mammals/flies, ZW females in birds/butterflies). WHY: recessive incompatibility alleles on the X chromosome are **exposed (hemizygous)** in XY males (only one X) but **masked** in XX females (two X copies, second can compensate). XY males have no backup copy, so incompatibilities hit them first.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "**Allopolyploidy** = hybridization between TWO DIFFERENT SPECIES + genome duplication. **Autopolyploidy** = genome duplication within ONE species (extra copies of same genome). Allopolyploidy is far more common and evolutionarily important because the different chromosome sets pair properly in meiosis. ALLO = two different parents. AUTO = copies of yourself.",
              "label": "⚠ Trap — Allopolyploidy vs Autopolyploidy"
            },
            {
              "kind": "trap",
              "body": "NO. Allopolyploidy creates reproductive isolation IN A SINGLE GENERATION without any geographic separation. It is one of the few routes to sympatric speciation that is well-documented and uncontroversial. Plants are particularly prone to this because they tolerate polyploidy better than animals.",
              "label": "⚠ Trap — Allopolyploidy Requires Geographic Isolation?"
            },
            {
              "kind": "rem",
              "body": "Allopolyploidy = fastest possible speciation: 1 generation, no geography needed, immediately isolated from parents. ~50% of flowering plants have polyploid ancestry. Mule sterility is the FAILURE of this — no duplication step, so you get sterile hybrid not new species.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p030_img2.jpeg",
              "caption": "Reproductive Isolation Taxonomy — Complete Flowchart"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p031_img1.jpeg",
              "caption": "Hawthorn and Blueberry Fruit Flies — Host Race Divergence"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p031_img2.jpeg",
              "caption": "Flowering Phenology and Temporal Isolation — Stiles 1977"
            }
          ]
        },
        {
          "id": "ch13_figs",
          "num": "",
          "title": "Diagram gallery (from lecture)",
          "blocks": [
            {
              "kind": "figure",
              "src": "/exam3/figures/p031_img3.jpeg",
              "caption": "Hummingbird-Pollinated Red Tubular Flower — Temporal Isolation"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p031_img4.jpeg",
              "caption": "Behavioral Isolation — Mate Recognition Failure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p032_img1.jpeg",
              "caption": "Mule — Hybrid Sterility from Chromosomal Incompatibility"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p032_img2.jpeg",
              "caption": "Apple Maggot Fly Rhagoletis pomonella — Two Host Plants"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p033_img1.jpeg",
              "caption": "Rhagoletis Sympatric Speciation — Phenological Divergence and Phylogeny"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p033_img2.jpeg",
              "caption": "Allopatric Speciation Four-Step Model"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p034_img1.jpeg",
              "caption": "Dispersal Biogeography — Island Colonization Sequence (Panel a, repeated)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p034_img2.jpeg",
              "caption": "Predicted Ladder Phylogeny from Stepwise Island Colonization"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p034_img3.jpeg",
              "caption": "Hawaiian Islands Geological Ages Map"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p035_img1.jpeg",
              "caption": "Hawaiian Cricket Laupala — Dispersal Map"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p036_img1.jpeg",
              "caption": "Laupala Cricket Time-Calibrated Phylogeny — 30+ Species by Island"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p036_img2.jpeg",
              "caption": "Laupala Cricket Phylogeny with QTL Data for Song and Preference"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 13 · Species Concepts & Reproductive Isolation** — What is a species — and how do new ones form?\n\n**§ 13.1 The Four Species Concepts**\n• ~25 definitions exist.\n• ⚠ Know all three for Robbins' scenario questions: (1) FOSSILS — can't test gene flow; (2) ASEXUAL species — bacteria, archaea; (3) HYBRIDIZING…\n\n**§ 13.2 Reproductive Isolating Mechanisms**\n• ⚠ Mules are healthy and vigorous but CANNOT REPRODUCE — 63 chromosomes can't pair in meiosis.\n\n**§ 13.3 Allopatric vs. Sympatric Speciation**\n• Apple trees introduced ~400 ya.\n• ⚠ **Dispersal** = organisms MOVE to new area.\n\n**§ 13.4 Allopolyploidy (Instant Speciation) & Haldane's Rule**\n• **Allopolyploidy** = hybridization between two different species + whole-genome duplication.\n• ⚠ **Allopolyploidy** = hybridization between TWO DIFFERENT SPECIES + genome duplication."
    },
    {
      "id": "ch14",
      "num": "14",
      "title": "Biogeography, Speciation & Extinction",
      "tagline": "Diversity through time and space.",
      "sections": [
        {
          "id": "c141",
          "num": "14.1",
          "title": "Dispersal vs. Vicariance (Biogeography)",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Biogeography** = study of spatial and temporal distribution of biodiversity. Initiated by Darwin and Wallace. Two processes explain why related species end up in different places: **dispersal** (organisms move) and **vicariance** (barrier forms). **Phylogeography** = linking phylogenetic relationships to geography to reconstruct historical events.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Oldest fossils: China 150 mya → dispersed to N. America ~120 mya → S. America → crossed Antarctica (when warm) → arrived in Australia ~55 mya. Australia drifted into isolation for 40+ million years with no placental mammals (until bats/rats arrived ~15 mya). Result: Australian marsupials radiated convergently into ecological roles paralleling placentals elsewhere — marsupial mole, marsupial wolf, etc.",
              "label": null
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p038_img1.jpeg",
              "caption": "Global Vascular Plant Diversity Map"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p039_img1.jpeg",
              "caption": "Continental Positions at 150 Million Years Ago — Late Jurassic"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p040_img1.jpeg",
              "caption": "Plate Tectonics Through Time — Five Globe Series"
            }
          ]
        },
        {
          "id": "c142",
          "num": "14.2",
          "title": "Standing Diversity Math",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Standing diversity (D)** = number of species present at a given time. **λ** = origination rate (species/my). **μ** = extinction rate (species/my). **Turnover** = total originations + extinctions.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **D&sub2 = D&sub1 + originations − extinctions**\n\r\n2. At global scale: immigration and emigration cancel out — exclude them\n\r\n3. If λ > μ: diversity increases. If μ > λ: decreases. If λ ≈ μ: stable diversity + turnover\n\r\n4. Worked example (lecture): Start 24 sp. Stage B: +10, -6 = 28. Stage C: +8, -12 = 24.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "At GLOBAL scale: D&sub2 = D&sub1 + originations − extinctions ONLY. Immigration/emigration cancel globally. At LOCAL scale they matter. Robbins tests the global formula as fill-in-the-blank.",
              "label": "⚠ Trap — Global vs. Local Scale"
            },
            {
              "kind": "mn",
              "body": "“**Diversity = Species Births minus Species Deaths**” at global scale. λ = birth rate of species. μ = death rate of species.",
              "label": "Mnemonic"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p041_img1.jpeg",
              "caption": "Vicariance Speciation Model — Continent Splitting Populations"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p042_img1.png",
              "caption": "World Tectonic Plate Map"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p043_img1.jpeg",
              "caption": "Marsupial Global Distribution and Diversity"
            }
          ]
        },
        {
          "id": "c143",
          "num": "14.3",
          "title": "Adaptive Radiation",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Adaptive radiation** = λ greatly exceeds μ → rapid diversification into many ecological roles. Triggers: new habitat with no competitors, **key innovation** opening new resource space, or mass extinction removing competitors.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Example",
                "Trigger"
              ],
              "rows": [
                [
                  "Hawaiian honeycreepers (>50 sp)",
                  "Colonization of Hawaii ~5 mya; new island; no competitors"
                ],
                [
                  "African cichlids (~500 sp, Lake Victoria)",
                  "Colonization of Great Lakes; no competitors; jaw diversity"
                ],
                [
                  "Cenozoic mammals",
                  "K-T extinction freed niches monopolized by dinosaurs for 160M years"
                ],
                [
                  "Cretaceous angiosperms",
                  "Key innovation: flowers → coevolution with insect pollinators"
                ],
                [
                  "Eleutherodactylus frogs (>400 sp)",
                  "Key innovation: direct development on land, skips tadpole, freed from aquatic larval competition"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Key innovation = NOT \"the organism got smarter.\" It is a specific adaptation that grants ACCESS TO previously unavailable habitats or resources by removing a constraint. Eleutherodactylus key = bypasses aquatic larval competition. The removed constraint + available niche = key innovation.",
              "label": "⚠ Trap — Key Innovation Definition"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p044_img1.jpeg",
              "caption": "Marsupial Phylogeny — South American and Australian Lineages"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p044_img2.jpeg",
              "caption": "Marsupial Area Phylogeny — North America, South America, Antarctica, Australia"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p044_img3.jpeg",
              "caption": "Marsupial Origin — Late Jurassic to Early Cretaceous (150–120 Ma)"
            }
          ]
        },
        {
          "id": "c144",
          "num": "14.4",
          "title": "Mass Extinctions: The Big 5 + 6th",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "Event",
                "Date",
                "Loss",
                "Primary Cause"
              ],
              "rows": [
                [
                  "**End-Ordovician**",
                  "444 mya",
                  "~86%",
                  "Glacial episodes; atmospheric + ocean chemistry; global cooling"
                ],
                [
                  "**Late Devonian**",
                  "375–359 mya",
                  "~75%",
                  "Multiple pulses; CO&sub2 drop; oceanic anoxia"
                ],
                [
                  "**End-Permian \"Great Dying\"**",
                  "252 mya",
                  "**~96%**",
                  "Siberian Traps volcanism → CO&sub2 spike + global warming + ocean acidification + anoxia"
                ],
                [
                  "**End-Triassic**",
                  "202 mya",
                  "~80%",
                  "Elevated CO&sub2; ocean calcification; volcanism"
                ],
                [
                  "**K-T / K-Pg**",
                  "66 mya",
                  "~76%",
                  "Chicxulub asteroid + CO&sub2 → global climate disruption; non-avian dinosaurs + ~76% species"
                ],
                [
                  "**6th (ongoing)**",
                  "Now",
                  "100–1000× background",
                  "Humans: habitat destruction, invasive species, climate change, overexploitation"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "End-PERMIAN = BIGGEST (~96% loss). K-T = MOST FAMOUS (~76% loss, dinosaurs). \"Most severe?\" = Permian. \"Killed non-avian dinosaurs?\" = K-T. Do not confuse them.",
              "label": "⚠ Trap — Biggest vs. Most Famous"
            },
            {
              "kind": "mn",
              "body": "“**Old Dogs Play Tennis Carefully**” = Ordovician, Devonian, Permian, Triassic, Cretaceous. Permian = WORST. Cretaceous = most famous.",
              "label": "Mnemonic — Big 5 Order"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p045_img1.jpeg",
              "caption": "Marsupial Dispersal to Australia — Late Cretaceous to Paleogene (70–55 Ma)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p045_img2.jpeg",
              "caption": "Marsupial Extinctions in the Paleogene (40–25 Ma)"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p045_img3.jpeg",
              "caption": "Great American Biotic Interchange — Pliocene (3 Ma)"
            }
          ]
        },
        {
          "id": "c145",
          "num": "14.5",
          "title": "Island Biogeography (MacArthur & Wilson 1967)",
          "blocks": [
            {
              "kind": "wb",
              "body": "Island species richness reflects a **dynamic equilibrium** between immigration (adds species) and extinction (removes species). At equilibrium immigration rate = extinction rate = stable species number. But species COMPOSITION keeps changing (turnover).",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Larger islands → more species (more niches; lower extinction rate)\n\r\n2. Islands closer to mainland → more species (higher immigration rate)\n\r\n3. Large + near = most species. Small + far = fewest.\n\r\n4. Equilibrium number is STABLE; species IDENTITY still turns over\n\r\n5. Applies to any isolated habitat: forest fragments, mountaintops, nature reserves",
              "label": null
            },
            {
              "kind": "trap",
              "body": "At equilibrium the NUMBER is stable but species COMPOSITION changes continuously through turnover. Equilibrium ≠ same species stay forever.",
              "label": "⚠ Trap — Equilibrium = Same Number NOT Same Species"
            },
            {
              "kind": "rem",
              "body": "Island biogeography is foundational for conservation — habitat fragments behave like islands. Larger + more connected reserves = more species preserved.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p046_img1.jpeg",
              "caption": "Australia in Isolation — Over 40 Million Years of Independent Evolution"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p047_img1.jpeg",
              "caption": "Convergent Evolution Table — Placental Mammals vs. Australian Marsupials"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p048_img1.png",
              "caption": "Species Diversity Equation — Origination, Extinction, Immigration, Emigration"
            }
          ]
        },
        {
          "id": "c145b",
          "num": "14.6",
          "title": "Wallace Line, Conservation Genetics & 50/500 Rule",
          "blocks": [
            {
              "kind": "wb",
              "body": "A sharp biogeographic boundary running through the Malay Archipelago (between Bali and Lombok; between Borneo and Sulawesi). **West of line**: Asian fauna (primates, tigers, elephants). **East of line**: Australasian fauna (marsupials, cockatoos). The line marks the edge of the continental shelves of Asia and Australia. Even during ice age low sea levels, a deep water channel remained — preventing most organisms from crossing. Discovered by Alfred Russel Wallace in 1859. Classic example of vicariance creating biogeographic patterns.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Minimum viable population size guideline: (1) **Ne ≥ 50** in the short term to prevent rapid inbreeding depression (limits inbreeding rate to ~1% per generation); (2) **Ne ≥ 500** in the long term to maintain sufficient genetic variation for adaptive evolution. **Ne** (effective population size) is always smaller than N (census population) due to unequal sex ratios, variance in reproductive success, and population fluctuations. Some scientists suggest 100/1000 as more realistic.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Inbreeding increases homozygosity. Mechanisms of harm: (1) deleterious recessive alleles normally masked in heterozygotes become expressed in homozygotes; (2) loss of heterozygote advantage (e.g., MHC immune genes where heterozygotes recognize more pathogens). Classic example: **cheetahs** have so little genetic diversity that skin grafts between unrelated individuals are accepted without immune rejection (normally rejected due to MHC diversity). Result: ~70% abnormal sperm, high disease susceptibility.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "A third speciation mode (between allopatric and sympatric). Populations have PARTIAL geographic separation — they meet along a narrow contact zone where some gene flow occurs. Strong selection gradients on each side can overcome gene flow, driving divergence. If assortative mating evolves in the contact zone, full speciation can result. Less common than allopatric; harder to document than sympatric.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Effective population size (Ne) is ALWAYS smaller than census population (N). Ne reflects the number of breeding individuals that contribute equally to the next generation. Most real populations have Ne much smaller than N due to unequal reproductive success, sex ratio imbalances, and population bottlenecks. Conservation policy targets Ne, not N.",
              "label": "⚠ Trap — Ne vs. N"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p049_img1.png",
              "caption": "Fossil Range Chart — Species Through Geological Stages A–D"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p049_img2.png",
              "caption": "Origination and Extinction Rate Calculations"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p050_img1.png",
              "caption": "Standing Diversity Calculation — Worked Examples Through Stages"
            }
          ]
        },
        {
          "id": "ch14_figs",
          "num": "",
          "title": "Diagram gallery (from lecture)",
          "blocks": [
            {
              "kind": "figure",
              "src": "/exam3/figures/p050_img2.png",
              "caption": "What Happens When Origination Rate Exceeds Extinction Rate — Beetle Diversity"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p051_img1.jpeg",
              "caption": "Dinosaur Origination and Extinction — High Turnover Rate"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p051_img2.jpeg",
              "caption": "Extinction Tracks Origination Rates — Four Mammal Clades"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p052_img1.jpeg",
              "caption": "Darwin's Finches Adaptive Radiation — 13+ Galápagos Species"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p053_img1.jpeg",
              "caption": "Hawaiian Honeycreeper Adaptive Radiation"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p054_img1.png",
              "caption": "Adaptive Radiation Summary Table — Four Major Radiations"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p054_img2.jpeg",
              "caption": "Cichlid Adaptive Radiation — Convergent Evolution in African Lakes"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p055_img1.png",
              "caption": "Background Extinction vs. Mass Extinction — Definition and Contrast"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p055_img2.jpeg",
              "caption": "Big Five Mass Extinctions — Extinction Rate Scatter Plot"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p056_img1.png",
              "caption": "Big Five Mass Extinctions — Species Loss Percentages and Causes"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p057_img1.jpeg",
              "caption": "Siberian Traps and the Permian Mass Extinction — Science Article"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p058_img1.jpeg",
              "caption": "Sixth Mass Extinction — Current Vertebrate Extinction Rates vs. Big Five"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p058_img2.jpeg",
              "caption": "Early Human-Induced Extinctions — Three Case Studies"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p059_img1.jpeg",
              "caption": "Three Documented Recent Extinctions — Passenger Pigeon, Gastric Brooding Frog, Macounia Moss"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 14 · Biogeography, Speciation & Extinction** — Diversity through time and space.\n\n**§ 14.1 Dispersal vs. Vicariance (Biogeography)**\n• **Biogeography** = study of spatial and temporal distribution of biodiversity.\n\n**§ 14.2 Standing Diversity Math**\n• **Standing diversity (D)** = number of species present at a given time.\n• ⚠ At GLOBAL scale: D&sub2 = D&sub1 + originations − extinctions ONLY.\n\n**§ 14.3 Adaptive Radiation**\n• **Adaptive radiation** = λ greatly exceeds μ → rapid diversification into many ecological roles.\n• ⚠ Key innovation = NOT \"the organism got smarter.\" It is a specific adaptation that grants ACCESS TO previously unavailable habitats or resour…\n\n**§ 14.4 Mass Extinctions: The Big 5 + 6th**\n• ⚠ End-PERMIAN = BIGGEST (~96% loss).\n\n**§ 14.5 Island Biogeography (MacArthur & Wilson 1967)**\n• Island species richness reflects a **dynamic equilibrium** between immigration (adds species) and extinction (removes species).\n• ⚠ At equilibrium the NUMBER is stable but species COMPOSITION changes continuously through turnover.\n\n**§ 14.6 Wallace Line, Conservation Genetics & 50/500 Rule**\n• A sharp biogeographic boundary running through the Malay Archipelago (between Bali and Lombok; between Borneo and Sulawesi).\n• ⚠ Effective population size (Ne) is ALWAYS smaller than census population (N)."
    },
    {
      "id": "ch8",
      "num": "8",
      "title": "Humans as a Selective Force",
      "tagline": "Evolution happening right now — because of us.",
      "sections": [
        {
          "id": "c81",
          "num": "8.1",
          "title": "Humans as Selective Agents",
          "blocks": [
            {
              "kind": "wb",
              "body": "Humans impose intense, consistent, directional selection on other species through hunting, medicine, agriculture, and habitat change. Because selection is strong and repeatable, evolution can be tracked in real time — years to decades, not millions of years.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Human Activity",
                "Selection Pressure",
                "Evolutionary Response"
              ],
              "rows": [
                [
                  "**Trophy hunting**",
                  "Removes individuals with largest heritable traits (horns, tusks, body size)",
                  "Populations evolve smaller traits; African elephants evolving tusklessness"
                ],
                [
                  "**Antibiotic use**",
                  "Kills susceptible bacteria; pre-existing resistant variants survive",
                  "Spread of resistance alleles; MRSA, drug-resistant TB"
                ],
                [
                  "**Pesticide use**",
                  "Kills susceptible insects; resistant individuals reproduce",
                  "Pesticide resistance in mosquitoes (DDT); Bt resistance in crop pests"
                ],
                [
                  "**Size-selective fishing**",
                  "Removes large fish; small ones escape nets and reproduce",
                  "Atlantic cod: smaller body, earlier maturation evolved over decades"
                ],
                [
                  "**Habitat fragmentation**",
                  "Isolates populations; reduces gene flow; increases drift",
                  "Loss of genetic diversity; inbreeding; local adaptation or extinction"
                ],
                [
                  "**Selective breeding**",
                  "Intentional selection for desired traits",
                  "Dog breeds; high-yield crops (corn from teosinte); dairy cattle"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Antibiotics do NOT cause resistance mutations. Mutations are **random and pre-existing**. Antibiotics KILL susceptibles and SELECT FOR pre-existing resistant variants. \"Bacteria evolved resistance BECAUSE OF antibiotics\" = implies directed mutation = WRONG.",
              "label": "⚠ Trap — Antibiotics Don't Cause Mutations"
            },
            {
              "kind": "rem",
              "body": "Humans are the most powerful selective force on Earth today. Strong selection = fast evolution. Antibiotic resistance: days. Fish body size: decades. We are running an unplanned global evolution experiment.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p062_img1.jpeg",
              "caption": "Humans as intentional agents of selection — domestication overview"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p062_img2.jpeg",
              "caption": "Artificial selection on wild cabbage (Brassica oleracea) — one species, many crops"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p063_img1.jpeg",
              "caption": "Artificial selection on dog breeds — extreme morphological divergence"
            }
          ]
        },
        {
          "id": "c81b",
          "num": "8.2",
          "title": "Specific Human-Driven Evolution Examples",
          "blocks": [
            {
              "kind": "wb",
              "body": "Trophy hunting selectively removes individuals with the LARGEST traits (biggest horns = most desirable trophy). Over 30 years of trophy hunting in Canadian bighorn sheep: average horn size declined approximately 20%. Mechanism: large-horned males killed before they can maximize reproduction → genes for smaller horns increase in frequency. This is directional selection **opposing** natural selection (which favors larger horns for male–male competition). The evolutionary change may be difficult to reverse because the alleles for larger horns have been depleted.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "In Mozambique, decades of intense ivory poaching during the civil war (1977–1992) drove rapid evolution of tusklessness in elephants. Before the war: ~18% of females were naturally tuskless. After: ~33% tuskless in heavily poached populations. Tusklessness is heritable and linked to a dominant allele. Selection coefficient was extremely strong — tusked females were killed. Classic human-imposed directional selection on a heritable trait.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Four main mechanisms: (1) **Target modification** — mutations alter the antibiotic binding site (e.g., ribosome changes block tetracycline); (2) **Enzymatic degradation** — beta-lactamases destroy the beta-lactam ring of penicillin/ampicillin; (3) **Efflux pumps** — membrane proteins actively pump antibiotics OUT of the cell; (4) **Horizontal gene transfer (HGT)** — resistance plasmids passed between bacterial species via conjugation, transformation, or transduction — spreads resistance ACROSS species lines.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Trophy hunting creates selection in the OPPOSITE direction from natural selection. Natural selection favors LARGE horns (male competition for mates). Trophy hunting removes large-horned individuals before they can fully reproduce, favoring SMALL horns. This is one of the clearest demonstrations that humans impose strong, unnatural selection pressures on wild populations.",
              "label": "⚠ Trap — Trophy Hunting Selection Direction"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p070_img1.png",
              "caption": "Housefly insecticide resistance timeline (1940–1975) — 10 insecticides"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p071_img1.png",
              "caption": "Housefly resistance → pest-control failure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p067_img2.png",
              "caption": "Prairie chicken inbreeding — egg hatching success vs allele diversity"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 8 · Humans as a Selective Force** — Evolution happening right now — because of us.\n\n**§ 8.1 Humans as Selective Agents**\n• Humans impose intense, consistent, directional selection on other species through hunting, medicine, agriculture, and habitat change.\n• ⚠ Antibiotics do NOT cause resistance mutations.\n\n**§ 8.2 Specific Human-Driven Evolution Examples**\n• Trophy hunting selectively removes individuals with the LARGEST traits (biggest horns = most desirable trophy).\n• ⚠ Trophy hunting creates selection in the OPPOSITE direction from natural selection."
    },
    {
      "id": "ch17",
      "num": "17",
      "title": "Human Evolution",
      "tagline": "~7 million years from chimp-ancestor to H. sapiens.",
      "sections": [
        {
          "id": "c171",
          "num": "17.1",
          "title": "Humans as Primates",
          "blocks": [
            {
              "kind": "wb",
              "body": "Linnaeus (1758) placed humans in Order Primates based on anatomical similarities: forward-facing eyes, gripping hands with nails, large relative brain. Darwin (1871, Descent of Man) explained why: common ancestry with apes. Molecular phylogenetics unequivocally places humans nested within Primates. Most recent common ancestor of all primates: ~66–69 mya (K-T boundary).",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Human chromosome 2 = fusion of chimp chromosomes 2A + 2B (telomeric sequences in the middle prove fusion — definitive molecular evidence of common descent). ~98.5% DNA similarity with chimpanzees. Coccyx = vestigial tail (homologous to primate tails).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "FALSE. Humans and chimps share a COMMON ANCESTOR ~7 mya. We are SISTER LINEAGES, not ancestor/descendant. Neither is the ancestor of the other. Both have been evolving since the split. Correct statement: \"humans and chimps diverged from a common ancestor ~7 mya.\"",
              "label": "⚠ Trap — \"We Evolved FROM Chimps\""
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide04_img2.png",
              "caption": "Figure — Progression of scientific understanding of human origins: taxonomy (Linnaeus, 1740s), evolutionary theory (Darwin, 1870s), and phylogenomics (Finstermeier, 2013)"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide05_img1.jpg",
              "caption": "Figure 14.29 — Hominoid nomenclature. Phylogeny of primates with hierarchical classification labels: Superfamily Hominoidea → Family Hominidae/Hylobatidae → Subfamily Homininae/Pongidae → Tribe Hominini/Gorillini → Subtribe Hominina/Panina → Genus Homo, Pan, Gorilla, Pongo, gibbon genera."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide06_img1.jpg",
              "caption": "Figure — Map of Africa showing locations of early hominin fossil discoveries, including Chad (Sahelanthropus ~7 mya), Kenya (Orrorin ~6 mya), Ethiopia (Ardipithecus ~4.4 mya), and East African Rift sites"
            }
          ]
        },
        {
          "id": "c172",
          "num": "17.2",
          "title": "Hominin Timeline",
          "blocks": [
            {
              "kind": "table",
              "head": [
                "Species",
                "Time (mya)",
                "Key Features"
              ],
              "rows": [
                [
                  "**Sahelanthropus tchadensis**",
                  "~7 (Chad)",
                  "Earliest potential hominin; small canines; foramen magnum suggests upright posture; brain ~320–380cc"
                ],
                [
                  "**Ardipithecus**",
                  "4.4–5.8",
                  "Facultative biped; forest habitat (NOT savannah); smaller canines than apes"
                ],
                [
                  "**Australopithecus**",
                  "4–1.2",
                  "Obligate bipeds; brain ~450cc (ape-sized); Lucy (Au. afarensis, 3.2 mya); Laetoli footprints (3.5 mya)"
                ],
                [
                  "**Homo habilis**",
                  "2.1–1.5",
                  "First Homo; brain ~700cc; Oldowan stone tools (~2.6 mya)"
                ],
                [
                  "**Homo erectus**",
                  "1.9–0.07",
                  "FIRST hominin out of Africa; brain ~900–1100cc; Acheulean hand axes; first regular fire use; fossils in Java + China"
                ],
                [
                  "**Homo neanderthalensis**",
                  "0.4–0.04",
                  "Europe/W. Asia; brain ~1500cc (≥ H. sapiens); buried dead; Mousterian tools; interbred with H. sapiens; extinct ~40 kya"
                ],
                [
                  "**Homo sapiens**",
                  "0.3–now",
                  "E. Africa origin (~300–315 kya, revised; Jebel Irhoud, Morocco); brain ~1350cc; symbolic thought; language; art; behaviorally modern ~70–100 kya; spread globally"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Neanderthals had brains EQUAL TO or LARGER than modern humans (~1500cc vs ~1350cc average). Bigger brain ≠ survival advantage. Neanderthals went extinct despite larger brains. Brain organization and social behavior matter more than raw volume.",
              "label": "⚠ Trap — Neanderthal Brain Size"
            },
            {
              "kind": "mn",
              "body": "“**Sadly Australians Have Eaten Neanderthal Snacks**” = Sahelanthropus, Ardipithecus, Australopithecus, Habilis, Erectus, Neanderthal, Sapiens. Oldest → most recent.",
              "label": "Mnemonic"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide06_img3.jpg",
              "caption": "Figure — Sahelanthropus tchadensis skull (\"Toumaï\"), ~6–7 million years old, from Chad. Foramen magnum position and facial morphology suggest one of the earliest known hominins."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide08_img2.jpg",
              "caption": "Figure — Comparison of posture and locomotion across primates, illustrating the progression toward upright bipedal gait in the human lineage"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide08_img3.jpg",
              "caption": "Figure — Skeletal series showing bipedal adaptations: Proconsul (quadruped), Hylobates (bipedal when not brachiating), Ardipithecus (facultative biped, ~4.4 mya), Oreopithecus, and Homo (obligate biped). Sahelanthropus skull indicated at Ardipithecus position."
            }
          ]
        },
        {
          "id": "c173",
          "num": "17.3",
          "title": "Bipedalism",
          "blocks": [
            {
              "kind": "wb",
              "body": "Habitual upright locomotion on two legs. Evolved ~6–7 mya. Bipedalism was the FIRST major hominin innovation; large brain expansion came LATER.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. **Foramen magnum position:** humans = bottom center (upright head); apes = rear\n\r\n2. **Pelvis shape:** wide + bowl-shaped in humans; elongated in apes for quadrupedal locomotion\n\r\n3. **Valgus femur angle:** human femur angles inward to knee (feet under center of gravity); ape femur is vertical\n\r\n4. **Laetoli footprints (3.5 mya, Tanzania):** arched foot + forward-pointing big toe = bipedal walking identical to modern humans\n\r\n5. **Lucy's knee joint:** Au. afarensis knee anatomy confirms bipedal biomechanics",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Thermoregulation:** upright posture reduces direct sun exposure; tall body dissipates heat better. **Freeing hands:** frees forelimbs for carrying food, tools, and infants. Both likely contributed.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Bipedalism came with real costs: ~80% of humans have lower back pain (spine retrofitted from horizontal to vertical without redesign); difficult childbirth (narrow bipedal pelvis + large infant head = obstetric dilemma). Evolutionary CONSTRAINTS from modifying an ancestral quadruped design.",
              "label": "⚠ Trap — Bipedalism Trade-offs (Maladaptations)"
            },
            {
              "kind": "rem",
              "body": "BIPEDALISM FIRST (~6–7 mya) → BIG BRAIN LATER. Australopithecus walked fully upright with ~450cc ape-sized brain. Don't say brain size drove bipedalism.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide09_img1.jpg",
              "caption": "Figure — Proximal femur comparison across five taxa. Left to right: Pan troglodytes (blue arrowhead — non-bipedal), Sahelanthropus tchadensis, Orrorin tugenensis, Australopithecus afarensis, Homo sapiens (red arrowheads mark bipedal features). Progressive shift in femoral head orientation and shaft angle tracks the evolution of bipedalism."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide10_img1.jpg",
              "caption": "Figure — Foramen magnum position comparison. In quadrupeds (e.g., chimp), the opening faces rearward; in bipeds (Homo), it faces downward. This shift allows the spine to support the skull vertically without heavy posterior neck musculature."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide10_img2.jpg",
              "caption": "Figure — Additional comparison of foramen magnum position across hominin specimens, demonstrating the diagnostic anatomical shift associated with bipedalism"
            }
          ]
        },
        {
          "id": "c174",
          "num": "17.4",
          "title": "Brain, Tools & Language (FOXP2)",
          "blocks": [
            {
              "kind": "wb",
              "body": "Brain size tripled from ~450cc (Australopithecus) to ~1350cc (H. sapiens). Brain is energetically expensive (~20% of caloric budget). Selection pressures: tool use, social cooperation, language, ecological problem-solving.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Tool Tradition",
                "Date",
                "Hominin",
                "Features"
              ],
              "rows": [
                [
                  "**Oldowan**",
                  "~2.6 mya",
                  "H. habilis",
                  "Simple flaked stones; chopping and cutting"
                ],
                [
                  "**Acheulean**",
                  "1.7 mya–200 kya",
                  "H. erectus",
                  "Hand axes; bifacially worked; symmetric; planning required"
                ],
                [
                  "**Mousterian**",
                  "300–30 kya",
                  "Neanderthals + early H. sapiens",
                  "Prepared core; more diverse toolkit"
                ],
                [
                  "**Upper Paleolithic**",
                  "~45 kya",
                  "Behaviorally modern H. sapiens",
                  "Blades, bone tools, art, ornamentation, long-distance trade"
                ]
              ]
            },
            {
              "kind": "wb",
              "body": "**FOXP2** = transcription factor regulating orofacial fine motor control. Mutations cause severe speech/language disorders. Highly conserved in mammals; human version has 2 unique amino acid changes after chimp split. Functions in mice (ultrasonic vocalizations) and songbirds (vocal learning). **Neanderthals have the human version of FOXP2** — mutations likely predated the Neanderthal/H. sapiens split (~600 kya).",
              "label": null
            },
            {
              "kind": "trap",
              "body": "FOXP2 is necessary but NOT sufficient for language. Functions in non-human animals too. It's a transcription factor for fine orofacial motor control co-opted in hominins for language. Calling it \"the language gene\" is an oversimplification Robbins may penalize.",
              "label": "⚠ Trap — FOXP2 Is NOT \"The Language Gene\""
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide11_img2.jpg",
              "caption": "Figure — Foramen magnum in early hominin specimens, further illustrating the anatomical evidence for bipedalism across the hominin lineage"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide12_img1.jpg",
              "caption": "Figure — Three-way comparison of skulls (top row) and lower limb bones/tibia pairs (bottom row). Left: Pan troglodytes; center: Sahelanthropus tchadensis (dark, crushed fossil); right: Homo sapiens. Differences in skull dome height, prognathism, and limb bone morphology document the ape-to-human transition."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide13_img1.jpg",
              "caption": "Figure — (A) Artistic reconstruction of Australopithecus afarensis in a savanna setting — upright posture with long, ape-like arms. (B) Annotated skeleton with C (climbing) and W (walking) labels on specific anatomical features: C = upwardly oriented shoulder joint, long arms, short legs, long curved toes; W = lumbar curve, large femoral head and neck, sideways-facing hip bone, reinforced knee, large heel bone, partial foot arch."
            }
          ]
        },
        {
          "id": "c175",
          "num": "17.5",
          "title": "Neanderthals, Modern Humans & Out of Africa",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Out of Africa hypothesis:** anatomically modern H. sapiens evolved in Africa (~195 kya) and expanded globally beginning ~70–50 kya, largely replacing other hominin populations but with interbreeding. Svante Pääbo's ancient DNA work (Nobel Prize 2022) provided molecular evidence.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. Neanderthals diverged from H. sapiens lineage ~600–800 kya\n\r\n2. Interbreeding after H. sapiens left Africa → **non-African humans carry ~1–4% Neanderthal DNA**; sub-Saharan Africans carry little to none\n\r\n3. Denisovans (Siberia; known from a finger bone + DNA) also interbred → some Melanesians carry ~5% Denisovan DNA\n\r\n4. Neanderthals extinct ~40 kya — reasons debated: outcompeted, assimilation, disease, climate\n\r\n5. Oldest H. sapiens: Omo Kibish, Ethiopia (~195 kya)",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Multiregional: H. sapiens evolved simultaneously in multiple regions from H. erectus with continuous gene flow. Out of Africa: evolved once in Africa, spread and replaced others (with some interbreeding). Genetic evidence strongly supports Out of Africa. The geographic pattern of Neanderthal DNA (non-Africans only) PROVES it was post-migration interbreeding, not just shared ancestry.",
              "label": "⚠ Trap — Out of Africa vs. Multiregional"
            },
            {
              "kind": "rem",
              "body": "Non-African humans carry ~1–4% Neanderthal DNA. Geographic restriction to non-Africans = proof of post-migration interbreeding. All humans trace to African origins. African populations have greatest genetic diversity.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide14_img5.jpg",
              "caption": "Figure — Comparison of proposed adaptive advantages of bipedalism: fruit collection in forested settings (broad pelvis for stable stretching) vs. thermoregulatory efficiency and locomotor economy in open savanna environments"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide15_img3.jpg",
              "caption": "Figure — (A) Artistic reconstruction of early Homo (likely H. ergaster/erectus) holding a wooden spear in open grassland — upright, long-legged, narrow-waisted. (B) Annotated skeleton labeling adaptations for running (r) and walking (w): balanced head, reduced neck muscles, external nose, narrow waist, enlarged gluteus maximus, enlarged hindlimb joints, long legs, short toes, strong longitudinal arch."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide16_img1.jpg",
              "caption": "Figure — Map of Africa, Europe, and Asia showing the dispersal of Homo erectus. Red arrows trace migration routes with age estimates in millions of years: Africa origin (~1.8 mya), through Dmanisi (~1.7–1.2 mya) to Europe (~0.6–1.1 mya) and to East Asia and Southeast Asia (~1.6–1.1 mya). Blue squares mark fossil localities."
            }
          ]
        },
        {
          "id": "c175b",
          "num": "17.6",
          "title": "Denisovans, Anatomically vs. Behaviorally Modern, Brain Evolution",
          "blocks": [
            {
              "kind": "wb",
              "body": "An archaic hominin group identified primarily through DNA from a finger bone in Denisova Cave, Siberia (2010). Known from very few fossils but extensive genomic data. Diverged from Neanderthals ~400 kya. Interbred with modern humans: **Melanesians/Papua New Guineans carry ~3–6% Denisovan DNA**; some mainland Asian and Indigenous Australian populations also show traces. Key finding: the **EPAS1 gene** (high-altitude adaptation) in Tibetans originated from a Denisovan gene variant. Modern humans acquired a Denisovan adaptation through interbreeding — direct fitness benefit from archaic introgression.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Anatomically modern H. sapiens**: oldest fossils ~195 kya (Omo Kibish, Ethiopia) / ~315 kya revised (Jebel Irhoud, Morocco). Have modern skeletal features (high domed skull, reduced brow ridges, chin).**\r\n**Behaviorally modern H. sapiens**: appear ~70–100 kya. Show symbolic thought, abstract art, personal ornaments (shell beads), long-distance trade networks, composite tools. There was a ~100,000 year gap between anatomical modernity and full behavioral modernity.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Social brain hypothesis:** tracking complex social relationships in large groups favored larger neocortex. **Ecological hypothesis:** environmental problem-solving (foraging, tool use) drove brain expansion. **Cooking hypothesis (Wrangham):** cooking food with fire dramatically increased caloric yield from same raw ingredients → provided energy to support larger, metabolically expensive brains. Cooking may have made brain expansion energetically feasible.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**Major Histocompatibility Complex (MHC)** = immune gene region with extreme polymorphism. Studies show humans prefer mates with DIFFERENT MHC types (detected via body odor — \"sweaty T-shirt\" experiments). Benefit: offspring with diverse MHC can recognize more pathogens. This is one of the few documented cases of genetic mate choice in humans driven by immune gene diversity.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "Anatomically modern H. sapiens (modern skeleton) appeared ~195 kya (or ~315 kya with latest revisions). **Behaviorally** modern humans (art, symbols, long-distance trade) appeared only ~70–100 kya. There was a gap of ~100,000–200,000 years where humans looked like us but didn't yet act like us. Don't conflate these two milestones.",
              "label": "⚠ Trap — Anatomical vs. Behavioral Modernity"
            },
            {
              "kind": "trap",
              "body": "Denisovan DNA is found primarily in **Melanesians/Pacific Islanders** (~3–6%) and some Asian populations — NOT in sub-Saharan Africans or Western Europeans at comparable levels. Compare: Neanderthal DNA is in ALL non-African modern humans (~1–4%). The different distributions reflect different geographic regions where interbreeding occurred.",
              "label": "⚠ Trap — Denisovan DNA Location"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide17_img1.jpg",
              "caption": "Figure — Map illustrating African origin of hominin lineages and dispersal routes out of Africa into Eurasia, highlighting the multiple waves of hominin migration"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide18_img4.jpg",
              "caption": "Figure — Homo heidelbergensis fossil specimen or reconstruction, showing intermediate anatomy between H. erectus and later Homo species. Brain volume ~1200 cc; associated with cooperative hunting using wooden spears."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide19_img4.jpg",
              "caption": "Figure — Full skeleton comparison: Homo neanderthalensis (left, fossilized brown/orange bones) and Homo sapiens (right, pale modern bones). Neanderthal shows broader ribcage, more robust limbs, larger brow ridges, wider nasal aperture, and stockier build; both species are approximately the same height."
            }
          ]
        },
        {
          "id": "ch17_figs",
          "num": "",
          "title": "Diagram gallery (from lecture)",
          "blocks": [
            {
              "kind": "figure",
              "src": "/img/lec19/slide19_img5.jpg",
              "caption": "Figure — Additional evidence related to Neanderthal biology or behavior, including symbolic shell use (colored/drilled shells indicating ornamentation), associated with cognitive complexity comparable to early H. sapiens"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide20_img1.jpg",
              "caption": "Figure — Map illustrating geographic origins: Neanderthals arose in Eurasia (from heidelbergensis that had dispersed there); H. sapiens arose in Africa (from African heidelbergensis population); subsequent H. sapiens dispersal replaced other archaic Homo species globally."
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide21_img3.jpg",
              "caption": "Figure — Homo sapiens fossils from Ethiopia (Herto or Omo Kibish sites), among the oldest known anatomically modern human specimens, dated to 160,000–200,000 years ago"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide21_img4.jpg",
              "caption": "Figure — Diverse stone tool assemblages from early H. sapiens in Africa, illustrating the Middle Stone Age technological complexity and range of tool types associated with behavioral modernity"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide22_img2.jpg",
              "caption": "Figure — Artifacts demonstrating early H. sapiens symbolic behavior and long-distance trade networks: ochre pieces, perforated shells, and engraved items found far from their raw material sources"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide23_img1.jpg",
              "caption": "Figure — World map showing dispersal routes of anatomically modern Homo sapiens from Africa across all continents, with approximate dates for colonization of major regions"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide26_img3.jpg",
              "caption": "Figure — Map showing the migration of H. sapiens out of Africa (~100,000 ya) and geographic overlap with Neanderthals, H. erectus, and other archaic hominin species around 50,000 years ago"
            },
            {
              "kind": "figure",
              "src": "/img/lec19/slide27_img4.png",
              "caption": "Figure — Scatter plot of mean haplotype heterozygosity vs. geographic distance from Addis Ababa, Ethiopia. Each point is a human population colored by region: red = Africa (highest diversity), green = Europe, dark red = Middle East, teal = Central/South Asia, orange = East Asia, dark blue = Oceania, purple = Americas (lowest diversity, ~25,000 km from Addis Ababa). Strong negative linear trend confirms serial founder effects during the out-of-Africa expansion."
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 17 · Human Evolution** — ~7 million years from chimp-ancestor to H. sapiens.\n\n**§ 17.1 Humans as Primates**\n• Linnaeus (1758) placed humans in Order Primates based on anatomical similarities: forward-facing eyes, gripping hands with nails, large relative brain.\n• ⚠ FALSE.\n\n**§ 17.2 Hominin Timeline**\n• ⚠ Neanderthals had brains EQUAL TO or LARGER than modern humans (~1500cc vs ~1350cc average).\n\n**§ 17.3 Bipedalism**\n• Habitual upright locomotion on two legs.\n• ⚠ Bipedalism came with real costs: ~80% of humans have lower back pain (spine retrofitted from horizontal to vertical without redesign); diffi…\n\n**§ 17.4 Brain, Tools & Language (FOXP2)**\n• Brain size tripled from ~450cc (Australopithecus) to ~1350cc (H.\n• ⚠ FOXP2 is necessary but NOT sufficient for language.\n\n**§ 17.5 Neanderthals, Modern Humans & Out of Africa**\n• **Out of Africa hypothesis:** anatomically modern H.\n• ⚠ Multiregional: H.\n\n**§ 17.6 Denisovans, Anatomically vs. Behaviorally Modern, Brain Evolution**\n• An archaic hominin group identified primarily through DNA from a finger bone in Denisova Cave, Siberia (2010).\n• ⚠ Anatomically modern H."
    },
    {
      "id": "ch18",
      "num": "18",
      "title": "Evolutionary Medicine",
      "tagline": "Why aren't we perfectly adapted?",
      "sections": [
        {
          "id": "c181",
          "num": "18.1",
          "title": "Why We Get Sick: 6 Evolutionary Reasons (Nesse 2005)",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Evolutionary medicine** = applying evolutionary biology to understand disease vulnerability. Natural selection maximizes reproductive fitness, NOT health or longevity. Our bodies are modified ancestral structures, not engineered for modern environments.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "#",
                "Reason",
                "Mechanism",
                "Example"
              ],
              "rows": [
                [
                  "1",
                  "**Pathogens evolve faster**",
                  "Short generations + high mutation = outpace host defenses",
                  "HIV ~1 billion descendants/day; new flu strains each season"
                ],
                [
                  "2",
                  "**Selection lags behind environment** (Mismatch)",
                  "Modern environment changed faster than evolution can track",
                  "Obesity: fat storage evolved for feast/famine; now perpetual feast"
                ],
                [
                  "3",
                  "**Trade-offs**",
                  "Selection can't solve some problems without creating others",
                  "Sickle cell: malaria protection vs. disease in homozygotes; narrow pelvis vs. large infant head"
                ],
                [
                  "4",
                  "**Evolutionary history constrains solutions**",
                  "Selection tinkers with existing structures; can't redesign from scratch",
                  "Human eye blind spot; horizontal spine retrofitted to vertical = back pain in 80%"
                ],
                [
                  "5",
                  "**Antagonistic pleiotropy**",
                  "Early reproductive benefits maintained even if costly late in life (selection can't see post-reproductive costs)",
                  "Testosterone: mating success early, prostate cancer/heart disease late"
                ],
                [
                  "6",
                  "**Apparent disease is actually adaptation**",
                  "Some symptoms ARE defenses, not the disease itself",
                  "Fever = kills pathogens by heat; morning sickness = protects fetus during organogenesis"
                ]
              ]
            },
            {
              "kind": "trap",
              "body": "Both explain aging. **Antagonistic pleiotropy** = one allele with BOTH early-life BENEFITS AND late-life costs (e.g., testosterone). Selected for early benefits. **Mutation accumulation** = late-acting deleterious mutations accumulate because selection is weak after reproduction — NO early benefit. Key: does the allele HELP early? Yes = antagonistic pleiotropy.",
              "label": "⚠ Trap — Antagonistic Pleiotropy vs. Mutation Accumulation"
            },
            {
              "kind": "mn",
              "body": "“**Pathogens Laugh, Trade-offs Really Embarrass Anyone**” = Pathogens faster, Lag/mismatch, Trade-offs, Restraints from history, (ant)Agonistic pleiotropy, Apparent disease = adaptation.",
              "label": "Mnemonic"
            },
            {
              "kind": "hb",
              "body": "1. **Defenses** — fever, cough, nausea, pain are ADAPTATIONS not diseases. Suppressing them may worsen outcomes.\n\r\n2. **Infection** — pathogens evolve faster than hosts; arms races and Red Queen dynamics.\n\r\n3. **Novel environments (Mismatch)** — genome adapted to ancestral environment; modern diet/activity → obesity, T2 diabetes, myopia.\n\r\n4. **Genes** — disease alleles may have past benefits (sickle cell = malaria protection; heterozygote advantage preserves them).\n\r\n5. **Design compromises** — evolutionary history constrains anatomy: upright walking + large brain = obstetric dilemma; inverted retina = blind spot.\n\r\n6. **Slow evolutionary change** — selection is slow; new pathogens and environments arise faster than hosts can adapt.",
              "label": null
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p062_img1.jpeg",
              "caption": "Humans as Intentional Agents of Selection — Domestication"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p062_img2.jpeg",
              "caption": "Artificial Selection on Wild Cabbage — Brassica oleracea Domesticates"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p063_img1.jpeg",
              "caption": "Artificial Selection on Dog Breeds — Extreme Morphological Divergence"
            }
          ]
        },
        {
          "id": "c182",
          "num": "18.2",
          "title": "Evolving Pathogens & Virulence",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Virulence** = degree of harm a pathogen causes its host. Pathogens evolve like any organism. Fitness = within-host replication × transmission to new hosts. This creates a fundamental **virulence trade-off**: maximizing replication may reduce transmission by killing the host too fast.",
              "label": null
            },
            {
              "kind": "hb",
              "body": "1. High virulence → more replication → more pathogen output per unit time\n\r\n2. But high virulence → kills/incapacitates host faster → fewer total transmission events\n\r\n3. Selection favors INTERMEDIATE virulence in most cases\n\r\n4. **Exception:** if transmission doesn't need active host (water-borne = cholera), high virulence can be maintained — bedridden/dead hosts still contaminate water supplies",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Bacteria evolve resistance through: (1) point mutations altering drug targets; (2) enzymes degrading antibiotics (beta-lactamases destroy penicillin); (3) efflux pumps expelling drugs from the cell; (4) **horizontal gene transfer (HGT)** — resistance plasmids passed between bacterial species, spreading resistance across phylogenetic lines rapidly.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Introduced to Australia (1950) to kill invasive rabbits. Initially killed 99.8%. Within years: virus evolved LOWER virulence (rabbits survived longer = more mosquito feeding = more transmission). Rabbits evolved resistance. Classic coevolutionary arms race + virulence trade-off in real time.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "WRONG. Virulence evolves toward whatever maximizes pathogen FITNESS. Water-borne pathogens (cholera) can maintain HIGH virulence. Evolution has no direction and no \"niceness.\" Transmission mode is the key determinant.",
              "label": "⚠ Trap — Virulence Always Decreases?"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p063_img2.jpeg",
              "caption": "Artificial Selection on Crops — Wild vs. Domesticated Comparisons"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p064_img1.jpeg",
              "caption": "Maize Domestication Timeline — Archaeological Evidence"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p064_img2.jpeg",
              "caption": "Humans as Unintentional Agents of Evolution — Four Pathways"
            }
          ]
        },
        {
          "id": "c183",
          "num": "18.3",
          "title": "Evolutionary Mismatch & Conserved Gene Networks",
          "blocks": [
            {
              "kind": "wb",
              "body": "**Evolutionary mismatch** = modern diseases arising because our evolved biology is mismatched to current environments. Our bodies evolved under very different ancestral conditions.",
              "label": null
            },
            {
              "kind": "table",
              "head": [
                "Ancestral Environment",
                "Modern Environment",
                "Mismatch Disease"
              ],
              "rows": [
                [
                  "Feast/famine; low calorie density foods",
                  "Constant high-calorie processed foods",
                  "Obesity, type 2 diabetes, metabolic syndrome"
                ],
                [
                  "High physical activity (hunter-gatherer)",
                  "Sedentary lifestyle",
                  "Cardiovascular disease, osteoporosis, depression"
                ],
                [
                  "High parasite/pathogen load",
                  "Very clean environments; reduced pathogen exposure",
                  "Increased autoimmune disease, allergies, asthma (hygiene hypothesis)"
                ],
                [
                  "Horizontal quadruped spine (300M years)",
                  "Bipedal vertical spine (7M year retrofit)",
                  "Lower back pain in ~80% of adults; herniated discs"
                ],
                [
                  "Many pregnancies (fewer ovulatory cycles)",
                  "Fewer pregnancies; more ovulatory cycles per lifetime",
                  "Increased breast/ovarian cancer risk (more lifetime estrogen)"
                ]
              ]
            },
            {
              "kind": "wb",
              "body": "Humans and yeast share a common ancestor >1 billion years ago. Many gene networks are preserved. Marcotte et al. found yeast cell-wall repair gene networks are homologous to human blood vessel growth (angiogenesis) networks. Used well-characterized yeast genetics to identify 8 new human angiogenesis genes — potential cancer drug targets. Ancient evolutionary conservation enables modern medical discovery.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "More cleanliness = MORE autoimmune/allergy disease, NOT less. Immune system evolved calibrated to high parasite load. Without those targets, it attacks harmless antigens (allergies) or self-antigens (autoimmunity). Farm children have significantly LOWER allergy rates. Counterintuitive direction matters on exams.",
              "label": "⚠ Trap — Hygiene Hypothesis Direction"
            },
            {
              "kind": "rem",
              "body": "Mismatch = our evolved biology in an environment it wasn't shaped for. Evolution optimized us for ancestral conditions, not modern ones.",
              "label": "The thing to remember is:"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p065_img1.jpeg",
              "caption": "Habitat Fragmentation — Four-Stage Sequence and Consequences"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p065_img2.png",
              "caption": "Extinction Vortex — Positive Feedback Loop to Extinction"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p066_img1.jpeg",
              "caption": "Greater Prairie Chicken — Population Decline Case Study"
            }
          ]
        },
        {
          "id": "c183b",
          "num": "18.4",
          "title": "Sickle Cell, Cancer as Somatic Evolution & More Trade-offs",
          "blocks": [
            {
              "kind": "wb",
              "body": "Sickle cell is caused by a single nucleotide change in beta-globin: Glutamic acid → Valine (Glu6Val). **HbS/HbS homozygotes**: severe sickle cell anemia (sickling of red blood cells, chronic illness, early death without treatment). **HbA/HbS heterozygotes**: ~25% protection against severe Plasmodium falciparum malaria (parasitized cells sickle and are cleared by spleen; intracellular environment hostile to parasite). In malaria-endemic Africa, HbS maintained at 10–20% frequency — classic **heterozygote advantage (balancing selection via overdominance)**. In non-malarial regions: HbS is purely deleterious (no compensating benefit for heterozygotes).",
              "label": null
            },
            {
              "kind": "wb",
              "body": "Cancer is evolution happening INSIDE the body within a single lifetime. Key parallels: (1) **Heritable variation:** somatic mutations create variant cell lineages; (2) **Natural selection:** cells with mutations allowing faster proliferation, immune evasion, or metastasis are selected; (3) **Adaptation:** tumors evolve resistance to chemotherapy (same mechanism as antibiotic resistance). Why doesn't selection eliminate cancer-causing alleles? Because most cancers hit late in life — **antagonistic pleiotropy**: p53 prevents cancer early (fitness benefit) but its high activity may accelerate aging (cost). Also: high cell division rates in early development are good for growth but increase mutation risk later.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "**p53** = tumor suppressor protein encoded by the TP53 gene. Triggers cell cycle arrest, DNA repair, or apoptosis (programmed cell death) when DNA damage is detected. Early-life benefit: prevents cancer during reproductive years. Late-life cost: excessive p53 activity may deplete stem cells → tissue atrophy, reduced regeneration = accelerated aging. Mouse experiments: enhanced p53 → reduced cancer BUT accelerated aging. Classic antagonistic pleiotropy.",
              "label": null
            },
            {
              "kind": "wb",
              "body": "The human spine evolved from a horizontal quadruped design (~300 million years of evolution) and was co-opted for vertical bipedalism only ~6–7 million years ago. The S-curve compensates for upright posture but creates mechanical vulnerabilities: lumbar disc herniation, vertebral compression fractures, spondylolisthesis, chronic lower back pain. ~80% of humans experience significant back pain. This is evolutionary constraint (Reason #4): selection can only tinker with existing structures, not redesign from scratch.",
              "label": null
            },
            {
              "kind": "trap",
              "body": "In malaria-endemic regions: fitness ranking is **HbA/HbS > HbA/HbA > HbS/HbS**. Heterozygotes have the HIGHEST fitness (heterozygote advantage). In non-malarial regions: HbA/HbA > HbA/HbS > HbS/HbS (sickle cell is just deleterious). The SAME genotype has completely different fitness in different environments. This is why the allele is found at high frequency in sub-Saharan Africa but not in non-malarial populations.",
              "label": "⚠ Trap — Sickle Cell Heterozygote Fitness"
            },
            {
              "kind": "trap",
              "body": "Cancer IS evolution — it is natural selection acting on somatic cell lineages within a body. Cells with mutations enabling faster proliferation, immune evasion, or metastasis are \"selected for\" within the tumor microenvironment. Tumors evolve drug resistance by the same mechanism bacteria evolve antibiotic resistance: pre-existing variation + selection. Chemotherapy resistance = same logic as antibiotic resistance.",
              "label": "⚠ Trap — Cancer Is Evolution"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p067_img1.png",
              "caption": "Jasper County Prairie Chicken Population Crash — 1963–1997"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p067_img2.png",
              "caption": "Prairie Chicken Inbreeding Evidence — Egg Hatching Success and Allele Diversity"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p068_img1.jpeg",
              "caption": "Prairie Chicken Gene Flow Rescue — Recovery After Translocation"
            }
          ]
        },
        {
          "id": "ch18_figs",
          "num": "",
          "title": "Diagram gallery (from lecture)",
          "blocks": [
            {
              "kind": "figure",
              "src": "/exam3/figures/p068_img2.jpeg",
              "caption": "Chicago Tribune Prairie Chicken Article — 2013"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p069_img1.jpeg",
              "caption": "Pollution as an Evolutionary Driver — Forms and Consequences"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p070_img1.png",
              "caption": "Housefly Insecticide Resistance Timeline — 10 Insecticides, 1940–1975"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p071_img1.png",
              "caption": "Housefly Resistance Consequences — Pest Control Failure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p071_img2.jpeg",
              "caption": "Hunting and Overharvesting as Evolutionary Pressure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p072_img1.jpeg",
              "caption": "Bighorn Sheep Horn Length Decline Under Trophy Hunting Pressure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p072_img2.jpeg",
              "caption": "Atlantic Cod Age at Maturity Decline Under Fishing Pressure"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p073_img1.jpeg",
              "caption": "Global Climate Change Sources — Fossil Fuels and Deforestation"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p073_img2.jpeg",
              "caption": "Atmospheric Greenhouse Gas Concentrations — 2000-Year Record"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p074_img1.jpeg",
              "caption": "Natural vs. Enhanced Greenhouse Effect — Two-Panel Diagram"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p074_img2.jpeg",
              "caption": "Global Temperature Anomaly 1880–2000 — 0.74°C Rise"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p075_img1.jpeg",
              "caption": "Species Responses to Climate Change — Four Options"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p075_img2.jpeg",
              "caption": "Climate-Driven Range Shifts — Purple Finch and American Pika"
            },
            {
              "kind": "figure",
              "src": "/exam3/figures/p076_img1.png",
              "caption": "Section 5 Take-Home Points — Anthropogenic Evolution"
            }
          ]
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch 18 · Evolutionary Medicine** — Why aren't we perfectly adapted?\n\n**§ 18.1 Why We Get Sick: 6 Evolutionary Reasons (Nesse 2005)**\n• **Evolutionary medicine** = applying evolutionary biology to understand disease vulnerability.\n• ⚠ Both explain aging.\n\n**§ 18.2 Evolving Pathogens & Virulence**\n• **Virulence** = degree of harm a pathogen causes its host.\n• ⚠ WRONG.\n\n**§ 18.3 Evolutionary Mismatch & Conserved Gene Networks**\n• **Evolutionary mismatch** = modern diseases arising because our evolved biology is mismatched to current environments.\n• ⚠ More cleanliness = MORE autoimmune/allergy disease, NOT less.\n\n**§ 18.4 Sickle Cell, Cancer as Somatic Evolution & More Trade-offs**\n• Sickle cell is caused by a single nucleotide change in beta-globin: Glutamic acid → Valine (Glu6Val).\n• ⚠ In malaria-endemic regions: fitness ranking is **HbA/HbS > HbA/HbA > HbS/HbS**."
    },
    {
      "id": "chmix",
      "num": "★",
      "title": "Mixed Review & Extra Practice",
      "tagline": "Scenario drills across all chapters.",
      "sections": [
        {
          "id": "cbonus",
          "num": "★",
          "title": "Mixed Review — Scenario Questions, Fill-in Anchors & “Which is NOT”",
          "blocks": []
        },
        {
          "id": "cextra1",
          "num": "★",
          "title": "Extra Practice — Ch 3 & Ch 4 Deep Cuts",
          "blocks": []
        },
        {
          "id": "cextra2",
          "num": "★",
          "title": "Extra Practice — Ch 13 & Ch 14 Deep Cuts",
          "blocks": []
        },
        {
          "id": "cextra3",
          "num": "★",
          "title": "Extra Practice — Ch 8, Ch 17, Ch 18 Deep Cuts",
          "blocks": []
        }
      ],
      "group": "Exam 3",
      "cheatsheet": "**Ch ★ · Mixed Review & Extra Practice** — Scenario drills across all chapters.\n\n**§ ★ Mixed Review — Scenario Questions, Fill-in Anchors & “Which is NOT”**\n\n**§ ★ Extra Practice — Ch 3 & Ch 4 Deep Cuts**\n\n**§ ★ Extra Practice — Ch 13 & Ch 14 Deep Cuts**\n\n**§ ★ Extra Practice — Ch 8, Ch 17, Ch 18 Deep Cuts**"
    },
    {
      "id": "ch_visuals",
      "num": "★",
      "title": "Interactive Visuals",
      "group": "Visuals",
      "tagline": "Venn diagrams · Category sorters · Concept pairs",
      "visualsAnchor": true,
      "sections": []
    }
  ],
  "test": [
    {
      "prompt": "A population of mice is culled: larger mice are selectively removed. However, ALL of the size variation in this population is due to differences in food availability (not genetics). What happens to mean body size in the next generation?",
      "choices": [
        "Decreases — selection removes large mice, so the population will evolve smaller size",
        "Stays the same — if h² = 0, R = h² × S = 0; no evolutionary change despite selection",
        "Increases — removing large individuals leaves only small mice to reproduce, increasing size through drift",
        "Decreases, but slowly — it takes many generations for non-heritable selection to cause evolution",
        "Increases — removing large mice relaxes competition for food, allowing the remaining small mice to grow larger via developmental plasticity"
      ],
      "answer": 1,
      "why": "&#9989; **B.** This is the Selection Without Heritability trap. R = h² × S. If all variation is environmental (h² = 0), then R = 0 regardless of selection differential. Selection is occurring (larger mice die) but allele frequencies don't change because the size differences aren't genetic. No evolution. | **Wrong E:** Developmental plasticity from reduced competition is an environmental (non-heritable) effect and cannot change the population mean body size across generations when h² = 0 — any such plastic increase would not be transmitted to the next generation.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "The selection differential (S) in an artificial selection experiment is LARGEST when:",
      "choices": [
        "The breeders chosen are representative of the entire population",
        "Heritability is high for the selected trait",
        "The mean phenotype of selected breeders deviates maximally from the population mean",
        "Population size is large enough to prevent genetic drift",
        "The narrow-sense heritability (h²) is close to 1.0, because S = h² × R by rearranging the breeder's equation"
      ],
      "answer": 2,
      "why": "&#9989; **C.** S = mean of breeders − mean of total population. S is maximized when the BREEDERS are most different (extreme) from the whole population. Heritability (B) determines how much of S translates to R, but S itself is purely about how different breeders are from the population. | **Wrong E:** S is not a function of h²; S is defined solely as the phenotypic difference between selected breeders and the whole population, and the breeder's equation is R = h² × S (not S = h² × R) — confusing these two quantities inverts the causal relationship.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Why does a rare beneficial recessive allele increase in frequency slowly even though natural selection favors it?",
      "choices": [
        "Recessive alleles mutate back to dominant alleles, counteracting selection",
        "When the allele is rare, nearly all copies are in heterozygotes where the recessive phenotype is masked; selection cannot see and act on it",
        "Natural selection is too weak to act on single alleles; only multiple alleles at a locus create detectable selection",
        "Gene flow constantly imports the original allele from other populations",
        "Recessive alleles are inherently less stable than dominant alleles and spontaneously revert to the dominant form at a high rate"
      ],
      "answer": 1,
      "why": "&#9989; **B.** When a recessive allele is rare, nearly all copies occur in Aa heterozygotes — where the dominant allele MASKS the recessive phenotype. Selection can only act on the expressed phenotype. Since Aa looks like AA, selection can't distinguish them and can't favor the recessive allele efficiently. Only when the allele becomes common enough that aa homozygotes appear in significant numbers does selection become fully effective. | **Wrong E:** Recessive alleles are not inherently less stable than dominant alleles and do not spontaneously revert at high rates — mutation rates are similarly low (~10⁻⁸ per base per generation) for all allele classes, and dominance/recessiveness describes phenotypic expression in heterozygotes, not chemical stability of the DNA sequence.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following populations will show the GREATEST evolutionary response to selection (R), satisfying ALL required conditions?",
      "choices": [
        "A population with high heritability (h²=0.9) but zero selection differential (S=0) on the trait",
        "A population with strong selection (S=5 cm) but zero heritability (h²=0) because all variation is environmental",
        "A population with high heritability (h²=0.8), strong selection differential (S=4 cm), and large N (N=5000)",
        "A small bottlenecked population (N=8) with high heritability (h²=0.85) and strong selection (S=3 cm)",
        "A population with moderate heritability (h²=0.4) and moderate S, but fixed alleles at the selected locus (no variation)"
      ],
      "answer": 2,
      "why": "&#9989; **C.** R = h² × S; both h² > 0 AND S > 0 are required, AND large N prevents drift from overriding selection. | A fails: S = 0 → R = 0 regardless of heritability. | B fails: h² = 0 → R = 0 regardless of selection strength. | D fails: N=8 means intense genetic drift likely overwhelms even strong selection (small Ne). | E fails: no variation at the locus means S effectively = 0 and no response is possible.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Natural selection requires which of the following conditions to produce evolutionary change? (I) Phenotypic variation among individuals. (II) Variation must be heritable (genetic). (III) Variation must affect reproductive success. (IV) The population must be large.",
      "choices": [
        "I and III only",
        "I, II, and III only",
        "I, II, III, and IV",
        "II and III only",
        "All four conditions are required"
      ],
      "answer": 1,
      "why": "&#9989; **B. I, II, and III only.** These are Darwin's three classic conditions: variation (I), heritability (II), and differential fitness (III). Verify each: I ✓ — without phenotypic variation there is nothing to select on. II ✓ — without heritability variation is not transmitted and allele frequencies cannot change. III ✓ — if all variants survive/reproduce equally, there is no differential selection. IV is FALSE — natural selection can occur in small populations; large size is not a requirement. (Large N does make selection more efficient relative to drift, but it is not a logical requirement of selection itself.)",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following correctly describes the step-by-step mechanism by which directional selection shifts the mean trait value in one generation?",
      "choices": [
        "Individuals in the upper tail of the phenotypic distribution survive/reproduce at higher rates (S > 0) → the mean of breeders exceeds the population mean → offspring inherit a fraction h² of that differential → mean shifts by R = h² × S",
        "Random genetic drift removes low-fitness alleles → the mean of breeders exceeds the population mean → offspring inherit a fraction h² of that differential → mean shifts by R = h² × S",
        "Individuals in the upper tail survive at higher rates (S > 0) → offspring inherit the FULL selection differential → mean shifts by R = S (heritability does not moderate the response)",
        "Individuals in the upper tail survive at higher rates (S > 0) → the mean of breeders exceeds the population mean → offspring inherit a fraction VP/VA of that differential → mean shifts by R = (VP/VA) × S",
        "Mutation introduces new high-fitness alleles → these spread by selection → mean shifts by R = h² × S, where S is the mutation rate"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the exact mechanism behind the Breeder's Equation R = h² × S. | B fails: the mechanism is selection (non-random), not random genetic drift — drift does not preferentially remove low-fitness alleles in any predictable direction. | C fails: offspring do NOT inherit the full S; only the heritable fraction h² transmits across generations. | D fails: the multiplier is h² = VA/VP, not its inverse VP/VA. | E fails: S is the selection differential (phenotypic difference between breeders and population), not the mutation rate.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following does NOT describe natural selection?",
      "choices": [
        "It acts on phenotypes, not directly on alleles",
        "It is the only evolutionary mechanism that consistently produces adaptation",
        "It requires heritable variation in fitness-related traits to change allele frequencies",
        "It produces random, undirected changes in allele frequencies across generations",
        "It can act on continuous quantitative traits as well as discrete Mendelian traits"
      ],
      "answer": 3,
      "why": "&#9989; **D.** Random, undirected changes in allele frequencies describes GENETIC DRIFT, not natural selection. Selection is explicitly NON-RANDOM — it consistently and directionally favors alleles that increase fitness in the current environment. | A is true: selection sees phenotypes; allele frequency changes are the downstream consequence. | B is true: only selection produces consistent adaptation (drift and mutation are directionless with respect to fitness). | C is true: this is the heritability requirement — without it R = 0. | E is true: selection acts on any heritable phenotypic variation regardless of the underlying genetic architecture.",
      "sectionId": "s_ns",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "The Amish community in Lancaster, PA has an unusually high frequency of Ellis-van Creveld syndrome (a recessive condition). This is BEST explained by:",
      "choices": [
        "Natural selection favoring the allele in Amish farming environments",
        "High inbreeding causing the allele to be expressed more frequently in homozygotes",
        "Founder effect — the community was founded by a small group that happened to carry a high frequency of this allele, and that frequency was preserved through isolation",
        "Mutation pressure — the Amish lifestyle increases DNA damage and thus mutation rates",
        "Heterozygote advantage — carriers of the Ellis-van Creveld allele have higher reproductive fitness in the Amish agricultural environment"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This is the textbook founder effect example. A small founding group of ~200 settlers in the 1700s happened to include several carriers of the EVC allele. Because the community remained genetically isolated, this high allele frequency was maintained and expressed. No selection FOR the allele — it's purely a historical accident of who founded the colony. | **Wrong E:** There is no evidence of heterozygote advantage for Ellis-van Creveld syndrome in the Amish; the elevated allele frequency is fully explained by the founder effect (random sampling in the founding population), not by any fitness benefit conferred on carriers.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "What is the key difference between the Bottleneck Effect and Founder Effect?",
      "choices": [
        "Bottleneck only applies to plants; Founder Effect only applies to animals",
        "Bottleneck reduces genetic diversity by shrinking an existing population; Founder Effect creates a new isolated population from a small group colonizing a new area",
        "Bottleneck always leads to extinction; Founder Effect never reduces genetic diversity",
        "Bottleneck involves natural disasters only; Founder Effect requires intentional migration",
        "Bottleneck and Founder Effect are identical events that both describe small groups colonizing a new geographic area after a catastrophe"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Both are extreme genetic drift events. Bottleneck = existing population dramatically shrinks (then may recover, but with reduced diversity). Founder Effect = small group LEAVES and starts new isolated population elsewhere (e.g., island colonization). Both result in reduced genetic variation and potentially non-representative allele frequencies compared to the original large population. | **Wrong E:** Bottleneck and Founder Effect are not identical — the bottleneck describes a population that survives in its original location after a size crash, whereas the founder effect specifically involves geographic colonization of a new area by a small subset; the two events differ in their geographic context and demographic history.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following BEST characterizes a founder effect, satisfying ALL defining criteria?",
      "choices": [
        "A large population is struck by disease, killing 90% of individuals; the survivors rebuild the population with reduced genetic diversity",
        "A small group of individuals migrates to a new area but maintains continuous gene flow with the source population",
        "A small group colonizes a new area and carries alleles representative of the full source population in accurate proportions",
        "A small, genetically non-representative group colonizes a new isolated area, establishing a population whose allele frequencies diverge from the source by chance",
        "Natural selection in a new environment rapidly changes allele frequencies in a recently colonized small population"
      ],
      "answer": 3,
      "why": "&#9989; **D.** All four criteria are met: small group + colonizes new area + genetically non-representative (random sampling) + genetic divergence from source. | A fails: this describes a bottleneck effect — the population shrinks in place rather than colonizing a new area. | B fails: continuous gene flow with the source prevents divergence; founder effect requires isolation. | C fails: if the group is representative, there is no founder effect — the defining feature is non-representativeness by chance sampling. | E fails: this describes natural selection acting in a new environment, not the random founder effect drift mechanism.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Both the bottleneck effect AND the founder effect result in which of the following? (I) Reduced genetic variation relative to the original large population. (II) Non-representative allele frequencies compared to the source population. (III) Geographic isolation of the new population from the original. (IV) Complete extinction of all original genotypes in the source population.",
      "choices": [
        "I and II only",
        "I, II, and III",
        "I, II, III, and IV",
        "II and IV only",
        "I only"
      ],
      "answer": 0,
      "why": "&#9989; **A. I and II only.** Verify each: I ✓ — both events involve a small sample of the original gene pool, so rare alleles are lost and common alleles may be over- or under-represented, reducing overall diversity. II ✓ — by random chance, the small founding/surviving group will not perfectly mirror the source allele frequencies. III is FALSE for bottlenecks — a bottlenecked population remains in the same location; geographic isolation is characteristic of the founder effect but not the bottleneck. IV is FALSE — the source population continues to exist with its original alleles in both cases.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following correctly describes the step-by-step mechanism by which a population bottleneck reduces genetic variation?",
      "choices": [
        "The bottleneck event increases mutation rate → new deleterious mutations accumulate → rare alleles are outcompeted by new variants → net loss of original diversity",
        "Population size crashes to a small number → only a random subset of pre-existing alleles are carried by survivors → rare alleles are likely absent in the small sample → even if population recovers, those alleles remain lost",
        "Population size crashes → natural selection intensifies because competition is higher → low-fitness alleles are purged → genetic variation decreases by adaptive, not random, processes",
        "Population size crashes → inbreeding forces heterozygotes to become homozygotes → allele frequencies p and q change → genetic variation is permanently lost",
        "Population size crashes → gene flow stops → local mutations fix by selection → the population diverges adaptively rather than by random sampling"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The bottleneck mechanism is purely about random sampling: few survivors = small sample = rare alleles statistically unlikely to be present = permanent loss even after population recovers. | A fails: bottlenecks do not increase mutation rates; the loss is due to sampling, not new mutations. | C fails: the reduction is NON-ADAPTIVE — drift (random sampling), not selection, drives the loss. | D fails: inbreeding changes genotype frequencies but does NOT change allele frequencies p and q; the bottleneck reduces total allele diversity by losing alleles entirely. | E fails: local adaptation by selection is a different process from the random sampling that defines a bottleneck.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following does NOT increase the effect of genetic drift on a population?",
      "choices": [
        "Reducing effective population size (Ne) to fewer than 50 individuals",
        "Geographic isolation that prevents immigration of new alleles",
        "Increasing the effective population size from 100 to 100,000 individuals",
        "A severe bottleneck that reduces a population of 10,000 to 20 survivors",
        "High inbreeding that reduces the genetic effective population size"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Increasing Ne from 100 to 100,000 dramatically REDUCES the effect of genetic drift — larger populations sample alleles more reliably each generation, so random fluctuations in allele frequency are smaller. Drift is inversely proportional to Ne. | A increases drift: small Ne means large sampling error each generation. | B increases drift: isolation prevents gene flow from replenishing lost alleles, so drift proceeds unchecked. | D increases drift: a severe bottleneck is the textbook example of extreme drift. | E increases drift: inbreeding reduces the genetically effective population size (Ne), amplifying drift effects even if census population size is large.",
      "sectionId": "s_drift",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "FST values near zero between two populations indicate:",
      "choices": [
        "Strong natural selection is maintaining different alleles in each population",
        "High gene flow is homogenizing the two populations, keeping their allele frequencies similar",
        "High genetic drift is causing both populations to independently lose alleles",
        "The two populations are highly diverged due to long geographic separation",
        "Natural selection is acting on both populations in the same direction, independently driving them toward identical allele frequencies at the measured loci"
      ],
      "answer": 1,
      "why": "&#9989; **B.** FST = fixation index for subpopulations. FST near 0 = little genetic differentiation = populations have similar allele frequencies. This happens when gene flow is HIGH (migrants constantly move alleles between populations, preventing divergence). High FST would indicate restricted gene flow + independent drift/selection in each population. | **Wrong E:** While parallel selection could theoretically produce similar allele frequencies at selected loci, FST near zero across many genome-wide markers most parsimoniously indicates high gene flow, not convergent selection acting at every measured locus simultaneously — convergent selection is a far less likely explanation for genome-wide low FST values.",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "A population of bacteria is treated with a new antibiotic. Within 2 weeks, some bacteria survive. The CORRECT interpretation is:",
      "choices": [
        "The antibiotic caused mutations that created resistance in some bacteria",
        "Bacteria directed their mutations toward resistance because they sensed the antibiotic",
        "Pre-existing random mutations conferring resistance were already present at low frequency; the antibiotic selected FOR those variants by killing susceptible bacteria",
        "Gene flow from resistant bacteria in a nearby hospital created the resistance",
        "The bacterial population underwent a bottleneck when most cells died, and random genetic drift fixed the resistance allele in the survivors by chance rather than by selection"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Mutations are RANDOM. Resistance alleles existed before the antibiotic was applied (as pre-existing variation from prior random mutations). The antibiotic didn't create them — it SELECTED for them by eliminating susceptibles. This is also why stopping antibiotics early is dangerous: resistant variants that were always there now have no competition. | **Wrong E:** The mechanism is non-random directional selection (the antibiotic specifically kills susceptible bacteria based on their phenotype), not random genetic drift — if drift alone were responsible, resistant and susceptible survivors would be equally likely, but only resistant cells survive antibiotic treatment, which is the defining signature of selection, not drift.",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which scenario results in HIGH genetic differentiation (high FST) between two populations, satisfying ALL required conditions?",
      "choices": [
        "Two populations separated by a mountain range but connected by 50 migrants per generation",
        "Two large populations (N=50,000 each) in the same habitat with overlapping ranges",
        "Two populations recently split 10 generations ago with no barriers to dispersal",
        "Two populations on separate islands but with a stepping-stone corridor allowing occasional migration every few generations",
        "Two populations on separate continents with no migration, isolated for 100,000 generations, each evolving independently by drift and selection"
      ],
      "answer": 4,
      "why": "&#9989; **E.** All three conditions for high FST are met: low gene flow (zero migration) + geographic isolation + long separation allowing independent divergence. | A fails: 50 migrants/generation is sufficient gene flow to homogenize allele frequencies and keep FST low. | B fails: large overlapping populations with shared habitat implies high gene flow → low FST. | C fails: only 10 generations of separation is insufficient time for significant divergence; populations still share nearly identical allele frequencies. | D fails: even occasional migration (stepping-stone) dramatically reduces FST; even Nm=1 migrant/generation is enough to prevent strong differentiation.",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following statements about gene flow and mutation as evolutionary forces are TRUE? (I) Mutation is the only source of alleles that did not previously exist in any population. (II) Gene flow homogenizes allele frequencies between connected populations. (III) Mutations are directed toward fitness benefit when environmental conditions are harsh. (IV) Gene flow can prevent local adaptation by constantly importing alleles suited to a different environment.",
      "choices": [
        "I and II only",
        "II and IV only",
        "I, II, and IV only",
        "I, II, III, and IV",
        "I and IV only"
      ],
      "answer": 2,
      "why": "&#9989; **C. I, II, and IV only.** Verify each: I ✓ — only mutation creates truly new alleles; all other forces rearrange existing variation. II ✓ — gene flow moves alleles between populations, equalizing their frequencies and reducing FST. III is FALSE — this is Lamarckian thinking; mutations are random with respect to fitness and do not \"know\" what the environment needs. IV ✓ — gene flow imports alleles from other environments, which can swamp locally adaptive alleles and prevent local adaptation (gene flow–selection antagonism).",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following correctly describes the step-by-step mechanism by which gene flow reduces FST between two previously isolated populations?",
      "choices": [
        "Individuals migrate between populations → they carry alleles at their source-population frequencies into the recipient population → recipient allele frequencies shift toward the source → repeated migration events gradually equalize frequencies → FST decreases toward zero",
        "Individuals migrate between populations → migration increases mutation rate in the recipient population → new alleles converge on the same sequences in both populations → FST decreases toward zero",
        "Individuals migrate between populations → natural selection in the recipient population favors immigrant alleles → immigrant alleles replace resident alleles → FST decreases because both populations now match the immigrant source",
        "Individuals migrate between populations → migrants interbreed → heterozygosity increases → increased heterozygosity directly causes FST to increase as subpopulation structure becomes more apparent",
        "Individuals migrate between populations → they carry alleles at source-population frequencies → recipient allele frequencies shift away from the source → FST increases as populations diverge further"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the correct mechanism: migrants physically transport alleles, diluting frequency differences between populations, reducing FST. | B fails: gene flow does not increase mutation rates; the homogenization is through allele transport, not convergent mutation. | C fails: the mechanism is not selection favoring immigrant alleles but simple mixing of allele pools; selection is not required. | D fails: increased heterozygosity from admixture is a consequence of gene flow, but FST measures between-population differentiation — gene flow reduces FST, it does not increase it. | E fails: gene flow moves allele frequencies toward similarity, not further apart; divergence is caused by isolation, not gene flow.",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following does NOT correctly describe mutation as an evolutionary force?",
      "choices": [
        "Mutation is the ultimate source of all genetic variation on which other evolutionary forces act",
        "Mutations are directed toward whatever phenotype would increase the organism's fitness in its current environment",
        "Mutation rates are typically so low that mutation pressure alone changes allele frequencies very slowly",
        "Most new mutations are neutral or slightly deleterious with respect to fitness",
        "The same mutation can be beneficial, neutral, or deleterious depending on the environment"
      ],
      "answer": 1,
      "why": "&#9989; **B.** This is the classic Lamarckian error. Mutations are RANDOM with respect to fitness — they occur due to replication errors, radiation, chemical damage, etc., with no \"knowledge\" of what the organism needs. The antibiotic resistance example is key: bacteria don't mutate toward resistance because antibiotics are present; pre-existing random mutations are selected post-hoc. | A is true: mutation is the ultimate source of all new alleles. | C is true: typical mutation rates (~10⁻⁸ per base per generation) are so low that mutation pressure alone would take millions of generations to substantially shift allele frequencies. | D is true: most mutations are neutral (in non-functional DNA) or slightly deleterious. | E is true: the fitness effect of a mutation depends entirely on the environment (e.g., sickle-cell allele is protective in malaria regions, deleterious elsewhere).",
      "sectionId": "s_gf_mut",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following scenarios CORRECTLY identifies the evolutionary mechanism producing drug resistance in bacteria, satisfying ALL criteria: (1) mutation predates drug exposure, (2) selection kills susceptibles, (3) resistant variants increase in frequency, (4) heritable allele frequency change occurs?",
      "choices": [
        "Bacteria sense the antibiotic and activate a stress-response pathway that generates targeted resistance mutations in real time",
        "The antibiotic chemically modifies bacterial DNA at the resistance locus, converting susceptible alleles to resistant ones through direct mutagenesis",
        "Bacteria acquire resistance by absorbing DNA fragments released by dead resistant cells, then pass this acquired resistance to all offspring via Lamarckian inheritance",
        "Pre-existing random mutations conferred resistance before the drug was introduced; the drug selectively kills susceptible bacteria, increasing the frequency of the resistance allele across generations",
        "The antibiotic causes a population bottleneck that removes all susceptible genotypes by drift, leaving only resistant variants by chance rather than by selection"
      ],
      "answer": 3,
      "why": "&#9989; **D.** All four criteria are satisfied: mutations predate drug exposure ✓, selection (drug) kills susceptibles ✓, resistant variants increase in frequency ✓, heritable allele frequency change occurs ✓. | **A fails:** bacteria do not generate targeted adaptive mutations in response to a stressor — this is Lamarckian directed mutation, which does not occur. | **B fails:** antibiotics do not chemically convert alleles; they kill cells carrying susceptible alleles. | **C fails:** horizontal gene transfer (transformation) is real but is not Lamarckian inheritance; additionally, this scenario incorrectly invokes Lamarckian mechanisms. | **E fails:** the mechanism is non-random directional selection, not random genetic drift; antibiotics specifically kill susceptible bacteria (fitness-based), not a random bottleneck.",
      "sectionId": "s_applied",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which processes are shared by antibiotic resistance evolution AND domestication (e.g., greyhounds bred for speed)? (I) Heritable variation in a target trait exists before selection begins. (II) Selection is non-random — it consistently favors one variant over another. (III) Mutations are directed by the selective agent toward the favored phenotype. (IV) Allele frequencies change over generations in response to selection.",
      "choices": [
        "I and II only",
        "I, II, and IV only",
        "II and IV only",
        "I, II, III, and IV",
        "I and IV only"
      ],
      "answer": 1,
      "why": "&#9989; **B. I, II, and IV only.** Verify each: I &#10003; — both antibiotic resistance and domestication act on pre-existing heritable variation (standing genetic variation in bacteria; standing variation in ancestral wolves). II &#10003; — both involve non-random selection consistently favoring the resistant/fast variant over alternatives. III is FALSE — this is the Lamarckian error; mutations are random with respect to fitness in both systems; breeders do not direct dogs to mutate toward speed, and antibiotics do not direct bacteria to mutate toward resistance. IV &#10003; — in both cases allele frequencies at selected loci change heritably over generations, which is the definition of evolution. | **A fails:** III is incorrectly excluded while the correct answer needs I, II, and IV. | **C fails:** excludes I, which is shared. | **D fails:** includes III, which is false. | **E fails:** excludes II, which is shared.",
      "sectionId": "s_applied",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "A pharmaceutical company introduces a new antiviral drug. Which of the following correctly describes the step-by-step mechanism by which viral resistance evolves?",
      "choices": [
        "Virus population contains random genetic variation from prior mutations → drug kills variants lacking resistance → rare pre-existing resistant variant survives and replicates → resistant variants outcompete susceptibles in drug-treated host → resistance allele frequency rises over generations",
        "Drug is introduced → drug molecules bind to viral RNA polymerase → this binding causes the polymerase to introduce specific resistance mutations into newly replicated viral genomes → resistant viruses emerge as a direct product of drug exposure",
        "Drug is introduced → all viruses die initially → surviving viral fragments recombine randomly → new recombinant viruses happen to be resistant → resistance allele appears de novo after drug is introduced",
        "Drug is introduced → infected host immune system responds to drug-induced stress by generating resistant viral variants through directed somatic hypermutation → resistant viruses spread to new hosts",
        "Drug is introduced → resistant viruses are more virulent than susceptibles → virulence-selection automatically creates resistance → resistance and virulence are genetically linked and always co-evolve together"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the correct Darwinian mechanism: pre-existing random variation &#8594; selection kills susceptibles &#8594; resistant survivor replicates &#8594; frequency of resistance allele rises. RNA viruses in particular have high standing variation due to error-prone polymerases. | **B fails:** drugs do not direct the polymerase to make specific beneficial mutations; drug binding may cause errors but not targeted resistance mutations. | **C fails:** viral fragments do not recombine to generate resistance; resistance must come from pre-existing mutations, not post-death recombination. | **D fails:** the host immune system does not generate viral mutations; this confuses host antibody diversification (somatic hypermutation) with viral evolution. | **E fails:** resistance and virulence are not automatically linked; resistant viruses can be less virulent, more virulent, or equally virulent — the traits evolve independently depending on selection pressures.",
      "sectionId": "s_applied",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following does NOT represent an example of humans driving evolution through strong directional selection on a heritable trait?",
      "choices": [
        "Hospital use of antibiotics consistently selects for resistant bacterial strains across millions of patients worldwide",
        "Greyhounds selectively bred for racing speed over hundreds of generations, producing a population with extreme running morphology",
        "Commercial fishing fleets targeting only the largest cod, causing the average size at maturity to decrease over decades",
        "Farmers spraying pesticides on crop fields, selecting for resistant insect populations within a few seasons",
        "A population of wild deer living in a national park with no hunting evolves larger body size over 50 years"
      ],
      "answer": 4,
      "why": "&#9989; **E.** Wild deer with no hunting and no human-imposed selection pressure are NOT an example of human-driven evolution. Any size change over 50 years could reflect natural selection, genetic drift, or environmental change — but not human directional selection. Compare to A–D: all involve consistent, intentional or systematic human selection pressure on a heritable trait in a specific direction. | **A fails to be the answer:** antibiotic use is the canonical example of human activity driving rapid evolution. | **B fails to be the answer:** domestication/artificial selection for racing speed is textbook human-driven evolution. | **C fails to be the answer:** size-selective fishing is a well-documented case of unintentional human-driven evolution (Trophy hunting paradox). | **D fails to be the answer:** pesticide resistance is directly parallel to antibiotic resistance — human chemical selection driving allele frequency change.",
      "sectionId": "s_applied",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "A population shows EXCESS homozygotes compared to Hardy-Weinberg expectations. Which mechanism is MOST likely NOT responsible?",
      "choices": [
        "Inbreeding — relatives mating increases homozygosity",
        "Population subdivision — Wahlund effect creates apparent excess homozygotes when subpopulations with different allele frequencies are lumped together",
        "Heterozygote advantage (overdominance) — selection favoring heterozygotes would DECREASE homozygotes below HWE expectations",
        "Assortative mating — similar phenotypes mating together can increase homozygosity at trait-associated loci",
        "Directional selection removing one homozygote class — for example, selection strongly eliminating aa individuals each generation"
      ],
      "answer": 2,
      "why": "&#9989; **C is NOT responsible.** Heterozygote advantage (e.g., sickle cell) produces EXCESS HETEROZYGOTES compared to HWE, not excess homozygotes. Selection maintaining both alleles (balancing selection) favors Aa over AA and aa, resulting in more Aa than predicted by HWE. ALL other options (A, B, D) produce excess homozygotes. On Robbins' exams, &ldquo;Which is NOT&rdquo; questions like this are common. | **Wrong E:** Directional selection removing aa individuals would reduce the aa class below HWE expectation, but would simultaneously increase relative frequency of Aa heterozygotes and AA homozygotes — this does not specifically produce an overall excess of homozygotes; the net effect on homozygote frequency depends on which class is eliminated and does not uniformly increase homozygosity the way inbreeding or population subdivision do.",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Inbreeding in a population changes:",
      "choices": [
        "Both allele frequencies and genotype frequencies",
        "Genotype frequencies only — allele frequencies p and q remain unchanged",
        "Allele frequencies only — the same alleles exist but in different ratios",
        "Neither; inbreeding has no detectable effect on population genetics",
        "Allele frequencies only, but in a predictable direction — inbreeding systematically increases the frequency of the rarer recessive allele q over generations"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Inbreeding increases the probability of homozygosity (identical alleles by descent) without changing which alleles exist or at what frequencies. If p = 0.7 before inbreeding, it's still 0.7 after. But the 2pq heterozygote class shrinks and the p² + q² homozygote classes grow. This violates HWE assumptions but doesn't change allele frequencies directly. | **Wrong E:** Inbreeding does not change allele frequencies at all (neither p nor q), let alone systematically increase q — the recessive allele frequency q stays constant under inbreeding; only the proportion of alleles present in homozygous vs. heterozygous combinations changes.",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following CORRECTLY describes the population-genetic effect of inbreeding, satisfying ALL criteria?",
      "choices": [
        "Inbreeding increases homozygosity AND directly increases the frequency of deleterious recessive alleles (q rises)",
        "Inbreeding decreases heterozygosity AND directly causes evolution by changing allele frequencies p and q",
        "Inbreeding increases homozygosity AND decreases heterozygosity, but does NOT directly change allele frequencies p and q",
        "Inbreeding changes allele frequencies by concentrating recessive alleles in homozygotes, making q larger over generations",
        "Inbreeding increases homozygosity, changes allele frequencies, and also directly causes local adaptation by fixing locally beneficial alleles"
      ],
      "answer": 2,
      "why": "&#9989; **C.** All three criteria are met: homozygosity increases ✓, heterozygosity decreases ✓, allele frequencies p and q remain unchanged ✓. | A fails: inbreeding does NOT increase q — it exposes recessive alleles already present to selection, but q itself stays constant. | B fails: the first part is correct (heterozygosity decreases) but the second part is wrong — inbreeding does not change p or q; it is not itself an evolutionary force in the allele frequency sense. | D fails: q does not get larger — the deleterious recessive allele may be expressed more in homozygotes, but its frequency q is unchanged by inbreeding alone. | E fails: inbreeding does not change allele frequencies and does not directly cause local adaptation.",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Inbreeding has which of the following effects on a population? (I) Increases the frequency of homozygous genotypes (AA and aa). (II) Decreases the frequency of heterozygotes (Aa). (III) Changes allele frequencies p and q. (IV) Exposes recessive deleterious alleles to selection by increasing aa homozygote frequency.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III",
        "I, II, and IV only",
        "All four"
      ],
      "answer": 3,
      "why": "&#9989; **D. I, II, and IV only.** Verify each: I ✓ — inbreeding increases identity by descent, producing more AA and aa homozygotes. II ✓ — the 2pq heterozygote class shrinks as homozygosity increases. III is FALSE — this is the key exam trap; p and q do not change due to inbreeding alone. IV ✓ — more aa homozygotes means deleterious recessive phenotypes are expressed more often, exposing them to natural selection (which CAN then change q indirectly, but inbreeding itself does not).",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following correctly describes the mechanism by which inbreeding depression manifests in a population?",
      "choices": [
        "Related individuals mate → offspring have elevated probability F of receiving two IBD copies of the same allele → frequency of aa homozygotes exceeds HWE expectation → deleterious recessive phenotypes are expressed → reduced mean fitness (inbreeding depression)",
        "Related individuals mate → offspring receive new deleterious mutations from both parents simultaneously → mutation load doubles each generation → fitness declines through accumulation of new mutations",
        "Related individuals mate → allele frequency q of deleterious recessives increases → more aa homozygotes appear → fitness declines because selection can no longer remove the allele",
        "Related individuals mate → heterozygote advantage is lost → selection now favors AA homozygotes over Aa → the population shifts toward fixation of the dominant allele → fitness declines from loss of balanced polymorphism",
        "Related individuals mate → gene flow between relatives is blocked → isolated family lineages fix deleterious alleles by selection → fitness declines through selective sweeps of harmful alleles"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the correct mechanism: IBD → excess homozygotes → exposed recessives → expressed deleterious phenotypes → inbreeding depression. | B fails: inbreeding does not increase the mutation rate; depression is due to expression of pre-existing recessive alleles, not new mutations. | C fails: inbreeding does NOT change q; the frequency of deleterious alleles stays the same — only their expression (in homozygotes) increases. | D fails: inbreeding depression is not primarily about loss of heterozygote advantage; it is about exposure of recessive lethals/deleterious alleles genome-wide. | E fails: the mechanism is random IBD sampling, not selection fixing harmful alleles; gene flow is unrelated to the core inbreeding depression mechanism.",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "Which of the following does NOT result directly from inbreeding?",
      "choices": [
        "Increased frequency of homozygous genotypes relative to HWE expectations",
        "Decreased frequency of heterozygotes relative to HWE expectations",
        "Greater expression of deleterious recessive phenotypes in the population",
        "A direct change in allele frequencies p and q at inbred loci",
        "A violation of Hardy-Weinberg genotype frequency expectations"
      ],
      "answer": 3,
      "why": "&#9989; **D.** Inbreeding does NOT directly change allele frequencies p and q — this is the single most important and most-tested fact about inbreeding in population genetics. Genotype frequencies shift (more homozygotes, fewer heterozygotes), but if you calculate p from the inbred population's genotype counts you get exactly the same p as before. | A is a direct result of inbreeding (IBD increases homozygosity). | B is a direct result (heterozygotes are depleted). | C is a direct result (more aa homozygotes → more recessive phenotype expression). | E is a direct result (inbreeding violates the random mating assumption of HWE, so genotype frequencies deviate from p²:2pq:q² expectations).",
      "sectionId": "s_inbreeding",
      "chapterId": "ch_s_evo_mech"
    },
    {
      "prompt": "In a population of 500 individuals, you observe: AA = 245, Aa = 210, aa = 45. What is the frequency of the A allele (p)?",
      "choices": [
        "p = 0.245",
        "p = 0.49",
        "p = 0.70",
        "p = 0.455",
        "p = 0.35"
      ],
      "answer": 2,
      "why": "&#9989; **C. p = 0.70.** p = (2×AA + Aa) / (2×N) = (2×245 + 210) / (2×500) = (490 + 210) / 1000 = 700/1000 = 0.70. Then q = 1 - 0.70 = 0.30. Expected HWE counts: AA = 0.49×500 = 245, Aa = 0.42×500 = 210, aa = 0.09×500 = 45. These match observed! This population IS in HWE. | **Wrong E:** p = 0.35 is incorrect — this value would require far fewer AA individuals and far more aa individuals than observed; the correct calculation using the allele-counting formula p = (2×AA + Aa)/2N gives 700/1000 = 0.70, not 0.35.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Using p = 0.7 and q = 0.3, what is the expected frequency of HETEROZYGOTES under HWE?",
      "choices": [
        "0.30",
        "0.42",
        "0.49",
        "0.09",
        "0.21"
      ],
      "answer": 1,
      "why": "&#9989; **B. 2pq = 2 × 0.7 × 0.3 = 0.42.** This is always the biggest genotype frequency class when both alleles exist at intermediate frequencies. Remember: p² + 2pq + q² = 0.49 + 0.42 + 0.09 = 1.0 ✓. If you observe FEWER heterozygotes than 0.42, suspect inbreeding. If MORE, suspect heterozygote advantage. | **Wrong A:** 0.30 is simply q — the frequency of the recessive allele alone — not the heterozygote frequency; confusing an allele frequency with a genotype frequency is a common error; the heterozygote formula is 2pq, which requires multiplying both allele frequencies together and doubling. | **Wrong E:** 0.21 equals p × q (without the factor of 2), which is a common error — the heterozygote frequency under HWE is 2pq because a heterozygote Aa can form two ways (A from father, a from mother, or a from father, A from mother), so the correct formula requires multiplying p × q by 2 to give 2 × 0.7 × 0.3 = 0.42.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "A recessive disorder occurs at frequency 1/10,000 in a large randomly mating population. What is the carrier (heterozygote) frequency?",
      "choices": [
        "1/10,000 (same as affected frequency)",
        "1/100 (square root of affected frequency — the recessive allele frequency)",
        "~1/50 (approximately 2pq ≈ 2q when q is small)",
        "1/5,000 (half the affected frequency)",
        "~1/200 (because carrier frequency = 2 × q² when q is small)"
      ],
      "answer": 2,
      "why": "&#9989; **C. ~1/50.** q² = 1/10,000, so q = 1/100 = 0.01. Carrier frequency = 2pq ≈ 2×(0.99)×(0.01) ≈ 0.0198 ≈ 1/50. CRITICAL insight: carriers are ~200× more common than affected individuals! (1/50 vs 1/10,000). Most recessive disease alleles in a population are hiding in heterozygote carriers, not in affected homozygotes. | **Wrong E:** The formula 2 × q² is incorrect — carrier frequency is 2pq (the heterozygote class), not 2 × q²; using 2 × q² would give 2/10,000 = 1/5,000, which confuses the heterozygote formula with twice the homozygote frequency; the correct carrier calculation requires first taking the square root of the affected frequency to find q, then computing 2pq.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following populations is MOST likely to be in Hardy-Weinberg equilibrium at a given locus, satisfying ALL five HWE assumptions?",
      "choices": [
        "A population of 25 individuals on a remote island, mating randomly, with no immigration",
        "A large urban population with random mating, but subject to strong directional selection on the locus in question",
        "A large population with random mating and no selection, but receiving 200 immigrants per generation from a population with different allele frequencies",
        "A large captive population (N=10,000) with random mating, no selection on the locus, no mutation at the locus, and no immigration",
        "A large wild population with random mating and no gene flow, but with a high mutation rate at the locus due to a nearby mutagen"
      ],
      "answer": 3,
      "why": "&#9989; **D.** All five HWE assumptions are satisfied: large N (no significant drift) ✓, random mating ✓, no selection at the locus ✓, no mutation ✓, no gene flow ✓. | A fails: N=25 means genetic drift is substantial — HWE requires effectively infinite population size. | B fails: strong directional selection directly changes allele frequencies and genotype distributions away from HWE. | C fails: 200 immigrants/generation with different allele frequencies = gene flow violation — recipient allele frequencies are shifted by incoming migrants. | E fails: high mutation rate violates the no-mutation assumption; even though mutation rates are usually low, the question specifies a high rate here.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following violations of HWE cause EXCESS HOMOZYGOTES relative to HWE predictions? (I) Inbreeding. (II) Population subdivision / Wahlund effect. (III) Heterozygote advantage (overdominance). (IV) Positive assortative mating (like phenotypes mate together).",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and IV only",
        "I, II, III, and IV",
        "II and IV only"
      ],
      "answer": 2,
      "why": "&#9989; **C. I, II, and IV only.** Verify each: I ✓ — inbreeding directly increases IBD homozygosity, producing excess homozygotes. II ✓ — the Wahlund effect: pooling subpopulations with different allele frequencies artificially deflates the apparent heterozygote count relative to a single HWE expectation, giving apparent excess homozygotes. III is FALSE — heterozygote advantage (overdominance, e.g., sickle cell) selects FOR heterozygotes, producing EXCESS HETEROZYGOTES relative to HWE, not excess homozygotes. IV ✓ — assortative mating (AA × AA, aa × aa preferred) concentrates homozygous combinations, increasing observed homozygotes above HWE expectation.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "A researcher counts genotypes in a population of 200: AA=98, Aa=84, aa=18. Which of the following correctly describes the step-by-step process to test for HWE deviation?",
      "choices": [
        "Calculate p = (2×98 + 84)/(2×200) = 280/400 = 0.70; q = 1−0.70 = 0.30 → Expected: AA=0.49×200=98, Aa=0.42×200=84, aa=0.09×200=18 → Observed matches Expected → population IS in HWE",
        "Calculate p = 98/200 = 0.49; q = 18/200 = 0.09 → Expected: AA=0.49×200=98, Aa=0.42×200=84 → compare observed to expected → population IS in HWE",
        "Calculate p = (2×98 + 84)/(200) = 280/200 = 1.40; recognize this is impossible → conclude the population cannot be tested for HWE",
        "Calculate p = (2×98 + 84)/(2×200) = 0.70 → Expected heterozygotes = p×q×200 = 0.70×0.30×200 = 42 → observed Aa=84 ≠ 42 → population is NOT in HWE",
        "Calculate p = 98/200 = 0.49; Expected AA = p²×N = 0.49×200 = 98 → since AA matches, conclude population is in HWE without checking other genotypes"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct procedure: use 2N alleles (not N individuals) in the denominator when calculating allele frequency. p = (2×AA + Aa)/2N. Then compute expected counts using p², 2pq, q² × N. Here all three genotype classes match — population is in HWE. | B fails: p ≠ 98/200; that formula uses genotype count not allele count — the denominator must be 2N=400. | C fails: the error in B produces an impossible value; the correct formula gives p=0.70 which is perfectly valid. | D fails: heterozygote expected frequency is 2pq, not p×q — missing the factor of 2; 2×0.70×0.30×200=84, which matches observed. | E fails: checking only one genotype class is insufficient; all three must match HWE expectations before concluding equilibrium.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following does NOT violate Hardy-Weinberg assumptions?",
      "choices": [
        "A population in which taller individuals consistently survive predation better than shorter individuals",
        "A population in which individuals preferentially mate with others of similar body size",
        "A population that receives 10 migrants per generation from a neighboring population with different allele frequencies",
        "A population of only 30 individuals on a small island",
        "A large population with random mating in which individuals vary continuously in body size due to polygenic inheritance"
      ],
      "answer": 4,
      "why": "&#9989; **E.** Phenotypic variation in body size — even continuous polygenic variation — does NOT violate any HWE assumption as long as mating is random with respect to genotype, population size is large, there is no selection at the specific locus being tested, no mutation, and no gene flow. HWE describes genotype frequencies at a locus; the mere existence of phenotypic variation does not violate it. | A violates HWE: differential survival based on a heritable trait = natural selection. | B violates HWE: mating based on similar phenotype (assortative mating) = non-random mating. | C violates HWE: immigrants with different allele frequencies = gene flow. | D violates HWE: N=30 means substantial genetic drift — HWE requires effectively infinite population size.",
      "sectionId": "s_hwe",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which component of phenotypic variance is MOST directly responsible for the response to natural selection (R in the breeder's equation)?",
      "choices": [
        "VD — dominance variance, because it determines heterozygote expression",
        "VE — environmental variance, because organisms must match their environment",
        "VA — additive genetic variance, because it determines parent-offspring resemblance and h²",
        "VI — epistatic variance, because gene-gene interactions create new combinations",
        "VG — total genetic variance (VA + VD + VI), because it captures all heritable effects including dominance and epistasis"
      ],
      "answer": 2,
      "why": "&#9989; **C. VA** — additive variance is the component that parent-offspring regression captures. h² = VA/VP. R = h² × S = (VA/VP) × S. Dominance and epistasis (VD, VI) don't transfer as predictably across generations because the allele combinations that create them may not be preserved. | **Wrong E:** VG = VA + VD + VI is broad-sense genetic variance, which overestimates the response to selection because VD (dominance) and VI (epistasis) create non-additive allele interactions that are reshuffled by meiosis and fertilization each generation and do not reliably transmit parent phenotype to offspring — only the additive component VA transmits predictably, which is why the breeder's equation uses h² = VA/VP, not H² = VG/VP.",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "A parent-offspring regression for beak length in finches has a slope of 0.65. This means:",
      "choices": [
        "65% of phenotypic variance is due to the environment",
        "Narrow-sense heritability (h²) = 0.65 — 65% of phenotypic variance is due to additive genetic effects",
        "65% of individuals will inherit the same beak length as their parents",
        "The breeder's equation predicts a selection differential of 0.65 for beak length",
        "Broad-sense heritability (H²) = 0.65 — the slope of a parent-offspring regression estimates the total genetic component including dominance"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The SLOPE of a parent-offspring regression IS narrow-sense heritability h². A slope of 0.65 means h² = 0.65. 65% of phenotypic variance is attributable to additive genetic effects. This is actually the reported heritability for beak length in the Grants' Galápagos finch study. | **Wrong E:** The parent-offspring regression slope specifically estimates narrow-sense h² (= VA/VP), not broad-sense H² (= VG/VP); broad-sense heritability requires comparing identical twins or full-sibling designs that capture dominance and epistasis, whereas the midparent–offspring regression captures only the additive component that is faithfully transmitted from parent to offspring.",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which experimental result would give the HIGHEST narrow-sense heritability estimate (h²), satisfying ALL required conditions?",
      "choices": [
        "A parent-offspring regression with a shallow slope (≈0.1) and high scatter around the line",
        "A parent-offspring regression with a steep slope (≈0.9), low environmental variance (VE small), and high additive genetic variance (VA large)",
        "Identical twins raised apart showing very similar phenotypes, indicating high broad-sense heritability H² but unknown VA",
        "A selection experiment where S is large but R is near zero after many generations",
        "A population reared in a highly uniform environment where VE ≈ 0 but VA is also near zero"
      ],
      "answer": 1,
      "why": "&#9989; **B.** All three conditions for high h² are met: steep parent-offspring regression slope (slope = h²) ✓, low VE (less environmental noise inflating VP) ✓, high VA (the numerator of h² = VA/VP) ✓. | A fails: shallow slope ≈ 0.1 means h² ≈ 0.1 — very low heritability. | C fails: twin studies estimate broad-sense H² = VG/VP, which includes dominance and epistasis, not narrow-sense h² = VA/VP. | D fails: large S but R ≈ 0 means h² ≈ 0 by the breeder's equation (R = h² × S). | E fails: if both VE and VA are near zero, VP is near zero and h² is undefined or trivially low — there is no meaningful variation to analyze.",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following statements about narrow-sense heritability (h²) are TRUE? (I) h² = VA/VP. (II) The slope of a parent-offspring regression estimates h². (III) h² applies universally across all environments and populations for a given trait. (IV) R = h² × S.",
      "choices": [
        "I and IV only",
        "I, II, and III",
        "II and IV only",
        "I, II, and IV only",
        "All four"
      ],
      "answer": 3,
      "why": "&#9989; **D. I, II, and IV only.** Verify each: I ✓ — by definition, narrow-sense heritability equals additive variance divided by total phenotypic variance. II ✓ — the regression of offspring phenotype on midparent phenotype has a slope equal to h²; this is the standard empirical method for estimating heritability. III is FALSE — h² is population-specific and environment-specific; it can differ between populations with different VA or VP, and the same population can show different h² in different environments (e.g., if VE changes). IV ✓ — the Breeder's Equation R = h² × S is the fundamental formula linking heritability, selection intensity, and evolutionary response.",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following correctly describes the step-by-step mechanism by which a plant breeder uses h² and S to predict and achieve response to selection?",
      "choices": [
        "Measure trait in whole population → select top individuals as breeders → calculate S = mean(breeders) − mean(population) → apply R = h² × S to predict offspring mean → cross selected plants → verify offspring mean shifted by ≈R",
        "Measure trait in whole population → select top individuals → calculate S = mean(breeders) − mean(population) → apply R = VD/VP × S to predict offspring mean → cross selected plants",
        "Measure trait in whole population → select top individuals → calculate S = mean(breeders) − mean(population) → apply R = h² × VP to predict offspring mean → cross selected plants",
        "Measure trait in whole population → select top individuals → calculate S = mean(population) − mean(breeders) → apply R = h² × S → because S is negative, offspring mean decreases regardless of trait direction",
        "Measure trait in whole population → select top individuals → calculate S = mean(breeders) × mean(population) → apply R = h² × S → cross selected plants → verify offspring mean shifted by ≈R"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the exact procedure: measure → select → compute S as difference (breeders minus population mean) → multiply by h² → predict R → verify. | B fails: uses VD/VP (dominance component) instead of h² = VA/VP; dominance variance does not predict parent-offspring resemblance reliably. | C fails: R = h² × S, not h² × VP; multiplying heritability by total variance gives units of variance, not a mean shift. | D fails: S = mean(breeders) − mean(population), not the reverse; if selecting the top individuals, S is positive (breeders exceed population mean). | E fails: S is a difference (subtraction), not a product (multiplication) of the two means.",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following does NOT contribute to narrow-sense heritability (h²)?",
      "choices": [
        "Additive effects of alleles at a single locus (each copy adds a constant increment to the phenotype)",
        "Additive effects of alleles across multiple loci acting independently (polygenic additive model)",
        "Dominance variance (VD) arising from interactions between alleles within a locus, and epistatic variance (VI) from interactions between loci",
        "Any source of variance that produces a predictable linear parent-offspring resemblance",
        "Additive genetic variance as estimated from the slope of a parent-offspring regression"
      ],
      "answer": 2,
      "why": "&#9989; **C.** VD (dominance variance) and VI (epistatic/interaction variance) are NOT part of narrow-sense heritability h² = VA/VP. They are part of broad-sense heritability H² = VG/VP. Dominance and epistasis create non-additive genetic effects that do not transmit predictably from parent to offspring because allele combinations are reshuffled each generation. | A contributes: single-locus additive effects are the core of VA. | B contributes: polygenic additive effects sum into VA. | D contributes: by definition, h² captures the linear (additive) parent-offspring covariance. | E contributes: the parent-offspring regression slope directly estimates h².",
      "sectionId": "s_quant_gen",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following CORRECTLY describes additive allele effects, satisfying ALL criteria: (1) Aa phenotype = midpoint between AA and aa, (2) effect is linear with copy number, (3) no dominance or masking occurs, (4) quantitative traits commonly show this pattern?",
      "choices": [
        "In an additive model, the Aa heterozygote always has the same phenotype as the AA homozygote because one copy of the A allele is sufficient to produce the full phenotypic effect",
        "In an additive model, the Aa heterozygote has a phenotype closer to aa than AA because recessive alleles contribute more to the phenotype when paired with a dominant allele",
        "In an additive model, each copy of allele A produces a non-linear, threshold effect — the first copy has no effect, but two copies (AA) produce the full phenotype",
        "In an additive model, each copy of allele A adds a fixed amount to the trait; an Aa individual has a phenotype exactly intermediate between AA and aa, and the effect on VP is captured by VA",
        "In an additive model, the environment determines how much each allele contributes, so Aa phenotype varies widely across environments and cannot be predicted from parental genotypes"
      ],
      "answer": 3,
      "why": "&#9989; **D.** All four criteria satisfied: Aa = midpoint &#10003;, effect is linear per copy &#10003;, no dominance/masking &#10003;, quantitative traits captured by VA &#10003;. | **A fails:** Aa = AA describes complete dominance of A, not additivity — in a dominant model one copy is sufficient; in an additive model one copy gives only half the effect. | **B fails:** Aa closer to aa would describe incomplete dominance biased toward the recessive — not the midpoint additivity model. | **C fails:** threshold effects describe recessive (not additive) action — in a recessive model the first copy has no phenotypic effect; additivity requires each copy to contribute equally. | **E fails:** additivity refers to genetic architecture (each allele copy adds a fixed genetic increment), not environmental sensitivity; phenotypic plasticity (VE) is a separate component of VP from VA.",
      "sectionId": "s_alleles",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which statements about allele dominance are TRUE? (I) Dominant alleles mask recessive alleles in heterozygotes — the recessive phenotype is not expressed when one dominant copy is present. (II) When a beneficial allele is recessive and rare, it spreads slowly because most copies are hidden in heterozygotes where they are masked from selection. (III) Additive alleles show complete dominance — one copy produces the full phenotype just as two copies do. (IV) Rare recessive beneficial alleles eventually spread faster as they become more common and more aa homozygotes appear, making selection more effective.",
      "choices": [
        "I and II only",
        "I, II, and III",
        "I, II, and IV only",
        "I and IV only",
        "All four"
      ],
      "answer": 2,
      "why": "&#9989; **C. I, II, and IV only.** Verify each: I &#10003; — this is the definition of dominance: A masks a in Aa, so the recessive phenotype requires aa. II &#10003; — when q is small, 2pq >> q², so most recessive alleles hide in Aa heterozygotes invisible to selection; this is the core reason rare recessives spread slowly. III is FALSE — additive alleles are specifically defined by the absence of complete dominance; Aa has an intermediate phenotype between AA and aa (each copy adds half the full effect), which is the opposite of complete dominance. IV &#10003; — as q rises, q² becomes an increasingly large fraction of the recessive allele pool; more aa homozygotes appear, selection becomes progressively more effective, and the rate of spread accelerates. | **A fails:** omits IV which is true. | **B fails:** includes III which is false. | **D fails:** omits II which is true. | **E fails:** includes III which is false.",
      "sectionId": "s_alleles",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "A new beneficial mutation that is completely recessive arises in a large population at frequency q = 0.001. Which of the following correctly describes the mechanism of its initial slow spread?",
      "choices": [
        "When q = 0.001, HWE predicts ~0.2% of individuals are Aa heterozygotes (2pq ≈ 0.002) but only 0.0001% are aa homozygotes (q² = 0.000001); the beneficial phenotype only appears in aa, so selection acts on an extremely rare class; Aa individuals are indistinguishable from AA, making the allele nearly invisible to selection and causing very slow initial spread",
        "When q = 0.001, the allele spreads quickly because even though most copies are in heterozygotes, the additive effect means each copy contributes a small but detectable benefit that selection can act on in Aa individuals",
        "When q = 0.001, all copies of the recessive allele are in aa homozygotes because HWE concentrates rare alleles in homozygotes; selection acts efficiently on all copies simultaneously, causing rapid spread",
        "When q = 0.001, the allele spreads at the same rate as a dominant allele of equal fitness benefit because selection strength depends only on the fitness coefficient s, not on the allele's dominance",
        "When q = 0.001, genetic drift is the main force acting because q is too small for natural selection to have any effect regardless of whether the allele is dominant or recessive"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This correctly applies HWE math to the problem: 2pq = 2(0.999)(0.001) &#8776; 0.002; q² = 0.000001. The ratio of heterozygotes to homozygotes is 2000:1 — the overwhelming majority of copies are masked in Aa. Since the recessive phenotype only appears in aa (frequency 0.000001), selection has almost nothing to act on and the allele drifts more than it is selected. | **B fails:** the question specifies the allele is completely recessive, not additive — in Aa there is no phenotypic effect, so selection cannot act on Aa individuals at all. | **C fails:** this reverses the HWE prediction entirely; rare alleles are concentrated in heterozygotes (2pq >> q² when q is small), not homozygotes. | **D fails:** spread rate depends critically on dominance; a dominant allele of the same s is immediately visible in Aa (frequency 2pq) and spreads much faster than a recessive allele of the same s. | **E fails:** while drift matters when q is tiny, selection does act — just very weakly because so few aa homozygotes exist; as q rises, selection becomes progressively more effective. The key point is that recessiveness, not just small q, is the bottleneck.",
      "sectionId": "s_alleles",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following does NOT correctly describe a dominant allele?",
      "choices": [
        "A dominant allele produces its associated phenotype when present in one copy (heterozygote Aa expresses the dominant phenotype)",
        "A dominant allele masks the phenotypic expression of the recessive allele it is paired with in a heterozygote",
        "A dominant allele always has higher fitness than the recessive allele it masks — dominance implies a selective advantage",
        "Dominance describes the pattern of expression in a heterozygote, not the fitness consequence of the allele",
        "A dominant allele can be deleterious — for example, Huntington's disease is caused by a dominant allele with severely reduced fitness"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Dominance describes EXPRESSION in heterozygotes (whether one copy is sufficient to produce a phenotype), not fitness. A dominant allele can be highly deleterious — Huntington's disease is the textbook example of a dominant disease allele that reduces fitness dramatically. Dominance &ne; fitness advantage. | **A is correct:** this is the definition of a dominant allele — one copy suffices for expression. | **B is correct:** masking of the recessive is the mechanism of dominance. | **D is correct:** dominance is purely about phenotypic expression in Aa; it says nothing about whether the allele increases or decreases fitness. | **E is correct:** Huntington's (CAG repeat expansion) is dominant and severely fitness-reducing — a dominant deleterious allele that persists because it acts after reproductive age.",
      "sectionId": "s_alleles",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "A reaction norm graph shows genotype A as a flat horizontal line and genotype B as a steep positive slope across environments 1-4. Which statement is CORRECT?",
      "choices": [
        "Genotype A is more plastic than B because it maintains the same phenotype across all environments",
        "There is no G×E because one genotype is flat",
        "Genotype B is more plastic than A; there IS G×E (non-parallel lines) because the two genotypes respond differently to the environment",
        "G×E requires that the reaction norms cross each other; non-crossing non-parallel lines have no G×E",
        "Both genotypes show equal plasticity because genotype A is buffered against the environment and genotype B amplifies it, meaning they have the same average phenotype across environments"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Plasticity = slope of the reaction norm for a given genotype. Genotype A (flat) = no plasticity. Genotype B (steep) = high plasticity. G×E = non-parallel slopes between genotypes = they respond differently to environment. A flat line vs. a steep line = non-parallel = G×E. Crossing is ONE type of G×E but not the only type. | **Wrong E:** A flat reaction norm (slope = 0) indicates zero plasticity for genotype A, while a steep slope for genotype B indicates high plasticity — these are definitionally unequal degrees of plasticity; having the same average phenotype across environments would require the lines to have the same mean height, but plasticity is measured by the slope of each line, not by averages.",
      "sectionId": "s_plasticity",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following BEST describes genotype-by-environment interaction (G×E), satisfying ALL defining criteria?",
      "choices": [
        "All genotypes in a population show the same degree of phenotypic change across environments, producing parallel reaction norm lines",
        "A single genotype produces different phenotypes in different environments, with a sloped reaction norm",
        "Different genotypes respond differently to the same environmental gradient, producing non-parallel reaction norm slopes",
        "The environment changes allele frequencies by selecting against certain genotypes, altering p and q over generations",
        "All genotypes show flat reaction norms, indicating no phenotypic plasticity in any genotype"
      ],
      "answer": 2,
      "why": "&#9989; **C.** G×E requires: different genotypes + respond differently + non-parallel reaction norms. All three criteria met. | A fails: parallel slopes mean all genotypes respond equally — this is plasticity (if sloped) but NOT G×E; G×E requires non-parallel slopes. | B fails: this describes phenotypic plasticity of a single genotype, not G×E; G×E requires comparing the responses of at least two genotypes. | D fails: this describes natural selection changing allele frequencies — a separate process from G×E, which is about phenotypic response patterns, not allele frequency change. | E fails: flat reaction norms in all genotypes means no plasticity and, since all are equally flat, no G×E either.",
      "sectionId": "s_plasticity",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Reaction norm analysis can demonstrate which of the following? (I) Phenotypic plasticity of individual genotypes across environments. (II) G×E interaction when reaction norm slopes differ between genotypes. (III) That genetic variation is absent if reaction norms are parallel across genotypes. (IV) That high plasticity necessarily means high narrow-sense heritability for the trait.",
      "choices": [
        "I and II only",
        "I, II, and III",
        "I, II, and IV",
        "All four",
        "II and III only"
      ],
      "answer": 0,
      "why": "&#9989; **A. I and II only.** Verify each: I ✓ — a sloped reaction norm for a given genotype directly demonstrates that genotype is plastic (phenotype changes with environment). II ✓ — non-parallel slopes between genotypes is the definition of G×E; reaction norm plots make this visually apparent. III is FALSE — parallel reaction norms mean all genotypes respond similarly (same plasticity), but the genotypes can still differ in their mean phenotype (vertical offset between lines) — genetic variation can be present even with parallel slopes. IV is FALSE — plasticity (phenotypic change across environments) reflects VGxE and VE, not VA; a highly plastic trait can have low h² if most variance is environmental.",
      "sectionId": "s_plasticity",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following correctly describes how polyphenic development produces discrete alternative phenotypes from a single genotype?",
      "choices": [
        "A single genotype encounters an environmental cue (e.g., larval nutrition level or temperature) during a critical developmental window → the cue triggers a developmental switch → gene expression programs diverge → discrete alternative phenotypes (e.g., queen vs. worker bee) are produced",
        "A single genotype encounters an environmental cue → the cue causes new mutations in developmental genes → the mutated offspring develop along a different pathway → discrete phenotypes appear in subsequent generations",
        "A single genotype encounters an environmental cue during adulthood → the cue permanently alters the DNA sequence of key developmental genes → alternative phenotypes are inherited by offspring (Lamarckian mechanism)",
        "Two different genotypes in a population respond to the same temperature cue → each genotype produces one phenotype → the population shows two discrete forms → this is polyphenism caused by genetic polymorphism",
        "A single genotype encounters a nutritional cue → continuous gradation of phenotypes is produced proportional to nutrition level → the most extreme value at high nutrition is called the polyphenic form"
      ],
      "answer": 0,
      "why": "&#9989; **A.** Polyphenism: one genome + environmental switch during development → discrete alternative phenotypes. The key features are: single genotype, developmental timing of the cue, gene expression divergence (not DNA change), and discrete (not continuous) outcome. | B fails: polyphenism does not involve new mutations — the genome is unchanged; only gene expression patterns differ. | C fails: environmental cues do not alter DNA sequence; this describes a Lamarckian inheritance mechanism that does not occur. | D fails: if two genotypes each produce one form, that is genetic polymorphism, not polyphenism — polyphenism requires a SINGLE genotype producing multiple forms. | E fails: continuous gradation proportional to environment describes continuous plasticity, not polyphenism; polyphenism is specifically discrete (switch-like), not graded.",
      "sectionId": "s_plasticity",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following does NOT indicate genotype-by-environment interaction (G×E)?",
      "choices": [
        "Two genotypes whose reaction norms cross each other across an environmental gradient",
        "One genotype with a steep positive reaction norm slope and another genotype with a steep negative slope across the same environments",
        "One genotype whose phenotype increases strongly with temperature while another genotype's phenotype is unaffected by temperature",
        "Two genotypes with parallel, positively sloped reaction norms — both increase their phenotype by the same amount across environments",
        "Two genotypes whose rank order of phenotypic values reverses between environment 1 and environment 2"
      ],
      "answer": 3,
      "why": "&#9989; **D.** Parallel slopes = both genotypes respond identically to environmental change = NO G×E. G×E requires that genotypes differ in HOW they respond (different slopes). Parallel lines show plasticity (if sloped) but the same plasticity in both genotypes — no interaction. | A indicates G×E: crossing reaction norms are the classic visual signature of G×E. | B indicates G×E: one positive and one negative slope are maximally non-parallel — strong G×E. | C indicates G×E: one genotype plastic, one flat = non-parallel = G×E. | E indicates G×E: rank reversal (the genotype ranked higher in environment 1 is ranked lower in environment 2) is the strongest form of G×E and has important implications for selection.",
      "sectionId": "s_plasticity",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "DNA methylation of a gene's promoter region most directly affects gene expression at which level?",
      "choices": [
        "Post-translational — methylation adds chemical groups that change protein function",
        "Post-transcriptional — methylation degrades existing mRNA transcripts",
        "Pre-transcriptional — methylation condenses chromatin, making the DNA inaccessible for transcription",
        "Transcriptional — methylation directly inhibits RNA polymerase activity",
        "Post-transcriptional — methylation targets the 5' cap of the mRNA transcript, triggering its rapid degradation in the cytoplasm"
      ],
      "answer": 2,
      "why": "&#9989; **C.** DNA methylation at promoter regions causes chromatin condensation (heterochromatin), making the DNA physically inaccessible to transcription factors and RNA polymerase. This is a PRE-transcriptional mechanism — it prevents transcription from even beginning. miRNA acts post-transcriptionally; post-translational mechanisms act after protein is made. | **Wrong E:** DNA methylation at promoter CpG islands acts on the DNA template in the nucleus before any mRNA is produced — it does not target the mRNA 5' cap; mRNA cap targeting is a post-transcriptional mechanism used by decapping enzymes and miRNA pathways, which are mechanistically and spatially distinct from promoter CpG methylation.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Pseudogenes in a genome are BEST described as:",
      "choices": [
        "Genes that control the expression of other genes at the transcriptional level",
        "Non-functional copies of genes that have accumulated mutations rendering them inactive, often relics of gene duplication or retrotransposition",
        "Genes expressed only in embryonic development, silenced in adults",
        "Mobile genetic elements that can move to different chromosomal locations",
        "Short repetitive sequences (~300 bp) dispersed throughout the genome that are transcribed into ribosomal RNA and serve a structural role in ribosomes"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Pseudogenes are DEAD GENES — sequences with strong homology to functional genes but containing mutations (frameshifts, premature stops) that prevent expression of functional protein. They're evolutionary relics. Humans have thousands of pseudogenes (e.g., olfactory receptor pseudogenes). They're important evidence of evolution (shared pseudogenes in related species = common ancestor had a functional copy). | **Wrong E:** Short dispersed repetitive sequences that produce ribosomal RNA describe SINE elements or rDNA repeats, not pseudogenes — pseudogenes are specifically non-functional gene-like sequences with recognizable homology to functional protein-coding genes, and they do not produce ribosomal RNA or contribute to ribosome structure.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following CORRECTLY matches each regulatory mechanism with its level of eukaryotic gene expression, with ALL four pairs correct?",
      "choices": [
        "DNA methylation → pre-transcriptional; transcription factor binding → transcriptional; miRNA degradation of mRNA → post-transcriptional; ubiquitin-mediated protein degradation → post-translational",
        "DNA methylation → transcriptional; transcription factor binding → pre-transcriptional; miRNA → post-translational; ubiquitination → post-transcriptional",
        "DNA methylation → post-transcriptional; transcription factor binding → transcriptional; miRNA → pre-transcriptional; ubiquitination → post-translational",
        "DNA methylation → pre-transcriptional; transcription factor binding → post-transcriptional; miRNA → transcriptional; ubiquitination → post-translational",
        "DNA methylation → pre-transcriptional; transcription factor binding → transcriptional; miRNA → post-translational; ubiquitination → post-transcriptional"
      ],
      "answer": 0,
      "why": "&#9989; **A.** All four pairs are correct: DNA methylation condenses chromatin BEFORE transcription begins (pre-transcriptional) ✓; transcription factors bind promoters/enhancers to control RNA polymerase DURING transcription (transcriptional) ✓; miRNA binds to mRNA AFTER transcription to promote degradation or block translation (post-transcriptional) ✓; ubiquitin tags proteins for proteasomal degradation AFTER translation (post-translational) ✓. | B fails: methylation acts pre-transcriptionally (not transcriptionally) and TF binding is transcriptional (not pre-transcriptional). | C fails: methylation is pre-transcriptional, not post-transcriptional; miRNA acts post-transcriptionally, not pre-transcriptionally. | D fails: TF binding is transcriptional (not post-transcriptional); miRNA is post-transcriptional (not transcriptional). | E fails: miRNA acts post-transcriptionally (degrades/blocks mRNA), not post-translationally; ubiquitination is post-translational, not post-transcriptional.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following statements about eukaryotic genome structure are TRUE? (I) Approximately 1.5% of the human genome encodes protein. (II) Mobile genetic elements (transposons) make up roughly 45% of the human genome. (III) Genome size correlates positively with organismal complexity. (IV) Pseudogenes are non-functional relics of gene duplication or retrotransposition.",
      "choices": [
        "I and IV only",
        "I, II, and III",
        "I, II, and IV only",
        "All four",
        "II and IV only"
      ],
      "answer": 2,
      "why": "&#9989; **C. I, II, and IV only.** Verify each: I ✓ — only ~1.5% of the ~3 billion base-pair human genome codes for protein; the rest is introns, regulatory sequences, repetitive elements, and non-coding DNA. II ✓ — transposable elements (SINEs, LINEs, DNA transposons, retroviral remnants) collectively account for ~45% of the human genome by sequence. III is FALSE — this is the C-value paradox: genome size does NOT correlate with organismal complexity; onions have larger genomes than humans, and many salamanders dwarf mammals in genome size. IV ✓ — pseudogenes arise through gene duplication (one copy accumulates disabling mutations) or retrotransposition (reverse-transcribed mRNA re-inserted without regulatory sequences) and are evolutionary fossils.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following correctly describes the step-by-step mechanism by which DNA methylation silences a gene?",
      "choices": [
        "Methyltransferase adds methyl groups to cytosines at CpG islands in the promoter region → methyl-CpG-binding proteins recruit histone deacetylases → histones deacetylated → chromatin condenses into heterochromatin → RNA polymerase and transcription factors cannot access the promoter → gene is silenced BEFORE transcription begins",
        "Methyltransferase adds methyl groups to cytosines in the coding region → methylated mRNA is exported from the nucleus → ribosome cannot translate methylated mRNA → protein is not produced → gene is silenced POST-transcriptionally",
        "Methyltransferase adds methyl groups to cytosines at the promoter → methylation directly cleaves the mRNA transcript → gene is silenced POST-transcriptionally via mRNA degradation",
        "Methyltransferase adds methyl groups to cytosines at the promoter → RNA polymerase binds but transcribes a non-coding RNA → the non-coding RNA blocks translation → gene is silenced POST-translationally",
        "Methyltransferase adds methyl groups to histones (not DNA) → histones are displaced from the promoter → chromatin opens → transcription is activated, not silenced"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the correct pre-transcriptional silencing cascade: DNA methylation at CpG promoter islands → chromatin condensation via histone deacetylation → physical inaccessibility → no transcription. | B fails: methylation occurs on DNA at the promoter, not on mRNA; mRNA methylation is a separate regulatory mechanism (m6A), and this description is of a post-transcriptional mechanism, not DNA methylation silencing. | C fails: DNA methylation does not cleave mRNA; it prevents transcription from starting — the mRNA never exists to be cleaved. | D fails: the described mechanism (non-coding RNA blocking translation) describes a post-transcriptional/translational mechanism, not the DNA methylation pathway. | E fails: methylation of histones can have activating OR silencing effects depending on which residue is modified, but DNA methylation at CpG islands is specifically a silencing mechanism, not activation.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Which of the following does NOT correctly describe pseudogenes?",
      "choices": [
        "They share sequence homology with functional paralogous genes in the same genome",
        "They accumulate mutations (frameshifts, premature stop codons) that prevent production of a functional protein",
        "They are currently transcribed and translated into fully functional proteins in most cell types",
        "They serve as evolutionary evidence that an ancestral genome carried a functional version of the gene",
        "Processed pseudogenes arise through retrotransposition of reverse-transcribed mRNA lacking introns and regulatory sequences"
      ],
      "answer": 2,
      "why": "&#9989; **C.** By definition, pseudogenes are NON-FUNCTIONAL — they cannot be translated into fully functional proteins because they contain disabling mutations. Some pseudogenes are transcribed into non-coding RNAs that may have regulatory roles, but they are not translated into functional proteins — that would make them functional genes, not pseudogenes. | A is correct: pseudogenes show clear sequence homology to their functional paralogs — that homology is how they are identified. | B is correct: the accumulated mutations (frameshift insertions/deletions, premature stop codons, splice site mutations) are exactly what render them non-functional. | D is correct: shared pseudogenes between species (e.g., the GULO pseudogene in humans and guinea pigs) are compelling evidence of common ancestry. | E is correct: processed (retro)pseudogenes lack introns and have a poly-A tail — hallmarks of reverse-transcribed mRNA reintegrated into the genome without its original regulatory sequences.",
      "sectionId": "s_genome",
      "chapterId": "ch_s_genetics"
    },
    {
      "prompt": "Alfred Russel Wallace's key contribution to evolutionary biology was:",
      "choices": [
        "Discovering the fossil record and demonstrating that species had gone extinct",
        "Proposing the inheritance of acquired characteristics before Darwin",
        "Independently conceiving natural selection and prompting Darwin to publish by sending him a letter in 1858",
        "Providing the geological evidence of deep time that Darwin needed for evolution to work",
        "Conducting breeding experiments with pea plants that quantified the inheritance of discrete traits and established the laws of segregation and independent assortment"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Wallace independently developed natural selection working in Southeast Asia. His 1858 letter to Darwin describing his theory forced Darwin to act. Darwin had been developing his theory since 1838 but delayed publication. The threat of losing priority prompted the joint Darwin-Wallace presentation to the Linnean Society in 1858 and Darwin's publication of Origin in 1859. | **Wrong E:** Pea plant breeding experiments and the laws of segregation and independent assortment were the contributions of Gregor Mendel (published 1866), not Wallace; Wallace's work was in biogeography and natural history in the Malay Archipelago, not controlled breeding experiments.",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "The 'Great Chain of Being' differs from modern evolutionary theory in which fundamental way?",
      "choices": [
        "It placed humans at the top of a hierarchy, while evolutionary theory considers humans just another branch",
        "It proposed no mechanism for evolutionary change, while Darwin provided natural selection",
        "It proposed that species are FIXED and do not change; it had no concept of common descent, extinction as we know it, or species transforming over time",
        "All of the above — A, B, and C are all correct differences",
        "It differed from evolutionary theory primarily in timescale — the Great Chain of Being accepted gradual species change but believed it occurred over only thousands of years rather than millions"
      ],
      "answer": 3,
      "why": "&#9989; **D.** The Great Chain of Being was a pre-scientific, pre-Darwinian concept. It proposed: (A) humans at top of a hierarchical chain of beings, (B) no evolutionary mechanism — species were fixed in their station, (C) species were static, immutable entities created in their current form. Modern evolutionary theory has all three elements: humans are one branch (not top), natural selection is the mechanism, and species change over time. | **Wrong E:** The Great Chain of Being did not accept gradual species change at any timescale — its defining feature was that species were fixed and immutable entities; it was not a question of timescale but of whether change was possible at all, and the Chain explicitly held that each organism occupied a permanent, divinely assigned rank in a static hierarchy.",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "William Smith's major contribution to evolutionary thought was:",
      "choices": [
        "Proposing that all species shared a common ancestor",
        "Demonstrating that different rock strata contain different fossil assemblages, establishing the reality of extinction and the geological history of life",
        "Proposing uniformitarianism: the idea that present processes explain the geological past",
        "Discovering the first hominin fossils in England",
        "Proposing that organisms acquire characteristics during their lifetime that improve their survival and pass these acquired traits to offspring"
      ],
      "answer": 1,
      "why": "&#9989; **B.** William Smith (1769-1839) was a surveyor who noticed that each rock stratum contained a distinct, characteristic assemblage of fossils. Crucially: organisms in older (deeper) strata no longer existed — they had gone EXTINCT. This established extinction as a geological reality and provided a way to correlate and date rock layers worldwide. Lyell (C) proposed uniformitarianism. | **Wrong E:** The proposal that organisms acquire heritable characteristics during their lifetime (use/disuse inheritance) was Lamarck's contribution, not William Smith's; Smith was a geological surveyor whose work was empirical stratigraphy, not theoretical biology or mechanism-of-inheritance reasoning.",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following correctly identifies the contribution of Alfred Russel Wallace to evolutionary biology, satisfying ALL defining criteria?",
      "choices": [
        "Wallace proposed uniformitarianism — the idea that geological processes acting over deep time provided the temporal framework needed for biological evolution",
        "Wallace used stratigraphy and fossil assemblages to demonstrate that species had gone extinct, establishing the geological reality of species change over time",
        "Wallace independently conceived natural selection while working in Southeast Asia, sent Darwin a letter describing the theory in 1858, and thereby prompted Darwin to finally publish",
        "Wallace proposed the inheritance of acquired characteristics, providing the first serious mechanistic framework for evolutionary change before Darwin",
        "Wallace conducted the Beagle voyage observations of finch beak variation that provided Darwin with the empirical evidence for natural selection"
      ],
      "answer": 2,
      "why": "&#9989; **C.** All three criteria met: independently conceived natural selection ✓, 1858 letter to Darwin ✓, prompted Darwin to publish ✓. | A fails: uniformitarianism was Charles Lyell's contribution, not Wallace's. | B fails: stratigraphy and fossil layer dating was William Smith's contribution. | D fails: inheritance of acquired characteristics (use/disuse) was Lamarck's theory; Wallace proposed natural selection, not Lamarckian inheritance. | E fails: the Beagle voyage was Darwin's own expedition; Wallace worked independently in the Malay Archipelago (Southeast Asia), not on the Beagle.",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following historical figure–contribution pairs are CORRECTLY matched? (I) Lamarck → inheritance of acquired characteristics (use/disuse). (II) Charles Lyell → uniformitarianism and geological deep time. (III) William Smith → proposed natural selection before Darwin. (IV) Darwin → variation + heritability + differential reproduction = natural selection.",
      "choices": [
        "I and II only",
        "II and IV only",
        "I, II, and IV",
        "I, II, and IV only",
        "All four"
      ],
      "answer": 3,
      "why": "&#9989; **D. I, II, and IV only.** Verify each: I ✓ — Lamarck's theory of evolution centered on the inheritance of traits acquired during an organism's lifetime (e.g., giraffes stretching necks → longer-necked offspring). II ✓ — Lyell's Principles of Geology argued that slow, uniform geological processes acting over vast timescales shaped Earth's surface; this deep-time framework was essential for Darwin. III is FALSE — William Smith developed stratigraphy (using fossil assemblages to date and correlate rock layers); he did NOT propose natural selection. Natural selection was independently conceived by Darwin and Wallace. IV ✓ — Darwin's theory requires all three components: heritable phenotypic variation among individuals, and that variation affects survival/reproduction (differential fitness).",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following correctly describes the chain of observations and reasoning that led Darwin to formulate the theory of natural selection?",
      "choices": [
        "Beagle voyage → Darwin observes geographic variation in finches and tortoises → Lyell's geology provides deep time → Malthus's essay on population pressure → Darwin reasons: variation + heritable + differential survival in limited resources = natural selection; develops theory ~1838, publishes 1859 after Wallace's 1858 letter",
        "Wallace's Malay Archipelago observations → Wallace shares results with Darwin → Darwin combines Wallace's biogeography with Lyell's geology → Darwin reasons that species change via natural selection → Darwin publishes immediately in 1844",
        "Beagle voyage → Darwin observes variation → William Smith's stratigraphy provides the deep time framework Darwin needed → Darwin formulates natural selection → publishes Origin in 1859 after Smith urges him to publish",
        "Darwin reads Lamarck → rejects use/disuse but adopts the idea that species change over time → reads Malthus → formulates natural selection → Wallace's 1858 letter confirms Darwin's theory but does not prompt publication",
        "Beagle voyage → Darwin observes finch variation → Lyell's geology provides deep time → Darwin formulates natural selection in 1859 just before Wallace independently arrives at the same theory"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This correctly attributes: Beagle voyage observations (empirical variation data), Lyell's geology (deep time), Malthus's population essay (resource limitation driving competition), and Wallace's 1858 letter as the publication trigger. Darwin developed the theory ~1838 but delayed ~20 years. | B fails: Wallace did not share results with Darwin before the 1858 letter; Darwin's theory developed independently from his own Beagle observations, not from Wallace. | C fails: deep time came from Lyell (uniformitarianism), not William Smith (stratigraphy); Smith provided fossil layering, not temporal depth. | D fails: Wallace's 1858 letter absolutely DID prompt publication — this is the central exam fact about Wallace's role. | E fails: Darwin formulated natural selection around 1838 (not 1859), and Wallace arrived at the theory independently years before 1859 (his 1858 letter proves this).",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following does NOT correctly describe the 'Great Chain of Being'?",
      "choices": [
        "It arranged all living things in a fixed, hierarchical order from lowest to highest forms",
        "It proposed that species undergo gradual change over millions of years driven by environmental pressure",
        "It placed humans at or near the top of the hierarchy of living things",
        "It conceived of species as fixed, immutable entities that do not transform into other species",
        "It was a pre-Darwinian concept rooted in Aristotelian natural philosophy, superseded by evolutionary thinking"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The Great Chain of Being explicitly held that species are FIXED and IMMUTABLE — it proposed NO gradual change over time and NO transformation of species. Gradual change driven by environmental pressure is a description of evolutionary thinking (closer to Lamarck or Darwin), which is precisely what the Great Chain of Being contradicts. | A is correct: the Scala Naturae (Great Chain) arranged organisms in a strict linear hierarchy from minerals to angels. | C is correct: humans occupied a privileged position near the top of the earthly chain. | D is correct: fixity of species is the defining feature that evolutionary theory overturned. | E is correct: the concept traces to Aristotle and was dominant in European natural philosophy until the 18th–19th century.",
      "sectionId": "s_key_figures",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following CORRECTLY characterizes a scientific theory, satisfying ALL criteria: (1) supported by a large body of evidence, (2) generates testable hypotheses, (3) is more certain than a single hypothesis, (4) explains a broad phenomenon?",
      "choices": [
        "A scientific theory is a tentative explanation for a single observation that has not yet been tested — essentially a well-worded hypothesis waiting for experimental confirmation",
        "A scientific theory is less certain than a hypothesis because it makes broader claims that are harder to test directly and therefore more likely to contain errors",
        "A scientific theory is a mathematical model that exactly predicts all outcomes of all experiments in its domain — a theory that fails even one prediction is immediately discarded",
        "A scientific theory is a well-substantiated explanation of a broad phenomenon that has withstood extensive testing and generates many testable hypotheses",
        "A scientific theory is equivalent to a scientific law — both describe phenomena with equal certainty and are interchangeable terms in modern biology"
      ],
      "answer": 3,
      "why": "&#9989; **D.** All four criteria are satisfied: large body of evidence &#10003;, generates testable hypotheses &#10003;, more certain than a single hypothesis &#10003;, explains a broad phenomenon &#10003;. | **A fails:** this describes a hypothesis, not a theory; theories have already been extensively tested across many lines of evidence. | **B fails:** this inverts the relationship — theories are MORE supported and MORE certain than individual hypotheses, not less. | **C fails:** scientific theories are not discarded upon a single anomalous result; anomalies prompt refinement and further investigation, not immediate abandonment (see Kuhnian philosophy of science). | **E fails:** theories and laws are not interchangeable; a scientific law describes a pattern (e.g., law of gravity describes what happens), while a theory explains the mechanism (e.g., general relativity explains why gravity works as it does).",
      "sectionId": "s_sci_method",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which statements correctly describe the relationship between hypotheses and theories in science? (I) A hypothesis is a tentative, testable explanation for a specific observation. (II) A scientific theory is less certain than a hypothesis because it covers more phenomena. (III) Theories generate many testable hypotheses. (IV) Evolution is a scientific theory supported by genetics, paleontology, comparative anatomy, and direct observation.",
      "choices": [
        "I and III only",
        "I and IV only",
        "I, III, and IV only",
        "I, II, and IV",
        "All four"
      ],
      "answer": 2,
      "why": "&#9989; **C. I, III, and IV only.** Verify each: I &#10003; — a hypothesis is provisional, falsifiable, and addresses a specific observation; this is the standard definition. II is FALSE — a scientific theory is MORE certain than a hypothesis, not less; theories have survived far more extensive testing. Breadth of coverage does not reduce certainty — it increases it because more lines of independent evidence converge. III &#10003; — a hallmark of a good scientific theory is that it generates many new, independently testable predictions (hypotheses). IV &#10003; — the theory of evolution is supported by multiple independent fields: molecular genetics (shared DNA sequences), paleontology (fossil progression), comparative anatomy (homologous structures), biogeography (species distribution), and direct experimental observation (e.g., antibiotic resistance, Grants' finches). | **A fails:** omits IV which is true. | **B fails:** omits III which is true. | **D fails:** includes II which is false. | **E fails:** includes II which is false.",
      "sectionId": "s_sci_method",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "A scientist observes that bacteria in penicillin-treated plates die while a small number survive. Which of the following correctly describes the step-by-step scientific reasoning process applied to this observation?",
      "choices": [
        "(1) Observation: some bacteria survive penicillin; (2) Hypothesis: pre-existing random mutations confer resistance; (3) Prediction: if hypothesis is correct, survivors' offspring should also be resistant; (4) Experiment: culture offspring and test penicillin sensitivity; (5) Result consistent with prediction: hypothesis is supported; (6) After extensive independent replication, this becomes part of the theory of antibiotic resistance evolution",
        "(1) Observation: some bacteria survive penicillin; (2) Theory: bacteria acquired resistance in direct response to penicillin exposure; (3) Prediction: removing penicillin will cause resistance to disappear in one generation; (4) This theory is immediately published because it explains the observation",
        "(1) Observation: some bacteria survive penicillin; (2) Hypothesis: surviving bacteria are a different species; (3) Prediction: survivors will not interbreed with susceptibles; (4) Experiment confirms this; (5) Theory: penicillin creates new species, which is now a proven scientific law",
        "(1) Observation: some bacteria survive penicillin; (2) Hypothesis: resistance is heritable; (3) Experiment: sequence the genome; (4) Result: resistance gene found; (5) Hypothesis is now a theory because one experiment confirmed it; (6) Theory is published",
        "(1) Observation: some bacteria survive penicillin; (2) The observation itself constitutes a scientific theory because it is based on empirical data; (3) No further testing is required once empirical data exist"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This correctly follows the scientific method: observation &#8594; hypothesis &#8594; prediction &#8594; experiment &#8594; result &#8594; iterative support across replications &#8594; elevation to theoretical framework. | **B fails:** jumping directly from observation to \"theory\" without testing is not science; additionally, \"bacteria acquired resistance in response to penicillin\" is the Lamarckian hypothesis, which has been falsified (Luria-Delbr&uuml;ck experiment 1943 demonstrated mutations predate drug exposure). | **C fails:** the prediction does not follow logically; surviving bacteria are not a different species; and a single experiment does not confirm a \"theory\" or produce a \"scientific law.\" | **D fails:** one confirming experiment does not elevate a hypothesis to a theory; theories require extensive independent replication and survive challenges from multiple angles. | **E fails:** an observation alone is not a theory; a theory is an explanatory framework, not a data point.",
      "sectionId": "s_sci_method",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "Which of the following does NOT correctly describe evolution as a scientific theory?",
      "choices": [
        "The theory of evolution generates many testable hypotheses, including predictions about molecular sequence divergence, fossil succession, and the geographic distribution of related species",
        "The theory of evolution is supported by multiple independent lines of evidence — genetics, paleontology, comparative anatomy, biogeography, and direct experimental observation",
        "The theory of evolution is called a \"theory\" in the scientific sense, meaning it is an explanatory framework with a high level of evidential support, not a guess",
        "Evolution is called a \"theory\" because scientists are still unsure whether evolution actually occurs — the label reflects ongoing scientific uncertainty about the basic phenomenon",
        "As a scientific theory, evolution can in principle be falsified — a discovery of rabbit fossils in Precambrian rock strata, for example, would be strong evidence against it"
      ],
      "answer": 3,
      "why": "&#9989; **D.** Scientists are NOT unsure whether evolution occurs — this is one of the most strongly evidenced conclusions in all of science. Evolution is called a theory in the SCIENTIFIC sense: a well-substantiated explanatory framework. The label \"theory\" reflects the highest confidence level in science, not uncertainty. Confusion arises only from conflating the everyday and scientific uses of the word \"theory.\" | **A is correct:** the theory of evolution generates hundreds of independently testable predictions that have been verified. | **B is correct:** convergent support from multiple independent fields is precisely what elevates evolution to the status of scientific theory. | **C is correct:** this states the key point directly — scientific \"theory\" &#8800; everyday \"guess.\" | **E is correct:** evolution is falsifiable (e.g., J.B.S. Haldane's famous \"fossil rabbits in the Precambrian\" response); falsifiability is a hallmark of scientific theories.",
      "sectionId": "s_sci_method",
      "chapterId": "ch_s_hist"
    },
    {
      "prompt": "The fact that Pax6 gene activates eye development in both Drosophila (flies) and mice, despite these species having very different eye structures, BEST demonstrates:",
      "choices": [
        "Convergent evolution — both independently evolved Pax6 for eye development",
        "Conservation of a developmental genetic toolkit (genetic module) across vastly different animal lineages, with different downstream targets producing different eye types",
        "That the same gene can only produce one type of eye, constraining evolution",
        "Horizontal gene transfer of Pax6 between the insect and vertebrate lineages",
        "Neofunctionalization — Pax6 duplicated in a common ancestor and each copy evolved a different eye-development role in each lineage"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Pax6 is a MASTER REGULATORY GENE conserved across bilaterian animals. The same gene triggers eye development in flies (compound eye) and mice (camera eye) — very different end structures produced by the same upstream trigger. This shows the conserved developmental toolkit: the 'switch' (Pax6) is ancient and shared, but what the switch turns on (downstream targets) varies between lineages. | **Wrong E:** Pax6 is a single ancestral gene conserved by descent, not a product of lineage-specific duplication; its conservation across bilaterians reflects shared ancestry of the gene, not neofunctionalization of separate copies.",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Heterochrony in evolutionary developmental biology refers to:",
      "choices": [
        "The independent evolution of similar traits in unrelated lineages",
        "Changes in the TIMING or RATE of developmental gene expression that produce phenotypic changes without changing the genes' coding sequences",
        "The duplication of genes that allows new functions to evolve",
        "The movement of regulatory elements to new chromosomal positions",
        "Mutations in the protein-coding exons of Hox genes that alter the amino acid sequence of homeodomain proteins"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Heterochrony = hetero (different) + chronos (time). Changes in WHEN developmental events occur. Example: neoteny (retaining juvenile features into adulthood). Paedomorphosis in axolotls: retain larval (juvenile) features permanently due to heterochrony in thyroid hormone signaling. Same genes, different timing = radically different phenotype. | **Wrong E:** Coding-sequence mutations in Hox genes describe a different evo-devo mechanism (changes to the protein itself); heterochrony specifically involves changes in expression timing and rate, not changes to the gene's protein product.",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which of the following correctly characterizes Hox genes, satisfying ALL conditions: conserved across animals, define body axis identity, changes produce major morphological differences, found in both insects and vertebrates?",
      "choices": [
        "They are found only in vertebrates and define segment identity along the anterior-posterior axis",
        "They define anterior-posterior axis identity, are highly conserved, and changes produce major body plan differences in both insects and vertebrates",
        "They control eye development specifically and are conserved only in chordates",
        "They are protein-coding sequences that define cell type, not body segment identity",
        "They regulate timing of development via histone modifications only"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Hox genes satisfy all four conditions simultaneously: they are found in insects AND vertebrates, they define anterior-posterior axis segment identity, they are deeply conserved across bilaterians, and changes in Hox expression produce large body-plan differences. | **Wrong A:** Hox genes are found in all bilaterians including insects, not vertebrates only. | **Wrong C:** Pax6 controls eye development, not Hox genes; Hox genes define segment identity along the body axis. | **Wrong D:** Hox genes are transcription factors defining segment identity, not cell type per se. | **Wrong E:** Heterochrony (not Hox genes) involves timing changes; Hox genes work by defining positional identity.",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which of the following statements about evolutionary developmental biology (evo devo) are TRUE? (I) Regulatory mutations produce larger morphological changes than coding mutations per base-pair change (II) Pax6 controls eye development in both Drosophila and mice despite different eye structures (III) Heterochrony changes the coding sequence of genes (IV) Protein promiscuity allows new functions to evolve while retaining old ones",
      "choices": [
        "I and II only",
        "II and IV only",
        "I, II, and III",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I, II, and IV are true. Regulatory mutations (I) can redirect entire developmental programs without changing protein structure. Pax6 (II) is the classic conserved master regulator of eye development across bilaterians. Protein promiscuity (IV) describes how proteins gain new functions while retaining originals. | **Wrong A:** Correct as far as it goes but misses IV, which is also true. | **Wrong B:** Misses I, which is also true. | **Wrong C:** III is FALSE — heterochrony changes TIMING of expression, not the coding sequence itself. | **Wrong E:** III is false, ruling out \"all of the above.\"",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "A researcher discovers that expressing Pax6 ectopically in a fly's leg produces ectopic eyes. The correct step-by-step interpretation is:",
      "choices": [
        "Pax6 is a master regulatory switch that activates a downstream eye-development program; it does not encode structural eye components itself, but triggers a cascade of tissue-appropriate downstream target genes",
        "Pax6 directly encodes the photoreceptor proteins, so wherever it is expressed, photoreceptors self-assemble regardless of tissue context",
        "Pax6 only functions as an eye regulator in vertebrates; in flies it activates a leg-patterning program that happens to produce eye-like structures by coincidence",
        "Pax6 requires a specific chromatin context found only in eye imaginal discs; the ectopic eyes are artifacts of overexpression, not genuine developmental activation",
        "The result shows horizontal gene transfer of Pax6 from vertebrates into Drosophila, explaining why the fly can produce vertebrate-type eyes"
      ],
      "answer": 0,
      "why": "&#9989; **A.** Pax6 is a master transcription factor (regulatory switch) that triggers a cascade of downstream target genes appropriate to the local tissue — it does not itself encode structural photoreceptor proteins. | **Wrong B:** Pax6 encodes a transcription factor, not photoreceptor structural proteins; the downstream cascade builds the eye. | **Wrong C:** Pax6 is functionally conserved across insects and vertebrates — the classic result is that mouse Pax6 can induce fly eyes and vice versa. | **Wrong D:** Ectopic expression studies are well-validated; the ectopic eyes are genuine activation of the eye program, not artifacts. | **Wrong E:** Pax6 conservation is due to deep homology from a common ancestor, not horizontal gene transfer.",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which of the following does NOT accurately describe a constraint on complex trait evolution?",
      "choices": [
        "Historical contingency limits which structures are available as starting material for new traits",
        "Each evolutionary step must provide a fitness advantage for selection to maintain it",
        "Given sufficient time, natural selection can design optimal traits from scratch regardless of ancestral history",
        "Developmental constraints mean that some phenotypic changes require coordinated changes in multiple genes",
        "The human eye's blind spot persists because evolution cannot redesign the retina from scratch"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Evolution cannot design from scratch — it is constrained by historical contingency (what existed before). Selection can only modify existing structures; it cannot start over with an optimal design. The human eye's blind spot persists because of this constraint. | **Wrong A:** This accurately describes historical contingency as a real constraint. | **Wrong B:** This accurately describes the requirement for incremental fitness advantages. | **Wrong D:** Developmental constraints are real and well-documented. | **Wrong E:** This correctly describes why the human eye retains its inverted retina despite the octopus having a superior non-inverted design.",
      "sectionId": "s_evoeye",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "The wings of bats and insects are BOTH used for flight. Regarding their evolutionary relationship, which is CORRECT?",
      "choices": [
        "They are homologous — both evolved from a common ancestor with rudimentary wings",
        "They are analogous (convergent) — flight evolved independently in each lineage using completely different developmental mechanisms; the structures are not inherited from a shared winged ancestor",
        "They are homoplasious only in function, not structure — all animal wings are structurally identical",
        "They represent parallel evolution because both lineages used the same genetic changes",
        "They are homologous because both are dorsal appendages that use the same Hox gene expression domains for positional identity along the body axis"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Bat wings and insect wings are ANALOGOUS (convergent). They evolved independently. Bat wings are modified tetrapod forelimbs (bone + membrane). Insect wings are outgrowths of the thoracic wall (exoskeleton-derived). Completely different developmental origins. Same function (flight) produced by natural selection in separate lineages. If the same gene pathway (e.g., wingless/Wnt) is involved, it would be parallel, but the structures themselves are non-homologous. | **Wrong E:** Shared use of Hox genes for broad positional identity does not establish homology of the wing structures themselves; the relevant criterion is whether the wing structures are inherited from a common ancestral wing, which they are not.",
      "sectionId": "s_homoana",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which pair of features is HOMOLOGOUS, satisfying ALL criteria: same developmental origin, inherited from a common ancestor, and may differ in function?",
      "choices": [
        "Bat wing and insect wing — both used for flight, both derived from dorsal body wall outgrowths",
        "Human arm and bat wing — same tetrapod bone arrangement (humerus, radius, ulna), inherited from a common tetrapod ancestor, different functions (manipulation vs. flight)",
        "Fish fin and dolphin flipper — both used for aquatic locomotion, shaped by the same selective pressures",
        "Bird wing and butterfly wing — both used for flight in vertebrates and invertebrates respectively",
        "Shark dorsal fin and tuna dorsal fin — same position, same stabilizing function, same ancestor"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Human arm and bat wing satisfy all three criteria: same developmental origin (tetrapod forelimb bones), inherited from a common tetrapod ancestor, but used for different functions. | **Wrong A:** Bat and insect wings are analogous — insect wings are exoskeletal outgrowths, not modified forelimbs; completely different developmental origins. | **Wrong C:** Fish fins and dolphin flippers share some ancestry but the criterion here is same function driving the comparison — this describes convergent aquatic adaptation (analogy) as the basis of similarity. | **Wrong D:** Bird wings (modified forelimbs) and butterfly wings (exoskeletal) have entirely different developmental origins — analogous. | **Wrong E:** Shark and tuna are not closely related tetrapods; their dorsal fins evolved convergently for stabilization.",
      "sectionId": "s_homoana",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which statements correctly distinguish homology from analogy? (I) Homologous structures share developmental origin; analogous structures do not (II) Analogous traits mislead phylogenetic analysis; homologous traits support it (III) Parallel evolution in closely related lineages produces homologous structures (IV) Convergent evolution can produce analogous structures that look superficially similar",
      "choices": [
        "I and IV only",
        "I, II, and III",
        "II, III, and IV",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I, II, and IV are correct. Shared developmental origin defines homology (I). Analogous traits used as phylogenetic characters create false groupings — homoplasy misleads analysis (II). Convergent evolution independently produces similar-looking structures with different developmental origins — analogous (IV). | **Wrong A:** Misses II, which is also true. | **Wrong B:** III is FALSE — parallel evolution in related lineages still means the similarity arose independently (the structures are not inherited from a shared structured ancestor), so they are technically homoplasious, not homologous in the strict sense. | **Wrong C:** III is false; see above. | **Wrong E:** III is false, ruling out all of the above.",
      "sectionId": "s_homoana",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which step-by-step process correctly describes how convergent evolution produces analogous traits?",
      "choices": [
        "(1) Same selective pressure acts independently in two lineages → (2) Each lineage evolves toward similar phenotype via different genetic/developmental pathways → (3) Similar appearance results but molecular basis differs → analogous structure",
        "(1) Two lineages share a common ancestor with the trait → (2) Each lineage independently modifies the inherited structure → (3) Similar appearance results from shared ancestry → homologous structure with analogous function",
        "(1) Same selective pressure acts in two lineages → (2) Both lineages use the exact same gene mutations → (3) Identical developmental pathways produce identical structures → parallel evolution creating homologs",
        "(1) Gene flow between lineages spreads adaptive alleles → (2) Both lineages acquire the same developmental pathway → (3) Similar phenotype results from shared genetic mechanism → analogous by gene transfer",
        "(1) Random genetic drift in isolated populations → (2) Chance mutations produce similar phenotypes → (3) Natural selection maintains the similarity → analogous by neutral evolution"
      ],
      "answer": 0,
      "why": "&#9989; **A.** Convergent evolution: same selective pressure (e.g., aquatic locomotion) independently shapes two unrelated lineages toward similar phenotypes via different genetic routes — the result looks similar but the developmental and molecular basis differs. | **Wrong B:** Describes homology, not analogy — sharing a common ancestor with the trait is the definition of homology. | **Wrong C:** If both lineages use identical gene mutations, that is parallel evolution, not convergent; and the resulting structures would technically be parallelous, not analogous. | **Wrong D:** Gene flow between lineages producing similarity is neither convergence nor analogy — it is introgression. | **Wrong E:** Neutral drift producing similar phenotypes that selection then maintains is extremely unlikely and not the standard definition of convergent evolution.",
      "sectionId": "s_homoana",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "Which does NOT constitute evidence for homology between the human arm and whale flipper?",
      "choices": [
        "Both structures contain the same set of bones: humerus, radius, ulna, carpals, and phalanges",
        "Both develop from the same embryonic limb bud tissue via the same developmental pathway",
        "Both serve a locomotor function — the arm for manipulation/swimming and the flipper for steering in water",
        "Both are inherited from the same common tetrapod ancestor",
        "The same Hox gene expression patterns govern fore-limb development in both humans and whales"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Having the same function is evidence of analogy (convergence), NOT homology. Homology is established by shared developmental origin, same underlying bone structure, and inheritance from a common ancestor — regardless of function. The whale flipper and human arm differ in function but are still homologous. | **Wrong A:** Shared bone arrangement is strong evidence of homology. | **Wrong B:** Same embryonic developmental origin directly supports homology. | **Wrong D:** Common ancestry is the definition of homology. | **Wrong E:** Conserved Hox patterning supports common developmental origin and thus homology.",
      "sectionId": "s_homoana",
      "chapterId": "ch_s_ch10"
    },
    {
      "prompt": "In a New Zealand lake, snails in parasite-rich habitats are mostly sexual, while snails in parasite-free habitats are mostly asexual. This pattern BEST supports:",
      "choices": [
        "Muller's Ratchet — asexual snails accumulate mutations more quickly in parasite-free environments",
        "The Red Queen Hypothesis — sexual reproduction generates rare genotypes that parasites haven't evolved to exploit, providing an advantage specifically where parasites are present",
        "The twofold cost of sex — sexual snails are outcompeting asexual snails in all environments",
        "Kin selection — parasites prefer genetically diverse hosts because they can infect more relatives",
        "Genetic drift — the small population sizes in parasite-rich habitats cause sexual genotypes to fix by chance rather than through selection"
      ],
      "answer": 1,
      "why": "&#9989; **B.** This is the key study supporting the Red Queen hypothesis. Where parasites are COMMON: common genotypes are exploited → sexual reproduction generates rare genotypes → sex is advantageous → sexual individuals persist. Where parasites are RARE: no frequency-dependent advantage to rare genotypes → asexual reproduction (no twofold cost) wins. The geographic pattern exactly matches what Red Queen predicts. | **Wrong E:** The consistent geographic pattern correlating sexual reproduction with parasite richness across multiple lakes cannot be explained by random drift; the systematic association with parasite load requires a selective explanation.",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Muller's Ratchet describes the disadvantage of asexual reproduction because:",
      "choices": [
        "Asexual organisms cannot combine beneficial mutations that occur in different individuals",
        "Asexual populations irreversibly accumulate deleterious mutations — the genome with the fewest mutations can only be lost, never restored, without recombination",
        "Asexual reproduction is less energetically efficient than sexual reproduction",
        "Both A and B are correct descriptions of Muller's Ratchet",
        "Asexual populations are more susceptible to Muller's Ratchet because meiosis introduces more replication errors than mitosis does"
      ],
      "answer": 3,
      "why": "&#9989; **D.** Muller's Ratchet has two related consequences: (1) it's impossible to reassemble a low-mutation genome without recombination (the &ldquo;ratchet&rdquo; only clicks toward more mutations), AND (2) beneficial mutations that occur in different individuals in an asexual lineage cannot be combined — they must compete (clonal interference). Sex solves both by recombination, which can remove deleterious mutations AND combine beneficial ones. | **Wrong E:** Muller's Ratchet affects ASEXUAL lineages, not sexual ones; it is caused by the absence of recombination in asexual reproduction, not by higher mutation rates from mitosis versus meiosis.",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which hypothesis predicts that sexual reproduction is advantageous SPECIFICALLY in environments with high parasite diversity, satisfying ALL criteria: frequency-dependent selection, parasites tracking common genotypes, rare genotypes favored?",
      "choices": [
        "Muller's Ratchet — parasites accelerate mutation accumulation in asexual lineages, making sex advantageous",
        "Clonal interference hypothesis — parasites prevent beneficial mutations from spreading in asexual populations",
        "Red Queen hypothesis — parasites evolve to exploit common host genotypes; sex generates rare genotypes that parasites cannot yet exploit, providing frequency-dependent advantage specifically where parasites are abundant",
        "Kin selection hypothesis — sexual reproduction reduces relatedness among siblings, decreasing competition",
        "Muller's Ratchet and Red Queen together — both are required and neither alone explains parasite-rich advantage"
      ],
      "answer": 2,
      "why": "&#9989; **C.** The Red Queen satisfies all three criteria: it is frequency-dependent (common genotypes become targets), parasites track the most prevalent host genotypes, and rare novel genotypes produced by sex escape current parasite pressure. The advantage is specifically tied to parasite richness. | **Wrong A:** Muller's Ratchet is about irreversible mutation accumulation — it predicts a general advantage of sex not specifically tied to parasite diversity. | **Wrong B:** Clonal interference is about competing beneficial mutations, not parasites. | **Wrong D:** Kin selection concerns relatedness and altruism, not parasite resistance. | **Wrong E:** Both mechanisms contribute to maintaining sex, but the Red Queen alone satisfies the specific \"parasite diversity\" criterion.",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which benefits of sexual reproduction correctly oppose the twofold cost? (I) Combining beneficial mutations from different individuals via recombination (II) Preventing Muller's Ratchet accumulation of deleterious mutations (III) Reducing the metabolic costs of meiosis compared to mitosis (IV) Generating rare host genotypes that parasites cannot yet exploit",
      "choices": [
        "I and II only",
        "II and IV only",
        "I, II, and III",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (combining beneficial mutations), II (halting Muller's Ratchet), and IV (Red Queen — generating rare genotypes) are all genuine benefits that offset the twofold cost. | **Wrong A:** Misses IV, which is also a valid benefit. | **Wrong B:** Misses I, which is also a valid benefit. | **Wrong C:** III is FALSE — meiosis is metabolically MORE costly than mitosis, not less; the \"twofold cost\" partly reflects the energetic investment in producing males who do not directly reproduce. | **Wrong E:** III is false, eliminating \"all of the above.\"",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism by which Muller's Ratchet degrades asexual lineages?",
      "choices": [
        "(1) Deleterious mutations arise randomly each generation; (2) The class of genomes with the fewest mutations can only be lost — it cannot be reconstructed without recombination; (3) Each generation the minimum mutation load irreversibly increases; (4) Fitness declines over time in asexual lineages",
        "(1) Deleterious mutations arise randomly; (2) Natural selection removes all mutant genomes each generation; (3) Occasional back-mutations restore low-mutation genomes; (4) The ratchet can reverse if the environment changes, restoring fitness in asexual lineages",
        "(1) Deleterious mutations arise; (2) Sexual recombination reassembles low-mutation genomes each generation; (3) The ratchet cannot click forward because sex prevents accumulation; (4) Only asexual lineages avoid this ratchet because mitosis is more accurate",
        "(1) Deleterious mutations arise; (2) The ratchet only applies to RNA viruses with high mutation rates; (3) DNA-based asexual organisms are immune; (4) Sexual organisms are more susceptible to Muller's Ratchet because meiosis introduces more errors",
        "(1) Deleterious mutations arise; (2) They accumulate only in males; (3) Females purge deleterious alleles each generation via recombination in mitosis; (4) Sex is only beneficial for males in Muller's Ratchet framework"
      ],
      "answer": 0,
      "why": "&#9989; **A.** Muller's Ratchet: the lowest-mutation genome class is lost stochastically each generation (finite population drift) and cannot be reconstructed without recombination — so the minimum load ratchets irreversibly upward. | **Wrong B:** The ratchet specifically CANNOT reverse without recombination; back-mutations are too rare to counteract forward mutation accumulation. | **Wrong C:** Inverts the logic — sex is the SOLUTION to the ratchet, not the cause; asexual lineages are the ones that suffer. | **Wrong D:** Muller's Ratchet applies to all asexual organisms with finite population sizes, not just RNA viruses. | **Wrong E:** The ratchet affects the whole genome, not just males; recombination in meiosis (not mitosis) repairs it.",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which does NOT represent a cost of asexual reproduction?",
      "choices": [
        "Beneficial mutations arising in different individuals cannot be combined in the same offspring (clonal interference)",
        "It eliminates the need for meiosis, saving metabolic energy relative to sexual reproduction",
        "Deleterious mutations accumulate irreversibly via Muller's Ratchet",
        "Common asexual genotypes become targets for parasite adaptation (Red Queen disadvantage)",
        "All offspring are genetically identical to the parent, reducing phenotypic diversity across sibling competition"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Eliminating meiosis is an ADVANTAGE of asexual reproduction, not a cost — it saves the metabolic investment in meiosis and avoids the twofold cost of males. This is precisely why asexual mutants would spread in a sexual population if benefits of sex didn't outweigh it. | **Wrong A:** Clonal interference is a genuine cost of asexual reproduction. | **Wrong C:** Muller's Ratchet is a genuine cost. | **Wrong D:** Red Queen disadvantage for common genotypes is a genuine cost. | **Wrong E:** Reduced diversity and increased sibling competition is a genuine cost of clonal reproduction.",
      "sectionId": "s_whysex",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "A species of fish has females that produce millions of tiny eggs and males that produce far fewer, larger sperm with additional nutrients. According to anisogamy theory, which prediction is MOST likely correct?",
      "choices": [
        "Males will be choosy about mates and females will compete for access to males (because males invest more per gamete)",
        "Both sexes will be equally choosy because both invest energetically in their gametes",
        "Females will be choosy and males will compete, following the standard pattern of anisogamy driving sexual selection",
        "There will be no sexual selection because both sexes are investing comparably in reproduction",
        "Females will evolve larger body size and brighter coloration while males remain drab, regardless of gamete investment, because sexual dimorphism is always expressed in the female sex"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is a REVERSAL of standard anisogamy predictions — when males invest MORE per gamete (fewer, larger, nutrient-rich sperm), the standard Bateman gradient is flipped. Males become the limiting resource → females compete for access to males, and males become choosy. This is called sex-role reversal. The example tests whether you understand that choosiness follows from INVESTMENT per gamete, not from sex per se. | **Wrong E:** Elaborate ornamentation and choosiness follow from gamete investment, not from being female per se; in standard anisogamy it is males that are ornamented, and sex-role reversal can produce female ornamentation when males invest more.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Sexual dimorphism (males having elaborate traits like peacock tails that reduce survival) persists because:",
      "choices": [
        "Natural selection favors traits that reduce competition between sexes for food",
        "The traits were beneficial in ancestral environments and have been maintained by evolutionary lag",
        "The mating success advantage of the elaborate trait outweighs the survival cost — sexual selection is stronger than natural selection in this case",
        "Females prefer elaborate males because elaborate males are better foragers",
        "Elaborate male traits are maintained by Muller's Ratchet — the population has accumulated so many tail-elongating mutations that they cannot be reversed without recombination"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Sexual dimorphism reflects the balance between SEXUAL selection (favors elaborate traits → increases matings) and NATURAL selection (disfavors elaborate traits → reduces survival). The peacock's tail persists because the increase in mating success is GREATER than the cost in reduced survival. Zahavi's handicap principle: the tail's costliness is actually the point — only genuinely high-quality males can afford to survive with such a burden. | **Wrong E:** Muller's Ratchet describes irreversible accumulation of deleterious mutations in asexual lineages and has nothing to do with the maintenance of sexually selected ornaments in sexual species.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which scenario correctly demonstrates INTERSEXUAL selection (mate choice), satisfying ALL criteria: one sex evaluating the other, choosiness based on heritable traits, and leading to sexual dimorphism?",
      "choices": [
        "Male elephant seals fighting each other for exclusive access to a beach full of females — the winner mates with all females present",
        "Female birds preferentially mating with males whose bright plumage correlates with parasite resistance, producing heritable offspring that are also brighter and more resistant",
        "Males and females of a monogamous species pairing randomly based on geographic proximity rather than trait assessment",
        "Females and males competing equally for limited nesting sites, with both sexes evolving larger body size",
        "Males producing pheromones that suppress female reproduction — a form of sexual conflict, not mate choice"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Intersexual selection (mate choice): females evaluate males on heritable traits (plumage brightness correlating with parasite resistance), leading to dimorphism as males evolve brighter plumage. All three criteria satisfied. | **Wrong A:** This is INTRAsexual selection — male-male competition, not female choice. | **Wrong C:** Random pairing based on proximity is not selective mate choice and produces no directional dimorphism. | **Wrong D:** Both sexes competing for the same resource drives convergent evolution in both sexes, not dimorphism via intersexual selection. | **Wrong E:** Sexual conflict involves one sex manipulating the other against its interests — not the same as active mate-quality assessment.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which of the following correctly describe consequences of anisogamy? (I) Females invest more energy per gamete than males (II) Male reproductive success is more strongly limited by access to females than females' success is limited by access to males (III) Females typically compete more intensely than males for mates in most species (IV) Sexual selection produces traits that maximize mating success even at survival cost",
      "choices": [
        "I and II only",
        "I, II, and III",
        "II and IV only",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (female gametes costlier), II (male fitness more mate-number limited — Bateman gradient), and IV (sexually selected traits persist despite survival costs) all follow from anisogamy theory. | **Wrong A:** Misses IV, which is also a consequence. | **Wrong B:** III is FALSE — in most species MALES compete more intensely for mates; females are choosy. Female competition is the exception (sex-role reversal) when males invest more per gamete. | **Wrong C:** Misses I, which is also a direct consequence. | **Wrong E:** III is false in standard anisogamy theory.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism by which anisogamy drives the Bateman gradient?",
      "choices": [
        "(1) Eggs are large and costly — females produce few; (2) Female total reproductive output is limited by egg-production time and resources; (3) Male output is limited by access to females, not sperm production; (4) Males gain more fitness per additional mate than females do; (5) This asymmetry drives male-male competition and female choosiness",
        "(1) Sperm are costly to produce — males invest heavily per gamete; (2) Male total reproductive output is limited by sperm supply; (3) Female output is limited by access to males; (4) Females gain more fitness per additional mate; (5) This drives female-female competition and male choosiness",
        "(1) Both gametes are equally costly in energetic terms; (2) The sex ratio determines which sex competes; (3) Whichever sex is rarer will be choosy; (4) In 50:50 sex ratio species, neither sex is choosy; (5) Sexual selection only occurs when sex ratios are skewed",
        "(1) Eggs and sperm are equally cheap; (2) Competition arises from territorial defense, not gamete investment; (3) Larger body size in males evolves for predator defense; (4) Female choice is based on territory quality alone; (5) Anisogamy is irrelevant to sexual dimorphism",
        "(1) Eggs are costly; (2) Both sexes invest equally overall because males expend energy competing; (3) Total reproductive investment is equal across sexes; (4) No Bateman gradient exists in nature; (5) Sexual selection is driven by ecological factors, not gamete size"
      ],
      "answer": 0,
      "why": "&#9989; **A.** This is the correct Bateman gradient logic: costly eggs → females' output limited by egg production → males' output limited by mate number → males gain more per additional mate → male competition and female choice. | **Wrong B:** Inverts the gamete cost asymmetry — sperm are cheap, not costly; this describes sex-role reversal conditions, not the standard case. | **Wrong C:** The operational sex ratio does modulate competition, but the root cause is gamete investment asymmetry, not just the ratio. | **Wrong D:** Incorrectly claims gametes are equally cheap and denies the role of anisogamy. | **Wrong E:** Equal total investment is a common misconception; what matters is investment per gamete, not total energetic expenditure summed across all competitive behaviors.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which does NOT follow from standard anisogamy theory when applied to a species where males provide ALL parental care and females abandon eggs immediately after laying?",
      "choices": [
        "Males become the limiting reproductive resource for females",
        "Females are expected to compete for access to high-quality males",
        "Males become choosy about which females they accept as mates",
        "Females will be choosy and males will compete intensely for females",
        "Sexual dimorphism may develop with females being more ornamented or larger than males"
      ],
      "answer": 3,
      "why": "&#9989; **D.** When males provide ALL parental care and females abandon eggs, the standard anisogamy prediction is REVERSED (sex-role reversal). Males now invest heavily post-fertilization → males become the limiting resource → females compete for males, and males become choosy. \"Females choosy, males compete\" is the standard prediction that does NOT apply here. | **Wrong A:** Correctly follows — with male care, males ARE the limiting resource. | **Wrong B:** Correctly follows — females should compete for caring males. | **Wrong C:** Correctly follows — males should be choosy when they invest heavily in each brood. | **Wrong E:** Correctly follows — sex-role reversal can produce female ornamentation (e.g., jacanas, pipefish).",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which of the following CORRECTLY describes sperm competition, satisfying ALL criteria: within a female's reproductive tract, multiple males' sperm competing, selection on male traits for competitive advantage, and drives evolution of testis size?",
      "choices": [
        "Males compete physically before mating to prevent rivals from approaching females, and the winner's sperm fertilize the eggs without any sperm-level competition",
        "Males produce fewer, higher-quality sperm to outcompete rivals, leading to evolution of smaller testes that invest in quality over quantity",
        "Sperm competition occurs when females mate with multiple males and sperm from different males compete to fertilize the same eggs, driving evolution of larger testes and more competitive sperm morphologies",
        "Sperm competition only occurs in externally fertilizing species where sperm are released into open water and randomly encounter eggs",
        "Sperm competition selects for males that mate-guard exclusively, eliminating the need for competitive sperm traits because rivals cannot approach the female"
      ],
      "answer": 2,
      "why": "&#9989; **C.** All four criteria satisfied: sperm competition occurs within the female's reproductive tract, involves sperm from different males, creates selection on male competitive traits, and drives larger testes (more sperm volume = competitive advantage). | **Wrong A:** Pre-mating physical competition is intrasexual selection (male-male competition), not sperm competition — sperm competition occurs AFTER mating, inside the female. | **Wrong B:** Sperm competition drives LARGER testes (more sperm = better competition), not smaller; quality-only investment without quantity would be disadvantageous under sperm competition. | **Wrong D:** Sperm competition is most intensely studied in internally fertilizing species (e.g., insects, birds, mammals) — it is not limited to external fertilizers. | **Wrong E:** Mate-guarding reduces sperm competition intensity but does not eliminate the selective pressure on sperm traits where polyandry occurs.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which statements about sexual conflict are TRUE? (I) Sexual conflict arises when male and female reproductive interests differ (II) Drosophila seminal fluid proteins increase male fitness while reducing female longevity (III) Sexual conflict always results in stable coexistence with no further evolution (IV) Female coevolutionary responses to sexual conflict can themselves drive further male counter-adaptation",
      "choices": [
        "I and II only",
        "I and III only",
        "I, II, and III",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (conflict from divergent interests), II (Drosophila SFPs — male benefit, female cost), and IV (female resistance drives further male counter-adaptation — ongoing arms race) are all true. | **Wrong A:** Misses IV, which is also true — the arms race is ongoing, not resolved. | **Wrong B:** III is FALSE and misses II; sexual conflict produces ongoing coevolutionary dynamics, not stable coexistence. | **Wrong C:** III is FALSE — sexual conflict creates perpetual arms-race dynamics because whenever females evolve resistance, selection favors males with more potent counter-adaptations. | **Wrong E:** III is false, eliminating \"all of the above.\"",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which correctly describes the Drosophila sexual conflict mechanism step-by-step?",
      "choices": [
        "(1) Male seminal fluid proteins (SFPs) bind female reproductive tract; (2) SFPs reduce female remating (benefit to male) and increase egg-laying rate (benefit to male); (3) SFPs are toxic to female nervous/immune system → reduces female lifespan (cost to female); (4) Selection favors females resistant to SFP effects; (5) Selection favors males with more potent SFPs that overcome female resistance; (6) Ongoing coevolutionary arms race within species",
        "(1) Males produce SFPs that benefit both sexes by increasing offspring survival; (2) SFPs coordinate male and female reproductive effort; (3) Both sexes are selected to maximize SFP production; (4) No conflict exists because SFP effects are mutualistic; (5) Sexual conflict theory does not apply to Drosophila",
        "(1) Females produce proteins that reduce male fertility to control mating frequency; (2) Males evolve resistance to female manipulation; (3) This is a female-initiated arms race, not male-initiated; (4) SFPs are female-produced, not male-produced",
        "(1) SFPs increase female lifespan by reducing the physiological cost of egg production; (2) Males benefit from longer-lived females because they can be mated more times; (3) SFPs represent mutualistic coevolution between male and female interests; (4) No fitness cost to females exists",
        "(1) SFPs are produced by both sexes; (2) They coordinate gamete production timing; (3) Any fitness effects are symmetric between sexes; (4) The conflict arises only when SFPs are overproduced due to genetic drift"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct Drosophila mechanism: male-produced SFPs manipulate female physiology to benefit the male (less remating, more eggs) at a direct cost to the female (reduced longevity) → selection on females to resist → selection on males for more potent SFPs → perpetual within-species arms race. | **Wrong B:** SFPs are NOT mutualistic — they have documented fitness costs to females (reduced lifespan in SFP-exposed females vs. controls). | **Wrong C:** SFPs are male-produced, not female-produced; the arms race is male-initiated in the Drosophila system. | **Wrong D:** SFPs do NOT increase female lifespan — the empirical data show reduced female longevity when exposed to male SFPs. | **Wrong E:** SFPs are specifically male-produced seminal proteins; the fitness effects are asymmetric by definition of sexual conflict.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Which does NOT correctly describe an evolutionary consequence of sperm competition?",
      "choices": [
        "Species where females mate with multiple males typically have males with larger testes relative to body size than monogamous species",
        "Sperm competition favors evolution of SMALLER testes because energetic savings can be redirected to territory defense",
        "Males in high-sperm-competition species may evolve sperm with longer flagella for increased swimming speed",
        "Mate-guarding behavior can reduce sperm competition intensity, potentially relaxing selection for large testes in guarding species",
        "Sperm competition has driven evolution of seminal fluid proteins that can suppress female remating in some insects"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Sperm competition consistently favors LARGER testes relative to body size, because producing more sperm increases competitive ability when multiple males' sperm are present in the female. Smaller testes are predicted when mate-guarding reduces sperm competition — the opposite of what this answer claims. The logic about \"energetic savings redirected to territory defense\" is precisely the alternative strategy that reduces sperm competition intensity. | **Wrong A:** This correctly describes the comparative pattern — polyandrous species have relatively larger testes (well-documented across primates, insects, birds). | **Wrong C:** Longer flagella for speed is a documented sperm morphology adaptation under competition. | **Wrong D:** Mate-guarding as an alternative to sperm competition is a real evolutionary trade-off — investing in guarding reduces the need for sperm quantity. | **Wrong E:** Seminal proteins suppressing female remating (e.g., Drosophila SFPs) are a classic sperm-competition-related adaptation.",
      "sectionId": "s_sexsel",
      "chapterId": "ch_s_ch11"
    },
    {
      "prompt": "Guppies transplanted from high-predation streams to low-predation streams evolved over ~30 generations. Which life history changes occurred?",
      "choices": [
        "Earlier maturation, smaller body size, more offspring per litter (matching high-predation environment)",
        "Earlier maturation and larger body size (faster growth in safer environment)",
        "Later maturation, larger body size at maturity, fewer offspring per litter (matching low-predation strategy)",
        "No detectable change — 30 generations is insufficient for life history evolution",
        "Earlier maturation and more offspring per litter because low-predation environments have abundant food resources, removing all constraints on reproductive investment"
      ],
      "answer": 2,
      "why": "&#9989; **C.** In low-predation environments: guppies can SURVIVE to reproduce multiple times → invest more in growth and survival → evolve LATER maturation, LARGER body at maturity, FEWER but larger offspring per litter. This is the K-selected direction. In high-predation: evolve EARLY maturation (reproduce before being eaten), smaller body, more offspring. Reznick's famous experiment directly demonstrated this in ~30 generations. | **Wrong E:** Food abundance is not the primary driver of life-history evolution in this system; the key selective force is extrinsic mortality (predation risk), and low predation selects for delayed reproduction, not accelerated reproduction.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which factor MOST strongly predicts whether a species will have a 'fast' vs. 'slow' life history?",
      "choices": [
        "Geographic range — species with larger ranges have slower life histories due to more stable resources",
        "Body size — large-bodied species always have slow life histories regardless of environment",
        "Level of extrinsic mortality (predation, disease) — high extrinsic mortality favors fast life histories (reproduce early before dying); low extrinsic mortality favors slow life histories",
        "Phylogenetic position — only mammals can evolve slow life histories",
        "Climate zone — species in tropical environments invariably evolve fast life histories because high ambient temperature accelerates metabolic rate and therefore developmental rate"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Extrinsic mortality (predation risk, disease) is the strongest predictor. HIGH extrinsic mortality → individuals often die before reproducing multiple times → selection favors EARLY reproduction and many offspring per bout (fast life). LOW extrinsic mortality → individuals survive long enough to reproduce many times → selection can favor LATER reproduction, fewer offspring per bout, more investment in each offspring (slow life). | **Wrong E:** Climate can influence metabolic rate proximately, but life history strategy is determined by selection on extrinsic mortality, not ambient temperature per se; many tropical species have slow life histories when predation risk is low.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which combination of traits describes a \"fast\" life history strategy, satisfying ALL conditions: early maturation, many small offspring, short lifespan, AND high extrinsic mortality environment?",
      "choices": [
        "Elephant: matures at ~10 years, one calf per birth, 60-year lifespan, low predation on adults",
        "Annual weed in a disturbed field: germinates and flowers within weeks, produces hundreds of tiny seeds, dies after one season, high disturbance mortality",
        "Albatross: matures at 10 years, one egg per year, 50-year lifespan, low adult predation at sea",
        "Bowhead whale: matures at ~25 years, one calf per birth every 3–4 years, potentially 200-year lifespan, low adult predation",
        "Human: matures at ~15 years reproductively, low offspring number per birth, long lifespan, low contemporary predation"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The annual weed satisfies ALL four criteria: early (fast) maturation, many small offspring (seeds), short lifespan, and high extrinsic mortality (disturbance). Classic r-selected fast life history. | **Wrong A:** Elephants have late maturation, few large offspring, and long lifespan — classic slow (K-selected) life history. | **Wrong C:** Albatrosses are extreme K-selected: very late maturation, minimal reproductive effort per year, long lifespan. | **Wrong D:** Bowhead whales are among the slowest life histories known. | **Wrong E:** Humans have moderate lifespan but relatively late maturation and low offspring number — slow life history.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which changes occurred in Reznick's guppy experiment after ~30 generations in low-predation environments? (I) Later age at maturation (II) Larger body size at first reproduction (III) Fewer offspring per litter (IV) Earlier maturation to exploit the safer environment",
      "choices": [
        "I and II only",
        "I, II, and IV",
        "I, II, and III only",
        "II, III, and IV",
        "All of the above"
      ],
      "answer": 2,
      "why": "&#9989; **C.** I, II, and III are the documented results: later maturation, larger body size at maturity, and fewer offspring per litter — all shifts toward a slower (K-selected) life history in response to reduced predation. | **Wrong A:** Misses III (fewer offspring), which also occurred. | **Wrong B:** IV is FALSE — earlier maturation is the high-predation response; low-predation selects for LATER maturation. | **Wrong D:** IV is false; see above. | **Wrong E:** IV is false, eliminating \"all of the above.\"",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism by which high extrinsic mortality selects for early reproduction?",
      "choices": [
        "(1) In a high-predation environment, most individuals die before old age; (2) Alleles for late reproduction are rarely expressed — carriers die before reproducing late; (3) Selection cannot favor late-reproducing alleles; (4) Alleles for early, fast reproduction confer higher fitness because carriers are more likely to reproduce at all; (5) Population evolves fast life history",
        "(1) Low predation means individuals live long enough to reproduce many times; (2) Selection favors alleles for early reproduction because more reproductive events = more total offspring; (3) Early maturation evolves; (4) Body size decreases because energy is diverted to early reproduction; (5) Low-predation populations evolve fast life history",
        "(1) High predation increases food availability by reducing competitors; (2) Better nutrition allows earlier maturation via phenotypic plasticity; (3) Early maturation is fixed genetically over generations; (4) High-predation populations evolve fast life history through nutritional pathways",
        "(1) High predation selects for large body size for defense; (2) Large bodies mature later; (3) Late maturation is favored because large individuals survive predation better; (4) High-predation populations evolve slow life history",
        "(1) High predation causes stress hormones to accelerate development; (2) Phenotypic plasticity produces early maturation within one generation; (3) This plastic response becomes genetically fixed via epigenetic inheritance; (4) No selection on allele frequencies is involved"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism: high predation kills individuals before late-acting alleles are expressed → selection is blind to late-reproduction alleles → early-reproduction alleles are strongly favored → fast life history evolves genetically over generations. | **Wrong B:** Inverts the logic — low predation, not high predation, is associated with long life; this describes slow life history selection. | **Wrong C:** Confuses proximate (nutritional/plastic) mechanism with ultimate (selection) mechanism; food availability is not the primary driver. | **Wrong D:** Large body for predator defense is not the dominant life history prediction under high predation — fast reproduction is. | **Wrong E:** Epigenetic inheritance is not the standard mechanism; the guppy experiment demonstrated genuine allele frequency change, not only plasticity.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which does NOT support the prediction that low predation should evolve slower aging?",
      "choices": [
        "Island opossums with low predation evolved later onset of senescence compared to mainland opossums (Austad)",
        "With low extrinsic mortality, individuals live long enough for late-acting deleterious alleles to reduce fitness — selection can now remove them",
        "Organisms in safe environments should reproduce as early as possible to maximize lifetime reproductive output",
        "Low predation shifts the force of selection further into old age, allowing selection to \"see\" antagonistically pleiotropic late-life costs",
        "Bat species, which are relatively safe from predation due to flight, have much longer lifespans than similarly sized ground-dwelling mammals"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This is the OPPOSITE of what the theory predicts in low-predation environments. Low predation extends the expected future lifespan, so selection FAVORS delayed reproduction and slower aging — not earlier reproduction. Maximizing early reproduction is the HIGH-predation (fast life history) strategy. | **Wrong A:** The Austad opossum result directly supports slower aging under low predation. | **Wrong B:** This correctly explains the mechanism by which low predation leads to slower aging. | **Wrong D:** Correctly describes how reduced extrinsic mortality extends the window of selection into old age. | **Wrong E:** Bat longevity relative to body size is a classic comparative example supporting the low-extrinsic-mortality → slow-aging prediction.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which correctly characterizes a Seychelles Warbler female's decision to act as a helper, satisfying ALL conditions: only in high-quality territories, fitness return exceeds dispersal option, does NOT require kin relationship as primary driver, and is a conditional life history tactic?",
      "choices": [
        "A female helps whenever she is related to the breeding pair (r ≥ 0.5), regardless of territory quality, because kin selection alone drives her decision",
        "A female helps on a high-quality territory when helping yields higher inclusive fitness than dispersing to a low-quality territory independently",
        "A female always helps on any available territory because cooperative breeding maximizes group productivity regardless of individual fitness",
        "A female helps only when her own reproductive output has already been maximized and she has surplus energy to donate",
        "A female helps on low-quality territories because helpers are needed most where breeding success is lowest"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The Seychelles warbler system shows condition-dependent helping: females help on high-quality territories because the inclusive fitness return from helping exceeds what they could gain by dispersing to a low-quality territory. All four criteria are satisfied simultaneously. | **Wrong A:** Kin relationship is not the primary driver — territory quality is; unrelated females will help on high-quality territories, and related females will NOT help on low-quality ones. | **Wrong C:** Group productivity is not the decision criterion; individual inclusive fitness determines the choice. | **Wrong D:** Helpers do not wait for personal surplus — they help when the fitness return from helping exceeds the dispersal alternative. | **Wrong E:** This is precisely backwards: helpers avoid low-quality territories because helping there yields no fitness return.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which statements about Seychelles Warbler helpers are TRUE? (I) Helping occurs when territory quality is high enough to make helping more profitable than independent reproduction (II) Helpers are purely altruistic and gain no direct fitness benefit (III) Helpers may gain indirect fitness if they are related to the breeding pair (IV) When high-quality territories become available, helpers may switch to independent reproduction",
      "choices": [
        "I and IV only",
        "I and II only",
        "I, II, and III",
        "I, III, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (territory quality drives helping), III (helpers related to breeders gain indirect fitness), and IV (helpers switch to independent reproduction when high-quality territories open up) are all true. | **Wrong A:** Misses III, which is also true — kin-based indirect fitness can add to the inclusive fitness calculation. | **Wrong B:** II is FALSE — helpers are NOT purely altruistic; they are making an optimal life-history decision that may also yield experience benefits and indirect fitness gains. | **Wrong C:** II is false; see above. | **Wrong E:** II is false, eliminating \"all of the above.\"",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "A female Seychelles Warbler on a low-quality territory decides to delay reproduction. Which step-by-step logic is correct?",
      "choices": [
        "(1) Female assesses territory quality; (2) Low-quality territory: independent breeding yields low reproductive success; (3) Dispersal options are also poor; (4) Female delays reproduction rather than waste reproductive effort on a territory with low returns; (5) This is NOT altruism — it is the optimal life history decision given ecological constraints",
        "(1) Female assesses territory quality; (2) Low-quality territory: she helps the resident breeding pair anyway because kin selection overrides territory quality; (3) Even on poor territory, helping spreads her alleles through relatives; (4) Helping is always optimal when breeders are related",
        "(1) Female is evicted from high-quality territory by dominant female; (2) She is forced to help on a low-quality territory against her optimal strategy; (3) Forced helping reduces her fitness but benefits the dominant; (4) This illustrates sexual conflict in cooperative breeders",
        "(1) Female delays reproduction to avoid depleting food resources for future generations; (2) Group selection favors population-level restraint; (3) Individual restraint is enforced by other group members; (4) This is an example of Wynne-Edwards group selection in birds",
        "(1) Female helps on low-quality territory because experience gained compensates for low fitness returns; (2) After gaining experience, she acquires a high-quality territory and breeds successfully; (3) The delay is always worth it regardless of the specific territory quality"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism: on low-quality territory, independent breeding has low returns AND dispersal is constrained, so delaying reproduction is the optimal life-history decision — not altruism. | **Wrong B:** Helping on a low-quality territory is precisely what does NOT happen in Seychelles warblers — the system shows that helping is only profitable on high-quality territories. | **Wrong C:** Eviction and forced helping describe a different conflict scenario, not the standard Seychelles warbler decision-making framework. | **Wrong D:** Wynne-Edwards group selection is the discredited hypothesis that animals voluntarily restrain reproduction for group benefit — this is not what the Seychelles warbler system shows. | **Wrong E:** Experience benefits may contribute, but the conditional \"always worth it regardless of territory quality\" is incorrect — the empirical pattern shows helping is quality-dependent.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which does NOT correctly describe why helpers do NOT help on low-quality territories?",
      "choices": [
        "On poor territories, the breeding pair produces few offspring, so the inclusive fitness return from helping is too low to exceed the fitness from dispersal",
        "Helping on a poor territory yields negligible direct or indirect benefits compared to the opportunity cost of delayed reproduction",
        "On poor territories, helpers cannot gain any indirect fitness benefits through kin selection",
        "The net inclusive fitness from helping on a low-quality territory is lower than dispersing to any available territory, however poor",
        "Poor territory quality means the helped breeders produce very few extra offspring even with helper assistance, making the rB term in Hamilton's Rule very small"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This is NOT the correct explanation. Indirect kin-selection benefits COULD still operate on low-quality territories if the breeders are relatives. The key reason helpers avoid poor territories is that the LOW TOTAL inclusive fitness return (direct + indirect) from helping on poor territory is outweighed by alternative options — not the complete absence of kin-selection benefits. | **Wrong A:** This correctly identifies the fitness-return logic: few offspring produced = low inclusive fitness gain. | **Wrong B:** Correctly identifies that opportunity cost of delayed reproduction exceeds the benefit on poor territories. | **Wrong D:** Correctly identifies the comparative fitness framework — net helping benefit vs. dispersal alternative. | **Wrong E:** Correctly applies Hamilton's Rule: few extra offspring raised (low B) × relatedness (r) = small rB that cannot exceed C.",
      "sectionId": "s_lifehistory",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "An experiment removes predators from a population of mice for many generations. Evolutionary theory predicts the mice would evolve:",
      "choices": [
        "Faster aging — with no predators, they waste energy on survival mechanisms",
        "Earlier reproduction — safer environment means more food available for rapid reproduction",
        "Slower aging — with lower extrinsic mortality, individuals survive long enough to experience late-life costs of aging, so selection can now act against deleterious late-acting alleles and antagonistically pleiotropic genes",
        "No change in aging — aging is genetically fixed and cannot respond to changes in predation",
        "Faster aging because the absence of predators causes antagonistic pleiotropy alleles to accumulate at a higher rate due to increased population size and elevated genetic drift"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This is the KEY life history test. Without predators, mice LIVE LONG ENOUGH to suffer late-life fitness costs. Now selection can &ldquo;see&rdquo; late-acting deleterious mutations and antagonistically pleiotropic genes. Over generations, these are removed/modified → slower aging. Austad's opossum study: island opossums (low predation) evolved slower aging than mainland opossums (high predation) in just 4,000 years. | **Wrong E:** Removing predators extends lifespan into old age, making selection MORE effective against late-acting harmful alleles and thus producing slower aging — the opposite of faster aging; population size changes do not cause faster antagonistic pleiotropy accumulation.",
      "sectionId": "s_aging",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which feature of aging is explained by ANTAGONISTIC PLEIOTROPY but NOT by mutation accumulation alone?",
      "choices": [
        "Late-acting deleterious alleles accumulate because selection cannot remove them from individuals who die young",
        "Species with higher extrinsic mortality evolve faster aging because selection acts less on late-life genes",
        "High testosterone variants increase early mating success but also increase late-life prostate cancer and cardiovascular disease risk from the same alleles — an early benefit and late cost from the same gene",
        "Removing late-acting deleterious mutations would extend lifespan",
        "Aging is more severe in organisms that rarely survive to old age in the wild"
      ],
      "answer": 2,
      "why": "&#9989; **C.** Antagonistic pleiotropy requires one allele with opposite fitness effects at different life stages — early benefit AND late cost from the SAME gene. Testosterone exemplifies this: same alleles boost early reproductive success and cause late-life pathology. Mutation accumulation cannot explain why removing the allele would also remove an early benefit. | **Wrong A:** This describes mutation accumulation theory, not antagonistic pleiotropy. | **Wrong B:** Both theories predict this — it is not unique to antagonistic pleiotropy. | **Wrong D:** This follows from mutation accumulation theory; antagonistic pleiotropy predicts that removing some aging alleles would also reduce early-life fitness. | **Wrong E:** Both theories predict this pattern of more severe aging under higher extrinsic mortality.",
      "sectionId": "s_aging",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which predictions follow from BOTH mutation accumulation AND antagonistic pleiotropy theories of aging? (I) Late-acting deleterious alleles are less constrained by selection than early-acting ones (II) Species with lower extrinsic mortality should evolve slower aging (III) A single gene can have opposite fitness effects at different life stages (IV) Removing all late-acting deleterious mutations would completely eliminate aging",
      "choices": [
        "I and II only",
        "I, II, and III",
        "II and IV only",
        "I, III, and IV",
        "All of the above"
      ],
      "answer": 0,
      "why": "&#9989; **A.** Both theories predict I (late alleles escape selection) and II (low extrinsic mortality → selection extends into old age → slower aging). III is unique to antagonistic pleiotropy — mutation accumulation does not require one gene to have opposite effects, just neutral late-acting effects. IV is FALSE under antagonistic pleiotropy — removing those alleles would also eliminate early-life benefits, so aging cannot be fully eliminated. | **Wrong B:** III is specific to AP only, not predicted by both. | **Wrong C:** IV is false under AP theory. | **Wrong D:** III is AP-specific; IV is false. | **Wrong E:** III is AP-specific and IV is false.",
      "sectionId": "s_aging",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism of the mutation accumulation theory of aging?",
      "choices": [
        "(1) Random mutations with late-acting harmful effects arise in the population; (2) Most individuals die of extrinsic causes before reaching old age; (3) Selection rarely acts on individuals who express late-acting effects; (4) These late-acting deleterious alleles are not removed by selection; (5) They accumulate over generations; (6) Late-life fitness deteriorates — aging evolves",
        "(1) Mutations are specifically directed to late-life gene expression by aging-related epigenetic mechanisms; (2) These mutations accumulate with each cell division; (3) Selection actively maintains these mutations because they free up resources for young individuals; (4) Aging is adaptive — it benefits the population by removing old individuals",
        "(1) Late-acting mutations arise; (2) Selection acts equally on all life stages; (3) Late-acting alleles are just as likely to be removed as early-acting ones; (4) Therefore aging must be explained by something other than mutation accumulation — e.g., group selection",
        "(1) Late-acting mutations arise; (2) They are selectively neutral at all life stages; (3) Genetic drift alone fixes them in populations; (4) Aging rate is therefore independent of extrinsic mortality and body size",
        "(1) Somatic mutations accumulate in body cells during an individual's lifetime; (2) These are passed to offspring via germline transmission; (3) Each generation accumulates more somatic mutations; (4) Aging accelerates across generations via Lamarckian inheritance"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism: late-acting mutations escape selection because carriers die before expressing them → they accumulate → late-life deterioration evolves. | **Wrong B:** Mutations are not \"directed\" to late life — they are random; aging is not adaptive in this framework (that would be group selection). | **Wrong C:** The key insight of the theory is precisely that selection does NOT act equally on all life stages — late stages are nearly invisible to selection. | **Wrong D:** While drift contributes, the theory is fundamentally about SELECTION being weaker on late-acting alleles, not about neutrality; also, aging rate IS predicted to correlate with extrinsic mortality. | **Wrong E:** This describes somatic mutation theory of aging (proximate mechanism), not the evolutionary mutation accumulation theory; Lamarckian inheritance is incorrect.",
      "sectionId": "s_aging",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "Which does NOT support the evolutionary theory of aging?",
      "choices": [
        "Island opossums with lower predation evolved slower senescence than mainland opossums within ~4,000 years",
        "Bats live far longer than expected for their body size — consistent with low extrinsic mortality from flight extending the selective window into old age",
        "Castrated male animals often live longer — consistent with testosterone being an antagonistically pleiotropic allele with early reproductive benefit and late-life cost",
        "Removing all late-acting deleterious mutations would completely eliminate aging because antagonistic pleiotropy alleles can be deleted without any early-life fitness cost",
        "Species under high extrinsic predation pressure evolve earlier senescence — consistent with selection being weaker on late-life alleles when few individuals survive to old age"
      ],
      "answer": 3,
      "why": "&#9989; **D.** This is FALSE under antagonistic pleiotropy theory — AP alleles have EARLY BENEFITS that would be lost if the allele were deleted. Complete elimination of aging by removing all late-acting alleles is not predicted by AP; some aging is maintained because eliminating the allele also eliminates early-life fitness advantages. | **Wrong A:** The opossum experiment directly supports the evolutionary theory. | **Wrong B:** Bat longevity is a classic comparative test supporting the theory. | **Wrong C:** Castration longevity studies support the AP mechanism for testosterone. | **Wrong E:** The correlation between extrinsic mortality and aging rate is a core prediction of both mutation accumulation and AP theories.",
      "sectionId": "s_aging",
      "chapterId": "ch_s_ch12"
    },
    {
      "prompt": "In the garter snake-newt coevolutionary arms race, snakes with high TTX resistance have slower locomotion speed. This illustrates:",
      "choices": [
        "Antagonistic pleiotropy — the resistance allele has both beneficial (survives eating toxic newts) and costly (slower movement) effects",
        "Genetic drift — resistance alleles were fixed by chance in snake populations",
        "The Red Queen hypothesis — snakes constantly cycling genotypes to stay ahead of newt toxin evolution",
        "Geographic isolation — resistant snakes are speciated from non-resistant ones",
        "Müllerian mimicry — the resistant snakes evolved warning coloration matching the toxic newts so that predators avoid both species equally"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The TTX-resistance mutation in the snake's sodium channel confers a BENEFIT (survives eating toxic newts) and a COST (slower movement from slightly impaired muscle function). This is a fitness trade-off or antagonistic pleiotropic effect of the same genetic change. It's not A-P in the aging sense but it is a single mutation with two fitness consequences. Also illustrates why the arms race doesn't escalate to infinity — costs constrain how extreme traits can become. | **Wrong E:** Müllerian mimicry involves unpalatable species sharing warning coloration for mutual predator-avoidance benefit; garter snakes are predators of newts, not prey avoiding a shared threat, and the resistance is biochemical, not visual.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "A population of garter snakes lives far from any toxic newts. According to the Geographic Mosaic Theory, what do you expect for their TTX resistance?",
      "choices": [
        "They would have high resistance because TTX resistance is always maintained as a backup",
        "Low resistance — with no toxic newts (no selection for resistance), and a metabolic cost to maintaining resistance, snakes should evolve LOW resistance levels",
        "Variable resistance due to genetic drift in this isolated population",
        "High resistance due to gene flow from populations that do coexist with toxic newts",
        "Intermediate resistance that tracks the average toxicity across the entire species range, because gene flow homogenizes resistance levels globally to a single equilibrium value"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Geographic Mosaic Theory predicts COLDSPOTS where the coevolutionary interaction is absent. Without selection pressure (no toxic newts), AND with a cost to resistance (slower locomotion), resistance alleles should be at LOW frequency. This is what's observed: newt-free areas → low-resistance snakes. Hotspots (coexisting toxic newts) → high-resistance snakes. Geographic variation in trait expression = the mosaic. | **Wrong E:** Geographic Mosaic Theory specifically predicts that local selection at hotspots and coldspots maintains geographic variation in resistance despite gene flow; global homogenization to a single intermediate value is not predicted and contradicts the observed patchwork of high- and low-resistance populations.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which of the following CORRECTLY describes a coevolutionary hotspot according to Geographic Mosaic Theory, satisfying ALL criteria: both species present, intense reciprocal selection, AND extreme trait values in both species?",
      "choices": [
        "A Pacific Coast site where garter snakes are common but Taricha newts are absent — snakes have moderate TTX resistance maintained by historical selection",
        "An inland site where Taricha newts are highly toxic but no Thamnophis snakes are present — one-sided selection with no reciprocal response",
        "A Pacific Coast site where highly toxic Taricha newts coexist with highly TTX-resistant Thamnophis snakes — both species present with extreme trait values driven by reciprocal escalation",
        "A site where newts and snakes coexist but both have low toxicity and low resistance — stable equilibrium with no ongoing escalation",
        "Any location where both species occur sympatrically, regardless of trait values — species presence alone defines a hotspot"
      ],
      "answer": 2,
      "why": "&#9989; **C.** A hotspot requires all three: both species present, intense reciprocal selection, AND extreme trait values in both. The Pacific Coast TTX-rich/resistance-rich sites satisfy all three criteria. | **Wrong A:** With newts absent there is no current reciprocal selection — this is a coldspot (or historical residual). | **Wrong B:** One species present means selection is one-sided, not reciprocal — not a hotspot. | **Wrong D:** Low trait values despite co-occurrence suggests weak or absent reciprocal selection — a coldspot, not a hotspot. | **Wrong E:** Species co-occurrence alone is insufficient — hotspots require intense reciprocal selection and escalated traits, not just sympatry.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which features distinguish a coevolutionary ARMS RACE from RED QUEEN dynamics? (I) Arms race = directional escalation of traits over time; Red Queen = frequency-dependent cycling (II) Both involve reciprocal evolutionary change between species (III) Arms races involve the same species cycling genotypes; Red Queen requires two different species (IV) Red Queen produces ever more extreme traits; arms races maintain cycling frequency",
      "choices": [
        "I and II only",
        "I, II, and III",
        "I, III, and IV",
        "II and IV only",
        "All of the above"
      ],
      "answer": 0,
      "why": "&#9989; **A.** I and II are correct. Arms races show directional escalation (newt toxicity and snake resistance both increase over time). Both dynamics involve reciprocal change between interacting species. | **Wrong B:** III is FALSE — Red Queen cycling occurs between host and parasite (two different species); arms races also involve two different species. The statement inverts which applies to whom. | **Wrong C:** IV is also FALSE — it inverts the definitions: arms races produce escalating extreme traits; Red Queen produces cycling, not escalation. | **Wrong D:** IV is false (inverted). | **Wrong E:** III and IV are both false.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism by which a geographic mosaic of coevolved traits forms?",
      "choices": [
        "(1) Coevolving species interact at varying intensities across the landscape; (2) Hotspots form where both species are present and reciprocal selection is intense; (3) Coldspots form where the interaction is weak or one partner is absent; (4) Gene flow between hotspots and coldspots homogenizes some traits; (5) Result: geographic patchwork of coevolved trait values across the range",
        "(1) Geographic barriers isolate populations; (2) Allopatric speciation produces new species in each isolated region; (3) Secondary contact creates hotspots; (4) Gene flow is impossible across barriers; (5) The mosaic forms only after speciation is complete",
        "(1) A single hotspot of coevolution spreads outward across the range; (2) The most extreme traits always eventually cover the entire species range; (3) Coldspots are temporary and always converted to hotspots; (4) Geographic mosaics are unstable and collapse to uniformity over time",
        "(1) Both species must be present everywhere for coevolution to occur; (2) Absence of either species from any location prevents a mosaic; (3) Geographic barriers are required; (4) Without barriers, gene flow eliminates all geographic variation in coevolved traits",
        "(1) Coevolution occurs only in hotspots; (2) Coldspot populations go extinct because they lack coevolved defenses; (3) Only hotspot populations survive long-term; (4) The mosaic simplifies over evolutionary time to only hotspot populations"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The geographic mosaic forms through variation in interaction intensity across the landscape, with gene flow between hotspots and coldspots creating a patchwork — not requiring geographic barriers or speciation. | **Wrong B:** The mosaic does not require geographic barriers or speciation — it forms within continuously distributed species through variation in selection intensity and gene flow. | **Wrong C:** Hotspots do not inevitably spread to cover the whole range — coldspots persist because selection is absent or weak there. | **Wrong D:** Both species need not be present everywhere — coldspots exist precisely where one or both partners are absent or weakly interacting. | **Wrong E:** Coldspot populations do not go extinct — they persist with low coevolved trait values, contributing to the mosaic.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which does NOT describe a coevolutionary arms race?",
      "choices": [
        "Taricha newts evolving higher TTX production in response to snake TTX resistance, and snakes evolving higher resistance in response to newt toxicity",
        "Frequency-dependent selection favoring rare host genotypes that parasites cannot exploit, preventing directional escalation and causing trait values to cycle",
        "Host immune systems evolving more potent defenses as pathogens evolve greater virulence in a reciprocal escalating fashion",
        "Plant toxin concentrations increasing over evolutionary time as herbivore detoxification enzymes become more potent",
        "Cheetah speed and gazelle speed both increasing over evolutionary time through reciprocal selection pressure"
      ],
      "answer": 1,
      "why": "&#9989; **B.** This describes Red Queen dynamics — frequency-dependent cycling of host genotypes driven by parasite tracking — NOT an arms race. Arms races show directional escalation of trait values; Red Queen dynamics show cycling without net escalation. | **Wrong A:** This is the textbook definition of a coevolutionary arms race — reciprocal directional escalation. | **Wrong C:** Reciprocal escalation of immune defenses and pathogen virulence is an arms race. | **Wrong D:** Reciprocal escalation of plant toxins and herbivore detoxification is a classic arms race example. | **Wrong E:** The cheetah-gazelle speed escalation is the classic \"evolutionary arms race\" metaphor.",
      "sectionId": "s_coevo_basics",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Heliconius butterfly species in the Neotropics are all toxic and share the same striking warning color patterns within each region. This is an example of:",
      "choices": [
        "Batesian mimicry — the most common species mimics the rarest toxic species",
        "Müllerian mimicry — multiple unpalatable species converge on the same warning signal, mutually reinforcing predator learning",
        "Cryptic mimicry — all species mimic the local leaf litter for camouflage",
        "Batesian mimicry is ruled out because only one species can be the model",
        "Kin selection — the Heliconius species are closely related and share warning patterns to protect relatives in the same geographic area through Hamilton's Rule"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Müllerian mimicry: all species involved are UNPALATABLE (toxic). By sharing warning patterns, predator learning about one species benefits ALL species with that pattern. The more common the pattern, the faster predators learn to avoid it. Both species benefit — mutualistic mimicry. Batesian mimicry requires one palatable mimic and one unpalatable model (not applicable when all are toxic). | **Wrong E:** Kin selection operates via genetic relatedness between individuals, not via shared coloration patterns between different species; Heliconius species that share warning patterns are not necessarily closely related, and the benefit is predator-learning, not indirect fitness through shared alleles.",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which evidence MOST directly supports the endosymbiotic origin of mitochondria from ancient bacteria?",
      "choices": [
        "Mitochondria are surrounded by a single membrane like other eukaryotic organelles",
        "Mitochondria have their own circular DNA, divide by binary fission, and have 70S ribosomes that are inhibited by bacterial (but not eukaryotic) antibiotics",
        "Mitochondria produce ATP, which is the same molecule that bacteria use for energy",
        "Mitochondria are present in all eukaryotic cells, suggesting they were present in LUCA",
        "Mitochondrial proteins are synthesized on 80S cytoplasmic ribosomes encoded entirely by the nuclear genome, demonstrating complete genetic integration with the host cell"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The definitive evidence package for endosymbiotic origin: (1) circular DNA = bacterial-style genome, (2) binary fission = bacterial-style division, (3) 70S ribosomes = bacterial-type ribosomes sensitive to bacterial antibiotics (chloramphenicol, erythromycin) but NOT eukaryotic antibiotics (cycloheximide). Option A is WRONG — mitochondria have DOUBLE membranes (inner from original bacterium, outer from engulfment vesicle). | **Wrong E:** Mitochondria retain their own 70S ribosomes and translate a small set of proteins encoded in their own circular genome; complete reliance on nuclear-encoded 80S ribosomes would actually argue against, not for, an endosymbiotic bacterial origin.",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which scenario CORRECTLY describes Batesian mimicry, satisfying ALL criteria: harmless mimic, unpalatable or dangerous model, visual resemblance, AND maintained at low mimic frequency?",
      "choices": [
        "Two toxic Heliconius butterfly species that share the same red-and-black warning pattern across a geographic region — both species benefit from predator learning",
        "A palatable red-banded king snake (mimic) resembling a venomous coral snake (model) in areas where coral snakes are common — the harmless snake benefits from predator avoidance learned from the toxic model",
        "A harmless hoverfly population that has become so abundant it outnumbers local bees tenfold — predators now frequently encounter harmless hoverflies and no longer avoid them",
        "A toxic frog species that evolves coloration matching another toxic frog species in the same region — both species reinforce the warning signal",
        "A cuckoo that mimics the appearance of a hawk to deter aggression from host birds defending their nests — behavioral mimicry without a palatable/unpalatable distinction"
      ],
      "answer": 1,
      "why": "&#9989; **B.** All four criteria satisfied: king snake is harmless (palatable), coral snake is venomous (unpalatable model), visual resemblance is the mechanism, and the system works when coral snakes are common (mimic frequency low relative to model). | **Wrong A:** This is Müllerian mimicry — both species are toxic and mutually benefit; neither is a harmless mimic. | **Wrong C:** This describes a BREAKDOWN of Batesian mimicry — when mimics outnumber models, the signal becomes unreliable and protection is lost. Not a valid Batesian system. | **Wrong D:** Two toxic species converging on the same pattern is Müllerian, not Batesian. | **Wrong E:** Behavioral mimicry for aggression deterrence is not standard Batesian mimicry, which requires a learned predator-avoidance response to an unpalatable model.",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which evidence supports the endosymbiotic origin of mitochondria? (I) Mitochondria have their own circular DNA (II) Mitochondria have 70S ribosomes inhibited by antibacterial antibiotics (III) Mitochondria divide by binary fission like bacteria (IV) Mitochondria have a nucleus containing the majority of their genetic material",
      "choices": [
        "I and III only",
        "I, II, and IV",
        "I, II, and III only",
        "II, III, and IV",
        "All of the above"
      ],
      "answer": 2,
      "why": "&#9989; **C.** I (circular DNA), II (70S ribosomes inhibited by bacterial antibiotics like chloramphenicol), and III (binary fission) are all genuine evidence for endosymbiotic bacterial origin. | **Wrong A:** Misses II, which is also strong evidence. | **Wrong B:** IV is FALSE — mitochondria have NO nucleus; their genes are on circular DNA in the matrix, not in a nucleus. Having a nucleus is a eukaryotic feature, not a bacterial or mitochondrial one. | **Wrong D:** IV is false. | **Wrong E:** IV is false, eliminating \"all of the above.\"",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism maintaining Batesian mimicry?",
      "choices": [
        "(1) Predator eats unpalatable model and learns to avoid its warning coloration; (2) Harmless mimic shares the warning pattern; (3) Predator avoids the mimic too — mimic survives; (4) If mimics become too common, predators frequently encounter harmless individuals; (5) Warning signal becomes unreliable; (6) Predators stop avoiding the pattern — mimics lose protection",
        "(1) Predator learns to avoid the mimic because it is common; (2) The mimic's abundance reinforces avoidance learning; (3) More mimics = stronger protection for all mimics; (4) Mimic frequency can increase indefinitely without degrading protection; (5) No frequency-dependence in Batesian mimicry",
        "(1) Both mimic and model are unpalatable; (2) Predator learns to avoid the shared pattern; (3) Higher combined frequency of both species accelerates predator learning; (4) More individuals sharing the pattern = greater protection for all; (5) This is why mimics should be as common as possible",
        "(1) Mimic evolves to look like model through genetic drift; (2) No predator learning is required; (3) The resemblance protects mimics simply because predators cannot distinguish species; (4) Mimic frequency has no effect on protection strength",
        "(1) Mimic is toxic; (2) Model is harmless; (3) Predators learn to avoid the common toxic mimic; (4) The harmless model benefits by resembling the toxic mimic; (5) Protection increases as mimic frequency increases"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism: predator learns from unpalatable model → avoids mimic → but frequency-dependence means if mimics become too common, the signal degrades and protection is lost. | **Wrong B:** Inverts the frequency-dependence — Batesian mimicry DOES have frequency-dependence; higher mimic frequency REDUCES, not increases, protection. | **Wrong C:** Describes Müllerian mimicry (both unpalatable), not Batesian; also correctly states that higher frequency helps in Müllerian but not Batesian. | **Wrong D:** Predator learning IS required — the mechanism depends on learned avoidance of the model's signal being generalized to the mimic. | **Wrong E:** Completely inverts the roles — in Batesian mimicry the MIMIC is harmless and the MODEL is unpalatable, not the reverse.",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "Which does NOT distinguish Müllerian from Batesian mimicry?",
      "choices": [
        "In Müllerian mimicry, all species sharing the warning pattern are unpalatable; in Batesian mimicry, the mimic is palatable",
        "Müllerian mimicry works better when the shared pattern is common; Batesian mimicry works better when mimics are rare relative to models",
        "In Müllerian mimicry, one species is palatable and mimics an unpalatable species to gain protection",
        "In Batesian mimicry the mimic \"cheats\" — it gains protection without contributing to predator learning; in Müllerian mimicry all species contribute to predator learning",
        "Müllerian complexes are mutualistic — all species benefit; Batesian mimicry is parasitic — the mimic benefits at the model's expense by diluting the honest signal"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This describes Batesian mimicry, NOT Müllerian. In Müllerian mimicry ALL species sharing the warning pattern are unpalatable — there is no palatable mimic. Calling Müllerian a system where one species is palatable is factually incorrect. | **Wrong A:** This correctly distinguishes them — accurate statement. | **Wrong B:** This correctly distinguishes the frequency-dependence direction — accurate statement. | **Wrong D:** This correctly identifies the \"cheating\" asymmetry in Batesian vs. mutual reinforcement in Müllerian. | **Wrong E:** The mutualism vs. parasitism framing correctly distinguishes the two types.",
      "sectionId": "s_mimicry",
      "chapterId": "ch_s_ch15"
    },
    {
      "prompt": "In the Hawk-Dove game, when the value of the resource (V) is LESS than the cost of injury (C), the ESS is:",
      "choices": [
        "Pure Hawk — aggression always wins when the resource is too costly to give up",
        "Pure Dove — if costs exceed resources, everyone should avoid fighting",
        "A mixed strategy where frequency of Hawks = V/C — at this frequency, Hawks and Doves have equal fitness",
        "Group selection determines the outcome — the strategy that benefits the group will be favored",
        "A pure Hawk ESS because V/C > 1 when V < C, meaning Hawks will always exceed Doves at equilibrium and eventually take over the population"
      ],
      "answer": 2,
      "why": "&#9989; **C.** When V < C (risk of injury outweighs resource value): pure Hawk isn't stable (if everyone is a Hawk, injuries are frequent and costly). Pure Dove isn't stable (a Hawk mutant always wins against all Doves). The ESS is a MIXED strategy: proportion of Hawks = V/C. At this frequency, Hawk and Dove have EQUAL fitness → no selection for either to increase → stable equilibrium. | **Wrong E:** When V < C, V/C is a fraction less than 1, not greater than 1; this means Hawks stabilize at a MINORITY frequency, not fixation, and pure Hawk is destabilized by the high injury cost when Hawks are common.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which of the following strategies is an Evolutionarily Stable Strategy (ESS), satisfying ALL criteria: when common it cannot be invaded by a rare mutant, fitness payoffs are frequency-dependent, and it does not necessarily maximize individual fitness in isolation?",
      "choices": [
        "Pure Hawk when V < C — Hawks always get the resource so pure Hawk gives the highest individual payoff regardless of opponent frequency",
        "Pure Dove when V < C — Doves avoid injury so pure Dove gives the highest individual survival rate in all populations",
        "The mixed strategy with Hawks at frequency V/C when V < C — at this frequency Hawks and Doves have equal fitness and no mutant strategy can invade",
        "Whichever strategy the majority currently plays — ESS is simply the most common strategy in the population at any given time",
        "The strategy that maximizes average population fitness — ESS equals the group-optimal strategy"
      ],
      "answer": 2,
      "why": "&#9989; **C.** The mixed ESS at V/C satisfies all three criteria: it cannot be invaded (both strategies have equal fitness at equilibrium), payoffs are frequency-dependent, and it does not maximize individual fitness (pure Dove meeting all Doves gets V/2, which could be higher than the mixed ESS payoff). | **Wrong A:** Pure Hawk when V < C is NOT stable — when Hawks are common, they frequently fight each other, paying (V−C)/2 which is negative; a Dove mutant does better. | **Wrong B:** Pure Dove is not stable — a rare Hawk mutant in an all-Dove population always wins the resource (payoff V vs. Dove's V/2). | **Wrong D:** ESS is not simply the most common strategy — it is defined by invasion resistance, not frequency alone. | **Wrong E:** ESS does not equal the group-optimal strategy; it is an individual-level stability concept and can be inefficient for the group.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which statements about the Hawk-Dove game are TRUE? (I) When V < C, neither pure Hawk nor pure Dove is an ESS (II) The ESS frequency of Hawks = V/C when V < C (III) ESS represents the strategy with maximum individual fitness at all frequencies (IV) A rare Hawk in an all-Dove population does BETTER than the resident Doves",
      "choices": [
        "I and II only",
        "I, II, and III",
        "II and IV only",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (neither pure strategy is ESS when V < C), II (ESS frequency of Hawks = V/C), and IV (rare Hawk beats Doves — gets full resource V vs. Dove's V/2) are all true. | **Wrong A:** Misses IV, which is also true — rare Hawks invade Dove populations, which is exactly why pure Dove is not an ESS. | **Wrong B:** III is FALSE — ESS is about invasion resistance, not maximum individual fitness; at the mixed ESS both strategies have EQUAL (not maximum) fitness. | **Wrong C:** Misses I, which is also true. | **Wrong E:** III is false.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which correctly describes the step-by-step derivation of the ESS frequency in the Hawk-Dove game when V < C?",
      "choices": [
        "(1) Hawk vs. Hawk payoff = (V−C)/2; (2) Hawk vs. Dove payoff = V; (3) Dove vs. Hawk payoff = 0; (4) Dove vs. Dove payoff = V/2; (5) At ESS frequency p*, Hawk fitness = Dove fitness; (6) Solving: p*(V−C)/2 + (1−p*)V = p*(0) + (1−p*)V/2 → p* = V/C",
        "(1) Hawk vs. Hawk payoff = V; (2) Hawk vs. Dove payoff = (V−C)/2; (3) At ESS, Hawks outnumber Doves; (4) ESS frequency of Hawks = C/V; (5) When C > V, Hawks dominate because injury cost is high",
        "(1) The ESS is simply the strategy with the highest average payoff in the population; (2) Calculate average payoff for each strategy; (3) The strategy with higher average payoff is the ESS; (4) No equilibrium condition is needed; (5) ESS = maximum fitness strategy",
        "(1) Hawk and Dove payoffs are equal at all frequencies; (2) No equilibrium frequency exists; (3) The ESS is determined by genetic drift; (4) The ratio V/C has no relevance to the ESS frequency; (5) Group selection determines which strategy prevails",
        "(1) Dove vs. Dove payoff = V; (2) Dove vs. Hawk payoff = V/2; (3) At ESS, Doves dominate because they avoid injury; (4) ESS frequency of Doves = V/C; (5) Hawks only persist by genetic drift"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct derivation: set Hawk fitness = Dove fitness at equilibrium frequency p* and solve. The four payoffs (HH, HD, DH, DD) feed into the fitness equations; solving gives p* = V/C. | **Wrong B:** Swaps the payoffs — Hawk vs. Hawk should be (V−C)/2 (split resource minus injury risk), not V; also inverts the ratio to C/V. | **Wrong C:** ESS is not simply the highest average payoff strategy — it is defined by the invasion resistance condition, requiring the equilibrium condition. | **Wrong D:** Payoffs are NOT equal at all frequencies; the whole point is that they are equal only at the ESS frequency p* = V/C. | **Wrong E:** Dove vs. Dove is V/2 (split resource), not V; Dove vs. Hawk is 0 (retreats), not V/2; the entire payoff matrix is wrong.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which does NOT correctly characterize an ESS?",
      "choices": [
        "An ESS cannot be invaded by a rare alternative mutant strategy when it is the resident strategy",
        "An ESS is the strategy that maximizes individual fitness regardless of what frequency it is at in the population",
        "At a mixed ESS equilibrium, all strategies present have equal fitness",
        "ESS fitness payoffs are frequency-dependent — the payoff to a strategy depends on what other strategies are in the population",
        "The Rock-Paper-Scissors dynamics of side-blotched lizards represent a three-strategy ESS that cycles stably"
      ],
      "answer": 1,
      "why": "&#9989; **B.** An ESS is defined by invasion resistance, NOT by maximizing individual fitness regardless of frequency. At the mixed Hawk-Dove ESS, both strategies have EQUAL fitness — neither is at its individual maximum. A strategy that maximized fitness at all frequencies would be an \"unbeatable strategy,\" a stronger concept than ESS. | **Wrong A:** Invasion resistance is the correct definition of ESS. | **Wrong C:** Equal fitness of all strategies at a mixed ESS equilibrium is correct — this is what makes it stable. | **Wrong D:** Frequency-dependence is the defining feature of ESS game theory. | **Wrong E:** Side-blotched lizard RPS dynamics are a valid three-strategy cyclic ESS example.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which of the following CORRECTLY characterizes the evolutionary dynamics of side-blotched lizard color morphs, satisfying ALL criteria: three morphs, cyclic frequency-dependent selection, no single ESS wins permanently, and population frequencies oscillate?",
      "choices": [
        "The three morphs converge on a fixed mixed-strategy ESS like Hawk-Dove, where all three are maintained at stable constant frequencies indefinitely",
        "Orange throat males eventually outcompete all others because ultra-dominance is the highest fitness strategy regardless of population composition",
        "The three throat-color morphs form a cyclic rock-paper-scissors dominance relationship; population morph frequencies oscillate over years as each strategy outperforms the next in a frequency-dependent cycle",
        "Blue mate-guarders are the stable ESS because guarding behavior is favored whenever sneakers and dominant males are present simultaneously",
        "The three morphs are maintained by mutation-selection balance rather than frequency-dependent selection, with each morph arising anew each generation"
      ],
      "answer": 2,
      "why": "&#9989; **C.** All four criteria satisfied: three morphs exist, frequency-dependent cyclic selection operates (each morph outperforms the next as frequencies shift), no single strategy wins permanently, and empirical data show multi-year oscillations in morph frequencies. | **Wrong A:** The Hawk-Dove fixed equilibrium is a different ESS type — side-blotched lizards show a CYCLIC ESS, not a fixed mixed-strategy equilibrium. | **Wrong B:** Orange is not dominant regardless of frequency — when Orange is common, Yellow sneakers infiltrate successfully, reducing Orange fitness. | **Wrong C (distractor check):** C is the correct answer. | **Wrong D:** Blue is not a stable ESS alone — when Blue is common, Orange males outcompete Blue territorially. | **Wrong E:** The morphs are maintained by frequency-dependent selection (each morph is favored when rare), not neutral mutation-selection balance.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which statements about the side-blotched lizard system are TRUE? (I) Orange throat males control large territories and outcompete blue males (II) Yellow \"sneaker\" males mimic females to enter orange territories undetected (III) Blue mate-guarders can detect and block yellow sneakers (IV) The equilibrium reached is a fixed mixed-strategy ESS like the Hawk-Dove game",
      "choices": [
        "I and II only",
        "I, II, and IV",
        "II, III, and IV",
        "I, II, and III only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (Orange outcompetes Blue territorially), II (Yellow sneakers mimic females to infiltrate Orange territories), and III (Blue mate-guarders recognize and block Yellow sneakers) are all true. | **Wrong A:** Misses III, which is also true — Blue's advantage over Yellow comes precisely from the mate-guarding ability to detect sneakers. | **Wrong B:** IV is FALSE — the side-blotched lizard system produces a CYCLIC ESS where frequencies oscillate over years, NOT a fixed mixed-strategy equilibrium like Hawk-Dove. | **Wrong C:** IV is false; see above. | **Wrong E:** IV is false, eliminating \"all of the above.\"",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which correctly describes the step-by-step cycle in side-blotched lizard morph frequencies over multiple years?",
      "choices": [
        "(1) Orange frequent → controls large territories → Yellow sneakers infiltrate easily → (2) Yellow spreads as Orange frequency rises → (3) Blue mate-guarders who recognize sneakers do better when Yellow is common → Blue spreads → (4) Blue males guard individually and are outcompeted territorially by aggressive Orange males when Blue is common → Orange spreads → back to step 1",
        "(1) Blue frequent → mate-guarders dominate → Orange invades because dominance beats guarding → (2) Orange spreads → Yellow invades because sneakers enter unguarded territories → (3) Yellow spreads → Blue invades because guarding beats sneaking → (4) Back to step 1 — cycle runs Blue → Orange → Yellow → Blue",
        "(1) All three morphs start at equal frequency; (2) Random genetic drift shifts one morph to fixation; (3) The fixed morph is then invaded by one of the others; (4) The cycle repeats but each morph reaches fixation before replacement — no true cycling equilibrium",
        "(1) Yellow sneakers are always most common because mimicry is the most successful strategy; (2) Orange and Blue persist only due to genetic drift; (3) The cycle is not driven by frequency-dependent selection but by environmental fluctuation",
        "(1) Orange beats Yellow, Yellow beats Blue, Blue beats Orange — the dominance order is Orange > Yellow > Blue; (2) This creates a linear hierarchy, not a cycle; (3) Orange eventually fixes in the population as the dominant ESS"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct cycle follows the RPS dominance order: Orange (large territory) → exploited by Yellow (sneaker) → Blue (guarding) detects Yellow → Blue outperformed by Orange (territorial dominance) → cycle continues. This is frequency-dependent cycling over observable multi-year timescales. | **Wrong B:** Reverses the dominance order — Blue does NOT beat Orange; Orange outcompetes Blue territorially. The cycle stated (Blue → Orange → Yellow → Blue) inverts the actual dominance relationships. | **Wrong C:** The cycle does NOT involve fixation of any morph — all three are maintained in the population simultaneously through ongoing frequency dependence, not sequential fixation events. | **Wrong D:** Yellow is not permanently dominant; Yellow's advantage is specific to when Orange is common. The cycle is driven by frequency-dependent selection, not random environmental variation. | **Wrong E:** The dominance relationships are not linear — they form a cycle (Orange beats Blue, Blue beats Yellow, Yellow beats Orange), not a hierarchy where Orange always wins.",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which does NOT correctly describe an evolutionarily stable strategy (ESS)?",
      "choices": [
        "An ESS cannot be invaded by a rare alternative mutant strategy when it is already common in the population",
        "At a mixed ESS equilibrium, all strategies present in the population have equal fitness",
        "An ESS is stable because it always produces the highest possible fitness for every individual in the population",
        "ESS payoffs are frequency-dependent — the fitness of a strategy depends on what other strategies are present",
        "The Rock-Paper-Scissors cycling in side-blotched lizards is a cyclic form of ESS distinct from the fixed mixed-strategy ESS of Hawk-Dove"
      ],
      "answer": 2,
      "why": "&#9989; **C.** An ESS is stable because it CANNOT BE INVADED by rare mutant strategies — it does NOT necessarily maximize individual fitness. In Hawk-Dove, both Hawks and Doves at the ESS frequency have EQUAL fitness, not maximum individual fitness. A pure Dove in an all-Dove population would get V/2, which might be higher, but pure Dove is not an ESS because Hawks can invade. | **Wrong A:** Invasion resistance is the correct defining property of an ESS. | **Wrong B:** Equal fitness of coexisting strategies at mixed ESS equilibrium is correct — this is what prevents either strategy from increasing. | **Wrong D:** Frequency-dependence is the core feature that makes ESS a game-theoretic concept. | **Wrong E:** Correctly distinguishes the two ESS types — Hawk-Dove (fixed mixed) vs. RPS (cyclic).",
      "sectionId": "s_ess",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "An altruistic act costs an individual 3 offspring (C=3) and benefits a full sibling (r=0.5) by 10 offspring (B=10). Is this act favored by kin selection?",
      "choices": [
        "No — the direct cost (3 offspring) exceeds the indirect benefit (10 × 0.5 = 5) rB = 5, which is greater than C = 3, so we need to recalculate",
        "Yes — rB = 0.5 × 10 = 5 > C = 3; the indirect fitness gain exceeds the direct cost",
        "No — kin selection only applies when r ≥ 0.5",
        "Cannot be determined without knowing the total population size",
        "Yes — and the cost C must also be multiplied by r = 0.5, giving an adjusted cost of 1.5, so the net gain is 5 − 1.5 = 3.5 offspring equivalents"
      ],
      "answer": 1,
      "why": "&#9989; **B.** Apply Hamilton's Rule: rB > C? rB = 0.5 × 10 = 5. C = 3. 5 > 3 = YES, this act IS favored. The altruist loses 3 units of direct fitness but gains 5 units of indirect fitness (through their sibling's enhanced reproduction, weighted by r). Net inclusive fitness change = +2. The altruist's alleles come out ahead. | **Wrong E:** The cost C is NEVER multiplied by r — the actor pays 100% of their own cost regardless of relatedness; only the benefit B is discounted by r because benefits only propagate shared alleles in proportion to relatedness.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "In a haplodiploid (Hymenoptera) bee colony, a worker bee is related to her full SISTERS at r=0.75. What is her relatedness to her mother (the queen)?",
      "choices": [
        "r = 0.75 — the same as sister relatedness in haplodiploidy",
        "r = 0.5 — same as parent-offspring relatedness in diploid organisms",
        "r = 0.25 — brothers and mother have the same relatedness in haplodiploidy",
        "r = 1.0 — the queen passes her entire genome to female workers",
        "r = 0.375 — the average of sister relatedness (0.75) and brother relatedness (0.25) divided by two, because workers are equally related to all siblings on average"
      ],
      "answer": 1,
      "why": "&#9989; **B.** In haplodiploidy: worker's relatedness to QUEEN (mother) = 0.5 (same as normal diploid parent-offspring). The extraordinary relatedness is to SISTERS (r = 0.75) because: sisters share ALL of the father's genome (father is haploid → all sperm identical) plus half of mother's genome. This asymmetry (sisters r=0.75 vs. own offspring r=0.5) is what theoretically makes raising sisters MORE genetically profitable than having your own children. | **Wrong E:** Relatedness to the queen (mother) is calculated directly from the mother-offspring genetic relationship (r = 0.5), not as an average of sibling relatednesses; averaging sibling values does not give the parent-offspring coefficient.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which scenario satisfies Hamilton's Rule (rB > C) and predicts that altruism WILL evolve, satisfying ALL conditions with specific numbers?",
      "choices": [
        "r=0.25 (half-sibling), B=4 offspring gained, C=3 offspring lost: rB = 0.25×4 = 1.0, C = 3; 1.0 < 3 → altruism NOT favored",
        "r=0.125 (first cousin), B=20 offspring gained, C=3 offspring lost: rB = 0.125×20 = 2.5, C = 3; 2.5 < 3 → altruism NOT favored",
        "r=0.5 (full sibling), B=10 offspring gained, C=3 offspring lost: rB = 0.5×10 = 5, C = 3; 5 > 3 → altruism IS favored",
        "r=0.5 (full sibling), B=4 offspring gained, C=3 offspring lost: rB = 0.5×4 = 2, C = 3; 2 < 3 → altruism NOT favored",
        "r=0 (unrelated individual), B=100 offspring gained, C=1 offspring lost: rB = 0×100 = 0, C = 1; 0 < 1 → altruism NOT favored even with huge benefit"
      ],
      "answer": 2,
      "why": "&#9989; **C.** r=0.5, B=10, C=3: rB = 5 > C = 3 → altruism is favored by kin selection. Net inclusive fitness gain = +2 offspring equivalents. | **Wrong A:** rB=1 < C=3 — the rule is not satisfied; altruism is not favored. | **Wrong B:** rB=2.5 < C=3 — just below threshold; altruism not favored. | **Wrong D:** rB=2 < C=3 — not satisfied despite full-sibling relatedness; the B value is too low. | **Wrong E:** When r=0, no relatedness exists; any cost makes altruism unfavored via kin selection regardless of B magnitude.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which statements about Hamilton's Rule (rB > C) are TRUE? (I) Only the benefit B is multiplied by relatedness r; the cost C is paid in full by the actor (II) r for full siblings in diploids = 0.5 (III) r for full sisters in haplodiploidy (Hymenoptera) = 0.75 (IV) Group selection is generally stronger than kin selection in maintaining cooperation",
      "choices": [
        "I and II only",
        "I, II, and IV",
        "I, II, and III only",
        "II, III, and IV",
        "All of the above"
      ],
      "answer": 2,
      "why": "&#9989; **C.** I (only B is discounted by r; C is paid in full), II (diploid full siblings r=0.5), and III (haplodiploid full sisters r=0.75) are all true. | **Wrong A:** Misses III, which is also true. | **Wrong B:** IV is FALSE — group selection is generally WEAKER than individual (kin) selection; within-group selfish individuals consistently outcompete cooperators unless kin selection or other mechanisms operate. | **Wrong D:** IV is false. | **Wrong E:** IV is false.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which correctly describes the step-by-step mechanism by which haplodiploidy raises the potential for eusociality in Hymenoptera?",
      "choices": [
        "(1) Females develop from fertilized eggs (diploid); males from unfertilized eggs (haploid); (2) Father produces genetically identical sperm (haploid); (3) Full sisters share ALL of father's genome + half of mother's = r=0.75; (4) r to own offspring = 0.5; (5) Helping raise sisters can yield higher inclusive fitness than reproducing independently; (6) BUT haplodiploidy alone is insufficient — many haplodiploid species are not eusocial",
        "(1) Males and females both develop from fertilized eggs; (2) Full sisters share 75% of genes by chance; (3) r=0.75 applies to both brothers and sisters; (4) Workers maximize inclusive fitness by raising any sibling equally; (5) Haplodiploidy always causes eusociality in species where it occurs",
        "(1) Females are haploid; males are diploid; (2) Full sisters share half their genes as in diploid species; (3) r=0.5 for sisters in haplodiploidy; (4) No special relatedness asymmetry exists; (5) Eusociality in Hymenoptera must be explained by ecological constraints alone",
        "(1) Males develop from fertilized eggs; females from unfertilized eggs; (2) Full sisters share only maternal genes; (3) r=0.25 for sisters; (4) Workers are less related to sisters than to own offspring; (5) Kin selection actually opposes eusociality in haplodiploidy",
        "(1) All Hymenoptera are haplodiploid; (2) r=0.75 between sisters means workers always gain more inclusive fitness helping than reproducing; (3) Hamilton's Rule is always satisfied for worker behavior; (4) Therefore all haplodiploid species are obligate eusocial; (5) No exceptions exist"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism: haploid fathers produce identical sperm → sisters share all paternal genes + half maternal = r=0.75 > r=0.5 to own offspring → kin selection can favor worker behavior. But haplodiploidy is not sufficient alone — many haplodiploid species are solitary. | **Wrong B:** Males are haploid (from unfertilized eggs), not diploid; r=0.75 does NOT apply to brothers (brothers share only maternal genes with workers, r=0.25). | **Wrong C:** Inverts the sex chromosome logic — females are diploid, males are haploid in Hymenoptera. | **Wrong D:** Completely inverts the sex determination system; females develop from fertilized eggs (diploid), males from unfertilized (haploid). | **Wrong E:** Haplodiploidy is neither necessary nor sufficient for eusociality — termites (diploid) are eusocial; many haplodiploid bees/wasps are solitary.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which does NOT correctly apply Hamilton's Rule?",
      "choices": [
        "A worker bee helping raise 4 full sisters (r=0.75 each) gain 2 offspring each, at a cost of 3 own offspring: rB = 0.75×8 = 6 > C = 3 → favored",
        "A ground squirrel giving an alarm call that saves 2 full siblings (r=0.5 each) who each gain 3 offspring, at a cost of 1 own offspring: rB = 0.5×6 = 3 > C = 1 → favored",
        "If r=0 between two individuals, altruism can still evolve via kin selection because group benefits exceed individual costs when the group is large enough",
        "Haldane's quip \"I would lay down my life for 2 brothers or 8 cousins\" correctly applies rB > C: 2 × r(0.5) = 1.0 ≥ C(1.0) and 8 × r(0.125) = 1.0 ≥ C(1.0)",
        "A meerkat sentinel whose alarm call benefits 4 full siblings (r=0.5) each gaining 1 offspring, at a cost of 0.5 own offspring: rB = 0.5×4 = 2 > C = 0.5 → favored"
      ],
      "answer": 2,
      "why": "&#9989; **C.** This misapplies Hamilton's Rule: when r=0, kin selection cannot operate regardless of group size or benefit magnitude. rB = 0×B = 0, which is never > C > 0. Group benefits with r=0 would require a different mechanism (reciprocal altruism, group selection) — not kin selection via Hamilton's Rule. | **Wrong A:** Correctly applies the rule: rB = 0.75×(4×2) = 6 > 3. | **Wrong B:** Correctly applies the rule: rB = 0.5×(2×3) = 3 > 1. | **Wrong D:** Haldane's quip is a correct break-even application of the rule. | **Wrong E:** Correctly applies the rule: rB = 0.5×4 = 2 > 0.5.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Group selection is generally considered WEAKER than individual selection in most scenarios because:",
      "choices": [
        "Groups reproduce too slowly for selection to act effectively",
        "Within-group selection consistently favors SELFISH individuals (who defect/cheat), and these spread within the group even if they harm the group as a whole — unless other mechanisms (kin selection, punishment) oppose this",
        "Groups do not have heritable genetic variation, only individuals do",
        "Group selection requires geographic isolation which is rarely achieved",
        "Group selection is irrelevant because all cooperation in nature is explained by direct reciprocity alone"
      ],
      "answer": 1,
      "why": "&#9989; **B.** The fundamental problem with group selection: even if groups of cooperators outcompete groups of selfish individuals, WITHIN each cooperating group, selfish mutants have higher individual fitness than cooperators. Selfish individuals spread WITHIN the group → eventually all cooperators converted → group fails. The within-group selection against altruism is typically stronger than between-group selection favoring it. Kin selection &ldquo;solves&rdquo; this by making the group also be relatives. | **Wrong E:** Direct reciprocity (tit-for-tat) is one mechanism maintaining cooperation, but kin selection, punishment, and other mechanisms also contribute — cooperation is not exclusively maintained by reciprocity.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which of the following CORRECTLY explains why group selection is generally considered WEAK, satisfying ALL criteria: within-group selection favors selfishness, between-group selection favors cooperation, within-group selection usually stronger, and selfish individuals spread even in cooperative groups?",
      "choices": [
        "Group selection is weak because groups do not have heritable genetic variation — only individuals have genes that can be selected",
        "Group selection is weak because cooperating groups never outcompete selfish groups — cooperation is always a net disadvantage at every level of organization",
        "Within any group, selfish individuals consistently have higher fitness than cooperators, so within-group selection overcomes between-group selection unless groups are extremely isolated",
        "Group selection is weak because geographic barriers required for group isolation are rarely found in nature, preventing groups from diverging in cooperative behavior",
        "Group selection is weak because cooperators and defectors always mix freely between groups, preventing any group from becoming more cooperative than others"
      ],
      "answer": 2,
      "why": "&#9989; **C.** All four criteria satisfied: within-group selection consistently favors selfish individuals (they have higher relative fitness than cooperators), between-group selection can favor cooperation (cooperative groups do better), but within-group selection typically overcomes between-group selection, so selfish alleles spread even within initially cooperative groups. | **Wrong A:** Groups DO have heritable variation (in group composition and cooperative norms) — the problem is not absence of heritability but the direction of within-group selection. | **Wrong B:** Cooperative groups CAN outcompete selfish groups (between-group selection is real); the problem is that this is overwhelmed by within-group selfishness, not that cooperation never helps at group level. | **Wrong D:** Geographic isolation is not required for group selection theory — the weakness is a logical/selective one, not a geographic one. | **Wrong E:** While mixing does weaken group selection, the fundamental problem is within-group selection dynamics even in structured populations.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which statements correctly describe the multi-level selection framework? (I) Total selection = within-group selection + between-group selection (II) Within-group selection consistently favors selfish individuals over cooperators (III) Cooperative groups consistently outcompete selfish groups, making group selection strong (IV) Kin selection is more effective than group selection because it works via individual inclusive fitness, not group productivity",
      "choices": [
        "I and II only",
        "I, II, and III",
        "II and IV only",
        "I, II, and IV only",
        "All of the above"
      ],
      "answer": 3,
      "why": "&#9989; **D.** I (multi-level selection framework correctly defined), II (within-group selection consistently favors selfishness), and IV (kin selection operates via individual inclusive fitness and is better supported than group selection) are all true. | **Wrong A:** Misses IV, which is also true. | **Wrong B:** III is FALSE — while cooperative groups CAN outcompete selfish groups in some scenarios, the claim that this makes group selection STRONG is incorrect; within-group dynamics typically overwhelm between-group advantages. | **Wrong C:** Misses I, which is also true; the multi-level framework is a real and important conceptual tool. | **Wrong E:** III is false, eliminating \"all of the above.\"",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Why did Wynne-Edwards' group selection hypothesis fail? Which correctly describes the mechanism?",
      "choices": [
        "(1) Wynne-Edwards proposed animals voluntarily limit reproduction for group benefit; (2) Suppose a mutation arises: one individual reproduces at full capacity instead of restraining; (3) This individual leaves more offspring than restrained neighbors; (4) The \"selfish\" allele spreads within the group each generation; (5) Eventually voluntary restraint is eliminated from within; (6) Group selection cannot prevent within-group spread of selfishness",
        "(1) Wynne-Edwards proposed animals limit reproduction voluntarily; (2) Groups with restrained individuals go extinct because they have too few offspring; (3) Only non-restrained groups survive; (4) Wynne-Edwards' model fails because it predicts extinction of cooperative groups, not their success",
        "(1) Wynne-Edwards' hypothesis requires geographic isolation that never occurs; (2) Without isolation, restrained and unrestrained individuals interbreed freely; (3) Restraint alleles are diluted by gene flow each generation; (4) The failure is entirely due to gene flow, not within-group selection",
        "(1) Voluntary restraint does evolve via group selection; (2) Wynne-Edwards was correct; (3) The hypothesis failed only because of insufficient data, not logical flaws; (4) Modern multi-level selection theory fully vindicates group selection as equally powerful as individual selection",
        "(1) Voluntary restraint alleles are maintained by kin selection — related individuals in the group benefit; (2) Wynne-Edwards' hypothesis and kin selection make identical predictions; (3) The two theories are equivalent and both well-supported; (4) Distinguishing them requires no additional evidence"
      ],
      "answer": 0,
      "why": "&#9989; **A.** The correct mechanism of failure: within any group of restrainers, a selfish mutant that ignores the group benefit and reproduces fully has higher individual fitness → spreads within the group → replaces the restraint allele → group cooperation collapses from within. | **Wrong B:** Inverts the logic — groups WITH restrained reproduction would have fewer offspring per individual but groups of restrainers would be more stable; the problem is not that cooperative groups go extinct but that selfishness spreads within them. | **Wrong C:** Gene flow can weaken group selection, but the fundamental logical flaw is within-group individual selection, which operates even in isolated populations. | **Wrong D:** Wynne-Edwards' hypothesis is widely considered flawed on logical grounds; modern multi-level selection does NOT vindicate group selection as equally powerful as individual selection in most circumstances. | **Wrong E:** Kin selection and group selection are NOT equivalent — kin selection operates via individual inclusive fitness; equating them confuses two distinct mechanisms.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "Which does NOT correctly explain why kin selection is NOT the same as group selection?",
      "choices": [
        "Kin selection works through individual inclusive fitness — the actor's alleles propagate when related recipients reproduce; group productivity is not the currency",
        "Group selection requires that whole groups differ in fitness; kin selection requires only that the actor and recipient share alleles by descent",
        "An individual can help a single relative in isolation with no other group members present — kin selection operates without requiring a group context",
        "Kin selection requires that related individuals act together as a group, making it equivalent to group selection",
        "Kin selection is mathematically well-supported by Hamilton's Rule; group selection is generally considered weak because within-group selection opposes it"
      ],
      "answer": 3,
      "why": "&#9989; **D.** This is FALSE — kin selection does NOT require group action. An individual can help a single relative in isolation (e.g., a bee that helps only its queen mother). Kin selection works through individual inclusive fitness calculations, not group membership or collective action. Calling kin selection equivalent to group selection is the conceptual error this answer illustrates. | **Wrong A:** Correctly distinguishes kin selection (individual inclusive fitness) from group selection (group productivity). | **Wrong B:** Correctly identifies the different units of selection: groups vs. dyadic relatedness. | **Wrong C:** Correctly demonstrates that kin selection does not require a group context — a single helping act between two relatives suffices. | **Wrong E:** Correctly summarizes the empirical and theoretical status of the two mechanisms.",
      "sectionId": "s_altruism",
      "chapterId": "ch_s_ch16"
    },
    {
      "prompt": "A paleontologist finds volcanic ash surrounding a ~2 million year old hominin fossil. Which isotope system is most appropriate?",
      "choices": [
        "Carbon-14 — hominins are relatively recent",
        "Potassium-Argon — works on volcanic rock in the million-year range",
        "Uranium-Lead — longest half-life so most accurate",
        "Rubidium-Strontium — most precise for organic material",
        "Electron spin resonance — best for dating volcanic minerals in this range"
      ],
      "answer": 1,
      "why": "**B.** K-Ar (half-life 1.3 bya) is ideal for volcanic rock in the million-year range. C-14 only reaches ~50,000 years. Volcanic ash resets the clock when it solidifies — perfect for K-Ar. | **Wrong E:** Electron spin resonance dates tooth enamel and shells, not volcanic ash; K-Ar is the standard for volcanic rock in the million-year range.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "Why was Lord Kelvin's estimate of Earth's age (~20 million years) wrong?",
      "choices": [
        "He used variable sediment accumulation rates",
        "He lacked access to deep mantle rock cores",
        "He didn't know radioactive decay generates heat continuously inside Earth, invalidating his passive cooling model",
        "He relied on Darwin's inaccurate sediment estimates",
        "He assumed Earth formed from a cold accretion disk and never had internal heat"
      ],
      "answer": 2,
      "why": "**C.** Kelvin assumed Earth cooled passively. Radioactive decay generates heat continuously internally — making his cooling model invalid. Darwin's sediment-based estimate was independent and closer to correct. | **Wrong E:** Kelvin actually assumed a hot initial state cooling over time; his error was ignoring internal heat generation from radioactive decay, not the starting conditions.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which property of radioactive isotopes makes radiometric dating reliable for establishing absolute ages of rocks?",
      "choices": [
        "The decay rate speeds up when temperatures rise above 100°C",
        "Daughter isotopes are volatile and escape from the mineral lattice over time",
        "Half-lives can be calibrated using known historical eruption dates",
        "The half-life of each isotope is constant regardless of temperature, pressure, or chemical environment",
        "Parent isotopes are replenished by cosmic-ray bombardment of minerals"
      ],
      "answer": 3,
      "why": "**D.** Constant half-lives under all physical conditions are what make radiometric clocks reliable. | **A fails:** decay rates are unaffected by temperature. | **B fails:** daughter retention (not escape) is what is measured. | **C fails:** calibration is unnecessary because decay constants are measured in the lab. | **E fails:** cosmic rays produce cosmogenic nuclides only at the surface, not deep minerals.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following statements about radiometric dating are TRUE?**I. Carbon-14 dating is suitable for material up to ~50,000 years old.**II. Potassium-40 decays to Argon-40 with a half-life of ~1.25 billion years.**III. Uranium-Lead dating can be used on zircon crystals billions of years old.**IV. Carbon-14 can reliably date dinosaur bones from the Cretaceous (~66 Ma).",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and III are all correct. | **IV fails:** C-14 half-life is ~5,730 years; after 50,000 years essentially no C-14 remains, making it useless for 66-million-year-old fossils.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "In K-Ar (potassium-argon) dating of a volcanic rock, what happens at the moment of lava crystallization that \"resets\" the radiometric clock?",
      "choices": [
        "Argon-40 is trapped in the crystal lattice at a known initial concentration",
        "All previously accumulated radiogenic Ar-40 escapes as a gas, so the mineral starts with zero Ar-40",
        "Potassium-40 concentration is set to a fixed ratio by the high temperature",
        "Cosmic radiation converts surface K-40 to Ar-40 at a calibrated rate",
        "The crystal lattice preferentially incorporates Ar-40 from the melt"
      ],
      "answer": 1,
      "why": "**B.** At high temperatures Ar-40 diffuses out of the mineral; upon cooling the lattice seals and any subsequent Ar-40 accumulates from K-40 decay, recording elapsed time. | **A fails:** initial Ar-40 is effectively zero, not \"known.\" | **C fails:** K concentration is not reset. | **D fails:** cosmic rays are irrelevant to K-Ar. | **E fails:** crystals exclude noble gases.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following does NOT correctly describe radioactive half-life?",
      "choices": [
        "After one half-life, 50% of the original parent isotope remains",
        "After two half-lives, 25% of the original parent isotope remains",
        "The half-life of a parent isotope decreases as the parent concentration decreases over time",
        "Different isotopes have vastly different half-lives ranging from milliseconds to billions of years",
        "Half-life is independent of the initial quantity of the parent isotope"
      ],
      "answer": 2,
      "why": "**C.** Half-life is constant — it does not change as parent atoms are consumed. This is the defining property of first-order radioactive decay. | **A, B, D, E** are all accurate statements about half-life.",
      "sectionId": "c31",
      "chapterId": "ch3"
    },
    {
      "prompt": "What makes RNA uniquely suited for the RNA World hypothesis?",
      "choices": [
        "RNA is more stable than DNA for long-term storage",
        "RNA was found in the Murchison meteorite proving space origin",
        "RNA can replicate itself without any enzymes unlike DNA",
        "RNA can both store genetic information AND catalyze reactions (ribozymes) — bifunctional",
        "RNA uses thymine instead of uracil, making it more chemically versatile than DNA"
      ],
      "answer": 3,
      "why": "**D.** RNA's bifunctionality = the key. DNA only stores. Proteins only catalyze. RNA does both — hence the hypothetical original molecule of life. | **Wrong E:** RNA uses uracil, not thymine; DNA uses thymine. This distinction does not explain RNA World suitability.",
      "sectionId": "c32",
      "chapterId": "ch3"
    },
    {
      "prompt": "The Principle of Superposition applies when which set of conditions is met?",
      "choices": [
        "Rocks have been metamorphosed, erasing original layering",
        "Tectonic forces have overturned the strata since deposition",
        "Only igneous intrusions are present, with no sedimentary layers",
        "Sedimentary strata have not been overturned and are roughly horizontal",
        "Radioactive isotopes have been measured to confirm absolute ages"
      ],
      "answer": 3,
      "why": "**D.** Superposition requires undisturbed, roughly horizontal strata — lower layers were deposited first and are therefore older. | **A fails:** metamorphism destroys original layering. | **B fails:** overturned strata invert the age order. | **C fails:** the principle applies to sedimentary, not igneous, sequences. | **E fails:** superposition is a relative-dating principle; isotope measurement is absolute dating.",
      "sectionId": "c32",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which statements about relative dating using stratigraphy are TRUE?**I. Index fossils are of organisms that lived for long time spans and are geographically restricted.**II. The principle of cross-cutting relationships states that a fault is younger than the rock it cuts.**III. Unconformities represent gaps in the rock record caused by erosion or non-deposition.**IV. Correlation allows matching of strata across different geographic locations.",
      "choices": [
        "I and II only",
        "II and III only",
        "I, III, and IV only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 3,
      "why": "**D.** Statements II, III, and IV are correct. | **I fails:** index fossils are of organisms with SHORT time spans (so they are stratigraphically precise) but WIDE geographic ranges — the opposite of the statement.",
      "sectionId": "c32",
      "chapterId": "ch3"
    },
    {
      "prompt": "A geologist finds a fault cutting through three sedimentary layers but stopping below a fourth overlying layer. What is the correct temporal interpretation?",
      "choices": [
        "The fault formed before all four layers were deposited",
        "The fault formed after the fourth (top) layer was deposited",
        "The fault formed after the bottom three layers but before the fourth layer was deposited",
        "The fourth layer is older than the fault because it is closer to the surface",
        "No temporal relationship can be inferred from cross-cutting alone"
      ],
      "answer": 2,
      "why": "**C.** Cross-cutting relationships: the fault must post-date all rocks it cuts (layers 1-3) and pre-date rocks it does not cut (layer 4). | **A fails:** the fault cuts layers 1-3, so it post-dates them. | **B fails:** the fault does not cut layer 4. | **D fails:** proximity to surface does not determine age. | **E fails:** cross-cutting relationships are a foundational relative-dating tool.",
      "sectionId": "c32",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following does NOT represent a method of relative dating?",
      "choices": [
        "Principle of superposition",
        "Cross-cutting relationships",
        "Index fossil correlation",
        "Identification of unconformities",
        "Uranium-lead isotope ratio measurement"
      ],
      "answer": 4,
      "why": "**E.** U-Pb isotope ratio measurement yields an absolute (numerical) age, not a relative age. | **A–D** are all classic relative-dating methods that establish sequence without numerical dates.",
      "sectionId": "c32",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which ordering is correct oldest to most recent?",
      "choices": [
        "Biomarkers → Stromatolites → Eukaryotes → Multicellular eukaryotes",
        "Stromatolites → Biomarkers → Multicellular eukaryotes → Eukaryotes",
        "Eukaryotes → Biomarkers → Stromatolites → Multicellular eukaryotes",
        "Biomarkers → Eukaryotes → Stromatolites → Multicellular eukaryotes",
        "Multicellular eukaryotes → Eukaryotes → Biomarkers → Stromatolites"
      ],
      "answer": 0,
      "why": "**A.** Biomarkers 3.8 bya, stromatolites 3.45 bya, eukaryotes 1.8 bya, multicellular eukaryotes (red algae) 1.2 bya. | **Wrong E:** This reverses the actual timeline; simpler forms (biomarkers, stromatolites) appeared billions of years before complex multicellular eukaryotes.",
      "sectionId": "c33",
      "chapterId": "ch3"
    },
    {
      "prompt": "A fossil qualifies as a \"transitional form\" when it exhibits which combination of features?",
      "choices": [
        "Exclusively ancestral features with no derived characters of the descendant group",
        "Exclusively derived features of the descendant group only",
        "A mosaic of ancestral and derived characters linking two major groups",
        "Features identical to a living species plus soft-tissue preservation",
        "Stratigraphic position exactly intermediate between two named species"
      ],
      "answer": 2,
      "why": "**C.** Transitional forms are mosaics — they retain some ancestral features while possessing derived features of the descendant clade, documenting evolutionary change. | **A fails:** purely ancestral forms are not transitional. | **B fails:** purely derived forms belong to the descendant group. | **D fails:** soft-tissue preservation is not required. | **E fails:** exact stratigraphic intermediacy is not a requirement.",
      "sectionId": "c33",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following are considered well-documented transitional fossils?**I. Archaeopteryx — showing both reptilian teeth/claws and avian feathers/wishbone.**II. Pakicetus — an early whale relative with functional legs.**III. Tiktaalik — a lobe-finned fish with a neck and proto-limb fins.**IV. Dimetrodon — a transitional form between fish and amphibians.",
      "choices": [
        "I only",
        "I and III only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four are transitional fossils"
      ],
      "answer": 2,
      "why": "**C.** Archaeopteryx, Pakicetus, and Tiktaalik are classic transitional fossils in the dinosaur-to-bird, land-mammal-to-whale, and fish-to-tetrapod transitions respectively. | **IV fails:** Dimetrodon is a synapsid (stem mammal) transitional to mammals, not a fish-to-amphibian transitional form.",
      "sectionId": "c33",
      "chapterId": "ch3"
    },
    {
      "prompt": "What sequence of evolutionary changes does the fossil record of whale evolution (cetacean origins) document?",
      "choices": [
        "Terrestrial artiodactyl ancestors → semi-aquatic forms with reduced hind limbs → fully aquatic whales with vestigial pelvis",
        "Aquatic fish → amphibious crawlers → terrestrial mammals → secondarily aquatic whales",
        "Reptilian mosasaurs → archaeocetes → modern mysticetes and odontocetes",
        "Small rodent-like insectivores → pinnipeds → whales over 10 million years",
        "Marine ichthyosaurs convergently evolved into modern cetaceans"
      ],
      "answer": 0,
      "why": "**A.** Cetacean evolution: terrestrial artiodactyls (e.g., Pakicetus) became semi-aquatic (Ambulocetus), then lost functional hind limbs, retaining only vestigial pelvic bones. | **B fails:** whales evolved from land mammals, not from fish directly. | **C fails:** mosasaurs are not whale ancestors. | **D fails:** rodents are not cetacean ancestors. | **E fails:** ichthyosaur-cetacean similarity is convergent, not ancestral.",
      "sectionId": "c33",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following does NOT support the existence of transitional forms in the fossil record?",
      "choices": [
        "Archaeopteryx preserves both feathers and reptilian teeth in the same specimen",
        "The sequence of Pakicetus → Ambulocetus → Rodhocetus documents limb reduction in whale ancestors",
        "Tiktaalik possesses wrist bones and a neck absent in typical fish",
        "Thrinaxodon shows both reptilian and mammalian jaw bone features",
        "The Cambrian Explosion shows the sudden appearance of animal phyla without obvious precursors"
      ],
      "answer": 4,
      "why": "**E.** The Cambrian Explosion is often cited as a challenge to gradual transitional sequences, not as support for them. | **A–D** all directly demonstrate mosaic transitional features bridging major taxonomic groups.",
      "sectionId": "c33",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which period is the \"Age of Fishes\" AND saw first vertebrates with legs?",
      "choices": [
        "Silurian — first land animals including early vertebrates",
        "Carboniferous — amphibians were first land vertebrates",
        "Devonian — predatory fish dominated; tetrapod fossils appear ~370 mya",
        "Ordovician — early bony fishes alongside tetrapod evolution",
        "Permian — synapsids evolved limbs for terrestrial locomotion during this period"
      ],
      "answer": 2,
      "why": "**C.** Devonian (416–359 mya) = Age of Fishes. Dunkleosteus 6m, Tiktaalik 375 mya, earliest tetrapods 370 mya. Silurian first land animal = millipede (invertebrate, not vertebrate). Carboniferous amphibians came AFTER Devonian tetrapods. | **Wrong E:** The Permian featured synapsid diversification, but the Age of Fishes and first tetrapods belong to the Devonian (416-359 mya), not Permian (299-251 mya).",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "Primary evidence the K-T extinction was caused by an asteroid impact?",
      "choices": [
        "Abrupt disappearance of dinosaur fossils at 66 mya",
        "Global iridium-rich layer at K-T boundary plus Chicxulub crater matching estimated size and age",
        "Carbon isotope shifts from Siberian Traps volcanism",
        "Rapid global cooling in deep-sea oxygen isotope ratios",
        "Presence of shocked quartz and tektites caused by gradual tectonic stress at plate boundaries"
      ],
      "answer": 1,
      "why": "**B.** Iridium (rare on Earth, rich in asteroids) found globally at K-T boundary. Chicxulub crater (Yucatan) matches ~10 km asteroid size and dates to 66 mya. Fossil disappearance (A) is the outcome. C describes the Permian extinction, not K-T. | **Wrong E:** Shocked quartz and tektites are actually impact indicators supporting the asteroid hypothesis, not products of gradual tectonic stress.",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "A valid monophyletic group (clade) must include which combination of taxa?",
      "choices": [
        "Only the most derived descendants of an ancestor, excluding basal lineages",
        "An ancestor and ALL of its descendants, with no exclusions",
        "Two or more lineages that share a convergent adaptation but not a common ancestor",
        "Any group of species that share at least one morphological character",
        "Taxa that are geographically co-distributed regardless of phylogenetic relationship"
      ],
      "answer": 1,
      "why": "**B.** A clade = an ancestor + all of its descendants. Leaving out any descendant creates a paraphyletic group (e.g., \"Reptilia\" excluding birds). | **A fails:** excluding basal lineages creates paraphyly. | **C fails:** sharing convergent traits without common ancestry defines polyphyly. | **D fails:** shared morphology can be convergent and does not define a clade. | **E fails:** geography is irrelevant to clade membership.",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which statements about cladistic analysis are TRUE?**I. Synapomorphies (shared derived characters) are used to define clades.**II. Symplesiomorphies (shared ancestral characters) are informative for grouping taxa into derived clades.**III. Parsimony favors the phylogenetic tree requiring the fewest evolutionary changes.**IV. Outgroup comparison helps determine which character states are ancestral versus derived.",
      "choices": [
        "I only",
        "I and III only",
        "I, III, and IV only",
        "I, II, and III only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, III, and IV are correct. | **II fails:** symplesiomorphies (ancestral shared characters) are NOT informative for defining derived clades — they pre-date the split and are shared by the outgroup too. Only synapomorphies define clades.",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "When constructing a cladogram by parsimony, what is the correct sequence of steps?",
      "choices": [
        "Identify characters → polarize as ancestral/derived using outgroup → score taxa → find tree with minimum steps",
        "Choose taxa → measure genetic distance → group by overall similarity → draw UPGMA tree",
        "Identify convergent characters → remove them → group remaining taxa by geography",
        "Score all morphological characters → weight derived characters more → use neighbor-joining",
        "Sequence mitochondrial DNA → align sequences → apply Bayesian relaxed clock model"
      ],
      "answer": 0,
      "why": "**A.** Parsimony cladistics: (1) select characters, (2) polarize using an outgroup, (3) build character matrix, (4) find the most parsimonious tree (fewest implied changes). | **B fails:** UPGMA uses overall distance, not parsimony. | **C fails:** convergent characters are handled by parsimony, not removed. | **D fails:** parsimony does not weight characters. | **E fails:** Bayesian clock is a molecular method, not parsimony cladistics.",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "Which of the following does NOT correctly describe a paraphyletic group?",
      "choices": [
        "\"Reptilia\" (excluding birds) is paraphyletic because birds evolved from reptilian ancestors",
        "A paraphyletic group includes an ancestor but excludes some of its descendants",
        "\"Fish\" as traditionally defined is paraphyletic because tetrapods evolved from lobe-finned fish",
        "A paraphyletic group includes taxa from multiple independent evolutionary origins with no single common ancestor",
        "Paraphyletic groups are rejected in strict cladistic classifications"
      ],
      "answer": 3,
      "why": "**D.** That description defines a POLYPHYLETIC group (multiple independent origins), not paraphyletic. Paraphyletic groups DO have a single common ancestor — they just exclude some descendants. | **A, B, C, E** are all accurate descriptions of paraphyletic groups.",
      "sectionId": "c34",
      "chapterId": "ch3"
    },
    {
      "prompt": "\"Sister taxa\" in a phylogenetic tree are defined as:",
      "choices": [
        "All members of the same taxonomic family",
        "Lineages that share the root node of the entire tree",
        "Lineages that diverged from the same immediate ancestral node — each other's closest relatives",
        "Taxa sharing the same morphological traits regardless of ancestry",
        "The two oldest lineages branching from the root of the entire tree"
      ],
      "answer": 2,
      "why": "**C.** Sister taxa share the most recent common node — each other's closest relatives. They diverged from each other more recently than from any other taxon shown. | **Wrong E:** Root branches are the most basal divergence, not sister taxa; sister taxa share the same immediate ancestral node regardless of tree position.",
      "sectionId": "c41",
      "chapterId": "ch4"
    },
    {
      "prompt": "Natural selection will reliably change allele frequencies in a population when which set of conditions is met?",
      "choices": [
        "Traits are learned rather than inherited, and the environment is stable",
        "All individuals have identical genotypes and the environment fluctuates randomly",
        "Mutations occur at high rates but all variants have equal fitness",
        "The population is very large, mating is random, and no selection occurs",
        "There is heritable variation in a trait, and that variation correlates with differential reproductive success"
      ],
      "answer": 4,
      "why": "**E.** The three requirements for natural selection: (1) variation exists, (2) variation is heritable, (3) variation affects fitness (reproductive success). | **A fails:** learned traits are not inherited. | **B fails:** identical genotypes means no heritable variation. | **C fails:** equal fitness means no differential reproductive success. | **D fails:** this describes Hardy-Weinberg equilibrium, which PREVENTS allele-frequency change.",
      "sectionId": "c41",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which statements about modes of natural selection are TRUE?**I. Directional selection shifts the population mean toward one extreme phenotype.**II. Stabilizing selection reduces phenotypic variance and favors intermediate phenotypes.**III. Disruptive selection can maintain two distinct phenotypic peaks in one population.**IV. Sexual selection always opposes natural selection and reduces population fitness.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Directional, stabilizing, and disruptive selection are all accurately described. | **IV fails:** sexual selection is a form of natural selection; it can sometimes reduce survival (e.g., peacock tails) but increases reproductive success, so it does not always oppose overall fitness.",
      "sectionId": "c41",
      "chapterId": "ch4"
    },
    {
      "prompt": "In the peppered moth case study, what is the correct sequence of events that produced a shift toward melanic moths during industrialization?",
      "choices": [
        "Soot darkened tree bark → light moths became more visible to bird predators → dark moths had higher survival → dark allele frequency increased",
        "Soot caused mutations producing dark moths → dark moths were less toxic to birds → dark moths spread",
        "Dark moths migrated from unpolluted forests → outcompeted light moths for food → dark allele spread",
        "Industrialization increased temperature → dark moths had better thermoregulation → frequency increased",
        "Light moths lost camouflage and stopped reproducing entirely within one generation"
      ],
      "answer": 0,
      "why": "**A.** This is classic directional selection via differential predation: environmental change altered selective pressure, favoring pre-existing dark alleles. | **B fails:** soot did not cause mutations; variation pre-existed. | **C fails:** migration is not the mechanism. | **D fails:** thermoregulation was not the selective agent. | **E fails:** selection is gradual over many generations, not complete in one.",
      "sectionId": "c41",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which of the following does NOT represent a form of natural selection?",
      "choices": [
        "Larger-beaked finches surviving drought by cracking hard seeds",
        "Human birth weight being highest at intermediate values (not too large or small)",
        "Male peacocks with larger, more colorful tails gaining more mates",
        "Allele frequencies shifting in a small isolated population purely by random chance",
        "Two distinct color morphs both surviving better than intermediates in a heterogeneous habitat"
      ],
      "answer": 3,
      "why": "**D.** Random allele-frequency change in small populations is genetic drift, not natural selection. Selection requires differential survival/reproduction based on heritable traits. | **A** = directional, **B** = stabilizing, **C** = sexual, **E** = disruptive selection.",
      "sectionId": "c41",
      "chapterId": "ch4"
    },
    {
      "prompt": "A taxonomic group with a common ancestor and SOME but not all of its descendants is:",
      "choices": [
        "Monophyletic",
        "Paraphyletic",
        "Polyphyletic",
        "Holophyletic",
        "Cladistic — a formal hierarchical category in systematic classification"
      ],
      "answer": 1,
      "why": "**B.** Paraphyletic = ancestor + some descendants. Classic example: \"Reptiles\" without birds. | **Wrong E:** 'Cladistic' is not a group type; the correct term for ancestor + some (not all) descendants is paraphyletic.",
      "sectionId": "c42",
      "chapterId": "ch4"
    },
    {
      "prompt": "Genetic drift has its strongest effect on allele frequencies when which combination of conditions is present?",
      "choices": [
        "Population is very large, and selection is strong",
        "Population is large, mating is random, and migration is absent",
        "Population is very small, and chance events determine which individuals reproduce",
        "All alleles are selectively neutral, and the population is at carrying capacity",
        "Migration rate is high between multiple large subpopulations"
      ],
      "answer": 2,
      "why": "**C.** Drift is inversely proportional to population size (N); in small populations, sampling error dominates allele-frequency change. | **A fails:** large N minimizes drift. | **B fails:** large N + Hardy-Weinberg conditions minimize drift. | **D fails:** neutrality alone does not amplify drift; small N is required. | **E fails:** high migration among large populations counters drift.",
      "sectionId": "c42",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which statements about genetic drift are TRUE?**I. The bottleneck effect occurs when a population is drastically reduced, losing rare alleles by chance.**II. The founder effect occurs when a small group colonizes a new area, carrying a non-representative allele sample.**III. Genetic drift always moves allele frequencies in an adaptive direction.**IV. Genetic drift can lead to fixation or loss of alleles regardless of their fitness effects.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and IV only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and IV are correct. | **III fails:** drift is random — it is just as likely to fix a deleterious allele as a beneficial one.",
      "sectionId": "c42",
      "chapterId": "ch4"
    },
    {
      "prompt": "The Northern elephant seal was hunted to ~20 individuals in the 1890s. Which sequence of events best explains its current low genetic diversity?",
      "choices": [
        "Hunters selectively removed the most genetically diverse individuals, reducing diversity directionally",
        "Bottleneck reduced N to ~20 → rare alleles lost by chance → population recovered from few founders → low heterozygosity persists",
        "Small population size increased mutation rate → new alleles replaced old ones → diversity decreased",
        "Inbreeding caused lethal alleles to spread → diverse genotypes were eliminated by selection",
        "Migration to new habitat caused founder effect → only common alleles were carried to new range"
      ],
      "answer": 1,
      "why": "**B.** This is the classic bottleneck effect: extreme N reduction causes allele loss by sampling error; recovery from few survivors locks in reduced diversity. | **A fails:** hunters were not selectively targeting genetic diversity. | **C fails:** small N does not increase mutation rate. | **D fails:** inbreeding depression is a separate phenomenon. | **E fails:** elephant seals did not migrate; this is a bottleneck not a founder effect.",
      "sectionId": "c42",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which of the following does NOT describe a consequence or feature of genetic drift?",
      "choices": [
        "Drift can fix neutral or even slightly deleterious alleles in small populations",
        "Drift reduces genetic variation within a population over time",
        "Drift can cause different isolated populations to diverge genetically even without selection",
        "The founder effect is a special case of genetic drift involving colonization",
        "Drift consistently increases population mean fitness by purging deleterious alleles"
      ],
      "answer": 4,
      "why": "**E.** Drift is random and does not consistently improve fitness; it can just as easily fix deleterious alleles. Purging deleterious alleles is a function of purifying (negative) natural selection, not drift. | **A–D** are all accurate descriptions of genetic drift.",
      "sectionId": "c42",
      "chapterId": "ch4"
    },
    {
      "prompt": "Dolphins and sharks have similar streamlined bodies despite very different ancestry. BEST described as:",
      "choices": [
        "Convergent evolution (homoplasy) — same shape evolved independently from same aquatic selective pressure",
        "Homology — both vertebrates with shared body plan from common ancestor",
        "A synapomorphy defining all aquatic vertebrates",
        "Parallel evolution using same developmental genetic pathways",
        "Vestigial structures — both retain ancestral fins from a common aquatic ancestor"
      ],
      "answer": 0,
      "why": "**A.** Classic convergent evolution/homoplasy. Independent evolution driven by the same selective pressure (hydrodynamic efficiency). Very different developmental genetics so NOT parallel evolution. | **Wrong E:** Dolphin flippers and shark fins are not vestigial; they are functional structures that convergently evolved similar hydrodynamic shapes from very different ancestral structures.",
      "sectionId": "c43",
      "chapterId": "ch4"
    },
    {
      "prompt": "Gene flow acts as a homogenizing force on allele frequencies when which conditions are met?",
      "choices": [
        "Populations are isolated by a geographic barrier and no individuals cross it",
        "Migrants move between populations but do not reproduce after arrival",
        "Populations have identical allele frequencies and migration is bidirectional",
        "Migrants move between populations, reproduce successfully, and carry different allele frequencies",
        "Only one allele is present in each population and migration is unidirectional"
      ],
      "answer": 3,
      "why": "**D.** Gene flow homogenizes populations when migrants: (1) move between populations, (2) differ in allele frequencies, and (3) reproduce successfully. | **A fails:** no migration means no gene flow. | **B fails:** migration without reproduction does not transfer alleles. | **C fails:** if frequencies are already identical, flow has no effect. | **E fails:** fixed populations with one allele each cannot be homogenized by unidirectional flow.",
      "sectionId": "c43",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which statements about gene flow are TRUE?**I. Gene flow can introduce new alleles into a population without mutation.**II. Gene flow between populations reduces their genetic differentiation (FST).**III. Gene flow always prevents speciation regardless of geographic distance.**IV. Reduced gene flow due to geographic isolation can allow allopatric speciation.",
      "choices": [
        "I only",
        "I and IV only",
        "I, II, and IV only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and IV are correct. | **III fails:** gene flow can be overcome by strong divergent selection even with some migration (parapatric/sympatric speciation), and geographic isolation reduces gene flow enough for speciation regardless.",
      "sectionId": "c43",
      "chapterId": "ch4"
    },
    {
      "prompt": "How does reduced gene flow between an island population and the mainland eventually contribute to speciation?",
      "choices": [
        "Geographic barrier reduces migration → populations accumulate independent mutations and drift → local selection differs → reproductive isolation evolves",
        "Geographic barrier increases mutation rate on island → new species arise by saltational mutation",
        "Island individuals interbreed with mainland individuals but select against hybrids immediately",
        "Reduced gene flow causes allele frequencies to converge → populations become genetically identical → speciate",
        "The island population grows larger than the mainland → competitive exclusion drives speciation"
      ],
      "answer": 0,
      "why": "**A.** Allopatric speciation sequence: (1) barrier stops/reduces gene flow, (2) independent drift and mutation diverge both populations, (3) different environments impose divergent selection, (4) eventual reproductive isolation. | **B fails:** barriers do not increase mutation rates. | **C fails:** if they still interbreed, reproductive isolation is incomplete. | **D fails:** reduced gene flow causes divergence, not convergence. | **E fails:** size difference is not the mechanism.",
      "sectionId": "c43",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which of the following does NOT represent a mechanism or example of gene flow?",
      "choices": [
        "Pollen carried by wind from one plant population to another",
        "A bird from an island population flying to the mainland and breeding",
        "Seeds dispersed by ocean currents to a distant island where they germinate",
        "A chromosomal inversion suppressing recombination between two populations in the same habitat",
        "Human-assisted translocation of wolves between two isolated national park populations"
      ],
      "answer": 3,
      "why": "**D.** A chromosomal inversion suppressing recombination is a barrier to gene flow within a region of the genome (important in parapatric speciation) — it does not itself constitute gene flow. | **A, B, C, E** all describe physical movement of alleles between populations.",
      "sectionId": "c43",
      "chapterId": "ch4"
    },
    {
      "prompt": "Swim bladders in ray-finned fish are homologous to tetrapod lungs. The BEST concept describing this is:",
      "choices": [
        "Convergent evolution — both manage gas for similar functions",
        "Homoplasy — fish and tetrapods independently evolved gas-filled sacs",
        "Parallel evolution from shared ancestral buoyancy organ",
        "Exaptation — ancestral lung (breathing) co-opted into swim bladder (buoyancy) in many fish lineages",
        "Atavism — swim bladders are a reversion to an ancestral gill-breathing state"
      ],
      "answer": 3,
      "why": "**D.** Classic lecture exaptation example. Same structure (lung), different function (buoyancy) in different lineages after co-option. | **Wrong E:** Atavism is the reappearance of an ancestral trait in an individual; swim bladders are co-opted lungs (exaptation) that became standard in ray-finned fish, not reversions.",
      "sectionId": "c44",
      "chapterId": "ch4"
    },
    {
      "prompt": "A mutation will serve as the ultimate source of new alleles for evolution when which conditions apply?",
      "choices": [
        "It occurs in a somatic cell and the organism reproduces asexually",
        "It is a silent synonymous substitution in a non-coding intron",
        "It is repaired by the cell's mismatch-repair machinery before replication",
        "It causes a frameshift that is immediately lethal to the organism",
        "It occurs in germline cells and is passed to offspring"
      ],
      "answer": 4,
      "why": "**E.** Only germline mutations are heritable and thus contribute to evolutionary change across generations. | **A fails:** somatic mutations are not transmitted to offspring in sexual reproducers. | **B fails:** intronic synonymous changes may have minimal effect, but the key issue is germline transmission. | **C fails:** repaired mutations are not passed on. | **D fails:** lethal mutations are eliminated immediately.",
      "sectionId": "c44",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which statements about mutation and evolution are TRUE?**I. Most mutations that affect fitness are deleterious rather than beneficial.**II. Neutral mutations can become fixed in populations through genetic drift.**III. The mutation rate sets an upper limit on how fast evolution can occur.**IV. Mutations are directional — they preferentially produce adaptations that organisms need.",
      "choices": [
        "I only",
        "I and III only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and III are correct. | **IV fails:** mutations are random with respect to need — this is the central distinction between Darwinian and Lamarckian evolution.",
      "sectionId": "c44",
      "chapterId": "ch4"
    },
    {
      "prompt": "A single base-pair deletion occurs near the start of a protein-coding gene. What is the most likely downstream consequence?",
      "choices": [
        "A conservative amino acid substitution at one position with no change elsewhere",
        "Premature termination of transcription, producing a short mRNA",
        "A frameshift altering every codon downstream, likely producing a non-functional protein",
        "Activation of a cryptic splice site producing an alternatively spliced variant",
        "Duplication of the gene by unequal crossing over"
      ],
      "answer": 2,
      "why": "**C.** A single-base deletion shifts the reading frame for all codons 3' of the deletion, producing a completely different amino acid sequence and often a premature stop codon. | **A fails:** single-residue changes result from missense substitutions, not frameshifts. | **B fails:** deletions do not terminate transcription. | **D fails:** splice-site activation requires deletion at specific splice-site sequences. | **E fails:** gene duplication requires recombination events.",
      "sectionId": "c44",
      "chapterId": "ch4"
    },
    {
      "prompt": "Which of the following does NOT correctly describe the relationship between mutation and natural selection?",
      "choices": [
        "Mutation supplies the raw variation upon which natural selection acts",
        "Selection can increase the frequency of a beneficial mutation that arose randomly",
        "A beneficial mutation in one environment may be neutral or harmful in a different environment",
        "Natural selection directs which specific mutations will arise to solve environmental challenges",
        "Most new mutations with phenotypic effects are eliminated by purifying selection"
      ],
      "answer": 3,
      "why": "**D.** Natural selection does not direct or cause specific mutations; mutations are random. Selection only acts on pre-existing variation after it arises. This was Lamarck's error, not Darwin's insight. | **A, B, C, E** are all accurate statements about mutation-selection relationships.",
      "sectionId": "c44",
      "chapterId": "ch4"
    },
    {
      "prompt": "Two bacterial populations look identical but have completely different metabolic genes. BSC is unhelpful because:",
      "choices": [
        "Bacteria are too small for morphological analysis",
        "BSC requires at least 3 populations",
        "BSC doesn't apply to asexual organisms — reproductive isolation can't be tested",
        "HGT always connects bacterial populations into one species",
        "BSC fails because bacteria exchange DNA too freely through conjugation to ever form distinct species"
      ],
      "answer": 2,
      "why": "**C.** BSC requires sexual reproduction to test gene flow. Bacteria reproduce asexually — \"reproductive isolation\" is meaningless here. | **Wrong E:** While HGT complicates bacterial species concepts, the fundamental problem is that BSC requires sexual reproduction and reproductive isolation, which do not apply to asexual organisms.",
      "sectionId": "c131",
      "chapterId": "ch13"
    },
    {
      "prompt": "Allopatric speciation requires which combination of conditions?",
      "choices": [
        "Two populations occupy the same geographic range and experience divergent selection pressures",
        "A geographic barrier reduces or eliminates gene flow, allowing independent divergence",
        "Polyploidy doubles the chromosome number, creating immediate reproductive isolation",
        "Disruptive selection within a single panmictic population splits phenotypes into two groups",
        "Hybrid offspring are sterile due to chromosomal incompatibilities"
      ],
      "answer": 1,
      "why": "**B.** Allopatric speciation requires a geographic barrier that prevents gene flow, allowing divergence by selection, drift, or mutation independently in each population. | **A fails:** same geographic range describes sympatric speciation. | **C fails:** polyploidy is a sympatric mechanism. | **D fails:** single panmictic population is sympatric. | **E fails:** hybrid sterility is an outcome, not the initial condition for allopatric speciation.",
      "sectionId": "c131",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which statements about allopatric speciation are TRUE?**I. The formation of the Isthmus of Panama ~3 Ma caused vicariant speciation of marine species on Atlantic and Pacific sides.**II. Darwin's finches on the Galapagos are an example of dispersal-based allopatric speciation followed by adaptive radiation.**III. Secondary contact between allopatric populations always results in reinforcement of reproductive isolation.**IV. Allopatric speciation is considered the most common mode of speciation in animals.",
      "choices": [
        "I and II only",
        "I, II, and IV only",
        "II and IV only",
        "I, II, and IV only",
        "All four statements are true"
      ],
      "answer": 3,
      "why": "**D (= I, II, and IV).** Statements I, II, and IV are correct. | **III fails:** secondary contact can result in reinforcement OR fusion (if barriers are incomplete) OR hybrid zone maintenance — it does not \"always\" lead to reinforcement.",
      "sectionId": "c131",
      "chapterId": "ch13"
    },
    {
      "prompt": "What is the sequence of events in vicariant allopatric speciation?",
      "choices": [
        "Ancestral population → geographic barrier arises → gene flow stops → populations diverge → reproductive isolation evolves",
        "Small group disperses → colonizes new area → founder effect → rapid divergence → new species",
        "Hybridization between species → polyploidy → reproductive isolation → new allopolyploid species",
        "Disruptive selection → assortative mating → reduced gene flow within population → sympatric speciation",
        "Barrier disappears → secondary contact → reinforcement → new species recognized"
      ],
      "answer": 0,
      "why": "**A.** Vicariance: barrier splits existing range → gene flow ceases → both populations evolve independently → become reproductively isolated. | **B fails:** this describes founder-effect / dispersal allopatry, not vicariance. | **C fails:** this is allopolyploidy. | **D fails:** this is sympatric speciation. | **E fails:** this describes secondary contact, not the initial speciation process.",
      "sectionId": "c131",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which of the following does NOT support allopatric speciation as the explanation for biodiversity patterns?",
      "choices": [
        "Sister species pairs on opposite sides of the Andes show high genetic divergence",
        "Island archipelago species are most closely related to nearby mainland species, not to each other",
        "Species diversity is highest where geographic barriers (mountain ranges, rivers) are most numerous",
        "Sympatric populations of cichlid fish in Lake Victoria rapidly diversified without geographic barriers",
        "Continental drift separating landmasses correlates with the divergence times of marsupial lineages"
      ],
      "answer": 3,
      "why": "**D.** Lake Victoria cichlid diversification in sympatry is evidence for sympatric (or micro-allopatric) speciation, not classic allopatric speciation. | **A, B, C, E** all support allopatric speciation as an explanation for biodiversity patterns.",
      "sectionId": "c131",
      "chapterId": "ch13"
    },
    {
      "prompt": "Two frog species in the same pond; one breeds March, the other July. Which barrier applies?",
      "choices": [
        "Gametic incompatibility — wrong-species sperm can't fertilize eggs",
        "Temporal isolation (prezygotic, pre-mating) — different breeding seasons prevent mating",
        "Hybrid sterility — any hybrids produced would be sterile",
        "Habitat isolation — different microhabitats in the pond",
        "Mechanical isolation — incompatible reproductive structures prevent copulation between the two species"
      ],
      "answer": 1,
      "why": "**B.** Same habitat (same pond) but different breeding time = temporal isolation = prezygotic pre-mating barrier. NOT habitat isolation since they share the same pond. | **Wrong E:** Mechanical isolation involves physical incompatibility of reproductive organs; the scenario describes non-overlapping breeding seasons, which is temporal (seasonal) isolation.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "Reinforcement in speciation refers to:",
      "choices": [
        "Physical barriers getting stronger over geological time",
        "Postzygotic barriers converting into prezygotic barriers",
        "Hybrid offspring having higher fitness through hybrid vigor",
        "Natural selection strengthening prezygotic isolation when hybrids have low fitness — individuals avoiding cross-species mating waste fewer reproductive resources",
        "Genetic assimilation — learned mate preferences become genetically encoded over generations"
      ],
      "answer": 3,
      "why": "**D.** Reinforcement = selection favoring stronger mate preferences AGAINST interspecies mating because those matings produce low-fitness hybrids. Gamete waste is costly. Step 4 in allopatric speciation model (lecture slide 25). | **Wrong E:** Genetic assimilation involves environmentally induced phenotypes becoming genetically fixed; reinforcement specifically describes natural selection strengthening prezygotic barriers when hybrids are unfit.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "Sympatric speciation by allopolyploidy requires which combination of events?",
      "choices": [
        "Geographic barrier separates two populations for millions of years before hybridization",
        "Disruptive selection alone splits a population into two non-interbreeding groups",
        "Interspecific hybridization produces an infertile F1, followed by chromosome doubling restoring fertility",
        "A founder population colonizes a new island and undergoes rapid genetic drift",
        "Prezygotic isolation evolves before any chromosome-number change occurs"
      ],
      "answer": 2,
      "why": "**C.** Allopolyploidy: (1) species A x species B = infertile hybrid (mismatched chromosomes), (2) chromosome doubling gives each chromosome a homolog, (3) fertile allopolyploid is immediately reproductively isolated from both parents. | **A fails:** geographic isolation is not required in sympatric speciation. | **B fails:** disruptive selection alone is slow and rare in sympatry. | **D fails:** this describes founder-effect allopatric speciation. | **E fails:** prezygotic isolation is the result, not a precondition, of polyploidy.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which statements about sympatric speciation are TRUE?**I. Wheat (Triticum aestivum) is a hexaploid allopolyploid derived from three ancestral diploid species.**II. Host-race formation in insects (e.g., apple vs. hawthorn Rhagoletis flies) can initiate sympatric speciation.**III. Sympatric speciation by polyploidy is more common in animals than in plants.**IV. Disruptive selection combined with assortative mating can theoretically produce sympatric speciation.",
      "choices": [
        "I and II only",
        "II and IV only",
        "I, II, and IV only",
        "I, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and IV are correct. | **III fails:** it is the reverse — polyploidy-based sympatric speciation is far more common in PLANTS than in animals.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "How did bread wheat (Triticum aestivum, 6n) most likely arise?",
      "choices": [
        "A diploid wheat species underwent three successive autopolyploidy events, tripling its own genome",
        "Three different diploid grass species hybridized in two steps, with chromosome doublings producing a fertile hexaploid",
        "A diploid wheat was exposed to high UV radiation causing genome-wide duplication",
        "Two tetraploid species fused their genomes through horizontal gene transfer",
        "Bread wheat arose by directional selection on a single diploid ancestor over 10,000 years of agriculture"
      ],
      "answer": 1,
      "why": "**B.** T. aestivum formed by: (1) Einkorn (AA) x wild grass (BB) → infertile AB hybrid → doubled to AABB tetraploid emmer; (2) AABB x another diploid (DD) → AABBDD hexaploid. | **A fails:** autopolyploidy only multiplies one genome; allopolyploidy combines multiple. | **C fails:** UV does not cause precise whole-genome duplication. | **D fails:** horizontal gene transfer is a bacterial/viral mechanism. | **E fails:** artificial selection does not cause polyploidy.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which of the following does NOT represent a mechanism or example of sympatric speciation?",
      "choices": [
        "Allopolyploidy in wild plant hybrids",
        "Host-race divergence in phytophagous insects that mate on their host plant",
        "Disruptive selection on beak size combined with assortative mating in a single population",
        "Autopolyploidy in a plant producing a fertile tetraploid from a diploid parent",
        "A river forming a new geographic barrier splitting an existing frog population in two"
      ],
      "answer": 4,
      "why": "**E.** A river forming a barrier is the classic mechanism of allopatric (vicariant) speciation, not sympatric speciation. | **A, B, C, D** are all mechanisms that can produce speciation without geographic separation.",
      "sectionId": "c132",
      "chapterId": "ch13"
    },
    {
      "prompt": "The Isthmus of Panama rose ~3 mya, separating Atlantic and Pacific shrimp populations that then diverged into distinct species. This is:",
      "choices": [
        "Sympatric speciation driven by ecological divergence between ocean environments",
        "Allopatric speciation by dispersal — some shrimp colonized the opposite ocean",
        "Reinforcement after secondary contact between diverged populations",
        "Allopatric speciation by vicariance — a geological barrier appeared in the middle of an existing range",
        "Parapatric speciation — populations diverged along an environmental gradient across the isthmus"
      ],
      "answer": 3,
      "why": "**D.** Vicariance = geological event splits existing range; organisms don't move. The Isthmus rose, splitting Atlantic and Pacific populations. Compare to dispersal: if shrimp swam around the isthmus to colonize the other ocean, THAT would be dispersal. | **Wrong E:** Parapatric speciation involves divergence along a gradient with partial contact; the Panama scenario is classic vicariance allopatry where a barrier completely split a continuous range.",
      "sectionId": "c133",
      "chapterId": "ch13"
    },
    {
      "prompt": "Temporal isolation is in effect when which combination of conditions applies?",
      "choices": [
        "Two species live in different habitats within the same geographic area",
        "Mating calls of two species are structurally distinct and not recognized cross-species",
        "Hybrid embryos die early in development due to incompatible gene expression",
        "Two species breed in the same habitat but have non-overlapping mating seasons or times of day",
        "Pollen tubes of one plant species cannot grow through the style of another species"
      ],
      "answer": 3,
      "why": "**D.** Temporal isolation = populations reproduce at different times (seasons, daily cycles) within the same habitat. | **A fails:** different habitats = habitat isolation. | **B fails:** distinct mating calls = behavioral/acoustic isolation. | **C fails:** embryo death = post-zygotic (hybrid inviability). | **E fails:** pollen-style incompatibility = mechanical/gametic isolation.",
      "sectionId": "c133",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which of the following are PRE-zygotic isolating mechanisms?**I. Habitat isolation — species use different microhabitats within the same region.**II. Hybrid sterility — hybrid offspring are viable but cannot produce offspring.**III. Behavioral isolation — species do not recognize each other's courtship signals.**IV. Gametic isolation — sperm cannot penetrate eggs of the other species.",
      "choices": [
        "I only",
        "I and III only",
        "I, III, and IV only",
        "II, III, and IV only",
        "All four are pre-zygotic"
      ],
      "answer": 2,
      "why": "**C.** Habitat, behavioral, and gametic isolation all prevent fertilization from occurring (pre-zygotic). | **II fails:** hybrid sterility is POST-zygotic — fertilization has already occurred and a hybrid individual exists, but it cannot reproduce.",
      "sectionId": "c133",
      "chapterId": "ch13"
    },
    {
      "prompt": "What is the sequence by which reinforcement strengthens pre-zygotic isolation upon secondary contact?",
      "choices": [
        "Secondary contact → hybrids have lower fitness → selection favors individuals that avoid heterospecific mating → pre-zygotic barriers strengthen",
        "Secondary contact → hybrids have high fitness → gene flow increases → species fuse back into one",
        "Secondary contact → mutations increase hybrid fertility → post-zygotic barriers disappear",
        "Geographic barrier re-forms → populations re-isolated → diverge further → stronger isolation upon next contact",
        "Post-zygotic barriers arise first → cause pre-zygotic barriers to degrade over time"
      ],
      "answer": 0,
      "why": "**A.** Reinforcement: low hybrid fitness = wasted reproductive effort, so alleles that cause choosy (conspecific-preferring) mating are favored by selection, strengthening pre-zygotic barriers. | **B fails:** high-fitness hybrids lead to fusion, not reinforcement. | **C fails:** increased hybrid fertility opposes speciation. | **D fails:** this describes renewed allopatry, not reinforcement. | **E fails:** reinforcement strengthens pre-zygotic barriers, it does not degrade them.",
      "sectionId": "c133",
      "chapterId": "ch13"
    },
    {
      "prompt": "Which of the following does NOT correctly classify the reproductive isolating mechanism described?",
      "choices": [
        "Eastern and western meadowlarks look similar but have different songs and do not interbreed — behavioral isolation",
        "Wood frogs and leopard frogs breed in the same pond but at different times of spring — temporal isolation",
        "Mules (horse x donkey hybrids) are sterile — pre-zygotic gametic isolation",
        "Two Drosophila species can mate but their hybrid larvae die before reproducing — post-zygotic hybrid inviability",
        "Two plant species flower in the same meadow but are pollinated by different insects — mechanical/pollinator isolation"
      ],
      "answer": 2,
      "why": "**C.** Mule sterility is POST-zygotic hybrid sterility, not pre-zygotic gametic isolation. Gametic isolation prevents fertilization; mules are the product of successful fertilization and development. | **A, B, D, E** are all correctly classified.",
      "sectionId": "c133",
      "chapterId": "ch13"
    },
    {
      "prompt": "Convergent evolution is confirmed when which combination of observations is made?",
      "choices": [
        "Two species share a trait and also share a recent common ancestor that had the trait",
        "Two species have identical DNA sequences in the gene controlling a shared trait",
        "Two species live in the same geographic region and share multiple derived characters",
        "Two distantly related species independently evolved similar traits in similar environments without sharing a common ancestor with that trait",
        "Two species share traits because they hybridize regularly and exchange alleles"
      ],
      "answer": 3,
      "why": "**D.** Convergence = similar traits evolving independently in distantly related lineages under similar selective pressures, WITHOUT inheritance from a common ancestor that had the trait. | **A fails:** shared ancestry for a trait is homology, not convergence. | **B fails:** identical DNA sequences would imply homology or horizontal transfer. | **C fails:** geographic co-occurrence is not convergence; shared derived characters from a common ancestor is homology. | **E fails:** hybridization producing similar traits is introgression, not convergence.",
      "sectionId": "c141",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which pairs represent examples of convergent evolution?**I. The streamlined body shape of dolphins (mammals) and sharks (fish).**II. The forelimbs of humans, bats, and whales — all derived from the same ancestral tetrapod limb.**III. Eyes of vertebrates and cephalopod mollusks (octopus), which evolved independently.**IV. The wings of birds and bats, both derived from ancestral tetrapod forelimbs.",
      "choices": [
        "I and III only",
        "I, II, and III only",
        "I, III, and IV only",
        "II and IV only",
        "All four are convergent evolution"
      ],
      "answer": 0,
      "why": "**A (= I and III).** Dolphin/shark streamlining and vertebrate/cephalopod eyes are classic convergences. | **II fails:** human/bat/whale forelimbs are HOMOLOGOUS structures (same ancestral bone arrangement). | **IV fails:** bird and bat wings are both modified forelimbs from a common tetrapod ancestor — they are homologous in origin, though independently specialized as wings (a nuanced case, but the forelimb itself is homologous).",
      "sectionId": "c141",
      "chapterId": "ch14"
    },
    {
      "prompt": "Why did marsupial wolves (thylacines) and placental wolves (canids) independently evolve similar skull and body morphology?",
      "choices": [
        "They share a recent common ancestor that was a wolf-like apex predator",
        "They exchanged genes through hybridization across the Pacific land bridge",
        "Both lineages faced similar selective pressures for pursuit predation, favoring convergent skull and body shapes optimized for that niche",
        "The marsupial wolf migrated from North America to Australia, carrying wolf genes",
        "Shared developmental constraints forced both lineages into the same body plan regardless of ecology"
      ],
      "answer": 2,
      "why": "**C.** Convergence is driven by similar ecological roles (pursuit predation) imposing similar selection pressures. Natural selection independently sculpted both lineages toward the same functional solution. | **A fails:** marsupials and placentals diverged >100 Ma before wolves existed. | **B fails:** marsupials and placentals do not hybridize. | **D fails:** thylacines are native to Australia; no land-bridge dispersal from N. America. | **E fails:** developmental constraints can channel but do not fully explain convergence; ecology is primary.",
      "sectionId": "c141",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following does NOT represent convergent evolution?",
      "choices": [
        "Echolocation independently evolving in bats and toothed whales",
        "The pentadactyl (five-digit) forelimb shared by humans, horses, bats, and dolphins",
        "C4 photosynthesis evolving independently in grasses and dicots more than 60 times",
        "Sabre-tooth morphology evolving in both placental felids (Smilodon) and marsupial thylacosmilids",
        "Cacti (Americas) and euphorbs (Africa) independently evolving succulent stem-water storage"
      ],
      "answer": 1,
      "why": "**B.** The pentadactyl limb is a HOMOLOGOUS structure inherited from a common tetrapod ancestor — it is the textbook example of homology, not convergence. | **A, C, D, E** all describe traits that evolved independently in distantly related lineages.",
      "sectionId": "c141",
      "chapterId": "ch14"
    },
    {
      "prompt": "A global clade starts with 50 species. Over 10 million years, 30 originate and 15 go extinct. Standing diversity at the end?",
      "choices": [
        "35 species",
        "45 species",
        "65 species",
        "80 species",
        "95 species — background extinction must be subtracted separately from the original 50"
      ],
      "answer": 2,
      "why": "**C.** D&sub2 = 50 + 30 − 15 = **65**. Turnover = 30 + 15 = 45. λ = 3.0/my > μ = 1.5/my → clade growing. | **Wrong E:** Standing diversity = start + originations minus extinctions = 50 + 30 minus 15 = 65; the 15 extinctions already account for all losses.",
      "sectionId": "c142",
      "chapterId": "ch14"
    },
    {
      "prompt": "Two structures are confirmed to be homologous when which conditions apply?",
      "choices": [
        "They look similar and perform the same function in both species",
        "They are found in species that live in the same habitat and share similar diets",
        "They share the same embryonic developmental origin and can be traced to the same ancestral structure in a common ancestor",
        "They are coded by genes with identical DNA sequences in both species",
        "They appear at the same body position in both species and are the same size"
      ],
      "answer": 2,
      "why": "**C.** Homology is defined by shared evolutionary origin (common ancestry) and common developmental pathway, regardless of current function. | **A fails:** similar function with different origin = analogy/convergence. | **B fails:** shared habitat does not imply common ancestry of structures. | **D fails:** homologous genes can diverge significantly in sequence. | **E fails:** body position and size can change through evolution; developmental origin is the criterion.",
      "sectionId": "c142",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following pairs represent HOMOLOGOUS structures?**I. Human arm and whale flipper — same bone arrangement, different function.**II. Bird wing and butterfly wing — both used for flight but unrelated in origin.**III. Human hair and bird feathers — both are integumentary structures derived from the same ancestral protein (beta-keratin).**IV. Dog forelimb and cat forelimb — derived from the same ancestral tetrapod limb.",
      "choices": [
        "I and IV only",
        "I, II, and IV only",
        "I and IV only",
        "II and III only",
        "All four pairs are homologous"
      ],
      "answer": 2,
      "why": "**C (= I and IV).** Human/whale forelimbs and dog/cat forelimbs share common tetrapod ancestry (homologous). | **II fails:** bird wings and butterfly wings are analogous (convergent) — entirely different structures. | **III fails:** hair and feathers are NOT homologous — feathers evolved from reptilian scales; mammalian hair is a separate derived structure.",
      "sectionId": "c142",
      "chapterId": "ch14"
    },
    {
      "prompt": "How does comparative embryology provide evidence for homology between vertebrate forelimbs?",
      "choices": [
        "All vertebrate embryos pass through a stage with the same basic limb bud structure governed by the same Hox gene expression patterns, confirming common descent",
        "Adult vertebrate forelimbs look identical in size and shape, confirming a single ancestor",
        "Fossil intermediates show all limb types present in a single Cambrian ancestor",
        "All vertebrates have the same number of digits (five) in both forelimbs and hindlimbs",
        "Molecular clocks show all vertebrate forelimb genes evolved at the same rate"
      ],
      "answer": 0,
      "why": "**A.** Vertebrate embryos share conserved limb-bud development (AER, ZPA, Hox genes) — this developmental commonality reflects common ancestry. | **B fails:** adult forelimbs are dramatically different in form. | **C fails:** Cambrian fossils do not show all limb types in one ancestor. | **D fails:** many vertebrates have fewer than 5 digits (horses: 1, snakes: 0). | **E fails:** molecular clock rates vary among genes.",
      "sectionId": "c142",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following does NOT represent a homologous structure?",
      "choices": [
        "The humerus of a human and the humerus of a cat",
        "The mitochondria of a yeast cell and a human cell",
        "The HoxA gene cluster of mice and fruit flies",
        "The wing of a bird and the wing of a dragonfly",
        "The eye lens crystallin proteins of vertebrates and their ancestral heat-shock proteins"
      ],
      "answer": 3,
      "why": "**D.** Bird wings and dragonfly wings are analogous (convergent) structures — they evolved flight independently and have entirely different developmental origins. | **A, B, C, E** are all homologous structures traceable to common ancestry.",
      "sectionId": "c142",
      "chapterId": "ch14"
    },
    {
      "prompt": "Eleutherodactylus frogs underwent massive adaptive radiation primarily because:",
      "choices": [
        "They colonized tropical islands where competitors were absent",
        "Key innovation: direct development on land skips the tadpole stage, freeing larvae from intense aquatic competition",
        "A mass extinction eliminated their aquatic competitors",
        "High tropical mutation rates accelerated their speciation",
        "Symbiosis with mycorrhizal fungi gave them access to nutrients unavailable to competitors"
      ],
      "answer": 1,
      "why": "**B.** Directly from lecture slide 27. Direct development = eggs hatch as tiny froglets, bypassing the tadpole stage. Tadpoles compete intensely for aquatic resources. Skipping that stage removes a major constraint, opening up enormous ecological space. | **Wrong E:** The key innovation for Eleutherodactylus was direct development (no tadpole stage), not fungal symbiosis; this freed them from intense aquatic competition.",
      "sectionId": "c143",
      "chapterId": "ch14"
    },
    {
      "prompt": "A structure qualifies as \"vestigial\" when which conditions are met?",
      "choices": [
        "The structure is small in size and located in an internal body cavity",
        "The structure performs the same primary function as the homolog in a related species",
        "The structure is reduced or functionless in the current species but homologous to a functional structure in ancestors or relatives",
        "The structure appeared recently through a new mutation in the current lineage",
        "The structure is only present during embryonic development and disappears in adults"
      ],
      "answer": 2,
      "why": "**C.** Vestigial structures are reduced/functionless remnants of structures that were functional in ancestral forms — their homology to functional structures in relatives is the defining criterion. | **A fails:** size or location alone is insufficient; function is the key. | **B fails:** if it still performs the same function, it is not vestigial. | **D fails:** vestigial structures are ancient, not new. | **E fails:** atavistic structures are embryonic reversions; vestigial structures may persist in adults (e.g., whale pelvis).",
      "sectionId": "c143",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following are correctly identified as vestigial structures?**I. The human coccyx — remnant of an ancestral tail.**II. The whale pelvic girdle — remnant of hind limb skeleton from terrestrial ancestors.**III. The human appendix — a vestige of a larger cecum used for cellulose fermentation.**IV. The human little toe — a functional digit that aids in balance and walking.",
      "choices": [
        "I and II only",
        "I, II, and IV only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four are vestigial"
      ],
      "answer": 2,
      "why": "**C.** The coccyx, whale pelvis, and human appendix are classic vestigial structures. | **IV fails:** the little toe still performs a functional role in balance and gait — it is not vestigial.",
      "sectionId": "c143",
      "chapterId": "ch14"
    },
    {
      "prompt": "What evolutionary process causes previously functional structures to become vestigial over time?",
      "choices": [
        "Strong positive selection for the structure's alternative function replaces its original role",
        "Relaxed selection on the original function allows mutations that reduce it to accumulate; if the structure is costly, negative selection may further reduce it",
        "Lamarckian disuse directly causes genetic changes that reduce the structure",
        "Horizontal gene transfer from a related species introduces alleles that suppress the structure",
        "Punctuated equilibrium causes sudden loss of the structure during a speciation event"
      ],
      "answer": 1,
      "why": "**B.** When a structure loses its original function, selection no longer purges loss-of-function mutations; these accumulate by drift. If maintenance is costly, negative selection actively reduces the structure. | **A fails:** acquisition of a new function would not make the old function vestigial. | **C fails:** Lamarckian inheritance is false. | **D fails:** horizontal gene transfer is not the mechanism in animals. | **E fails:** vestigialization is gradual, not punctuated.",
      "sectionId": "c143",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following does NOT represent evidence from vestigial structures supporting evolution?",
      "choices": [
        "Python skeletons contain tiny remnant leg bones with no locomotor function",
        "Some blind cavefish species have vestigial eye structures beneath unpigmented skin",
        "Kiwi birds have tiny vestigial wings hidden under feathers that cannot support flight",
        "Humans have a palmaris longus muscle absent in ~14% of the population with no loss of hand strength",
        "The placenta in eutherian mammals is a newly evolved structure with no ancestral precursor"
      ],
      "answer": 4,
      "why": "**E.** The placenta is not a vestigial structure — it is a derived innovation. Moreover, saying it has \"no ancestral precursor\" is incorrect (homologous structures exist in earlier synapsids). | **A, B, C, D** all correctly describe vestigial structures as evidence for evolution.",
      "sectionId": "c143",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which mass extinction was MOST severe in species lost, and what caused it?",
      "choices": [
        "End-Permian (~252 mya, ~96%): Siberian Traps volcanism → CO&sub2 spike, global warming, ocean anoxia",
        "K-T (~66 mya, ~76%): Chicxulub asteroid impact",
        "End-Ordovician (~444 mya, ~86%): glacial episodes and global cooling",
        "6th extinction (ongoing): human activity at 100–1000× background rate",
        "Late Devonian (~372 mya, ~75%): caused by rapid ocean cooling from plant root weathering"
      ],
      "answer": 0,
      "why": "**A.** End-Permian \"Great Dying\" (~252 mya) killed ~96% of marine species and ~70% of terrestrial vertebrates. Siberian Traps erupted for ~1 million years releasing massive CO&sub2. Recovery took 5–10 million years. K-T is more famous but less severe. | **Wrong E:** The Late Devonian extinction was severe but not the MOST severe; the End-Permian at ~96% species loss holds that record.",
      "sectionId": "c144",
      "chapterId": "ch14"
    },
    {
      "prompt": "Biogeographic evidence supports evolution when which combination of patterns is observed?",
      "choices": [
        "Identical species are found on all continents with no correlation to geographic proximity",
        "Species distributions are random with respect to geological and climatic history",
        "Endemic species on oceanic islands are identical to species on the nearest mainland",
        "Species on isolated landmasses are most closely related to nearby species, not to morphologically similar species on distant continents",
        "All biodiversity is concentrated at the equator regardless of island history or continental proximity"
      ],
      "answer": 3,
      "why": "**D.** Biogeography supports evolution: species on isolated landmasses descend from the nearest source population (dispersal), and vicariance produces related species on separated landmasses, not random or pantropical distributions. | **A fails:** identical global distributions would negate evolutionary biogeography. | **B fails:** distributions are highly correlated with geological history. | **C fails:** island endemics are related to but distinct from mainland relatives. | **E fails:** equatorial concentration (latitudinal diversity gradient) is a separate pattern.",
      "sectionId": "c144",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which biogeographic observations are consistent with evolution by common descent and continental drift?**I. Marsupials are found almost exclusively in Australia and South America — the two southern continents once joined in Gondwana.**II. Lungfish are found in Africa, South America, and Australia — Gondwana fragments.**III. The Hawaiian honeycreepers are all descended from a single finch-like ancestor that colonized the islands.**IV. Placental mammals dominate all continents equally, showing no geographic pattern.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III only",
        "II, III, and IV only",
        "All four are consistent with common descent"
      ],
      "answer": 2,
      "why": "**C.** Statements I, II, and III reflect vicariance (Gondwana fragmentation) and dispersal-based adaptive radiation. | **IV fails:** placentals are absent from Australia (until human introduction) — the geographic pattern strongly supports evolutionary biogeography.",
      "sectionId": "c144",
      "chapterId": "ch14"
    },
    {
      "prompt": "How does the Wallace Line in Southeast Asia provide biogeographic evidence for evolution?",
      "choices": [
        "It marks a deep-water channel between Bali/Borneo and Lombok/Sulawesi that was never bridged, separating Asian fauna from Australian fauna even when sea levels dropped during ice ages",
        "It marks the boundary of the Asian tectonic plate, where volcanic activity drove mass extinctions and rapid speciation",
        "It separates tropical from subtropical climates, explaining why different species live on each side",
        "It represents a former land bridge used by marsupials to disperse from Asia to Australia",
        "It marks the edge of the Pleistocene glaciers, which isolated Asian and Australian species during ice ages"
      ],
      "answer": 0,
      "why": "**A.** The Wallace Line is a deep oceanic trench that persisted even at glacial sea-level lows, acting as a permanent barrier. Asian species (tigers, orangutans) could not cross to the Australasian side (kangaroos, cockatoos), creating a sharp faunal boundary. | **B fails:** tectonic plate boundaries do not correlate with the Wallace Line. | **C fails:** climate changes gradually and does not produce a sharp line. | **D fails:** no land bridge crossed the Wallace Line. | **E fails:** glaciers did not reach Southeast Asia.",
      "sectionId": "c144",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following does NOT represent biogeographic evidence for evolution?",
      "choices": [
        "Darwin's finches on the Galapagos are most closely related to South American finches",
        "African and South American lungfish are more closely related to each other than either is to Australian lungfish",
        "New Zealand has no native land mammals except bats (which can fly across water gaps)",
        "Madagascar's lemurs are found nowhere else and are most closely related to African primates",
        "The same photosynthetic light reactions occur in all plants regardless of their location on Earth"
      ],
      "answer": 4,
      "why": "**E.** Universal photosynthesis (shared biochemistry) is evidence for common descent but is NOT biogeographic evidence — it is biochemical/molecular evidence. Biogeography specifically concerns geographic distributions. | **A, B, C, D** are all classic biogeographic evidence for evolution.",
      "sectionId": "c144",
      "chapterId": "ch14"
    },
    {
      "prompt": "According to island biogeography theory, which island has the MOST species at equilibrium?",
      "choices": [
        "Small, far from mainland",
        "Small, close to mainland",
        "Large, far from mainland",
        "Large, close to mainland",
        "Small, at an intermediate distance from the mainland"
      ],
      "answer": 3,
      "why": "**D.** Large = lower extinction rate (more niches, larger populations). Close = higher immigration rate. Both factors push richness up. Large + close = maximum species. | **Wrong E:** Intermediate distance does not maximize species richness; the equilibrium theory predicts large + close islands have the most species due to highest immigration and lowest extinction rates.",
      "sectionId": "c145",
      "chapterId": "ch14"
    },
    {
      "prompt": "Molecular sequence data supports common descent when which pattern is observed?",
      "choices": [
        "All organisms have identical DNA sequences for all genes, indicating a single ancestor",
        "Sequence similarity between species decreases with increasing evolutionary distance, mirroring the pattern of morphological and fossil evidence",
        "DNA sequences are identical between distantly related species due to convergent molecular evolution",
        "Molecular divergence rates are random and show no correlation with fossil-calibrated divergence times",
        "Only mitochondrial DNA can be used to infer phylogenetic relationships"
      ],
      "answer": 1,
      "why": "**B.** Common descent predicts nested similarity: closely related species share more similar sequences. This pattern holds consistently across genes and matches fossil/morphological phylogenies. | **A fails:** sequences diverge after speciation. | **C fails:** convergent molecular evolution occurs rarely and is detectable as an exception. | **D fails:** molecular clocks are correlated with fossil-calibrated dates. | **E fails:** nuclear, chloroplast, and many other DNA sources are used in phylogenetics.",
      "sectionId": "c145",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which molecular observations provide evidence for evolution?**I. Humans and chimpanzees share ~98.7% DNA sequence identity.**II. Pseudogenes (non-functional gene copies) are found at the same chromosomal locations in humans and chimpanzees.**III. All living organisms use the same genetic code (with minor exceptions), suggesting a universal common ancestor.**IV. Endogenous retroviruses (ERVs) are inserted at identical chromosomal positions in humans and other great apes.",
      "choices": [
        "I only",
        "I and III only",
        "I, II, and III only",
        "I, III, and IV only",
        "All four observations provide evidence for evolution"
      ],
      "answer": 4,
      "why": "**E.** All four are powerful molecular evidence for evolution. Shared ERV insertions (IV) are particularly compelling because the probability of independent identical retroviral insertions is astronomically low.",
      "sectionId": "c145",
      "chapterId": "ch14"
    },
    {
      "prompt": "How are molecular clocks used to estimate divergence times between species?",
      "choices": [
        "Radioactive decay of DNA base pairs is measured directly to give an absolute age",
        "The number of morphological differences is counted and divided by the generation time",
        "The rate of neutral molecular change is calibrated using fossil-dated nodes, then applied to unknown divergence times",
        "Shared ancestral DNA sequences are amplified by PCR from fossilized specimens to get direct dates",
        "The GC content of DNA is measured; higher GC indicates older lineages"
      ],
      "answer": 2,
      "why": "**C.** Molecular clocks: (1) identify neutral sequence positions, (2) estimate substitution rate using fossil-calibrated divergence events, (3) apply that rate to species pairs with unknown divergence times. | **A fails:** DNA does not undergo radioactive decay. | **B fails:** morphological differences are not molecular. | **D fails:** ancient DNA degrades and cannot be amplified from most fossils. | **E fails:** GC content does not correlate with age.",
      "sectionId": "c145",
      "chapterId": "ch14"
    },
    {
      "prompt": "Which of the following does NOT represent molecular evidence for common descent?",
      "choices": [
        "Humans and yeast share ~30% identical amino acid sequence in the ATP synthase subunit",
        "The FOXP2 gene controlling speech/language in humans is also present in similar form in other vertebrates",
        "Cytochrome c sequence differences between species match their phylogenetic relationships inferred from morphology",
        "All organisms synthesize ATP from ADP and inorganic phosphate — a universal metabolic process",
        "Human chromosome 2 shows fusion marks matching two separate chromosomes in other great apes"
      ],
      "answer": 3,
      "why": "**D.** Universal ATP synthesis is biochemical evidence for common descent, but it is not specifically MOLECULAR SEQUENCE evidence. The question asks for molecular (sequence-based) evidence, and ATP synthesis is a metabolic/biochemical observation. | **A, B, C, E** all explicitly reference molecular sequences supporting common descent.",
      "sectionId": "c145",
      "chapterId": "ch14"
    },
    {
      "prompt": "Over decades, Atlantic cod show smaller body size and earlier maturation. Which principle BEST explains this heritable change?",
      "choices": [
        "Genetic drift from small population size caused random allele frequency changes",
        "Directional selection — nets preferentially capture large fish; small-bodied early-maturing fish escape and reproduce, increasing those alleles",
        "Phenotypic plasticity — fish grow smaller due to decreased food from overfishing",
        "Sexual selection — females now prefer smaller males in depleted populations",
        "Stabilizing selection — the population is converging toward an optimal intermediate body size"
      ],
      "answer": 1,
      "why": "**B.** Directional selection by humans as a size-selective predator. Nets consistently remove large individuals. Over generations, alleles for small body size + early maturation increase in frequency. Genuine genetic evolution (heritable change), not just plasticity. | **Wrong E:** Stabilizing selection maintains the mean and reduces variance; the observed directional shift toward smaller size is directional selection imposed by size-selective fishing mortality.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "A patient stops antibiotics after 3 days feeling better. The most likely evolutionary outcome:",
      "choices": [
        "No problem — antibiotics continue working for days after last dose",
        "Bacteria mutate rapidly in response to antibiotic removal, becoming more virulent",
        "Susceptible bacteria were killed first; pre-existing resistant survivors multiply unchecked and may spread resistance",
        "The immune system eliminates remaining bacteria before resistance can develop",
        "The remaining bacteria become physiologically dependent on the antibiotic after partial exposure"
      ],
      "answer": 2,
      "why": "**C.** Stopping early kills the most susceptible cells first. Pre-existing resistant variants — always there at low frequency — now have no competition and no antibiotic pressure. They multiply. Antibiotics don't cause new mutations; they select from existing variation. | **Wrong E:** Bacteria do not become dependent on antibiotics; pre-existing resistant variants simply survive and proliferate when susceptible competitors are removed by incomplete treatment.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "Hardy-Weinberg equilibrium (HWE) is maintained when which complete set of conditions is met?",
      "choices": [
        "The population is small, mating is random, no selection occurs, mutation is present, gene flow is absent",
        "The population is large, mating is assortative, no mutation, no selection, gene flow is absent",
        "The population is large, mating is random, mutation is present, no selection, gene flow is absent",
        "The population is small, mating is random, no mutation, no selection, gene flow is absent",
        "The population is large, mating is random, no mutation, no selection, gene flow is absent"
      ],
      "answer": 4,
      "why": "**E.** All five HWE conditions must hold simultaneously: (1) large N, (2) random mating, (3) no mutation, (4) no selection, (5) no gene flow (migration). | **A fails:** small population allows drift. | **B fails:** assortative mating violates random mating. | **C fails:** mutation present violates HWE. | **D fails:** small population allows drift.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "Which statements about Hardy-Weinberg equilibrium are TRUE?**I. If p + q = 1 for two alleles, genotype frequencies are p² + 2pq + q² = 1.**II. HWE serves as a null model; deviations indicate that evolutionary forces are acting.**III. A population in HWE is evolving rapidly due to strong selection.**IV. HWE applies to diploid, sexually reproducing populations.",
      "choices": [
        "I and II only",
        "I, II, and IV only",
        "I, II, and IV only",
        "II, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C (= I, II, and IV).** Statements I, II, and IV are correct. | **III fails:** a population in HWE is NOT evolving — it is in equilibrium. Strong selection is exactly what disrupts HWE.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "In a population, the frequency of a recessive allele (q) for albinism is 0.1. Assuming HWE, what is the frequency of carriers (heterozygotes)?",
      "choices": [
        "0.01 (= q²)",
        "0.81 (= p²)",
        "0.18 (= 2pq, where p = 0.9 and q = 0.1)",
        "0.10 (= q)",
        "0.20 (= 2q)"
      ],
      "answer": 2,
      "why": "**C.** p = 1 - q = 0.9. Carrier frequency = 2pq = 2(0.9)(0.1) = 0.18. Note that carriers are 18x more frequent than affected individuals (q² = 0.01). | **A fails:** 0.01 = q² = frequency of affected homozygotes, not carriers. | **B fails:** 0.81 = p² = frequency of homozygous dominant. | **D fails:** 0.10 = q = allele frequency, not genotype frequency. | **E fails:** 2q is not a HWE genotype frequency formula.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "Which of the following does NOT violate Hardy-Weinberg equilibrium?",
      "choices": [
        "Cheetahs have extremely low genetic diversity due to a past bottleneck (small population effect)",
        "Humans preferentially mate with individuals of similar height (assortative mating)",
        "A large, isolated island population of birds mates randomly with no immigration or emigration, no mutation, and no selection on beak color",
        "Strong selection against sickle-cell homozygotes reduces their frequency each generation",
        "A hurricane kills 90% of a lizard population at random, drastically reducing population size"
      ],
      "answer": 2,
      "why": "**C.** A large isolated population with random mating, no migration, no selection, and (implied) no mutation satisfies all five HWE conditions — allele frequencies will not change. | **A** = bottleneck (drift), **B** = assortative mating, **D** = selection, **E** = bottleneck/drift — all violate HWE.",
      "sectionId": "c81",
      "chapterId": "ch8"
    },
    {
      "prompt": "Human chromosome 2 contains telomeric sequences in its middle (normally only at chromosome ends). The BEST explanation:",
      "choices": [
        "Humans gained genetic material through horizontal gene transfer from microbes",
        "Two ancestral chromosomes (corresponding to chimp 2A and 2B) fused end-to-end in the human lineage after divergence from our common ancestor",
        "A whole-chromosome duplication event in chimps gave them the extra chromosome",
        "Humans lost a chromosome through a major deletion in the hominin lineage",
        "A reciprocal translocation between chromosomes 2 and 13 created a novel fusion chromosome in humans"
      ],
      "answer": 1,
      "why": "**B.** Telomeric sequences in the middle of chromosome 2 = molecular signature of end-to-end fusion. The fusion happened in the human lineage after the split from the common ancestor with chimps (who still have two separate chromosomes). Powerful molecular evidence of common descent. | **Wrong E:** The evidence (internal telomeric sequences matching chimp 2A+2B) points specifically to end-to-end fusion of two ancestral chromosomes, not a reciprocal translocation involving chromosome 13.",
      "sectionId": "c171",
      "chapterId": "ch17"
    },
    {
      "prompt": "Sexual selection favors a trait in the opposite sex when which conditions are met?",
      "choices": [
        "The trait improves survival under current environmental conditions",
        "The trait is expressed equally in both sexes and is linked to resource acquisition",
        "The trait evolved by genetic drift in a small founding population",
        "Choosy individuals that prefer the trait gain a reproductive advantage by mating with higher-quality or more attractive partners",
        "The trait is neutral with respect to fitness in both sexes"
      ],
      "answer": 3,
      "why": "**D.** Sexual selection operates through mate choice: if individuals with a preference for a trait have higher reproductive success (because the preferred trait indicates good genes or produces attractive offspring), the preference allele and the trait allele spread together. | **A fails:** sexually selected traits often reduce survival (peacock tail). | **B fails:** resource traits are naturally selected, not necessarily sexually. | **C fails:** drift is not sexual selection. | **E fails:** neutral traits are not sexually selected.",
      "sectionId": "c171",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which statements about sexual selection are TRUE?**I. Intrasexual selection involves competition between members of the same sex for mating opportunities.**II. Intersexual selection involves mate choice by one sex (usually females) based on traits of the other.**III. Runaway selection (Fisher's runaway) requires a genetic correlation between female preference and male ornament.**IV. Sexual selection always reduces overall population fitness by favoring maladaptive traits.",
      "choices": [
        "I and II only",
        "I, II, and III only",
        "I, II, and III only",
        "I, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C (= I, II, and III).** | **IV fails:** sexual selection does not \"always\" reduce fitness; the good-genes hypothesis argues it can improve offspring quality and population fitness. Even when survival costs exist, reproductive benefits may outweigh them.",
      "sectionId": "c171",
      "chapterId": "ch17"
    },
    {
      "prompt": "How does Fisher's runaway selection produce extreme male ornaments over evolutionary time?",
      "choices": [
        "Females with a preference for longer tails produce sons with longer tails AND daughters with the preference → preference and ornament genes become genetically correlated → the preference drives the ornament to extremes until counteracted by natural selection",
        "Longer tails directly improve male survival by helping escape predators → natural selection favors longer tails",
        "Males compete physically for females → larger ornaments win fights → intrasexual selection drives ornament size",
        "Longer tails signal higher testosterone → honest indicator of parasite resistance → Hamilton-Zuk hypothesis",
        "Mutations producing longer tails arise more frequently under high predation → adaptive mutation drives runaway"
      ],
      "answer": 0,
      "why": "**A.** Fisher's runaway: genetic linkage between preference genes and ornament genes causes both to increase together, self-reinforcing until natural selection (predation, energetic cost) halts further increase. | **B fails:** runaway ornaments typically REDUCE survival. | **C fails:** this describes intrasexual competition, not intersexual runaway. | **D fails:** this is the Hamilton-Zuk good-genes hypothesis, not Fisher's runaway. | **E fails:** adaptive mutation is not how evolution works.",
      "sectionId": "c171",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following does NOT represent an example of sexual selection?",
      "choices": [
        "Male elephant seals fighting for beach territories where females aggregate",
        "Female bird-of-paradise preferentially mating with males performing more elaborate dances",
        "Male elk growing large antlers used in competition for access to females",
        "Female guppies preferring males with more orange coloration, which correlates with carotenoid-based health",
        "Female worker bees being sterile and raising the queen's offspring rather than their own"
      ],
      "answer": 4,
      "why": "**E.** Worker bee sterility is explained by kin selection / inclusive fitness, not sexual selection. Workers share 75% of genes with sisters (due to haplodiploidy) — it is more fitness-efficient to raise sisters than own offspring. | **A** = intrasexual, **B** = intersexual/choice, **C** = intrasexual, **D** = intersexual/good-genes.",
      "sectionId": "c171",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which hominin was FIRST to leave Africa, and approximately when?",
      "choices": [
        "Homo sapiens — Out of Africa expansion ~70 kya",
        "Australopithecus — spread across savannah ~3 mya",
        "Homo erectus — first outside-Africa fossils ~1.9–1.5 mya in Java and China",
        "Homo habilis — followed megafauna migrations across the Sinai ~1.5 mya",
        "Homo naledi — its small brain size suggests it was the first hominin to leave Africa"
      ],
      "answer": 2,
      "why": "**C.** H. erectus fossils appear in Java (Indonesia) and China (\"Peking Man\") at ~1.9–1.5 mya — first known hominin outside Africa. H. sapiens' Out of Africa expansion was much later (~70 kya). H. habilis fossils are only found in Africa. | **Wrong E:** H. naledi fossils are found only in South Africa; H. erectus has the earliest confirmed out-of-Africa fossils at ~1.9 mya in Java and Georgia.",
      "sectionId": "c172",
      "chapterId": "ch17"
    },
    {
      "prompt": "According to Hamilton's rule, an altruistic behavior will be favored by natural selection when which condition is met?",
      "choices": [
        "The cost to the actor (C) exceeds the benefit to the recipient (B) multiplied by their relatedness (r)",
        "The relatedness (r) between actor and recipient equals zero",
        "The benefit to the recipient (B) multiplied by their relatedness (r) exceeds the cost to the actor (C), i.e., rB > C",
        "The actor and recipient are unrelated, but the benefit is very large",
        "The population is very small, so all interactions are between close relatives"
      ],
      "answer": 2,
      "why": "**C.** Hamilton's rule: altruism is favored when rB > C — the genetic benefit to relatives (weighted by their relatedness) exceeds the personal cost. | **A fails:** this describes when altruism is NOT favored (C > rB). | **B fails:** r = 0 means the actor gains no inclusive fitness from the act. | **D fails:** r = 0 means rB = 0 regardless of B. | **E fails:** small population size alone does not guarantee altruism is favored; the rB > C condition must hold.",
      "sectionId": "c172",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which statements about kin selection and inclusive fitness are TRUE?**I. Inclusive fitness includes both direct fitness (own reproduction) and indirect fitness (reproduction of relatives).**II. Ground squirrels give alarm calls more often when close relatives are nearby, consistent with kin selection.**III. Eusociality in Hymenoptera (bees, ants, wasps) is explained solely by haplodiploidy.**IV. Reciprocal altruism can evolve between unrelated individuals if interactions are repeated.",
      "choices": [
        "I and II only",
        "I, II, and IV only",
        "I and IV only",
        "I, II, and IV only",
        "All four statements are true"
      ],
      "answer": 3,
      "why": "**D (= I, II, and IV).** | **III fails:** haplodiploidy helps but is not the sole explanation for eusociality — termites are eusocial and diploid. Ecological factors (fortress defense, resource defense) also promote eusociality.",
      "sectionId": "c172",
      "chapterId": "ch17"
    },
    {
      "prompt": "Why do worker honey bees (r = 0.75 with sisters in a haplodiploid colony) behave altruistically?",
      "choices": [
        "They are genetically programmed by selfish queen pheromones to sacrifice themselves regardless of relatedness",
        "Because r = 0.75 with sisters exceeds r = 0.5 with their own daughters, workers transmit more of their genes by raising sisters than by reproducing directly, satisfying rB > C",
        "Worker bees have no reproductive cells and cannot physically reproduce, so altruism is the only option",
        "The benefit (B) of producing a new worker is lower than the cost (C) of foraging, so the rB > C condition is never met",
        "Haplodiploidy makes all colony members genetically identical, eliminating any conflict of interest"
      ],
      "answer": 1,
      "why": "**B.** Haplodiploidy: females are diploid (from fertilized eggs), males haploid. Full sisters share 75% of genes. Since r(sister) = 0.75 > r(daughter) = 0.50, helping raise sisters increases inclusive fitness more than direct reproduction. | **A fails:** queen pheromones suppress reproduction but Hamilton's rule is the evolutionary explanation. | **C fails:** workers do have ovaries and can lay unfertilized (male) eggs under some conditions. | **D fails:** B is high for colony-level production of reproductives. | **E fails:** r = 0.75, not 1.0; colony members are not genetically identical.",
      "sectionId": "c172",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following does NOT represent altruistic behavior explained by kin selection?",
      "choices": [
        "A Belding's ground squirrel giving an alarm call that attracts predator attention, warning nearby relatives",
        "Worker ants tending larvae in a eusocial colony instead of reproducing independently",
        "Naked mole-rat workers digging tunnels and defending a colony in which only the queen reproduces",
        "A vampire bat sharing blood meals with an unrelated roost-mate who fed it when it was hungry last month",
        "A scrub jay acting as a helper at the nest of its parents, raising younger siblings"
      ],
      "answer": 3,
      "why": "**D.** Vampire bat reciprocal food sharing among unrelated individuals is explained by RECIPROCAL ALTRUISM (tit-for-tat), not kin selection. The benefit comes from future reciprocation, not shared genes. | **A, B, C, E** all involve helping close relatives and are explained by kin selection / Hamilton's rule.",
      "sectionId": "c172",
      "chapterId": "ch17"
    },
    {
      "prompt": "The Laetoli footprints (3.5 mya, Tanzania) are significant because:",
      "choices": [
        "They show bipedal tracks with arched foot and aligned big toe, confirming Au. afarensis walked fully upright",
        "They are the oldest hominin fossils, predating Sahelanthropus tchadensis",
        "They show knuckle-walking alongside bipedal tracks, showing a transition period",
        "Stone tools found alongside prints directly link bipedalism to toolmaking",
        "They contain preserved ancient DNA that was sequenced to confirm the species identity of the track-maker"
      ],
      "answer": 0,
      "why": "**A.** Laetoli footprints (Au. afarensis, ~3.5 mya) show a distinctly human-like arch and forward-pointing big toe in volcanic ash. No stone tools at the site. They don't predate Sahelanthropus (~7 mya). Direct behavioral evidence for early bipedalism. | **Wrong E:** DNA does not survive 3.5 million years; the footprints are significant because their morphology (arched foot, adducted big toe) directly demonstrates bipedal locomotion.",
      "sectionId": "c173",
      "chapterId": "ch17"
    },
    {
      "prompt": "Coevolution occurs when which combination of conditions is present?",
      "choices": [
        "Two species share the same geographic range but do not interact",
        "One species evolves in response to a constant, unchanging abiotic environment",
        "Two or more species reciprocally affect each other's evolution through their ecological interactions",
        "A single species evolves adaptations to multiple independent environmental pressures simultaneously",
        "Two species independently evolve similar traits in similar environments"
      ],
      "answer": 2,
      "why": "**C.** Coevolution = reciprocal evolutionary change between interacting species: each species' evolution is driven by and drives the other's. | **A fails:** no interaction means no coevolution. | **B fails:** evolution in response to abiotic factors is not coevolution. | **D fails:** adaptation to multiple environments is not coevolution unless other species are involved. | **E fails:** independent evolution of similar traits is convergence, not coevolution.",
      "sectionId": "c173",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following are examples of coevolution?**I. The Red Queen hypothesis — parasites and hosts evolve in a continuous arms race.**II. Milkweed toxin (cardenolide) resistance and sequestration in monarch butterflies.**III. The long nectary spur of Angraecum sesquipedale orchids and the matching proboscis of its hawk-moth pollinator.**IV. Mycorrhizal fungi forming mutualistic associations with plant roots.",
      "choices": [
        "I and III only",
        "I, II, and III only",
        "II and IV only",
        "I, III, and IV only",
        "All four examples involve coevolution"
      ],
      "answer": 4,
      "why": "**E.** All four are coevolution: host-parasite arms races (I), plant-herbivore chemical arms races (II), flower-pollinator mutualism (III), and plant-fungus mutualism (IV) all involve reciprocal evolutionary change. | **None of the partial answers are correct** — all four qualify.",
      "sectionId": "c173",
      "chapterId": "ch17"
    },
    {
      "prompt": "In a host-parasite coevolutionary arms race, what is the expected sequence of evolutionary responses?",
      "choices": [
        "Host evolves resistance → parasite evolves counter-resistance → host evolves new resistance → continuing cycle (Red Queen dynamics)",
        "Host evolves resistance → parasite goes extinct → host resistance genes are lost by drift",
        "Parasite evolves virulence → host goes extinct → parasite finds new host",
        "Both species simultaneously evolve identical adaptations to a shared abiotic stress",
        "Host builds immunity within lifetime → offspring inherit acquired immunity → parasite cannot evolve counter-resistance"
      ],
      "answer": 0,
      "why": "**A.** The Red Queen hypothesis: perpetual coevolutionary cycling — host resistance spreads → parasite counter-adapts → new host alleles favored → cycle continues. Neither species \"wins\" permanently. | **B fails:** parasites rarely go extinct; they coevolve. | **C fails:** virulent parasites that kill hosts typically evolve reduced virulence (epidemiological tradeoff). | **D fails:** coevolution is between species, not adaptation to shared abiotic stress. | **E fails:** Lamarckian inheritance of acquired immunity is false.",
      "sectionId": "c173",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following does NOT represent coevolution?",
      "choices": [
        "Acacia trees producing extra-floral nectaries to reward ant defenders that protect them from herbivores",
        "Cuckoo eggs mimicking host eggs in color/pattern, and host birds evolving better egg discrimination",
        "Clownfish and sea anemone developing mutual protection and nutrition exchange",
        "Polar bears evolving white fur to match their snowy Arctic environment",
        "Yucca plants and yucca moths being exclusively interdependent for pollination and larval nutrition"
      ],
      "answer": 3,
      "why": "**D.** Polar bear fur color is adaptation to an abiotic environment (snow), not a response to another species. No reciprocal evolutionary interaction with another organism is involved. | **A** = plant-ant mutualism, **B** = brood parasite-host arms race, **C** = marine mutualism, **E** = obligate mutualism — all are coevolution.",
      "sectionId": "c173",
      "chapterId": "ch17"
    },
    {
      "prompt": "Neanderthals possess the human-specific version of FOXP2. Most parsimonious explanation:",
      "choices": [
        "FOXP2 mutations evolved independently (convergently) in both Neanderthals and H. sapiens",
        "Mutations occurred in the common ancestor of both lineages before divergence ~600 kya — Neanderthals inherited them and may have had vocal communication capacity",
        "Neanderthals acquired FOXP2 through interbreeding with H. sapiens",
        "FOXP2 is unimportant for language since Neanderthals had it but apparently didn't develop full language",
        "The FOXP2 gene was horizontally transferred from H. sapiens to Neanderthals via shared viral vectors"
      ],
      "answer": 1,
      "why": "**B.** Parsimony: one origin of FOXP2 mutations in the common ancestor is simpler than two independent origins. Mutations predated the lineage split. Neanderthals inherited them. Compatible with vocal communication — consistent with complex behaviors (burials, tools, ochre use). Interbreeding (C) doesn't explain a mutation that predates divergence. | **Wrong E:** Horizontal gene transfer between hominin species via viruses is not a recognized mechanism; the shared FOXP2 variant is most parsimoniously explained by inheritance from a common ancestor.",
      "sectionId": "c174",
      "chapterId": "ch17"
    },
    {
      "prompt": "An event qualifies as a \"mass extinction\" when which combination of conditions is met?",
      "choices": [
        "A single species goes extinct due to overhunting by humans",
        "Background extinction rates slightly exceed speciation rates for 10,000 years",
        "A large proportion of Earth's species (typically >50%) are lost across many taxonomic groups in a geologically short time interval",
        "A single taxonomic group (e.g., all dinosaurs) goes extinct due to a specific cause",
        "Species diversity decreases in a single biome while remaining stable globally"
      ],
      "answer": 2,
      "why": "**C.** Mass extinctions are defined by: (1) high proportion of species lost (typically >50%), (2) spanning multiple phyla/groups, (3) geologically rapid (thousands to millions of years, short relative to Earth history). | **A fails:** single-species extinction is background extinction, not mass. | **B fails:** slight imbalance for 10 ky is not a mass extinction event. | **D fails:** targeting one group is a biotic crisis, not a mass extinction. | **E fails:** regional loss without global impact is not a mass extinction.",
      "sectionId": "c174",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which statements about mass extinctions are TRUE?**I. The End-Permian extinction (~252 Ma) was the largest, eliminating ~96% of marine species.**II. The End-Cretaceous extinction (~66 Ma) was caused solely by massive volcanism in the Deccan Traps.**III. Mass extinctions reset ecological dominance, opening niches for surviving lineages to diversify.**IV. The Cambrian Explosion is an example of rapid diversification following a mass extinction.",
      "choices": [
        "I only",
        "I and III only",
        "I and III only",
        "I, II, and III only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C (= I and III).** | **II fails:** the K-Pg extinction is now understood to have been primarily caused by the Chicxulub asteroid impact, with Deccan volcanism as a contributing factor, not the sole cause. | **IV fails:** the Cambrian Explosion (~541 Ma) followed the Ediacaran period; it was not driven by a preceding mass extinction — it was a radiation of novel body plans.",
      "sectionId": "c174",
      "chapterId": "ch17"
    },
    {
      "prompt": "What sequence of events best explains how an asteroid impact caused the End-Cretaceous mass extinction?",
      "choices": [
        "Asteroid impact → rapid global warming → ocean anoxia → food web collapse from bottom up",
        "Asteroid impact → ejecta + fires blocked sunlight → photosynthesis collapsed → plant/phytoplankton die-off → cascading food web collapse",
        "Asteroid impact → triggered supervolcanoes globally → CO₂ caused acid rain → carbonate shells dissolved",
        "Asteroid impact → direct heat pulse killed all animals in impact zone → disease spread globally from carcasses",
        "Asteroid impact → magnetic field reversal → increased UV radiation → DNA damage in all organisms"
      ],
      "answer": 1,
      "why": "**B.** Impact winter: (1) dust + sulfate aerosols block solar radiation, (2) global cooling + dark, (3) photosynthesis stops, (4) plants and phytoplankton collapse, (5) herbivores and then carnivores starve. | **A fails:** initial cooling (not warming) was the primary effect. | **C fails:** the impact did not trigger global supervolcanoes. | **D fails:** direct heat was regional, not global. | **E fails:** impacts do not cause magnetic reversals.",
      "sectionId": "c174",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following does NOT correctly describe a consequence of the End-Cretaceous (K-Pg) mass extinction?",
      "choices": [
        "Non-avian dinosaurs went extinct, removing dominant large terrestrial vertebrates",
        "Surviving small mammals subsequently diversified into the ecological niches vacated by non-avian dinosaurs",
        "Ammonites went extinct at the K-Pg boundary while nautiloids survived",
        "All marine life was eliminated at the K-Pg boundary, requiring complete re-colonization from freshwater",
        "The K-Pg boundary is marked by an iridium anomaly in the global rock record"
      ],
      "answer": 3,
      "why": "**D.** The K-Pg extinction did NOT eliminate all marine life — many marine groups survived (sharks, bony fish, marine turtles, crocodilians, birds). About 50% of marine species went extinct, not all. | **A, B, C, E** are all accurate descriptions of K-Pg extinction events.",
      "sectionId": "c174",
      "chapterId": "ch17"
    },
    {
      "prompt": "Why does ~1-4% Neanderthal DNA in non-African (but not sub-Saharan African) humans prove interbreeding occurred AFTER H. sapiens left Africa?",
      "choices": [
        "Africans simply lost Neanderthal DNA through genetic drift over time",
        "Neanderthals were ancestral to all humans; Africans diverged first and lost the alleles",
        "If it were just shared common ancestry, all humans including Africans would carry equal amounts. The geographic restriction to non-Africans pinpoints interbreeding after H. sapiens migrated out but before spreading globally",
        "Sub-Saharan Africans have more diverse immune genes that eliminated Neanderthal alleles through selection",
        "Neanderthal DNA was introduced into non-African populations by a separate back-migration of Neanderthals into Africa that later reversed"
      ],
      "answer": 2,
      "why": "**C.** Common ancestry from divergence ~600 kya would give ALL humans similar amounts. Non-African-specific pattern means gene flow happened specifically where H. sapiens first encountered Neanderthals — Middle East/Europe/Asia — after leaving Africa. Sub-Saharan Africans never geographically encountered Neanderthals. | **Wrong E:** There is no evidence of Neanderthals migrating into sub-Saharan Africa; the geographic restriction of Neanderthal DNA to non-Africans points to interbreeding after the Out of Africa dispersal.",
      "sectionId": "c175",
      "chapterId": "ch17"
    },
    {
      "prompt": "Adaptive radiation is most likely to occur when which combination of conditions is present?",
      "choices": [
        "A diverse, species-rich environment with many established competitors and predators",
        "A single large panmictic population subject to stabilizing selection in a stable environment",
        "Multiple ancestral species invade a new environment simultaneously and compete for limited niches",
        "A lineage enters an ecologically open environment (e.g., after extinction or island colonization) with available niches and sufficient genetic variation",
        "A species undergoes polyploidy, instantly producing multiple reproductively isolated variants"
      ],
      "answer": 3,
      "why": "**D.** Adaptive radiation requires: (1) ecological opportunity (open niches — empty island, post-extinction), (2) a lineage capable of diversifying, (3) key innovation or morphological plasticity. | **A fails:** established competitors resist invasion and suppress radiation. | **B fails:** stabilizing selection maintains the status quo. | **C fails:** multiple invaders competing does not promote radiation the same way as a single pioneer lineage. | **E fails:** polyploidy creates new species but not necessarily adaptive radiation into multiple niches.",
      "sectionId": "c175",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following are recognized examples of adaptive radiation?**I. Darwin's finches on the Galapagos — diversifying from a single finch ancestor into ~15 species.**II. Hawaiian honeycreepers — diversifying from a single rosefinch ancestor into 50+ species.**III. Cichlid fish in African Great Lakes — hundreds of species diverging within lakes in <2 million years.**IV. The persistence of horseshoe crabs largely unchanged for ~450 million years.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III only",
        "I, II, III, and IV",
        "None of these are adaptive radiation"
      ],
      "answer": 2,
      "why": "**C.** Galapagos finches, Hawaiian honeycreepers, and African cichlids are all classic adaptive radiations. | **IV fails:** horseshoe crabs are a case of evolutionary stasis (living fossils), the opposite of adaptive radiation.",
      "sectionId": "c175",
      "chapterId": "ch17"
    },
    {
      "prompt": "What sequence of events produced the adaptive radiation of cichlid fish in Lake Victoria?",
      "choices": [
        "Single ancestor colonized lake → vacant niches available → disruptive selection + sexual selection → rapid speciation into hundreds of species with different feeding ecologies",
        "Multiple ancestor species invaded simultaneously → competitive exclusion → each species specialized → diversity stabilized",
        "Continental drift isolated fish populations in separate basins → vicariant speciation → reconnection created mixed fauna",
        "Hybridization between distant relatives → allopolyploidy → hundreds of polyploid species",
        "Climate change drove extinction of diverse fauna → cichlids expanded into vacant niches by phenotypic plasticity without speciation"
      ],
      "answer": 0,
      "why": "**A.** Lake Victoria cichlids: single colonization → open niche space → disruptive selection on feeding morphology + sexual selection on color → rapid sympatric/parapatric radiation into ~500 species in <15,000 years. | **B fails:** multiple simultaneous invasions do not produce radiation; the single-ancestor bottleneck is key. | **C fails:** Lake Victoria cichlids are not vicariant — they radiated within the lake. | **D fails:** allopolyploidy is rare in fish. | **E fails:** speciation (not just plasticity) occurred.",
      "sectionId": "c175",
      "chapterId": "ch17"
    },
    {
      "prompt": "Which of the following does NOT represent a factor that promotes adaptive radiation?",
      "choices": [
        "Key morphological innovations that allow exploitation of new resources (e.g., the tetrapod limb)",
        "Ecological opportunity provided by mass extinctions vacating niches",
        "Island or lake colonization providing geographic isolation from source competitors",
        "Strong stabilizing selection maintaining a single optimal phenotype across all populations",
        "High phenotypic plasticity allowing a lineage to exploit multiple new environments"
      ],
      "answer": 3,
      "why": "**D.** Stabilizing selection homogenizes populations toward a single optimum — it is the opposite of diversification. Adaptive radiation requires divergent/disruptive selection. | **A, B, C, E** all promote or are associated with adaptive radiation.",
      "sectionId": "c175",
      "chapterId": "ch17"
    },
    {
      "prompt": "Testosterone increases mating success in young men but raises prostate cancer and heart disease risk in older men. Which concept BEST explains why this allele persists?",
      "choices": [
        "Evolutionary lag — testosterone hasn't been eliminated because selection hasn't had enough time",
        "Mutation accumulation — the late-life costs are late-acting mutations selection can't see",
        "An immunological trade-off between reproductive investment and immune defense",
        "Antagonistic pleiotropy — early reproductive benefits outweigh late-life costs, especially under ancestral conditions where few males survived to old age",
        "Genetic drift — testosterone-related alleles fluctuate randomly with no consistent fitness effect across populations"
      ],
      "answer": 3,
      "why": "**D.** Classic antagonistic pleiotropy. In ancestral environments, most males died before prostate cancer would manifest — selection strongly favored early benefits and couldn't \"see\" late costs. B is wrong: mutation accumulation has NO early benefit, just neutral late-acting accumulation. | **Wrong E:** The consistent pattern of early-life benefit and late-life cost across populations is not random drift; it is antagonistic pleiotropy where the same gene has opposing fitness effects at different life stages.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "Morning sickness in early pregnancy (nausea + food aversions) is BEST explained as:",
      "choices": [
        "A side effect of hormonal changes with no fitness consequences",
        "Evolutionary mismatch — our ancestors ate different foods",
        "An adaptation — aversion to potentially contaminated foods protects the fetus during organogenesis (weeks 6–18), when it is most vulnerable to toxins",
        "Antagonistic pleiotropy — beneficial for the fetus but costly for the mother",
        "Kin selection — the mother's nausea signals to relatives that she needs provisioning during pregnancy"
      ],
      "answer": 2,
      "why": "**C.** Reason #6: apparent disease is actually adaptation. Morning sickness peaks at 6–18 weeks — exactly when fetal organs develop and are most vulnerable to teratogens. Women with morning sickness have lower miscarriage rates. Food aversions are strongest for potentially contaminated foods. The \"sickness\" IS the defense. | **Wrong E:** Kin selection involves helping genetic relatives at a cost to the helper; morning sickness is best explained as a direct maternal adaptation protecting the embryo during organogenesis, not a social signaling mechanism.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "The \"Cambrian Explosion\" refers to which specific phenomenon?",
      "choices": [
        "A volcanic super-eruption at the Precambrian-Cambrian boundary that killed 90% of life",
        "The gradual diversification of multicellular life over 500 million years of the Precambrian",
        "The geologically rapid appearance of most major animal body plans (~541 Ma) within ~25 million years, as recorded in the fossil record",
        "The simultaneous extinction of all Ediacaran organisms at 541 Ma followed by recolonization from microbes",
        "A sudden increase in atmospheric oxygen at 541 Ma that made complex animal life impossible before that time"
      ],
      "answer": 2,
      "why": "**C.** The Cambrian Explosion: ~541 Ma, most metazoan phyla appear within ~25 My — a rapid diversification by geological standards, though still millions of years of actual evolution. | **A fails:** no super-eruption defines the boundary. | **B fails:** the explosion is rapid (<25 My), not gradual over 500 My. | **D fails:** some Ediacaran lineages may have persisted into the Cambrian; the explosion was not recolonization from microbes. | **E fails:** increased oxygen is a contributing factor, not the definition of the explosion itself.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which hypotheses have been proposed to explain the Cambrian Explosion?**I. The rise of atmospheric oxygen enabled larger, more metabolically active animal bodies.**II. Evolution of predator-prey arms races (e.g., eyes, mineralized skeletons) drove rapid diversification.**III. Snowball Earth thaw released nutrients and created ecological opportunities for diversification.**IV. The Cambrian Explosion was caused by a single mutation that created the genetic toolkit for all animal body plans.",
      "choices": [
        "I only",
        "I and II only",
        "I, II, and III only",
        "I, II, III, and IV",
        "None — the cause remains entirely unknown"
      ],
      "answer": 2,
      "why": "**C.** Oxygen rise, predator-prey arms races, and Snowball Earth nutrient release are all legitimate hypotheses with supporting evidence. | **IV fails:** Hox genes and developmental toolkits existed before the Cambrian; a single mutation does not explain the explosion.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "What does the Burgess Shale (British Columbia) reveal about Cambrian life?",
      "choices": [
        "Exceptional soft-body preservation shows diverse animal body plans — including many that do not fit neatly into modern phyla — indicating experimental morphological diversity during the Cambrian",
        "Only mineralized skeletons are preserved, providing a biased but complete picture of Cambrian diversity",
        "Burgess Shale fossils show exclusively Precambrian life forms that pre-date the Cambrian Explosion",
        "The Burgess Shale confirms that only vertebrates survived the Cambrian, with all invertebrate phyla going extinct",
        "Soft-tissue preservation in Burgess Shale is due to rapid mineralization by hydrothermal vents"
      ],
      "answer": 0,
      "why": "**A.** Burgess Shale's exceptional preservation (Lagerstatten) reveals soft-bodied organisms including anomalocaridids, opabiniids, and others with no clear modern relatives — suggesting a much greater morphological disparity than species richness alone would suggest. | **B fails:** both hard and soft tissues are preserved. | **C fails:** Burgess Shale is ~508 Ma, firmly within the Cambrian. | **D fails:** all major modern phyla have Cambrian representatives. | **E fails:** preservation was by rapid burial in anoxic sediment, not hydrothermal mineralization.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which of the following does NOT correctly describe the Cambrian Explosion?",
      "choices": [
        "Most major animal phyla first appear in the fossil record within a geologically short interval around 541 Ma",
        "The appearance of hard mineralized parts (shells, exoskeletons) in the early Cambrian improved fossilization potential",
        "Precambrian Ediacaran fauna (~635-541 Ma) represents an earlier radiation of multicellular organisms",
        "The Cambrian Explosion demonstrates that species can evolve without common ancestry, refuting evolution",
        "Molecular clock data suggest that many animal lineages had deeper Precambrian origins than the fossil record shows"
      ],
      "answer": 3,
      "why": "**D.** The Cambrian Explosion does not refute evolution or common ancestry — it is evidence for rapid diversification from common ancestors. Molecular data and phylogenetics support deep shared ancestry. | **A, B, C, E** are all accurate descriptions of the Cambrian Explosion and its context.",
      "sectionId": "c181",
      "chapterId": "ch18"
    },
    {
      "prompt": "Cholera tends to maintain high virulence. The BEST evolutionary explanation:",
      "choices": [
        "Cholera hasn't had enough evolutionary time to reduce its virulence",
        "Cholera spreads via contaminated water — even bedridden or dead hosts contaminate water supplies, so high virulence doesn't reduce transmission fitness",
        "High virulence triggers stronger immune responses that paradoxically help cholera spread",
        "Cholera's genome is too small to evolve toward lower virulence",
        "Cholera maintains high virulence because a co-infecting bacteriophage continuously selects for increased toxin production"
      ],
      "answer": 1,
      "why": "**B.** Transmission mode determines optimal virulence. Cholera doesn't need a mobile, active host.\r\n\r\nDiagram: Virulence Trade-off Model\r\n\r\n\r\n\r\n1. \r\n2. \r\nPathogen Fitness\r\nVirulence (harm to host)\r\n\r\nLow\r\nMedium\r\nHigh\r\n\r\n\r\n\r\n3. \r\n\r\nOptimal virulence\r\n(most pathogens)\r\n\r\n\r\nWater-borne\r\n(e.g., cholera)\r\nhigh virulence maintained\r\n\r\nLow within-host\r\nreplication\r\nKills host before\r\ntransmission\r\n\r\n4. \r\nDirect/respiratory transmission\r\n5. \r\nWater-borne transmission\r\n\r\nGold curve: for most pathogens, intermediate virulence maximizes fitness (enough replication to transmit, not so much it kills host before spreading). Blue dashed: water-borne pathogens (cholera) can maintain high virulence because transmission doesn't require an active mobile host.",
      "sectionId": "c182",
      "chapterId": "ch18"
    },
    {
      "prompt": "Punctuated equilibrium predicts which specific pattern in the fossil record?",
      "choices": [
        "Continuous, gradual morphological change throughout a species' stratigraphic range",
        "Long periods of morphological stasis punctuated by geologically rapid bursts of change associated with speciation events",
        "Random, unpredictable changes in morphology with no correlation to speciation or environment",
        "Large evolutionary jumps (saltations) caused by single major mutations changing body plans instantly",
        "Rapid change only in geologically recent species, with ancient species showing more gradualism"
      ],
      "answer": 1,
      "why": "**B.** Punctuated equilibrium (Eldredge & Gould 1972): most morphological change occurs rapidly during speciation events; between speciation events, lineages remain in stasis. This produces a \"stepped\" rather than smoothly graded fossil record. | **A fails:** this is phyletic gradualism. | **C fails:** the pattern is not random. | **D fails:** saltation involves macro-mutations; P.E. works via standard microevolutionary mechanisms applied rapidly. | **E fails:** P.E. is not restricted to recent species.",
      "sectionId": "c182",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which statements about punctuated equilibrium are TRUE?**I. Morphological stasis may reflect strong stabilizing selection maintaining the phenotypic optimum.**II. Rapid change during speciation in P.E. is driven by saltational macro-mutations, not standard natural selection.**III. P.E. is consistent with standard neo-Darwinian mechanisms — it predicts where and when change is concentrated, not a different mechanism.**IV. The fossil record of some lineages (e.g., trilobites, brachiopods) shows stasis over millions of years consistent with P.E.",
      "choices": [
        "I only",
        "I and IV only",
        "I, III, and IV only",
        "I, III, and IV only",
        "All four statements are true"
      ],
      "answer": 3,
      "why": "**D (= I, III, and IV).** | **II fails:** Eldredge and Gould explicitly stated that P.E. does NOT require saltational mutations — it operates through normal microevolutionary processes concentrated in peripheral isolate populations during speciation.",
      "sectionId": "c182",
      "chapterId": "ch18"
    },
    {
      "prompt": "According to Eldredge and Gould, why do peripheral isolate populations experience more rapid evolutionary change than the central (core) population?",
      "choices": [
        "Peripheral populations have higher mutation rates due to increased cosmic-ray exposure at range edges",
        "Peripheral populations are larger and thus have more raw material for selection to act on",
        "Peripheral populations are small (enhancing drift) and face different local selection pressures; they are also buffered from gene flow from the central population",
        "Peripheral populations experience more frequent hybridization events, generating novel genotypes",
        "Central populations evolve faster because they have more resources and reproduce more rapidly"
      ],
      "answer": 2,
      "why": "**C.** Small peripheral populations: (1) drift is stronger (small N), (2) local environment differs (different selection), (3) isolation from central gene flow allows divergence to persist. This is the classic peripatric speciation model underlying P.E. | **A fails:** mutation rates are not elevated at range edges. | **B fails:** peripheral populations are smaller, not larger. | **D fails:** hybridization is not the mechanism. | **E fails:** central populations are large and buffered by gene flow, promoting stasis.",
      "sectionId": "c182",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which of the following does NOT correctly describe the contrast between punctuated equilibrium and phyletic gradualism?",
      "choices": [
        "Gradualism predicts transitional intermediates should be common; P.E. predicts they should be rare (rapid change in small populations leaves few fossils)",
        "P.E. predicts that most species in the fossil record will appear suddenly and persist largely unchanged until extinction",
        "Gradualism assumes change is spread throughout the duration of a lineage; P.E. concentrates change at cladogenesis events",
        "P.E. requires different genetic mechanisms than gradualism, relying on macro-mutations rather than allele frequency change",
        "Both P.E. and gradualism accept that evolution occurs; they differ on the rate and timing of morphological change"
      ],
      "answer": 3,
      "why": "**D.** Eldredge and Gould specifically rejected the idea that P.E. requires different genetic mechanisms. P.E. uses standard microevolutionary processes (selection, drift, mutation) — it just concentrates them at speciation events rather than spreading them throughout lineage history. | **A, B, C, E** accurately contrast P.E. and gradualism.",
      "sectionId": "c182",
      "chapterId": "ch18"
    },
    {
      "prompt": "The hygiene hypothesis explains increased allergy and autoimmune disease rates in industrialized nations as:",
      "choices": [
        "Environmental pollutants causing immune gene mutations increasing allergy risk",
        "Greater pathogen diversity in urban environments overwhelming immune tolerance",
        "High-calorie diets causing chronic inflammation that cross-reacts with self-antigens",
        "Reduced parasite/pathogen exposure in clean environments creates a mismatch — our immune system evolved for high pathogen load and misdirects against harmless antigens when that load is absent",
        "Antibiotic overuse in childhood destroys beneficial gut bacteria, triggering autoimmune attacks on self-tissues"
      ],
      "answer": 3,
      "why": "**D.** Evolutionary mismatch: immune system's calibration evolved alongside high parasites/pathogens. In clean modern environments, it becomes misdirected. Farm children with high animal + microbe exposure have significantly lower allergy rates. | **Wrong E:** While antibiotic-microbiome disruption may contribute, the hygiene hypothesis specifically addresses reduced pathogen/parasite exposure creating an evolutionary mismatch for the immune system evolved under high pathogen load.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "The finding that yeast cell-wall repair genes are homologous to human blood vessel growth genes demonstrates:",
      "choices": [
        "Yeast and humans are more closely related than morphology suggests",
        "Gene networks were transferred horizontally between fungi and vertebrate ancestors",
        "Ancient conserved gene networks can be studied in tractable model organisms to identify medically relevant genes in humans",
        "Convergent evolution repurposes genes for similar functions in unrelated organisms",
        "The similarity is coincidental — conserved genes in such distantly related organisms arise by chance alone"
      ],
      "answer": 2,
      "why": "**C.** Marcotte's research (Ch 18 intro). Yeast gene networks are well-characterized and easy to manipulate. Because of evolutionary conservation (>1 billion years of shared ancestry), studying yeast networks identified 8 new human angiogenesis genes — potential cancer targets. Evolution-based comparative research = practical medicine. | **Wrong E:** Deep homology of gene networks across 1+ billion years of divergence is not coincidental; it reflects conserved ancestral pathways that can inform medical research through model organisms like yeast.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "Evolutionary developmental biology (Evo-Devo) focuses on explaining macroevolution by examining which relationship?",
      "choices": [
        "The relationship between geographic isolation and speciation rates",
        "The relationship between neutral mutations and molecular clock rates",
        "How changes in developmental gene expression and regulatory networks produce morphological diversity and evolutionary novelties",
        "How natural selection acting on adult phenotypes drives population-level allele frequency changes",
        "How ecological interactions between species shape community structure over evolutionary time"
      ],
      "answer": 2,
      "why": "**C.** Evo-Devo bridges development and evolution: mutations in developmental regulatory genes (Hox, Pax, Dll) or their cis-regulatory elements alter when, where, and how much genes are expressed, producing major morphological changes. | **A fails:** this is speciation biology. | **B fails:** this is molecular evolution / phylogenetics. | **D fails:** this is population genetics / standard neo-Darwinism. | **E fails:** this is community ecology / coevolution.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which statements about Hox genes and Evo-Devo are TRUE?**I. Hox genes specify segment identity along the anterior-posterior axis in bilaterians.**II. Hox genes are conserved across insects, vertebrates, and other bilaterians, suggesting deep common ancestry.**III. Changes in Hox gene expression patterns (not just protein sequence) can produce major morphological differences.**IV. Evo-Devo shows that morphological evolution requires the evolution of entirely new gene families for each new structure.",
      "choices": [
        "I and II only",
        "I, II, and III only",
        "I, II, and III only",
        "I, III, and IV only",
        "All four statements are true"
      ],
      "answer": 2,
      "why": "**C (= I, II, and III).** | **IV fails:** Evo-Devo demonstrates the opposite — evolutionary novelties often arise from co-option and rewiring of EXISTING genes and regulatory networks, not from de novo evolution of entirely new gene families.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "How can a single regulatory mutation in a Hox gene's cis-regulatory element produce a large morphological change?",
      "choices": [
        "It directly alters the amino acid sequence of the Hox protein, changing which DNA sequences it binds",
        "It changes the spatial or temporal expression domain of the Hox gene, causing a different set of downstream target genes to be activated in a new body region or developmental stage",
        "It increases the overall mutation rate of the genome, accelerating evolution of all downstream genes",
        "It causes gene duplication, providing a new gene copy that can evolve a new function",
        "It triggers horizontal gene transfer from a symbiotic microbe, introducing novel biochemical pathways"
      ],
      "answer": 1,
      "why": "**B.** Cis-regulatory mutations alter enhancer/silencer function: the Hox protein sequence is unchanged, but WHERE and WHEN it is expressed changes → downstream target genes are activated in new body regions → major morphological change. Classic example: Ubx expression changes correlating with limb loss in snake ancestors. | **A fails:** cis-regulatory mutations affect expression, not protein sequence. | **C fails:** Hox mutations do not increase general mutation rate. | **D fails:** gene duplication is a separate event from cis-regulatory mutation. | **E fails:** horizontal gene transfer from microbes is not relevant to Hox gene function in animals.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which of the following does NOT represent evidence or a finding from Evo-Devo?",
      "choices": [
        "The Pax6 gene controls eye development in both Drosophila and vertebrates despite their structurally different eyes, suggesting deep homology",
        "The Distal-less (Dll) gene is involved in appendage development in arthropods, vertebrates, and echinoderms",
        "Changes in the spatial expression of Ubx in Drosophila vs. crustaceans correlate with differences in thoracic limb number",
        "The neutral theory of molecular evolution explains why synonymous substitutions accumulate at a constant rate",
        "Heterochrony (changes in developmental timing) can produce paedomorphic or peramorphic morphologies"
      ],
      "answer": 4,
      "why": "**D.** The neutral theory of molecular evolution (Kimura) explains substitution rates at the molecular level — it is a finding of molecular population genetics, not Evo-Devo. Evo-Devo focuses on regulatory gene networks and their role in morphological change. | **A, B, C, E** are all core findings or concepts from Evo-Devo.",
      "sectionId": "c183",
      "chapterId": "ch18"
    },
    {
      "prompt": "A hybrid plant produced from two different species (both with 2n=14) is sterile. Then one of its cells undergoes accidental genome doubling, producing offspring with 2n=28. This offspring is MOST LIKELY:",
      "choices": [
        "Still sterile — the chromosome number mismatch from the original hybridization persists",
        "Fertile and able to interbreed freely with both parent species",
        "Fertile and reproductively isolated from both parent species — a new allopolyploid species formed in a single generation",
        "Fertile but genetically identical to one parent species, having lost the other parent's genome",
        "Fertile but only with one parent species — genome doubling restores compatibility with the maternal parent only"
      ],
      "answer": 2,
      "why": "**C.** This is allopolyploidy in action. The genome doubling gives each chromosome a pairing partner — meiosis now works correctly, so the offspring is fertile. But when it tries to mate with either parent (2n=14), the chromosome number mismatch (28 × 14) causes meiotic failure → reproductively isolated from both parents. New species, one generation, no geography required. | **Wrong E:** Allopolyploids are reproductively isolated from BOTH parents because their chromosome number (4n=28) does not match either parent (2n=14), producing triploid offspring that cannot segregate chromosomes properly.",
      "sectionId": "c133b",
      "chapterId": "ch13"
    },
    {
      "prompt": "When two mammal species hybridize, the male (XY) hybrid offspring are sterile but the female (XX) hybrids are fertile. This pattern is predicted by:",
      "choices": [
        "Temporal isolation — males mature at different rates in hybrids",
        "Haldane's Rule — heterogametic sex (XY) is more likely to be sterile/inviable because recessive incompatibility alleles on the X are exposed (hemizygous), with no backup X to mask them",
        "Hybrid vigor — females benefit from heterosis while males are harmed by it",
        "Sexual selection — females are preferred mates and therefore protected from hybrid incompatibilities",
        "Genomic imprinting — paternal X-chromosome genes are silenced in male hybrids but expressed normally in females"
      ],
      "answer": 1,
      "why": "**B.** Haldane's Rule (1922): in hybrids, the heterogametic sex (XY in mammals) is preferentially sterile/inviable. Mechanism: recessive incompatibility alleles on the X are hemizygous in XY males — no second X to mask them. XX females have a second X that can compensate. In birds, females are ZW (heterogametic) and tend to be the sterile hybrid sex. | **Wrong E:** Genomic imprinting affects specific genes, not entire sex chromosomes; Haldane's Rule explains male hybrid sterility through exposure of recessive incompatibility alleles on the single X in XY individuals.",
      "sectionId": "c133b",
      "chapterId": "ch13"
    },
    {
      "prompt": "The Wallace Line separates Asian and Australasian fauna even though the islands are geographically close. The BEST explanation is:",
      "choices": [
        "Climate differences between the two sides favor completely different adaptations",
        "Active geological uplift created a mountain barrier preventing migration",
        "Historical biogeographers drew the line artificially based on species counts",
        "A deep water channel between the Asian and Australian continental shelves persisted even during ice age low sea levels, preventing most terrestrial organisms from crossing",
        "Competitive exclusion — Asian species outcompete Australasian species whenever they come into contact across the line"
      ],
      "answer": 3,
      "why": "**D.** The Wallace Line marks the edge of the continental shelves. Even when sea levels dropped during ice ages (exposing many land bridges), a deep ocean channel remained between Asia and Australia. This water barrier prevented most terrestrial animals from crossing — creating the sharp biogeographic discontinuity Wallace documented in 1859. | **Wrong E:** The Wallace Line is explained by a persistent deep-water barrier preventing dispersal, not by competitive exclusion; the faunas largely never had the opportunity to compete.",
      "sectionId": "c145b",
      "chapterId": "ch14"
    },
    {
      "prompt": "A wildlife conservation plan proposes maintaining a breeding population of 45 individuals. The 50/500 rule suggests this is:",
      "choices": [
        "Acceptable for long-term genetic health if food resources are sufficient",
        "Insufficient even for short-term inbreeding prevention — short-term minimum is Ne ≥ 50; long-term minimum is Ne ≥ 500",
        "Fine because the 500 rule only applies to endangered species, not conservation plans",
        "Adequate if the 45 individuals are genetically diverse",
        "The 50/500 rule has been replaced by the 100/1000 rule, so 45 individuals meets the older standard"
      ],
      "answer": 1,
      "why": "**B.** The 50/500 rule: Ne ≥ 50 is the short-term minimum to keep inbreeding rate below ~1% per generation. Ne ≥ 500 is the long-term minimum to maintain adaptive genetic variation. 45 individuals falls below even the short-term threshold. Also note: Ne < N in real populations, so 45 census individuals = even fewer effective breeders. | **Wrong E:** While some researchers suggest higher thresholds, the 50/500 rule remains widely used; the key point is that 45 falls below even the minimum short-term threshold of Ne=50.",
      "sectionId": "c145b",
      "chapterId": "ch14"
    },
    {
      "prompt": "Over 30 years of trophy hunting, average bighorn sheep horn size declined ~20%. This demonstrates:",
      "choices": [
        "Phenotypic plasticity — sheep grow smaller horns when large-horned individuals are removed from the population",
        "Genetic drift — random chance caused horn size alleles to decline in small trophy-hunted populations",
        "Human-imposed directional selection opposing natural selection — trophy hunting preferentially removes large-horned males before full reproduction, increasing small-horn allele frequency",
        "Disruptive selection — trophy hunting favors both very large and very small horns",
        "Stabilizing selection — horn size is converging on an intermediate optimum balancing mating success with predator avoidance"
      ],
      "answer": 2,
      "why": "**C.** Trophy hunters preferentially kill the largest-horned males (highest trophy value). Large-horned males that would normally maximize fitness through many matings are killed early, before they can fully pass on their genes. Small-horn alleles increase in frequency over generations — the opposite of what natural selection would produce. This is human-imposed directional selection. | **Wrong E:** Stabilizing selection maintains the mean; the observed 20% decline in horn size over 30 years is a directional shift caused by selective removal of large-horned males by trophy hunters.",
      "sectionId": "c81b",
      "chapterId": "ch8"
    },
    {
      "prompt": "Which of the following is NOT an established mechanism by which bacteria acquire antibiotic resistance?",
      "choices": [
        "Efflux pumps that actively expel the antibiotic from the bacterial cell",
        "Enzymes (beta-lactamases) that degrade the antibiotic molecule",
        "Mutations that alter the antibiotic's molecular target (e.g., ribosome modification)",
        "Bacteria actively sensing the antibiotic and inducing directed mutations to neutralize it",
        "Horizontal gene transfer (HGT) via conjugation or plasmids spreading resistance genes between bacterial cells"
      ],
      "answer": 3,
      "why": "**D.** Bacteria do NOT \"sense\" antibiotics and then produce directed mutations. Mutations are RANDOM and pre-existing. The antibiotic doesn't instruct the bacterium to mutate — it simply kills susceptible bacteria and leaves behind those with pre-existing random mutations that confer resistance. Options A, B, C, and E are all real, established resistance mechanisms. | **Wrong D:** The concept of bacteria \"actively sensing and inducing directed mutations\" contradicts the fundamental principle that mutations are random and non-directional; this is essentially a neo-Lamarckian error.",
      "sectionId": "c81b",
      "chapterId": "ch8"
    },
    {
      "prompt": "A Tibetan high-altitude adaptation gene (EPAS1) was found to have originated from Denisovans. This demonstrates:",
      "choices": [
        "Convergent evolution — both Denisovans and Tibetans independently evolved the same EPAS1 variant",
        "The Denisovans were ancestors of all modern Asian populations",
        "Adaptive introgression — modern humans acquired a beneficial archaic allele through interbreeding that was then favored by natural selection in high-altitude environments",
        "Convergent evolution between Tibetans and Denisovans due to shared high-altitude environments",
        "Incomplete lineage sorting — the EPAS1 variant was present in the common ancestor of all hominins and retained only in Tibetans by chance"
      ],
      "answer": 2,
      "why": "**C.** Adaptive introgression = when gene flow from an archaic/related population introduces an allele that is then positively selected. Denisovans (who lived in Asia including high-altitude regions) already had an EPAS1 variant adapted for low oxygen. When H. sapiens interbred with Denisovans, this variant entered the human gene pool. At high altitudes in Tibet, it was strongly favored. This is one of the clearest examples of archaic introgression providing a direct adaptive benefit. | **Wrong E:** Phylogenetic analysis showed the Tibetan EPAS1 haplotype clusters specifically with Denisovan sequences, confirming introgression rather than incomplete lineage sorting from an ancestral population.",
      "sectionId": "c175b",
      "chapterId": "ch17"
    },
    {
      "prompt": "H. sapiens fossils at Omo Kibish, Ethiopia (~195 kya) show modern anatomy but NO art, no personal ornaments, and no evidence of long-distance trade. This means:",
      "choices": [
        "These are not actually H. sapiens — behavioral evidence is needed to classify as modern human",
        "Anatomical modernity (~195 kya) preceded behavioral modernity (~70–100 kya) by ~100,000 years; these were anatomically but not yet behaviorally modern humans",
        "Behavioral evidence doesn't preserve in fossils, so we can't make any claims about behavior",
        "These humans lacked language — language evolved simultaneously with art and personal ornaments ~70 kya",
        "These fossils are misidentified — true H. sapiens first appeared only ~70 kya when behavioral modernity emerged"
      ],
      "answer": 1,
      "why": "**B.** There is a ~100,000–200,000 year gap between anatomical modernity (modern skeleton at ~195 kya+) and behavioral modernity (symbolic thought, art, ornaments, long-distance trade at ~70–100 kya). These Omo fossils had modern bodies but pre-modern behavior. Modern skulls came first; modern minds came later. | **Wrong E:** The Omo Kibish fossils are definitively H. sapiens based on cranial morphology; anatomical and behavioral modernity are distinct phenomena that evolved at different times.",
      "sectionId": "c175b",
      "chapterId": "ch17"
    },
    {
      "prompt": "In malaria-endemic West Africa, the HbS allele is maintained at ~10–20% frequency despite causing severe anemia in homozygotes. This is BEST explained by:",
      "choices": [
        "Mutation-selection balance — the mutation rate for HbS is high enough to maintain the allele despite selection against it",
        "Heterozygote advantage (balancing selection/overdominance) — HbA/HbS heterozygotes have ~25% protection against severe malaria, giving them higher fitness than both homozygotes in malaria-endemic environments",
        "Genetic drift in small populations where the allele became fixed by chance",
        "Frequency-dependent selection favoring HbS when it is rare",
        "Directional selection — the HbS allele is steadily increasing toward fixation in malaria-endemic regions"
      ],
      "answer": 1,
      "why": "**B.** This is the classic heterozygote advantage (overdominance) example. HbA/HbS heterozygotes are protected from severe malaria — parasitized cells sickle and are cleared. This fitness advantage in malaria-endemic regions outweighs the cost of homozygous HbS/HbS disease. Selection maintains both alleles at intermediate frequencies. In non-malarial regions, HbS is purely deleterious (no compensating benefit), explaining its low frequency in non-African populations. | **Wrong E:** HbS is maintained at a stable intermediate frequency (10-20%) by balancing selection (heterozygote advantage), not increasing toward fixation; HbS/HbS homozygotes suffer severe anemia.",
      "sectionId": "c183b",
      "chapterId": "ch18"
    },
    {
      "prompt": "A tumor initially responds to chemotherapy but after several months becomes drug-resistant. By analogy with antibiotic resistance, the MOST likely explanation is:",
      "choices": [
        "Chemotherapy induced the tumor cells to mutate and become resistant",
        "The patient's immune system failed, allowing new resistant tumor cells to form",
        "Pre-existing resistant cancer cells (with random mutations) were selected for as the drug killed susceptible cells, allowing the resistant clone to expand",
        "The chemotherapy drug evolved lower toxicity over time due to selective pressure from the tumor",
        "The tumor cells acquired drug resistance genes from gut bacteria through horizontal gene transfer"
      ],
      "answer": 2,
      "why": "**C.** This is somatic evolution in action — identical mechanism to antibiotic resistance. Tumors are genetically heterogeneous (different cell lineages with different mutations). Chemotherapy kills susceptible cells. Pre-existing resistant variants (random mutations already present before treatment) are selected for and expand. This is why cancer treatment strategies now focus on targeting multiple pathways simultaneously — to prevent resistant clones from expanding. | **Wrong E:** Human cancer cells do not acquire resistance genes from bacteria via HGT; drug resistance arises through selection of pre-existing somatic mutations within the tumor cell population.",
      "sectionId": "c183b",
      "chapterId": "ch18"
    },
    {
      "prompt": "Which of the following is NOT one of Nesse's six evolutionary reasons why humans remain vulnerable to disease?",
      "choices": [
        "Pathogens evolve faster than their hosts",
        "Evolutionary history constrains solutions (can't redesign from scratch)",
        "Apparent disease is actually an adaptation (fever, morning sickness)",
        "Natural selection always optimizes health and longevity alongside reproductive fitness",
        "Genetic constraints prevent organisms from evolving resistance to all pathogens simultaneously"
      ],
      "answer": 3,
      "why": "**D.** D is the WRONG one — natural selection optimizes REPRODUCTIVE FITNESS, NOT health or longevity. This is actually the central insight of evolutionary medicine. Selection can maintain alleles that are harmful to health if they improve reproductive success. The other three (A, B, C) are all genuine Nesse reasons. The sixth reason not listed here is: selection lags behind environmental change (mismatch). | **Wrong E:** Genetic/historical constraints ARE one of Nesse's six reasons; the incorrect answer (D) falsely states that natural selection optimizes health alongside reproductive fitness, which it does not.",
      "sectionId": "c183b",
      "chapterId": "ch18"
    },
    {
      "prompt": "Carbon-14 has a half-life of 5,730 years. A bone sample shows that only 25% of the original Carbon-14 remains. Approximately how old is the bone?",
      "choices": [
        "~5,730 years (one half-life has passed)",
        "~8,595 years (1.5 half-lives have passed)",
        "~11,460 years (two half-lives have passed: 100% → 50% → 25%)",
        "~17,190 years (three half-lives have passed)",
        "~22,920 years (four half-lives have passed: 100% → 50% → 25% → 12.5% → 6.25%)"
      ],
      "answer": 2,
      "why": "**C.** After ONE half-life: 100% → 50% remains. After TWO half-lives: 50% → 25% remains. So 25% remaining = 2 half-lives = 2 × 5,730 = **11,460 years**. After three half-lives you'd have 12.5%, not 25%. | **Wrong E:** Four half-lives would leave only 6.25% parent isotope remaining, not 25%; the sample at 25% has undergone exactly two half-lives = ~11,460 years.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two populations of plants look morphologically different but readily produce fertile hybrids in the lab. Under the Biological Species Concept they would be considered _____, but under the Morphospecies Concept they would be considered _____.",
      "choices": [
        "The SAME species (fertile hybrids = gene flow possible); DIFFERENT species (morphologically distinct)",
        "DIFFERENT species (different morphology); SAME species (same morphology)",
        "SAME species (BSC); SAME species (morphospecies) — all concepts agree",
        "DIFFERENT species under both concepts because morphology always overrides fertility",
        "DIFFERENT species under BSC because lab hybrids don't count; SAME under morphospecies because all plants look similar"
      ],
      "answer": 0,
      "why": "**A.** This scenario shows where BSC and morphospecies DISAGREE. Under BSC: fertile hybrids = gene flow possible = SAME species (not reproductively isolated). Under morphospecies: morphologically distinguishable = DIFFERENT species. This is one of the core cases showing no single species concept is universally applicable. | **Wrong E:** BSC considers fertile hybridization as evidence of gene flow (same species); the scenario states the plants look morphologically different, so morphospecies would classify them as different species.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is NOT a prezygotic reproductive isolating mechanism?",
      "choices": [
        "Two species of fireflies have different flash patterns — females only respond to their species-specific pattern",
        "Two plant species flower at different times of year",
        "Sperm from Species A cannot penetrate the egg of Species B due to incompatible surface proteins",
        "Hybrid offspring of two toad species develop normally but are completely sterile",
        "Two populations of frogs use completely different species-specific mating calls that prevent cross-attraction"
      ],
      "answer": 3,
      "why": "**D.** D is POSTZYGOTIC — the hybrid is formed (zygote exists) but is sterile. This is hybrid sterility, a postzygotic barrier. A = behavioral isolation (prezygotic, pre-mating). B = temporal isolation (prezygotic, pre-mating). C = gametic incompatibility (prezygotic, post-mating but pre-fertilization). The hybrid sterility in D is the only postzygotic option. | **Wrong E:** Species-specific mating calls are a prezygotic behavioral barrier; the question asks for what is NOT prezygotic, and hybrid sterility (D) is postzygotic because it occurs after fertilization.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "A clade has 100 species. Over 4 million years, the origination rate is 5 species/my and extinction rate is 8 species/my. What happens to standing diversity?",
      "choices": [
        "Increases to 112 species (net +3 per million years × 4 my)",
        "Decreases to 88 species (μ > λ: net loss of 3 species/my × 4 my = -12; 100 − 12 = 88)",
        "Stays at 100 species because clade will reach equilibrium",
        "Goes extinct entirely because extinction rate exceeds origination rate",
        "Increases to 120 species because extinction rate is already factored into the origination rate"
      ],
      "answer": 1,
      "why": "**B.** Net change = λ − μ = 5 − 8 = −3 species/my. Over 4 my: −3 × 4 = −12 species. 100 − 12 = **88 species**. The clade is declining but hasn't gone extinct in just 4 million years. Extinction would require μ ≫ λ sustained much longer. | **Wrong E:** Origination and extinction are independent rates that must be calculated separately: 100 + (5 x 4) minus (8 x 4) = 88 species.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is NOT a standard component of a phylogenetic tree?",
      "choices": [
        "Tips (terminal ends representing living taxa or sequences)",
        "Nodes (points where lineages split = speciation events)",
        "Fitness vectors (arrows showing the direction of selection on each branch)",
        "Root (the most recent common ancestor of all taxa shown)",
        "Bootstrap values (statistical confidence scores placed on each branch to indicate reliability)"
      ],
      "answer": 2,
      "why": "**C.** Phylogenetic trees have tips, branches, nodes, and a root. \"Fitness vectors\" is not a real component — phylogenetic trees show evolutionary relationships, not selection pressures. A, B, and D are all standard tree components taught in lecture (slide 4 of Lecture 15). | **Wrong E:** Bootstrap values are analytical annotations used in phylogenetic inference, not structural components of a phylogenetic tree like tips, nodes, branches, and root.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two closely related species of salamanders that share ~90% of their DNA both independently evolved reduced limb lengths via changes to the same HOX gene regulatory region. This is BEST described as:",
      "choices": [
        "Convergent evolution (homoplasy) because both evolved similar morphology independently",
        "Parallel evolution (homoplasy) because they are closely related and used the same genetic/developmental mechanism to reach the same morphological outcome",
        "Homology because both species inherited the reduced limbs from a shared ancestor",
        "Exaptation because the HOX genes were originally used for other developmental purposes",
        "Co-evolution — both salamander species evolved reduced limbs in response to a shared predator driving reciprocal adaptation"
      ],
      "answer": 1,
      "why": "**B.** Parallel evolution = similar outcome via the SAME genetic mechanism in closely related lineages. Key markers here: (1) closely related (~90% DNA similarity), (2) same molecular mechanism (same HOX gene regulatory change). Convergent evolution typically involves DIFFERENT mechanisms in more distantly related lineages (e.g., camera eye in vertebrates vs. octopus). Both are homoplasy; the distinction is mechanism and relatedness. | **Wrong E:** Co-evolution involves reciprocal evolutionary change between interacting species; two closely related species independently evolving the same trait via the same genetic mechanism is parallel evolution, not co-evolution.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "The Great Oxidation Event (~2.4 bya) was caused by:",
      "choices": [
        "Evolution of oxygenic photosynthesis in cyanobacteria, which pumped O2 into an atmosphere that previously had essentially none",
        "The first eukaryotes evolving mitochondria, which began aerobic respiration and released O2",
        "Massive volcanic activity releasing O2 from oxidized minerals in Earth's mantle",
        "UV radiation splitting water molecules (H2O) in the upper atmosphere into H2 and O2",
        "Iron-oxidizing archaea at deep-sea vents released O&sub2 as a metabolic waste product that accumulated globally"
      ],
      "answer": 0,
      "why": "**A.** Cyanobacteria evolved oxygenic photosynthesis ~2.6 bya, producing O2 as a byproduct. This O2 accumulated in the atmosphere, triggering the Great Oxidation Event ~2.4 bya. Consequences: mass extinction of obligate anaerobes, formation of the ozone layer, and eventual evolution of aerobic respiration. Mitochondria (B) are thought to have originated ~1.8 bya as endosymbionts — AFTER the GOE. | **Wrong E:** Iron-oxidizing archaea do not produce O&sub2; the Great Oxidation Event was driven by oxygenic photosynthesis in cyanobacteria, which release O&sub2 as a byproduct of splitting water.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "After a mass extinction 66 mya, mammals rapidly diversified into many new ecological roles previously occupied by dinosaurs. The BEST description of this event:",
      "choices": [
        "Key innovation — mammals evolved a new adaptation that allowed them to outcompete dinosaurs",
        "Vicariance — continental drift separated mammal populations, allowing independent diversification",
        "Adaptive radiation triggered by extinction of competitors — mass extinction removed dinosaurs that had monopolized ecological niches for ~160 million years, releasing mammals into vacant adaptive space",
        "Sympatric speciation — mammals diversified within the same geographic range as the remaining dinosaurs",
        "Founder effect — the few surviving mammal lineages had limited genetic variation that drove rapid speciation through drift"
      ],
      "answer": 2,
      "why": "**C.** This is the classic \"extinction-triggered adaptive radiation.\" Mammals had been small and ecologically limited for ~160 million years due to competitive exclusion by dinosaurs. When the K-T extinction removed this competition, ecological niches became available. Within ~10 million years, all major mammalian orders appeared. This is NOT key innovation — mammals didn't evolve anything new to outcompete dinosaurs; rather, the competitors were removed. | **Wrong E:** The founder effect reduces genetic variation and would slow diversification; the mammalian adaptive radiation was driven by ecological opportunity from vacant niches after dinosaur extinction.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "A newly discovered pathogen is transmitted ONLY through direct physical contact with infected individuals. Evolutionary theory predicts this pathogen will evolve toward:",
      "choices": [
        "Lower or intermediate virulence — if the pathogen kills or severely incapacitates the host, transmission (requiring physical contact) drops to zero; selection favors keeping hosts mobile",
        "Higher virulence — more damage to the host means more pathogen particles available for transmission",
        "No evolutionary change in virulence — pathogens evolve resistance, not virulence",
        "Virulence is determined by the host immune system, not by pathogen evolution",
        "Maximum virulence — contact-transmitted pathogens must overwhelm the host immune system before the contact opportunity closes"
      ],
      "answer": 0,
      "why": "**A.** For contact-transmitted pathogens, transmission REQUIRES the host to be mobile and socially active (coming into physical contact with others). If the pathogen kills or bedrids the host, transmission stops. Selection therefore strongly favors lower/intermediate virulence. Compare to cholera (water-borne) where the host doesn't need to be active for transmission — cholera can be highly virulent because dying hosts still contaminate water. Transmission mode is the key determinant of optimal virulence. | **Wrong E:** Maximum virulence would incapacitate or kill the host, reducing the physical contact needed for transmission; selection favors lower/intermediate virulence to keep hosts mobile and social.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two species of fish live on opposite sides of a coral reef. They can see and smell each other but only mate with members of their own species due to color pattern differences that drive mate choice. No physical barrier separates them. This is BEST classified as:",
      "choices": [
        "Allopatric speciation by vicariance — the reef acts as a physical barrier",
        "Sympatric speciation (or completed sympatric divergence) — two species have diverged in the same geographic area with no geographic barrier, maintained by behavioral/sexual isolation",
        "Allopatric speciation by dispersal — one species colonized the other side of the reef",
        "This cannot be speciation because both species share the same habitat",
        "Peripatric speciation — a small founder population budded off from the main population at the reef edge"
      ],
      "answer": 1,
      "why": "**B.** The two fish occupy the same geographic area with no physical barrier between them. The reproductive isolation is BEHAVIORAL (color pattern-based mate choice), not geographic. This is sympatric speciation maintained by assortative mating. D is wrong — sharing a habitat doesn't prevent speciation; sympatric speciation is specifically when new species form WITHOUT geographic isolation. | **Wrong E:** Peripatric speciation involves geographic isolation of a small founder population; the scenario describes two species coexisting in the same area with behavioral isolation, which is sympatric divergence.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two possible trees for 3 species (A, B, C) require 5 and 7 evolutionary steps respectively. Under the principle of parsimony, you should:",
      "choices": [
        "Prefer the 5-step tree as the working hypothesis, since parsimony says choose the tree requiring fewest evolutionary changes",
        "Prefer the 7-step tree because more evolutionary steps means more evolutionary history is captured",
        "Accept both trees as equally valid since parsimony doesn't apply to trees with fewer than 4 taxa",
        "Reject both trees and collect more data before applying parsimony",
        "Choose the tree with the longest total branch length, as this captures the most evolutionary information"
      ],
      "answer": 0,
      "why": "**A.** Parsimony = choose the tree requiring the fewest evolutionary changes as the WORKING HYPOTHESIS. More steps = more homoplasy assumed = less parsimonious. The 5-step tree is preferred. This doesn't mean the 5-step tree is definitely correct — it's a hypothesis that can be revised with new evidence (other methods like Bayesian or maximum likelihood may give different results, especially when homoplasy is common). | **Wrong E:** Branch length reflects amount of change, not tree quality; parsimony selects the tree requiring the fewest total evolutionary changes (steps), not the longest branches.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Arrange these hominins in order of INCREASING brain size (smallest to largest average):",
      "choices": [
        "Homo sapiens → Neanderthal → H. erectus → Australopithecus",
        "Australopithecus → H. sapiens → Neanderthal → H. erectus",
        "H. sapiens → Neanderthal → Australopithecus → H. erectus",
        "Australopithecus (~450cc) → H. erectus (~900–1100cc) → H. sapiens (~1350cc) → Neanderthal (~1500cc)",
        "H. erectus (~900cc) → Australopithecus (~450cc) → Neanderthal (~1500cc) → H. sapiens (~1350cc)"
      ],
      "answer": 3,
      "why": "**D.** Brain sizes: Australopithecus ~450cc (ape-sized), H. erectus ~900–1100cc, H. sapiens ~1350cc average, Neanderthal ~1500cc (LARGEST on average). This is a key numerical anchor — Neanderthals had larger brains than modern humans on average. Brain expansion was gradual through the Homo lineage but Neanderthals exceeded our average. | **Wrong E:** This ordering does not proceed from smallest to largest; the correct sequence is Australopithecus (~450cc) then H. erectus (~900-1100cc) then H. sapiens (~1350cc) then Neanderthal (~1500cc).",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is NOT evidence supporting the common ancestry of humans and chimpanzees?",
      "choices": [
        "Human chromosome 2 contains telomeric sequences in its interior, consistent with fusion of two ancestral chromosomes (chimp 2A + 2B)",
        "Humans and chimps share ~98.5% DNA sequence similarity",
        "Humans and chimps are ecologically similar — both live in tropical forest environments and eat similar diets",
        "The human coccyx is homologous to the primate tail, consistent with descent from a common tailed ancestor",
        "Both species exhibit juvenile play behavior, suggesting shared cognitive ancestry"
      ],
      "answer": 2,
      "why": "**C.** Ecological similarity does NOT demonstrate common ancestry — that would be convergent evolution (organisms in similar environments may evolve similar traits independently). Actual evidence for common ancestry is molecular (chromosome 2 fusion, DNA similarity) and anatomical (homologous structures like coccyx). Ecological similarity alone is irrelevant to phylogenetic relationships. | **Wrong E:** Play behavior occurs in many mammalian lineages and is not specific evidence for human-chimp common ancestry; molecular and chromosomal evidence is far more compelling.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "The End-Permian \"Great Dying\" (~252 mya) is MOST associated with which cause?",
      "choices": [
        "Asteroid impact at the Chicxulub crater releasing massive energy and debris",
        "Siberian Traps volcanism erupting for ~1 million years, releasing massive CO2 causing global warming, ocean acidification, and marine anoxia",
        "Glacial episodes lowering global temperatures and sea levels during the Permian Ice Age",
        "Elevated atmospheric CO2 from early coal-forming swamp forests being burned by lightning",
        "A gamma-ray burst from a nearby supernova sterilized Earth's surface at 252 mya"
      ],
      "answer": 1,
      "why": "**B.** End-Permian = Siberian Traps. Massive volcanism released enormous CO2 + SO2, causing: runaway greenhouse warming, ocean acidification (CO2 dissolved in seawater), marine anoxia (low oxygen), and ozone depletion. ~96% of marine species and ~70% of terrestrial vertebrates went extinct. Recovery took 5–10 million years. Chicxulub asteroid = K-T (~66 mya), not Permian. Glacial episodes = End-Ordovician. | **Wrong E:** There is no geological evidence for a gamma-ray burst at the Permian-Triassic boundary; the evidence overwhelmingly points to Siberian Traps flood basalt volcanism.",
      "sectionId": "cbonus",
      "chapterId": "chmix"
    },
    {
      "prompt": "A radioactive sample starts at 100% parent isotope. After 3 half-lives, what percentage of the original PARENT isotope remains?",
      "choices": [
        "25%",
        "12.5%",
        "6.25%",
        "37.5%",
        "50% — each half-life removes one-sixth of the total, so 3 half-lives = 50% removed"
      ],
      "answer": 1,
      "why": "**B.** After 1 half-life: 50%. After 2: 25%. After 3: 12.5%. Each half-life cuts the remaining parent by half. 100 → 50 → 25 → 12.5%. | **Wrong E:** Half-life decay is exponential, not linear subtraction; each half-life halves the REMAINING amount: 100% to 50% to 25% to 12.5% after three half-lives.",
      "sectionId": "cextra1",
      "chapterId": "chmix"
    },
    {
      "prompt": "Early Earth's atmosphere lacked oxygen. Why was this CRITICAL for the origin of life?",
      "choices": [
        "O2 is required for ATP synthesis, which powers early chemical reactions",
        "Oxygen provides the chemical energy needed to form amino acid bonds",
        "O2 is a strong oxidant that would break down organic molecules as fast as they formed — no O2 allowed organic molecules to accumulate in the prebiotic soup",
        "O2 absorbs UV radiation; without it, more radiation drove chemistry",
        "Without O&sub2, no ozone layer existed, so stronger UV radiation provided more energy for prebiotic synthesis"
      ],
      "answer": 2,
      "why": "**C.** Oxygen is a powerful oxidizing agent that destroys organic compounds. If early Earth had O2, organic molecules like amino acids would oxidize immediately. The ABSENCE of O2 was essential for organic molecules to accumulate in the prebiotic soup. (Option D has some truth about UV but misses the critical point about oxidation.) | **Wrong E:** While partly true, the CRITICAL reason the absence of O&sub2 mattered is that oxygen would have oxidized and destroyed organic molecules; UV as an energy source is a secondary factor.",
      "sectionId": "cextra1",
      "chapterId": "chmix"
    },
    {
      "prompt": "Arrange these events in correct chronological order (oldest first): eukaryotes, stromatolites, Great Oxidation Event, first animals",
      "choices": [
        "First animals → eukaryotes → stromatolites → Great Oxidation Event",
        "Stromatolites → Great Oxidation Event → first animals → eukaryotes",
        "Great Oxidation Event → stromatolites → eukaryotes → first animals",
        "Stromatolites (3.45 bya) → Great Oxidation Event (2.4 bya) → eukaryotes (1.8 bya) → first animals (650-635 mya)",
        "Great Oxidation Event → first animals → stromatolites → eukaryotes"
      ],
      "answer": 3,
      "why": "**D.** Stromatolites 3.45 bya → GOE 2.4 bya (cyanobacteria pumped O2) → eukaryotes 1.8 bya → first animals (sponges) 650-635 mya. The GOE was CAUSED by cyanobacteria (bacteria, not eukaryotes), and eukaryotes appeared AFTER the GOE (aerobic metabolism became possible). | **Wrong E:** This ordering is incorrect; stromatolites (3.45 bya) preceded the GOE (2.4 bya), and eukaryotes (1.8 bya) preceded animals (~635 mya).",
      "sectionId": "cextra1",
      "chapterId": "chmix"
    },
    {
      "prompt": "In a phylogenetic tree, taxon A is at the far left tip and taxon B is at the far right tip. Taxon C is in the middle. Based on this positional information alone, which is most closely related to B?",
      "choices": [
        "A, because it is farthest from B and therefore most different",
        "C, because it is closest to B in position on the page",
        "A, because it is next to C which is in the middle",
        "You CANNOT determine relatedness from tip position — you must trace back to the SHARED NODE to determine relatedness",
        "Taxon C is equally related to both A and B because it is equidistant from each on the page"
      ],
      "answer": 3,
      "why": "**D.** This is the most common phylogenetics reading error. Tip ORDER on a tree does NOT indicate relatedness. You must trace back to the most recent SHARED NODE. Rotating branches around a node doesn't change tree meaning. The position on page is arbitrary — the branching topology (which nodes are shared) is what matters. | **Wrong E:** Physical distance on a cladogram does not indicate evolutionary relatedness; you must trace shared nodes to determine which taxa share a more recent common ancestor.",
      "sectionId": "cextra1",
      "chapterId": "chmix"
    },
    {
      "prompt": "Early fish evolved lungs to gulp air from the surface, supplementing O2 in low-oxygen water. In many ray-finned fish lineages, this lung was later modified into a swim bladder for buoyancy. This is an example of:",
      "choices": [
        "Convergent evolution — fish and tetrapods independently evolved gas-filled structures",
        "Parallel evolution — both fish and tetrapods retained the same structure for the same purpose",
        "Exaptation — a structure that evolved for one function (breathing) was co-opted for a new function (buoyancy)",
        "Adaptive radiation — fish diversified into many niches using the swim bladder as a key innovation",
        "Homology — both the swim bladder and lungs perform the same respiratory function in their respective organisms"
      ],
      "answer": 2,
      "why": "**C.** Classic exaptation (from lecture). The lung evolved for BREATHING (original function). In many fish lineages, it was co-opted for BUOYANCY (new function). Original function ≠ current function = exaptation. Tetrapods retained lungs for breathing. This also illustrates that structures can diverge in function across lineages. | **Wrong E:** While the structures are homologous in origin, they perform DIFFERENT functions (buoyancy vs. breathing); this functional shift is what defines exaptation.",
      "sectionId": "cextra1",
      "chapterId": "chmix"
    },
    {
      "prompt": "How many generations does allopolyploid speciation require?",
      "choices": [
        "One — the allopolyploid organism is immediately reproductively isolated from both parent species in a single generation",
        "Hundreds to thousands, as postzygotic barriers gradually strengthen",
        "Tens of thousands, similar to allopatric speciation timescales",
        "It cannot be determined without knowing mutation rates in the hybrid lineage",
        "Millions of years — allopolyploidy requires the same slow accumulation of mutations as allopatric speciation"
      ],
      "answer": 0,
      "why": "**A.** Allopolyploidy = INSTANT SPECIATION. The doubled genome creates immediate reproductive isolation: when the allopolyploid tries to mate with either parent species, the ploidy mismatch (e.g., 4n × 2n = 3n offspring) causes meiotic failure. New species in ONE generation. This is one of the strongest arguments that speciation can be extremely rapid. | **Wrong E:** Allopolyploidy produces immediate reproductive isolation because the polyploid cannot produce viable gametes with either diploid parent; this is instantaneous speciation in one generation.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "Why is Rhagoletis pomonella considered an example of sympatric speciation IN PROGRESS (not completed)?",
      "choices": [
        "The flies are fully reproductively isolated — they never produce hybrids",
        "The apple and hawthorn populations are diverging genetically and reproductively isolating (host preference = mating isolation) but are not yet fully reproductively isolated — some interbreeding still occurs",
        "Geographic barriers have partially formed between apple orchards and hawthorn stands",
        "The populations are morphologically identical so species status cannot yet be assigned",
        "The apple and hawthorn populations have been diverging for over 1 million years based on molecular clock estimates"
      ],
      "answer": 1,
      "why": "**B.** Rhagoletis is a MODEL of speciation IN PROGRESS — not completed. The apple and hawthorn populations show: genetic divergence at several loci, different emergence timing (temporal isolation developing), and assortative mating (flies mate on their host plant). BUT some interbreeding still occurs. This makes it ideal for studying the early stages of speciation. | **Wrong E:** The apple-hawthorn divergence began only ~150 years ago when apples were introduced to North America; they are still in the early stages of speciation with some gene flow remaining.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "Hawaiian honeycreepers (>50 species) evolved from a single ancestor that colonized ~5 mya. This is BEST classified as:",
      "choices": [
        "Sympatric speciation — all species occur on the same islands",
        "Allopatric speciation by vicariance — geographic barriers formed between islands",
        "Adaptive radiation — one colonizing lineage rapidly diversified into many ecological roles in a new habitat with no prior competitors; geographic isolation between islands also contributed",
        "Reinforcement — the species evolved stronger reproductive isolation after secondary contact",
        "Parapatric speciation along elevational gradients within each Hawaiian island"
      ],
      "answer": 2,
      "why": "**C.** This is adaptive radiation triggered by: (1) colonization of a new habitat (Hawaii), (2) no prior competitors (ecological opportunity). Within the archipelago, allopatric speciation between islands also contributes. The key features of adaptive radiation are: single ancestor + rapid diversification + many ecological roles. Calling it purely allopatric misses the ecological opportunity driver. | **Wrong E:** While elevational gradients may contribute, the honeycreeper radiation is a textbook adaptive radiation driven by ecological opportunity, combining geographic isolation between islands with niche diversification.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which mass extinction actually BENEFITED the mammalian lineage by creating the conditions for their diversification?",
      "choices": [
        "End-Permian — wiped out reptile competitors allowing early mammal ancestors to evolve",
        "K-T (~66 mya) — eliminated non-avian dinosaurs that had monopolized ecological niches for ~160 million years, releasing mammals into vacant adaptive space",
        "End-Ordovician — reduced marine diversity allowing early vertebrates to diversify",
        "End-Triassic — allowed early dinosaurs to diversify, which later competed with mammals",
        "End-Devonian — eliminated large predatory fish, allowing early tetrapods and eventually mammals to diversify"
      ],
      "answer": 1,
      "why": "**B.** The K-T extinction was catastrophic for most groups but was the BEST thing that ever happened to mammals. For ~160 million years, dinosaurs monopolized large-body ecological niches. The asteroid killed them (and ~76% of other species). Within ~10 million years after, ALL major mammalian orders appeared — whales, bats, elephants, primates, etc. Extinction-triggered adaptive radiation. | **Wrong E:** The End-Devonian extinction did not directly benefit mammals, which did not exist until the Mesozoic; the K-T extinction at 66 mya directly opened niches for mammalian adaptive radiation.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "A city proposes replacing a large forest with 10 small isolated forest patches of equal total area. Island biogeography theory predicts this will:",
      "choices": [
        "Maintain the same species richness since total area is preserved",
        "Increase species richness because more habitat patches = more niches",
        "Decrease species richness — 10 small isolated patches have higher per-patch extinction rates and lower immigration rates between them than one large connected habitat",
        "Have no effect because species richness is determined by latitude, not habitat area",
        "Increase species richness because edge habitat between the 10 patches promotes biodiversity"
      ],
      "answer": 2,
      "why": "**C.** Island biogeography applied to conservation: habitat fragments = islands. Smaller patches = smaller populations = higher extinction rates per patch. Isolation = lower immigration rates between patches (can't rescue locally extinct species). One large contiguous habitat supports more species than the same area split into many small pieces. This is the SLOSS debate (Single Large Or Several Small) in conservation biology — theory strongly favors single large. | **Wrong E:** Increased edge habitat generally favors generalists and invasives while reducing interior habitat; island biogeography predicts fragmentation decreases overall species richness.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "A wolf pack has 40 animals total (census population N=40), but only 2 breeding pairs that successfully raise offspring each year. The effective population size (Ne) is approximately:",
      "choices": [
        "Much less than 40 — possibly as low as 8–16, because Ne is primarily determined by the number of breeding individuals, not total census population",
        "Exactly 40 — census population equals effective population size in a pack structure",
        "Greater than 40 — larger packs have greater genetic diversity due to cooperation",
        "20 — Ne is always half the census population in social animals",
        "Exactly 4 — Ne always equals the number of breeding pairs times two"
      ],
      "answer": 0,
      "why": "**A.** Ne is determined by the number of individuals that ACTUALLY CONTRIBUTE genetically to the next generation. With only 2 breeding pairs (4 breeders), Ne ≈ 4 × (4-1) = small, possibly 8-16 depending on how equal their reproductive success is. The 36 non-breeding wolves contribute nothing to the next generation's gene pool. Ne << N when reproductive success is highly unequal. This is why conservation policy targets Ne, not N. | **Wrong E:** While breeding individuals determine Ne, the calculation depends on sex ratio and variance in reproductive success; Ne for 2 breeding pairs is low but typically estimated higher than 4 using the harmonic mean formula.",
      "sectionId": "cextra2",
      "chapterId": "chmix"
    },
    {
      "prompt": "Atlantic cod in heavily fished populations now mature at smaller sizes and younger ages compared to unfished populations. A critic argues this is just phenotypic plasticity (fish get smaller because of less food). What evidence would BEST demonstrate this is GENETIC evolution?",
      "choices": [
        "The changes happened quickly — less than 50 years",
        "The fish look morphologically different from unfished populations",
        "When fished-population fish are raised in identical conditions to unfished fish (with the same food availability), fished-population fish still mature earlier and at smaller sizes — the trait persists independent of environment",
        "Fishing removes large fish, so obviously small fish increase by default",
        "Fished populations show higher genetic diversity than unfished populations, which proves the changes are evolutionary"
      ],
      "answer": 2,
      "why": "**C.** The definitive test: raise fish from both populations in identical, controlled environments. If the difference persists (fished fish still mature earlier/smaller despite same food), the trait is GENETIC, not a plastic response to food availability. This is the common garden experiment approach. Speed (A) and morphological differences (B) are consistent with either genetic or plastic changes. | **Wrong E:** Reduced population size from fishing typically DECREASES genetic diversity; the key evidence for heritable change is that trait differences persist when fish are raised in identical (common-garden) conditions.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Ardipithecus (~4.4–5.8 mya) was found in FOREST, not savannah environments. Why does this matter for understanding bipedalism?",
      "choices": [
        "It shows that forests were the origin of all human traits including large brains",
        "It confirms that hominins only lived in forests until the Devonian period",
        "It proves that bipedalism evolved because of tree-climbing, not walking",
        "It challenges the 'savannah hypothesis' — bipedalism may NOT have evolved as an adaptation to open grasslands, since early bipedal hominins lived in forested environments",
        "It proves Ardipithecus was an ancestral ape rather than a hominin, since true hominins only lived in savannahs"
      ],
      "answer": 3,
      "why": "**D.** The traditional explanation was that bipedalism evolved for open grassland/savannah locomotion. Ardipithecus being a FOREST biped challenges this narrative. Bipedalism apparently predated open savannah habitats. This means the savannah hypothesis (freeing hands for tools in open grassland, or heat regulation in the sun) cannot be the original driver. The HOW and WHY of bipedalism origins is still actively debated. | **Wrong E:** Ardipithecus is classified as a hominin based on derived bipedal features; its forest habitat challenges the savannah hypothesis but does not remove it from the hominin clade.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is NOT a characteristic that distinguishes anatomically modern H. sapiens from archaic hominins like H. erectus?",
      "choices": [
        "High domed skull with reduced brow ridges",
        "Creation of sophisticated art and personal ornaments",
        "Chin (a projection of the lower mandible unique to H. sapiens)",
        "Smaller face and teeth relative to brain size",
        "Obligate bipedalism with a valgus (angled) knee for efficient upright walking"
      ],
      "answer": 1,
      "why": "**B.** Art and personal ornaments are characteristics of BEHAVIORALLY modern H. sapiens (~70–100 kya), not just anatomically modern ones (~195 kya). Anatomically modern = skeletal features (A, C, D). The gap between anatomical modernity and behavioral modernity is ~100,000+ years. You can be anatomically modern but pre-behaviorally-modern. | **Wrong E:** Obligate bipedalism is an ANATOMICAL skeletal trait, not a behavioral one; the question asks for what is NOT an anatomically modern trait, and sophisticated art/ornaments (B) is behavioral.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Some doctors advocate routinely suppressing fever with antipyretics (fever-reducing drugs). Evolutionary medicine's perspective on this practice would be:",
      "choices": [
        "Correct — fever is always harmful and should be reduced immediately",
        "Irrelevant — fever is a purely mechanical response with no evolved function",
        "Potentially counterproductive — fever may be an ADAPTATION (the body intentionally raising temperature to slow pathogen replication). Suppressing it may worsen infection outcomes. The cost-benefit should be evaluated case by case.",
        "Wrong — pathogens actually grow faster at higher temperatures so fever always makes infections worse",
        "Fever is a purely mechanical byproduct of inflammation with no adaptive function independent of the immune response"
      ],
      "answer": 2,
      "why": "**C.** This is Nesse's Reason #6: apparent disease may be adaptation. Fever raises body temperature, which: slows bacterial/viral replication (many pathogens are optimized for normal body temp), activates immune cells, and stimulates antibody production. Studies show that suppressing fever can prolong some infections. Evolutionary medicine doesn't say 'never treat fever' — it says evaluate whether the symptom is a defense before automatically suppressing it. | **Wrong E:** Evidence shows fever is actively regulated by the hypothalamus at significant metabolic cost, suggesting it is an adaptation that enhances immune function, not merely a passive byproduct.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "A patient with HIV is treated with a single antiretroviral drug. After 6 months the drug becomes ineffective. By analogy with antibiotic resistance, what MOST LIKELY happened?",
      "choices": [
        "HIV mutated in response to the drug and developed resistance specifically against it",
        "Within the diverse HIV population inside the patient, pre-existing drug-resistant variants were selected for as the drug killed susceptible viruses — the resistant lineage expanded",
        "The patient's immune system failed to combat the viral variants created by the drug",
        "The drug gradually lost its effectiveness due to chemical degradation in the patient's body",
        "The patient's T-cells co-evolved resistance to HIV, forcing the virus to counter-evolve resistance to the drug"
      ],
      "answer": 1,
      "why": "**B.** HIV generates ~1 billion descendants per day with a high mutation rate (no repair enzymes). A diverse viral population already exists when treatment starts. The drug kills the susceptible majority, but pre-existing resistant variants (already present at low frequency) now have a massive competitive advantage. They expand. Same mechanism as antibiotic resistance. This is why combination therapy (multiple drugs simultaneously) is used — much harder for a single viral strain to have pre-existing resistance to 3+ drugs simultaneously. | **Wrong E:** T-cells do not evolve resistance to HIV in the evolutionary sense; HIV drug resistance arises from natural selection acting on pre-existing genetic variation within the viral population.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is BEST explained as an evolutionary mismatch disease (not antagonistic pleiotropy or genetic constraint)?",
      "choices": [
        "Lower back pain due to the human spine being retrofitted for bipedalism (originally evolved for quadrupeds)",
        "Prostate cancer risk from testosterone that also provides early reproductive benefits",
        "Hybrid sterility in mules due to chromosomal incompatibility",
        "Type 2 diabetes in populations that have recently shifted from traditional diets to high-calorie processed foods — fat storage genes evolved for feast/famine are now maladaptive in constant-feast environments",
        "Sickle cell disease in malaria-endemic regions, maintained by heterozygote advantage (balancing selection)"
      ],
      "answer": 3,
      "why": "**D.** D is the clearest evolutionary mismatch: the evolved trait (efficient fat storage for feast/famine cycles) is now maladaptive in the modern constant-feast environment. A is evolutionary CONSTRAINT (Reason 4 — can't redesign spine from scratch). B is ANTAGONISTIC PLEIOTROPY (Reason 5 — early benefit + late cost). C is not a human disease example at all. Mismatch = evolved for environment X, now living in environment Y. | **Wrong E:** Sickle cell is maintained by balancing selection (heterozygote advantage), which is a different evolutionary mechanism from mismatch; Type 2 diabetes is the mismatch example because ancestral fat-storage genes are maladaptive in modern calorie-rich environments.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which of the following is NOT one of Nesse's (2005) six evolutionary reasons why humans remain vulnerable to disease?",
      "choices": [
        "Pathogens evolve faster than their hosts, staying ahead of immune defenses",
        "What appears to be disease is actually an adaptation (fever, nausea)",
        "Natural selection always optimizes both reproductive fitness AND individual health simultaneously",
        "Evolutionary history constrains solutions — selection tinkers with existing structures, can't redesign from scratch",
        "Random genetic drift is the primary cause of most human diseases, with natural selection playing no role"
      ],
      "answer": 2,
      "why": "**C.** C is the WRONG one — it contradicts the entire premise of evolutionary medicine. Natural selection optimizes REPRODUCTIVE FITNESS, not health. Health and longevity are only selected for to the extent they increase fitness. Selection can maintain alleles that harm health if they increase reproduction (antagonistic pleiotropy). The other options (A, B, D) are all genuine Nesse reasons. The 6th reason not shown is: selection lags behind environmental change (mismatch). | **Wrong E:** While drift can influence disease allele frequencies, Nesse's framework identifies six specific evolutionary reasons for disease vulnerability; the false claim is that selection simultaneously optimizes both health and reproduction.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Cystic fibrosis (CF) alleles persist at ~4% frequency in European populations — higher than expected from mutation alone. The BEST evolutionary explanation is:",
      "choices": [
        "CF alleles are neutral and maintained by genetic drift",
        "CF heterozygote advantage — one copy of the CF allele may protect against cholera/typhoid by reducing CFTR function (the receptor cholera toxin uses to cause deadly diarrhea), giving carriers higher fitness during epidemics",
        "CF alleles are linked to immune system genes that provide protection against viral infections",
        "High mutation rates in European populations continuously regenerate CF alleles",
        "The CF allele provides protection against tuberculosis by thickening airway mucus to trap mycobacteria more effectively"
      ],
      "answer": 1,
      "why": "**B.** Same logic as sickle cell heterozygote advantage. CF homozygotes (two copies) have severe lung/digestive disease. But ONE copy may reduce CFTR function just enough that cholera toxin causes less deadly diarrhea — carriers had higher survival during cholera/typhoid epidemics that historically ravaged Europe. The 4% frequency is too high for mutation alone to maintain. Heterozygote advantage (balancing selection) is the most parsimonious explanation. | **Wrong E:** The proposed CF heterozygote advantage involves resistance to cholera/typhoid through reduced CFTR chloride secretion, not tuberculosis resistance through mucus thickening.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two bird species have: different habitat preferences (marshes vs. forest), mate attraction songs that species only respond to their own, and any hybrid offspring have abnormal development and die as nestlings. How many TYPES of reproductive barriers are present?",
      "choices": [
        "One — only hybrid inviability (postzygotic) is a true barrier since the others could break down",
        "Two — habitat isolation and hybrid inviability",
        "Two — behavioral isolation and hybrid inviability",
        "Three — habitat isolation (prezygotic, pre-mating) + behavioral/acoustic isolation (prezygotic, pre-mating) + hybrid inviability (postzygotic)",
        "Four barriers — habitat, behavioral, and hybrid inviability plus the geographic distance between their preferred habitats"
      ],
      "answer": 3,
      "why": "**D.** Multiple reproductive barriers can and often do reinforce each other. Here we have: (1) HABITAT isolation — different microhabitats mean populations rarely encounter each other (prezygotic, pre-mating); (2) BEHAVIORAL isolation — species-specific songs prevent mating even if individuals meet (prezygotic, pre-mating); (3) HYBRID INVIABILITY — the rare hybrids that form die as nestlings (postzygotic). All three act as sequential filters. This is actually the norm for well-established species — they have multiple layers of isolation. | **Wrong E:** Geographic distance between habitats is not a separate barrier in this scenario (the species coexist in the same area); the three barriers are habitat isolation, behavioral isolation, and hybrid inviability.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "The human coccyx (tailbone) anchors muscles used for upright posture, while in other primates it is part of a functional tail. Darwin used this as evidence for common ancestry. This is an example of:",
      "choices": [
        "A vestigial structure that is homologous to primate tails — shares the same evolutionary origin but has changed function",
        "Convergent evolution — humans and primates independently evolved similar posterior bones",
        "An exaptation where a locomotion structure was co-opted for posture",
        "Horizontal gene transfer of structural genes between humans and other primates",
        "An analogous structure — the coccyx evolved independently in humans for postural support, unrelated to primate tails"
      ],
      "answer": 0,
      "why": "**A.** The coccyx is a vestigial structure: it retains its homology to primate tails (same bones, same developmental origin, same genetic basis) but is greatly reduced in size and has changed function (from tail movement to posture muscle attachment). It is evidence of common ancestry because the most parsimonious explanation for sharing this structure is descent from a common tailed ancestor. Darwin used it explicitly in Descent of Man (1871). | **Wrong E:** The coccyx is homologous to primate tails (same embryological origin, same caudal vertebrae); calling it analogous would mean independent evolution, which contradicts the shared developmental evidence.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Which type of similarity is LEAST reliable as evidence for inferring phylogenetic relationships?",
      "choices": [
        "Shared derived characters (synapomorphies) that evolved in the ancestor of a specific clade",
        "Analogous structures that provide the same function but evolved independently in unrelated lineages (homoplasy)",
        "DNA sequence similarities in highly conserved gene regions",
        "Shared developmental pathways involving homologous regulatory genes",
        "Shared ancestral characters (symplesiomorphies) retained unchanged from a distant common ancestor"
      ],
      "answer": 1,
      "why": "**B.** Analogous structures (homoplasy) are the LEAST reliable for phylogenetics because they arise from convergent evolution — independent evolution in unrelated lineages due to similar selective pressures. Using them as evidence for relationship gives false groupings. Synapomorphies (A), molecular data (C), and developmental homologies (D) all reflect shared ancestry and are reliable. Cladistics specifically excludes analogous traits and focuses only on synapomorphies. | **Wrong E:** Symplesiomorphies are shared ancestral traits that are uninformative for grouping taxa into specific derived clades; analogous structures from convergent evolution (B) are even more misleading for phylogenetics.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two populations of oak trees produce fertile hybrids in the narrow zone where their ranges overlap. However, morphologists classify them as separate species based on leaf shape differences. Which statement BEST represents the situation?",
      "choices": [
        "They are definitely the same species — fertile hybrids prove gene flow is occurring",
        "They are definitely different species — morphological differences always define species boundaries",
        "Different species concepts give different answers: BSC might consider them one species (gene flow occurring); morphospecies treats them as different. No single concept is always correct — context matters.",
        "They cannot be classified until their full genome is sequenced",
        "They are ring species — populations forming a geographic ring where the terminal populations cannot interbreed"
      ],
      "answer": 2,
      "why": "**C.** Oaks are famous for hybridizing across apparent species boundaries — a classic problem for species concepts. BSC: fertile hybrids = some gene flow = possibly one species. Morphospecies: different enough morphologically = different species. The general lineage concept might consider them different if the bulk of each population is evolving independently despite rare hybridization. This illustrates WHY no single species concept works universally — hybridizing plants regularly break BSC assumptions. | **Wrong E:** Ring species involve a continuous geographic chain of interbreeding populations; the oak scenario describes two morphologically distinct populations with a hybrid zone, interpreted differently by BSC and morphospecies concepts.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Two islands have the same equilibrium species number (50 species each). Island A is far from the mainland; Island B is close. At equilibrium, which island has higher species turnover?",
      "choices": [
        "Island A — remote islands have more unique species that turn over more rapidly",
        "Island B — closer island has higher immigration rate, and to maintain the same equilibrium number, must also have higher extinction rate; turnover (originations+extinctions) is higher",
        "Both islands have the same turnover because they have the same species number",
        "Turnover is determined by island size, not distance from mainland",
        "Island A — remote islands accumulate more endemic species that turn over faster due to their evolutionary uniqueness"
      ],
      "answer": 1,
      "why": "**B.** Key MacArthur-Wilson insight: equilibrium species number is the same, but the RATES can differ. Island B (close) has a HIGH immigration rate. To reach the same equilibrium, it must also have a high extinction rate (more colonizers arriving = more competition = more local extinctions). Higher immigration + higher extinction = HIGHER TURNOVER at the same equilibrium number. Island A has LOW immigration and LOW extinction = same number but lower turnover. Species identity changes faster on B. | **Wrong E:** Endemism does not increase turnover rate; turnover is the rate of species replacement, and closer islands (B) have higher immigration and extinction rates, yielding higher turnover at the same equilibrium number.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "A population of bacteria is treated with antibiotic X for one week. Resistance evolves. The bacteria are then treated with a COMBINATION of antibiotics X+Y simultaneously. Why is combination therapy much harder for bacteria to overcome?",
      "choices": [
        "Combination therapy prevents bacteria from mutating by blocking DNA replication",
        "Two antibiotics attack the same pathway simultaneously, making resistance impossible",
        "Bacteria do not develop resistance to multiple drugs because they can only mutate one gene at a time",
        "Pre-existing resistance mutations to X and Y must occur simultaneously in the same cell to survive — the probability of a single cell having pre-existing mutations to BOTH drugs is extremely low (product rule of probability)",
        "Two antibiotics together reduce the bacterial population below the minimum size needed for any new mutation to occur"
      ],
      "answer": 3,
      "why": "**D.** This is evolutionary logic applied to medicine. Single-drug resistance: the bacterial population already contains some cells with pre-existing resistance to drug X (frequent mutation). Combination therapy: a cell needs SIMULTANEOUS pre-existing resistance to BOTH X and Y. If resistance frequency to X is 10⁻⁶ and to Y is 10⁻⁶, the probability of one cell having both is ~10⁻¹² — vanishingly rare in a normal infection. This is why HIV triple therapy revolutionized AIDS treatment and why TB treatment uses 4+ drugs. | **Wrong E:** Mutations occur regardless of population size (they are random errors during replication); the key is that simultaneously carrying resistance to BOTH drugs is the product of two independent low probabilities, making it extremely unlikely.",
      "sectionId": "cextra3",
      "chapterId": "chmix"
    },
    {
      "prompt": "Because evolution is a theory, that means:",
      "choices": [
        "It is a guess or a hunch.",
        "It has very little evidence to support it.",
        "Scientists may or may not believe in it.",
        "It has never been observed.",
        "None of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 1:** Like Einstein's General Theory of Relativity, evolutionary theory is a set of overarching mechanisms and principles backed by decades of evidence, examination, experimentation, and testing. A scientific theory is not a 'guess.' Evolution has been directly observed in lab and nature, and its evidence spans geology, genetics, geography, and more. Incorrect options: (A) 'Theory' colloquially means 'guess,' but to scientists it carries weight. (B) There is abundant evidence, from Darwin to the Modern Synthesis. (C) Science is not about 'belief'; it follows evidence. (D) Evolution HAS been observed directly in lab and field.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Why is understanding evolution important?",
      "choices": [
        "Understanding evolution can help us understand biodiversity issues associated with deforestation and global warming.",
        "Understanding evolution can help us understand the evolution of antibiotic resistance and cancer.",
        "Understanding evolution can help us understand our own genetic makeup and how it affects our lives.",
        "All of the above"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 1:** A, B, and C are each individually correct; D (All of the above) is the best overall answer. Understanding evolution informs biodiversity/extinction threats, antibiotic resistance and cancer, and the evolution of our own genome.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Which of the following statements about evolution is true?",
      "choices": [
        "Once biologists find all the missing links, they will be able to understand evolution.",
        "Evolution is a process that leads to more and more complex organisms.",
        "Evolution is entirely random.",
        "Some forms of life are higher on the ladder than other forms of life.",
        "None of the above is a true statement."
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 1:** None is true. The fossil record is always incomplete yet evolution is well supported by many lines of evidence. Evolution does not require increasing complexity; mutations are random but selection is not; life is a branched bush, not a ladder. (A) 'Missing links' is a misnomer; key transitional fossils (e.g., Tiktaalik) exist. (B) Complexity may increase OR decrease. (C) Selection and other non-random forces shape evolution (note convergence of whales and fishes). (D) Every organism has adaptations; humans are not the 'top' of any ladder.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Match the term to its correct definition from the list of choices. TERM: Biological evolution",
      "choices": [
        "Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
        "A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
        "Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
        "Any change to the genomic sequence of an organism",
        "Characteristics that are similar in two or more species because they are inherited from a common ancestor"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 1:** Biological evolution = Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Match the term to its correct definition from the list of choices. TERM: Homologous traits",
      "choices": [
        "Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
        "A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
        "Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
        "Any change to the genomic sequence of an organism",
        "Characteristics that are similar in two or more species because they are inherited from a common ancestor"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 1:** Homologous traits = Characteristics that are similar in two or more species because they are inherited from a common ancestor",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Match the term to its correct definition from the list of choices. TERM: Mutation",
      "choices": [
        "Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
        "A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
        "Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
        "Any change to the genomic sequence of an organism",
        "Characteristics that are similar in two or more species because they are inherited from a common ancestor"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 1:** Mutation = Any change to the genomic sequence of an organism",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Match the term to its correct definition from the list of choices. TERM: Natural selection",
      "choices": [
        "Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
        "A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
        "Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
        "Any change to the genomic sequence of an organism",
        "Characteristics that are similar in two or more species because they are inherited from a common ancestor"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 1:** Natural selection = A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Match the term to its correct definition from the list of choices. TERM: Viral reassortment",
      "choices": [
        "Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
        "A mechanism that can lead to evolution, whereby differential survival and reproduction of individuals cause some of them to survive and reproduce more effectively than others",
        "Any change in the inherited traits of a population that occurs from one generation to the next (i.e., over a time period longer than the lifetime of an individual in the population)",
        "Any change to the genomic sequence of an organism",
        "Characteristics that are similar in two or more species because they are inherited from a common ancestor"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 1:** Viral reassortment = Occurs when genetic material from different strains gets mixed into new combinations within a single individual",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Which of the following is a true statement?",
      "choices": [
        "Mutations always cause the improvement of a trait.",
        "Having bigger brains gave both advantages and disadvantages to human ancestors.",
        "The ancestors to whales needed more food than could be found on land, so they evolved features that allowed them to survive in the water.",
        "Natural selection always favors viruses that infect only the weakest individuals in a population."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 1:** Adaptations are often trade-offs. Larger brains offered cognitive advantages (tool use, language) but also costs (higher metabolic demand, risky childbirth). (A) Wrong - most mutations are neutral or harmful. (C) Wrong - evolution does not operate by 'need.' (D) Wrong - natural selection favors variants that maximize transmission, not only those targeting the weakest.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Whales are most closely related to which group of animals?",
      "choices": [
        "Camels",
        "Fish",
        "Seals",
        "They are equally related to all of the above."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 1:** Whales are cetaceans, nested within Artiodactyla (even-toed ungulates). Their closest living relatives are hippos, with other artiodactyls like camels more closely related to whales than are fish (superficial convergence only) or seals (pinniped carnivorans).",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "According to Figure 1.8, which shared derived character (synapomorphy) links modern whales and the fossil whale Indohyus?",
      "choices": [
        "A nasal opening that is shifted backwards",
        "A large powerful tail",
        "The presence of an involucrum",
        "All of the above",
        "None of the above"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 1:** The involucrum is a thickened medial lip of the ear bone (tympanic bulla) found only in cetaceans and their fossil relatives, including Indohyus - a defining cetacean synapomorphy.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Which trait would you consider the most important in determining whether a fossil should be considered a cetacean or not?",
      "choices": [
        "The teeth, because modern whales have peg-like teeth but Dorudon, one of the earliest cetacean fossils completely adapted to life in the water, had diverse teeth",
        "The involucrum, because it has a unique form in cetaceans not found in other mammals",
        "The astragalus, because if cetaceans evolved from artiodactyls, then early cetaceans should have double-pulley astragali",
        "The presence of flippers, because the earliest whale fossils had flippers much like those of modern whales",
        "The absence of legs, because cetaceans do not have legs"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 1:** The involucrum is unique to cetaceans among mammals, making it the most diagnostic trait for identifying a fossil as a cetacean. Teeth, astragali, flippers, and leg presence are either variable within cetaceans or found in other mammals.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "What characters of Dorudon are similar to modern whales?",
      "choices": [
        "Presence of flippers",
        "A long vertebral column",
        "The shape of the involucrum",
        "All of the above are characters shared by Dorudon and modern whales.",
        "None of the above is a character shared by Dorudon and modern whales."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 1:** Dorudon, a late Eocene cetacean fully adapted to aquatic life, shares flippers, an elongated vertebral column, and the cetacean-type involucrum with modern whales.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Why was finding the fossils of Pakicetus so important in understanding whale evolution?",
      "choices": [
        "Because the fossils made the researchers famous",
        "Because Pakicetus shared many whale traits, but it lived on land",
        "Because Pakicetus was not really a whale because it lived on land",
        "Because the fossils weren't old enough to be considered the common ancestor of whales"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 1:** Pakicetus shared diagnostic whale traits (including the involucrum) yet was clearly terrestrial, providing crucial transitional evidence that whales evolved from land-dwelling ancestors.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "Which is more important to the evolution of viruses, mutations or rapid reproductive potential?",
      "choices": [
        "Mutations, because they are harmful to viruses and reduce reproductive potential",
        "Mutations, because all mutations benefit the virus",
        "Both, because mutations add variation on which natural selection can act through reproductive potential",
        "Rapid reproductive potential, because viruses that reproduce more rapidly can spread more rapidly",
        "Neither, because the ability to invade a host cell is the most important factor affecting virus evolution"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 1:** Mutations supply the variation on which selection can act, and rapid reproduction both amplifies mutations and spreads favorable variants. Both processes work together to drive viral evolution; neither is sufficient alone.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "What mechanism do scientists suggest led to the appearance of the H7N9 flu virus?",
      "choices": [
        "Eating chicken",
        "Reassortment",
        "Natural selection",
        "The evolution of hemagglutinin",
        "None of the above"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 1:** H7N9 arose via reassortment, in which gene segments from different avian influenza strains combined inside a co-infected host to produce a novel strain capable of infecting humans.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "What do scientists understand about the evolutionary history of H7N9 and other emerging viruses?",
      "choices": [
        "That through reassortment, a variety of different strains can combine to produce one deadly virus strain",
        "That even within a host, strains resulting from reassortment continue to evolve",
        "That a single mutation to a virus strain may lead to a highly infectious virus",
        "That a virus strain can circulate among some animal hosts for years before a mutation allows it to jump to humans",
        "All of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 1:** All of A-D are true. Reassortment combines strains; within-host evolution continues after infection; single mutations can dramatically change infectivity; and viruses can circulate in animal reservoirs for years before a mutation enables host jumping.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "What is genetic drift?",
      "choices": [
        "A random process that changes the genetic composition of a population from one generation to the next",
        "An unimportant process in evolutionary biology",
        "A random change in amino acid sequences",
        "A random process that gives rise to genetic variation within a population from one generation to the next",
        "A statistical anomaly that results when gene frequencies change over time"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 1:** Genetic drift is a random process that changes allele/gene frequencies in a population from generation to generation. It does not create variation (mutation does that) and it is a genuine evolutionary force, particularly in small populations.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch01"
    },
    {
      "prompt": "How would you define biological evolution?",
      "choices": [
        "A gradual process in which something changes into a different and usually more complex or better form",
        "Any change in the frequency of heritable traits within a population from one generation to the next",
        "A process of slow, progressive change",
        "Any kind of change over time",
        "A theory that humans have their origin in other types of animals, such as apes, and that the distinguishable differences between humans and apes are due to modifications in successive generations"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 2:** Chapter 1 introduces the concept of biological evolution and its effects on organisms as small as viruses and as big as blue whales. Why the other options are incorrect: A) Incorrect. Evolution does not have a purpose; it does not necessarily move from simple to complex or from worse to better forms. Misconceptions about what evolution is or how it acts are pretty common, so each chapter of the study guide includes an Overcoming Misconceptions section designed to help you understand evolutionary theory. C) Incorrect. Biological evolution is not necessarily slow, let alone progressive. Evolution can occur quite rapidly (within months in viruses and other short-lived organisms; see Section 1.2), and it does not have a purpose. D) Incorrect. Change over time does not necessarily reflect the heritable changes that are necessary for biological evolution. A whale can grow and develop, changing over time from a small, young calf to a large adult, but this change occurs within an individual's lifespan. Biological evolution is the change in the frequency of heritable traits within a population from one generation to the next. E) Incorrect. Biological evolution certainly can explain the historical relationship between humans and apes, but that is not its only implication. Biological evolution affects every living organism. In Dobzhansky's essay \"Nothing in Biology Makes Sense Except in the Light of Evolution\" (1973), he emphasized the important role evolution plays in understanding everything from fossils to the diversity of life.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Why are mutations important in evolution?",
      "choices": [
        "Because mutations are always deleterious, and organisms with these deleterious mutations do not survive and reproduce",
        "Because mutations only occur in viruses",
        "Because mutations are random, and evolution is a random process",
        "Because mutations create the variation among individuals on which other mechanisms of evolution can act"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 2:** Mutations affect the genetic sequences that generate an organism's phenotype. So, even when the effect on the phenotype may not be readily apparent to evolutionary biologists, mutations can lead to genetic variation among phenotypes—the raw material for evolution through both natural selection and genetic drift (see Chapter 1). Why the other options are incorrect: A) Incorrect. Mutations can often be deleterious, but they can also be beneficial, or even neutral. Mutations provide the variation among individuals on which the mechanisms of evolution can act. Beneficial mutations may lead to greater survival or reproduction through their effects on the characteristics, or phenotype, of an organism. B) Incorrect. Mutations can occur in any organisms during the process of DNA (or RNA) replication or when these molecules are damaged. Because viruses reproduce at such a rapid rate, lineages can evolve rapidly, and this evolution can be observed both in natural settings (e.g., with flu viruses) and in the lab. C) Incorrect. Mutations are random, but evolution is not necessarily a random process. In fact, natural selection is decidedly not random. Natural selection acts on mutations that affect the success or failure of the individual—those individuals with mutations that increase survival or reproduction will do better. This non-randomness is clear in adaptations that have converged on the same form, such as the streamlined shape of whales and fishes.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Match the term \"Adaptations\" to its definition from the list below.",
      "choices": [
        "Groups of organisms that a taxonomist judges to be cohesive units, such as species or orders",
        "An overarching set of mechanisms or principles that explain a major aspect of the natural world",
        "Inherited aspects of an individual that allow it to outcompete other members of a population that lack the trait (or that have a slightly different version of the trait). They are traits that have evolved through the mechanism of natural selection",
        "The study of prehistoric life",
        "The permanent loss of a species. It is marked by the death or failure to breed of the last individual"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 2:** Adaptations are inherited aspects of an individual that allow it to outcompete other members of a population that lack the trait (or that have a slightly different version of the trait). They are traits that have evolved through the mechanism of natural selection.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Match the term \"Extinction\" to its definition from the list below.",
      "choices": [
        "Groups of organisms that a taxonomist judges to be cohesive units, such as species or orders",
        "An overarching set of mechanisms or principles that explain a major aspect of the natural world",
        "Inherited aspects of an individual that allow it to outcompete other members of a population",
        "The study of prehistoric life",
        "The permanent loss of a species. It is marked by the death or failure to breed of the last individual"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 2:** Extinction is the permanent loss of a species. It is marked by the death or failure to breed of the last individual.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Match the term \"Paleontology\" to its definition from the list below.",
      "choices": [
        "Groups of organisms that a taxonomist judges to be cohesive units",
        "An overarching set of mechanisms or principles that explain a major aspect of the natural world",
        "Inherited aspects of an individual that allow it to outcompete other members of a population",
        "The study of prehistoric life",
        "The permanent loss of a species"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 2:** Paleontology is the study of prehistoric life.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Match the term \"Theory\" to its definition from the list below.",
      "choices": [
        "Groups of organisms that a taxonomist judges to be cohesive units",
        "An overarching set of mechanisms or principles that explain a major aspect of the natural world",
        "Inherited aspects of an individual that allow it to outcompete other members of a population",
        "The study of prehistoric life",
        "The permanent loss of a species"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 2:** A theory is an overarching set of mechanisms or principles that explain a major aspect of the natural world.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Match the term \"Taxa (singular, taxon)\" to its definition from the list below.",
      "choices": [
        "Groups of organisms that a taxonomist judges to be cohesive units, such as species or orders",
        "An overarching set of mechanisms or principles that explain a major aspect of the natural world",
        "Inherited aspects of an individual that allow it to outcompete other members of a population",
        "The study of prehistoric life",
        "The permanent loss of a species"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 2:** Taxa (singular, taxon) are groups of organisms that a taxonomist judges to be cohesive units, such as species or orders.",
      "chapterId": "ch_s_hist",
      "sectionId": "ch_s_hist",
      "source": "textbook",
      "textbookRef": "ch02"
    },
    {
      "prompt": "Why is the study of stratigraphy important to understanding evolutionary theory?",
      "choices": [
        "Because stratigraphy provides evidence for the relative age of fossils",
        "Because Nicolaus Steno recognized that rocks occurred in layers even though he didn't believe in evolution",
        "Because stratigraphy characterizes the process of fossilization",
        "All of the above",
        "None of the above"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 3:** Stratigraphy is the study of layering in rock (stratification) as a method for reconstructing the past. It was first developed by Nicolaus Steno in the mid-1600s, before the development of evolutionary theory. Stratigraphy was instrumental in helping scientists examine change over time (see Chapter 2).",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "What was Georges Cuvier's contribution to evolutionary theory?",
      "choices": [
        "He strongly objected to Jean-Baptiste Lamarck's ideas about life evolving from simple to complex, drumming Lamarck out of the scientific establishment.",
        "He invented paleontology.",
        "He recognized that some fossils were both similar to and distinct from living species, and many fossil animals no longer existed.",
        "He was the first to organize and map strata according to a geological history.",
        "He rejected the idea that species evolved, instead believing that life's history was a series of appearances and extinctions of species."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 3:** Cuvier studied the fossil remains of elephants and compared them to living elephants. He discovered that some characters of the fossils, such as the shapes of teeth, were distinct from living elephants, and provided some of the first compelling evidence for extinction (see Chapter 2).",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "What is a scientific theory?",
      "choices": [
        "A belief that scientists try to prove as fact",
        "A set of laws that define the natural world",
        "A set of mechanisms or principles that explain a major aspect of the natural world",
        "A guess based on a few facts that scientists try to prove as correct",
        "An educated guess based on some experience that allows scientists to test evidence"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 3:** A scientific theory is different from the word theory used in everyday language. Scientific theories are not just guesses; they are overarching sets of mechanisms or principles that explain and provide testable predictions. Darwin contributed the first overarching set of mechanisms for the theory of evolution as natural selection and sexual selection (see Section 2.3).",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Which of the following is a true statement?",
      "choices": [
        "Scientists debate about the Earth's age.",
        "Scientific tools that only give results as a range of numbers are not valuable tools.",
        "Scientists use independent lines of evidence to validate results.",
        "When aging rocks, scientists use isotopes that will give them the results they think are best."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 3:** Scientists use independent lines of evidence to validate results. Radiometric dates are not only supported by volumes of consistent results from multiple isotope systems, they have been validated with independent lines of evidence such as tree rings and varved sediments.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Why was Lord Kelvin's estimate for the age of the Earth inaccurate?",
      "choices": [
        "Because he failed to account for plate tectonics and how that might affect heat flow",
        "Because he could not directly measure the age of any rock",
        "Because he used a model to generate a prediction for the age of the Earth",
        "Because he was trying to prove that evolution by natural selection could not occur",
        "Because he could not estimate cooling of rocks found deeper than in mines"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 3:** Kelvin modeled Earth's cooling as a simple conductive process from an initially molten state. He did not know about radioactive decay (a continuous internal heat source) or plate tectonics (which convectively transports heat from the mantle to the surface). These unaccounted mechanisms caused his estimate of ~20–100 million years to be far too young.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Why can't scientists hope to find conventional fossils from very early in Earth's history?",
      "choices": [
        "Because plate tectonics have destroyed almost all of the planet's original surface",
        "Because most fossils from that period are tiny zircons that do not have body forms",
        "Because the process of fossilization has changed over the course of Earth's history",
        "All of the above",
        "None of the above"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 3:** Most of Earth's original crust has been recycled by plate tectonics — subducted, remelted, or metamorphosed — destroying any fossils it may have contained. This is why the earliest evidence of life comes from biomarkers and isotopic signatures, not conventional body fossils.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Which of the following molecules has NOT been used as a biomarker, an organic chemical signature of once living organisms?",
      "choices": [
        "Carbon isotopes",
        "Oxygen isotopes",
        "Sodium ions",
        "Cellular pigments",
        "All of the above have been used as organic chemical signatures."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 3:** Biomarkers are organic molecules or stable-isotope signatures left by once-living organisms. Carbon and oxygen isotope ratios, lipids, and cellular pigments (such as degradation products of chlorophyll) are all used. Sodium ions are simple inorganic ions with no unique biological origin, so they are not used as biomarkers.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "How confident are scientists about the discoveries related to the earliest signs of life on Earth?",
      "choices": [
        "Very confident. Two scientists found organic carbon produced by photosynthetic bacteria, so now all scientists accept the 3.7-billion-year-old carbon as the earliest sign of life.",
        "Fairly confident. Stromatolite formation is a process observable today, and scientists have discovered stromatolite fossils that are 3.45 billion years old.",
        "Not very confident. Scientists all have different opinions about the oldest signs of life on Earth.",
        "Not confident. Scientists constantly have to test new techniques, so they can't be sure until they find an identifiable fossil.",
        "It's all just a guess."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 3:** Stromatolites — layered structures produced by microbial mats — form by an observable modern process, giving scientists a clear analog. Fossil stromatolites dated to ~3.45 billion years ago are generally accepted as evidence of early microbial life. Older claims (e.g., 3.7-billion-year-old biogenic carbon) remain under debate.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Which of the following statements about the history of life is TRUE?",
      "choices": [
        "Because cyanobacteria, the lineage of bacteria that carries out photosynthesis, have not changed in 2.6 billion years, evolution must not be occurring.",
        "Scientists have not found any fossils from before the Cambrian period, 542 million years ago.",
        "Because scientists have not been able to resolve many of the relationships among the three domains of life, they cannot know anything about the early history of life.",
        "Living bacteria can offer clues about how the first multicellular animals evolved.",
        "None of the above is a true statement."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 3:** Living bacteria — including colony-forming and biofilm-producing species — can illuminate evolutionary transitions to multicellularity, since many of the genetic and behavioral building blocks for multicellular cooperation are present in modern prokaryotes. The other options are factually wrong (pre-Cambrian fossils exist, morphological stasis in cyanobacteria does not disprove evolution, and domain-level uncertainty does not erase what we know of early life).",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Which fossils often took the form of disks, fronds, or blobs?",
      "choices": [
        "Prokaryotes",
        "Cambrian",
        "Stromatolites",
        "Ediacaran fauna",
        "None of the above"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 3:** The Ediacaran fauna (~575–535 million years ago) are known for soft-bodied organisms preserved as impressions of fronds, geometric disks, and blob-like forms — many with no clear affinity to modern animal phyla.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Did all the different organisms classified as Ediacaran fauna appear in the fossil record at the same time?",
      "choices": [
        "No. The fossil record indicates that some organisms appeared as early as 575 million years ago, but other organisms did not appear until 20 million years later.",
        "Yes. The fossil record indicates that most organisms in the Ediacaran fauna coexisted, and radiometric dating is not accurate enough to distinguish when different organisms appeared.",
        "Maybe. The fossil record is incomplete, and not enough is known about the Avalon Assemblage to state that the Ediacaran fauna didn't appear at the same time.",
        "Yes. Even though the fossil record indicates that some organisms existed for long periods, and many organisms existed for relatively short periods, scientists cannot know whether these organisms appeared at the same time or not.",
        "No. Scientists are unable to determine the relationships of Ediacaran fauna because they are so diverse."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 3:** Ediacaran organisms did not all appear simultaneously. The earliest (Avalon Assemblage) forms appear by ~575 million years ago, followed by progressively different assemblages (White Sea, Nama) over roughly 40 million years, with some taxa appearing 20 million years after the earliest forms.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "Which group does the following idea NOT apply to: \"many of the most diverse animal and plant species alive today belong to relatively recent radiations\"?",
      "choices": [
        "Flowering plants",
        "Insects",
        "Birds",
        "Bacteria",
        "Mammals"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 3:** Flowering plants, insects, birds, and mammals all underwent major adaptive radiations relatively recently (mostly within the last ~150 million years). Bacteria, by contrast, have been diversifying for ~3.5 billion years — their current diversity is the product of deep, not recent, evolutionary history.",
      "chapterId": "ch3",
      "sectionId": "ch3",
      "source": "textbook",
      "textbookRef": "ch03"
    },
    {
      "prompt": "How does homology relate to the theory of evolution?",
      "choices": [
        "Homology refers to traits that only superficially look alike, like bat wings and human arms; the theory of evolution cannot explain these similarities.",
        "Homology refers to traits that look alike but have entirely different origins, like the fins of dolphins and of fish; the theory of evolution cannot explain the origins.",
        "Homology refers to traits that are structurally similar in different organisms, like bat wings and human arms, because they each were inherited from a shared common ancestor with those traits; the theory of evolution provides a mechanism for those observations.",
        "Homology refers to traits that have converged on a shared form; the theory of evolution provides a mechanism for those observations."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 4:** Darwin, and many scientists before him, recognized homology as a basis for organization for comparative biology—that related organisms often had similar morphologies. The fact that many homologies are found together in the same groups of species strengthens support for Darwin's idea of descent with modification (see Chapter 2).",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "How accurate is radiometric dating?",
      "choices": [
        "Not very accurate because scientists cannot know how much of a particular isotope was originally present in a rock, and thus, they cannot know how much of it has decayed",
        "Very accurate because scientists can determine the exact age of rocks and the fossils found within them",
        "Accurate because radiometric dating can determine estimates for the ages of rocks and fossils, often with relatively small margins of error",
        "Not very accurate because scientists use probabilities to determine decay rates for each isotope they use in radiometric dating"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 4:** Radiometric dating provides estimates of age based on the half-life of the isotopes within the rocks. Different isotopes can be used to measure different time scales, and the time scale being addressed can affect the precision of the estimate. Isotopes with very long half-lives can be used to determine the ages of very old rocks with relative accuracy—say a 3 million year range for stromatolite fossils dating back 3.4 billion years. Whereas isotopes with shorter half-lives can provide more precise estimates for younger rocks—for example, a margin of error of 7000 years. Scientists can also use different elements to check and hone their estimates (see Chapter 3).",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "Besides radiometric dating, what other lines of evidence can be used to determine the ages of fossils?",
      "choices": [
        "Stratigraphy",
        "Homology",
        "Complexity",
        "a and b only",
        "All of the above"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 4:** Stratigraphy can be used to determine the relative ages of fossils from strata that are widespread and can be correlated in time. With the advent of radiometric dating, more precise estimates of age can be applied to fossils (see Chapter 3). Homology can be used to identify fossils that share a common ancestor, but it cannot be used to determine the ages of fossils. Complexity of fossils is not appropriate to determine the age of fossils—evolution has not been a \"march of progress,\" and the development of complexity is not necessarily related to age.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "Which of the following is a true statement?",
      "choices": [
        "The fewer the nodes between species, the more related to each other they are.",
        "Straight lines in phylogenies indicate species that have not evolved.",
        "Lineages that branch off later are more advanced than lineages that branch off earlier.",
        "Scientists are not looking for missing links."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 4:** Scientists are not looking for missing links. Paleontologists do not search for missing links in the sense of a direct line of evolutionary history. Instead, they look for fossils that can help resolve uncertainties in phylogenies and that can help resolve the history by which characters evolved in major clades.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "Which of the following is NOT a monophyletic group?",
      "choices": [
        "A clade",
        "Reptilia",
        "Aves",
        "Amphibia",
        "All of the above are monophyletic groups."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 4:** Reptilia, as traditionally defined (turtles, lizards, snakes, crocodiles), is a paraphyletic group because it excludes birds (Aves), which are descended from the common ancestor of all reptiles. A monophyletic group must include the common ancestor and ALL of its descendants. A clade, Aves, and Amphibia are all monophyletic.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "Based on your understanding of Carl Linnaeus' classification system, how would you treat his conclusions?",
      "choices": [
        "His concept of nested hierarchies accurately characterized and organized species relationships, so his conclusions are valid.",
        "His concept of nested hierarchies doesn't reflect modern understanding of species relationships, so Linnaean classification has no place in modern science.",
        "His classification scheme is based on evidence that has been refuted with modern techniques and should be ignored.",
        "His classification scheme provides a useful convention for naming species and thinking about species relationships, so his conclusions could be used as a starting point for examining taxonomic relationships.",
        "His classification scheme provides a useful convention for naming species, so the taxonomic units he named should be maintained."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 4:** Linnaeus' classification scheme provides a useful convention for naming species and thinking about species relationships, so his conclusions could be used as a starting point for examining taxonomic relationships. Compared with the tools of scientists today, Linnaeus built his taxonomic system on a relatively basic understanding of morphology, but evolutionary theory has added new explanations for these relationships and new insight to the meaning of taxonomic groupings.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "In the past, morphological evidence alone was used to examine the relationships of the cetaceans to other groups. According to this phylogeny (showing Balaenoptera, Tursiops, Ambulocetus, Protocetus, Pakicetus, Elomeryx, Archaeotherium, Hippopotamus, and Equus):",
      "choices": [
        "The extinct genus Ambulocetus is more distantly related to the genus Balaenoptera than to the extinct genus Protocetus.",
        "The genus Equus (horses) is more closely related to the genus Hippopotamus (hippos) than to the extinct genus Pakicetus.",
        "More changes have occurred in the whale lineage than in the horse lineage.",
        "Horses (genus Equus) were the ancestor of whales and hippos.",
        "None of the above are correct statements."
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 4:** None of the statements are correct. Ambulocetus shares a more recent common ancestor with Balaenoptera (within the whale clade) than with non-whale genera, so option A is wrong. Equus is more distantly related to Hippopotamus than Hippopotamus is to Pakicetus (whales and hippos share a recent common ancestor), so B is wrong. Branch length on a cladogram does not directly represent the amount of morphological change, so C cannot be concluded, and horses are not ancestral to whales or hippos—they share a common ancestor but lie on a separate lineage (D wrong).",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "How does including fossils in phylogenies of extant taxa affect the conclusions scientists can draw?",
      "choices": [
        "Including fossils can change the hypothesis generated by the phylogeny.",
        "Including fossils can define the timing of branching events.",
        "Including fossils can affect understanding of common ancestors.",
        "Including fossils can generate new questions about clades.",
        "All of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 4:** All of the above. Fossils can revise the hypothesis of a phylogeny, calibrate the timing of branching events (molecular clock calibration), clarify the character states of inferred common ancestors, and raise new questions about clade relationships and the tempo of character evolution.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "Which group of theropod dinosaurs did NOT have feathers according to the evogram in Figure 4.29?",
      "choices": [
        "Allosaurids",
        "Compsognathids",
        "Tyrannosauroids",
        "Oviraptorosaurs",
        "None of the theropod dinosaurs had feathers"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 4:** Allosaurids did not have feathers according to the evogram. Feathered branches include Compsognathids, Tyrannosauroids, Oviraptorosaurs, Dromeosaurids, Archaeopteryx, and living birds — these share synapomorphies for feather-related characters (tufted feathers, hollow cylindrical feathers with melanosomes, closed/asymmetrical feathers) that evolved after the Allosaurid branch split off.",
      "chapterId": "ch4",
      "sectionId": "ch4",
      "source": "textbook",
      "textbookRef": "ch04"
    },
    {
      "prompt": "How can the phylogeny on the left (showing family relationships among you, your sister, and your cousins) be used to understand the phylogeny on the right (showing relationships among humans, frogs, goldfish, and trout)?",
      "choices": [
        "The phylogeny on the left shows that you and your sister are more closely related to each other than you are to your cousins, just as humans and frogs are more closely related to each other than they are to goldfish or trout.",
        "The phylogeny on the left shows that the relationship between humans and frogs cannot be compared with the relationship between siblings.",
        "The phylogeny on the left shows that your cousins must be more closely related to each other than you and your sister because trout and goldfish are more closely related to each other than frogs and humans.",
        "The phylogeny on the right shows that humans are more closely related to goldfish than to trout."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 5:** Although the phylogeny on the left shows the relationships among individual family members and not groups of organisms, the idea of common ancestry is essentially the same. Humans are more closely related to frogs than they are to fish because they share a more recent common ancestor with frogs (P) — just like you and your sister share a more recent common ancestor (P) than you and your cousins (G). Humans share a more distant common ancestor with fish (G). The branches on a phylogeny can swing freely (like a mobile), so flipping positions does not change relatedness.",
      "chapterId": "ch_s_genetics",
      "sectionId": "ch_s_genetics",
      "source": "textbook",
      "textbookRef": "ch05"
    },
    {
      "prompt": "According to the text, what is an organism's phenotype?",
      "choices": [
        "The interaction of an organism's genes with the environment to produce characteristics such as how the amount of light a plant is exposed to influences its height",
        "Characteristics of an organism that can be classified into discrete categories, such as gender or eye color",
        "Any aspect of an organism that can be measured, such as how it looks, how it behaves, how it's structured",
        "The genetic makeup of an individual",
        "Both b and d"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 6:** The phenotype is linked to the genotype—genes interact with other genes and with the environment during the development of the phenotype. Some aspects of the phenotype can be classified into discrete categories, such as gender (female or male) or eye color (blue, green, brown), but many other characteristics cannot, such as height, length of the femur, or antler size (these traits vary in a range around a mean). The phenotype is any aspect of an organism that can be measured: morphology, physiology, and behavior. Why the others are wrong: - A: Genes do interact with the environment during development, but the phenotype is the characteristic itself, not the interaction. - B: Some phenotypic characteristics are discrete, but many are continuous; limiting the definition to discrete categories is too narrow. - D: The genetic makeup of an individual is the genotype, not the phenotype. - E: Combines two incorrect definitions.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "How many alleles can a genetic locus in a diploid individual have?",
      "choices": [
        "One",
        "Two",
        "More than two",
        "It depends on the locus."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 6:** There are no hard and fast rules about the number of alleles at any particular genetic locus. Mutations can create new alleles at any genetic locus, and the number of alleles and their frequencies within a population can change as a result of natural selection and genetic drift. A more appropriate way of representing alleles uses subscripts (A1, A2, A3, A4) or superscripts (Ester1, Ester4), reflecting the diverse number of alleles that may exist at any particular locus. Why the others are wrong: - A: Only fixed alleles (where all members of a population are homozygous) show a single allele; fixed loci are not typical. - B: Simple models using AA/Aa/aa notation imply only two alleles exist, but this is merely a convention. - C: A locus can have more than two alleles, but it can also have only one (fixed) or two; the actual count depends on the locus.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "Why is the variation of phenotypic traits often continuous, distributed around a mean in a bell-shaped curve?",
      "choices": [
        "Because phenotypic traits are a result of dominance",
        "Because phenotypic traits are not related to genotypes",
        "Because phenotypic traits are only influenced by the environment",
        "Because phenotypic traits are often polygenic"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 6:** Most phenotypic traits involve more than one gene (i.e., they are polygenic), and the different alleles from these different genes contribute to the trait differently. The result is a continuous distribution (like height, with all possible measurements in between). Most individuals will have measurements near the mean, with fewer and fewer in the \"tails,\" so the curve appears bell-shaped. Why the others are wrong: - A: Dominance can affect phenotypic traits, but it refers to alleles at a single genetic locus—most traits are not reducible to simple Mendelian patterns. - B: Although the relationship is complex, genotype and phenotype are intimately related. - C: The environment influences phenotypic expression, but a distinct genetic architecture underlies it.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "Which of the following is a true statement?",
      "choices": [
        "A dominant allele is an allele that produces the same phenotype whether it is homozygous or heterozygous.",
        "The dominant allele of a trait will always have the highest frequency in a population.",
        "Genetic drift does not occur in large populations.",
        "Alleles are different forms of genes."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 6:** A dominant allele is defined by its phenotypic effect: a single copy is sufficient to produce the trait, so the homozygous (AA) and heterozygous (Aa) individuals show the same phenotype. The answer key for this chapter identifies option A as the correct true statement. Why the others are wrong: - B: Dominance refers to phenotypic expression, not frequency. Huntington's disease is rare but dominant; blood type O is common but recessive. Allele frequencies are determined by selection and drift, not by dominance. - C: Genetic drift occurs in all populations—it is the random sampling of alleles each generation. Larger populations simply experience smaller proportional changes from drift because more copies of each allele are present. - D: Although intuitive-sounding, this answer is imprecise. An allele is a specific alternative form of a gene or genetic locus, identified by a particular DNA sequence; a gene is a segment of DNA whose sequence codes for protein/RNA or regulates expression. Calling alleles \"different forms of genes\" treats \"gene\" and \"allele\" as interchangeable, which the textbook flags as a misconception.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "What are genetic loci?",
      "choices": [
        "Variants of a particular gene or DNA region",
        "The plural form of genetic locus",
        "The specific locations of genes or base pairs",
        "Both a and b",
        "Both b and c"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 6:** A genetic locus is the specific location of a gene or piece of DNA sequence on a chromosome; \"loci\" is the plural of \"locus.\" Both B (plural form) and C (specific locations) are correct, so the combined answer E is correct. Why the others are wrong: - A: Variants of a gene are alleles, not loci. An allele is the DNA sequence variant; the locus is the location where that variant sits. Confusing these is a common misconception. - D and F: Incorporate the incorrect answer A.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "In a tetraploid organism, how many copies of the same allele will it carry at a locus if it is heterozygous at that locus?",
      "choices": [
        "one",
        "two",
        "three",
        "four",
        "a, b, or c"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 6:** A tetraploid organism carries four copies of each chromosome, so four alleles at each locus. \"Heterozygous\" simply means NOT all identical. The four alleles could be distributed as 3-1, 2-2, 2-1-1, or 1-1-1-1 combinations. Therefore the number of copies of \"the same allele\" the organism carries at a heterozygous locus could be 1 (all four different, or three different plus one copy of the focal allele), 2 (two pairs), or 3 (three copies of one allele and one of another). Four copies of the same allele would be homozygous, not heterozygous. So the answer is a, b, or c (one, two, or three). Why the others are wrong: - A, B, C each alone: Any of these is possible but not the only possibility. - D (four): Four copies of the same allele means homozygous, the opposite of the premise.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "How can population genetics help us understand the evolution of mosquito resistance?",
      "choices": [
        "By examining how the applications of pesticides cause mortality of mosquitoes",
        "By examining the distribution of alleles within populations and the mechanisms that cause allele frequencies to change over time",
        "By examining the mating and reproductive tactics of mosquitoes across populations that are resistant and non-resistant",
        "By examining the phylogenetic relationships among species of mosquitoes and their common ancestors",
        "Populations genetics examines all of the above."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 6:** Population genetics is defined in Chapter 6 as the study of the distribution of alleles within populations and the mechanisms that can cause allele frequencies to change over time. Applying this framework to mosquitoes allows researchers to quantify resistance-allele frequencies across populations, identify selective sweeps, and estimate the strength and speed of selection driven by insecticide use. Why the others are wrong: - A: Describes toxicology/pharmacology, not allele-level dynamics. - C: Describes behavioral ecology, not the genetic architecture of resistance. - D: Describes phylogenetics at the species level—a different scale. - E: Incorrect because options A, C, and D are not part of population genetics.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "What are population geneticists referring to when they say that sexually reproducing organisms are mating at random?",
      "choices": [
        "That, for a focal genetic locus, the probability of fertilization of one gamete by another will not vary depending on which allele is carried by the gametes",
        "That mate choice is not an important factor for sexually reproducing organisms",
        "That some gametes are not any more likely to encounter other gametes",
        "That models of population genetics have to make unrealistic assumptions about sexually reproducing organisms to be useful",
        "That sexually reproducing organisms choose mates randomly within the population"
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 6:** \"Random mating\" in population genetics is a technical statement about gamete-level probabilities at a focal locus: the chance that one gamete fertilizes another does not depend on the alleles they carry at that locus. This assumption is what allows Hardy-Weinberg expectations (p^2 + 2pq + q^2) to hold. It does NOT mean organisms lack mate preferences in general—only that, with respect to the locus under study, those preferences do not create a correlation between allele identity and fertilization probability. Why the others are wrong: - B: Mate choice is often very important; the assumption is about allele-level outcomes at a specific locus, not the absence of mate choice. - C: Incorrect—random mating assumes gametes DO have equal opportunity to encounter others. - D: A philosophical mischaracterization of the purpose of models. - E: Organisms do not literally pick mates at random; this is a common misreading of the assumption.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "In a population of 100 offspring, how many individuals would you predict will be heterozygous at a particular locus with two alleles if the frequency of one of the alleles in the parent generation is 0.4?",
      "choices": [
        "16",
        "36",
        "48",
        "52",
        "100"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 6:** Using Hardy-Weinberg, with p = 0.4 and q = 0.6, the expected frequency of heterozygotes is: 2pq = 2 × 0.4 × 0.6 = 0.48. For 100 offspring: 100 × 0.48 = 48 heterozygous individuals. Why the others are wrong: - A (16): That's p^2 × 100 = 0.16 × 100 — the frequency of the p-homozygote, not heterozygotes. - B (36): That's q^2 × 100 = 0.36 × 100 — the frequency of the q-homozygote. - D (52): No simple calculation produces this value. - E (100): Would require that every offspring be heterozygous, which is impossible when p and q are both nonzero and mating is random.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "Which of these statements about balancing selection is TRUE?",
      "choices": [
        "It is possible only in sexually reproducing species.",
        "It is responsible for maintaining the S allele for sickle-cell anemia within humans.",
        "It is not possible when heterozygotes have a higher fitness.",
        "It is why sickle-cell anemia is selected against in areas with high levels of malaria.",
        "None. All are false statements."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 6:** Heterozygote advantage is a form of balancing selection. In regions with endemic malaria, heterozygotes (AS) at the β-hemoglobin locus have higher fitness than either AA (more vulnerable to malaria) or SS (severe sickle-cell anemia). This maintains the S allele at appreciable frequency in the population even though SS homozygotes have drastically reduced fitness—a textbook illustration of balancing selection preserving allelic diversity. Why the others are wrong: - A: Balancing selection can operate in any species with heritable variation; it is not restricted to sexual reproducers. - C: Heterozygote advantage is itself a form of balancing selection, so balancing selection is certainly possible when heterozygotes have higher fitness. - D: Sickle-cell homozygotes (SS) are selected against, but balancing selection explains why S is MAINTAINED, not why it is selected against. The statement misrepresents the mechanism.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "How does drift affect the frequencies of alleles within a population?",
      "choices": [
        "Some individuals are more likely to breed with other individuals, and so only their alleles will appear in the next generation.",
        "Random mating does not equal uniform mating, and as a result of this imperfect sampling, some alleles do not get represented in the next generation.",
        "In large populations, the likelihood that all individuals will be able to mate is low, so the likelihood that all alleles being represented in the next generation is also low.",
        "Drift results in a variety of genotypes over many generations because the heterozygotes mate randomly leading to some homozygotes of each allele and some heterozygotes, changing the frequency of the alleles.",
        "Random mating within a population mixes alleles at a particular locus into many different combinations, and when this happens, frequencies of alleles change across generations."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 6:** Genetic drift is the random, nonrepresentative sampling of alleles from the parental gene pool during breeding. Even if mating is random in the technical sense, the finite number of gametes that actually contribute to the next generation is a sample of the parental allele frequencies, and sampling produces stochastic deviations. Some alleles (especially rare ones) may fail to be sampled and drop to lower frequency or disappear entirely by chance alone. This is exactly what \"imperfect sampling\" captures in option B. Why the others are wrong: - A: Describes nonrandom mating (e.g., sexual selection or assortative mating), not drift. - C: Inverts the relationship—drift is MORE potent in small populations, not large ones. - D: Describes Mendelian segregation into genotype classes, not drift's effect on allele frequencies. - E: Random mating shuffles genotype combinations but does not itself change allele frequencies; that's a key Hardy-Weinberg insight.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "According to Figure 6.8, what is the difference between the probabilities that a rare allele and a common allele will be lost in a population bottleneck of 20 individuals?",
      "choices": [
        "About 65 percent",
        "100 percent",
        "5 percent",
        "0.9 percent",
        "It depends on the allele."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 6:** Figure 6.8 plots the probability of losing an allele through a bottleneck as a function of both starting allele frequency and bottleneck size. At a bottleneck size of 20 individuals, the probability of losing a rare allele is high (near or above ~65%) while the probability of losing a common allele is very low (near 0%). The difference is approximately 65 percentage points. Why the others are wrong: - B (100%): Implies certainty of loss of the rare allele AND certainty of retention of the common allele, an overestimate. - C (5%): Too small—matches the probability of losing a common allele alone, not the difference. - D (0.9%): Far too small. - E: Not appropriate because the figure specifically quantifies this comparison.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "What is the difference between bottlenecks and founder effects?",
      "choices": [
        "Bottlenecks reduce genetic variation because of drift; founder effects reduce genetic variation by shrinking the population size.",
        "Bottlenecks reduce genetic variation by shrinking the population size; founder effects reduce genetic variation because of drift.",
        "Bottlenecks can happen to any population; founder effects only happen when small numbers of individuals start a new population.",
        "Bottlenecks are events that reduce the number of individuals; founder effects describe the loss of genetic variation that accompanies events like bottlenecks.",
        "Bottlenecks only affect the diversity of alleles when they severely cut down the population; founder effects always severely cut down the population."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 6:** Bottlenecks are drastic reductions in the size of an existing population (e.g., from disease, climate, or hunting), and they can happen to any population. Founder effects are a specific type of drift that occurs when a small number of individuals colonize a new area and establish a new population, so that the new population begins with an unrepresentative sample of the source population's alleles. Both involve drift acting on a small sample, but they differ in scenario: bottleneck = existing population shrinks; founder effect = new population starts small. Why the others are wrong: - A and B: Incorrectly separate the mechanisms. Both bottlenecks and founder effects reduce genetic variation through drift acting on small sample sizes. - D: Conflates the two—both events reduce individuals AND involve loss of variation; they differ in context, not in whether they \"are events\" vs. \"describe loss.\" - E: Mischaracterizes both—bottlenecks can affect diversity at any severity, and founder effects do not require severe cuts in an existing population (they start fresh).",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "Which type of natural selection favors rare genotypes?",
      "choices": [
        "Balancing selection",
        "Negative-frequency dependent selection",
        "Negative selection",
        "Positive selection",
        "None of the above favor rare genotypes."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 6:** Negative frequency-dependent selection occurs when the fitness of an allele or genotype is higher when it is rare than when it is common. This specifically favors rare genotypes. The elderflower orchid example (Figure 6.18) and the bumblebee learning dynamic illustrate this mechanism, as do many host-parasite systems where parasites track the most common host genotype. Why the others are wrong: - A (Balancing selection): This is a broader umbrella term that includes negative frequency-dependent selection AND heterozygote advantage. B is more specific and precise for \"favors rare genotypes.\" - C (Negative selection): Removes deleterious alleles, reducing their frequency; it doesn't favor anything rare per se. - D (Positive selection): Increases allele frequency regardless of starting frequency; once an allele becomes common, positive selection still favors it, not \"rarity.\" - E: Incorrect because B exactly describes the phenomenon. Note: One could argue A is also technically correct since negative frequency-dependent selection is a type of balancing selection, but B is the more specific and direct answer the question is looking for.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "What does an inbreeding coefficient of 0.25 signify?",
      "choices": [
        "0.25 is the inbreeding coefficient assigned to Charles II.",
        "0.25 is the average probability that alleles at two loci in an individual are identical by descent.",
        "0.25 signifies the level of relatedness of most populations.",
        "0.25 is the inbreeding coefficient of most royal families.",
        "0.25 is the inbreeding coefficient of a child produced by a brother and sister mating."
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 6:** The inbreeding coefficient F is the probability that two alleles at a locus in an individual are identical by descent (IBD)—i.e., inherited from a common ancestor. For a child of full siblings (brother × sister), the probability that both alleles at any given locus trace back to the same grandparental allele is 0.25. This is the classic textbook value for a full-sib mating. Why the others are wrong: - A: Charles II of Spain had F ≈ 0.254 due to generations of cousin/uncle-niece marriages—coincidentally near 0.25, but this was the result of many generations of compound inbreeding, not a defining meaning of 0.25. The textbook uses him as a historical example but the definition of 0.25 is the full-sib value. - B: Misstates the definition—F is about alleles at a single locus (not \"two loci\"), identical by descent. - C: Most populations are not at F = 0.25. - D: Not a defining meaning; royal-family F values vary widely.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "Why would conservation biologists be concerned about inbreeding depression?",
      "choices": [
        "Because endangered species often have small populations prone to inbreeding",
        "Because rare, recessive alleles can become expressed in a homozygous state where they can reduce the fitness of individuals",
        "Because inbreeding depression can affect reproductive rates of endangered species",
        "Because inbreeding depression can reduce the genetic variation within a population",
        "All of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 6:** Every option identifies a legitimate conservation concern: - A: Small endangered populations are statistically more likely to experience mating between relatives simply because there are fewer unrelated individuals available. - B: The mechanistic basis of inbreeding depression—rare deleterious recessive alleles usually hidden in heterozygotes become exposed in homozygous descendants of related parents. - C: Reduced reproductive rates (lower fertility, offspring viability, juvenile survival) directly threaten population persistence. - D: Inbreeding homogenizes genotypes, reducing effective heterozygosity and thus the raw material for future adaptation. Together these illustrate why genetic rescue (e.g., the Florida panther Texas-puma translocation in the Go the Distance reading) is sometimes needed to restore heterozygosity and fitness.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch06"
    },
    {
      "prompt": "What is the difference between polyphenic traits and polygenic traits?",
      "choices": [
        "Polyphenic traits are the different traits that arise because different alleles lead to different phenotypes; polygenic traits are traits influenced by many genes leading to a continuous distribution of phenotypes over a given range.",
        "Polyphenic traits are the multiple, discrete phenotypes that can arise from different alleles within a population; polygenic traits vary continuously within a population because of heritable variation.",
        "Polyphenic traits are the multiple, discrete phenotypes that can arise from a single genotype depending on environmental circumstances; polygenic traits are traits influenced by many genes leading to a continuous distribution of phenotypic variation over a given range.",
        "Polyphenic traits are traits that result when natural selection favors rare genotypes leading to multiple phenotypes within a population; polygenic traits are traits that arise because a single gene affects the expression of many different phenotypic traits."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 7:** Section 5.4 introduces polyphenic and polygenic traits. Polyphenic traits often arise because of a threshold of sensitivity to the environment (e.g., an individual male beetle that would produce horns if food was plentiful but not produce horns if food was scarce). Polygenic traits are also known as quantitative traits - the topic of this chapter.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "Which of the following were important facts in Charles Darwin's development of theory of evolution by natural selection?",
      "choices": [
        "No two individuals are exactly the same; rather, every population displays enormous variability.",
        "Much of the variation among individuals within a population is heritable.",
        "Organisms can inherit characters that were acquired during their parents' lifetime.",
        "Both a and b",
        "Both b and c"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 7:** Darwin used two facts to infer that natural selection would lead to evolution and the production of new species: that no two individuals are exactly the same and much of the variation among individuals within a population was heritable (see Section 2.3 and Figure 2.19). Option c reflects Lamarck's theory of inheritance of acquired characteristics, which Darwin did not endorse.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "Can genes that respond to environmental stimuli be passed on to offspring?",
      "choices": [
        "Yes. Individuals that learn how to respond to the environment can pass that information to their offspring.",
        "Yes. Individuals can inherit the mechanisms that respond to the environment.",
        "No. The only \"environmental\" influences on gene expression that can be inherited come from other gene products, such as hormones, transcription factors, and cis- and trans-acting elements. Any effects of external environmental factors are not encoded by the genome, so they cannot be heritable.",
        "No. Environmental factors, such as the amount of food available to an individual or the temperature an egg is exposed to, are not heritable."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 7:** Some traits that are sensitive to environmental stimuli are heritable. Phenotypic plasticity is the changes in the phenotype produced by a single genotype in different environments (see Section 5.5). This chapter will explore the mechanism of phenotypic plasticity and its measurement (see Box 7.4 and Section 7.4).",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "What do the terms in the equation V_P = V_G + V_E mean?",
      "choices": [
        "Broad-sense heritability equals the ratio of variation due to genotype to the variation due to phenotype.",
        "Phenotypic variation results from variation due to the genotype plus variation due to the environment.",
        "Heritability is the proportion of the total phenotypic variance that is attributable to genetic variation among individuals.",
        "The variation due to genotype can be calculated by multiplying the phenotypic variance by broad-sense heritability.",
        "All of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 7:** From answer key (p. 318, Test Yourself 1.e). All statements are correct. V_P = V_G + V_E decomposes total phenotypic variance into genetic and environmental components (b). Broad-sense heritability H^2 = V_G / V_P (a, c). Rearranging gives V_G = H^2 x V_P (d). Therefore all statements describe correct aspects of the variance-components model.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "Figure 7.5 shows parent-offspring regressions for human height (slope h^2 = 0.57), tree swallow (Tachycineta bicolor) tarsus length (h^2 = 0.50), and wild radish (Raphanus raphanistrum) pistil length. Which of the populations would you predict will evolve most in response to selection?",
      "choices": [
        "Humans",
        "Tree swallows",
        "Wild radish",
        "Both a and b should evolve most.",
        "None of the populations should evolve."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 7:** From answer key (p. 318, Test Yourself 2.c). The population with the steepest parent-offspring regression slope (the highest narrow-sense heritability, h^2) will evolve fastest for a given selection differential, because R = h^2 x S. Of the three, wild radish has the highest h^2 (shown in Figure 7.5 as having the steepest slope), so it is predicted to evolve most in response to selection.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "According to Figure 7.13, how did Hoekstra and colleagues test whether the Agouti QTL they had discovered was coding for coat color?",
      "choices": [
        "They conducted a second hybridization study and found that coat color phenotypes were most closely correlated with the Agouti QTL.",
        "They went back to their original study and mapped genes paying particular attention to the Agouti QTL.",
        "They determined the \"logarithm of the odds\" score to estimate whether the marker and the gene influencing coat color were likely to lie next to each other on the chromosome.",
        "They examined the color of each mouse's coat at seven locations and determined which had the greatest influence on coat color overall.",
        "They conducted a second hybridization study and found that coat color was influenced by more than one gene."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 7:** From answer key (p. 318, Test Yourself 3.c). LOD (logarithm of the odds) is the statistical score used in QTL mapping to estimate the likelihood that a genetic marker lies next to a gene influencing a focal trait. High LOD scores at the Agouti locus indicated tight linkage between the marker and coat-color variation, supporting Agouti as a causal gene for coat color.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "Is coat color in oldfield mice a polygenic trait?",
      "choices": [
        "No. QTL regions are components of DNA produced by hybridization; they do not represent the actual DNA of oldfield mice.",
        "No. Agouti and Mc1r are QTL regions that encode for receptors and repressors; they are not actually genes, so coat color cannot be polygenic.",
        "Maybe. Scientists don't really understand the genes behind coat color: Agouti and Mc1r are just regions they can identify.",
        "Yes. Two genes are primarily involved in coat color: Agouti encoding a repressor that shuts down the Mc1r receptor; Mc1r encoding a receptor that triggers the production of pigment.",
        "Yes. All animal traits are polygenic."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 7:** From answer key (p. 318, Test Yourself 4.d). Coat color in oldfield mice is polygenic, with at least two major contributing loci: Agouti (which encodes a secreted protein that antagonizes the Mc1r receptor, promoting light pigment production) and Mc1r (a melanocortin-1 receptor whose activation triggers dark eumelanin synthesis). Because more than one gene contributes to the continuous variation in coat color, the trait is polygenic.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "According to Figure 7.21, which trait(s) of Caenorhabditis elegans is/are phenotypically plastic?",
      "choices": [
        "Age at maturity",
        "Fertility",
        "Chromosome IV",
        "Both a and b",
        "None of the above"
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 7:** From answer key (p. 318, Test Yourself 5.d). Figure 7.21 shows reaction norms for two C. elegans life-history traits across environments: age at maturity and fertility both change in response to environmental conditions (different genotypes show different reaction norms), which is the signature of phenotypic plasticity. Chromosome IV is a physical chromosome, not a phenotypic trait.",
      "chapterId": "ch_s_evo_mech",
      "sectionId": "ch_s_evo_mech",
      "source": "textbook",
      "textbookRef": "ch07"
    },
    {
      "prompt": "How do parents adjust the sex ratio of their broods?",
      "choices": [
        "Parents cannot adjust the sex ratios of their broods.",
        "Sex ratio adjustment only occurs in social insects, where females control the sex of offspring by fertilizing (female) or not (male) their eggs.",
        "Sex ratio adjustment only occurs in role-reversed species, so males choose which gender survives.",
        "Parents selectively feed some offspring and not others, so only the most competitive gender survives.",
        "The mechanisms are largely unknown, but substantial evidence indicates that parents can and do adjust the sex ratios of their broods."
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 12:** The mechanisms by which parents adjust offspring sex ratios are largely unknown, but substantial evidence indicates that parents can and do adjust the sex ratios of their broods across many taxa (answer key indicates Q1 = e/E).",
      "chapterId": "ch_s_ch12",
      "sectionId": "ch_s_ch12",
      "source": "textbook",
      "textbookRef": "ch12"
    },
    {
      "prompt": "Are scientists just guessing about gene imprinting?",
      "choices": [
        "Yes. Gene imprinting is just a theory, and therefore it is just a guess.",
        "Yes. Scientists don't really understand what genes are and what they do; they look for indirect evidence, but they are only guessing.",
        "Yes. Scientists have done a few experiments looking at how genes interact, but the evidence has not risen beyond the level of a guess.",
        "No. Gene imprinting has valid scientific context and initial experiments provide evidence to support Haig's hypothesis."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 12:** Gene imprinting is supported by valid scientific context and initial experiments providing evidence for Haig's hypothesis regarding parental conflict over gene expression in offspring.",
      "chapterId": "ch_s_ch12",
      "sectionId": "ch_s_ch12",
      "source": "textbook",
      "textbookRef": "ch12"
    },
    {
      "prompt": "Which is the definition of senescence?",
      "choices": [
        "The deterioration of the human mind as a person ages",
        "Alzheimer's disease",
        "The deterioration in the biological functions of an organism as it ages",
        "The tradeoff between reproducing and living longer",
        "None of the above"
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 12:** Senescence is defined as the deterioration in the biological functions of an organism as it ages. It is a whole-organism biological phenomenon, not limited to cognition (options A, B) nor the same as the life-history trade-off that may drive it (option D).",
      "chapterId": "ch_s_ch12",
      "sectionId": "ch_s_ch12",
      "source": "textbook",
      "textbookRef": "ch12"
    },
    {
      "prompt": "Why would some scientists argue that menopause simply results from life-history trade-offs?",
      "choices": [
        "Because everything is a trade-off, and it makes sense that a female's inability to breed late in life must be a trade-off",
        "Because natural selection cannot act on individuals that no longer reproduce.",
        "Because genetic imprinting by males can cause females to become infertile",
        "Because the mechanism that leads to infertility in menopausal women (i.e., damage to a female's eggs over time) is the same in other species",
        "All of the above"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 12:** The life-history trade-off argument for menopause centers on the idea that natural selection cannot directly act on traits expressed by individuals that no longer reproduce. Once a female has stopped reproducing, selection no longer filters alleles affecting her post-reproductive biology, so late-life infertility may simply emerge as a byproduct of earlier life-history trade-offs rather than a directly selected adaptation.",
      "chapterId": "ch_s_ch12",
      "sectionId": "ch_s_ch12",
      "source": "textbook",
      "textbookRef": "ch12"
    },
    {
      "prompt": "Which is NOT one of the three conditions necessary for evolution by natural selection to occur?",
      "choices": [
        "Individuals must differ in the characteristics of a trait.",
        "The differences among individuals in a trait must be at least partially heritable.",
        "Some individuals survive and reproduce more than others because of those differences.",
        "All individuals in the population must carry the same mutation."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 18:** The three conditions for natural selection are: (1) phenotypic variation exists, (2) variation is at least partially heritable, and (3) variation affects differential survival/reproduction (fitness). Choice d (all individuals carrying the same mutation) would ELIMINATE the variation needed — so it is NOT a requirement.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Which of the following is a reason we get sick, according to Nesse and Williams?",
      "choices": [
        "Defenses (like fever) that can feel like illness.",
        "Infections from rapidly evolving pathogens.",
        "Novel environments and design trade-offs.",
        "Slow evolution of humans vs. pathogens.",
        "All of the above"
      ],
      "answer": 4,
      "why": "📘 **Textbook Ch 18:** Nesse &amp; Williams identified six classes of reasons: defenses, infection, novel environments, genes with trade-offs, design compromises, and slow human evolution. All options a–d are valid members of that set.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Why is antibiotic resistance considered a textbook example of natural selection?",
      "choices": [
        "Bacteria can learn to resist.",
        "Antibiotics select pre-existing resistant variants that then reproduce more than susceptibles.",
        "All bacteria are resistant from birth.",
        "Resistance appears only after antibiotic use begins.",
        "Resistance requires human intervention to evolve."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 18:** Antibiotics filter existing genetic variation — they don't induce it. Resistant variants (from random mutation or horizontal gene transfer) survive antibiotic exposure and reproduce, while susceptibles die. This is Darwinian selection acting on a bacterial population in real time.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "The sickle-cell allele persists at high frequency in malaria-endemic regions because:",
      "choices": [
        "HbS homozygotes resist malaria.",
        "Mutations spontaneously re-create HbS.",
        "HbS is selectively neutral.",
        "Heterozygotes (HbA/HbS) have higher fitness than either homozygote."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 18:** This is balancing selection via heterozygote advantage. HbA/HbS heterozygotes resist malaria without developing full sickle-cell disease, making them fitter than either HbA/HbA (malaria-susceptible) or HbS/HbS (sickle-cell disease).",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Fever during infection is best understood as:",
      "choices": [
        "An evolved host defense that inhibits pathogen growth.",
        "A malfunction of the immune system.",
        "Caused by the pathogen for its benefit.",
        "Always harmful and needing suppression."
      ],
      "answer": 0,
      "why": "📘 **Textbook Ch 18:** Elevated body temperature inhibits replication of many pathogens and enhances immune-cell function. Fever is an evolved defense — not the disease itself — so aggressive fever suppression can sometimes prolong infection.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Which is an example of a 'mismatch disease'?",
      "choices": [
        "Smallpox",
        "Type 2 diabetes",
        "Down syndrome",
        "Measles",
        "Sickle-cell anemia"
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 18:** Mismatch diseases arise when traits that evolved under ancestral conditions become maladaptive in modern environments. Type 2 diabetes reflects a mismatch between ancestral metabolism (thrifty under scarcity) and modern diets (chronic caloric excess).",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Aging (senescence) is best explained evolutionarily by:",
      "choices": [
        "Genes programmed to kill the organism at a set age.",
        "Oxidative damage alone.",
        "Telomere shortening alone.",
        "Weak selection on late-life traits → antagonistic pleiotropy and mutation accumulation.",
        "Random chance."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 18:** Because most reproduction occurs early, selection is weak against alleles that cause late-life harm. Williams' antagonistic pleiotropy (alleles good early, bad late) and Medawar's mutation accumulation produce senescence as an evolutionary side-effect — not a programmed process.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "The hygiene hypothesis proposes that:",
      "choices": [
        "Hand-washing causes allergies.",
        "Too-clean early environments disrupt immune development, increasing allergies/autoimmunity.",
        "All infections are beneficial.",
        "Hygiene is unnecessary.",
        "Hygiene caused cancer."
      ],
      "answer": 1,
      "why": "📘 **Textbook Ch 18:** The immune system co-evolved with a rich microbial milieu. Modern ultra-hygienic environments may underexpose developing immune systems, increasing rates of allergies, asthma, and autoimmune diseases. It does NOT argue against basic hygiene.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Pathogens with vector-borne or waterborne transmission tend to evolve:",
      "choices": [
        "Lower virulence than direct-contact pathogens.",
        "The same virulence as direct-contact pathogens.",
        "Higher virulence — because hosts don't need to be mobile for transmission.",
        "No virulence at all.",
        "Intermittent virulence."
      ],
      "answer": 2,
      "why": "📘 **Textbook Ch 18:** Virulence evolves with transmission mode. When transmission doesn't require the host to move (waterborne, vector-borne), pathogens can exploit hosts heavily without losing transmission. Direct-contact pathogens depend on mobile hosts and usually evolve lower virulence.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    },
    {
      "prompt": "Which of the following best summarizes the evolutionary-medicine perspective?",
      "choices": [
        "Replace clinical medicine with evolutionary theory.",
        "Treat all diseases as adaptations.",
        "Ignore proximate mechanisms.",
        "Complement clinical practice by asking WHY our bodies are vulnerable, not just HOW disease works.",
        "Treat pathogens as unchanging."
      ],
      "answer": 3,
      "why": "📘 **Textbook Ch 18:** Evolutionary medicine complements — does not replace — mechanistic medicine. It adds the 'ultimate why' (evolutionary history, trade-offs, mismatch) to the clinical 'proximate how'. Understanding both yields better prevention, diagnosis, and treatment.",
      "chapterId": "ch18",
      "sectionId": "ch18",
      "source": "textbook",
      "textbookRef": "ch18"
    }
  ],
  "flashcards": []
};
