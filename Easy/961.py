class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        lenght = len(nums)
        for i in h:
            if h[i] * 2 == lenght:
                return i
