class Solution(object):
    def findContentChildren(self, g, s):
        res = 0
        i, j = 0, 0
        x, y = sorted(s), sorted(g)
        n, m = len(g), len(s)
        while i < n and j < m:
            if x[j] >= y[i]:
                res = res + 1
                i = i + 1
            j = j + 1
        return res
