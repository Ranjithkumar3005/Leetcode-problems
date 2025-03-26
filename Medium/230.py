# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

#


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        dum = []
        que = deque([root])
        while que:
            val1 = que.popleft()
            dum.append(val1.val)
            if val1.left:
                que.append(val1.left)
            if val1.right:
                que.append(val1.right)

        dum = sorted(dum)
        return dum[k - 1]


#
