from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                arr[j][i] = matrix[i][j]
        return arr
