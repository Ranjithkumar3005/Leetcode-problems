class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i is start position
        # j is end position
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if j == i + 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] == True:
                    count += 1
        return count
