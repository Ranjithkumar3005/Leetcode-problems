from collections import deque
from typing import List


class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        def bfs(start, end):
            if not blocked:
                return True
            block = set(map(tuple, blocked))
            queue = deque([tuple(start)])
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            visited = set([tuple(start)])
            limit = len(block) * (len(block) - 1) // 2

            while queue:
                x, y = queue.popleft()
                if (x, y) == tuple(end):
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < 10**6
                        and 0 <= ny < 10**6
                        and (nx, ny) not in visited
                        and (nx, ny) not in block
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                if len(visited) > limit:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)
