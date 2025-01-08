class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i in h:
                return i
            h[i] = 1
