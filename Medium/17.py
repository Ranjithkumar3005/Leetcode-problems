from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, curr):
            if i == len(digits):
                res.append(curr)
                return

            for k in keyboard[digits[i]]:
                backtrack(i + 1, curr + k)

        backtrack(0, "")
        return res
