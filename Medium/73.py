from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hr = {}
        hc = {}
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    hr[i] = 0
                    hc[j] = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in hr or j in hc:
                    matrix[i][j] = 0
