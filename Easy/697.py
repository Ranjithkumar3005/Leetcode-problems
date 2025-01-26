from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        freq = {}
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())
        start_indices = [i for i, freq in freq.items() if freq == max_freq]
        shortest_len = float("inf")
        for i in start_indices:
            val1 = 0
            val2 = 0
            for j in range(0, len(nums)):
                if nums[j] == i:
                    val1 = j
                    break
            for k in range(0, len(nums)):
                if nums[len(nums) - 1 - k] == i:
                    val2 = len(nums) - 1 - k
                    break
            shortest_len = min(shortest_len, val2 - val1 + 1)
        return shortest_len
