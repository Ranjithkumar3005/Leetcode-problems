# Python3 Code
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ptr = TreeNode()
        res = ptr

        def inorder(node):
            nonlocal ptr
            if not node:
                return

            inorder(node.left)
            ptr.right = TreeNode(node.val)
            ptr = ptr.right
            inorder(node.right)

        inorder(root)
        return res.right
