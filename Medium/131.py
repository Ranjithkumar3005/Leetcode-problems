from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispali(sub):
            return sub == sub[::-1]

        def dfs(start, path, res):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if ispali(substring):
                    # If the substring is a palindrome, add it to the path and continue to find further partitions
                    path.append(substring)
                    dfs(i + 1, path, res)  # Recurse with updated path
                    path.pop()  # Backtrack

        res = []
        dfs(0, [], res)
        return res
