# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = deque([root])
        res = []
        check = False
        while que:
            len1 = len(que)
            curr = []
            for _ in range(len1):
                pl = que.popleft()
                curr.append(pl.val)
                if pl.left:
                    que.append(pl.left)
                if pl.right:
                    que.append(pl.right)
            if check:
                res.append(curr[::-1])
            else:
                res.append(curr)
            check = not check
        return res
