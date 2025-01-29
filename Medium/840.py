class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        if len(grid) < 2 or len(grid[0]) < 2:
            return 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                square = [row[j : j + 3] for row in grid[i : i + 3]]
                if max(max(row) for row in square) < 10 and square[1][1] == 5:
                    if (
                        sum(square[0]) == 15
                        and sum(square[1]) == 15
                        and square[0][0] + square[1][1] + square[2][2] == 15
                        and square[0][0] + square[1][0] + square[2][0] == 15
                        and square[0][1] + square[1][1] + square[2][1] == 15
                    ):
                        if {square[k][l] for k in range(3) for l in range(3)} == {
                            k for k in range(1, 10)
                        }:
                            count += 1
                            # return square
        return count
