class Solution(object):
    def isPowerOfFour(self, n):
        def isPower(n):
            if n == 1:
                return True
            if n <= 0 or n % 4 != 0:
                return False
            return isPower(n // 4)

        return isPower(n)
