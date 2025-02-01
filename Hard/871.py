import heapq


class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float("inf")))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1
