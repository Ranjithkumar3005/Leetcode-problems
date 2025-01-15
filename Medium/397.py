class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                if n == 3 or (n & 2) == 0:
                    n -= 1
                else:
                    n += 1
            c += 1
        return c


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        numop = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                numop += 1
            elif n == 3:
                numop += 2
                break
            elif n % 4 == 3:
                n += 1
                numop += 1
            else:
                n -= 1
                numop += 1

        return numop
