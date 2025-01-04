from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [0] * (rowIndex + 1)
        result[0] = 1

        for row in range(1, rowIndex + 1):
            result[row] = 1

            for index in range(row - 1, 0, -1):
                result[index] += result[index - 1]

        return result
