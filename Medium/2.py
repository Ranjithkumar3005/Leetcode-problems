# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum_value = carry

            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next

            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next

            val = sum_value % 10
            carry = sum_value // 10

            if temp is None:
                head = temp = ListNode(val)
            else:
                temp.next = ListNode(val)
                temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        return head
