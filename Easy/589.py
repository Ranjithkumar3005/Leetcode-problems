# Python Code
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        res = []

        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                preOrder(child)

        preOrder(root)
        return res
