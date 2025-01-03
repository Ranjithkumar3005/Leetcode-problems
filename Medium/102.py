# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dum = []
        que = deque([root])
        while que:
            len1 = len(que)
            ch = []
            for i in range(len1):
                val = que.popleft()
                ch.append(val.val)
                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)
            dum.append(ch)
        return dum
