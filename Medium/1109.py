from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n

        for i in range(len(bookings)):
            if bookings[i][1] != n:
                diff[bookings[i][1]] -= bookings[i][2]
            diff[bookings[i][0] - 1] += bookings[i][2]

        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]

        return res
