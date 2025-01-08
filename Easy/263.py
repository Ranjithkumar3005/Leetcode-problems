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
