class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        sList = s.strip().split()

        return " ".join(sList[::-1])
