"""EvoDiagram data modules.

Each sibling file exports a function that returns a validated diagram dict.
Usage from lecture modules:

    from diagrams.hwe_punnett import hwe_punnett_diagram
    build_node(..., diagram=hwe_punnett_diagram())
"""

from .types import validate_diagram, make_node, make_edge

__all__ = ['validate_diagram', 'make_node', 'make_edge']
