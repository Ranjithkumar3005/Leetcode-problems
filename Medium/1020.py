from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        queue = deque()

        # **Step 1: Process only the boundary land cells**
        for i in range(rows):
            for j in [0, cols - 1]:  # Only left and right boundary
                if grid[i][j] == 1:
                    queue.append((i, j))
        for j in range(cols):
            for i in [0, rows - 1]:  # Only top and bottom boundary
                if grid[i][j] == 1:
                    queue.append((i, j))

        # **Step 2: BFS to mark all reachable land cells as visited**
        while queue:
            i, j = queue.popleft()
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = 0  # Mark as visited
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        queue.append((ni, nj))

        # **Step 3: Count remaining land cells (which are enclosed)**
        return sum(row.count(1) for row in grid)


# Example usage:
grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
solution = Solution()
print(solution.numEnclaves(grid))  # Output: 1
