from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = sum(row.count("X") for row in board)
        o = sum(row.count("O") for row in board)

        if x - o not in (0, 1):
            return False

        transpose = [a + b + c for a, b, c in zip(*board)]
        all_wins = (
            board
            + transpose
            + [board[0][0] + board[1][1] + board[2][2]]
            + [board[0][2] + board[1][1] + board[2][0]]
        )

        if "XXX" in all_wins and "OOO" in all_wins:
            return False
        if "OOO" in all_wins:
            return x == o
        if "XXX" in all_wins:
            return x > o
        return True
