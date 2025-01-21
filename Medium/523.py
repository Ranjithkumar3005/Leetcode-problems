class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            remainder = sum % k
            if remainder not in check:
                check[remainder] = i
            elif (i - check[remainder]) > 1:
                return True
        return False
