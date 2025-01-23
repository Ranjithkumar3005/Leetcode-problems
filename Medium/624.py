class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_dist = 0
        min_val, min_index = arrays[0][0], 0
        max_val, max_index = arrays[0][-1], 0

        for i in range(1, len(arrays)):
            max_dist = max(
                max_dist, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])
            )

            if arrays[i][0] < min_val:
                min_val, min_index = arrays[i][0], i
            if arrays[i][-1] > max_val:
                max_val, max_index = arrays[i][-1], i

        return max_dist
