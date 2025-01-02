# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy = M = ListNode()
        d1 = L = ListNode()

        while head:
            if head.val < x:
                L.next = head
                L = L.next
            else:
                M.next = head
                M = M.next
            head = head.next
        L.next = dummy.next
        M.next = None

        return d1.next
