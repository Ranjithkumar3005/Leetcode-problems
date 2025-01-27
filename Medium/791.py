class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        str1 = ""

        for i in order:
            if i in s:
                c = s.count(i)
                str1 += i * c

        for i in s:
            if i not in order:
                str1 += i
        return str1
