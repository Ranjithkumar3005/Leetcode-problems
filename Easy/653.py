from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        seen = set()  # Use a set to track visited values
        que = deque([root])  # Queue for level-order traversal

        while que:
            node = que.popleft()
            if k - node.val in seen:  # Check if the complement exists
                return True
            seen.add(node.val)  # Add the current node's value to the set
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return False  # Return False if no pair is found
