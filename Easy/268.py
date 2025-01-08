class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        ans1 = n * (n + 1) // 2
        ans2 = sum(nums)
        return ans1 - ans2


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i not in nums:
                return i
            i += 1
        return i
