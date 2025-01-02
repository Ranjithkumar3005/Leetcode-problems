class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty tree
        dp[1] = 1  # Base case: single-node tree

        # Fill the DP array using the recursive relation
        for nodes in range(2, n + 1):  # For each number of nodes
            for root in range(1, nodes + 1):  # For each root position
                left = root - 1  # Nodes in the left subtree
                right = nodes - root  # Nodes in the right subtree
                dp[nodes] += dp[left] * dp[right]

        return dp[n]
