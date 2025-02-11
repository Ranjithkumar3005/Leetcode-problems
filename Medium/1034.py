from collections import deque
from typing import List


class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = set()
        borders = []
        queue = deque([(row, col)])
        visited.add((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] != original_color:
                    is_border = True
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            if is_border:
                borders.append((r, c))

        print(borders)
        for r, c in borders:
            grid[r][c] = color

        return grid
