# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = set()
        que = deque([root])
        while que:
            val1 = que.popleft()
            val.add(val1.val)
            if len(val) > 1:
                return False
            if val1.left:
                que.append(val1.left)
            if val1.right:
                que.append(val1.right)
        return True
