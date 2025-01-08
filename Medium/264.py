import heapq


class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tot = n
        if n <= 0:
            return False
        while tot != 1:
            if tot % 2 == 0:
                tot = tot / 2
            elif tot % 3 == 0:
                tot = tot / 3
            elif tot % 5 == 0:
                tot = tot / 5
            else:
                return False
        return True


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ugly_numbers = []
        heapq.heappush(ugly_numbers, 1)
        res = []
        while len(res) < n:
            currSmallest = heapq.heappop(ugly_numbers)
            two = currSmallest * 2
            three = currSmallest * 3
            five = currSmallest * 5
            if two not in ugly_numbers:
                heapq.heappush(ugly_numbers, two)
            if three not in ugly_numbers:
                heapq.heappush(ugly_numbers, three)
            if five not in ugly_numbers:
                heapq.heappush(ugly_numbers, five)
            res.append(currSmallest)
        return res[len(res) - 1]
