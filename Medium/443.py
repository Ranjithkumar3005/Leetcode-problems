from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        j = 0
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                c += 1
            else:
                chars[j] = chars[i]
                j += 1
                if c > 1:
                    for digit in str(c):
                        chars[j] = digit
                        j += 1
                c = 1
        chars[j] = chars[-1]
        j += 1
        if c > 1:
            for digit in str(c):
                chars[j] = digit
                j += 1
        return j
