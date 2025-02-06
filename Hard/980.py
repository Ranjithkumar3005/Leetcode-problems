from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty_squares = 1
        start_x = start_y = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_squares += 1

        self.count = 0

        def backtrack(i, j, remaining):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == -1:
                return

            if grid[i][j] == 2:
                if remaining == 0:
                    self.count += 1
                return

            grid[i][j] = -1
            backtrack(i + 1, j, remaining - 1)
            backtrack(i - 1, j, remaining - 1)
            backtrack(i, j + 1, remaining - 1)
            backtrack(i, j - 1, remaining - 1)
            grid[i][j] = 0

        backtrack(start_x, start_y, empty_squares)
        return self.count
