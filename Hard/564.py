class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        def palindrome(a):  # to use in the 'else' below
            b = int(a + a[::-1]) if len(n) % 2 == 0 else int(a + a[-2::-1])
            if str(b) == n:
                b = 0  # to check if palindrm is same as n
            return b

        if len(n) == 1:
            return str(int(n) - 1)
        elif all(i == "9" for i in n):
            return str(int(n) + 2)
        elif int(n) > 10 ** (len(n) - 1) - 1 and int(n) <= 10 ** (len(n) - 1) + 1:
            return str(10 ** (len(n) - 1) - 1)

        else:
            x = n[: -(len(n) // 2)]
            p1 = palindrome(x)
            y = str(int(x) + 1)
            p2 = palindrome(y)
            y = str(int(x) - 1)
            p3 = palindrome(y)

            # except when they're equal to zero, assume p2 > p1 > p3

            if abs(int(n) - p2) >= abs(int(n) - p1):
                if abs(int(n) - p1) >= abs(int(n) - p3):
                    return str(p3)
                else:
                    return str(p1)
            else:
                if abs(int(n) - p2) >= abs(int(n) - p3):
                    return str(p3)
                else:
                    return str(p2)
