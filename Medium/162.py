class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_ind = 0
        len_nums = len(nums)
        right_ind = len(nums) - 1
        while left_ind < right_ind:
            mid_ind = (left_ind + right_ind) // 2

            if nums[mid_ind] > nums[mid_ind + 1]:
                right_ind = mid_ind
            else:
                left_ind = mid_ind + 1

        return left_ind
