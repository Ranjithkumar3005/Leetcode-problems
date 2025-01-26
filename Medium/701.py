# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        def bfs(root, val):
            if root.val > val:
                if root.left:
                    bfs(root.left, val)
                else:
                    root.left = TreeNode(val)
                    return
            else:
                if root.right:
                    bfs(root.right, val)
                else:
                    root.right = TreeNode(val)
                    return

        bfs(root, val)
        return root
