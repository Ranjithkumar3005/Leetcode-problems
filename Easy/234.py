# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp = head
        llval = []
        while temp:
            llval.append(temp.val)
            temp = temp.next
        while head:
            if llval[-1] == head.val:
                llval.pop()
            else:
                return False
            head = head.next

        if len(llval) == 0:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, head):
        slow, fast, rev = head, head, None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return rev == None
