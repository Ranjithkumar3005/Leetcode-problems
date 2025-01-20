class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        memo = {}

        def can_win(remaining: tuple, current_total: int) -> bool:
            if remaining in memo:
                return memo[remaining]

            for i in range(len(remaining)):
                if current_total + remaining[i] >= desiredTotal or not can_win(
                    remaining[:i] + remaining[i + 1 :], current_total + remaining[i]
                ):
                    memo[remaining] = True
                    return True

            # If no winning move is found, return False
            memo[remaining] = False
            return False

        return can_win(tuple(range(1, maxChoosableInteger + 1)), 0)
