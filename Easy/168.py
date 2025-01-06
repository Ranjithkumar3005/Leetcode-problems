class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        result = []

        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            dum = chr(ord("A") + (int(rem)))
            result.append(dum)
            columnNumber //= 26
        result.reverse()

        return "".join(result)
