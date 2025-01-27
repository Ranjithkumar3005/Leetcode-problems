from collections import Counter
import math
from typing import List


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answer_count = Counter(answers)
        total_rabbits = 0
        for answer, count in answer_count.items():
            group_size = answer + 1
            groups = math.ceil(count / group_size)
            total_rabbits += groups * group_size

        return total_rabbits


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = {}
        count = 0

        for answer in answers:
            if answer == 0:
                count += 1
            elif answer not in counts or counts[answer] == 0:
                counts[answer] = 1
                count += answer + 1
            else:
                counts[answer] += 1
                if counts[answer] > answer:
                    counts[answer] = 0

        return count
