class Solution(object):
    def eventualSafeNodes(self, graph):
        from collections import deque, defaultdict

        n = len(graph)
        reverse_graph = defaultdict(list)
        outdegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            outdegree[u] = len(graph[u])

        queue = deque([i for i in range(n) if outdegree[i] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                outdegree[neighbor] -= 1  # Decrease the outdegree
                if outdegree[neighbor] == 0:  # If outdegree becomes 0, it's safe
                    queue.append(neighbor)

        return sorted(safe_nodes)
