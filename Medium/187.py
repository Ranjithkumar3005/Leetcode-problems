class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        h = {}

        for i in range(0, len(s)):
            dum = s[i : i + 10]
            if dum in h:
                h[dum] += 1
            else:
                h[dum] = 0
        dum1 = []
        for i in h:
            if h[i] >= 1:
                dum1.append(i)
        return dum1
