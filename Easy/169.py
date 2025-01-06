class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in range(0, len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        maxi = max(h.values())
        for i in h:
            if h[i] == maxi:
                return i
