# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        h = {}  # Dictionary to track serialized subtrees and their counts
        arr = []  # List to store duplicate subtree roots

        def dfs(root):
            if not root:
                return "#"
            # Serialize the subtree: "node_val,left_subtree,right_subtree"
            left = dfs(root.left)
            right = dfs(root.right)
            serial = f"{root.val},{left},{right}"

            if serial in h:
                h[serial] += 1
                if h[serial] == 2:
                    arr.append(root)
            else:
                h[serial] = 1

            return serial

        dfs(root)
        return arr


from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # dum = {}
        dum1 = []
        visited = defaultdict(int)
        que = deque([root])

        while que:
            node = que.popleft()
            last = self.serialize(node)

            if visited[last] == 1:  # Check for duplicates
                # dum[last] = node
                dum1.append(node)
            visited[last] += 1  # Increment count of this subtree

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return dum1

    def serialize(self, node):
        if not node:
            return "#"  # Mark nulls to keep structure
        # Recursive serialization including value and structure of subtree
        return f"{node.val},{self.serialize(node.left)},{self.serialize(node.right)}"
