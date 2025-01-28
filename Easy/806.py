class Solution(object):
    def numberOfLines(self, widths, s):
        a = 0
        b = 0
        for x in s:
            a = a + widths[ord(x) - 97]
            if a > 100:
                b = b + 1
                a = widths[ord(x) - 97]
        if a > 0:
            b = b + 1
        return [b, a]
