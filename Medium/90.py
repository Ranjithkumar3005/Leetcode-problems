from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        visited = set()
        nums.sort()

        def backtrack(curr, i):
            if len(curr) == len(nums):
                return
            for k in range(i, len(nums)):
                curr.append(nums[k])
                if tuple(curr) not in visited:
                    res.append(curr[:])
                    visited.add(tuple(curr))
                backtrack(curr, k + 1)
                curr.pop()

        backtrack([], 0)
        return res
