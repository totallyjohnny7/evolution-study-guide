"""For every chapter in content-final.js, generate a concise one-page
cheat sheet synthesizing section titles + key 'what it is' (wb) blocks
+ traps. Store as ch.cheatsheet (string, markdown-ish)."""
import json, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
PUB = r'C:\Users\johnn\Desktop\School\Evolution_EVOL4230\evolution-study-guide\public'
CF = os.path.join(PUB,'js','content-final.js')
raw = open(CF, encoding='utf-8').read()
start = raw.index('window.COURSE = ') + len('window.COURSE = ')
data = json.loads(raw[start:].rstrip().rstrip(';').rstrip())

def clean(txt):
    txt = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', txt)  # keep bold
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def first_sentence(s, max_len=180):
    s = clean(s)
    # Take first sentence or cut at max_len
    m = re.match(r'(.+?[.!?])\s', s)
    out = m.group(1) if m else s
    if len(out) > max_len:
        out = out[:max_len].rstrip() + '…'
    return out

for ch in data['chapters']:
    if ch.get('visualsAnchor') or not ch.get('sections'):
        continue
    lines = []
    lines.append(f"**Ch {ch.get('num','?')} · {ch.get('title','')}** — {ch.get('tagline','')}")
    lines.append('')
    for sec in ch['sections']:
        if sec['id'].endswith('_figs'):
            continue  # skip gallery sections
        blocks = sec.get('blocks', [])
        wb = next((b for b in blocks if b.get('kind') == 'wb'), None)
        trap = next((b for b in blocks if b.get('kind') == 'trap'), None)
        rem = next((b for b in blocks if b.get('kind') == 'rem'), None)
        lines.append(f"**§ {sec.get('num','')} {sec.get('title','')}**")
        if wb:
            lines.append('• ' + first_sentence(wb.get('body', '')))
        if trap:
            lines.append('• ⚠ ' + first_sentence(trap.get('body', ''), 140))
        if rem and not trap:
            lines.append('• 💡 ' + first_sentence(rem.get('body', ''), 140))
        lines.append('')
    ch['cheatsheet'] = '\n'.join(lines).strip()

# Also for exam-group groupings, stash a master "everything in one page" cheat at the top
# (chapter-level cheat sheets are enough; a master is overkill for a 56-section course)

header = '/* auto-generated — Final = Exam1+2+3 + Textbook + Visuals + Cheatsheets. */\nwindow.COURSE = '
open(CF,'w',encoding='utf-8').write(header + json.dumps(data, indent=2, ensure_ascii=False) + ';\n')

# Stats
with_cs = sum(1 for ch in data['chapters'] if ch.get('cheatsheet'))
print(f"Chapters with cheat sheet: {with_cs}/{len(data['chapters'])}")
print(f"File size: {os.path.getsize(CF):,}")
# Sample one
for ch in data['chapters']:
    if ch.get('cheatsheet'):
        print("\n=== SAMPLE CHEAT SHEET (ch3) ===")
        print(ch['cheatsheet'][:800])
        break
