class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            res = min(
                res, max(nums[-1] - k, nums[i] + k) - min(nums[0] + k, nums[i + 1] - k)
            )
        return res
