class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)
        sides = [0] * k

        def backtrack(i):
            if i == len(nums):
                return all(side == target for side in sides)

            for j in range(k):
                if sides[j] + nums[i] <= target:
                    sides[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= nums[i]

                if sides[j] == 0:
                    break

            return False

        return backtrack(0)
