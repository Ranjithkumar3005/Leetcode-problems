from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithCapacity(capacity):
            total_weight = 0
            days_needed = 1
            for weight in weights:
                if total_weight + weight > capacity:
                    days_needed += 1
                    total_weight = 0
                total_weight += weight
                if days_needed > days:
                    return False
            return True

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShipWithCapacity(mid):
                right = mid
            else:
                left = mid + 1

        return left
