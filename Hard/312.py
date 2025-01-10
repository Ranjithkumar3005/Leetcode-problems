from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add padding to the input array
        nums = [1] + nums + [1]
        n = len(nums)
        # Initialize a dp table to store the maximum coins for subproblems
        dp = [[0] * n for _ in range(n)]

        # Iterate the input array in reverse order to fill the dp table
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                # Iterate k from i+1 to j-1 to find the last balloon to burst
                for k in range(i + 1, j):
                    # Compute the maximum coins for subproblems
                    dp[i][j] = max(
                        dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    )

        # The result is the maximum coins for the original problem
        return dp[0][n - 1]
