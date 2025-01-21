class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        max1 = 0
        dum = 0
        for i in timeSeries:
            val = i + duration
            if max1 < i:
                dum += duration
            else:
                tot = max1 - i
                dum += duration - tot
            max1 = val
        return dum
