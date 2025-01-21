class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        def dfs(start, path):
            if len(path) >= 2:
                result.add(tuple(path))
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    dfs(i + 1, path)  # Move to the next element
                    path.pop()  # Backtrack

        dfs(0, [])
        return list(result)
