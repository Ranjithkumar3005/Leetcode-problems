class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        char_store = {}
        store_char = {}
        while i < n:
            if t[i] in char_store:
                if char_store[t[i]] != s[i]:
                    return False
            elif s[i] in store_char:
                if store_char[s[i]] != t[i]:
                    return False
            else:
                char_store[t[i]] = s[i]
                store_char[s[i]] = t[i]
            i += 1
        return True
