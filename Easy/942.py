from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        res = []
        perm = [j for j in range(start, end + 1)]
        for i in s:
            if i == "I":
                res.append(perm[start])
                start += 1
            elif i == "D":
                res.append(perm[end])
                end -= 1

        # print(res,start,end)
        res.append(perm[start])
        return res
        # if s[-1]=="D":
        #     res.append()
