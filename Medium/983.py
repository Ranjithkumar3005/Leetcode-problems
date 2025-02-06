from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day = days[-1]
        dp = [0] * (day + 1)  # Initialize DP array with size equal to the last day + 1
        day_set = set(days)
        for i in range(1, day + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[i - 7] + costs[1] if i >= 7 else costs[1],  # 7-day pass
                    dp[i - 30] + costs[2] if i >= 30 else costs[2],  # 30-day pass
                )

        return dp[day]
