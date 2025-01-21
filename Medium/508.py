from collections import defaultdict
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sum_count = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum

            sum_count[subtree_sum] += 1

            return subtree_sum

        dfs(root)

        max_frequency = max(sum_count.values())
        result = [s for s, count in sum_count.items() if count == max_frequency]

        return result
