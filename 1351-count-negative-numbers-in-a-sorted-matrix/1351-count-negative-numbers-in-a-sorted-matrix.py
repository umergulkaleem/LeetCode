class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            print(i)
            for r in range(len(i)-1,-1,-1):
                if i[r] <0:
                    count+=1
                else:
                    continue
        return count

        