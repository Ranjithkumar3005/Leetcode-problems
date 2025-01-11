from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subsequence(nums, size):
            stack = []
            to_remove = len(nums) - size
            for num in nums:
                while to_remove > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_remove -= 1
                stack.append(num)
            return stack[:size]

        def merge(seq1, seq2):
            result = []
            while seq1 or seq2:
                if seq1 > seq2:
                    result.append(seq1.pop(0))
                else:
                    result.append(seq2.pop(0))
            return result

        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            seq1 = get_max_subsequence(nums1, i)
            seq2 = get_max_subsequence(nums2, k - i)
            merged = merge(seq1, seq2)
            max_result = max(max_result, merged)

        return max_result
