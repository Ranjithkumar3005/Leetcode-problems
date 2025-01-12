class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for i in magazine:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in ransomNote:
            if i not in h:
                return False
            h[i] -= 1
            if h[i] == 0:
                del h[i]
        return True
