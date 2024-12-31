from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(l, r, curr):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if l < n:
                backtrack(l + 1, r, curr + "(")
            if r < l:
                backtrack(l, r + 1, curr + ")")

        backtrack(0, 0, "")
        return res
