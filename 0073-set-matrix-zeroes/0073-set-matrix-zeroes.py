class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        number = []
        for i in range(len(matrix)):
            has_zero =False
            print(i,"at i")
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    number.append(j)
                    print(number)
                    has_zero = True
                    # print(matrix,"in j")
                    # print(matrix,"in j")
                    print(len(matrix[i]))
            if has_zero:
                matrix[i] = len(matrix[i])*[0]
                print(matrix,"in j")
                    
        print(number,"numbers")
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for k in number:
                    if j == k:
                        matrix[i][j]=0
        print(matrix)

        