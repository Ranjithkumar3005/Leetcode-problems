from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] ^ nums[i + 1] != 0:
                return nums[i]
        return nums[-1]
