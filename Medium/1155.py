class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * target for _ in range(2)]
        MOD = 10**9 + 7
        for i in range(min(target, k)):
            dp[0][i] = 1
        for i in range(1, n):
            s = 0
            for j in range(target):
                if j >= i:
                    dp[1][j] = s
                s += dp[0][j]
                if j >= k:
                    s -= dp[0][j - k]
            dp[0] = dp[1]
            dp[1] = [0] * target

        return dp[0][target - 1] % MOD


class Solution:
    mod = 10**9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)

    def recursion(self, dp: list, n: int, k: int, target: int) -> int:
        if target == 0 and n == 0:
            return 1
        if n == 0 or target <= 0:
            return 0

        if dp[n][target] != -1:
            return dp[n][target] % self.mod

        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod

        dp[n][target] = ways % self.mod
        return dp[n][target]
