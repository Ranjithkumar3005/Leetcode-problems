# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        que = deque([(root, False)])
        sum1 = 0
        while que:
            node, check = que.popleft()
            if check and not node.left and not node.right:
                sum1 += node.val
            if node.left:
                que.append((node.left, True))
            if node.right:
                que.append((node.right, False))
        return sum1
