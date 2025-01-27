from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        queue = deque([(src, 0)])
        distance = [float("inf")] * n
        distance[src] = 0

        adjList = defaultdict(list)
        for s, d, price in flights:
            adjList[s].append((d, price))

        while queue and k >= 0:
            for _ in range(len(queue)):
                node, price = queue.popleft()
                for neighbor, neighborPrice in adjList[node]:
                    if distance[neighbor] <= price + neighborPrice:
                        continue

                    queue.append((neighbor, price + neighborPrice))
                    distance[neighbor] = price + neighborPrice
            k -= 1

        return -1 if distance[dst] == float("inf") else distance[dst]
