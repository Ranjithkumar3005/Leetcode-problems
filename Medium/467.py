class Solution(object):
    def findSubstringInWraproundString(self, s):
        if not s:
            return 0

        max_len = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}

        current_len = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                current_len += 1
            else:
                current_len = 1
            max_len[s[i]] = max(max_len[s[i]], current_len)

        return sum(max_len.values())
