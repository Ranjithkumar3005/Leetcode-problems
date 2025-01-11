class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1

        # Keep removing parts of size 3 while n is greater than 4
        res = 1
        while n > 4:

            n -= 3
            res *= 3
            # Keep multiplying 3 to res

        return n * res
