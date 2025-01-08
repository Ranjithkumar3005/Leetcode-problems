class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        st = str(num)
        tot = 0

        while len(st) != 1:
            for i in range(0, len(st)):
                tot += int(st[i])
            st = str(tot)
            tot = 0
        return int(st)
