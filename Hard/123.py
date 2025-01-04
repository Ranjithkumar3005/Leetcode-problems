from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_profit = [0] * n
        right_profit = [0] * n
        min1 = prices[0]
        for i in range(1, n):
            min1 = min(min1, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min1)

        max1 = prices[-1]
        for i in range(n - 2, -1, -1):
            max1 = max(max1, prices[i])
            right_profit[i] = max(right_profit[i + 1], max1 - prices[i])

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i])
        return max_profit
