# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        count = 0
        is_in_component = False
        while head:
            if head.val in num_set:
                if not is_in_component:
                    count += 1
                    is_in_component = True
            else:
                is_in_component = False
            head = head.next

        return count
