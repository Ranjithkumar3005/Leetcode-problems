# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = {}
        while head:
            if head.next in h:
                return head.next
            h[head] = 0
            head = head.next
        return None
