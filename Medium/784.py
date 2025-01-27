from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.dum = []

        def backtrack(sub, index):
            if index == len(s):
                self.dum.append(sub)
                return
            if s[index].isdigit():
                backtrack(sub + s[index], index + 1)
            else:
                backtrack(sub + s[index].lower(), index + 1)
                backtrack(sub + s[index].upper(), index + 1)

        backtrack("", 0)
        return self.dum
