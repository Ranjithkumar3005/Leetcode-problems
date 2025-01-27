from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max(nums)
        for i in nums:
            if i == max1 or i == 0:
                continue
            if max1 // i >= 2:
                continue
            else:
                return -1
        return nums.index(max1)
