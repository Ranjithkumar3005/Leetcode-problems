from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        pre = []
        n = len(values)
        for i in range(0, n):
            pre.append(values[i] + i)
        suf = [0] * (n - 1)
        suf.append(values[n - 1] - (n - 1))
        for j in range(len(values) - 2, -1, -1):
            suf[j] = max(suf[j + 1], values[j] - j)
        max1 = 0
        for i in range(1, n):
            max1 = max(max1, pre[i - 1] + suf[i])
        return max1
