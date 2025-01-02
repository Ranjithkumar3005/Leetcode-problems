class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty or has only one node, no need to remove duplicates
        if not head:
            return head

        current = head
        while current and current.next:
            # If current node value is same as next node value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
