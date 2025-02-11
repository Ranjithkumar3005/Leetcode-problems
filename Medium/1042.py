from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        h = {}
        for i in paths:
            if i[0] - 1 in h:
                h[i[0] - 1].append(i[1] - 1)
            else:
                h[i[0] - 1] = [i[1] - 1]

            if i[1] - 1 in h:
                h[i[1] - 1].append(i[0] - 1)
            else:
                h[i[1] - 1] = [i[0] - 1]

        ans = [0] * n
        for i in range(n):
            used_flowers = {ans[j] for j in h.get(i, []) if ans[j] != 0}
            for k in range(1, 5):
                if k not in used_flowers:
                    ans[i] = k
                    break

        return ans
