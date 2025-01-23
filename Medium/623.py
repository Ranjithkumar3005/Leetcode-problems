# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        queue = deque([root])
        currentDepth = 1

        while queue:
            level_size = len(queue)

            if currentDepth == depth - 1:
                for _ in range(level_size):
                    node = queue.popleft()

                    old_left = node.left
                    node.left = TreeNode(val)
                    node.left.left = old_left

                    old_right = node.right
                    node.right = TreeNode(val)
                    node.right.right = old_right

                break
            else:
                for _ in range(level_size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                currentDepth += 1

        return root
