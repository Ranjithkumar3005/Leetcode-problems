# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next  # First node of the pair
            second = current.next.next  # Second node of the pair

            # Perform the swap
            first.next = second.next  # Link first to the node after second
            current.next = second  # Link current to the second node
            second.next = first  # Link second to the first node

            # Move the current pointer forward by two nodes
            current = first

        return dummy.next  # Return the new head of the swapped list
