# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            len1 = len(que)
            curr = []
            for _ in range(len1):
                pl = que.popleft()
                curr.append(pl.val)
                if pl.left:
                    que.append(pl.left)
                if pl.right:
                    que.append(pl.right)
            res.append(curr)
        return res[::-1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([root])
        result = deque()

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.appendleft(level)

        return list(result)
