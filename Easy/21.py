# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ori = ListNode()
        dum = ori
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 > val2:
                dum.next = ListNode(val2)
                list2 = list2.next
            else:
                dum.next = ListNode(val1)
                list1 = list1.next
            dum = dum.next
        if list1 and not list2:
            dum.next = list1

        elif list2 and not list1:
            dum.next = list2
        return ori.next
