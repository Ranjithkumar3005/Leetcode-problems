class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        stack = []

        # basket is used to store previous value
        basket = ""

        for p in S:
            if p == "(":
                stack.append(p)
            else:
                stack.pop()
            basket += p

            if not stack:
                res += basket[1:-1]
                basket = ""

        return res
