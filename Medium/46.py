class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(temp):
        if len(temp) == len(nums):
            result.append(temp[:])  # Add a copy of temp to the result
            return
        for num in nums:
            if num not in temp:  # Ensure uniqueness
                temp.append(num)
                backtrack(temp)
                temp.pop()  # Backtrack

    result = []
    backtrack([])
    return result


nums = [1, 2, 3]
print(permute(nums))
