from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None

        if not root1:
            return root2
        if not root2:
            return root1

        merged_root = TreeNode(root1.val + root2.val)

        que1 = deque([root1])
        que2 = deque([root2])
        que_merged = deque([merged_root])

        while que1 and que2:
            node1 = que1.popleft()
            node2 = que2.popleft()
            merged_node = que_merged.popleft()

            if node1.left and node2.left:
                merged_left = TreeNode(node1.left.val + node2.left.val)
                merged_node.left = merged_left
                que1.append(node1.left)
                que2.append(node2.left)
                que_merged.append(merged_left)
            elif node1.left:
                merged_node.left = node1.left
            elif node2.left:
                merged_node.left = node2.left

            if node1.right and node2.right:
                merged_right = TreeNode(node1.right.val + node2.right.val)
                merged_node.right = merged_right
                que1.append(node1.right)
                que2.append(node2.right)
                que_merged.append(merged_right)
            elif node1.right:
                merged_node.right = node1.right
            elif node2.right:
                merged_node.right = node2.right

        return merged_root
