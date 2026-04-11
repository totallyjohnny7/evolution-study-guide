"""One-shot wiring tool: inject `diagram=<fn>()` into every lecture node
listed in WIRINGS. Idempotent — skips nodes that already have diagram= set.

Run: python _wire_diagrams.py
"""
import os
import re
import sys
import ast

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BUILDER_DIR = os.path.dirname(os.path.abspath(__file__))

WIRINGS = [
    # (node_id, diagram function name, module stem under diagrams/)
    ('lec2-pre-darwin',                       'darwin_five_ingredients_diagram',      'darwin_five_ingredients'),
    ('lec2-natural-selection-ingredients',    'natural_selection_logic_flow_diagram', 'natural_selection_logic_flow'),
    ('lec2-finches-case',                     'peppered_moth_selection_diagram',      'peppered_moth_selection'),
    ('lec2-descent-modification',             'tree_thinking_components_diagram',     'tree_thinking_components'),
    ('lec3-genes-proteins',                   'hox_regulatory_network_diagram',       'hox_regulatory_network'),
    ('lec3-genotype-phenotype',               'reaction_norm_gxe_diagram',            'reaction_norm_gxe'),
    ('lec4-sources-evolution',                'hardy_weinberg_assumptions_diagram',   'hardy_weinberg_assumptions'),
    ('lec4-hardy-weinberg',                   'hwe_punnett_diagram',                  'hwe_punnett'),
    ('lec4-genetic-drift',                    'genetic_drift_bottleneck_vs_founder_diagram', 'genetic_drift_bottleneck_vs_founder'),
    ('lec4-selection-mechanism',              'peppered_moth_selection_diagram',      'peppered_moth_selection'),
    ('lec56-reaction-norms',                  'reaction_norm_gxe_diagram',            'reaction_norm_gxe'),
    ('lec7-beach-mice',                       'beach_mice_parallel_evolution_diagram', 'beach_mice_parallel_evolution'),
    ('lec7-tsd',                              'tsd_charnov_bull_diagram',             'tsd_charnov_bull'),
    ('lec7-fitness-landscape',                'fitness_landscape_diagram',            'fitness_landscape'),
    ('lec8-eye-evolution',                    'eye_evolution_stages_diagram',         'eye_evolution_stages'),
    ('lec8-evo-devo',                         'hox_regulatory_network_diagram',       'hox_regulatory_network'),
    ('lec9-antagonistic-arms',                'garter_snake_newt_arms_race_diagram',  'garter_snake_newt_arms_race'),
    ('lec9-mimicry',                          'mullerian_vs_batesian_compare_diagram', 'mullerian_vs_batesian_compare'),
    ('lec9-endosymbiosis',                    'endosymbiosis_flow_diagram',           'endosymbiosis_flow'),
    ('lec1011-why-sex',                       'red_queen_cycle_diagram',              'red_queen_cycle'),
    ('lec1011-anisogamy',                     'anisogamy_origin_diagram',             'anisogamy_origin'),
    ('lec1011-male-female-strategies',        'side_blotched_rps_cycle_diagram',      'side_blotched_rps_cycle'),
    ('lec1011-sperm-competition',             'sperm_competition_strategies_diagram', 'sperm_competition_strategies'),
    ('lec12-life-history-intro',              'r_vs_k_compare_diagram',               'r_vs_k_compare'),
    ('lec12-aging',                           'life_history_r_k_timeline_diagram',    'life_history_r_k_timeline'),
    ('lec13-ess-game',                        'hawk_dove_game_diagram',               'hawk_dove_game'),
    ('lec13-kin-altruism',                    'hamiltons_rule_kin_selection_diagram', 'hamiltons_rule_kin_selection'),
    ('lec14-cambrian-paleozoic',              'paleozoic_timeline_diagram',           'paleozoic_timeline'),
    ('lec14-mesozoic-cenozoic',               'mesozoic_kt_timeline_diagram',         'mesozoic_kt_timeline'),
    ('lec15-tree-thinking',                   'tree_thinking_components_diagram',     'tree_thinking_components'),
    ('lec15-cladistics-synapomorphy',         'cladistics_character_matrix_diagram',  'cladistics_character_matrix'),
    ('lec15-homoplasy-convergence',           'mono_para_polyphyletic_compare_diagram', 'mono_para_polyphyletic_compare'),
    ('lec15-fins-to-limbs',                   'tiktaalik_transition_flow_diagram',    'tiktaalik_transition_flow'),
    ('lec15-feathers-exaptation',             'feathers_before_flight_exaptation_diagram', 'feathers_before_flight_exaptation'),
]


def locate_nodes():
    """Map node_id -> absolute path of the .py file that builds it."""
    mapping = {}
    for fname in ('lectures_1_7.py', 'lectures_8_13.py', 'lectures_14_15.py', 'lectures_16_speciation.py'):
        path = os.path.join(BUILDER_DIR, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as fh:
            src = fh.read()
        for nid in re.findall(r"id='([^']+)'", src):
            mapping.setdefault(nid, path)
    return mapping


def ensure_import(src, fn, mod):
    """Return src with `from diagrams.<mod> import <fn>` added if missing."""
    imp_line = f'from diagrams.{mod} import {fn}'
    if imp_line in src:
        return src, False
    # Insert after the last existing `from ... import` or `import` at module top
    matches = list(re.finditer(r'^(?:from\s+\S+\s+import\s+.+|import\s+.+)$', src, flags=re.MULTILINE))
    if matches:
        pos = matches[-1].end()
        src = src[:pos] + '\n' + imp_line + src[pos:]
    else:
        src = imp_line + '\n' + src
    return src, True


def inject_diagram(src, node_id, fn):
    """Insert `diagram=<fn>(),\n        ` into the build_node call for node_id.

    Looks for id='<node_id>' then finds the closing `))` of the build_node call
    after the last `visual=` kwarg. Skips if diagram= is already present in the
    span between id and the closing paren.

    Handles two source styles:
      (a) lectures_1_7.py / lectures_8_13.py / lectures_14_15.py
          — use the helper `build_node(...)` → always closes with `    ))`
      (b) lectures_16_speciation.py
          — uses parenthesized multi-line strings, same `))` closer
    """
    id_marker = f"id='{node_id}'"
    id_idx = src.find(id_marker)
    if id_idx == -1:
        return src, 'id-not-found'
    visual_idx = src.find('visual=', id_idx)
    if visual_idx == -1:
        return src, 'visual-not-found'
    # Find the closing `))\n` pattern AFTER visual= — the end of the build_node call
    candidates = ['},\n    ))\n', '},\n        ))\n', '},\n    )\n)', '},\n))\n']
    closing = -1
    match_str = None
    for cand in candidates:
        c = src.find(cand, visual_idx)
        if c != -1 and (closing == -1 or c < closing):
            closing = c
            match_str = cand
    if closing == -1:
        return src, 'closing-not-found'
    # Check if diagram= already present in this build_node span
    span_text = src[id_idx:closing]
    if 'diagram=' in span_text:
        return src, 'already-wired'
    # Insert: }, diagram=<fn>(), ))
    # match_str starts with "},\n" and the indent, then ")) \n"
    indent_match = re.match(r'},\n(\s*)\)', match_str)
    indent = indent_match.group(1) if indent_match else '        '
    insertion = f"}},\n{indent}diagram={fn}(),\n    ))\n"
    src = src[:closing] + insertion + src[closing + len(match_str):]
    return src, 'wired'


def main():
    mapping = locate_nodes()
    touched = {}  # file -> count
    by_status = {'wired': 0, 'already-wired': 0, 'id-not-found': 0, 'visual-not-found': 0, 'closing-not-found': 0}
    changes_per_file = {}

    for nid, fn, mod in WIRINGS:
        path = mapping.get(nid)
        if path is None:
            print(f'  [skip] {nid}: not in any lecture file')
            by_status['id-not-found'] += 1
            continue
        with open(path, encoding='utf-8') as fh:
            src = fh.read()
        # Ensure import
        src, import_added = ensure_import(src, fn, mod)
        # Inject the diagram= kwarg
        src, status = inject_diagram(src, nid, fn)
        by_status[status] += 1
        if status in ('wired', 'already-wired') or import_added:
            # Only write if the file text actually changed
            with open(path, encoding='utf-8') as fh:
                orig = fh.read()
            if src != orig:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(src)
                changes_per_file[path] = changes_per_file.get(path, 0) + 1
        tag = status.upper()
        print(f'  [{tag:<16}] {nid}')

    print()
    print('Summary:')
    for k, v in by_status.items():
        print(f'  {k}: {v}')
    print()
    print('Files modified:')
    for p, c in changes_per_file.items():
        print(f'  {os.path.basename(p)}: {c} changes')

    # Sanity: ensure every modified file still parses
    print()
    print('Syntax check:')
    for p in changes_per_file:
        try:
            with open(p, encoding='utf-8') as fh:
                ast.parse(fh.read())
            print(f'  OK  {os.path.basename(p)}')
        except SyntaxError as e:
            print(f'  ERR {os.path.basename(p)}: line {e.lineno}: {e.msg}')


if __name__ == '__main__':
    main()
