from typing import List
from collections import defaultdict


class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        items = sorted(zip(values, labels), key=lambda x: -x[0])

        label_count = defaultdict(int)
        selected_sum = 0
        selected_count = 0

        for value, label in items:
            if selected_count == numWanted:
                break

            if label_count[label] < useLimit:
                selected_sum += value
                selected_count += 1
                label_count[label] += 1

        return selected_sum
