# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        sec_min = float("inf")

        def dfs(node):
            nonlocal sec_min
            if node:
                if root.val < node.val < sec_min:
                    sec_min = node.val
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if sec_min == float("inf"):
            return -1
        return sec_min
