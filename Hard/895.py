from collections import defaultdict


class FreqStack(object):

    def __init__(self):
        self.freq_map = defaultdict(int)
        self.group_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq = self.freq_map[val] + 1
        self.freq_map[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        self.group_map[freq].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group_map[self.max_freq].pop()

        self.freq_map[val] -= 1

        if not self.group_map[self.max_freq]:
            del self.group_map[self.max_freq]
            self.max_freq -= 1

        return val


# Example usage:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
