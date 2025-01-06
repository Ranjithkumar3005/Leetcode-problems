class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is greater than n

        # Rotate the array using slicing
        nums[:] = nums[-k:] + nums[:-k]
