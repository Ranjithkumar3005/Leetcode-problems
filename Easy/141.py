# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        while head:
            if head.next in h:
                return True
            h[head.next] = 0
            head = head.next
        return False
