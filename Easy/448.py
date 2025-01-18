class Solution(object):
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        result = [x for x in range(1, len(nums) + 1) if x not in s]
        return result
