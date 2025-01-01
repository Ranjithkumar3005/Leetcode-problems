from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        output = []
        output.append(intervals[0])

        for i in intervals[1:]:
            if i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        return output
