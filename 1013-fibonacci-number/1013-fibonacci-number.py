class Solution:
    def fib(self, n: int) -> int:

    # Recurision
        
        num =n
        if num == 0:
            return 0
        if num == 1:
            return  1
        ans = self.fib(num-1)+self.fib(num-2)
        return ans

    
    # constant space approach
        #Space Complexity good for

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return  1
        # curr = 0
        # prev = 1
        # for i in range(n):
        #     prev , curr = curr,prev+curr
        # return curr 

    #memoiazation
    #from top to bottom 
        # memo = {}
        # def helper(n):
        #     if n == 1:
        #         return 1
        #     if n == 0:
        #         return 0
        #     if n in memo :
        #         return memo[n]
        #     memo[n] = helper(n-1)+helper(n-2)
        #     return memo[n]
        # return helper(n)

    #tabulation

        # if n == 0:
        #     return 0

        # if n ==1:
        #     return 1
        # array = [-1]*(n+1) #array for -1

        # array[0] = 1
        # array[1] = 1

        # for i in range(2,n+1):
        #     print(i)
        #     array[i] = array[i - 1] + array[i - 2]
        # print(n,"n")
        # print(array)
        # return array[n-1]
    


            