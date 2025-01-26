class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        len1 = len(b) // len(a)
        c = 1

        while c <= len1 + 2:
            if b in a * c:
                return c
            else:
                c += 1
        return -1
