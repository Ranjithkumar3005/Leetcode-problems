from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []

        def backtrack(num, length):
            if length == n:
                result.append(num)
                return
            last_digit = num % 10
            next_digits = set([last_digit + k, last_digit - k])

            for next_digit in next_digits:
                if 0 <= next_digit <= 9:
                    backtrack(num * 10 + next_digit, length + 1)

        for i in range(1, 10):
            backtrack(i, 1)
        return result
