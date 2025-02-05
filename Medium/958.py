from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        end = False
        while queue:
            current = queue.popleft()
            if current.left:
                if end:
                    return False
                queue.append(current.left)
            else:
                end = True
            if current.right:
                if end:
                    return False
                queue.append(current.right)
            else:
                end = True
        return True
