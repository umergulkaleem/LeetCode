class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M = len(grid)
        N = len(grid[0])

        def postoval(r,c):
            return r*N+c
        def valtopos(v):
            return [v // N , v% N]
        res = [[0]*N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (postoval(r,c)+k) % (M*N)
                newr,newc = valtopos(newVal)
                res[newr][newc] = grid[r][c]
        return res        