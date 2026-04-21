#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download verified images for Exam 3 flashcards via Wikipedia API."""
import sys, json, time, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

OUT = Path(__file__).parent / "public" / "img" / "fc"
OUT.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Evolution StudyGuide/1.0; educational non-commercial)"

# Map: local_fname -> Wikipedia Commons file name to look up
FILE_MAP = [
    # CH3 — History of Life
    ("ch3_geologic_clock.jpg",  "Geologic_Clock_with_events_and_periods.svg"),
    ("ch3_miller_urey.jpg",     "Miller-Urey_experiment-en.svg"),
    ("ch3_stromatolites.jpg",   "Hamelin Pool Stromatolites 2.jpg"),
    ("ch3_tiktaalik.jpg",       "Tiktaalik roseae life restor.jpg"),
    ("ch3_burgess_shale.jpg",   "Burgess shale Anomalocaris.jpg"),
    ("ch3_three_domains.png",   "Phylogenetic tree.svg"),
    ("ch3_mass_extinction.png", "Extinction intensity.svg"),
    ("ch3_rna_world.jpg",       "RNA world.jpg"),
    # CH4 — Phylogenetics
    ("ch4_feathered_dino.jpg",  "Microraptor gui holotype ref.jpg"),
    ("ch4_archaeopteryx.jpg",   "Archaeopteryx lithographica (Berlin specimen).jpg"),
    ("ch4_cladogram.png",       "Cladogram of Reptilia.svg"),
    ("ch4_analogy.jpg",         "Analogous_Structures_(PSF).jpg"),
    # CH13 — Speciation
    ("ch13_mule.jpg",           "Mule.jpg"),
    ("ch13_speciation_modes.png","Speciation modes.svg"),
    ("ch13_rhagoletis.jpg",     "Rhagoletis pomonella.jpg"),
    ("ch13_polyploidy.png",     "Speciation by polyploidy.svg"),
    ("ch13_ring_species.png",   "Ring species.png"),
    # CH14 — Biogeography
    ("ch14_pangaea.jpg",        "Pangaea 250ma.jpg"),
    ("ch14_island_biogeo.png",  "Island Biogeography Graph.png"),
    ("ch14_plate_tectonics.jpg","Plates tect2 en.svg"),
    ("ch14_darwin_finches.jpg", "Darwin's finches by Gould.jpg"),
    # CH8 — Humans as selective force
    ("ch8_bighorn.jpg",         "Ovis canadensis 9474.jpg"),
    ("ch8_antibiotic_res.jpg",  "Antibiotic resistance.jpg"),
    ("ch8_elephant.jpg",        "African bush elephant.jpg"),
    ("ch8_peppered_moth.jpg",   "Biston.betularia.7200.jpg"),
    # CH17 — Human Evolution
    ("ch17_lucy.jpg",           "Lucy blackbg.jpg"),
    ("ch17_human_evo.jpg",      "Human evolution scheme.svg"),
    ("ch17_bipedalism.jpg",     "Australopith and human hip structures.png"),
    ("ch17_out_africa.jpg",     "Out of Africa 2.svg"),
    ("ch17_chromosome2.png",    "Evolution_chromosome_2.jpg"),
    ("ch17_neanderthal.jpg",    "Neanderthal type specimen.jpg"),
    # CH18 — Evolutionary Medicine
    ("ch18_sickle_cell.jpg",    "Sickle cell 01.jpg"),
    ("ch18_cancer_evo.jpg",     "Clonal evolution of cancer cells.jpg"),
    ("ch18_malaria_map.jpg",    "Sickle cell distribution.jpg"),
    ("ch18_myxoma.jpg",         "Myxomatosis in rabbit.jpg"),
    ("ch18_virulence.png",      "Virulence transmissibility tradeoff.svg"),
]

def api_lookup(fname):
    """Use Wikipedia API to get actual file URL."""
    enc = urllib.parse.quote(fname)
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles=File:{enc}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = json.loads(urllib.request.urlopen(req, timeout=10).read())
    for page in data["query"]["pages"].values():
        iis = page.get("imageinfo", [])
        if iis and iis[0].get("url"):
            return iis[0]["url"]
    return None

def download(url, dst):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    if len(data) < 2000:
        raise ValueError(f"Too small ({len(data)}B)")
    dst.write_bytes(data)
    return len(data)

ok, fail = [], []
for local_name, wiki_fname in FILE_MAP:
    dst = OUT / local_name
    try:
        real_url = api_lookup(wiki_fname)
        if not real_url:
            raise ValueError("API returned no URL")
        sz = download(real_url, dst)
        ok.append(local_name)
        print(f"OK  {local_name}  ({sz//1024}KB)  {real_url}")
    except Exception as e:
        fail.append((local_name, str(e)))
        print(f"FAIL {local_name}: {e}")
    time.sleep(0.5)

print(f"\n=== {len(ok)} downloaded, {len(fail)} failed ===")
for f,e in fail:
    print(f"  FAIL: {f}: {e}")
