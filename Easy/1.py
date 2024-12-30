class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # save nums in a hash map
        dict = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in dict and dict[n] != i:
                return [i, dict[n]]
        return None
