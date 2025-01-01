# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return None

        # first traverse locate end node and list length
        prev, cur, end = head, head, head
        length = 1

        while end.next:
            end = end.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # second traverse locate the last (k + 1) node
        for _ in range(length - k - 1):
            prev = prev.next
        cur = prev.next
        # disconnect prev node with cur node, and link end node to head, cur become new head node
        prev.next = None
        end.next = head

        return cur
