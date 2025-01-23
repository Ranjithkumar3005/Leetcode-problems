# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        dum = []
        que = deque([root])
        while que:
            sum1 = 0
            d = 0
            c = len(que)
            for i in range(c):
                val = que.popleft()
                sum1 += val.val
                if val.left:
                    que.append(val.left)
                if val.right:
                    que.append(val.right)
            dum.append(float(sum1) / c)
        return dum
