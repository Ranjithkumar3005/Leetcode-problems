from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min1 = min(nums)
        max1 = max(nums)
        val1 = min1 + k
        val2 = max1 - k
        if val1 >= val2:
            return 0
        return val2 - val1
