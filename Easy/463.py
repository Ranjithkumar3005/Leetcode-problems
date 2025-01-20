from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        hashset = set()
        count = 0
        col_length = len(grid[0])
        for row in range(len(grid)):
            for col in range(col_length):
                if grid[row][col] == 1:
                    count += 4
                    if (row, col - 1) in hashset:
                        count -= 2
                    if (row - 1, col) in hashset:
                        count -= 2
                    hashset.add((row, col))
        return count
