# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        arr = []
        while que:
            len1 = len(que)
            val = None
            for i in range(len1):
                val = que.popleft()
                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)
            if val != None:
                arr.append(val.val)
        return arr
