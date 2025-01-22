"""
# Definition for a Node.
"""

from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0
        que = deque([(root, 1)])
        max1 = float("-inf")
        while que:
            val, c = que.popleft()
            max1 = max(max1, c)
            if val.children:
                for j in val.children:
                    que.append((j, c + 1))
        return max1
