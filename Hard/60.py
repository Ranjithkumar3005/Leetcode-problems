import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        perm = ["0"] * len(nums)
        i = 0
        count = 0
        while i < len(perm):
            for j in range(n):
                if str(nums[j]) not in perm:
                    c = count + math.factorial(n - (i + 1))
                    if c < k:
                        count = c
                    else:
                        perm[i] = str(nums[j])
                        i += 1
                        break

        return "".join(perm)
