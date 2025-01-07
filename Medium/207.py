from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        counter = 0

        if numCourses <= 0:
            return True

        # Initialize inDegree array and adjacency list
        inDegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        # Build the graph and update inDegree for each node
        for edge in prerequisites:
            parent, child = edge[1], edge[0]
            graph[parent].append(child)
            inDegree[child] += 1

        # Initialize the queue with courses having no prerequisites (inDegree = 0)
        sources = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                sources.append(i)

        # Process nodes with no prerequisites
        while sources:
            course = sources.popleft()  # dequeue
            counter += 1

            # Process all the children of the current course
            for child in graph[course]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)  # enqueue child if inDegree becomes 0

        # If we processed all courses, return true
        return counter == numCourses
