"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloned_nodes = {}

        queue = deque([node])
        cloned_nodes[node] = Node(node.val)

        while queue:
            val = queue.popleft()
            for nei in val.neighbors:
                if nei not in cloned_nodes:
                    cloned_nodes[nei] = Node(nei.val)
                    queue.append(nei)
                cloned_nodes[val].neighbors.append(cloned_nodes[nei])
        return cloned_nodes[node]
