class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        def backtrack(curr, i):
            if len(curr) == len(nums):
                return
            for k in range(i, len(nums)):
                curr.append(nums[k])
                res.append(curr[:])
                backtrack(curr, k + 1)
                curr.pop()

        backtrack([], 0)
        return res
