from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()  # Set to track fresh oranges
        que = deque()  # Queue for BFS

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i, j, 0))  # (x, y, time)
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        time = 0
        while que:
            xi, xj, c = que.popleft()

            if not fresh:
                return time

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = xi + dx, xj + dy

                if (ni, nj) in fresh:
                    fresh.remove((ni, nj))
                    que.append((ni, nj, c + 1))
                    time = c + 1
        return -1 if fresh else time
