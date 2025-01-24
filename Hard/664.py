class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = float("inf")
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        # The minimum number of turns needed to print the entire string s is stored in dp[0][n-1]
        return dp[0][n - 1]
