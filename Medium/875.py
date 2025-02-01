import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # k must be between 1 and max(piles)

        while left < right:
            mid = (left + right) // 2  # Calculate the mid value
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours > h:
                left = mid + 1  # Increase k
            else:
                right = mid  # Try for a smaller k

        return left  # The minimum k found
