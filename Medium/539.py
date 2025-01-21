from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time points to minutes since the start of the day
        minutes = []
        for time in timePoints:
            hours, mins = map(int, time.split(":"))
            total_minutes = hours * 60 + mins
            minutes.append(total_minutes)

        # Sort the minutes to find the minimum difference easily
        minutes.sort()

        # Initialize the minimum difference with the difference between the first and last time point
        min_diff = 24 * 60  # Maximum possible difference (one day)

        # Calculate the difference between consecutive time points
        for i in range(len(minutes) - 1):
            diff = minutes[i + 1] - minutes[i]
            min_diff = min(min_diff, diff)

        # Calculate the circular difference between the last and first time point
        circular_diff = 24 * 60 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, circular_diff)

        return min_diff
