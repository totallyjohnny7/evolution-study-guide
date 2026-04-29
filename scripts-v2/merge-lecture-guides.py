"""Merge data/lecture-guides/L*.json into public-v2/content/lecture-guides.js as window.MANUAL_LECTURE_GUIDES."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
GUIDES_DIR = ROOT / "data" / "lecture-guides"
OUT_FILE = ROOT / "content" / "lecture-guides.js"

guides = {}
files = sorted(GUIDES_DIR.glob("L*.json"))
for fp in files:
    lid = fp.stem
    try:
        data = json.loads(fp.read_text(encoding="utf-8"))
        guides[lid] = data
        print(f"  + {lid}: {len(data.get('sections', []))} sections")
    except json.JSONDecodeError as e:
        print(f"  ! {lid}: INVALID JSON — {e}")

sorted_keys = sorted(guides.keys(), key=lambda k: int(k[1:]))
ordered = {k: guides[k] for k in sorted_keys}

js_body = json.dumps(ordered, indent=2, ensure_ascii=False)
out = (
    "/* Hand-authored lecture guides for BIOL 4230 Evolution.\n"
    "   Auto-merged by scripts-v2/merge-lecture-guides.py — edit data/lecture-guides/L*.json instead. */\n"
    f"window.MANUAL_LECTURE_GUIDES = {js_body};\n"
    "console.log('[lecture-guides loaded]', Object.keys(window.MANUAL_LECTURE_GUIDES).length, 'lectures');\n"
)
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(out, encoding="utf-8")
print(f"\nWrote {OUT_FILE} with {len(ordered)} lectures: {', '.join(sorted_keys)}")
