from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        requestCount = 0
        ages.sort()
        n = len(ages)
        for i in range(n):
            leftmostValidIndex = -1
            start, end = 0, n - 1
            while start <= end:
                mid = start + (end - start) // 2
                if ages[mid] > 0.5 * ages[i] + 7:
                    leftmostValidIndex = mid
                    end = mid - 1
                else:
                    start = mid + 1
            if leftmostValidIndex < 0:
                continue

            rightmostValidIndex = -1
            start, end = 0, n - 1

            while start <= end:
                mid = start + (end - start) // 2

                if ages[mid] <= ages[i]:
                    rightmostValidIndex = mid
                    start = mid + 1
                else:
                    end = mid - 1
            count = rightmostValidIndex - leftmostValidIndex
            requestCount += count if count > 0 else 0

        return requestCount
