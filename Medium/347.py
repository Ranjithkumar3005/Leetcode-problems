from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1

        arr = sorted(h.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in arr[:k]]
