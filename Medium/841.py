from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        check = set()
        que = deque([0])
        while que:
            val = que.popleft()
            if val not in check:
                check.add(val)
                for i in rooms[val]:
                    que.append(i)
        return len(check) == n
