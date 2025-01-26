from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        dum = []
        for i in range(left, right + 1):
            val1 = str(i)
            if "0" in val1:
                continue
            c = 0
            for j in val1:
                if i % int(j) == 0:
                    c += 1
                else:
                    break
            if c == len(val1):
                dum.append(i)
        return dum
