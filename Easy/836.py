class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Unpack all points
        r1_x1, r1_y1, r1_x2, r1_y2 = rec1
        r2_x1, r2_y1, r2_x2, r2_y2 = rec2

        # Return False if no overlap possible on X-Axis
        if r1_x2 <= r2_x1 or r2_x2 <= r1_x1:
            return False

        # Return False if no overlap possible on Y-Axis
        if r1_y2 <= r2_y1 or r2_y2 <= r1_y1:
            return False

        return True
