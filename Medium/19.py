# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        copy = head
        while copy:
            length += 1
            copy = copy.next

        prev = head
        remove_idx = length - n
        if length == 1 or remove_idx == 0:  # if only one node, or removing first node
            return head.next
        for i in range(remove_idx - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head
