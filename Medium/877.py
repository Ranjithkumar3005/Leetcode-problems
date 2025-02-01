from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a1 = 0
        b1 = 0
        check = True
        while piles:
            i = 0
            j = len(piles) - 1
            if check:
                check = False
                if piles[i] >= piles[j]:
                    a1 += piles[i]
                    piles.remove(piles[i])
                    i += 1
                else:
                    a1 += piles[j]
                    piles.pop()
                    j -= 1
            else:
                check = True
                if piles[i] <= piles[j]:
                    b1 += piles[i]
                    piles.remove(piles[i])
                    i += 1
                else:
                    b1 += piles[j]
                    piles.pop()
                    j -= 1
        return a1 >= b1
