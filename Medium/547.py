from collections import deque


class Solution(object):
    def bfs(self, idx, visit, arr):
        visit.add(idx)
        q = deque()
        q.append(idx)
        while q:
            node = q.popleft()
            for i in range(len(arr[node])):
                if arr[node][i] == 1 and i not in visit:
                    visit.add(i)
                    q.append(i)

    def findCircleNum(self, arr):
        visit = set()
        count = 0
        for i in range(len(arr)):
            if i not in visit:
                self.bfs(i, visit, arr)
                count += 1
        return count
