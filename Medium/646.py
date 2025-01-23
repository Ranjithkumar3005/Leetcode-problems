from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        longest_chain = 0
        current_end = float("-inf")  # Start with negative infinity

        for left, right in pairs:
            if left > current_end:
                longest_chain += 1  # Increment the chain length
                current_end = right

        return longest_chain
