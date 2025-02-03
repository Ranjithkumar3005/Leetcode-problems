class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[r], nums[left] = nums[left], nums[r]
                left += 1
        return nums
