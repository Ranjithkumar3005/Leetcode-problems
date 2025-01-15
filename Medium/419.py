class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0
        
        rows = len(board)
        cols = len(board[0])
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    # Check if it's the first cell of a battleship
                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        count += 1
                        
        return count



        # if not board:
        #     return 0 
        
        # row = len(board)
        # col = len(board[0])
        # num_ship = 0
        
        # def dfs(r, c):
        #     if r < 0 or r >= row or c <0 or c >= col or board[r][c] == ".":
        #         return 
        #     board[r][c] = "."
        #     dfs(r-1, c)
        #     dfs(r, c-1)
        #     dfs(r+1, c)
        #     dfs(r, c+1)

        # for r in range(row):
        #     for c in range(col):            
        #         if board[r][c] == 'X':
        #             num_ship+=1
        #             dfs(r, c)
                    
            
        # return num_ship  