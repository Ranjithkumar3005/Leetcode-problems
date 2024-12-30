class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max1 = 0
        left = 0
        h = {}
        for i in range(0, len(s)):
            if s[i] not in h:
                h[s[i]] = 0
                max1 = max(max1, len(h))
            else:
                while s[i] in h:
                    del h[s[left]]
                    left += 1
                h[s[i]] = 0
                max1 = max(max1, len(h))
        return max1
