import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        dum = []
        for i in h:
            heapq.heappush(dum, (-h[i], i))
        str1 = ""
        while dum:
            c, cr = heapq.heappop(dum)
            str1 += cr * -c
        return str1
