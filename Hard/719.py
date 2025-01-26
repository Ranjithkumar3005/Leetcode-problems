from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def countPairs(mid):
            count = 0
            left = 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
