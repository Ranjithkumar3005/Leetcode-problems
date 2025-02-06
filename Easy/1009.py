class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1 = str(bin(n))[2:]
        str2 = ""
        for i in str1:
            if i == "1":
                str2 += "0"
            else:
                str2 += "1"
        val = int(str2, 2)
        return val
