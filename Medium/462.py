from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        diff = 0
        n = len(nums)
        for i in range(0, n // 2):
            diff += abs(nums[i] - nums[n - i - 1])
        return diff
