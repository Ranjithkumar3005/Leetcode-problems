# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def post(self, root, ans):
        if root:
            self.post(root.left, ans)
            self.post(root.right, ans)
            ans.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.post(root, ans)
        return ans
