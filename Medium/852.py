from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        st, end = 0, len(arr) - 1
        while st < end:
            mid = st + (end - st) // 2
            if arr[mid] > arr[mid + 1]:
                end = mid
            else:
                st = mid + 1

        return st
