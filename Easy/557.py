class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        dum = []
        for i in arr:
            dum.append(i[::-1])
        return " ".join(dum)
