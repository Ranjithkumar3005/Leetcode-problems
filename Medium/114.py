from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []

        def traverse(node):
            if not node:
                return
            result.append(node)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        # Now we will use the result to flatten the tree
        for i in range(len(result) - 1):
            # For each node, set the left child to None and the right child to the next node in result
            result[i].left = None
            result[i].right = result[i + 1]

        # Ensure the last node points to None
        if result:
            result[-1].left = None
            result[-1].right = None
