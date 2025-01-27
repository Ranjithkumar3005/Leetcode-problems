class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        count = 0
        last_count = 0
        last_invalid = -1

        for i, num in enumerate(nums):
            if num > right:
                last_count = 0
                last_invalid = i
            elif num >= left:
                last_count = i - last_invalid
            count += last_count

        return count
