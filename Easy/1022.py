# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tot = 0
        que = deque([(root, str(root.val))])
        while que:
            node, val = que.popleft()
            if not node.left and not node.right:
                tot += int(val, 2)
            if node.left:
                que.append((node.left, val + str(node.left.val)))
            if node.right:
                que.append((node.right, val + str(node.right.val)))
        return tot
