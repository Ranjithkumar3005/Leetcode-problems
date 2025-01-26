# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dum = []
        que = deque([root])
        check = False
        while que:
            val1 = que.popleft()
            if val1.val == val:
                return val1
            if val1.left:
                que.append(val1.left)
            if val1.right:
                que.append(val1.right)
        return None
