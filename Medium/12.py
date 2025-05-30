class Solution:
    def intToRoman(self, num: int) -> str:
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        str1 = ""
        while num > 0:
            if num >= n[i]:
                str1 += s[i]
                num -= n[i]
            else:
                i += 1
        return str1
