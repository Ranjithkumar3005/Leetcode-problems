class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(0, len(s)):
            val = s[i + 1 :] + s[: i + 1]
            if val == goal:
                return True
        return False
