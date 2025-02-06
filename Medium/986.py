class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        intersections = []

        while i < len(firstList) and j < len(secondList):
            # Find the intersection between firstList[i] and secondList[j]
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If the intervals intersect
            if start <= end:
                intersections.append([start, end])

            # Move to the next interval in the list that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
