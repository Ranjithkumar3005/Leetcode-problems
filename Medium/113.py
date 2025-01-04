# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        que = deque([(root, root.val, [root.val])])
        res = []
        while que:
            node, current_sum, arr = que.popleft()

            if not node.left and not node.right and current_sum == targetSum:
                res.append(arr)

            if node.left:
                que.append(
                    (node.left, current_sum + node.left.val, arr + [node.left.val])
                )

            if node.right:
                que.append(
                    (node.right, current_sum + node.right.val, arr + [node.right.val])
                )

        return res
