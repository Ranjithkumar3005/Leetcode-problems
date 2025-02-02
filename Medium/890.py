from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        dum = []
        for i in words:
            h = {}
            h1 = {}
            check = True
            for j in range(0, len(pattern)):
                if pattern[j] in h:
                    if h[pattern[j]] != i[j]:
                        check = False
                        break
                else:
                    if i[j] in h1:
                        check = False
                        break
                    h1[i[j]] = 0
                    h[pattern[j]] = i[j]
            if check:
                dum.append(i)
        return dum
