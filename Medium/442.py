from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        dum = []
        for i in h:
            if h[i] == 2:
                dum.append(i)
        return dum
