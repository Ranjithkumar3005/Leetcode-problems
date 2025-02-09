# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        ptr = 0

        cur = head
        while cur:
            while stack and cur.val > stack[-1][1]:
                pttr, val = stack.pop()
                res[pttr] = cur.val
            stack.append([ptr, cur.val])
            res.append(0)
            ptr += 1
            cur = cur.next
            # print(stack, res)
        # print("SEPARATOR")
        return res
