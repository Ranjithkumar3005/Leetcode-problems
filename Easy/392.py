class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        sub_len = len(s)
        for i in t:
            if j < sub_len and i == s[j]:
                j += 1
            elif j == sub_len:
                return True
        return j == sub_len
