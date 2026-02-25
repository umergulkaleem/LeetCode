class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS ,COLS = len(board),len(board[0])

        def dfs(r,c):
            if (r<0 or c<0 or r==ROWS or c == COLS or  
            board[r][c] !="O"):
                return
            board[r][c] ="T"
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        #convert the border O in to T
        for  r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="O" and (r in [0 ,ROWS-1] or c in [0,COLS-1]):
                    print(f"{r},row,{c} col")
                    dfs(r,c)

        #changing the middle not border O into x
        for  r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c] = "X"
        
        #changing the remaing T into O again that are not surronded
        for  r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="T":
                    board[r][c] ="O"