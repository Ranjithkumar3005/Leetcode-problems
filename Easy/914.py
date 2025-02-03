import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1
        g = list(count.values())[0]
        for c in count.values():
            g = math.gcd(g, c)
        return g > 1
