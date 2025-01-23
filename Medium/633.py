from cmath import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        divisor = 2
        while divisor * divisor <= c:
            if c % divisor == 0:
                exponentCount = 0
                while c % divisor == 0:
                    exponentCount += 1
                    c //= divisor
                if divisor % 4 == 3 and exponentCount % 2 != 0:
                    return False
            divisor += 1
        return c % 4 != 3


class Solution:
    def judgeSquareSum(self, c):
        if c <= 2:
            return True

        while c % 2 == 0:
            c /= 2

        if c % 4 == 3:
            return False

        for i in range(3, int(sqrt(c)) + 1, 4):
            count = 0
            while c % i == 0:
                count += 1
                c /= i

            if count % 2 == 1:
                return False

        return c % 4 != 3
