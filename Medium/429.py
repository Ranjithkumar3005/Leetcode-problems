"""
# Definition for a Node.
"""


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        dum = []
        que = deque([root])
        while que:
            ch = []
            len1 = len(que)
            for i in range(len1):
                val = que.popleft()
                ch.append(val.val)
                if val.children:
                    for j in val.children:
                        que.append(j)

            dum.append(ch)
        return dum
