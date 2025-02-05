class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        dum = [0] * 8
        seen = {}

        while n > 0:
            state_tuple = tuple(cells)
            if state_tuple in seen:
                cycle_length = seen[state_tuple] - n
                n %= cycle_length
            seen[state_tuple] = n

            if n >= 1:
                for i in range(1, len(cells) - 1):
                    if cells[i - 1] == cells[i + 1]:
                        dum[i] = 1
                    else:
                        dum[i] = 0

                cells = dum[::]
                dum = [0] * 8
                n -= 1

        return cells
