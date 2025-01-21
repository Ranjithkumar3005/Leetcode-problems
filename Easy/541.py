class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        str1 = ""
        check = True
        for i in range(0, len(s), k):
            if check:
                str1 += s[i : i + k][::-1]
                check = False
            else:
                str1 += s[i : i + k]
                check = True
        return str1
