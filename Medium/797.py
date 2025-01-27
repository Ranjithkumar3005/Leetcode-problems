class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph:
            return []

        res = []
        st = [(0, [0])]
        target = len(graph) - 1

        while st:
            curr, route = st.pop()
            if curr == target:
                res.append(route)
            for node in graph[curr]:
                st.append((node, route + [node]))

        return res
