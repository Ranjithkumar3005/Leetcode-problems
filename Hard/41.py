from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        val = set(nums)
        i = 1
        while True:
            if i not in val:
                return i
            i += 1
