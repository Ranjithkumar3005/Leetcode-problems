# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        st = []

        while head:
            st.append(head.val)
            head = head.next

        st = sorted(st)
        dum = ListNode()
        d = dum
        for i in range(0, len(st)):
            d.next = ListNode(st[i])
            d = d.next
        return dum.next
