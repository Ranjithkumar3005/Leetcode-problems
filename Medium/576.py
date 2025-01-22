class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def dfs(i, j, remain):
            nonlocal dirs

            # base 1; infeasible
            if remain < 0:
                return 0
            # base 2; found one solution
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            # seen before
            if (i, j, remain) in memo:
                return memo[(i, j, remain)]

            # otherwise calculate memo[(i, j, remain)]
            res = 0
            for di, dj in dirs:
                di, dj = i + di, j + dj
                # recur on new indices
                res += dfs(di, dj, remain - 1)

            # final
            memo[(i, j, remain)] = res % kMod

            return memo[(i, j, remain)]

        kMod = 10**9 + 7
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # memo[(i, j, remain)] := total number of possible move at (i, j) with maximum remaining moves
        memo = dict()

        return dfs(startRow, startColumn, maxMove)
