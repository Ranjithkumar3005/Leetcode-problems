from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        h = {}
        for i in words:
            eve = ""
            odd = ""
            for j in range(0, len(i)):
                if j % 2 == 0:
                    eve += i[j]
                else:
                    odd += i[j]
            dum = "".join(sorted(eve) + sorted(odd))
            h[dum] = 1
        return len(h)
