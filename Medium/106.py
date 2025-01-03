# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(postorder, inorder):
            if not postorder:
                return None
            if inorder:
                idx = inorder.index(postorder.pop())
                root = TreeNode(inorder[idx])
                root.right = build(postorder, inorder[idx + 1 :])
                root.left = build(postorder, inorder[:idx])

                return root

        return build(postorder, inorder)
