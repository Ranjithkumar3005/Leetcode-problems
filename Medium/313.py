from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        n -= 1
        pool = primes.copy()
        heapify(pool)
        for _ in range(n - 1):
            num = heappop(pool)
            for prime in primes:
                heappush(pool, num * prime)
                if not num % prime:
                    break
        return pool[0]
