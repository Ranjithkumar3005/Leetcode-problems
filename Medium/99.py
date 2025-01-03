from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # Initialize a stack to simulate in-order traversal
        stack = deque()
        current = root
        prev = None
        first = second = None

        while stack or current:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Pop the node from the stack
            current = stack.pop()

            # If prev is not None and there's a violation
            if prev and prev.val > current.val:
                # If this is the first violation, store the first node
                if not first:
                    first = prev
                # Update the second node to the current node
                second = current

            # Update prev to the current node
            prev = current

            # Move to the right subtree
            current = current.right

        # Swap the values of the two nodes to recover the tree
        if first and second:
            first.val, second.val = second.val, first.val
