from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i in range(0, len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            val1 = r.popleft()
            val2 = d.popleft()
            if val1 < val2:
                r.append(val1 + len(senate))
            else:
                d.append(val2 + len(senate))
        return "Radiant" if r else "Dire"
