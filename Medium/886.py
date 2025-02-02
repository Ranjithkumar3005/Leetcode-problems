from collections import deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for a, b in dislikes:
            adj_list[a - 1].append(b - 1)
            adj_list[b - 1].append(a - 1)

        colors = [0] * n

        for start in range(n):
            if colors[start] == 0:
                queue = deque([start])
                colors[start] = 1

                while queue:
                    vertex = queue.popleft()
                    for neighbor in adj_list[vertex]:
                        if colors[neighbor] == 0:
                            colors[neighbor] = 3 - colors[vertex]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[vertex]:
                            return False
        return True
