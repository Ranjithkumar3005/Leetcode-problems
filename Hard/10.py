class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def check(s, p):
            dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
            dp[0][0] = True  # Empty pattern matches empty string

            # Handle cases where pattern has leading a* or a*b* etc.
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    dp[0][j] = dp[0][j - 2]

            for i in range(1, len(s) + 1):
                for j in range(1, len(p) + 1):
                    if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == "*":
                        # Check zero occurrence of the previous character
                        dp[i][j] = dp[i][j - 2]
                        # Check for one or more occurrences
                        if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                            dp[i][j] = dp[i][j] or dp[i - 1][j]

            return dp[len(s)][len(p)]

        return check(s, p)
