import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)

        max_heap = [(-count, char) for char, count in freq_map.items()]
        heapq.heapify(max_heap)

        result = []
        prev_count, prev_char = 0, ""
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            prev_count, prev_char = count + 1, char  # Decrement the count

        rearranged_str = "".join(result)
        if len(rearranged_str) != len(s):
            return ""

        return rearranged_str
