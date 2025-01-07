from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, arr, tot):
            if len(arr) == k:
                if tot == n:
                    res.append(arr[:])
                return
            for i in range(start, 9):
                arr.append(i + 1)
                backtrack(i + 1, arr, tot + i + 1)
                arr.pop()

        backtrack(0, [], 0)
        return res
