from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = {}
        for i in wall:
            t = 0
            for j in range(0, len(i) - 1):
                t += i[j]
                if t in h:
                    h[t] += 1
                else:
                    h[t] = 1
        if not h:
            return len(wall)
        max1 = max(h.values())
        return len(wall) - max1
