import heapq
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        dum = [1] * n
        val = []

        for i in range(n):
            heapq.heappush(val, (ratings[i], i))

        while val:
            rate, idx = heapq.heappop(val)

            if idx > 0 and ratings[idx] > ratings[idx - 1]:
                dum[idx] = dum[idx - 1] + 1
            if idx < n - 1 and ratings[idx] > ratings[idx + 1]:
                dum[idx] = max(dum[idx], dum[idx + 1] + 1)

        return sum(dum)
