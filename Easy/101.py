from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (
                p.val == q.val
                and isSameTree(p.left, q.right)
                and isSameTree(p.right, q.left)
            )

        if not root:
            return True
        return isSameTree(root.left, root.right)
