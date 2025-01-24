import heapq
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()

        def bfs(sx, sy, tx, ty):
            queue = [(0, sx, sy)]
            visited = set()
            visited.add((sx, sy))
            while queue:
                d, x, y = heapq.heappop(queue)
                if x == tx and y == ty:
                    return d
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and (nx, ny) not in visited
                        and forest[nx][ny]
                    ):
                        visited.add((nx, ny))
                        heapq.heappush(queue, (d + 1, nx, ny))
            return -1

        ans = 0
        sx, sy = 0, 0
        for _, tx, ty in trees:
            d = bfs(sx, sy, tx, ty)
            if d == -1:
                return -1
            ans += d
            sx, sy = tx, ty
        return ans
