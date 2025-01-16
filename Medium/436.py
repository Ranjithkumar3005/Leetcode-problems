class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Create a sorted list of intervals based on the start time
        sorted_intervals = sorted(
            (start, i) for i, (start, end) in enumerate(intervals)
        )
        result = []

        # Find the right interval for each interval
        for start, end in intervals:
            # Binary search to find the first interval with a start time >= end time
            low, high = 0, len(sorted_intervals)
            while low < high:
                mid = (low + high) // 2
                if sorted_intervals[mid][0] >= end:
                    high = mid
                else:
                    low = mid + 1

            # If low is within the bounds, get the index of the interval
            if low < len(sorted_intervals):
                result.append(sorted_intervals[low][1])
            else:
                result.append(-1)

        return result


# Example usage
s = Solution()
print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))  # Output: [-1, 0, 1]
