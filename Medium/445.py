# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head1, head2 = l1, l2
        num1, num2 = 0, 0

        while head1:
            num1 = num1 * 10 + head1.val
            head1 = head1.next

        while head2:
            num2 = num2 * 10 + head2.val
            head2 = head2.next

        num = str(num1 + num2)

        curr = head = ListNode()
        for dig in num:
            curr.next = ListNode(int(dig))
            curr = curr.next

        return head.next
