class Solution:
    def climbStairs(self, n: int) -> int:

        a=1
        b=2
        if n<=2:
            return n
        
        for i in range(3,n+1):
           
           b,a=a+b,b
        return b