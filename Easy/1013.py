from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        target = total_sum // 3
        current_sum = 0
        count = 0
        for num in arr:
            current_sum += num

            if current_sum == target:
                count += 1
                current_sum = 0

            if count == 3:
                return True

        return False
