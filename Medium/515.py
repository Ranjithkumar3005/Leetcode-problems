from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # Handle empty tree

        arr = []
        que = deque([root])

        while que:
            dum = float("-inf")  # Initialize to negative infinity
            len1 = len(que)

            for i in range(len1):
                val = que.popleft()
                dum = max(dum, val.val)
                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)

            arr.append(dum)

        return arr
