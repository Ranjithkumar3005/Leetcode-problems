class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nums = sorted(heights)
        c = 0
        for i in range(0, len(heights)):
            if heights[i] != nums[i]:
                c += 1
        return c
