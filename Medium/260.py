from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get XOR of the two unique numbers
        xor = 0
        for num in nums:
            xor ^= num

        # Step 2: Find the rightmost set bit in the XOR result
        diff_bit = xor & -xor

        # Step 3: Split numbers into two groups and XOR each group
        x, y = 0, 0
        for num in nums:
            if num & diff_bit:
                x ^= num
            else:
                y ^= num

        return [x, y]


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        result: list[int] = [0, 0]
        index = 0

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break
            if not found:
                result[index] = nums[i]
                index += 1
                if index == 2:
                    break

        return result
