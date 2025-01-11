# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = ListNode()
        dum = odd
        even = ListNode()
        dum1 = even
        i = 1
        while head:
            if i % 2 == 1:
                dum.next = head
                dum = dum.next
            else:
                dum1.next = head
                dum1 = dum1.next
            i += 1
            head = head.next
        dum1.next = None
        dum.next = even.next
        return odd.next
