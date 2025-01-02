from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
            if carry == 0:
                break
            c = 0
        if carry != 0:
            digits.insert(0, carry)
        return digits
