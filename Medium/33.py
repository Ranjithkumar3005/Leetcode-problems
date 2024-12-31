class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:  # Target in the left sorted part
                    right = mid - 1
                else:  # Target in the right part
                    left = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[right]:  # Target in the right sorted part
                    left = mid + 1
                else:  # Target in the left part
                    right = mid - 1

        return -1  # Target not found
