from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        longest = 0

        for i in range(1, n - 1):
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand left
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Expand right
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Calculate the length of the mountain subarray
                mountain_length = right - left + 1
                longest = max(longest, mountain_length)

        return longest if longest >= 3 else 0
