class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        # Calculate the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)

        # Calculate the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)

        sum = area1 + area2
        cx1 = max(ax1, bx1)
        cx2 = min(ax2, bx2)
        cy1 = max(ay1, by1)
        cy2 = min(ay2, by2)

        overlap_area = max(0, cx2 - cx1) * max(0, cy2 - cy1)

        return sum - overlap_area
