from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        h = {}  # Dictionary to store remainders
        c = 0  # Count of valid pairs

        for t in time:
            val = t % 60
            complement = (60 - val) % 60  # Find the required remainder

            if complement in h:
                c += h[complement]

            h[val] = h.get(val, 0) + 1

        return c
