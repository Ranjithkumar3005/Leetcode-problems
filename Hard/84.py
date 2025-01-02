from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                h = heights[st.pop()]
                width = i if not st else i - st[-1] - 1
                max_area = max(max_area, h * width)
            st.append(i)

        while st:
            h = heights[st.pop()]
            width = n if not st else n - st[-1] - 1
            max_area = max(max_area, h * width)
        return max_area
