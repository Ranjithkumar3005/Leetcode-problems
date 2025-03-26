# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        dum = []
        dummy = head
        while dummy != None:
            dum.append(dummy.val)
            dummy = dummy.next

        for i in range(0, len(dum) // 2):
            head.val = dum[i]
            head = head.next
            head.val = dum[len(dum) - i - 1]
            head = head.next

        if len(dum) % 2 != 0:
            head.val = dum[len(dum) / 2]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
