class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for i, n in enumerate(nums):

            while stack and stack[-1][0] < n:
                ele, idx = stack.pop()
                res[idx] = n
            stack.append((n, i))
        print(stack, res)
        if stack:
            for i, n in enumerate(nums):

                while stack and stack[-1][0] < n:
                    ele, idx = stack.pop()
                    res[idx] = n

        return res
