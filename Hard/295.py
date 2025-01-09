import heapq


class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max, -num)
        heapq.heappush(self.min, -heapq.heappop(self.max))
        if len(self.max) < len(self.min):
            heapq.heappush(self.max, -heapq.heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        else:
            return (-self.max[0] + self.min[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
