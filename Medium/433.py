from collections import deque


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        que = deque([(startGene, 0)])
        visited = set()  # To track visited genes

        while que:
            val, c = que.popleft()
            if val == endGene:
                return c
            for i in range(len(bank)):
                if bank[i] not in visited:  # Check if the gene is already visited
                    d = 0
                    for j in range(len(val)):
                        if bank[i][j] != val[j]:
                            d += 1
                    if d == 1:  # Valid mutation
                        que.append((bank[i], c + 1))
                        visited.add(bank[i])  # Mark the gene as visited
        return -1
