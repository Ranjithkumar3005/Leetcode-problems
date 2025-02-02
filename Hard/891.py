class Solution(object):
    def sumSubseqWidths(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % MOD

        total = 0
        for i in range(n):
            total = (total + nums[i] * (pow2[i] - pow2[n - i - 1])) % MOD

        return total
