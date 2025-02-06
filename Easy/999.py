class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x, y = i, j
                    break

        ans = 0
        h = board[x]
        v = [board[i][y] for i in range(8)]
        lsts = [h[x:], h[x::-1], v[y:], v[y::-1]]
        for lst in lsts:
            for i in lst:
                if i == ".":
                    continue
                if i == "p":
                    ans += 1
                    print(lst)
                    break
                if i == "B":
                    break
        return ans
