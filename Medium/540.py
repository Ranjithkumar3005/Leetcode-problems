from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums) - 1
        low = 1
        high = n - 1

        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n] != nums[n - 1]:
            return nums[n]

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (
                mid % 2 == 1 and nums[mid] == nums[mid - 1]
            ):

                low = mid + 1

            else:

                high = mid - 1
        return -1
