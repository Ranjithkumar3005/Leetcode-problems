from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle using backtracking with optimizations.
        """
        # Precompute sets to track used numbers in each row, column, and subgrid
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        # Fill in the sets with the current numbers on the board
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[(r // 3) * 3 + c // 3].add(num)

        # Function to check if placing a number in a cell is valid
        def is_safe(r, c, num):
            if (
                num in rows[r]
                or num in cols[c]
                or num in subgrids[(r // 3) * 3 + c // 3]
            ):
                return False
            return True

        # Function to find the cell with the fewest possible valid choices
        def get_next_empty():
            min_options = float("inf")
            min_cell = None
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        # Count possible valid numbers
                        valid_options = 0
                        for num in "123456789":
                            if is_safe(r, c, num):
                                valid_options += 1
                        if valid_options < min_options:
                            min_options = valid_options
                            min_cell = (r, c)
            return min_cell

        # Backtracking function to solve the puzzle
        def backtrack():
            cell = get_next_empty()
            if not cell:
                return True  # If there is no empty cell, the board is solved
            r, c = cell

            # Try placing numbers from '1' to '9'
            for num in "123456789":
                if is_safe(r, c, num):
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[(r // 3) * 3 + c // 3].add(num)

                    # Recursively solve the rest of the board
                    if backtrack():
                        return True

                    # Backtrack: remove the number
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    subgrids[(r // 3) * 3 + c // 3].remove(num)

            return False

        # Start the backtracking process
        backtrack()
