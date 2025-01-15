from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1
            queue = deque([(start, 1.0)])
            visited = set()
            while queue:
                node, product = queue.popleft()
                if node == end:
                    return product
                visited.add(node)
                for nei, wei in graph[node].items():
                    if nei not in visited:
                        queue.append((nei, product * wei))
            return -1

        res = []
        for C, D in queries:
            res.append(bfs(C, D))
        return res
