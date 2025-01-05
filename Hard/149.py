from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    slopes[(dy, dx)] += 1
            curr_max = max(slopes.values(), default=0) + duplicates
            max_points = max(max_points, curr_max)
        return max_points
