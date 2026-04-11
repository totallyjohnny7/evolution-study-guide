"""EvoDiagram validation helpers.

Each diagram data module returns a dict matching this shape:

    {
      'type': 'flow'|'tree'|'cycle'|'compare'|'timeline'|'punnett'|'matrix',
      'title': str,
      'nodes': [ {id, label, detail, mnemonic?, watchOut?, x?, y?, color?}, ... ],
      'edges': [ {from, to, label?, style?}, ... ]   # optional
      'mnemonic': str | None,                         # overall diagram mnemonic
    }

Call `validate_diagram(d)` to raise ValueError with a clear message if the
dict is malformed. The builder (`build.py`) calls this on every node.diagram
before serializing.
"""

VALID_TYPES = {'flow', 'tree', 'cycle', 'compare', 'timeline', 'punnett', 'matrix'}
VALID_EDGE_STYLES = {'solid', 'dashed', 'arrow', None}
VALID_COLORS = {
    'purple', 'teal', 'coral', 'amber', 'blue', 'gray', 'green', 'red', 'pink', None,
}


def validate_diagram(d, node_id='<unknown>'):
    """Raise ValueError if the diagram dict is malformed. Return d unchanged on success."""
    if d is None:
        return None
    if not isinstance(d, dict):
        raise ValueError(f"[{node_id}] diagram must be a dict, got {type(d).__name__}")

    t = d.get('type')
    if t not in VALID_TYPES:
        raise ValueError(f"[{node_id}] diagram.type '{t}' not in {VALID_TYPES}")

    title = d.get('title')
    if not title or not isinstance(title, str):
        raise ValueError(f"[{node_id}] diagram.title must be a non-empty string")

    nodes = d.get('nodes')
    if not isinstance(nodes, list) or not nodes:
        raise ValueError(f"[{node_id}] diagram.nodes must be a non-empty list")

    seen_ids = set()
    for i, n in enumerate(nodes):
        if not isinstance(n, dict):
            raise ValueError(f"[{node_id}] diagram.nodes[{i}] must be a dict")
        for req in ('id', 'label', 'detail'):
            if not n.get(req) or not isinstance(n[req], str):
                raise ValueError(f"[{node_id}] diagram.nodes[{i}].{req} missing or not a string")
        if n['id'] in seen_ids:
            raise ValueError(f"[{node_id}] diagram.nodes duplicate id '{n['id']}'")
        seen_ids.add(n['id'])
        for opt_str in ('mnemonic', 'watchOut', 'value'):
            if n.get(opt_str) is not None and not isinstance(n[opt_str], str):
                raise ValueError(f"[{node_id}] diagram.nodes[{i}].{opt_str} must be a string or None")
        for opt_num in ('x', 'y'):
            if n.get(opt_num) is not None:
                if not isinstance(n[opt_num], (int, float)):
                    raise ValueError(f"[{node_id}] diagram.nodes[{i}].{opt_num} must be numeric")
                if not (0 <= n[opt_num] <= 1):
                    raise ValueError(f"[{node_id}] diagram.nodes[{i}].{opt_num} must be in [0,1]")
        if n.get('color') is not None:
            c = n['color']
            if c not in VALID_COLORS and not (isinstance(c, str) and c.startswith('#')):
                raise ValueError(f"[{node_id}] diagram.nodes[{i}].color '{c}' not a palette name or hex")

    edges = d.get('edges') or []
    if not isinstance(edges, list):
        raise ValueError(f"[{node_id}] diagram.edges must be a list or None")
    for i, e in enumerate(edges):
        if not isinstance(e, dict):
            raise ValueError(f"[{node_id}] diagram.edges[{i}] must be a dict")
        for req in ('from', 'to'):
            if req not in e or not isinstance(e[req], str):
                raise ValueError(f"[{node_id}] diagram.edges[{i}].{req} missing or not a string")
            if e[req] not in seen_ids:
                raise ValueError(f"[{node_id}] diagram.edges[{i}].{req} '{e[req]}' is not a node id")
        if e.get('style') not in VALID_EDGE_STYLES:
            raise ValueError(f"[{node_id}] diagram.edges[{i}].style '{e.get('style')}' invalid")
        if e.get('label') is not None and not isinstance(e['label'], str):
            raise ValueError(f"[{node_id}] diagram.edges[{i}].label must be a string or None")

    if d.get('mnemonic') is not None and not isinstance(d['mnemonic'], str):
        raise ValueError(f"[{node_id}] diagram.mnemonic must be a string or None")

    return d


def make_node(id, label, detail, mnemonic=None, watchOut=None,
              x=None, y=None, color=None, value=None):
    """Convenience builder for a node dict — enforces key order and strips None."""
    n = {'id': id, 'label': label, 'detail': detail}
    if value is not None:
        n['value'] = value
    if mnemonic is not None:
        n['mnemonic'] = mnemonic
    if watchOut is not None:
        n['watchOut'] = watchOut
    if x is not None:
        n['x'] = x
    if y is not None:
        n['y'] = y
    if color is not None:
        n['color'] = color
    return n


def make_edge(from_id, to_id, label=None, style='solid'):
    """Convenience builder for an edge dict."""
    e = {'from': from_id, 'to': to_id, 'style': style}
    if label is not None:
        e['label'] = label
    return e
