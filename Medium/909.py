from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr = []
        check = True
        n = len(board)

        for i in range(n - 1, -1, -1):
            if check:
                arr += board[i]
            else:
                arr += board[i][::-1]
            check = not check

        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            i, c = queue.popleft()

            if i == n * n - 1:
                return c

            for j in range(1, 7):
                xi = i + j
                if xi < n * n and xi not in visited:
                    if arr[xi] == -1:
                        queue.append((xi, c + 1))
                    else:
                        queue.append((arr[xi] - 1, c + 1))
                    visited.add(xi)

        return -1
