from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        n = len(nums)
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        res = []
        for key, value in h.items():
            if value > n / 3:
                res.append(key)
        return res
