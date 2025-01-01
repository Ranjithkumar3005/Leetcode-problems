from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        d = []
        m1, m2 = len(matrix[0]), len(matrix)
        top, bottom, left, right = 0, m2 - 1, 0, m1 - 1
        while top <= bottom and left <= right:
            # Right
            for i in range(left, right + 1):
                d.append(matrix[top][i])
            top += 1

            # Bottom
            for i in range(top, bottom + 1):
                d.append(matrix[i][right])
            right -= 1

            # Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    d.append(matrix[bottom][i])
                bottom -= 1

            # Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    d.append(matrix[i][left])
                left += 1
        return d
