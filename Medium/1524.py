from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr = 0
        MOD = 10**9 + 7
        eve = 1
        odd = 0
        res = 0
        for i in arr:
            curr += i
            if curr % 2 == 0:
                res = (res + odd) % MOD
                eve += 1
            else:
                res = (res + eve) % MOD
                odd += 1
        return res
