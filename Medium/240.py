from json import loads
from sys import stdin
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    i = j = 0
    m, n = len(matrix), len(matrix[0])

    while i < m and matrix[i][j] <= target:
        if matrix[i][j] == target:
            return "true"
        i += 1

    i -= 1
    while i >= 0:
        j = 0
        while j < n and matrix[i][j] <= target:
            if matrix[i][j] == target:
                return "true"
            j += 1
        i -= 1

    return "false"


with open("user.out", "w") as f:
    inputs = list(map(loads, stdin))
    for matrix, target in zip(inputs[::2], inputs[1::2]):
        f.write(f"{searchMatrix(matrix, target)}\n")
exit(0)
