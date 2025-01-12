import random


class RandomizedSet(object):

    def __init__(self):
        self.h = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.h:
            self.h[val] = 1
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.h:
            self.h.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.h) == 0:
            return "null"
        return random.choice(list(self.h.keys()))
