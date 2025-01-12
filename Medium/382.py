# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random


class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self):
        """
        :rtype: int
        """
        len1 = len(self.arr)
        rand = random.randint(0, len1 - 1)
        return self.arr[rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
