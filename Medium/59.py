class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        m1, m2 = len(matrix[0]), len(matrix)  # Define the boundaries
        top, bottom, left, right = 0, m2 - 1, 0, m1 - 1  # Initialize boundaries
        c = 1
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                matrix[top][i] = c
                c += 1
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = c
                c += 1
            right -= 1

            # Traverse from right to left along the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = c
                    c += 1
                bottom -= 1

            # Traverse from bottom to top along the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = c
                    c += 1
                left += 1

        return matrix
