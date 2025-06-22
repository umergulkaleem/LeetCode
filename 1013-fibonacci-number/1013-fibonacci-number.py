class Solution:
    def fib(self, n: int) -> int:

        #Recurision
        
        # num =n
        # if num == 0:
        #     return 0
        # if num == 1:
        #     return  1
        # ans = self.fib(num-1)+self.fib(num-2)
        # return ans


        #Space Complexity 
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return  1
        # curr = 0
        # prev = 1
        # for i in range(n):
        #     prev , curr = curr,prev+curr
        # return curr 
        memo = {}
        def helper(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            if n in memo :
                return memo[n]
            memo[n] = helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)
            