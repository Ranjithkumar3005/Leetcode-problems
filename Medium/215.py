import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = {}
        arr = []
        for i in nums:
            heapq.heappush(arr, -i)
        val = 0
        while k != 0:
            val = -heapq.heappop(arr)
            k -= 1
        return val


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        return nums[k - 1]
