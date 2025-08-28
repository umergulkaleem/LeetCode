class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        diagonals = defaultdict(list)
        
        # Collect elements of each diagonal
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
        
        # Sort each diagonal depending on its region
        for key in diagonals:
            if key >= 0:  # bottom-left including main diagonal
                diagonals[key].sort(reverse=True)   # non-increasing
            else:         # top-right
                diagonals[key].sort()              # non-decreasing
        
        # Place sorted values back
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
        
        return grid
        