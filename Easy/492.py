class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for l in range(int(area**0.5), 0, -1):
            if area % l == 0:
                return [area // l, l]
