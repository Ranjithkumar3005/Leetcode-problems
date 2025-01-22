from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        max_length = 0

        for i in range(len(nums)):  # Iterate through all indices
            if i not in visited:  # Only start a new nest if not visited
                current_length = 0
                ch = i  # Start at index i
                while ch not in visited:
                    visited.add(ch)  # Mark this index as visited
                    ch = nums[ch]  # Move to the next index
                    current_length += 1

                max_length = max(max_length, current_length)
        return max_length
