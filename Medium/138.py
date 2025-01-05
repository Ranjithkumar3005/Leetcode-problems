"""
# Definition for a Node.
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        h = {}
        curr = head
        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            h[curr].next = h.get(curr.next)
            h[curr].random = h.get(curr.random)
            curr = curr.next
        return h[head]
