from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            sentences = []
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if prefix in wordSet:
                    rem = backtrack(end)
                    for sen in rem:
                        if sen:
                            sentences.append(prefix + " " + sen)
                        else:
                            sentences.append(prefix)
            memo[start] = sentences
            return sentences

        print(memo)
        return backtrack(0)
