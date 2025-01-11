from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i, j))

        cells.sort(reverse=True, key=lambda x: x[0])

        for val, x, y in cells:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[x][y]:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

        return max(max(row) for row in dp)
