class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        L = 0
        total = 0

        length = float("inf")

        for R in range(n):
            total += nums[R]

            while total >= target:

                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1

        return 0 if length == float("inf") else length
