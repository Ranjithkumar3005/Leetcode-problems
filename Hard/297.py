from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"

        str1 = ""
        que = deque([root])

        while que:
            val = que.popleft()
            if val:
                str1 += str(val.val) + ","
                que.append(val.left)
                que.append(val.right)
            else:
                str1 += "None,"

        return str1

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_lists = data.split(",")
        if tree_lists[0] == "None":  # Handle empty tree case
            return None

        root = TreeNode(int(tree_lists.pop(0)))
        que = deque([root])

        while que:
            node = que.popleft()

            left_val = tree_lists.pop(0)
            if left_val != "None":
                node.left = TreeNode(int(left_val))
                que.append(node.left)

            if tree_lists:
                right_val = tree_lists.pop(0)
                if right_val != "None":
                    node.right = TreeNode(int(right_val))
                    que.append(node.right)

        return root


# Example usage:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
