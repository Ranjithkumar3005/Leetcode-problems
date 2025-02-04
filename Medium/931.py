from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [row[:] for row in matrix]
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + matrix[i][j]
                elif j == cols - 1:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = (
                        min(dp[i + 1][j], dp[i + 1][j + 1], dp[i + 1][j - 1])
                        + matrix[i][j]
                    )

        return min(dp[0])
