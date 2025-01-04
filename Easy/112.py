from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        que = deque([(root, root.val)])  # Queue stores (node, cumulative sum)

        while que:
            node, current_sum = que.popleft()

            if not node.left and not node.right and current_sum == targetSum:
                return True

            if node.left:
                que.append((node.left, current_sum + node.left.val))

            if node.right:
                que.append((node.right, current_sum + node.right.val))

        return False
