import math


class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            limit = int(math.sqrt(num)) + 1
            for i in range(3, limit, 2):
                if num % i == 0:
                    return False
            return True

        if 8 <= n <= 11:
            return 11

        while True:
            val = str(n)
            if val == val[::-1]:
                if isPrime(n):
                    return n
            n += 1

            if 10**7 < n < 10**8:
                n = 10**8
