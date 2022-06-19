from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Node:
    data: int | float
    left: Optional["Node"] # Node | None
    right: Optional["Node"]

def append(n: Node, d: int | float) -> Node:
    """
        n: Node to append to
        d: int or float to append.
    """
    if n == None:
        return Node(d, None, None)
    if d == n.data:
        return None # No duplicated allowed.
        # assert 0
    if d < n.data:
        return Node(n.data, append(n.left, d), n.right)
    return Node(n.data, n.left, append(n.right, d))
