from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            if c < 2 or nums[i] != nums[c - 2]:
                nums[c] = nums[i]
                c += 1
        return c
