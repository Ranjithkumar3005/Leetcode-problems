class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipCount = 0
        oneCount = 0

        for i in range(len(s)):
            if s[i] == "1":
                oneCount += 1
            else:
                flipCount = min(flipCount + 1, oneCount)

        return flipCount
