from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        val = len(s) // 2
        len1 = len(s) - 1
        for i in range(0, val):
            tem = s[i]
            s[i] = s[len1 - i]
            s[len1 - i] = tem
