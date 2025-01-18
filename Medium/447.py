class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        tot = 0
        for i in points:
            h = {}
            for j in points:
                if i != j:
                    sum = (j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2
                    if sum in h:
                        h[sum] += 1
                    else:
                        h[sum] = 1

            for count in h.values():
                if count > 1:
                    tot += count * (count - 1)
        return tot
