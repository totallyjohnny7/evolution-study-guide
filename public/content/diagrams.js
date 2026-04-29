/* Hand-drawn lecture diagrams. Dark editorial theme matching the rest of the site.
   Palette: bg #0c0e12, bg-elev #14171d, ink #e6dfd0, ink-dim #a59a83, ink-faint #6b6353,
            accent #c89b2e, correct #5fa871, wrong #c86462, info #7a8fa8.
   Each SVG is ~720x220. Embedded inline so they inherit the page's font stack. */

window.LECTURE_DIAGRAMS = {

L01: `<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three requirements for natural selection to produce evolution">
<rect width="720" height="220" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">THREE REQUIREMENTS · NATURAL SELECTION → EVOLUTION</text>
<g font-family="Fraunces, serif" font-style="italic" font-size="16" fill="#e6dfd0">
  <rect x="40" y="60" width="170" height="100" fill="#0c0e12" stroke="#c89b2e" stroke-width="1.4" rx="4"/>
  <text x="125" y="92" text-anchor="middle">Variation</text>
  <text x="125" y="120" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#a59a83">individuals differ</text>
  <text x="125" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#a59a83">in a trait</text>
  <rect x="275" y="60" width="170" height="100" fill="#0c0e12" stroke="#c89b2e" stroke-width="1.4" rx="4"/>
  <text x="360" y="92" text-anchor="middle">Heritability</text>
  <text x="360" y="120" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#a59a83">trait differences</text>
  <text x="360" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#a59a83">are genetic</text>
  <rect x="510" y="60" width="170" height="100" fill="#0c0e12" stroke="#c89b2e" stroke-width="1.4" rx="4"/>
  <text x="595" y="92" text-anchor="middle">Differential</text>
  <text x="595" y="112" text-anchor="middle">reproduction</text>
  <text x="595" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#a59a83">some leave more offspring</text>
</g>
<path d="M 215 110 L 270 110" stroke="#c89b2e" stroke-width="1.4" marker-end="url(#arr1)"/>
<path d="M 450 110 L 505 110" stroke="#c89b2e" stroke-width="1.4" marker-end="url(#arr1)"/>
<defs><marker id="arr1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#c89b2e"/></marker></defs>
<text x="360" y="190" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="14" fill="#5fa871">All three required → evolution. Drop heritability → no evolution.</text>
</svg>`,

L02: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Timeline of evolutionary thought">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">PRE-DARWIN → DARWIN · KEY FIGURES</text>
<line x1="60" y1="120" x2="660" y2="120" stroke="#6b6353" stroke-width="1"/>
<g font-family="Inter,sans-serif" font-size="10" fill="#a59a83">
  <circle cx="100" cy="120" r="6" fill="#7a8fa8"/><text x="100" y="148" text-anchor="middle">~1750</text>
  <circle cx="220" cy="120" r="6" fill="#7a8fa8"/><text x="220" y="148" text-anchor="middle">1809</text>
  <circle cx="340" cy="120" r="6" fill="#7a8fa8"/><text x="340" y="148" text-anchor="middle">1830s</text>
  <circle cx="460" cy="120" r="6" fill="#7a8fa8"/><text x="460" y="148" text-anchor="middle">~1810</text>
  <circle cx="580" cy="120" r="6" fill="#c89b2e"/><text x="580" y="148" text-anchor="middle">1858–59</text>
</g>
<g font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#e6dfd0" text-anchor="middle">
  <text x="100" y="92">Linnaeus</text>
  <text x="100" y="108" font-family="Inter,sans-serif" font-size="10" fill="#a59a83" font-style="normal">classifies life</text>
  <text x="220" y="92">Lamarck</text>
  <text x="220" y="108" font-family="Inter,sans-serif" font-size="10" fill="#a59a83" font-style="normal">acquired traits</text>
  <text x="340" y="92">Lyell</text>
  <text x="340" y="108" font-family="Inter,sans-serif" font-size="10" fill="#a59a83" font-style="normal">deep time</text>
  <text x="460" y="92">W. Smith</text>
  <text x="460" y="108" font-family="Inter,sans-serif" font-size="10" fill="#a59a83" font-style="normal">extinction</text>
  <text x="580" y="92" fill="#c89b2e">Darwin / Wallace</text>
  <text x="580" y="108" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e" font-style="normal">natural selection</text>
</g>
<text x="360" y="200" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#5fa871">Lyell's deep time + Smith's extinction = the canvas; Darwin &amp; Wallace fill it in.</text>
</svg>`,

L03: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Levels of gene expression regulation">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">FOUR LEVELS OF GENE EXPRESSION REGULATION</text>
<g font-family="Fraunces,serif" font-style="italic" font-size="14" fill="#e6dfd0">
  <rect x="40" y="55" width="160" height="155" fill="#0c0e12" stroke="#7a8fa8" stroke-width="1" rx="4"/>
  <text x="120" y="80" text-anchor="middle" fill="#7a8fa8">Pre-transcriptional</text>
  <text x="120" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">DNA methylation</text>
  <text x="120" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Histone modification</text>
  <text x="120" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Chromatin remodeling</text>
  <text x="120" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-style="italic" fill="#a59a83">controls ACCESS</text>

  <rect x="210" y="55" width="160" height="155" fill="#0c0e12" stroke="#c89b2e" stroke-width="1" rx="4"/>
  <text x="290" y="80" text-anchor="middle" fill="#c89b2e">Transcriptional</text>
  <text x="290" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">TF binding</text>
  <text x="290" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Promoter / enhancer</text>
  <text x="290" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">RNA Pol II</text>
  <text x="290" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-style="italic" fill="#a59a83">controls RATE</text>

  <rect x="380" y="55" width="160" height="155" fill="#0c0e12" stroke="#5fa871" stroke-width="1" rx="4"/>
  <text x="460" y="80" text-anchor="middle" fill="#5fa871">Post-transcriptional</text>
  <text x="460" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Alt. splicing</text>
  <text x="460" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">microRNA</text>
  <text x="460" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">mRNA stability</text>
  <text x="460" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-style="italic" fill="#a59a83">edits the mRNA</text>

  <rect x="550" y="55" width="160" height="155" fill="#0c0e12" stroke="#c86462" stroke-width="1" rx="4"/>
  <text x="630" y="80" text-anchor="middle" fill="#c86462">Post-translational</text>
  <text x="630" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Phosphorylation</text>
  <text x="630" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Ubiquitination</text>
  <text x="630" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Cleavage / folding</text>
  <text x="630" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-style="italic" fill="#a59a83">edits the protein</text>
</g>
<text x="360" y="232" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">DNA → mRNA → Protein. Each arrow is a control point.</text>
</svg>`,

L04: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hardy-Weinberg equilibrium expected genotype frequencies">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">HARDY-WEINBERG · p² + 2pq + q² = 1</text>
<g font-family="Fraunces,serif" font-style="italic">
  <text x="200" y="58" text-anchor="middle" font-size="13" fill="#a59a83">Punnett at the population level (p = 0.6, q = 0.4)</text>
  <rect x="120" y="80" width="80" height="80" fill="#0c0e12" stroke="#c89b2e"/>
  <rect x="200" y="80" width="80" height="80" fill="#0c0e12" stroke="#c89b2e"/>
  <rect x="120" y="160" width="80" height="80" fill="#0c0e12" stroke="#c89b2e"/>
  <rect x="200" y="160" width="80" height="80" fill="#0c0e12" stroke="#c89b2e"/>
  <text x="160" y="74" text-anchor="middle" font-size="13" fill="#c89b2e">A (p=0.6)</text>
  <text x="240" y="74" text-anchor="middle" font-size="13" fill="#c89b2e">a (q=0.4)</text>
  <text x="100" y="125" text-anchor="end" font-size="13" fill="#c89b2e">A (p)</text>
  <text x="100" y="205" text-anchor="end" font-size="13" fill="#c89b2e">a (q)</text>
  <text x="160" y="120" text-anchor="middle" font-size="14" fill="#e6dfd0">AA</text>
  <text x="160" y="142" text-anchor="middle" font-size="11" font-style="normal" font-family="Inter,sans-serif" fill="#5fa871">p² = .36</text>
  <text x="240" y="120" text-anchor="middle" font-size="14" fill="#e6dfd0">Aa</text>
  <text x="240" y="142" text-anchor="middle" font-size="11" font-style="normal" font-family="Inter,sans-serif" fill="#5fa871">pq = .24</text>
  <text x="160" y="200" text-anchor="middle" font-size="14" fill="#e6dfd0">Aa</text>
  <text x="160" y="222" text-anchor="middle" font-size="11" font-style="normal" font-family="Inter,sans-serif" fill="#5fa871">pq = .24</text>
  <text x="240" y="200" text-anchor="middle" font-size="14" fill="#e6dfd0">aa</text>
  <text x="240" y="222" text-anchor="middle" font-size="11" font-style="normal" font-family="Inter,sans-serif" fill="#5fa871">q² = .16</text>
</g>
<g font-family="Inter,sans-serif" font-size="11" fill="#e6dfd0">
  <text x="380" y="64" font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#a59a83">5 assumptions:</text>
  <text x="380" y="86">·  no mutation</text>
  <text x="380" y="106">·  no migration / gene flow</text>
  <text x="380" y="126">·  no genetic drift (large N)</text>
  <text x="380" y="146">·  no natural selection</text>
  <text x="380" y="166">·  random mating</text>
  <text x="380" y="200" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#c89b2e">Deviations diagnose</text>
  <text x="380" y="218" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#c89b2e">which force is acting.</text>
</g>
</svg>`,

L05: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Reaction norm with G x E interaction">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">REACTION NORMS · PLASTICITY &amp; G×E</text>
<g stroke="#6b6353" stroke-width="1">
  <line x1="100" y1="200" x2="350" y2="200"/>
  <line x1="100" y1="60" x2="100" y2="200"/>
  <line x1="420" y1="200" x2="670" y2="200"/>
  <line x1="420" y1="60" x2="420" y2="200"/>
</g>
<g font-family="Inter,sans-serif" font-size="10" fill="#a59a83">
  <text x="225" y="220" text-anchor="middle">Environment</text>
  <text x="80" y="135" transform="rotate(-90 80 135)" text-anchor="middle">Phenotype</text>
  <text x="545" y="220" text-anchor="middle">Environment</text>
  <text x="400" y="135" transform="rotate(-90 400 135)" text-anchor="middle">Phenotype</text>
</g>
<g font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#e6dfd0">
  <text x="225" y="48" text-anchor="middle">Plasticity (no G×E)</text>
  <text x="545" y="48" text-anchor="middle">G×E interaction</text>
</g>
<line x1="105" y1="180" x2="345" y2="80" stroke="#c89b2e" stroke-width="2"/>
<text x="350" y="78" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e">Genotype A</text>
<line x1="105" y1="170" x2="345" y2="100" stroke="#5fa871" stroke-width="2"/>
<text x="350" y="105" font-family="Inter,sans-serif" font-size="10" fill="#5fa871">Genotype B</text>
<text x="225" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#a59a83" font-style="italic">parallel = same response to env</text>
<line x1="425" y1="180" x2="665" y2="80" stroke="#c89b2e" stroke-width="2"/>
<text x="670" y="78" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e" text-anchor="end">A</text>
<line x1="425" y1="80" x2="665" y2="180" stroke="#5fa871" stroke-width="2"/>
<text x="670" y="195" font-family="Inter,sans-serif" font-size="10" fill="#5fa871" text-anchor="end">B</text>
<text x="545" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#c86462" font-style="italic">crossing = G×E (different slopes)</text>
</svg>`,

L07: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Galapagos finch beak depth shift after 1977 drought">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">GRANTS' FINCHES · BEAK DEPTH SHIFT (1977 DROUGHT)</text>
<g stroke="#6b6353" stroke-width="1">
  <line x1="80" y1="200" x2="660" y2="200"/>
  <line x1="80" y1="60" x2="80" y2="200"/>
</g>
<text x="370" y="220" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">beak depth (mm) →</text>
<text x="50" y="135" transform="rotate(-90 50 135)" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">birds (count)</text>
<path d="M 100 200 Q 200 90 300 200 Z" fill="#7a8fa8" fill-opacity="0.3" stroke="#7a8fa8" stroke-width="1.4"/>
<path d="M 240 200 Q 360 70 480 200 Z" fill="#c89b2e" fill-opacity="0.3" stroke="#c89b2e" stroke-width="1.4"/>
<line x1="200" y1="210" x2="200" y2="200" stroke="#7a8fa8" stroke-width="2"/>
<line x1="360" y1="210" x2="360" y2="200" stroke="#c89b2e" stroke-width="2"/>
<text x="200" y="234" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#7a8fa8">~9.4 mm (1976)</text>
<text x="360" y="234" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e">~10.1 mm (1978)</text>
<text x="180" y="80" font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#7a8fa8">before</text>
<text x="340" y="60" font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#c89b2e">after drought</text>
<text x="540" y="120" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0">drought →</text>
<text x="540" y="138" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0">large hard seeds →</text>
<text x="540" y="156" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0">deep beaks survive →</text>
<text x="540" y="178" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#5fa871">next gen has deeper beaks</text>
</svg>`,

L08: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stepwise evolution of the eye">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">STEPWISE EYE EVOLUTION · EVERY STAGE FUNCTIONAL</text>
<g font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#e6dfd0" text-anchor="middle">
  <g transform="translate(90,120)">
    <ellipse cx="0" cy="0" rx="40" ry="20" fill="#0c0e12" stroke="#a59a83" stroke-width="1"/>
    <line x1="-30" y1="0" x2="30" y2="0" stroke="#c89b2e" stroke-width="3"/>
    <text y="50">1. Patch</text>
    <text y="68" font-family="Inter,sans-serif" font-size="10" font-style="normal" fill="#a59a83">light vs dark</text>
  </g>
  <g transform="translate(230,120)">
    <path d="M -30 -10 Q 0 25 30 -10" fill="#0c0e12" stroke="#a59a83" stroke-width="1"/>
    <path d="M -25 -8 Q 0 18 25 -8" stroke="#c89b2e" stroke-width="3" fill="none"/>
    <text y="50">2. Cup</text>
    <text y="68" font-family="Inter,sans-serif" font-size="10" font-style="normal" fill="#a59a83">+ direction</text>
  </g>
  <g transform="translate(370,120)">
    <ellipse cx="0" cy="0" rx="32" ry="22" fill="#0c0e12" stroke="#a59a83" stroke-width="1"/>
    <ellipse cx="0" cy="-22" rx="3" ry="2" fill="#14171d" stroke="#a59a83"/>
    <path d="M -22 0 Q 0 18 22 0" stroke="#c89b2e" stroke-width="3" fill="none"/>
    <text y="50">3. Pinhole</text>
    <text y="68" font-family="Inter,sans-serif" font-size="10" font-style="normal" fill="#a59a83">crude image (Nautilus)</text>
  </g>
  <g transform="translate(510,120)">
    <ellipse cx="0" cy="0" rx="36" ry="26" fill="#0c0e12" stroke="#a59a83" stroke-width="1"/>
    <ellipse cx="0" cy="-12" rx="14" ry="10" fill="#7a8fa8" fill-opacity="0.4" stroke="#7a8fa8"/>
    <path d="M -26 4 Q 0 22 26 4" stroke="#c89b2e" stroke-width="3" fill="none"/>
    <text y="50">4. Lens</text>
    <text y="68" font-family="Inter,sans-serif" font-size="10" font-style="normal" fill="#a59a83">sharp focus</text>
  </g>
  <g transform="translate(640,120)">
    <ellipse cx="0" cy="0" rx="32" ry="24" fill="#0c0e12" stroke="#c89b2e" stroke-width="1.6"/>
    <ellipse cx="0" cy="-10" rx="14" ry="11" fill="#c89b2e" fill-opacity="0.3" stroke="#c89b2e"/>
    <circle cx="0" cy="-10" r="5" fill="#0c0e12" stroke="#c89b2e"/>
    <path d="M -22 6 Q 0 24 22 6" stroke="#c89b2e" stroke-width="3" fill="none"/>
    <text y="50">5. Camera</text>
    <text y="68" font-family="Inter,sans-serif" font-size="10" font-style="normal" fill="#a59a83">vertebrate / cephalopod</text>
  </g>
</g>
<g stroke="#6b6353" stroke-width="1" fill="none">
  <path d="M 130 120 L 200 120" marker-end="url(#arr8)"/>
  <path d="M 270 120 L 340 120" marker-end="url(#arr8)"/>
  <path d="M 410 120 L 480 120" marker-end="url(#arr8)"/>
  <path d="M 550 120 L 610 120" marker-end="url(#arr8)"/>
</g>
<defs><marker id="arr8" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#6b6353"/></marker></defs>
</svg>`,

L09: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coevolutionary arms race between newts and snakes">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">NEWT–SNAKE ARMS RACE · GEOGRAPHIC MOSAIC</text>
<g font-family="Fraunces,serif" font-style="italic" font-size="14" fill="#e6dfd0">
  <text x="180" y="56" text-anchor="middle">Taricha (newt)</text>
  <text x="540" y="56" text-anchor="middle">Thamnophis (snake)</text>
  <ellipse cx="180" cy="125" rx="92" ry="40" fill="#5fa871" fill-opacity="0.16" stroke="#5fa871" stroke-width="1.5"/>
  <text x="180" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">TTX toxicity</text>
  <text x="180" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#5fa871" font-style="italic">↑ when snakes resistant</text>
  <ellipse cx="540" cy="125" rx="92" ry="40" fill="#c89b2e" fill-opacity="0.16" stroke="#c89b2e" stroke-width="1.5"/>
  <text x="540" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">Na+ channel resistance</text>
  <text x="540" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#c89b2e" font-style="italic">↑ when newts toxic</text>
</g>
<path d="M 280 105 Q 360 75 440 105" stroke="#c89b2e" stroke-width="2" fill="none" marker-end="url(#arrR)"/>
<path d="M 440 145 Q 360 175 280 145" stroke="#5fa871" stroke-width="2" fill="none" marker-end="url(#arrL)"/>
<defs>
  <marker id="arrR" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#c89b2e"/></marker>
  <marker id="arrL" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#5fa871"/></marker>
</defs>
<text x="360" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#c89b2e" font-style="italic">selection on snakes</text>
<text x="360" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#5fa871" font-style="italic">selection on newts</text>
<text x="360" y="220" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#7a8fa8">Reciprocal selection. Trait values vary regionally — Thompson's geographic mosaic.</text>
</svg>`,

L11: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Anisogamy and the basis of male-female differences">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">ANISOGAMY · THE FOUNDATION OF SEX DIFFERENCES</text>
<g font-family="Fraunces,serif" font-style="italic">
  <text x="180" y="56" text-anchor="middle" font-size="14" fill="#c89b2e">Female (Egg)</text>
  <circle cx="180" cy="130" r="44" fill="#c89b2e" fill-opacity="0.18" stroke="#c89b2e" stroke-width="1.5"/>
  <text x="180" y="135" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">large, costly,</text>
  <text x="180" y="151" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-style="normal" fill="#e6dfd0">few in number</text>
  <text x="180" y="200" text-anchor="middle" font-size="12" fill="#a59a83">→ choosy, invest in offspring</text>
  <text x="540" y="56" text-anchor="middle" font-size="14" fill="#7a8fa8">Male (Sperm)</text>
  <g>
    <circle cx="510" cy="130" r="6" fill="#7a8fa8"/><circle cx="525" cy="120" r="6" fill="#7a8fa8"/>
    <circle cx="540" cy="135" r="6" fill="#7a8fa8"/><circle cx="555" cy="125" r="6" fill="#7a8fa8"/>
    <circle cx="570" cy="138" r="6" fill="#7a8fa8"/><circle cx="500" cy="145" r="6" fill="#7a8fa8"/>
    <circle cx="555" cy="148" r="6" fill="#7a8fa8"/><circle cx="525" cy="150" r="6" fill="#7a8fa8"/>
  </g>
  <text x="540" y="200" text-anchor="middle" font-size="12" fill="#a59a83">→ compete, chase quantity</text>
</g>
<text x="360" y="232" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#5fa871">Different gamete sizes → different reproductive strategies → sexual dimorphism &amp; conflict.</text>
</svg>`,

L12: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Life history trade-offs and extrinsic mortality">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">LIFE HISTORY · EXTRINSIC MORTALITY → STRATEGY</text>
<g stroke="#6b6353" stroke-width="1">
  <line x1="80" y1="200" x2="660" y2="200"/>
  <line x1="80" y1="60" x2="80" y2="200"/>
</g>
<text x="370" y="222" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">extrinsic mortality (predation, disease) →</text>
<text x="55" y="135" transform="rotate(-90 55 135)" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">age at first reproduction</text>
<path d="M 100 80 Q 300 95 400 130 Q 500 170 660 195" stroke="#c89b2e" stroke-width="2" fill="none"/>
<circle cx="170" cy="92" r="4" fill="#c89b2e"/>
<text x="180" y="86" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0">elephants</text>
<text x="180" y="100" font-family="Inter,sans-serif" font-size="9" fill="#a59a83">low predation, late, few</text>
<circle cx="600" cy="190" r="4" fill="#c86462"/>
<text x="590" y="184" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0" text-anchor="end">mice</text>
<text x="590" y="172" font-family="Inter,sans-serif" font-size="9" fill="#a59a83" text-anchor="end">high predation, early, many</text>
<text x="370" y="60" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#7a8fa8">High extrinsic mortality favors fast life history.</text>
</svg>`,

L13: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hamiltons rule and rock paper scissors lizard morphs">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">HAMILTON'S RULE · rB &gt; C · &amp; ROCK-PAPER-SCISSORS</text>
<g font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#e6dfd0">
  <text x="160" y="60" text-anchor="middle" fill="#c89b2e">Hamilton's rule</text>
  <rect x="60" y="80" width="220" height="120" fill="#0c0e12" stroke="#c89b2e" stroke-width="1.4" rx="6"/>
  <text x="170" y="120" text-anchor="middle" font-size="22" fill="#e6dfd0">r · B &gt; C</text>
  <text x="170" y="148" text-anchor="middle" font-size="10" font-family="Inter,sans-serif" font-style="normal" fill="#a59a83">r = relatedness</text>
  <text x="170" y="164" text-anchor="middle" font-size="10" font-family="Inter,sans-serif" font-style="normal" fill="#a59a83">B = benefit to recipient</text>
  <text x="170" y="180" text-anchor="middle" font-size="10" font-family="Inter,sans-serif" font-style="normal" fill="#a59a83">C = cost to actor</text>

  <text x="540" y="60" text-anchor="middle" fill="#c89b2e">Rock–paper–scissors (Uta)</text>
  <g transform="translate(540,140)">
    <circle cx="0" cy="-40" r="25" fill="#c89b2e" fill-opacity="0.3" stroke="#c89b2e" stroke-width="1.4"/>
    <text y="-36" text-anchor="middle" font-size="11" fill="#c89b2e" font-family="Inter,sans-serif" font-style="normal">Orange</text>
    <circle cx="-46" cy="20" r="25" fill="#7a8fa8" fill-opacity="0.3" stroke="#7a8fa8" stroke-width="1.4"/>
    <text x="-46" y="24" text-anchor="middle" font-size="11" fill="#7a8fa8" font-family="Inter,sans-serif" font-style="normal">Blue</text>
    <circle cx="46" cy="20" r="25" fill="#c8a82e" fill-opacity="0.3" stroke="#c8a82e" stroke-width="1.4"/>
    <text x="46" y="24" text-anchor="middle" font-size="11" fill="#c8a82e" font-family="Inter,sans-serif" font-style="normal">Yellow</text>
    <path d="M -10 -25 L -36 5" stroke="#c89b2e" stroke-width="1.4" fill="none" marker-end="url(#arr13)"/>
    <path d="M -25 30 L 25 30" stroke="#7a8fa8" stroke-width="1.4" fill="none" marker-end="url(#arr13)"/>
    <path d="M 36 5 L 10 -25" stroke="#c8a82e" stroke-width="1.4" fill="none" marker-end="url(#arr13)"/>
  </g>
</g>
<defs><marker id="arr13" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#a59a83"/></marker></defs>
<text x="360" y="232" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#a59a83">Frequency-dependent selection · no single strategy wins.</text>
</svg>`,

L14: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Geological timeline of life">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">HISTORY OF LIFE · KEY MILESTONES</text>
<line x1="60" y1="130" x2="660" y2="130" stroke="#c89b2e" stroke-width="2"/>
<g font-family="Fraunces,serif" font-style="italic" font-size="11" fill="#e6dfd0" text-anchor="middle">
  <circle cx="80" cy="130" r="5" fill="#c89b2e"/>
  <text x="80" y="105">4.6 GYa</text>
  <text x="80" y="158" font-family="Inter,sans-serif" font-size="9" fill="#a59a83">Earth forms</text>
  <circle cx="180" cy="130" r="5" fill="#5fa871"/>
  <text x="180" y="105">~3.8 GYa</text>
  <text x="180" y="158" font-family="Inter,sans-serif" font-size="9" fill="#a59a83">first life</text>
  <circle cx="280" cy="130" r="5" fill="#5fa871"/>
  <text x="280" y="105">2.4 GYa</text>
  <text x="280" y="158" font-family="Inter,sans-serif" font-size="9" fill="#a59a83">Great Oxidation</text>
  <circle cx="380" cy="130" r="5" fill="#5fa871"/>
  <text x="380" y="105">541 MYa</text>
  <text x="380" y="158" font-family="Inter,sans-serif" font-size="9" fill="#a59a83">Cambrian explosion</text>
  <circle cx="470" cy="130" r="5" fill="#c86462"/>
  <text x="470" y="105">252 MYa</text>
  <text x="470" y="158" font-family="Inter,sans-serif" font-size="9" fill="#c86462">end-Permian (95% loss)</text>
  <circle cx="570" cy="130" r="5" fill="#c86462"/>
  <text x="570" y="105">66 MYa</text>
  <text x="570" y="158" font-family="Inter,sans-serif" font-size="9" fill="#c86462">K-Pg (asteroid)</text>
  <circle cx="650" cy="130" r="5" fill="#c89b2e"/>
  <text x="650" y="105">~300 KYa</text>
  <text x="650" y="158" font-family="Inter,sans-serif" font-size="9" fill="#c89b2e">H. sapiens</text>
</g>
<text x="360" y="210" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#7a8fa8">Five mass extinctions punctuate the Phanerozoic — each reset the trajectory of life.</text>
</svg>`,

L15: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Phylogenetic tree with synapomorphies and clades">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">PHYLOGENETIC TREE · CLADE = ANCESTOR + ALL DESCENDANTS</text>
<g stroke="#a59a83" stroke-width="1.6" fill="none">
  <path d="M 100 200 L 200 130 L 300 200" />
  <path d="M 200 130 L 300 80 L 400 200" />
  <path d="M 300 80 L 400 60 L 500 200" />
  <path d="M 400 60 L 500 50 L 600 200" />
</g>
<g font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#e6dfd0" text-anchor="middle">
  <circle cx="100" cy="200" r="4" fill="#7a8fa8"/><text x="100" y="222">Lamprey</text>
  <circle cx="300" cy="200" r="4" fill="#7a8fa8"/><text x="300" y="222">Shark</text>
  <circle cx="400" cy="200" r="4" fill="#7a8fa8"/><text x="400" y="222">Frog</text>
  <circle cx="500" cy="200" r="4" fill="#7a8fa8"/><text x="500" y="222">Lizard</text>
  <circle cx="600" cy="200" r="4" fill="#7a8fa8"/><text x="600" y="222">Mouse</text>
</g>
<g font-family="Inter,sans-serif" font-size="9" fill="#c89b2e">
  <text x="180" y="155">vertebral column</text>
  <text x="280" y="105">jaws</text>
  <text x="380" y="80">limbs</text>
  <text x="480" y="60">amniotic egg</text>
</g>
<g>
  <circle cx="200" cy="130" r="3" fill="#c89b2e"/>
  <circle cx="300" cy="80" r="3" fill="#c89b2e"/>
  <circle cx="400" cy="60" r="3" fill="#c89b2e"/>
  <circle cx="500" cy="50" r="3" fill="#c89b2e"/>
</g>
<text x="450" y="120" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="11" fill="#5fa871">amniotes (clade)</text>
<rect x="380" y="42" width="240" height="170" fill="none" stroke="#5fa871" stroke-dasharray="3,3" stroke-width="1"/>
<text x="100" y="80" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">tips = taxa · nodes = ancestors · marks = synapomorphies</text>
</svg>`,

L16: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pre and postzygotic reproductive isolation barriers">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">REPRODUCTIVE ISOLATION · PRE- vs POSTZYGOTIC</text>
<line x1="80" y1="130" x2="660" y2="130" stroke="#6b6353" stroke-width="1"/>
<circle cx="370" cy="130" r="22" fill="#c89b2e" fill-opacity="0.25" stroke="#c89b2e"/>
<text x="370" y="135" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#c89b2e">zygote</text>
<g font-family="Inter,sans-serif" font-size="10" fill="#e6dfd0">
  <text x="160" y="62" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="14" fill="#7a8fa8">PREZYGOTIC</text>
  <text x="160" y="80" text-anchor="middle" font-size="9" fill="#a59a83">acts BEFORE fertilization</text>
  <text x="160" y="106">·  temporal (different seasons)</text>
  <text x="160" y="124">·  behavioral (mating displays)</text>
  <text x="160" y="142">·  mechanical (genitalia mismatch)</text>
  <text x="160" y="160">·  gametic (sperm-egg incompat.)</text>
  <text x="160" y="178">·  habitat (different microenv)</text>

  <text x="580" y="62" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="14" fill="#c86462">POSTZYGOTIC</text>
  <text x="580" y="80" text-anchor="middle" font-size="9" fill="#a59a83">acts AFTER fertilization</text>
  <text x="580" y="106">·  hybrid inviability</text>
  <text x="580" y="124">·  hybrid sterility (mules)</text>
  <text x="580" y="142">·  hybrid breakdown (F2)</text>
  <text x="580" y="160" font-style="italic" fill="#a59a83">— hybrids form, but fitness ↓</text>
</g>
<path d="M 270 130 L 345 130" stroke="#7a8fa8" stroke-width="1.4" marker-end="url(#arr16)"/>
<path d="M 395 130 L 470 130" stroke="#c86462" stroke-width="1.4" marker-end="url(#arr16)"/>
<defs><marker id="arr16" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#a59a83"/></marker></defs>
<text x="360" y="220" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#5fa871">Reproductive isolation = the criterion of the Biological Species Concept (Mayr).</text>
</svg>`,

L17: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vicariance vs dispersal as biogeographic processes">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">BIOGEOGRAPHY · VICARIANCE vs DISPERSAL</text>
<g font-family="Fraunces,serif" font-style="italic" font-size="13" fill="#e6dfd0">
  <text x="180" y="56" text-anchor="middle" fill="#c89b2e">Vicariance</text>
  <text x="180" y="74" text-anchor="middle" font-size="10" font-family="Inter,sans-serif" font-style="normal" fill="#a59a83">barrier splits a continuous range</text>
  <ellipse cx="135" cy="125" rx="35" ry="25" fill="#5fa871" fill-opacity="0.3" stroke="#5fa871"/>
  <ellipse cx="225" cy="125" rx="35" ry="25" fill="#7a8fa8" fill-opacity="0.3" stroke="#7a8fa8"/>
  <line x1="180" y1="92" x2="180" y2="158" stroke="#c89b2e" stroke-width="2.5" stroke-dasharray="4,2"/>
  <text x="180" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e" font-style="italic">↑ new barrier</text>

  <text x="540" y="56" text-anchor="middle" fill="#c89b2e">Dispersal</text>
  <text x="540" y="74" text-anchor="middle" font-size="10" font-family="Inter,sans-serif" font-style="normal" fill="#a59a83">organisms cross existing barrier</text>
  <ellipse cx="500" cy="125" rx="35" ry="25" fill="#5fa871" fill-opacity="0.3" stroke="#5fa871"/>
  <ellipse cx="600" cy="125" rx="35" ry="25" fill="#5fa871" fill-opacity="0.18" stroke="#5fa871" stroke-dasharray="3,2"/>
  <path d="M 530 125 L 575 125" stroke="#c89b2e" stroke-width="2" fill="none" marker-end="url(#arr17)"/>
  <text x="540" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#c89b2e" font-style="italic">→ founder event</text>
</g>
<defs><marker id="arr17" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L7,4 L0,8 Z" fill="#c89b2e"/></marker></defs>
<text x="360" y="216" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#5fa871">Date the lineage split + the geological barrier formation to distinguish them.</text>
</svg>`,

L18: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Inbreeding depression and genetic rescue">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">SMALL POPULATIONS · INBREEDING DEPRESSION → GENETIC RESCUE</text>
<g stroke="#6b6353" stroke-width="1">
  <line x1="80" y1="200" x2="660" y2="200"/>
  <line x1="80" y1="50" x2="80" y2="200"/>
</g>
<text x="370" y="222" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">time →</text>
<text x="55" y="125" transform="rotate(-90 55 125)" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">fitness</text>
<path d="M 100 80 L 250 80 L 380 170 L 450 175" stroke="#c86462" stroke-width="2.4" fill="none"/>
<path d="M 450 175 Q 500 110 660 90" stroke="#5fa871" stroke-width="2.4" fill="none"/>
<circle cx="100" cy="80" r="4" fill="#7a8fa8"/>
<text x="100" y="68" font-family="Inter,sans-serif" font-size="10" fill="#7a8fa8">large pop</text>
<circle cx="280" cy="100" r="4" fill="#c86462"/>
<text x="280" y="88" font-family="Inter,sans-serif" font-size="10" fill="#c86462">fragmentation</text>
<circle cx="420" cy="172" r="4" fill="#c86462"/>
<text x="420" y="160" font-family="Inter,sans-serif" font-size="10" fill="#c86462">inbreeding</text>
<text x="420" y="190" font-family="Inter,sans-serif" font-size="10" fill="#c86462">depression</text>
<circle cx="450" cy="175" r="6" fill="#c89b2e" stroke="#c89b2e" stroke-width="2"/>
<text x="450" y="158" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#c89b2e" text-anchor="middle">genetic rescue</text>
<circle cx="600" cy="100" r="4" fill="#5fa871"/>
<text x="600" y="88" font-family="Inter,sans-serif" font-size="10" fill="#5fa871">recovered fitness</text>
</svg>`,

L19: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hominin family tree from chimp split to modern humans">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">HOMININ LINEAGE · 7 MYa → TODAY</text>
<g stroke="#a59a83" stroke-width="1.6" fill="none">
  <path d="M 80 200 L 150 130 L 250 200"/>
  <path d="M 150 130 L 230 100 L 320 200"/>
  <path d="M 230 100 L 310 80 L 380 200"/>
  <path d="M 310 80 L 400 65 L 460 200"/>
  <path d="M 400 65 L 500 50 L 540 200"/>
  <path d="M 500 50 L 580 40 L 600 200"/>
  <path d="M 580 40 L 660 30 L 660 200"/>
</g>
<g font-family="Fraunces,serif" font-style="italic" font-size="10" fill="#e6dfd0" text-anchor="middle">
  <text x="80" y="222">chimp</text>
  <text x="250" y="222" font-size="9">Sahelanthropus</text>
  <text x="320" y="222" font-size="9">Ardipithecus</text>
  <text x="380" y="222" font-size="9">A. afarensis</text>
  <text x="460" y="222" font-size="9">H. habilis</text>
  <text x="540" y="222" font-size="9">H. erectus</text>
  <text x="600" y="222" font-size="9">Neanderthal</text>
  <text x="660" y="222" font-size="9" fill="#c89b2e">H. sapiens</text>
</g>
<g font-family="Inter,sans-serif" font-size="9" fill="#c89b2e">
  <text x="155" y="124">bipedalism</text>
  <text x="245" y="92">stone tools</text>
  <text x="335" y="74">brain ↑</text>
  <text x="425" y="58">out of Africa</text>
  <text x="515" y="44">modern humans</text>
</g>
<g>
  <circle cx="150" cy="130" r="3" fill="#c89b2e"/>
  <circle cx="230" cy="100" r="3" fill="#c89b2e"/>
  <circle cx="310" cy="80" r="3" fill="#c89b2e"/>
  <circle cx="400" cy="65" r="3" fill="#c89b2e"/>
  <circle cx="500" cy="50" r="3" fill="#c89b2e"/>
</g>
<text x="80" y="62" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">~7 MYa: chimp split</text>
</svg>`,

L20: `<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Virulence-transmission trade-off">
<rect width="720" height="240" fill="#14171d" rx="6"/>
<text x="360" y="22" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" letter-spacing="2.4" fill="#a59a83">VIRULENCE–TRANSMISSION TRADE-OFF · MODE OF TRANSMISSION SHAPES OPTIMUM</text>
<g stroke="#6b6353" stroke-width="1">
  <line x1="80" y1="200" x2="660" y2="200"/>
  <line x1="80" y1="50" x2="80" y2="200"/>
</g>
<text x="370" y="222" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">virulence (host damage) →</text>
<text x="55" y="125" transform="rotate(-90 55 125)" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#a59a83">total transmission</text>
<path d="M 90 180 Q 200 70 350 70 Q 470 70 660 195" stroke="#c89b2e" stroke-width="2" fill="none" stroke-opacity="0.5"/>
<path d="M 90 180 Q 220 110 280 105 Q 350 100 580 195" stroke="#5fa871" stroke-width="2" fill="none"/>
<path d="M 90 180 Q 280 115 400 90 Q 520 70 660 95" stroke="#c86462" stroke-width="2" fill="none"/>
<text x="280" y="100" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#5fa871" text-anchor="middle">direct transmission</text>
<text x="280" y="116" font-family="Inter,sans-serif" font-size="9" fill="#5fa871" text-anchor="middle">(common cold)</text>
<text x="490" y="92" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#c86462" text-anchor="middle">vector / waterborne</text>
<text x="490" y="108" font-family="Inter,sans-serif" font-size="9" fill="#c86462" text-anchor="middle">(malaria, cholera)</text>
<circle cx="280" cy="105" r="5" fill="#5fa871"/>
<circle cx="500" cy="76" r="5" fill="#c86462"/>
<text x="360" y="58" text-anchor="middle" font-family="Fraunces,serif" font-style="italic" font-size="12" fill="#7a8fa8">Optimal virulence ≠ benign. Depends on whether host mobility matters for transmission.</text>
</svg>`

};

console.log('[diagrams loaded]', Object.keys(window.LECTURE_DIAGRAMS).length, 'lecture diagrams');
