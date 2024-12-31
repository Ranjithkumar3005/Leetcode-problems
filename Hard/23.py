# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(h, head.val)
                head = head.next
        dummy = ListNode(None)
        check = dummy
        while h:
            val = heapq.heappop(h)
            check.next = ListNode(val)
            check = check.next
        return dummy.next
