class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        for i in range(0, len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
        for i in range(0, len(s)):
            if h[s[i]] == 1:
                return i
        return -1
