from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        que = deque([(0, 0, 1)])
        visited = set((0, 0))
        while que:
            x, y, len1 = que.popleft()
            if (x, y) == (n - 1, n - 1):
                return len1
            for dx, dy in directions:
                x1 = x + dx
                y1 = y + dy
                if (
                    0 <= x1 < n
                    and 0 <= y1 < n
                    and grid[x1][y1] == 0
                    and (x1, y1) not in visited
                ):
                    visited.add((x1, y1))
                    que.append((x1, y1, len1 + 1))
        return -1
