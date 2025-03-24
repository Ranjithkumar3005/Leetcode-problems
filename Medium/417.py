from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Helper function for BFS
        def bfs(starts):
            visited = [[False] * n for _ in range(m)]
            queue = deque(starts)
            for r, c in starts:
                visited[r][c] = True

            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and not visited[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return visited

        # Start BFS from Pacific (top row and left column)
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        pacific_reachable = bfs(pacific_starts)

        # Start BFS from Atlantic (bottom row and right column)
        atlantic_starts = [(m - 1, c) for c in range(n)] + [
            (r, n - 1) for r in range(m)
        ]
        atlantic_reachable = bfs(atlantic_starts)

        # Find cells reachable by both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result
#