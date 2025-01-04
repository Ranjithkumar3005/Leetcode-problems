class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        dummy = ""
        for i in range(0, len(s)):
            val = ord(s[i])
            if (val > 47 and val < 58) or (val > 96 and val < 123):
                dummy += s[i]
        dummy1 = dummy[::-1]
        if dummy == dummy1:
            return True
        return False
