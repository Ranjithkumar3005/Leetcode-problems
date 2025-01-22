from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        leng = len(flowerbed)

        for i in range(leng):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == leng - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                count += 1
                i += 1
            if count >= n:
                return True

        return False
