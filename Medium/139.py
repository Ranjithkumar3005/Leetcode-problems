from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in wordSet and backtrack(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return backtrack(0)
