from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        # Initialize directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        step = 1  # Number of steps in a single direction
        x, y = rStart, cStart  # Start position

        result.append([x, y])  # Add the starting cell
        total_cells = rows * cols  # Total cells to be covered

        while len(result) < total_cells:  # Continue until all cells are visited
            for d in range(4):  # Traverse in 4 directions
                dx, dy = directions[d]
                # Move 'step' times in the current direction
                for _ in range(step):
                    x += dx
                    y += dy
                    if 0 <= x < rows and 0 <= y < cols:  # Check if within bounds
                        result.append([x, y])
                # Increase step after every 2 directions (right-down or left-up)
                if d == 1 or d == 3:
                    step += 1

        return result


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        directions = [0, 1, 0, -1, 0]
        res = [[rStart, cStart]]
        j = n = 0
        while len(res) < rows * cols:
            for i in range(n // 2 + 1):
                rStart += directions[j]
                cStart += directions[j + 1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            n += 1
            j = (j + 1) % 4
        return res
