class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1 = str(bin(n))[2:]
        c = 0
        max1 = 0
        for i in range(1, len(str1)):
            if str1[i] == "1":
                max1 = max(max1, c + 1)
                c = 0
            else:
                c += 1
        return max1
