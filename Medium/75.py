from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            idx = i
            min1 = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < min1:
                    idx = j
                    min1 = nums[j]
            tem = nums[i]
            nums[i] = nums[idx]
            nums[idx] = tem
