class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        str1 = ""
        is_negative = num < 0
        num = abs(num)
        while num > 0:
            val = num % 7
            str1 += str(val)
            num //= 7
        if is_negative:
            str1 += "-"
        return str1[::-1]
