class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x

            res = helper(x, n >> 1)
            res *= res
            return res * x if n & 1 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
