from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        h = {}
        for i in paths:
            arr = i.split(" ")
            path = arr[0]
            for j in range(1, len(arr)):
                inx = arr[j].index("(")
                val = arr[j][inx:]
                tot = path + "/" + arr[j][:inx]
                if val not in h:
                    h[val] = [tot]
                else:
                    h[val].append(tot)
        dum2 = []
        for i in h:
            if len(h[i]) > 1:
                dum2.append(h[i])
        return dum2
