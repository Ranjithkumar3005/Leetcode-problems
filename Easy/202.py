class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = str(n)
        h = {}
        tot = 0
        while st != "1":
            for i in range(0, len(st)):
                tot += int(st[i]) * int(st[i])
            if tot not in h:
                h[tot] = 1
            else:
                return False
            st = str(tot)
            tot = 0
        return True
