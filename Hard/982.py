from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        h = {}
        c = 0
        for i in nums:
            for j in nums:
                val = i & j
                if val in h:
                    h[val] += 1
                else:
                    h[val] = 1
        for i in nums:
            for j in h:
                if i & j == 0:
                    c += h[j]
        return c
