class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posd = set()
        negd= set()
        res = []
        board = [["."]*n for i in range(n)]

        def back(r):
            if r ==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c)in posd or (r-c) in negd:
                    continue
                col.add(c)
                posd.add(r+c)
                negd.add(r-c)
                board[r][c] = "Q"
                back(r+1)
                col.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
                board[r][c] = "."
        back(0)
        return res