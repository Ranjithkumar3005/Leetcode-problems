from collections import deque


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start = "".join(str(cell) for row in board for cell in row)
        target = "123450"

        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        queue = deque([(start, start.index("0"), 0)])
        visited = {start}
        while queue:
            start, zero_pos, steps = queue.popleft()
            if start == target:
                return steps
            for neighbour in moves[zero_pos]:
                new = list(start)
                new[neighbour], new[zero_pos] = new[zero_pos], new[neighbour]
                stat = "".join(new)

                if stat not in visited:
                    visited.add(stat)
                    queue.append((stat, neighbour, steps + 1))
        return -1
