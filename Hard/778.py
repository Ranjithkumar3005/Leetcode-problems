import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # at time t, the depth of the water everywhere is t
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        if not grid:
            return 0
        # can swim infinite distances in zero time
        min_heap = [(grid[0][0], 0, 0)]  # time, row, col
        visited = set()
        visited.add((0, 0))
        while min_heap:
            time, row, col = heapq.heappop(min_heap)
            if row == ROWS - 1 and col == COLS - 1:
                return time
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if (
                    new_r < 0
                    or new_r >= ROWS
                    or new_c < 0
                    or new_c >= COLS
                    or (new_r, new_c) in visited
                ):
                    continue
                else:
                    visited.add((new_r, new_c))
                    wait_time = max(time, grid[new_r][new_c])
                    heapq.heappush(min_heap, (wait_time, new_r, new_c))
        return -1
