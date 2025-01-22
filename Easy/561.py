class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        max1 = 0
        for i in range(0, len(nums), 2):
            max1 += nums[i + 1]
        return max1
