from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if (int(part) > 255) or (len(part) > 1 and part[0] == "0"):
                    break
                backtrack(end, parts + [part])

        backtrack(0, [])
        return res
