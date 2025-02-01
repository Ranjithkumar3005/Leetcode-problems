class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        dummy = s1.split(" ") + s2.split(" ")
        h = {}
        for i in dummy:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        dummy1 = []
        for i in range(0, len(dummy)):
            if h[dummy[i]] == 1:
                dummy1.append(dummy[i])
        return dummy1
