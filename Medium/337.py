class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            # Recursively solve for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]

            # If we do not rob this node, take the max of robbing or not robbing its children
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        # Start DFS from the root
        return max(dfs(root))
