class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        def isPrime(n):
            count = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    count += 1
            if count == 2:
                return True
            else:
                return False

        c = 0
        for i in range(left, right + 1):
            val = str(bin(i))
            co = val.count("1")
            if isPrime(co):
                c += 1
        return c
