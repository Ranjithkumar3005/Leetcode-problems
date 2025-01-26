from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        ori_col = image[sr][sc]
        if ori_col == color:
            return image
        que = deque([(sr, sc)])
        while que:
            r, c = que.popleft()
            image[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == ori_col:
                    que.append((nr, nc))
                    image[nr][nc] = color

        return image
