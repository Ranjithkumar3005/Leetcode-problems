from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        # Shrink the window until it contains exactly k elements
        while right - left + 1 > k:
            # Compare the distance from x to arr[left] and arr[right]
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        # The subarray from left to right will have the k closest elements
        return arr[left : right + 1]
