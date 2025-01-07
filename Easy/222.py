# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        c = 0
        que = deque([root])

        while que:
            val = que.popleft()
            c += 1
            if val.left:
                que.append(val.left)
            if val.right:
                que.append(val.right)

        return c
