from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Initialize the DP arrays
        length = [1] * n  # Length of LIS ending at each index
        count = [1] * n  # Count of LIS ending at each index

        # Compute length and count for each index
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        # Find the maximum length of LIS
        max_length = max(length)

        # Count the number of subsequences with the maximum length
        return sum(count[i] for i in range(n) if length[i] == max_length)
