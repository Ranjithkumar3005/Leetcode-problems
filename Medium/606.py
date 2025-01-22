# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        return self.dfs(root)

    def dfs(self, node: Optional[TreeNode]) -> str:
        if not node:
            return ""

        result = str(node.val)

        if node.left or node.right:
            result += "(" + self.dfs(node.left) + ")"

        if node.right:
            result += "(" + self.dfs(node.right) + ")"

        return result
