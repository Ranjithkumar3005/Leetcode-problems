class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 1
        c = 1
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                c += 1
            else:
                max1 = max(max1, c)
                c = 1
        max1 = max(max1, c)
        return max1
