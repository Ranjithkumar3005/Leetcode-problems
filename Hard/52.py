class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
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

                col.add(i)
                posDig.add(r + i)
                negDig.add(r - i)
                board[r][i] = "Q"

                backtrack(r + 1)

                col.remove(i)
                posDig.remove(r + i)
                negDig.remove(r - i)
                board[r][i] = "."

        backtrack(0)
        return len(res)
