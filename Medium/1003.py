class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 3:
            return False
        check = []
        for c in s:
            check.append(c)
            if len(check) >= 3:
                if (
                    check[-1] == "c" and check[-2] == "b" and check[-3] == "a"
                ):  # three last characters be a,b,c
                    check.pop()
                    check.pop()
                    check.pop()
        return not check
