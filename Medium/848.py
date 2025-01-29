from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = [""] * len(s)
        cumulative_shift = 0

        for index in range(len(s) - 1, -1, -1):
            cumulative_shift = cumulative_shift + shifts[index]
            result[index] = chr((ord(s[index]) - 97 + cumulative_shift) % 26 + 97)

        return "".join(result)
