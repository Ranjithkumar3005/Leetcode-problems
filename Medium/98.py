# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Sol 1
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(root, -float("inf"), float("inf"))]
        while stack:
            cur, low, high = stack.pop()

            if not low < cur.val < high:
                return False

            if cur.left:
                stack.append((cur.left, low, cur.val))
            if cur.right:
                stack.append((cur.right, cur.val, high))
        return True


# Sol 2.
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def isValid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return isValid(node.left, left, node.val) and isValid(
                node.right, node.val, right
            )

        return isValid(root, float("-inf"), float("inf"))


# Sol 3
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    def inorder(self, root, output):
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
