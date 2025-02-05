from collections import defaultdict


class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        freqs = defaultdict(int)

        for ele in arr:
            freqs[ele] += 1

        for key in sorted(freqs.keys(), key=abs):
            if freqs[key] > freqs[key * 2]:
                return False
            freqs[key * 2] -= freqs[key]
            # if not freqs[key*2]:
            #     del freqs[key*2]
            # del freqs[key]
        return True
