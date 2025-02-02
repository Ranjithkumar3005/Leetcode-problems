from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        for i in set(B):
            if i + diff in A:
                return [diff + i, i]
