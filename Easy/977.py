class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum = []
        for i in nums:
            dum.append(i**2)
        return sorted(dum)
