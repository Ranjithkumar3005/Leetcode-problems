# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tot = 0
        que = deque([(root, str(root.val))])
        while que:
            val, str1 = que.popleft()
            if not val.left and not val.right:
                tot += int(str1)
            if val.left:
                que.append((val.left, str1 + str(val.left.val)))
            if val.right:
                que.append((val.right, str1 + str(val.right.val)))
        return tot
