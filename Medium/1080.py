from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None

        queue = deque([(root, root.val)])
        nodes_to_keep = set()

        while queue:
            node, current_sum = queue.popleft()

            if not node.left and not node.right:
                if current_sum >= limit:
                    nodes_to_keep.add(node)  # Keep this leaf
            else:
                if node.left:
                    queue.append((node.left, current_sum + node.left.val))
                if node.right:
                    queue.append((node.right, current_sum + node.right.val))

        def prune(node):
            if not node:
                return None
            node.left = prune(node.left)
            node.right = prune(node.right)

            if node not in nodes_to_keep and (not node.left and not node.right):
                return None
            return node

        return prune(root)
