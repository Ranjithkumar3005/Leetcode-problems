from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones

        return ones


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in h:
            if h[i] == 1:
                return i
