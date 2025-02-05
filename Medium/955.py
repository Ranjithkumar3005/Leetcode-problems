from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])

        cur = ["" for i in range(m)]
        res = 0

        for i in range(n):
            temp = [x for x in cur]
            valid = True

            temp[0] += strs[0][i]
            for j in range(1, m):
                temp[j] += strs[j][i]
                if temp[j] < temp[j - 1]:
                    res += 1
                    valid = False
                    break

            if valid:
                cur = temp

        return res
