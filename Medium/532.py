from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:  # Check for empty input
            return 0

        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        res = 0
        if k == 0:
            for i in h:
                if h[i] > 1:
                    res += 1
            return res

        vis = set()
        for i in nums:
            if i not in vis:
                vis.add(i)
                tot = i + k
                if tot in h:
                    res += 1  # Count unique pairs
        return res
