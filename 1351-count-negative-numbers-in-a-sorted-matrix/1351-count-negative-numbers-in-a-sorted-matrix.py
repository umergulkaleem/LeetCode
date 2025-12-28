class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        pointer =len(grid[0])-1
        for i in range(len(grid)):
            # count +=count
            # print(pointer,"pointer")
            while pointer>=0 and grid[i][pointer]<0:
                pointer-=1
            val = (len(grid[i])-1)-pointer
            # print(val,"to add")
            count +=val
            # print(grid[i])
            # print(count)
        return count
        

        