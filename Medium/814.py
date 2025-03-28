# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def prune(node):
            if not node:
                return None

            node.left = prune(node.left)
            node.right = prune(node.right)

            if node.val == 0 and not node.left and not node.right:
                return None

            return node

        return prune(root)
