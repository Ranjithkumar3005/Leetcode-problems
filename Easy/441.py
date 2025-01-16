class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            c += 1
        return c


class Solution(object):
    def arrangeCoins(self, n):
        if n <= 3:
            return n if n == 1 else n - 1
        l, r = 1, (n // 2) + 1
        while l < r:
            m = (l + r) // 2
            if (m * (m + 1)) // 2 <= n:
                l = m + 1
            else:
                r = m
        return l - 1
