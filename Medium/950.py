from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        idxs = deque([i for i in range(n)])
        ordered_deck = [0] * n
        print(deck)
        for i in range(n):
            idx = idxs.popleft()
            ordered_deck[idx] = deck[i]
            if idxs:
                idxs.append(idxs.popleft())
            print(idxs)

        return ordered_deck
