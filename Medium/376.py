from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n < 2:
            return n

        c = 1  # Start with the first element
        max_length = 1  # The minimum wiggle sequence length is 1
        last_diff = 0  # Initialize the last difference

        for i in range(1, n):
            val = nums[i] - nums[i - 1]
            if val > 0 and last_diff <= 0:  # Upward wiggle
                c += 1
                last_diff = val
            elif val < 0 and last_diff >= 0:  # Downward wiggle
                c += 1
                last_diff = val

        return c
