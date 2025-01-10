import math


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        """if n == 1 or n == 0:
            return n
        if n == 2:
            return 1

        a = [1 for _ in range(n)]
      
        for r in range(1, n):
            if a[r] == 1:
                a[r] = 0
            else:
                a[r] = 1
        return sum(a)"""
        return int(math.sqrt(n))
