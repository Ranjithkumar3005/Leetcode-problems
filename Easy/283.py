class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0  # Tracks the index to place non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_count] = nums[i]  # Move non-zero element forward
                non_zero_count += 1

        # Fill the rest of the list with zeroes
        for i in range(non_zero_count, len(nums)):
            nums[i] = 0

        return nums
