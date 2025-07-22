class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # sum1 = 0
        # if len(mat) == 1:
        #     return mat[0][0]
        # sum1 +=mat[0][0]
        # sum1 +=mat[0][-1]
        # print(sum1,"innital")
        # for i in range(1,len(mat)-1):
        #     if len(mat) % 2==0:
        #         round1 = round(len(mat)/2)
        #         sum1+=mat[i][round1]
        #         sum1+=mat[i][round1-1]
        #         print(sum1,'in if')
        #     else:
        #         round1 = round(len(mat)/2)
        #         sum1+=mat[i][round1-1]
        #         print(sum1,"in else")
        # sum1 +=mat[-1][0]
        # sum1 +=mat[-1][-1]

        # return sum1
        # sum1 = 0
        # left =0 
        # right = -1
        # for i in range(len(mat)):
        #     if left ==right :
        #         sum1+=mat[i][left]
        #         print(sum1,"if")
        #     else:
        #         sum1+=mat[i][left]
        #         sum1+=mat[i][right]
        #         print(sum1,"in else")
        #     left+=1
        #     right-=1
        # return sum1

        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]            
            total += mat[i][n - 1 - i]    
        if n % 2 == 1:
            total -= mat[n//2][n//2]       
        return total

                
        