from typing import Counter, List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = []

        for row in matrix:
            pattern = tuple(row[0] ^ val for val in row)
            patterns.append(pattern)
        pattern_count = Counter(patterns)
        return max(pattern_count.values())
