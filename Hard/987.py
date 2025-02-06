from collections import deque, defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = defaultdict(list)
        que = deque([(root, 0, 0)])  # (node, row, col)

        while que:
            node, r, c = que.popleft()
            h[c].append((r, node.val))  # Store both row and value

            if node.left:
                que.append((node.left, r + 1, c - 1))
            if node.right:
                que.append((node.right, r + 1, c + 1))

        result = []
        for col in sorted(h.keys()):  # Sort by column index
            # Sort by (row index, value)
            result.append([val for r, val in sorted(h[col])])

        return result
