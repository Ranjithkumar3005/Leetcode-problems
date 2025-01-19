class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_intervals = sorted(points, key=lambda x: x[1])
        counter = 1
        end = sorted_intervals[0][1]
        for p in sorted_intervals[1:]:
            if p[0] > end:
                counter += 1
                end = p[1]
        return counter
