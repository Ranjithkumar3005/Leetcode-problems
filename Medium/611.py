from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:  # Valid triangle condition
                    count += j - i  # All pairs (i, i+1, ..., j) with j are valid
                    j -= 1  # Move the right pointer left
                else:
                    i += 1  # Move the left pointer right

        return count
