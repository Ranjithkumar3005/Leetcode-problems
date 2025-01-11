class Solution:
    def reverseVowels(self, s: str) -> str:
        dum = []
        for i in s:
            if i in "aeiouAEIOU":
                dum.append(i)
        dum = dum[::-1]
        c = 0
        str1 = ""
        for i in s:
            if i in "aeiouAEIOU":
                str1 += dum[c]
                c += 1
            else:
                str1 += i
        return str1
