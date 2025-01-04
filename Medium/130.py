from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            board[row][col] = "#"  # Mark as visited
            while queue:
                r, c = queue.popleft()
                for dr, dc in [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                ]:  # Explore 4 directions
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        board[nr][nc] = "#"  # Mark as visited
                        queue.append((nr, nc))

        # Mark all 'O's connected to the boundary
        for i in range(rows):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][cols - 1] == "O":
                bfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == "O":
                bfs(0, j)
            if board[rows - 1][j] == "O":
                bfs(rows - 1, j)

        # Convert the remaining 'O's to 'X' and '#' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
