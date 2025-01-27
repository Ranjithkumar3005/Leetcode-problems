import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for nei, wei in graph[node]:
                new_time = time + wei
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))
        max_time = max(dist.values())
        return max_time if max_time != float("inf") else -1
