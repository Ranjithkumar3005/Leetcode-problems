"""
# Definition for a Node.
"""

from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []

        def postOrder(root):
            if not root:
                return
            for child in root.children:
                postOrder(child)
            res.append(root.val)

        postOrder(root)
        return res
