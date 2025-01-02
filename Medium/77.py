from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]
        res = []

        def backtrack(curr, start):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return res
