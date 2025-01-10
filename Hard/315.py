from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pairs = [(num, i) for i, num in enumerate(nums)]
        counts = [0] * len(nums)

        def merge_sort(start, end):
            if end - start <= 1:
                return pairs[start:end]

            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = []
            i = 0  # Pointer for the left half
            j = 0  # Pointer for the right half

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    merged.append(left[i])
                    counts[left[i][1]] += j  # Add all elements from right seen so far
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                counts[left[i][1]] += j
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(0, len(nums))

        return counts
