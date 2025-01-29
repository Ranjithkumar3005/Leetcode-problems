class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        c = 1
        ind = 0
        dum = []
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                c += 1
            else:
                if c >= 3:
                    dum.append([ind, i])
                ind = i + 1
                c = 1
        if c >= 3:
            dum.append([ind, len(s) - 1])
        return dum
