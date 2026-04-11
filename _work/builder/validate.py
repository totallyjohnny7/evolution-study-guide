"""Post-build validator: enforces every node has clean content and >= 4 quiz questions."""
import json, re, sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data.json')

URL_RE = re.compile(r'https?://\S+')
PIC_RE = re.compile(r'Picture\d+|Graphic\d+\.(jpg|png|gif)', re.IGNORECASE)
ALT_RE = re.compile(r'alt\s*text', re.IGNORECASE)


def validate():
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)

    errors = []
    warnings = []

    for n in data['nodes']:
        nid = n['id']

        # Check popup sections
        for s in n.get('popup', {}).get('sections', []):
            body = s.get('body', '')
            if URL_RE.search(body):
                errors.append(f"{nid}/{s.get('label','?')}: raw URL")
            if PIC_RE.search(body):
                errors.append(f"{nid}/{s.get('label','?')}: Picture/Graphic ref")
            if ALT_RE.search(body):
                errors.append(f"{nid}/{s.get('label','?')}: alt text fragment")

        # Check quiz
        q = n.get('quiz')
        qcount = len(q) if isinstance(q, list) else (1 if q else 0)
        if qcount < 4:
            errors.append(f"{nid}: only {qcount} quiz questions (min 4)")
        elif qcount < 6:
            warnings.append(f"{nid}: only {qcount} questions (target 6+)")

        # Each question must have 3 distractors
        if isinstance(q, list):
            for i, qi in enumerate(q):
                d = qi.get('distractors', [])
                if len(d) != 3:
                    errors.append(f"{nid} Q{i+1}: has {len(d)} distractors, expected 3")
                if not qi.get('correct'):
                    errors.append(f"{nid} Q{i+1}: missing correct answer")
                if not qi.get('question'):
                    errors.append(f"{nid} Q{i+1}: missing question text")

    print(f"\n{'='*60}")
    print(f"VALIDATION RESULTS: {len(data['nodes'])} nodes")
    print(f"{'='*60}")

    total_q = sum(
        len(n['quiz']) if isinstance(n.get('quiz'), list) else (1 if n.get('quiz') else 0)
        for n in data['nodes']
    )
    print(f"Total quiz questions: {total_q}")
    print(f"Average per node: {total_q / len(data['nodes']):.1f}")

    if errors:
        print(f"\n❌ {len(errors)} ERRORS:")
        for e in errors[:20]:
            print(f"  - {e}")
        if len(errors) > 20:
            print(f"  ... +{len(errors)-20} more")
    else:
        print("\n✅ NO ERRORS")

    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNINGS (nodes with <6 questions):")
        for w in warnings[:15]:
            print(f"  - {w}")

    return len(errors) == 0


if __name__ == '__main__':
    ok = validate()
    sys.exit(0 if ok else 1)
