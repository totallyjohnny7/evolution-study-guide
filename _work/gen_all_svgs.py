#!/usr/bin/env python3
"""Generate all concept-specific SVG diagrams for evolution flashcards."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = "C:/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide/public/img/fc"
os.makedirs(OUT, exist_ok=True)

# SVG wrapper constants
VB = 'viewBox="0 0 240 150" width="240" height="150" xmlns="http://www.w3.org/2000/svg"'
BG = '<rect width="240" height="150" fill="#0a1220"/>'
# Font shorthand
FT = 'font-family="system-ui,Segoe UI,sans-serif"'

def W(name, body):
    path = os.path.join(OUT, f"svg_{name}.svg")
    svg = f'<svg {VB}>{BG}{body}</svg>'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

# Title helper
def T(text, y=14):
    return f'<text x="120" y="{y}" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="700" {FT}>{text}</text>'

def S(text, y=26, color="#94a3b8"):
    return f'<text x="120" y="{y}" text-anchor="middle" fill="{color}" font-size="9" {FT}>{text}</text>'

# =========================================================================
# GROUP A — HISTORY OF LIFE / DATING
# =========================================================================

W("earth_clock", T("EARTH'S HISTORY = 24-HOUR CLOCK") + S("Humans = last 2 seconds before midnight") + '''
<circle cx="120" cy="87" r="45" fill="#111827" stroke="#60a5fa" stroke-width="2"/>
<g stroke="#475569" stroke-width="1">
<line x1="120" y1="42" x2="120" y2="48"/>
<line x1="120" y1="126" x2="120" y2="132"/>
<line x1="75" y1="87" x2="81" y2="87"/>
<line x1="159" y1="87" x2="165" y2="87"/>
</g>
<path d="M120 87 L120 42 A45 45 0 0 1 161 95 Z" fill="#1e3a5f" opacity="0.7"/>
<path d="M161 94 L163 94 A45 45 0 0 1 162 99 Z" fill="#ef4444"/>
<line x1="120" y1="87" x2="120" y2="50" stroke="#e2e8f0" stroke-width="2.5" stroke-linecap="round"/>
<line x1="120" y1="87" x2="156" y2="93" stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round"/>
<circle cx="120" cy="87" r="3" fill="#fbbf24"/>
<text x="80" y="65" fill="#93c5fd" font-size="8" ''' + FT + '''>Bacteria</text>
<text x="145" y="60" fill="#86efac" font-size="8" ''' + FT + '''>Animals</text>
<text x="170" y="92" fill="#ef4444" font-size="8" font-weight="700" ''' + FT + '''>Humans</text>
<text x="120" y="145" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>4.568 billion years total</text>
''')

W("decay_curve", T("RADIOMETRIC DECAY") + '''
<line x1="30" y1="30" x2="30" y2="130" stroke="#475569" stroke-width="1.5"/>
<line x1="30" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.5"/>
<text x="8" y="34" fill="#94a3b8" font-size="7" ''' + FT + '''>100%</text>
<text x="12" y="80" fill="#94a3b8" font-size="7" ''' + FT + '''>50%</text>
<text x="12" y="105" fill="#94a3b8" font-size="7" ''' + FT + '''>25%</text>
<polyline points="30,30 75,80 120,105 165,118 210,124" fill="none" stroke="#ef4444" stroke-width="2.5"/>
<polyline points="30,130 75,80 120,55 165,42 210,36" fill="none" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="4,3"/>
<line x1="75" y1="80" x2="75" y2="130" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2"/>
<line x1="120" y1="105" x2="120" y2="130" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2"/>
<text x="73" y="142" text-anchor="middle" fill="#fbbf24" font-size="8" ''' + FT + '''>t½</text>
<text x="118" y="142" text-anchor="middle" fill="#fbbf24" font-size="8" ''' + FT + '''>2t½</text>
<rect x="155" y="32" width="8" height="3" fill="#ef4444"/>
<text x="166" y="36" fill="#fca5a5" font-size="8" ''' + FT + '''>Parent</text>
<rect x="155" y="42" width="8" height="3" fill="#60a5fa"/>
<text x="166" y="46" fill="#93c5fd" font-size="8" ''' + FT + '''>Daughter</text>
''')

W("halflife", T("HALF-LIFE") + S("50% of parent decays each half-life") + '''
<rect x="30" y="45" width="30" height="75" fill="#ef4444" rx="2"/>
<text x="45" y="135" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>0</text>
<text x="45" y="42" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>100%</text>
<rect x="80" y="82" width="30" height="38" fill="#ef4444" rx="2"/>
<text x="95" y="135" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>t½</text>
<text x="95" y="78" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>50%</text>
<rect x="130" y="101" width="30" height="19" fill="#ef4444" rx="2"/>
<text x="145" y="135" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>2t½</text>
<text x="145" y="97" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>25%</text>
<rect x="180" y="110" width="30" height="10" fill="#ef4444" rx="2"/>
<text x="195" y="135" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>3t½</text>
<text x="195" y="107" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>12.5%</text>
<line x1="20" y1="122" x2="220" y2="122" stroke="#334155" stroke-width="1"/>
<text x="120" y="147" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>Constant rate — independent of T, P, chemistry</text>
''')

W("isotopes", T("ISOTOPES") + S("Same element · different neutron count") + '''
<circle cx="65" cy="85" r="30" fill="none" stroke="#60a5fa" stroke-width="1" stroke-dasharray="3,2"/>
<circle cx="65" cy="85" r="13" fill="#1e3a5f"/>
<text x="65" y="89" text-anchor="middle" fill="#93c5fd" font-size="10" font-weight="700" ''' + FT + '''>¹²C</text>
<circle cx="50" cy="60" r="2" fill="#60a5fa"/><circle cx="80" cy="60" r="2" fill="#60a5fa"/>
<circle cx="90" cy="90" r="2" fill="#60a5fa"/><circle cx="40" cy="95" r="2" fill="#60a5fa"/>
<text x="65" y="128" text-anchor="middle" fill="#60a5fa" font-size="8" ''' + FT + '''>6p + 6n</text>
<text x="65" y="140" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>STABLE</text>
<text x="120" y="92" text-anchor="middle" fill="#475569" font-size="16" ''' + FT + '''>≠</text>
<circle cx="175" cy="85" r="32" fill="none" stroke="#ef4444" stroke-width="1" stroke-dasharray="3,2"/>
<circle cx="175" cy="85" r="15" fill="#3b1515"/>
<text x="175" y="89" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="700" ''' + FT + '''>¹⁴C</text>
<circle cx="160" cy="58" r="2" fill="#ef4444"/><circle cx="190" cy="58" r="2" fill="#ef4444"/>
<circle cx="200" cy="90" r="2" fill="#ef4444"/><circle cx="150" cy="95" r="2" fill="#ef4444"/>
<text x="175" y="128" text-anchor="middle" fill="#ef4444" font-size="8" ''' + FT + '''>6p + 8n</text>
<text x="175" y="140" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700" ''' + FT + '''>RADIOACTIVE</text>
''')

W("biomarkers", T("BIOMARKERS") + S("Chemical fingerprints of ancient life") + '''
<rect x="20" y="40" width="200" height="18" fill="#292524" rx="2"/>
<text x="25" y="53" fill="#a8a29e" font-size="8" ''' + FT + '''>Modern sediment</text>
<rect x="20" y="60" width="200" height="22" fill="#1c1917" rx="2"/>
<polygon points="65,70 72,66 79,70 79,76 72,80 65,76" fill="#7c3aed"/>
<polygon points="95,70 102,66 109,70 109,76 102,80 95,76" fill="#7c3aed"/>
<polygon points="125,70 132,66 139,70 139,76 132,80 125,76" fill="#7c3aed"/>
<text x="155" y="74" fill="#c4b5fd" font-size="8" ''' + FT + '''>Okenane</text>
<text x="155" y="82" fill="#94a3b8" font-size="7" ''' + FT + '''>1.64 bya layer</text>
<rect x="20" y="84" width="200" height="18" fill="#14110f" rx="2"/>
<text x="25" y="97" fill="#57534e" font-size="8" ''' + FT + '''>Older sediment</text>
<text x="120" y="118" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" ''' + FT + '''>Must be: specific · stable · biological</text>
<text x="120" y="132" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>Okenane → purple sulfur bacteria (1.64 bya)</text>
''')

W("stromatolites", T("STROMATOLITES") + '''
<rect x="20" y="40" width="200" height="5" fill="#1e40af" opacity="0.6"/>
<ellipse cx="70" cy="85" rx="28" ry="42" fill="#292524"/>
<ellipse cx="70" cy="95" rx="22" ry="10" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<ellipse cx="70" cy="105" rx="22" ry="8" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<ellipse cx="70" cy="113" rx="22" ry="6" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<ellipse cx="70" cy="45" rx="24" ry="4" fill="#166534"/>
<text x="70" y="32" text-anchor="middle" fill="#86efac" font-size="8" ''' + FT + '''>microbial mat</text>
<ellipse cx="160" cy="80" rx="24" ry="37" fill="#292524"/>
<ellipse cx="160" cy="88" rx="18" ry="9" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<ellipse cx="160" cy="98" rx="18" ry="7" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<ellipse cx="160" cy="45" rx="20" ry="4" fill="#166534"/>
<text x="120" y="130" text-anchor="middle" fill="#86efac" font-size="9" ''' + FT + '''>Fossil record: 3.45 bya</text>
<text x="120" y="142" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>Modern: Shark Bay, Australia</text>
''')

W("kt_boundary", T("K-T / K-Pg BOUNDARY 66 mya") + '''
<rect x="20" y="28" width="200" height="30" fill="#1a1a2e" rx="2"/>
<text x="120" y="47" text-anchor="middle" fill="#60a5fa" font-size="9" ''' + FT + '''>Paleogene (mammals, birds)</text>
<rect x="20" y="60" width="200" height="7" fill="#ca8a04"/>
<text x="120" y="66" text-anchor="middle" fill="#000" font-size="8" font-weight="700" ''' + FT + '''>IRIDIUM LAYER ★</text>
<rect x="20" y="69" width="200" height="30" fill="#1c1917" rx="2"/>
<text x="120" y="88" text-anchor="middle" fill="#d97706" font-size="9" ''' + FT + '''>Cretaceous (dinosaurs)</text>
<circle cx="195" cy="22" r="8" fill="#6b7280"/>
<text x="195" y="25" text-anchor="middle" fill="#f3f4f6" font-size="8" ''' + FT + '''>☄</text>
<line x1="190" y1="28" x2="155" y2="58" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2"/>
<text x="120" y="116" text-anchor="middle" fill="#94a3b8" font-size="9" ''' + FT + '''>Chicxulub · ~100 trillion tons TNT</text>
<text x="120" y="130" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="700" ''' + FT + '''>Killed 2/3 of all species</text>
<text x="120" y="143" text-anchor="middle" fill="#64748b" font-size="7" ''' + FT + '''>Iridium = extraterrestrial marker</text>
''')

W("rna_world", T("RNA WORLD HYPOTHESIS") + '''
<ellipse cx="120" cy="80" rx="32" ry="20" fill="#7c3aed" opacity="0.7"/>
<text x="120" y="84" text-anchor="middle" fill="#e9d5ff" font-size="13" font-weight="700" ''' + FT + '''>RNA</text>
<path d="M90 72 Q55 52 50 40" fill="none" stroke="#86efac" stroke-width="2"/>
<polygon points="50,40 54,45 46,45" fill="#86efac"/>
<text x="20" y="32" fill="#86efac" font-size="9" font-weight="700" ''' + FT + '''>Information</text>
<text x="20" y="43" fill="#86efac" font-size="7" ''' + FT + '''>storage (like DNA)</text>
<path d="M150 72 Q185 52 190 40" fill="none" stroke="#f9a8d4" stroke-width="2"/>
<polygon points="190,40 186,45 194,45" fill="#f9a8d4"/>
<text x="160" y="32" fill="#f9a8d4" font-size="9" font-weight="700" ''' + FT + '''>Catalysis</text>
<text x="160" y="43" fill="#f9a8d4" font-size="7" ''' + FT + '''>(ribozyme)</text>
<text x="120" y="118" text-anchor="middle" fill="#c4b5fd" font-size="9" ''' + FT + '''>Swiss Army knife molecule</text>
<text x="120" y="132" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Predates DNA + proteins</text>
''')

W("luca", T("LUCA — Last Universal Common Ancestor") + '''
<rect x="114" y="95" width="12" height="40" fill="#92400e" rx="3"/>
<line x1="120" y1="95" x2="55" y2="50" stroke="#92400e" stroke-width="3" stroke-linecap="round"/>
<line x1="120" y1="95" x2="120" y2="45" stroke="#92400e" stroke-width="3" stroke-linecap="round"/>
<line x1="120" y1="95" x2="185" y2="50" stroke="#92400e" stroke-width="3" stroke-linecap="round"/>
<circle cx="55" cy="42" r="14" fill="#1e3a5f"/>
<text x="55" y="46" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" ''' + FT + '''>BACTERIA</text>
<circle cx="120" cy="37" r="14" fill="#1a1a2e"/>
<text x="120" y="41" text-anchor="middle" fill="#a78bfa" font-size="8" font-weight="700" ''' + FT + '''>ARCHAEA</text>
<circle cx="185" cy="42" r="14" fill="#14532d"/>
<text x="185" y="46" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>EUKARYA</text>
<text x="120" y="112" text-anchor="middle" fill="#fbbf24" font-size="9" font-weight="700" ''' + FT + '''>LUCA ~3.8 bya</text>
<text x="120" y="145" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Universal genetic code · shared metabolism</text>
''')

W("endosymbiosis", T("ENDOSYMBIOTIC THEORY") + '''
<ellipse cx="42" cy="80" rx="28" ry="22" fill="#1e3a5f" stroke="#60a5fa" stroke-width="1.5"/>
<text x="42" y="76" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>proto-</text>
<text x="42" y="86" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>eukaryote</text>
<ellipse cx="42" cy="115" rx="11" ry="6" fill="#16a34a"/>
<text x="42" y="118" text-anchor="middle" fill="#dcfce7" font-size="6" ''' + FT + '''>α-proteo</text>
<text x="85" y="85" fill="#94a3b8" font-size="18" ''' + FT + '''>→</text>
<ellipse cx="130" cy="80" rx="32" ry="25" fill="#1e3a5f" stroke="#60a5fa" stroke-width="1.5"/>
<ellipse cx="135" cy="88" rx="12" ry="8" fill="#16a34a" stroke="#22c55e"/>
<text x="130" y="54" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>engulfed</text>
<text x="172" y="85" fill="#94a3b8" font-size="18" ''' + FT + '''>→</text>
<ellipse cx="210" cy="80" rx="15" ry="15" fill="#1e3a5f" stroke="#60a5fa" stroke-width="1.5"/>
<ellipse cx="213" cy="83" rx="5" ry="3" fill="#16a34a"/>
<text x="210" y="108" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>mito</text>
<text x="120" y="133" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Evidence: 2× membrane · own DNA · 70S ribos</text>
''')

W("oxygenation", T("GREAT OXYGENATION EVENT") + S("~2.4 bya — cyanobacteria polluted the sky") + '''
<line x1="20" y1="95" x2="220" y2="95" stroke="#334155" stroke-width="1"/>
<text x="20" y="108" fill="#64748b" font-size="7" ''' + FT + '''>4.5 bya</text>
<text x="205" y="108" fill="#64748b" font-size="7" ''' + FT + '''>now</text>
<polyline points="20,93 80,93 100,68 130,50 160,42 220,38" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
<line x1="100" y1="68" x2="100" y2="108" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2"/>
<text x="100" y="118" text-anchor="middle" fill="#fbbf24" font-size="8" ''' + FT + '''>2.4 bya</text>
<text x="100" y="128" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" ''' + FT + '''>GOE</text>
<circle cx="75" cy="60" r="5" fill="#166534"/>
<circle cx="70" cy="50" r="3" fill="#60a5fa" opacity="0.7"/>
<circle cx="82" cy="46" r="2.5" fill="#60a5fa" opacity="0.7"/>
<text x="73" y="42" fill="#93c5fd" font-size="7" ''' + FT + '''>O₂</text>
<text x="120" y="143" text-anchor="middle" fill="#86efac" font-size="8" ''' + FT + '''>Enabled aerobic respiration</text>
''')

W("cambrian", T("CAMBRIAN EXPLOSION ~541 mya") + '''
<line x1="30" y1="120" x2="210" y2="120" stroke="#334155" stroke-width="1.5"/>
<line x1="30" y1="120" x2="80" y2="120" stroke="#60a5fa" stroke-width="2"/>
<circle cx="80" cy="120" r="4" fill="#fbbf24"/>
<text x="80" y="133" text-anchor="middle" fill="#fbbf24" font-size="8" ''' + FT + '''>541 mya</text>
<g stroke="#86efac" stroke-width="1.5" fill="none">
<line x1="80" y1="120" x2="110" y2="70"/>
<line x1="80" y1="120" x2="120" y2="55"/>
<line x1="80" y1="120" x2="135" y2="48"/>
<line x1="80" y1="120" x2="150" y2="55"/>
<line x1="80" y1="120" x2="160" y2="70"/>
<line x1="80" y1="120" x2="165" y2="85"/>
<line x1="80" y1="120" x2="163" y2="100"/>
<line x1="80" y1="120" x2="105" y2="85"/>
</g>
<text x="105" y="65" fill="#86efac" font-size="7" ''' + FT + '''>Arthro</text>
<text x="115" y="50" fill="#86efac" font-size="7" ''' + FT + '''>Mollusc</text>
<text x="135" y="43" fill="#86efac" font-size="7" ''' + FT + '''>Chordata</text>
<text x="148" y="52" fill="#86efac" font-size="7" ''' + FT + '''>Echino</text>
<text x="158" y="68" fill="#86efac" font-size="7" ''' + FT + '''>Annelid</text>
<text x="15" y="105" fill="#64748b" font-size="7" ''' + FT + '''>Precambrian</text>
<text x="120" y="145" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Most animal phyla appear in ~20 Myr</text>
''')

W("tiktaalik", T("TIKTAALIK — The Fishapod (375 mya)") + '''
<ellipse cx="110" cy="85" rx="65" ry="22" fill="#1c4332" stroke="#22c55e" stroke-width="1.5"/>
<ellipse cx="50" cy="82" rx="20" ry="16" fill="#1c4332" stroke="#22c55e" stroke-width="1.5"/>
<circle cx="43" cy="77" r="3" fill="#fbbf24"/>
<path d="M175 85 L195 70 L195 100 Z" fill="#166534" stroke="#22c55e" stroke-width="1"/>
<path d="M75 95 Q65 110 60 115 Q70 115 82 107 Z" fill="#166534" stroke="#22c55e"/>
<path d="M130 95 Q120 110 115 118 Q125 118 138 110 Z" fill="#166534" stroke="#22c55e"/>
<text x="68" y="125" text-anchor="middle" fill="#86efac" font-size="8" ''' + FT + '''>weight-bearing fins</text>
<text x="42" y="108" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>NECK</text>
<line x1="20" y1="140" x2="220" y2="140" stroke="#334155" stroke-width="1"/>
<text x="20" y="148" fill="#60a5fa" font-size="8" ''' + FT + '''>Fish</text>
<text x="200" y="148" fill="#86efac" font-size="8" ''' + FT + '''>Tetrapod</text>
<circle cx="120" cy="140" r="4" fill="#fbbf24"/>
''')

W("permian", T("PERMIAN EXTINCTION ~252 mya") + S('"The Great Dying"', y=26, color="#fca5a5") + '''
<circle cx="75" cy="85" r="40" fill="#ef4444"/>
<path d="M75 85 L75 45 A40 40 0 0 1 90 122 Z" fill="#22c55e"/>
<text x="62" y="80" fill="#fecaca" font-size="13" font-weight="700" ''' + FT + '''>96%</text>
<text x="55" y="92" fill="#fecaca" font-size="7" ''' + FT + '''>extinct</text>
<text x="85" y="118" fill="#86efac" font-size="7" ''' + FT + '''>4% left</text>
<rect x="135" y="40" width="90" height="65" fill="#1a0a0a" rx="4" stroke="#7f1d1d"/>
<text x="180" y="55" text-anchor="middle" fill="#f87171" font-size="9" font-weight="700" ''' + FT + '''>CAUSE:</text>
<text x="180" y="68" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>Siberian Traps</text>
<text x="180" y="80" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>volcanism</text>
<text x="180" y="92" text-anchor="middle" fill="#fca5a5" font-size="8" ''' + FT + '''>CO₂ + acid rain</text>
<text x="120" y="130" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>LARGEST mass extinction</text>
<text x="120" y="142" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>70% terrestrial verts lost</text>
''')

W("lagerstaette", T("LAGERSTÄTTE") + S("Exceptional fossil preservation") + '''
<rect x="20" y="38" width="200" height="14" fill="#1c1917" rx="2"/>
<rect x="20" y="54" width="200" height="22" fill="#292524" rx="2"/>
<ellipse cx="70" cy="65" rx="18" ry="6" fill="none" stroke="#ca8a04" stroke-width="1.5"/>
<text x="70" y="69" text-anchor="middle" fill="#fde68a" font-size="7" ''' + FT + '''>soft body!</text>
<ellipse cx="155" cy="65" rx="18" ry="6" fill="none" stroke="#ca8a04" stroke-width="1.5"/>
<text x="155" y="69" text-anchor="middle" fill="#fde68a" font-size="7" ''' + FT + '''>preserved</text>
<rect x="20" y="78" width="200" height="14" fill="#1c1917" rx="2"/>
<text x="120" y="106" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>anoxic rapid burial</text>
<rect x="20" y="112" width="200" height="32" fill="#111" rx="3" stroke="#334155"/>
<text x="120" y="125" text-anchor="middle" fill="#fbbf24" font-size="9" font-weight="700" ''' + FT + '''>Famous examples:</text>
<text x="120" y="137" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Burgess Shale · Chengjiang</text>
''')

W("geologic_timeline", T("GEOLOGIC TIMELINE") + S("Camels Often Sit Down Carefully...", y=24) + '''
<rect x="15" y="32" width="20" height="12" fill="#7c3aed"/>
<text x="25" y="42" text-anchor="middle" fill="#e9d5ff" font-size="6" ''' + FT + '''>Cam</text>
<rect x="36" y="32" width="16" height="12" fill="#2563eb"/>
<text x="44" y="42" text-anchor="middle" fill="#bfdbfe" font-size="6" ''' + FT + '''>Ord</text>
<rect x="53" y="32" width="14" height="12" fill="#0891b2"/>
<text x="60" y="42" text-anchor="middle" fill="#cffafe" font-size="6" ''' + FT + '''>Sil</text>
<rect x="68" y="32" width="20" height="12" fill="#059669"/>
<text x="78" y="42" text-anchor="middle" fill="#d1fae5" font-size="6" ''' + FT + '''>Dev</text>
<rect x="89" y="32" width="18" height="12" fill="#d97706"/>
<text x="98" y="42" text-anchor="middle" fill="#fef3c7" font-size="6" ''' + FT + '''>Car</text>
<rect x="108" y="32" width="18" height="12" fill="#dc2626"/>
<text x="117" y="42" text-anchor="middle" fill="#fee2e2" font-size="6" ''' + FT + '''>Perm</text>
<rect x="127" y="32" width="14" height="12" fill="#9333ea"/>
<text x="134" y="42" text-anchor="middle" fill="#f3e8ff" font-size="6" ''' + FT + '''>Tri</text>
<rect x="142" y="32" width="16" height="12" fill="#0f766e"/>
<text x="150" y="42" text-anchor="middle" fill="#ccfbf1" font-size="6" ''' + FT + '''>Jur</text>
<rect x="159" y="32" width="22" height="12" fill="#166534"/>
<text x="170" y="42" text-anchor="middle" fill="#dcfce7" font-size="6" ''' + FT + '''>Cret</text>
<rect x="182" y="32" width="28" height="12" fill="#1d4ed8"/>
<text x="196" y="42" text-anchor="middle" fill="#dbeafe" font-size="6" ''' + FT + '''>Cenozoic</text>
<g fill="#ef4444">
<polygon points="52,50 48,60 56,60"/>
<polygon points="78,50 74,60 82,60"/>
<polygon points="117,50 113,60 121,60"/>
<polygon points="141,50 137,60 145,60"/>
<polygon points="181,50 177,60 185,60"/>
</g>
<text x="120" y="75" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="700" ''' + FT + '''>Big 5 extinctions ↑</text>
<text x="50" y="95" text-anchor="middle" fill="#fca5a5" font-size="7" ''' + FT + '''>End-Ord</text>
<text x="78" y="95" text-anchor="middle" fill="#fca5a5" font-size="7" ''' + FT + '''>Late-Dev</text>
<text x="117" y="95" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="700" ''' + FT + '''>End-Perm★</text>
<text x="141" y="95" text-anchor="middle" fill="#fca5a5" font-size="7" ''' + FT + '''>End-Tri</text>
<text x="181" y="95" text-anchor="middle" fill="#fca5a5" font-size="7" ''' + FT + '''>K-Pg</text>
<text x="15" y="115" fill="#64748b" font-size="7" ''' + FT + '''>541 mya</text>
<text x="190" y="115" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="120" y="135" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>10 periods · 5 mass extinctions</text>
''')

W("precambrian", T("PRECAMBRIAN = 88% of Earth's history") + '''
<rect x="20" y="50" width="176" height="15" fill="#1e3a5f" stroke="#60a5fa"/>
<rect x="196" y="50" width="24" height="15" fill="#166534" stroke="#22c55e"/>
<text x="108" y="60" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700" ''' + FT + '''>PRECAMBRIAN</text>
<text x="208" y="60" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>Phan</text>
<text x="20" y="78" fill="#64748b" font-size="7" ''' + FT + '''>4.568 bya</text>
<text x="193" y="78" fill="#fbbf24" font-size="7" ''' + FT + '''>541 mya</text>
<text x="218" y="78" fill="#64748b" font-size="7" ''' + FT + '''>now</text>
<line x1="40" y1="50" x2="40" y2="90" stroke="#86efac" stroke-width="1" stroke-dasharray="2,2"/>
<text x="40" y="100" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>First life</text>
<text x="40" y="109" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>3.8 bya</text>
<line x1="100" y1="50" x2="100" y2="118" stroke="#60a5fa" stroke-width="1" stroke-dasharray="2,2"/>
<text x="100" y="128" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>GOE 2.4bya</text>
<line x1="150" y1="50" x2="150" y2="135" stroke="#a78bfa" stroke-width="1" stroke-dasharray="2,2"/>
<text x="150" y="145" text-anchor="middle" fill="#c4b5fd" font-size="7" ''' + FT + '''>Eukaryotes 2.1bya</text>
''')

W("earliest_life", T("EARLIEST UNDISPUTED LIFE") + '''
<rect x="20" y="32" width="200" height="28" fill="#1c1917" rx="2"/>
<ellipse cx="60" cy="46" rx="20" ry="7" fill="#166534"/>
<ellipse cx="60" cy="55" rx="18" ry="4" fill="none" stroke="#ca8a04" stroke-width="0.8"/>
<text x="60" y="75" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>STROMATOLITES</text>
<text x="60" y="86" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>3.45 bya</text>
<text x="60" y="96" text-anchor="middle" fill="#64748b" font-size="7" ''' + FT + '''>morphological</text>
<rect x="145" y="32" width="70" height="28" fill="#1e1235" rx="2"/>
<circle cx="170" cy="46" r="3" fill="#7c3aed"/>
<circle cx="185" cy="46" r="3" fill="#7c3aed"/>
<circle cx="200" cy="46" r="3" fill="#7c3aed"/>
<text x="180" y="75" text-anchor="middle" fill="#c4b5fd" font-size="8" font-weight="700" ''' + FT + '''>BIOMARKERS</text>
<text x="180" y="86" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>3.8 bya</text>
<text x="180" y="96" text-anchor="middle" fill="#64748b" font-size="7" ''' + FT + '''>chemical</text>
<line x1="20" y1="115" x2="220" y2="115" stroke="#334155"/>
<text x="120" y="135" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" ''' + FT + '''>Earth formed 4.568 bya → life within 700 Myr</text>
''')

W("ribozymes", T("RIBOZYMES — RNA as Enzyme") + '''
<path d="M60 90 Q75 60 90 80 Q105 100 120 75 Q135 55 150 85 Q165 110 180 80" fill="none" stroke="#7c3aed" stroke-width="2.5"/>
<circle cx="120" cy="75" r="12" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2"/>
<text x="120" y="58" text-anchor="middle" fill="#fde68a" font-size="8" ''' + FT + '''>active site</text>
<circle cx="50" cy="90" r="5" fill="#86efac"/>
<text x="50" y="108" text-anchor="middle" fill="#86efac" font-size="8" ''' + FT + '''>substrate</text>
<text x="70" y="125" fill="#94a3b8" font-size="16" ''' + FT + '''>→</text>
<circle cx="195" cy="80" r="5" fill="#f9a8d4"/>
<circle cx="195" cy="95" r="3" fill="#f9a8d4"/>
<text x="195" y="115" text-anchor="middle" fill="#f9a8d4" font-size="8" ''' + FT + '''>products</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>RNA that catalyzes like a protein enzyme</text>
''')

W("kar_dating", T("K-Ar DATING") + S("t½ = 1.25 billion years") + '''
<polygon points="60,115 40,60 100,60 80,115" fill="#57534e"/>
<polygon points="100,60 110,40 110,60" fill="#ef4444"/>
<text x="70" y="95" text-anchor="middle" fill="#fde68a" font-size="8" ''' + FT + '''>lava</text>
<circle cx="160" cy="70" r="25" fill="#111827" stroke="#60a5fa" stroke-width="1.5"/>
<line x1="160" y1="70" x2="160" y2="50" stroke="#ef4444" stroke-width="2"/>
<circle cx="160" cy="70" r="2" fill="#fbbf24"/>
<text x="160" y="45" text-anchor="middle" fill="#fca5a5" font-size="7" ''' + FT + '''>reset!</text>
<text x="160" y="105" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" ''' + FT + '''>Clock = 0</text>
<text x="130" y="120" fill="#94a3b8" font-size="8" ''' + FT + '''>Eruption resets K/Ar ratio</text>
<text x="120" y="138" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>Dates volcanic rocks 100k to 4.5 bya</text>
''')

W("burgess_shale", T("BURGESS SHALE ~541 mya") + '''
<rect x="20" y="30" width="200" height="110" fill="#1c1917" rx="3"/>
<rect x="20" y="30" width="200" height="110" fill="none" stroke="#57534e" stroke-dasharray="3,2"/>
<ellipse cx="60" cy="60" rx="20" ry="10" fill="none" stroke="#ca8a04"/>
<line x1="50" y1="60" x2="80" y2="60" stroke="#ca8a04"/>
<text x="60" y="80" text-anchor="middle" fill="#fde68a" font-size="7" ''' + FT + '''>Anomalocaris</text>
<path d="M130 60 Q135 50 145 55 Q155 60 150 70 Q145 75 135 72 Z" fill="none" stroke="#ca8a04"/>
<text x="140" y="85" text-anchor="middle" fill="#fde68a" font-size="7" ''' + FT + '''>Opabinia</text>
<path d="M185 60 Q195 50 205 60 Q215 70 205 75" fill="none" stroke="#ca8a04"/>
<text x="195" y="85" text-anchor="middle" fill="#fde68a" font-size="7" ''' + FT + '''>Hallucigenia</text>
<text x="120" y="115" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" ''' + FT + '''>Soft-body preservation!</text>
<text x="120" y="130" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Window into Cambrian Explosion</text>
''')

W("ediacaran", T("EDIACARAN BIOTA 635–541 mya") + '''
<ellipse cx="55" cy="80" rx="18" ry="25" fill="none" stroke="#a78bfa" stroke-width="1.5"/>
<ellipse cx="55" cy="80" rx="12" ry="20" fill="none" stroke="#a78bfa" stroke-width="1"/>
<text x="55" y="120" text-anchor="middle" fill="#c4b5fd" font-size="7" ''' + FT + '''>Dickinsonia</text>
<path d="M115 100 L115 55 L100 45 L115 50 L130 45 L115 55" fill="none" stroke="#86efac" stroke-width="1.5"/>
<path d="M115 50 L105 55 L115 60 L125 55 L115 50" fill="none" stroke="#86efac"/>
<text x="115" y="120" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>Charnia</text>
<circle cx="180" cy="80" r="20" fill="none" stroke="#60a5fa" stroke-width="1.5"/>
<circle cx="180" cy="80" r="12" fill="none" stroke="#60a5fa" stroke-width="1"/>
<line x1="180" y1="60" x2="180" y2="100" stroke="#60a5fa"/>
<line x1="160" y1="80" x2="200" y2="80" stroke="#60a5fa"/>
<text x="180" y="120" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>Tribrachidium</text>
<text x="120" y="140" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Bizarre soft-bodied organisms before Cambrian</text>
''')

W("three_domains", T("THREE DOMAINS OF LIFE") + '''
<circle cx="120" cy="85" r="4" fill="#fbbf24"/>
<text x="120" y="108" text-anchor="middle" fill="#fbbf24" font-size="7" ''' + FT + '''>LUCA</text>
<line x1="120" y1="85" x2="50" y2="55" stroke="#60a5fa" stroke-width="2"/>
<line x1="120" y1="85" x2="120" y2="40" stroke="#a78bfa" stroke-width="2"/>
<line x1="120" y1="85" x2="190" y2="55" stroke="#22c55e" stroke-width="2"/>
<rect x="20" y="38" width="60" height="28" fill="#1e3a5f" rx="4"/>
<text x="50" y="50" text-anchor="middle" fill="#93c5fd" font-size="8" font-weight="700" ''' + FT + '''>BACTERIA</text>
<text x="50" y="60" text-anchor="middle" fill="#93c5fd" font-size="6" ''' + FT + '''>E.coli, cyano</text>
<rect x="90" y="22" width="60" height="28" fill="#1a1a2e" rx="4"/>
<text x="120" y="35" text-anchor="middle" fill="#a78bfa" font-size="8" font-weight="700" ''' + FT + '''>ARCHAEA</text>
<text x="120" y="45" text-anchor="middle" fill="#a78bfa" font-size="6" ''' + FT + '''>methanogens</text>
<rect x="160" y="38" width="60" height="28" fill="#14532d" rx="4"/>
<text x="190" y="50" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>EUKARYA</text>
<text x="190" y="60" text-anchor="middle" fill="#86efac" font-size="6" ''' + FT + '''>us, plants, fungi</text>
<text x="120" y="138" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>rRNA phylogenetics (Woese 1977)</text>
''')

W("circumstellar_disk", T("EARTH'S FORMATION 4.568 bya") + '''
<circle cx="120" cy="75" r="12" fill="#fbbf24"/>
<circle cx="120" cy="75" r="8" fill="#fde68a"/>
<text x="120" y="78" text-anchor="middle" fill="#000" font-size="6" ''' + FT + '''>Sun</text>
<ellipse cx="120" cy="75" rx="90" ry="22" fill="none" stroke="#60a5fa" stroke-width="1" opacity="0.6"/>
<ellipse cx="120" cy="75" rx="70" ry="17" fill="none" stroke="#a78bfa" stroke-width="1" opacity="0.6"/>
<ellipse cx="120" cy="75" rx="45" ry="11" fill="none" stroke="#f97316" stroke-width="1" opacity="0.6"/>
<circle cx="160" cy="75" r="3" fill="#f97316"/>
<circle cx="175" cy="78" r="2" fill="#64748b"/>
<circle cx="190" cy="80" r="4" fill="#22c55e"/>
<text x="190" y="97" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>Earth</text>
<circle cx="55" cy="80" r="2" fill="#64748b"/>
<circle cx="45" cy="72" r="1.5" fill="#64748b"/>
<text x="120" y="120" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Protoplanetary disk → planets coalesce</text>
<text x="120" y="138" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>Solar nebula → rocky planets inner orbits</text>
''')

W("ordovician_ext", T("ORDOVICIAN EXTINCTION 445 mya") + '''
<line x1="30" y1="100" x2="210" y2="100" stroke="#334155"/>
<polyline points="30,90 80,88 110,92 125,40 135,40 140,92 180,90 210,88" fill="none" stroke="#ef4444" stroke-width="2"/>
<line x1="130" y1="40" x2="130" y2="115" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2"/>
<text x="130" y="125" text-anchor="middle" fill="#fbbf24" font-size="8" ''' + FT + '''>445 mya</text>
<text x="130" y="135" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="700" ''' + FT + '''>86% species</text>
<text x="120" y="30" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>extinction rate</text>
<text x="25" y="145" fill="#64748b" font-size="7" ''' + FT + '''>500 mya</text>
<text x="180" y="145" fill="#64748b" font-size="7" ''' + FT + '''>400 mya</text>
<text x="120" y="65" text-anchor="middle" fill="#60a5fa" font-size="7" ''' + FT + '''>Glaciation → sea level drop</text>
''')

# =========================================================================
# GROUP B — PHYLOGENETICS
# =========================================================================

W("phylo_tree", T("TREE COMPONENTS") + '''
<line x1="25" y1="95" x2="60" y2="95" stroke="#60a5fa" stroke-width="2"/>
<line x1="60" y1="95" x2="60" y2="55" stroke="#60a5fa" stroke-width="2"/>
<line x1="60" y1="95" x2="60" y2="125" stroke="#60a5fa" stroke-width="2"/>
<line x1="60" y1="55" x2="105" y2="55" stroke="#60a5fa" stroke-width="2"/>
<line x1="60" y1="125" x2="105" y2="125" stroke="#60a5fa" stroke-width="2"/>
<line x1="105" y1="55" x2="105" y2="38" stroke="#60a5fa" stroke-width="2"/>
<line x1="105" y1="55" x2="105" y2="72" stroke="#60a5fa" stroke-width="2"/>
<line x1="105" y1="38" x2="145" y2="38" stroke="#60a5fa" stroke-width="2"/>
<line x1="105" y1="72" x2="145" y2="72" stroke="#60a5fa" stroke-width="2"/>
<circle cx="25" cy="95" r="5" fill="#ef4444"/>
<text x="9" y="82" fill="#fca5a5" font-size="8" font-weight="700" ''' + FT + '''>ROOT</text>
<circle cx="60" cy="95" r="4" fill="#a78bfa"/>
<circle cx="105" cy="55" r="4" fill="#a78bfa"/>
<text x="68" y="50" fill="#c4b5fd" font-size="7" ''' + FT + '''>node</text>
<circle cx="145" cy="38" r="5" fill="#fbbf24"/>
<circle cx="145" cy="72" r="5" fill="#fbbf24"/>
<circle cx="105" cy="125" r="5" fill="#fbbf24"/>
<text x="153" y="42" fill="#fde68a" font-size="7" ''' + FT + '''>tip A</text>
<text x="153" y="76" fill="#fde68a" font-size="7" ''' + FT + '''>tip B</text>
<text x="113" y="129" fill="#fde68a" font-size="7" ''' + FT + '''>tip C</text>
<rect x="148" y="30" width="3" height="50" fill="#86efac"/>
<text x="160" y="58" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>clade</text>
<text x="75" y="108" fill="#94a3b8" font-size="7" ''' + FT + '''>branch</text>
<text x="120" y="145" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Root · node · branch · tip · clade</text>
''')

W("sister_taxa", T("SISTER TAXA") + S("Share ONE immediate common ancestor") + '''
<line x1="30" y1="90" x2="80" y2="90" stroke="#60a5fa" stroke-width="2"/>
<line x1="80" y1="90" x2="80" y2="55" stroke="#fbbf24" stroke-width="2.5"/>
<line x1="80" y1="90" x2="80" y2="125" stroke="#fbbf24" stroke-width="2.5"/>
<line x1="80" y1="55" x2="160" y2="55" stroke="#fbbf24" stroke-width="2.5"/>
<line x1="80" y1="125" x2="160" y2="125" stroke="#fbbf24" stroke-width="2.5"/>
<circle cx="80" cy="90" r="6" fill="#a78bfa"/>
<text x="50" y="94" fill="#c4b5fd" font-size="7" ''' + FT + '''>common</text>
<text x="50" y="103" fill="#c4b5fd" font-size="7" ''' + FT + '''>ancestor</text>
<circle cx="160" cy="55" r="6" fill="#fbbf24"/>
<circle cx="160" cy="125" r="6" fill="#fbbf24"/>
<text x="170" y="59" fill="#fde68a" font-size="9" font-weight="700" ''' + FT + '''>SISTER A</text>
<text x="170" y="129" fill="#fde68a" font-size="9" font-weight="700" ''' + FT + '''>SISTER B</text>
<text x="200" y="92" fill="#86efac" font-size="24" ''' + FT + '''>}</text>
<text x="210" y="94" fill="#86efac" font-size="8" ''' + FT + '''>sister</text>
''')

W("synapomorphy", T("SYNAPOMORPHY = defines clade") + '''
<line x1="30" y1="100" x2="65" y2="100" stroke="#60a5fa" stroke-width="2"/>
<line x1="65" y1="100" x2="65" y2="60" stroke="#60a5fa" stroke-width="2"/>
<line x1="65" y1="100" x2="65" y2="135" stroke="#60a5fa" stroke-width="2"/>
<line x1="65" y1="135" x2="155" y2="135" stroke="#60a5fa" stroke-width="2"/>
<line x1="65" y1="60" x2="100" y2="60" stroke="#60a5fa" stroke-width="2"/>
<line x1="100" y1="60" x2="100" y2="42" stroke="#60a5fa" stroke-width="2"/>
<line x1="100" y1="60" x2="100" y2="78" stroke="#60a5fa" stroke-width="2"/>
<line x1="100" y1="42" x2="155" y2="42" stroke="#60a5fa" stroke-width="2"/>
<line x1="100" y1="78" x2="155" y2="78" stroke="#60a5fa" stroke-width="2"/>
<rect x="60" y="76" width="12" height="8" fill="#ef4444" rx="1"/>
<text x="66" y="83" text-anchor="middle" fill="#fff" font-size="6" font-weight="700" ''' + FT + '''>SYN</text>
<text x="160" y="46" fill="#94a3b8" font-size="8" ''' + FT + '''>taxon A</text>
<text x="160" y="82" fill="#94a3b8" font-size="8" ''' + FT + '''>taxon B</text>
<text x="160" y="139" fill="#64748b" font-size="8" ''' + FT + '''>outgroup</text>
<rect x="153" y="35" width="3" height="52" fill="#ef4444"/>
<text x="162" y="65" fill="#ef4444" font-size="8" font-weight="700" ''' + FT + '''>CLADE</text>
<text x="120" y="120" text-anchor="middle" fill="#fca5a5" font-size="9" ''' + FT + '''>Shared DERIVED character</text>
''')

W("symplesiomorphy", T("SYMPLESIOMORPHY") + S("Shared ANCESTRAL character") + '''
<line x1="30" y1="100" x2="60" y2="100" stroke="#475569" stroke-width="2"/>
<line x1="60" y1="100" x2="60" y2="55" stroke="#475569" stroke-width="2"/>
<line x1="60" y1="100" x2="60" y2="135" stroke="#475569" stroke-width="2"/>
<line x1="60" y1="55" x2="100" y2="55" stroke="#475569" stroke-width="2"/>
<line x1="60" y1="135" x2="100" y2="135" stroke="#475569" stroke-width="2"/>
<line x1="100" y1="55" x2="155" y2="55" stroke="#475569" stroke-width="2"/>
<line x1="100" y1="135" x2="155" y2="135" stroke="#475569" stroke-width="2"/>
<rect x="25" y="96" width="10" height="8" fill="#64748b" rx="1"/>
<text x="30" y="103" text-anchor="middle" fill="#fff" font-size="5" font-weight="700" ''' + FT + '''>ANC</text>
<circle cx="155" cy="55" r="4" fill="#64748b"/>
<text x="163" y="59" fill="#94a3b8" font-size="8" ''' + FT + '''>has trait ✓</text>
<circle cx="155" cy="135" r="4" fill="#64748b"/>
<text x="163" y="139" fill="#94a3b8" font-size="8" ''' + FT + '''>has trait ✓</text>
<text x="120" y="148" text-anchor="middle" fill="#ef4444" font-size="9" ''' + FT + '''>⚠ Outgroup has it too → NOT informative</text>
''')

W("monophyletic", T("MONOPHYLETIC (valid clade)") + '''
<rect x="55" y="100" width="105" height="45" fill="#14532d" opacity="0.3" rx="4"/>
<line x1="30" y1="85" x2="60" y2="85" stroke="#334155" stroke-width="2"/>
<line x1="60" y1="85" x2="60" y2="45" stroke="#334155" stroke-width="2"/>
<line x1="60" y1="85" x2="60" y2="125" stroke="#22c55e" stroke-width="2.5"/>
<line x1="60" y1="45" x2="100" y2="45" stroke="#334155" stroke-width="2"/>
<line x1="60" y1="125" x2="100" y2="125" stroke="#22c55e" stroke-width="2.5"/>
<line x1="100" y1="125" x2="100" y2="110" stroke="#22c55e" stroke-width="2.5"/>
<line x1="100" y1="125" x2="100" y2="140" stroke="#22c55e" stroke-width="2.5"/>
<line x1="100" y1="110" x2="155" y2="110" stroke="#22c55e" stroke-width="2.5"/>
<line x1="100" y1="140" x2="155" y2="140" stroke="#22c55e" stroke-width="2.5"/>
<line x1="100" y1="45" x2="155" y2="45" stroke="#334155" stroke-width="2"/>
<circle cx="155" cy="45" r="4" fill="#94a3b8"/>
<text x="163" y="49" fill="#64748b" font-size="7" ''' + FT + '''>outgroup</text>
<circle cx="155" cy="110" r="5" fill="#22c55e"/>
<text x="163" y="114" fill="#86efac" font-size="8" ''' + FT + '''>A ✓</text>
<circle cx="155" cy="140" r="5" fill="#22c55e"/>
<text x="163" y="144" fill="#86efac" font-size="8" ''' + FT + '''>B ✓</text>
<text x="120" y="78" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" ''' + FT + '''>"All kids at the reunion"</text>
<text x="120" y="90" text-anchor="middle" fill="#22c55e" font-size="10" font-weight="700" ''' + FT + '''>✓ VALID</text>
''')

W("paraphyletic", T("PARAPHYLETIC (invalid)") + S("Ancestor + SOME descendants") + '''
<rect x="50" y="28" width="110" height="45" fill="#92400e" opacity="0.25" rx="3"/>
<line x1="25" y1="90" x2="55" y2="90" stroke="#334155" stroke-width="2"/>
<line x1="55" y1="90" x2="55" y2="50" stroke="#334155" stroke-width="2"/>
<line x1="55" y1="90" x2="55" y2="130" stroke="#334155" stroke-width="2"/>
<line x1="55" y1="50" x2="95" y2="50" stroke="#334155" stroke-width="2"/>
<line x1="55" y1="130" x2="95" y2="130" stroke="#334155" stroke-width="2"/>
<line x1="95" y1="50" x2="95" y2="35" stroke="#334155" stroke-width="2"/>
<line x1="95" y1="50" x2="95" y2="65" stroke="#334155" stroke-width="2"/>
<line x1="95" y1="35" x2="155" y2="35" stroke="#d97706" stroke-width="2.5"/>
<line x1="95" y1="65" x2="155" y2="65" stroke="#d97706" stroke-width="2.5"/>
<line x1="95" y1="130" x2="155" y2="130" stroke="#22c55e" stroke-width="2"/>
<circle cx="155" cy="35" r="5" fill="#d97706"/>
<text x="163" y="39" fill="#fde68a" font-size="7" ''' + FT + '''>lizards ✓</text>
<circle cx="155" cy="65" r="5" fill="#d97706"/>
<text x="163" y="69" fill="#fde68a" font-size="7" ''' + FT + '''>crocs ✓</text>
<circle cx="155" cy="130" r="5" fill="#22c55e"/>
<text x="163" y="134" fill="#ef4444" font-size="8" font-weight="700" ''' + FT + '''>BIRDS ✗</text>
<text x="120" y="105" text-anchor="middle" fill="#f97316" font-size="8" ''' + FT + '''>"Reptilia" without birds</text>
<text x="120" y="118" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="700" ''' + FT + '''>✗ INVALID</text>
''')

W("polyphyletic", T("POLYPHYLETIC (invalid)") + S("Multiple ancestors · convergent trait") + '''
<line x1="25" y1="90" x2="70" y2="90" stroke="#334155" stroke-width="1.5"/>
<line x1="70" y1="90" x2="70" y2="55" stroke="#334155" stroke-width="1.5"/>
<line x1="70" y1="90" x2="70" y2="125" stroke="#334155" stroke-width="1.5"/>
<line x1="70" y1="55" x2="120" y2="55" stroke="#ef4444" stroke-width="2.5"/>
<line x1="70" y1="125" x2="120" y2="125" stroke="#334155" stroke-width="1.5"/>
<line x1="120" y1="55" x2="155" y2="45" stroke="#ef4444" stroke-width="2.5"/>
<line x1="120" y1="55" x2="155" y2="65" stroke="#334155" stroke-width="1.5"/>
<line x1="120" y1="125" x2="155" y2="115" stroke="#ef4444" stroke-width="2.5"/>
<line x1="120" y1="125" x2="155" y2="135" stroke="#334155" stroke-width="1.5"/>
<circle cx="155" cy="45" r="6" fill="#ef4444"/>
<text x="163" y="49" fill="#fca5a5" font-size="7" ''' + FT + '''>Elephant</text>
<circle cx="155" cy="115" r="6" fill="#ef4444"/>
<text x="163" y="119" fill="#fca5a5" font-size="7" ''' + FT + '''>Hippo</text>
<line x1="155" y1="46" x2="200" y2="82" stroke="#ef4444" stroke-width="1" stroke-dasharray="2,2"/>
<line x1="155" y1="116" x2="200" y2="82" stroke="#ef4444" stroke-width="1" stroke-dasharray="2,2"/>
<ellipse cx="200" cy="82" rx="18" ry="14" fill="#ef4444" opacity="0.2" stroke="#ef4444"/>
<text x="200" y="85" text-anchor="middle" fill="#fca5a5" font-size="6" ''' + FT + '''>grouped?</text>
<text x="120" y="148" text-anchor="middle" fill="#f87171" font-size="8" font-weight="700" ''' + FT + '''>✗ Not from shared ancestor</text>
''')

W("homoplasy", T("HOMOPLASY / CONVERGENT EVOLUTION") + '''
<line x1="30" y1="90" x2="70" y2="90" stroke="#334155" stroke-width="2"/>
<line x1="70" y1="90" x2="70" y2="55" stroke="#334155" stroke-width="2"/>
<line x1="70" y1="90" x2="70" y2="125" stroke="#334155" stroke-width="2"/>
<line x1="70" y1="55" x2="135" y2="55" stroke="#60a5fa" stroke-width="2"/>
<circle cx="140" cy="55" r="8" fill="#1e3a5f" stroke="#60a5fa" stroke-width="1.5"/>
<text x="140" y="59" text-anchor="middle" fill="#93c5fd" font-size="9" ''' + FT + '''>🦅</text>
<line x1="70" y1="125" x2="135" y2="125" stroke="#a78bfa" stroke-width="2"/>
<circle cx="140" cy="125" r="8" fill="#1e1235" stroke="#a78bfa" stroke-width="1.5"/>
<text x="140" y="129" text-anchor="middle" fill="#c4b5fd" font-size="9" ''' + FT + '''>🦇</text>
<line x1="150" y1="55" x2="175" y2="75" stroke="#86efac" stroke-width="1.5" stroke-dasharray="2,2"/>
<line x1="150" y1="125" x2="175" y2="105" stroke="#86efac" stroke-width="1.5" stroke-dasharray="2,2"/>
<ellipse cx="195" cy="90" rx="22" ry="20" fill="#14532d" opacity="0.4" stroke="#22c55e" stroke-width="1.5"/>
<text x="195" y="85" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700" ''' + FT + '''>WINGS</text>
<text x="195" y="96" text-anchor="middle" fill="#86efac" font-size="6" ''' + FT + '''>same</text>
<text x="195" y="105" text-anchor="middle" fill="#86efac" font-size="6" ''' + FT + '''>solution</text>
<text x="120" y="148" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Independent origins of same trait</text>
''')

W("parsimony", T("PARSIMONY — fewest steps wins") + '''
<text x="50" y="38" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Tree A</text>
<line x1="25" y1="90" x2="50" y2="90" stroke="#334155" stroke-width="1.5"/>
<line x1="50" y1="90" x2="50" y2="55" stroke="#334155" stroke-width="1.5"/>
<line x1="50" y1="90" x2="50" y2="120" stroke="#334155" stroke-width="1.5"/>
<line x1="50" y1="55" x2="85" y2="55" stroke="#334155" stroke-width="1.5"/>
<line x1="50" y1="120" x2="85" y2="120" stroke="#334155" stroke-width="1.5"/>
<g fill="#ef4444" stroke="#ef4444">
<rect x="58" y="52" width="4" height="6"/><rect x="68" y="52" width="4" height="6"/>
<rect x="58" y="117" width="4" height="6"/><rect x="68" y="117" width="4" height="6"/>
<rect x="75" y="117" width="4" height="6"/>
</g>
<text x="50" y="140" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="700" ''' + FT + '''>5 steps</text>
<text x="170" y="38" text-anchor="middle" fill="#22c55e" font-size="8" font-weight="700" ''' + FT + '''>Tree B ★</text>
<rect x="125" y="45" width="95" height="85" fill="#0d2e1a" opacity="0.5" rx="5"/>
<line x1="140" y1="90" x2="165" y2="90" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="90" x2="165" y2="55" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="90" x2="165" y2="120" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="55" x2="200" y2="55" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="120" x2="200" y2="120" stroke="#22c55e" stroke-width="2"/>
<g fill="#22c55e">
<rect x="180" y="52" width="4" height="6"/><rect x="187" y="52" width="4" height="6"/>
<rect x="180" y="117" width="4" height="6"/>
</g>
<text x="170" y="140" text-anchor="middle" fill="#22c55e" font-size="9" font-weight="700" ''' + FT + '''>3 steps — preferred</text>
''')

W("homology", T("HOMOLOGY") + S("Same blueprint · different building") + '''
<g stroke="#60a5fa" fill="#1e3a5f">
<rect x="15" y="40" width="10" height="30"/>
<rect x="15" y="73" width="10" height="25"/>
</g>
<text x="20" y="115" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>Human arm</text>
<g stroke="#60a5fa" fill="#1e3a5f">
<rect x="60" y="45" width="35" height="18" rx="5"/>
</g>
<text x="77" y="80" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>Whale flipper</text>
<polygon points="120,42 140,35 160,42 160,62 120,73" fill="#1e1235" stroke="#a78bfa"/>
<text x="140" y="88" text-anchor="middle" fill="#c4b5fd" font-size="7" ''' + FT + '''>Bat wing</text>
<polygon points="175,40 210,32 220,42 200,60 175,60" fill="#14532d" stroke="#22c55e"/>
<text x="197" y="75" text-anchor="middle" fill="#86efac" font-size="7" ''' + FT + '''>Bird wing</text>
<text x="120" y="110" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700" ''' + FT + '''>Same bones: humerus + radius + ulna</text>
<text x="120" y="125" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Modified for different functions</text>
<text x="120" y="140" text-anchor="middle" fill="#64748b" font-size="7" ''' + FT + '''>Evidence of common ancestry</text>
''')

W("exaptation", T("EXAPTATION") + S("Evolved for A → co-opted for B") + '''
<rect x="15" y="38" width="85" height="55" fill="#1c2a1e" rx="5" stroke="#86efac"/>
<text x="58" y="55" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700" ''' + FT + '''>FEATHERS</text>
<text x="58" y="68" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>Original:</text>
<text x="58" y="80" text-anchor="middle" fill="#94a3b8" font-size="8" ''' + FT + '''>insulation</text>
<text x="58" y="90" text-anchor="middle" fill="#94a3b8" font-size="7" ''' + FT + '''>(dinosaurs)</text>
<text x="110" y="70" fill="#fbbf24" font-size="22" ''' + FT + '''>→</text>
<rect x="140" y="38" width="85" height="55" fill="#1a2035" rx="5" stroke="#60a5fa"/>
<text x="182" y="55" text-anchor="middle" fill="#60a5fa" font-size="9" font-weight="700" ''' + FT + '''>FEATHERS</text>
<text x="182" y="68" text-anchor="middle" fill="#93c5fd" font-size="8" ''' + FT + '''>New:</text>
<text x="182" y="80" text-anchor="middle" fill="#93c5fd" font-size="9" font-weight="700" ''' + FT + '''>FLIGHT</text>
<text x="182" y="90" text-anchor="middle" fill="#93c5fd" font-size="7" ''' + FT + '''>(millions yr later)</text>
<text x="120" y="115" text-anchor="middle" fill="#d97706" font-size="8" ''' + FT + '''>Also: swim bladder → lungs</text>
<text x="120" y="130" text-anchor="middle" fill="#64748b" font-size="8" ''' + FT + '''>"Pickup truck → flatbed" repurposing</text>
''')

W("outgroup", T("OUTGROUP") + S("Roots the tree · polarizes characters") + '''
<line x1="25" y1="90" x2="60" y2="90" stroke="#334155" stroke-width="2"/>
<line x1="60" y1="90" x2="60" y2="55" stroke="#94a3b8" stroke-width="2"/>
<line x1="60" y1="90" x2="60" y2="120" stroke="#334155" stroke-width="2"/>
<line x1="60" y1="55" x2="150" y2="55" stroke="#ef4444" stroke-width="2"/>
<line x1="60" y1="120" x2="100" y2="120" stroke="#334155" stroke-width="2"/>
<line x1="100" y1="120" x2="100" y2="108" stroke="#22c55e" stroke-width="2"/>
<line x1="100" y1="120" x2="100" y2="132" stroke="#22c55e" stroke-width="2"/>
<line x1="100" y1="108" x2="150" y2="108" stroke="#22c55e" stroke-width="2"/>
<line x1="100" y1="132" x2="150" y2="132" stroke="#22c55e" stroke-width="2"/>
<circle cx="150" cy="55" r="6" fill="#7f1d1d"/>
<text x="160" y="59" fill="#ef4444" font-size="9" font-weight="700" ''' + FT + '''>OUTGROUP</text>
<text x="160" y="70" fill="#fca5a5" font-size="7" ''' + FT + '''>(known distant)</text>
<circle cx="150" cy="108" r="5" fill="#22c55e"/>
<text x="160" y="112" fill="#86efac" font-size="8" ''' + FT + '''>ingroup A</text>
<circle cx="150" cy="132" r="5" fill="#22c55e"/>
<text x="160" y="136" fill="#86efac" font-size="8" ''' + FT + '''>ingroup B</text>
<circle cx="60" cy="90" r="4" fill="#fbbf24"/>
<text x="30" y="78" fill="#fbbf24" font-size="7" ''' + FT + '''>ROOT</text>
''')

W("cladistics", T("CLADISTICS") + S("Synapomorphies → tree") + '''
<rect x="15" y="35" width="95" height="70" fill="#111" rx="3" stroke="#334155"/>
<text x="24" y="48" fill="#60a5fa" font-size="7" font-weight="700" ''' + FT + '''>Taxon</text>
<text x="55" y="48" fill="#fbbf24" font-size="7" font-weight="700" ''' + FT + '''>C1</text>
<text x="75" y="48" fill="#fbbf24" font-size="7" font-weight="700" ''' + FT + '''>C2</text>
<text x="95" y="48" fill="#fbbf24" font-size="7" font-weight="700" ''' + FT + '''>C3</text>
<line x1="15" y1="52" x2="110" y2="52" stroke="#334155"/>
<text x="24" y="63" fill="#94a3b8" font-size="7" ''' + FT + '''>A</text>
<text x="58" y="63" fill="#86efac" font-size="7" ''' + FT + '''>1</text>
<text x="78" y="63" fill="#86efac" font-size="7" ''' + FT + '''>1</text>
<text x="98" y="63" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="24" y="76" fill="#94a3b8" font-size="7" ''' + FT + '''>B</text>
<text x="58" y="76" fill="#86efac" font-size="7" ''' + FT + '''>1</text>
<text x="78" y="76" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="98" y="76" fill="#86efac" font-size="7" ''' + FT + '''>1</text>
<text x="24" y="89" fill="#94a3b8" font-size="7" ''' + FT + '''>Out</text>
<text x="58" y="89" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="78" y="89" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="98" y="89" fill="#64748b" font-size="7" ''' + FT + '''>0</text>
<text x="118" y="75" fill="#fbbf24" font-size="16" ''' + FT + '''>→</text>
<line x1="145" y1="85" x2="165" y2="85" stroke="#334155" stroke-width="1.5"/>
<line x1="165" y1="85" x2="165" y2="55" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="85" x2="165" y2="115" stroke="#334155" stroke-width="1.5"/>
<line x1="165" y1="55" x2="210" y2="45" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="55" x2="210" y2="65" stroke="#22c55e" stroke-width="2"/>
<line x1="165" y1="115" x2="210" y2="115" stroke="#64748b"/>
<text x="215" y="48" fill="#86efac" font-size="7" ''' + FT + '''>A</text>
<text x="215" y="68" fill="#86efac" font-size="7" ''' + FT + '''>B</text>
<text x="215" y="118" fill="#64748b" font-size="7" ''' + FT + '''>Out</text>
<text x="120" y="130" text-anchor="middle" fill="#94a3b8" font-size="7" ''' + FT + '''>0 = ancestral · 1 = derived</text>
''')

print("Group A + B complete — history of life + phylogenetics written")
print(f"Files in {OUT}: {len([f for f in os.listdir(OUT) if f.startswith('svg_')])}")
