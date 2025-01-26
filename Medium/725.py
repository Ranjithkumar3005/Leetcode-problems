# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        len1 = 0
        dummy = head

        while dummy:
            len1 += 1
            dummy = dummy.next

        size = len1 // k
        extra = len1 % k

        res = []
        current = head

        for i in range(k):
            part_head = current
            part_length = size + (1 if i < extra else 0)

            for j in range(part_length - 1):
                if current:
                    current = current.next
            if current:
                next = current.next
                current.next = None
                current = next

            res.append(part_head)
        return res
