from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        chunks = 0

        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])

            # If the maximum element up to index i is i, we can make a chunk
            if max_so_far == i:
                chunks += 1

        return chunks
