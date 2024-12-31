class Solution(object):
    def maxArea(self, height):
        max_area = 0
        l = 0
        r = len(height) - 1
        highest = max(height)
        while l < r:
            current_area = 0
            if height[l] > height[r]:
                current_area = height[r] * (r - l)
            else:
                current_area = height[l] * (r - l)
            if current_area > max_area:
                max_area = current_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if max_area >= highest * (r - l):
                break
        return max_area
