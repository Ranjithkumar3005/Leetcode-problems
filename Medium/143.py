# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
