class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        def dp(pos):
            if pos == len(s):
                return 1
            if pos in memo:
                return memo[pos]
            if s[pos] == "0":
                return 0
            res = 0
            if s[pos] == "*":
                res += 9 * dp(pos + 1)
            else:
                res += dp(pos + 1)

            if pos < len(s) - 1:
                if s[pos] == "*":
                    if s[pos + 1] == "*":
                        res += 15 * dp(pos + 2)
                    elif "0" <= s[pos + 1] <= "6":
                        res += 2 * dp(pos + 2)
                    else:
                        res += dp(pos + 2)

                elif s[pos] == "1":
                    if s[pos + 1] == "*":
                        res += 9 * dp(pos + 2)
                    else:
                        res += dp(pos + 2)
                elif s[pos] == "2":
                    if s[pos + 1] == "*":
                        res += 6 * dp(pos + 2)
                    elif "0" <= s[pos + 1] <= "6":
                        res += dp(pos + 2)

            memo[pos] = res % MOD
            return memo[pos]

        memo = {}
        return dp(0)
