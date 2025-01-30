from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildGraph(node, parent, graph):
    if not node:
        return
    if parent:
        graph[node.val].append(parent.val)
        graph[parent.val].append(node.val)
    buildGraph(node.left, node, graph)
    buildGraph(node.right, node, graph)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        buildGraph(root, None, graph)  # Convert tree to graph

        queue = deque([target.val])  # Use target.val instead of target
        visited = set([target.val])  # Use target.val instead of target
        distance = 0

        while queue:
            if distance == k:
                return list(queue)  # Return nodes at distance k

            for _ in range(len(queue)):
                val = queue.popleft()
                for nei in graph[val]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            distance += 1

        return []
