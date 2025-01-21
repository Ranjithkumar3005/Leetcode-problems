# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        h = {}
        dum = deque([root])
        while dum:
            dum1 = dum.popleft()
            if dum1.val in h:
                h[dum1.val] += 1
            else:
                h[dum1.val] = 1
            if dum1.left:
                dum.append(dum1.left)
            if dum1.right:
                dum.append(dum1.right)
        max1 = max(h.values())
        chec = []
        for i in h:
            if h[i] == max1:
                chec.append(i)
        return chec
