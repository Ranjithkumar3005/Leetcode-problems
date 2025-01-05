from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsum = nums[0]
        maxsum = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                minsum, maxsum = maxsum, minsum

            minsum = min(nums[i], minsum * nums[i])
            maxsum = max(nums[i], maxsum * nums[i])
            res = max(maxsum, res)

        return res
