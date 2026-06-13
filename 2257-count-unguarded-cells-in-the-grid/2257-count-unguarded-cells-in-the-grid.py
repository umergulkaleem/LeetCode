class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # grid = []
        # for i in range(m):
        #     grid.append(n*[0])
        # # guard is 1 and wall is 2
        # for r,c in walls:
        #     grid[r][c] = 2
        # # print( grid)
        # for gr, gc in guards:
    
        #     grid[gr][gc] = 1
            
        #     c = gc
        #     while c+1 < n and grid[gr][c+1] != 1 and grid[gr][c+1] != 2:
        #         c += 1
        #         grid[gr][c] = 3

        #     c = gc
        #     while c-1 >= 0 and grid[gr][c-1] != 1 and grid[gr][c-1] != 2:
        #         c -= 1
        #         grid[gr][c] = 3

        #     r = gr
        #     while r-1 >= 0 and grid[r-1][gc] != 1 and grid[r-1][gc] != 2:
        #         r -= 1
        #         grid[r][gc] = 3

        #     r = gr
        #     while r+1 < m and grid[r+1][gc] != 1 and grid[r+1][gc] != 2:
        #         r += 1
        #         grid[r][gc] = 3
                
        # res = 0
        # for row in grid:
        #     for cell in row:
        #         if cell == 0:
        #             res+=1
        # return res
        blocked = set()
        guarded = set()

        for r, c in walls:
            blocked.add((r, c))
        for r, c in guards:
            blocked.add((r, c))

        for gr, gc in guards:
            # right
            c = gc + 1
            while c < n and (gr, c) not in blocked:
                guarded.add((gr, c))
                c += 1
            # left
            c = gc - 1
            while c >= 0 and (gr, c) not in blocked:
                guarded.add((gr, c))
                c -= 1
            # up
            r = gr - 1
            while r >= 0 and (r, gc) not in blocked:
                guarded.add((r, gc))
                r -= 1
            # down
            r = gr + 1
            while r < m and (r, gc) not in blocked:
                guarded.add((r, gc))
                r += 1

        return m * n - len(blocked) - len(guarded)



        
        


        
        