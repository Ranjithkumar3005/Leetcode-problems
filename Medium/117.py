"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            nextLevel = []
            for i in range(len(level)):
                node = level[i]
                if i != 0:
                    prevNode = level[i - 1]
                    prevNode.next = node
                    node.next = None

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                queue.append(nextLevel)
        return root
