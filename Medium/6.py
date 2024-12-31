class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1:
            return s
        n = len(s)
        arr = ["" for _ in range(numRows)]
        down = True
        row = 0
        for i in range(n):
            arr[row] += s[i]
            if row == 0:
                down = True
            if row == numRows - 1:
                down = False
            if down:
                row += 1
            else:
                row -= 1
        return "".join(arr)
