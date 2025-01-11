import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
        for key in adj:
            adj[key].sort()

        itinerary = []

        def dfs(at):
            while adj[at]:
                nextDest = adj[at].pop(0)
                dfs(nextDest)
            itinerary.append(at)

        dfs("JFK")

        return itinerary[::-1]
