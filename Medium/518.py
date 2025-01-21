from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array with 0. dp[i] will store the number of ways to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: There's 1 way to make amount 0 (by choosing no coins)

        # Loop through each coin
        for coin in coins:
            # For each coin, update the dp array for all amounts from coin to amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        # Return the number of ways to make amount
        return dp[amount]
