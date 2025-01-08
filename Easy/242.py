class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        h1 = {}
        for i in t:
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1
        for i in h:
            if i not in h1:
                return False
            if h[i] != h1[i]:
                return False
            del h1[i]
        if h1:
            return False
        return True
