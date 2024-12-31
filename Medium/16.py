from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        output = float("inf")
        diff = float("inf")

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                current_diff = abs(current_sum - target)

                if current_diff < diff:
                    output = current_sum
                    diff = current_diff

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1

        return output
