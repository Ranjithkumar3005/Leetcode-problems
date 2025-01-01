class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sort the intervals based on start
        intervals.sort(key=lambda x: x[0])

        output = []
        output.append(intervals[0])

        for i in intervals[1:]:
            if i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
        return output
