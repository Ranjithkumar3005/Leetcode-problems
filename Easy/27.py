from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        return c
