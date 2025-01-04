class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell to the minimum path sum
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )

        # The top of the triangle now contains the minimum path sum
        return triangle[0][0]
