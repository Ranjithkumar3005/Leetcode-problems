# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        parent = {root: None}
        last_level = []
        while queue:
            last_level = list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)
        deepest_nodes = set(last_level)

        while len(deepest_nodes) > 1:
            new_deepest_nodes = set()
            for node in deepest_nodes:
                new_deepest_nodes.add(parent[node])
            deepest_nodes = new_deepest_nodes

        return deepest_nodes.pop()
