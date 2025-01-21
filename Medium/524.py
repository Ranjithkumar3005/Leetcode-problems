from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        def in_word(a, b):
            h = a.find(b[0])
            if h == -1:
                return False
            if len(b) == 1:
                return True
            return in_word(a[h + 1 :], b[1:])

        for i in range(len(d)):
            if len(d[i]) > len(s):
                continue
            if len(d[i]) == len(s):
                if s != d[i]:
                    continue
                else:
                    return d[i]
            if in_word(s, d[i]):
                return d[i]

        return ""
