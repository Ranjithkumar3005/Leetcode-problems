class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs[0])
        m = len(strs[-1])
        k = min(m, n)
        s = ""

        for i in range(k):
            if strs[0][i] == strs[-1][i]:
                s += strs[0][i]
            else:
                return s
        return s
