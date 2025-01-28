class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Step 1: Sort the array
        arr.sort()
        dp = {}
        total_trees = 0

        # Step 2: Iterate through each number and calculate ways to form it
        for num in arr:
            dp[num] = 1  # Each number can be a tree itself
            for factor in arr:
                if factor >= num:  # Stop if factor exceeds num
                    break
                if num % factor == 0:  # If factor is a factor of num
                    other_factor = num // factor
                    if other_factor in dp:  # Check if the other factor is present
                        dp[num] += dp[factor] * dp[other_factor]

        # Step 3: Sum all the possible trees
        total_trees = sum(dp.values()) % (10**9 + 7)
        return total_trees
