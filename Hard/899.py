class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = []
        if k == 1:
            # If k is 1, you can only rotate the string
            return min(s[i:] + s[:i] for i in range(len(s)))

        return "".join(sorted(s))
