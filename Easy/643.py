from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre = 0
        max1 = float("-inf")
        for i in range(0, len(nums)):
            pre += nums[i]
            if i >= k - 1:
                max1 = max(max1, (float(pre) / k))
                pre -= nums[i - k + 1]
        return max1
