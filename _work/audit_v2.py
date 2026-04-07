"""Strict 5-slot Lecture-Notes audit.

Reads V2 from _work/builder/v2_distillations.py and reports any
violations of the hard schema rules:

  definition:        single sentence, <=25 words
  keyTerms:          exactly 4, each def <=6 words, color in {teal,purple,coral,pink}
  mnemonic.hook:     <=8 words
  mnemonic.explanation: <=20 words
  examTrap:          <=25 words

Also flags duplicate mnemonic hooks (rule: distinctive mnemonics).

Exit 0 = clean. Exit 1 = violations.
"""
import sys, io, os, re

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'builder'))
from v2_distillations import V2

ALLOWED_COLORS = {'teal', 'purple', 'coral', 'pink'}


def wc(s):
    """Count whitespace-separated tokens."""
    return len(s.split())


def is_one_sentence(s):
    """A single sentence ends in exactly one terminal punctuation mark."""
    s = s.strip()
    interior = s[:-1] if s and s[-1] in '.!?' else s
    return not re.search(r'[.!?]\s', interior)


violations = []
hooks_seen = {}

for nid, n in V2.items():
    v = n['v2']

    # definition
    d = v['definition']
    if wc(d) > 25:
        violations.append(f'{nid}: definition has {wc(d)} words (>25): "{d}"')
    if not is_one_sentence(d):
        violations.append(f'{nid}: definition is not a single sentence: "{d}"')

    # keyTerms
    kt = v['keyTerms']
    if len(kt) != 4:
        violations.append(f'{nid}: has {len(kt)} keyTerms (expected 4)')
    for i, term in enumerate(kt):
        for required in ('term', 'def', 'color'):
            if required not in term:
                violations.append(f'{nid}: keyTerm[{i}] missing "{required}"')
        td = term.get('def', '')
        if wc(td) > 6:
            violations.append(f'{nid}: keyTerm[{i}] "{term.get("term")}" def has {wc(td)} words (>6): "{td}"')
        c = term.get('color')
        if c not in ALLOWED_COLORS:
            violations.append(f'{nid}: keyTerm[{i}] color "{c}" not in {ALLOWED_COLORS}')

    # mnemonic
    mn = v['mnemonic']
    h = mn['hook']
    e = mn['explanation']
    if wc(h) > 8:
        violations.append(f'{nid}: mnemonic.hook has {wc(h)} words (>8): "{h}"')
    if wc(e) > 20:
        violations.append(f'{nid}: mnemonic.explanation has {wc(e)} words (>20): "{e}"')
    hooks_seen.setdefault(h.lower(), []).append(nid)

    # examTrap
    et = v['examTrap']
    if wc(et) > 25:
        violations.append(f'{nid}: examTrap has {wc(et)} words (>25): "{et}"')

    # actions
    actions = v['actions']
    for k in ('quizPrompt', 'flashcardFront', 'flashcardBack'):
        if k not in actions or not actions[k]:
            violations.append(f'{nid}: actions.{k} missing or empty')

# Duplicate hooks (rule: distinctive mnemonics)
for hook, nodes in hooks_seen.items():
    if len(nodes) > 1:
        violations.append(f'duplicate mnemonic hook "{hook}" used in: {nodes}')

print(f'Audited {len(V2)} nodes against 5-slot Lecture-Notes schema')
print(f'Unique mnemonic hooks: {len(hooks_seen)}')
print()

if violations:
    print(f'=== {len(violations)} VIOLATIONS ===')
    for v in violations:
        print('  - ' + v)
    sys.exit(1)
else:
    print('=== ALL CLEAN ===')
    sys.exit(0)
