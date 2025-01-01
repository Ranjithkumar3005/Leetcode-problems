from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set()
        negDig = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for i in range(n):
                if i in col or (r + i) in posDig or (r - i) in negDig:
                    continue
                board[r][i] = "Q"
                col.add(i)
                posDig.add(r + i)
                negDig.add(r - i)
                backtrack(r + 1)

                col.remove(i)
                posDig.remove(r + i)
                negDig.remove(r - i)
                board[r][i] = "."

        backtrack(0)
        return res
