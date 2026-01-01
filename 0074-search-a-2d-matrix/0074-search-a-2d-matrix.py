class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix),len(matrix[0])
        top,bot = 0,ROW-1
        while top<=bot:
            row = (top+bot)//2
            if target>matrix[row][-1]:
                top =row+1
            elif target<matrix[row][0]:
                bot = row-1
            else:
                break
        
        if not (top<=bot):
            return False
        row = (top+bot)//2
        
        a,b = 0,COL-1
        while a<=b:
            mid = (a+b)//2
            if target>matrix[row][mid]:
                a = mid+1
            elif target<matrix[row][mid]:
                b = mid-1
            else:
                return True
        return False
        