# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Variables to track the minimum difference and the previous node value
        self.min_diff = float("inf")
        self.prev_val = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val

            inorder(node.right)

        inorder(root)

        return self.min_diff
