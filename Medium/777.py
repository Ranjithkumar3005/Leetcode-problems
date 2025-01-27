class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        i, j = 0, 0
        while i < len(start) and j < len(end):
            while i < len(start) and start[i] == "X":
                i += 1
            while j < len(end) and end[j] == "X":
                j += 1

            if i == len(start) and j == len(end):
                return True

            if i == len(start) or j == len(end):
                return False

            if start[i] != end[j]:
                return False

            if start[i] == "L" and i < j:  # 'L' cannot move right
                return False
            if start[i] == "R" and i > j:  # 'R' cannot move left
                return False

            i += 1
            j += 1

        while i < len(start):
            if start[i] != "X":
                return False
            i += 1
        while j < len(end):
            if end[j] != "X":
                return False
            j += 1

        return True
