from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dum = []
        for i in strs:
            dum.append((i, "".join(sorted(i))))
        dum = sorted(dum, key=lambda x: x[1])
        res = []
        ch = []

        for i in range(len(dum)):
            if i == 0 or dum[i][1] == dum[i - 1][1]:
                ch.append(dum[i][0])
            else:
                res.append(ch)
                ch = [dum[i][0]]
        res.append(ch)
        return res


# We can use Hashmap also
class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)

        return hashmap.values()
