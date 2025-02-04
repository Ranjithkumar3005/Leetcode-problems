from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float("-inf")  # Initialize max_sum to the smallest possible value
        current_max = 0  # Variable to keep track of the current maximum subarray sum
        min_sum = float("inf")  # Initialize min_sum to the largest possible value
        current_min = 0  # Variable to keep track of the current minimum subarray sum
        total_sum = 0  # Variable to keep track of the total sum of the array

        for num in nums:
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

            total_sum += num

        return max_sum if total_sum == min_sum else max(max_sum, total_sum - min_sum)
