from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 1  # Store the level with max sum
        max_sum = root.val  # Store the max sum found
        que = deque([root])
        level = 1  # Track current level

        while que:
            level_sum = 0
            for _ in range(len(que)):  # Process all nodes at current level
                node = que.popleft()
                level_sum += node.val  # Sum values of current level

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            # If the sum of this level is greater than max_sum, update answer
            if level_sum > max_sum:
                max_sum = level_sum
                ans = level

            level += 1

        return ans
