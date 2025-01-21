import random


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.c = n_cols
        self.start = 0
        self.end = n_rows * n_cols - 1
        self.d = {}

    def flip(self):
        rand = random.randint(self.start, self.end)
        res = self.d.get(rand, rand)
        self.d[rand] = self.d.get(self.start, self.start)
        self.start += 1
        return divmod(res, self.c)

    def reset(self):
        self.d = {}
        self.start = 0
