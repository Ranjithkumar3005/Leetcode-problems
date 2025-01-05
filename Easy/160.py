# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        h = {}
        while headA:
            h[headA] = 0
            headA = headA.next
        node = None
        check = True
        while headB:
            if headB in h:
                if check:
                    node = headB
                check = False
            else:
                node = None
                check = True
            headB = headB.next
        return node
