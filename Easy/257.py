# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        dum = []
        que = deque([(root, str(root.val))])
        while que:
            val, path = que.popleft()
            if not val.left and not val.right:
                dum.append(path)
            if val.left:
                que.append((val.left, path + "->" + str(val.left.val)))
            if val.right:
                que.append((val.right, path + "->" + str(val.right.val)))
        return dum
