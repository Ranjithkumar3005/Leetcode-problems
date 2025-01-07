# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum = ListNode()
        d = dum
        while head:
            if head.val != val:
                d.next = ListNode(head.val)
                d = d.next
            head = head.next

        return dum.next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return dummy.next  # remember that dummy is a node that we won't delete
