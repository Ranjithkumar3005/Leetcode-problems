class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if int(s[0]) == 0 else 1

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
