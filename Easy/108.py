class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def helper(left, right):
            if left > right:
                return None

            # Choose the middle element as the root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)
