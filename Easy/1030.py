class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = []
        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                cells.append((r, c, distance))
        cells.sort(key=lambda x: x[2])
        return [(r, c) for r, c, _ in cells]
