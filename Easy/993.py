# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        que = deque([[root, 0]])
        while que:
            len1 = len(que)
            dum = {}
            for i in range(len1):
                val1 = que.popleft()
                dum[val1[0].val] = val1[1]
                if val1[0].left:
                    que.append([val1[0].left, val1[0].val])
                if val1[0].right:
                    que.append([val1[0].right, val1[0].val])
            if x in dum and y in dum and dum[x] != dum[y]:
                return True
        return False
