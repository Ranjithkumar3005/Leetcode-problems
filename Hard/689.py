from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sums[0] = current_sum
        for i in range(1, len(window_sums)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = current_sum

        left = [0] * len(window_sums)
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * len(window_sums)
        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:
                best_right = i
            right[i] = best_right

        max_sum = 0
        result = []
        for mid in range(k, len(window_sums) - k):
            l, r = left[mid - k], right[mid + k]
            total_sum = window_sums[l] + window_sums[mid] + window_sums[r]
            if total_sum > max_sum:
                max_sum = total_sum
                result = [l, mid, r]
            elif total_sum == max_sum:
                result = min(result, [l, mid, r])  # Lexicographically smallest

        return result
